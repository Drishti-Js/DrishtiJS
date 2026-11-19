"""Verify release hashes and exercise the actual portable framework binaries."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import tempfile
import zipfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--manifest', default='releases/latest.json')
parser.add_argument('--platform', choices=('macos', 'windows', 'linux'))
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / args.manifest).read_text())
version = manifest['version']
assert re.fullmatch(r'[0-9]+\.[0-9]\.[0-9]', version), 'Invalid release version'
directory = (root / manifest['asset_directory']).resolve()
assert directory.is_relative_to(root)
assets = manifest['assets']
assert assets and len({a['filename'] for a in assets}) == len(assets)
for asset in assets:
    name = asset['filename']
    assert Path(name).name == name and '\\' not in name
    path = directory / name
    assert path.stat().st_size == asset['size_bytes'], name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset['sha256'], name
print(f'Verified {len(assets)} release artifact checksums for {version}', flush=True)
if not args.platform:
    raise SystemExit(0)
asset, = [a for a in assets if a['platform'] == args.platform and a['kind'] == 'portable']

def run(*argv, cwd=None):
    result = subprocess.run([str(v) for v in argv], cwd=cwd, capture_output=True,
                            text=True, timeout=120)
    assert result.returncode == 0, f'{argv}: {result.stdout}\n{result.stderr}'
    return result.stdout + result.stderr

with tempfile.TemporaryDirectory(prefix='drishti-release-') as temporary:
    stage = Path(temporary).resolve() / 'path with spaces'
    stage.mkdir()
    archive = directory / asset['filename']
    if archive.suffix == '.zip':
        with zipfile.ZipFile(archive) as bundle:
            assert all((stage / x.filename).resolve().is_relative_to(stage) for x in bundle.infolist())
            bundle.extractall(stage)
    else:
        with tarfile.open(archive) as bundle:
            bundle.extractall(stage, filter='data')
    folders = [p for p in stage.iterdir() if p.is_dir()]
    assert len(folders) == 1
    bin_dir = folders[0] / 'bin'
    extension = '.exe' if args.platform == 'windows' else ''
    cli = bin_dir / ('drish' + extension)
    runtime = bin_dir / ('drishti_runtime' + extension)
    assert run(cli, '--version').strip() == f'drish version {version}'
    assert 'Drishti CLI' in run(cli, 'help')
    for mode, suffix in (('javascript', 'js'), ('typescript', 'ts'), ('tsx', 'tsx')):
        name = 'Verify' + mode.title()
        run(cli, 'create', 'app', name, '--' + mode, cwd=stage)
        assert (stage / name / 'app' / ('main.' + suffix)).is_file()
        assert 'Validated Drishti app entry' in run(cli, 'node', 'build', '--app', stage / name, cwd=stage)
        package = json.loads((stage / name / 'package.json').read_text())
        assert 'drishtijs' in package['dependencies']
    script = stage / 'runtime-smoke.js'
    script.write_text('const result = 6 * 7; if (result !== 42) throw new Error("incorrect runtime result"); console.log("runtime smoke passed");\n')
    assert 'runtime smoke passed' in run(runtime, script, cwd=stage)
    modules = stage / 'nested-modules'
    (modules / 'lib').mkdir(parents=True)
    (modules / 'value.js').write_text('export const value = 42;\n')
    (modules / 'lib/dependency.js').write_text('import { value } from "../value.js"; export const result = value;\n')
    entry = modules / 'main.js'
    entry.write_text('import { result } from "./lib/dependency.js"; if (result !== 42) throw new Error("nested import failed"); console.log("nested imports passed");\n')
    assert 'nested imports passed' in run(runtime, entry, cwd=stage)
    assert 'nested imports passed' in run(cli, 'test', entry, cwd=stage)
    print(f'{args.platform}: native version/help, JavaScript/TypeScript/TSX app creation and build, runtime execution, nested imports and spaced paths passed', flush=True)
