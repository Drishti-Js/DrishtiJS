Drishti CLI and AI Commands
==============================

Binaries
- Main binary: `drish`
- Scaffold shortcut binary: `Drishti-Create-NewVisionApp`

- Run commands naturally:
  - `create ...`, `add ...`, `fix ...`, `debug ...`, `run ...`
- These command names are treated as first-class CLI entry points.

Quick Start (Recommended)
- Create app in current directory: `Create-NewVisionApp`
- Enter app root: `cd NewVisionApp`
- Home route module (default scaffold): `app/pages/home.<ext>`
- Legacy fallback remains supported: `app/routes/home.<ext>`
- App context auto-detect for NL commands:
  - If run from a parent folder with exactly one child app root, commands auto-target that app.
  - If child app `./drish` exists, it is preferred.
  - If multiple child app roots exist, pass `--app <dir>` explicitly.
- Start app from app root: `run`
- Open: `http://127.0.0.1:3000`

Portable Path Setup (for all users)
- Set these once per shell/session:
  - `export DRISHTI_ENGINE_DIR="$HOME/path/to/Drishti-Engine"`
  - `export DRISHTI_APP_DIR="$DRISHTI_ENGINE_DIR/drishti"`
- Example:
  - `export DRISHTI_ENGINE_DIR="$HOME/projects/Drishti-Engine"`
  - `export DRISHTI_APP_DIR="$DRISHTI_ENGINE_DIR/drishti"`

Run Modes
- Default app run: `run`
- Custom port: `run --port 4173`
- Enable CSS editor (no key, local dev): `DRISH_ENV=dev DRISH_DEV_EDITOR=1 run`
- Enable CSS editor with auth key: `run --dev-editor-key "your-secret"`
- Explicit editor toggle flag: `run --dev-editor`

Auto Routes (File-based)
- Optional route-array config: `app/router.js` (or `app/router.ts` / `app/router.tsx`)
- Preferred auto-route directory: `app/pages`
- Backward-compatible directory: `app/routes`
- Runtime always merges all three sources with precedence:
  - `app/router.*` > `app/pages/*` > `app/routes/*`
- Runtime indexes both directories and warns on duplicate patterns/collisions.
- Static route examples:
  - `app/pages/about.js` -> `/about`
  - `app/pages/docs/guides/index.js` -> `/docs/guides`
- Dynamic route examples:
  - `app/pages/orders/[id].js` -> `/orders/:id` pattern
  - `app/pages/blog/[...slug].js` -> catch-all pattern

Core Commands
1. `help`
2. `-h`
3. `--help`
4. `version`
5. `"< request>" [--app <dir>]`

AI Commands
6. `ai "< request>" [--app <dir>]`
7. `is < request words...> [--app <dir>]` (alias for `ai`)
8. `ask < request words...> [--app <dir>]` (alias for `ai`)
9. `ai doctor`
10. `ai scaffold-helper <path>`

Create Commands
11. `create app <name> [--typescript|--tsx|--javascript]`
    - Default scaffold route file: `app/pages/home.<ext>`
    - `--typescript`: TypeScript mode (`.ts` service/runtime modules, generated UI modules in `.tsx`)
    - `--tsx`: TSX-heavy app mode (advanced template mode)
    - `--javascript`: JavaScript mode (`.js` service/runtime modules and generated UI modules)
    - Removed aliases: `--ts` and `--js`
12. `create ai "< request>" [--app <dir>]`
13. `create "< request>" [--app <dir>]`
14. `create form [form-title] [--app <dir>]`
15. `create theme <natural-language prompt> [--app <dir>]`
16. `create page <natural-language prompt> [--app <dir>]`
    - Creates route modules in `app/pages` (or `app/routes` fallback)
    - Accepts route/file hints like `route /orders`, `users.js`, `orders/[id].js`
