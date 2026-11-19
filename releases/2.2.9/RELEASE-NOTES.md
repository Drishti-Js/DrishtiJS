# Drishti framework 2.2.9

New native framework distributions aligned with the existing drishtijs 2.2.9 npm package. This is the Drishti framework CLI/runtime release; DrishX Agent application and model releases are distributed separately.

- macOS: universal Intel and Apple Silicon binaries, macOS 14 or later; PKG, DMG and portable archive. OpenSSL is statically linked, so Homebrew is not required.
- Windows: x64 NSIS installer and portable ZIP. Portable binaries are exercised on Windows before publication.
- Linux: x86_64 Debian package and portable archive; glibc 2.35 or later and OpenSSL 3 system libraries. Ubuntu 22.04 and Debian 12 are suitable baselines.
- Windows module loading now preserves nested relative imports when callers use native backslash paths. Regression checks cover nested imports and directories containing spaces.
- CLI and Windows installer report the matching framework version rather than older hardcoded versions.
- Framework, QuickJS and relevant OpenSSL license notices are included. SHA256SUMS identifies the exact downloadable files.

Run `drish --version`, `drish help`, or `drish create app MyApp --typescript`. In the generated application, run `npm install` before using its npm scripts; those workflows require Node.js/npm.

The native macOS packages are not notarized with a publisher identity; the Windows installer has no publisher code signature. These are download packages, not an automatic update to installed system tools.

Publication is gated on native binary version/help, JavaScript/TypeScript/TSX scaffold and build checks, and runtime execution on macOS, Windows and Linux. These smoke checks do not certify every framework feature or installed application.
