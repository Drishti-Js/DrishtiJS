"""Publish verified assets by release ID; drafts do not yet have a Git tag."""
import hashlib
import json
import os
from pathlib import Path
import urllib.parse
import urllib.request

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'releases/latest.json').read_text())
directory = root / manifest['asset_directory']
version = manifest['version']
tag = 'v' + version
repository = os.environ['GITHUB_REPOSITORY']
api = 'https://api.github.com/repos/' + repository
headers = {'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
           'Accept': 'application/vnd.github+json', 'User-Agent': 'Drishti-framework-release'}

def request(url, method='GET', body=None, content_type='application/json'):
    raw = json.dumps(body).encode() if isinstance(body, dict) else body
    req = urllib.request.Request(url, data=raw, method=method,
                                 headers={**headers, 'Content-Type': content_type})
    with urllib.request.urlopen(req, timeout=120) as response:
        return json.load(response)

releases = request(api + '/releases?per_page=100')
matches = [r for r in releases if r['tag_name'] == tag]
assert len(matches) <= 1, 'Multiple releases share this tag; inspect before publishing'
notes = (directory / 'RELEASE-NOTES.md').read_text()
if matches:
    release = matches[0]
else:
    release = request(api + '/releases', 'POST', {
        'tag_name': tag, 'target_commitish': os.environ['GITHUB_SHA'],
        'name': 'Drishti framework ' + version, 'body': notes, 'draft': True})
release_url = api + '/releases/' + str(release['id'])
assets_url = release_url + '/assets?per_page=100'
files = [directory / a['filename'] for a in manifest['assets']]
files += [directory / 'SHA256SUMS', directory / 'RELEASE-NOTES.md', root / 'releases/latest.json']
expected = {p.name: ('sha256:' + hashlib.sha256(p.read_bytes()).hexdigest(), p.stat().st_size)
            for p in files}
present = {a['name']: a for a in request(assets_url)}
for path in files:
    digest, size = expected[path.name]
    if path.name in present:
        assert (present[path.name].get('digest'), present[path.name]['size']) == (digest, size), path.name
        continue
    assert release['draft'], 'Published releases are immutable; choose a new version'
    url = 'https://uploads.github.com/repos/' + repository + '/releases/' + str(release['id'])
    uploaded = request(url + '/assets?name=' + urllib.parse.quote(path.name), 'POST',
                       path.read_bytes(), 'application/octet-stream')
    assert (uploaded.get('digest'), uploaded['size']) == (digest, size), path.name
    print('Uploaded and verified:', path.name, flush=True)
present = {a['name']: a for a in request(assets_url)}
for name, expected_identity in expected.items():
    assert (present[name].get('digest'), present[name]['size']) == expected_identity, name
if release['draft']:
    release = request(release_url, 'PATCH', {
        'target_commitish': os.environ['GITHUB_SHA'], 'name': 'Drishti framework ' + version,
        'body': notes, 'draft': False, 'prerelease': False})
assert not release['draft']
print('Published verified release:', release['html_url'], flush=True)
