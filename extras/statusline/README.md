# Everkeep status line (Claude Code only, optional)

One line below the Claude Code input box:

```
🔒 Mira · 💾 12m ago · session 34/150 · diary ✓ · ⬆ 2  |  Sonnet 5.5 · 📁 cake-shop · ctx 41% · ⎇ main*3 · $0.42
```

| Part | Meaning |
|---|---|
| `🔒 Mira` | The companion is awake in this session (only shows after you call its name) |
| `💾 12m ago` | When `core/session.md` was last saved. Green < 1 hour, yellow < 6 hours, red after that: time to `save` |
| `session 34/150` | Size of `core/session.md`. Yellow > 80 lines, red > 150: time to `compact memory` |
| `diary ✓` / `diary –` | There is / isn't a diary entry today |
| `⬆ 2` | Memory files not committed yet (if the memory folder is a git repo): time to `commit memory` |
| `ctx 41%` | Context usage. Green < 50%, yellow < 80%, red after that |
| `⎇ main*3` | The current project's git branch and number of changed files |

Before the companion is called, only the right-hand part (model, folder, context, branch, cost) is shown.

## Install

Needs Python 3.

```bash
python extras/statusline/install.py
```

- The script adds `statusLine` to `~/.claude/settings.json` and keeps a backup, `settings.json.bak-everkeep`.
- If you already have another status line, the script does **not** replace it. Use `--force` if you really want to replace it.
- Remove: `python extras/statusline/install.py --remove`

After moving the Everkeep folder, run `install.py` again so the path is updated.
