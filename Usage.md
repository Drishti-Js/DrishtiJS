Drishti CLI Commands
==============================

Binaries
- Main CLI: `drish`
- Scaffold shortcut: `Drishti-Create-NewVisionApp`

Quick Start (Recommended)
- Create app in current directory: `Drishti-Create-NewVisionApp`
- Enter app root: `cd NewVisionApp`
- Start app from app root: `drish run`
- Open: `http://127.0.0.1:3000`

Run Modes
- Default app run: `drish run`
- Custom port: `drish run --port 4173`
- Enable CSS editor (no key, local dev): `DRISH_ENV=dev DRISH_DEV_EDITOR=1 drish run`
- Enable CSS editor with auth key: `drish run --dev-editor-key "your-secret"`
- Explicit editor toggle flag: `drish run --dev-editor`

Auto Routes (File-based)
- Preferred auto-route directory: `app/pages`
- Backward-compatible directory: `app/routes`
- `drish run` now indexes both (prefers `app/pages` when same route exists in both)
- Static route examples:
  - `app/pages/about.js` -> `/about`
  - `app/pages/docs/guides/index.js` -> `/docs/guides`
- Dynamic route examples:
  - `app/pages/orders/[id].js` -> `/orders/:id` pattern
  - `app/pages/blog/[...slug].js` -> catch-all pattern

Core Commands
1. `drish help`
2. `drish -h`
3. `drish --help`
4. `drish --version`
5. `drish "< request>" [--app <dir>]`

AI Commands
6. `drish ai "< request>" [--app <dir>]`
7. `drish is < request words...> [--app <dir>]` (alias for `ai`)
8. `drish ask < request words...> [--app <dir>]` (alias for `ai`)
9. `drish ai doctor`
10. `drish ai scaffold-helper <path>`

Create Commands
11. `drish create app <name> [--typescript|--tsx|--javascript]`
    - `--typescript`: TypeScript mode (`.ts` service/runtime modules, generated UI modules in `.tsx`)
    - `--tsx`: TSX-heavy app mode (advanced template mode)
    - `--javascript`: JavaScript mode (`.js` service/runtime modules and generated UI modules)
    - Removed aliases: `--ts` and `--js`
12. `drish create ai "< request>" [--app <dir>]`
13. `drish create "< request>" [--app <dir>]`
14. `drish create form [form-title] [--app <dir>]`
15. `drish create theme <natural-language prompt> [--app <dir>]`
16. `drish create page <natural-language prompt> [--app <dir>]`
    - Creates route modules in `app/pages` (or `app/routes` fallback)
    - Accepts route/file hints like `route /orders`, `users.js`, `orders/[id].js`
17. `drish create section <natural-language prompt> [--app <dir>]`
18. `drish create layout <natural-language prompt> [--app <dir>]`
19. `drish create dashboard <natural-language prompt> [--app <dir>]`
20. `drish create table <natural-language prompt> [--app <dir>]`
21. `drish create chart <natural-language prompt> [--app <dir>]`
22. `drish create api <natural-language prompt> [--app <dir>]`
23. `drish create auth <natural-language prompt> [--app <dir>]`

Natural-Language Routing Commands
24. `drish update "< request>" [--app <dir>]`
25. `drish add < request words...> [--app <dir>]` (alias for `update`)
26. `drish change < request words...> [--app <dir>]` (alias for `update`)
27. `drish improve < request words...> [--app <dir>]` (alias for `update`)
28. `drish fix "< request>" [--app <dir>]`
29. `drish debug "< request>" [--app <dir>]`
30. `drish why < request words...> [--app <dir>]` (alias for `debug`)
31. `drish explain "< request>" [--app <dir>]`
32. `drish make < request words...> [--app <dir>]` (alias for `create`)
33. `drish build < request words...> [--app <dir>]` (alias for `create`)

Route-focused NL Examples
- `drish create page "create page users" --app <dir>` -> `app/pages/users.<ext>`
- `drish create "create users.js" --app <dir>` -> `app/pages/users.<ext>`
- `drish create page "create orders page at route /orders" --app <dir>` -> `app/pages/orders.<ext>`
- `drish create page "create order details page at route /orders/[id]" --app <dir>` -> `app/pages/orders/[id].<ext>`
- `drish add "add ordersform only to route /orders create if missing" --app <dir>`

Other Commands
34. `drish generate <schema.json>`
35. `drish run [file.js|app-dir|drishti.app.js] [--port <port>] [--dev-editor] [--dev-editor-key <secret>]`
36. `drish node init [app-dir]`
37. `drish node install <pkg...> [--app <dir>]`
38. `drish node add <pkg...> [--app <dir>]` (alias for `node install`)
39. `drish cap-token --secret <s> --subject <sub> [--ttl <sec>] --perm <op:res> [--perm <op:res>]`

Capability Token Notes
- Valid ops: `read`, `write`, `update`, `delete`, `put`
- Example:
  `drish cap-token --secret mysecret --subject service-a --ttl 3600 --perm read:users --perm write:orders`

Shortcut Generator
40. `Drishti-Create-NewVisionApp`
41. `Drishti-Create-NewVisionApp --typescript`
42. `Drishti-Create-NewVisionApp --tsx`
43. `Drishti-Create-NewVisionApp --javascript`
44. `Drishti-Create-NewVisionApp --help`
45. Removed aliases: `--ts` and `--js`

Troubleshooting
- Ensure active binary:
  `command -v drish`
  `type -a drish`
- Start from app root if using `drish run`:
  `cd <your-app-dir>`
  `drish run`

Build & Install (Local)
1. `cd ~/projects/Drishti-Engine`
2. `cmake -S . -B build`
3. `cmake --build build --target drish Drishti-Create-NewVisionApp test_create_nl test_request_router`
4. `./build/test_create_nl`
5. `./build/test_request_router`
6. `ln -sf ~/projects/Drishti-Engine/build/drish ~/.local/bin/drish`
7. `ln -sf ~/projects/Drishti-Engine/build/Drishti-Create-NewVisionApp ~/.local/bin/Drishti-Create-NewVisionApp`
8. `hash -r`
9. `command -v drish`
10. `type -a drish`

Optional global install (requires sudo)
11. `sudo cp ~/projects/Drishti-Engine/build/drish /usr/local/bin/drish`
12. `sudo cp ~/projects/Drishti-Engine/build/Drishti-Create-NewVisionApp /usr/local/bin/Drishti-Create-NewVisionApp`
13. `hash -r`
