# Everkeep setup (a wizard your agent runs)

*User: open this folder in your coding agent and type **`setup`**. The agent runs the steps below.*

---

## Instructions for the agent

Run these steps one by one. Ask the user one question at a time, in the language they used to type `setup` (or the language they pick in question 4).

**Date and time:** whenever a step needs the date or time, get it from the system (e.g. `date` or PowerShell `Get-Date`) in the user's time zone. Never guess from model memory: models often get the day wrong.

### Step 1: Questions

1. What is your AI companion's name? (e.g. Mira, Jarvis, Luna). This name is also the **call word**.
2. Your name, or what you'd like to be called?
3. Relationship style? (e.g. coding partner and friendly assistant / mentor / professional assistant / casual friend)
4. Conversation language? (e.g. English / Bahasa Melayu / mixed)
5. Time zone? (e.g. Asia/Kuala_Lumpur). Detect it from the system and just ask the user to confirm.

### Step 2: Fill in the placeholders

Replace the placeholders in **all** `.md` and `.json` files, except the `_dev/` folder. **Except `{{MEMORY_ROOT}}`:** leave it in `connectors/CONNECTOR.md` and fill it in only in the copy added to the agent's global instructions file (Step 4). That way the memory folder can move to another computer without broken paths.

| Placeholder | Value |
|---|---|
| `{{AI_NAME}}` | answer 1 |
| `{{USER_NAME}}` | answer 2 |
| `{{RELATIONSHIP_STYLE}}` | answer 3 |
| `{{SETUP_DATE}}` | today's date, `YYYY-MM-DD`, **from the system** |
| `{{MEMORY_ROOT}}` | full path of this folder **on this computer**, with `/` (e.g. `C:/Everkeep` or `/home/ali/everkeep`). Only in the connector block |

Then search for `{{` to make sure no placeholder is left (except `{{MEMORY_ROOT}}` in `connectors/CONNECTOR.md`, plus `SETUP.md` and `_dev/`).

Also fill in the `<...>` parts of `core/identity.md` (language, voice) and `core/user.md` (language, time zone, field) from the answers. If the user did not answer something, leave the `<...>` as it is. Never make things up.

### Step 3: Record the setup

Create `diary/YYYY-MM-DD.md` with the first entry. Date and time come from the system; `[agent-name]` is the agent running the setup (e.g. `[claude-code]`, `[opencode]`), not the companion's name:

```markdown
# Diary YYYY-MM-DD

### HH:MM [agent-name] Setup
**What happened:** <AI name> was born. User: <name>. Style: <style>. Memory root: <path>.
**Next:** connect the agents and test the call.
```

### Step 4: Connect the agents

1. Show the table in `connectors/README.md` and ask which agents the user uses.
2. For each chosen agent:
   - If its global instructions file exists, **make a backup** (`<file>.bak-everkeep`).
   - Show the text that will be added, and wait for the user to agree.
   - **Append** the block from `connectors/CONNECTOR.md` to the end of the file, with `{{MEMORY_ROOT}}` replaced by this folder's path on this computer. Never overwrite existing content.
   - If a `<!-- everkeep:start -->` block is already there, update only that block.
3. For agents that only have a "Custom Instructions" box, give the user the text to paste themselves.
4. **Claude Code (optional):** offer to install the `everkeep-skills` plugin, the auto-trigger wrappers for the skills (see `plugins/everkeep-skills/README.md`).
5. **Claude Code (optional):** offer the status line that shows the last `save`, session size and today's diary (see `extras/statusline/README.md`). Install with `python extras/statusline/install.py`. If the user already has another status line, ask before using `--force`.

### Step 5: Git (optional, recommended)

Ask: "Do you want to keep your memory's history with git? It lets you undo if a file gets damaged."
If yes, run `git init` and make the first commit. **If this folder was cloned from the public Everkeep template repo**, remove or change `origin` (`git remote remove origin`) before any push, so personal memory is never sent to the public repo. The GitHub repo **must be private** if the user wants a cloud backup. If the user works on more than one computer, explain the options in `skills/git.md` → "Multiple devices" and record their choice.

### Step 6: Test

Ask the user to open a new session in a connected agent, from a different folder, and type the AI's name.
The test passes if the AI greets the user by name.

Finally, add the line `SETUP DONE: YYYY-MM-DD` at the top of this file so setup never runs twice.

---

## Another computer (existing memory)

The user already has Everkeep memory and wants to use it on another computer:

1. Get the memory folder onto the new computer: `git clone <the user's private repo>` (recommended), or copy the folder. **Only one copy per computer.**
2. Open that folder in the agent and type `setup`. The agent sees `SETUP DONE` at the top of this file (older setups may say `SETUP SELESAI`), so:
   - **Don't** ask the Step 1 questions or rewrite `core/`.
   - Run **Step 4 only** (connect the agents), with `{{MEMORY_ROOT}}` = the folder's path on this computer.
   - Optional: the Claude Code status line and plugin.
3. Follow `skills/git.md` → "Multiple devices": `git pull --rebase` before you start working, commit + push after `save`.
4. Test: open a new session from another folder and call the AI's name.

## After setup

The list of skills is in `skills/README.md`. To add your own skill, type `new skill`.