17. `create section <natural-language prompt> [--app <dir>]`
18. `create layout <natural-language prompt> [--app <dir>]`
19. `create dashboard <natural-language prompt> [--app <dir>]`
20. `create table <natural-language prompt> [--app <dir>]`
21. `create chart <natural-language prompt> [--app <dir>]`
22. `create api <natural-language prompt> [--app <dir>]`
23. `create auth <natural-language prompt> [--app <dir>]`

Natural-Language Routing Commands
24. `update "< request>" [--app <dir>]`
25. `add < request words...> [--app <dir>]` (alias for `update`)
26. `change < request words...> [--app <dir>]` (alias for `update`)
27. `improve < request words...> [--app <dir>]` (alias for `update`)
28. `fix "< request>" [--app <dir>]`
29. `debug "< request>" [--app <dir>]`
30. `why < request words...> [--app <dir>]` (alias for `debug`)
31. `explain "< request>" [--app <dir>]`
32. `make < request words...> [--app <dir>]` (alias for `create`)
33. `build < request words...> [--app <dir>]` (alias for `create`)
    - Route attach/create behavior is pages-first (`app/pages/*`) with legacy fallback (`app/routes/*`) when needed.

Route-focused NL Examples
- `create page "create page users" --app <dir>` -> `app/pages/users.<ext>`
- `create page "create a dynamic route users" --app <dir>` -> `app/pages/users.<ext>` with route pattern `/users/[id]`
- `create "create users.js" --app <dir>` -> `app/pages/users.<ext>`
- `create page "create orders page at route /orders" --app <dir>` -> `app/pages/orders.<ext>`
- `create page "create order details page at route /orders/[id]" --app <dir>` -> `app/pages/orders/[id].<ext>`
- `add "add ordersform only to route /orders create if missing" --app <dir>` -> creates/updates `app/pages/orders.<ext>` first

Other Commands
34. `generate <schema.json>`
35. `run [file.js|app-dir|drishti.app.js] [--port <port>] [--dev-editor] [--dev-editor-key <secret>]`
36. `test <file.js|file.ts|file.tsx>`
37. `convert mobile [--platform android|ios] [--app <dir>] [--out <relative-dir>] [--web-url <http(s)://...>]`
38. `node init [app-dir]`
39. `node install <pkg...> [--app <dir>]`
40. `node add <pkg...> [--app <dir>]` (alias for `node install`)
41. `cap-token --secret <s> --subject <sub> [--ttl <sec>] --perm <op:res> [--perm <op:res>]`

Capability Token Notes
- Valid ops: `read`, `write`, `update`, `delete`, `put`
- Example:
  `cap-token --secret mysecret --subject service-a --ttl 3600 --perm read:users --perm write:orders`

Shortcut Generator
42. `Drishti-Create-NewVisionApp`
43. `Drishti-Create-NewVisionApp --typescript`
44. `Drishti-Create-NewVisionApp --tsx`
45. `Drishti-Create-NewVisionApp --javascript`
46. `Drishti-Create-NewVisionApp --help`
47. Removed aliases: `--ts` and `--js`

Troubleshooting
- Ensure active human command:
  `command -v create`
  `type -a create`
- Ensure main binary:
  `command -v drish`
  `type -a drish`
- Start from app root if using run:
  `cd <your-app-dir>`
  `run`

Build & Install (Local)
1. `cd "$DRISHTI_ENGINE_DIR"`
2. `cmake -S . -B build`
3. `cmake --build build --target drish Drishti-Create-NewVisionApp test_create_nl test_request_router`
4. `./build/test_create_nl`
5. `./build/test_request_router`
6. `ln -sf "$DRISHTI_ENGINE_DIR/build/drish" ~/.local/bin/drish`
7. `ln -sf "$DRISHTI_ENGINE_DIR/build/Drishti-Create-NewVisionApp" ~/.local/bin/Drishti-Create-NewVisionApp`
8. `for c in create add update change improve fix debug explain why make build run runapp test node generate ai ask is help version; do ln -sf "$DRISHTI_ENGINE_DIR/build/drish" ~/.local/bin/$c; done`
9. `hash -r`
10. `command -v create`
11. `type -a create`
12. `command -v drish`
13. `type -a drish`

