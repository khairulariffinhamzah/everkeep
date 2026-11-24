# Connectors: where to put the `CONNECTOR.md` text for each agent

Each agent has its own global instructions file. Append the block in `CONNECTOR.md` to the end of that file. Never overwrite existing content.

> ⚠️ **Paths change.** Agents move these files between versions. Rows marked ✅ were tested in November 2026; check the others against the agent's current docs.

| Agent | Global instructions file | Status |
|---|---|---|
| Claude Code (CLI, VS Code, JetBrains) | `~/.claude/CLAUDE.md` | ✅ tested |
| Claude Desktop: **Code** tab | `~/.claude/CLAUDE.md`, same file as Claude Code | ⏳ should work, to be tested |
| Claude Desktop: **Cowork** tab | Cowork's own memory (see the Claude section below) | ⏳ to be tested |
| Claude Desktop / claude.ai: **Chat** tab | Project instructions or personal preferences + a file system connector | ⚠️ limited, see below |
| OpenCode | `~/.config/opencode/AGENTS.md` | ✅ tested (setup + wake-up, Nov 2026) |
| Antigravity | `~/.gemini/GEMINI.md` (Global Rules) | ✅ tested (wake-up, Nov 2026) |
| Gemini CLI | `~/.gemini/GEMINI.md`, same file as Antigravity | ⚠️ free individual accounts rejected by Google ("IneligibleTierError", Nov 2026): use Antigravity |
| Codex CLI | `~/.codex/AGENTS.md` | ⏳ to be tested |
| Cline | Global Rules folder (in Cline's settings) | ⏳ to be tested |
| Roo Code / Kilo Code | `~/.roo/rules/` / `~/.kilocode/rules/` | ⏳ to be tested |
| Aider | `~/.aider.conf.yml` → `read: [<memory root>/connectors/CONNECTOR.md]` (a filled-in copy) | ⏳ to be tested |
| Other agents | the "Custom Instructions" / "System Prompt" box in settings | paste by hand |

**WSL:** use the same Windows folder through `/mnt/c/...` (e.g. `/mnt/c/Everkeep`). Never make a second copy inside Linux. If the user works in both Windows and WSL, write both paths in the connector block.

`~` = the user's home folder (Windows: `C:\Users\<name>`). On Windows, most agents use `C:\Users\<name>\.claude`, `C:\Users\<name>\.gemini` and so on.

## Claude: which files are read

### Claude Code (CLI, IDE, Code tab in Claude Desktop)
For **project** rules, Claude Code reads:
1. `CLAUDE.md` (the main file; also searched upwards through parent folders)
2. `AGENTS.md`, **only as a fallback** when there is no `CLAUDE.md` (since v2.1.277; can be changed in `/config` → "Project instructions")

That is why `init project` always creates a `CLAUDE.md` containing `@AGENTS.md`:
- Older versions, the first session after an install/upgrade, and some setups (Bedrock, Vertex, gateways) only read `CLAUDE.md`.
- **If `CLAUDE.md` exists but does not reference `@AGENTS.md`, `AGENTS.md` is ignored.**
- The import does not make `AGENTS.md` load twice.

For **Everkeep**, the connector block goes in `~/.claude/CLAUDE.md` (global), so the companion can be called from any folder. The Code tab in Claude Desktop shares the same settings as the CLI.

### Claude Desktop: Cowork tab
Cowork has its own memory folder with a separate `CLAUDE.md`, not `~/.claude/CLAUDE.md`. Suggested (untested): paste the `CONNECTOR.md` block into Cowork's memory/instructions, and give Cowork access to the Everkeep folder.

### Claude Desktop / claude.ai: Chat tab
Chat does not read files on your computer by itself. Everkeep can only work if:
1. A file system connector (MCP) is installed and given access to the Everkeep folder, **and**
2. The `CONNECTOR.md` block is pasted into the Project instructions or personal preferences.

Otherwise, use the Code tab or Claude Code for work that needs Everkeep memory.

## Notes

- **Agents with your own API key** (Cline, Roo, Kilo, Aider, OpenCode and others): Everkeep does not depend on the model. As long as the model can read and write files through the agent, the memory works.
- **Small or cheap models** may skip steps in the protocol. If that happens, say it directly: "{{AI_NAME}}, read EVERKEEP.md".
- The `<!-- everkeep:start -->` / `<!-- everkeep:end -->` markers let setup and update scripts find this block without touching anything else.
