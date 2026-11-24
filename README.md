# 🔒 Everkeep

**English** · [Bahasa Melayu](README.ms.md)

**Long-term memory for your AI companion, in any coding agent.**

> *Ever* + *keep*: kept forever. **One memory, every coding agent.**
> Daily work lives in `session`, the story goes into `diary`, and what matters is kept in `core`.

Coding agents forget everything when a session ends, and each agent keeps its own memory that the others can't see. Everkeep gives you **one brain**: a folder of plain markdown files. Any agent can wake it up with a single word, the name you give your AI companion.

```
Claude Code ─┐
OpenCode    ─┤
Antigravity ─┼──►  📁 Everkeep  (identity · user · session · projects · diary)
Cline / Roo ─┤
Aider / ... ─┘
```

```
> hi Mira
Hi Ali, Mira here. Last time (yesterday, in OpenCode) we were on kedai-kek:
the order form is done, the WhatsApp button is next. Carry on?
```

## Why Everkeep

- **One brain, many agents.** Start in Claude Code, continue in OpenCode, and your AI still remembers.
- **No server, no database.** Just `.md` files you can read and edit yourself.
- **Model-agnostic.** Works with Claude, Gemini, GPT or any model through your own API key, as long as the agent can read and write files.
- **Your companion, your name.** Everkeep is the engine; you choose who your AI is.
- **No-code setup.** Your own agent runs the setup as a short Q&A.

## Get started in 3 steps

1. Clone or copy this folder to a permanent place, e.g. `C:\Everkeep` or `~/everkeep`. **Keep one copy only.**
   ```
   git clone https://github.com/khairulariffinhamzah/everkeep ~/everkeep
   ```
2. Open that folder in your coding agent and type: **`setup`**
3. Answer a few questions. Then open a new session in any connected agent, from any folder, and type your AI's name.

> ⚠️ **Your memory is private.** If you cloned this template, never push your memory to a public repo. Setup helps you switch to your own **private** repo.

## Daily commands

| Type | What happens |
|---|---|
| `<AI name>` / `hi <AI name>` | Loads memory and picks up where you left off |
| `save` | Saves session and project progress |
| `save diary` | Writes today's diary entry |
| `remember ...` | Stores one lasting fact |
| `do you remember ...` | Searches past diary and project notes |
| `log decision` | Records a decision and why, in the project file |
| `compact memory` | Trims memory that has grown too long |
| `new skill` | Creates your own skill |
| `commit memory` / `push memory` | Keeps memory history in git |
| `init project` | Sets up `AGENTS.md` + `CLAUDE.md` in a project so every agent reads the same rules |

Commands in other languages are understood too (e.g. Malay `simpan`, `tolong ingat`), but the English phrases above are the standard.

Your AI also offers to `save` when you say goodbye, switch projects or finish a big task, so work isn't lost.

## How it works

1. **Setup** adds a short connector block to each agent's global instruction file (for Claude Code, `~/.claude/CLAUDE.md`). It says: *when the user types "Mira", read `EVERKEEP.md` in this folder.*
2. **Waking up** reads `core/identity.md` (who the AI is), `core/user.md` (who you are), `core/session.md` (where you stopped) and, if the current folder matches, `projects/<folder>.md`.
3. **Skills** in `skills/` are plain markdown steps, so any agent can follow them without a plugin system. Claude Code can optionally install auto-trigger wrappers (`plugins/everkeep-skills`).
4. **Shared-brain rules** keep several agents from overwriting each other: read before write, append-only diary tagged with the agent's name, core files changed only on request, no secrets, absolute dates.

### Project rules vs. personal memory

| Kind of information | Where it lives |
|---|---|
| Project rules everyone and every AI should follow (stack, build/test commands, code style) | `AGENTS.md` **inside the project** (shared, committed) |
| Progress, decisions and why, open tasks, pitfalls | `projects/<folder>.md` in Everkeep (private) |
| Facts about you | `core/user.md` |

Each fact lives in one place. `init project` creates `AGENTS.md` plus a `CLAUDE.md` that only contains `@AGENTS.md`, so Claude Code reads the same rules as other agents.

## Supported agents

| Agent | Status |
|---|---|
| Claude Code (CLI, IDE, Desktop **Code** tab) | ✅ tested |
| OpenCode | ✅ tested (setup + wake-up) |
| Antigravity | ✅ tested (wake-up) |
| Gemini CLI, Codex CLI, Cline, Roo Code, Kilo Code, Aider | ⏳ connector locations listed, not yet tested |
| Claude Desktop **Cowork** / **Chat** | ⚠️ limited, see `connectors/README.md` |
| Anything else | paste the connector block into its custom instructions |

Small or cheap models may skip steps. If that happens, say: *"Mira, read EVERKEEP.md"*.

## More than one computer

Keep your memory in a **private** git repo. On the new computer, clone it and type `setup`: the agent sees setup is already done and only connects itself. Pull before you start, push after you `save`. Memory files contain no absolute paths, so the folder can live anywhere on each machine. Details: `SETUP.md` → *Komputer tambahan* and `skills/git.md` → *Banyak peranti*.

## Structure

```
EVERKEEP.md              entry point: wake-up, commands, shared-brain rules
AGENTS.md / CLAUDE.md    instructions when an agent opens this memory folder
SETUP.md                 setup wizard (run by the agent)
LICENSE                  MIT
core/
  identity.md            who the AI is
  user.md                who you are and how you work
  session.md             working memory: where you stopped (one active project)
projects/                one file per project, matched by folder name
diary/                   daily diary, append-only (archive/ for past months)
skills/                  plain-markdown skills any agent can follow
plugins/everkeep-skills/ auto-trigger wrappers for Claude Code (optional)
connectors/              connector block + instruction-file locations per agent
extras/statusline/       Claude Code status line: AI name, last save, session size (optional)
```

> **Note:** the protocol and skill files are currently written in Malay (agents read them fine in any language). An English version of the internal files is planned.

## License

MIT. See `LICENSE`.