Optional global install (requires sudo)
14. `sudo cp "$DRISHTI_ENGINE_DIR/build/drish" /usr/local/bin/drish`
15. `sudo cp "$DRISHTI_ENGINE_DIR/build/Drishti-Create-NewVisionApp" /usr/local/bin/Drishti-Create-NewVisionApp`
16. `for c in create add update change improve fix debug explain why make build run runapp test node generate ai ask is help version; do sudo ln -sf /usr/local/bin/drish /usr/local/bin/$c; done`
17. `hash -r`

Android App Commands
=================================

Requirements (one-time)
1. Install Android Studio with Android SDK, platform-tools, and emulator.
2. Ensure Java is installed with a currently supported JDK:
   - `java -version`
   - `which java`
   - `/usr/libexec/java_home -V  # macOS`
3. Set SDK env vars (macOS example):
   - `export ANDROID_SDK_ROOT="$HOME/Library/Android/sdk"`
   - `export ANDROID_HOME="$ANDROID_SDK_ROOT"`
   - `export PATH="$ANDROID_SDK_ROOT/platform-tools:$ANDROID_SDK_ROOT/emulator:$PATH"`
4. Verify tools:
   - `adb version`
   - `emulator -version`
   - `command -v curl`
   - `command -v unzip`

Engine / CLI build (before mobile conversion)
1. `cd "$DRISHTI_ENGINE_DIR"`
2. `cmake -S . -B build`
3. `cmake --build build --target drish`

Generate Android scaffold from app
1. Emulator/local-dev URL (default Android emulator host bridge):
   - `./build/drish convert mobile --platform android --app drishti --out mobile/android --web-url 'http://10.0.2.2:3000/'`
2. Cloud device/public test URL (must be public HTTPS):
   - `./build/drish convert mobile --platform android --app drishti --out mobile/android --web-url 'https://your-public-domain.com/'`

Build APK
1. `cd "$DRISHTI_APP_DIR/mobile/android"`
2. `chmod +x build-android-apk.sh`
3. `./build-android-apk.sh`

Install Gradle inside Android project (manual bootstrap, optional)
1. `cd "$DRISHTI_APP_DIR/mobile/android"`
2. `command -v gradle || brew install gradle`
3. `gradle -v`

Notes from build-android-apk.sh
- Requires a supported JDK version (script rejects unsupported Java).
- Resolves SDK from `ANDROID_SDK_ROOT` / `ANDROID_HOME` (or common defaults).
- Uses a bundled Gradle distribution (auto-downloads into `.drish-gradle` when needed).
- Falls back to system `gradle` if bundled gradle is unavailable.
- Gradle applies to Android builds only (`drishti/mobile/android`). iOS does not use Gradle.
- Produces debug APK at:
  `drishti/mobile/android/app/build/outputs/apk/debug/app-debug.apk`

Run app server for emulator WebView
1. `cd "$DRISHTI_ENGINE_DIR"`
2. `./build/drish run drishti --port 3000`
3. Keep this terminal running while testing the APK.

Install and launch on emulator/device
1. Start emulator:
   - `emulator -list-avds`
   - `emulator -avd <YOUR_AVD_NAME>`
2. Check connection:
   - `adb devices`
3. Install/reinstall debug APK:
   - `adb install -r "$DRISHTI_APP_DIR/mobile/android/app/build/outputs/apk/debug/app-debug.apk"`
4. Launch app:
   - `adb shell am start -n com.drishti.drishti/.MainActivity`

Rebuild loop (after app changes)
1. `cd "$DRISHTI_APP_DIR/mobile/android"`
2. `./build-android-apk.sh`
3. `adb install -r "$DRISHTI_APP_DIR/mobile/android/app/build/outputs/apk/debug/app-debug.apk"`

Debug commands
- App/device logs:
  `adb logcat | rg -i 'drishti|chromium|webview|ERR_|Unable to load app'`
- If WebView shows "Unable to load app":
  1. Confirm server is running: `./build/drish run drishti --port 3000`
  2. Confirm URL is reachable from emulator: use `http://10.0.2.2:3000/`
  3. Regenerate with correct URL using `drish convert mobile --web-url ...`

Convert command usage (reference)
- `drish convert mobile [--platform android|ios] [--app <dir>] [--out <relative-dir>] [--web-url <http(s)://...>]`

iOS App Commands
===========================================================

Important
- Default iOS output folder: `drishti/mobile/ios`
- Default iOS simulator web URL: `http://127.0.0.1:3000/`
- iOS does NOT use Gradle.

One-time iOS setup (Mac)
1. Install Xcode from App Store.
2. Point CLI tools to full Xcode:
   - `sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer`
3. Complete first launch + license:
   - `sudo xcodebuild -runFirstLaunch`
   - `sudo xcodebuild -license accept`
4. Confirm simulator runtimes:
   - `xcrun simctl list runtimes | rg -i ios`
5. Open simulator once:
   - `open -a Simulator`

Engine / CLI build (before iOS conversion)
1. `cd "$DRISHTI_ENGINE_DIR"`
2. `cmake -S . -B build`
3. `cmake --build build --target drish`

Start app server for iOS WebView
1. `cd "$DRISHTI_ENGINE_DIR"`
2. `./build/drish run drishti --port 3000 --dev-editor`
3. Keep this terminal running while using iOS app.

Generate iOS wrapper (choose one flow)
A) UI flow (recommended)
1. Open `http://127.0.0.1:3000`
2. Click `Convert To Mobile APP`
3. Select:
   - Platform: `iOS`
   - Output: `mobile/ios`
   - Web URL: `http://127.0.0.1:3000/`
4. Click `Convert to iOS`

B) CLI flow (equivalent)
1. `cd "$DRISHTI_ENGINE_DIR"`
2. `./build/drish convert mobile --platform ios --app drishti --out mobile/ios --web-url http://127.0.0.1:3000/`

Build iOS app (Simulator)
1. `cd "$DRISHTI_APP_DIR/mobile/ios"`
2. `chmod +x build-ios-app.sh`
3. `./build-ios-app.sh`

Open + run in Xcode
1. `open "$DRISHTI_APP_DIR/mobile/ios/DrishtiMobile.xcodeproj"`
2. Select an iPhone simulator device.
3. Run app: `Cmd+R`

Useful verify commands
1. `sed -n '1,20p' "$DRISHTI_APP_DIR/mobile/ios/App/WebViewConfig.swift"`
2. `curl -I http://127.0.0.1:3000/`

iOS troubleshooting
- Error: `NSURLErrorDomain / App Transport Security`
  1. Ensure URL is local simulator URL: `http://127.0.0.1:3000/`
  2. Re-run conversion (UI or CLI) and rebuild iOS app.
- Error: `Unable to find a destination matching ... iOS Simulator`
  1. Install iOS runtime in Xcode -> Settings -> Platforms
  2. `open -a Simulator`
  3. Retry `./build-ios-app.sh`
- Error: stale simulator cache
  1. In Xcode: `Product -> Clean Build Folder`
  2. Delete app from simulator
  3. Run again (`Cmd+R`)
- Error: missing project files
  - Re-run conversion to regenerate `drishti/mobile/ios`

TC (test checks) for iOS-related generator/runtime paths
1. `cd "$DRISHTI_ENGINE_DIR"`
2. `./build/test_create_app`
3. `./build/test_run`

Gradle note (Android only)
- Gradle commands apply only to `drishti/mobile/android`.
- iOS build uses Xcode / `xcodebuild`, not Gradle.
- Android Gradle bootstrap (optional):
  1. `cd "$DRISHTI_APP_DIR/mobile/android"`
  2. `command -v gradle || brew install gradle`
  3. `gradle -v`
