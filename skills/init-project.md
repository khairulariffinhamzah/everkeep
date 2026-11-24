# Skill: init project

**Triggered by:** `init project`, `setup project`; or offer it when the working folder is a project without `AGENTS.md`
**Writes:** `AGENTS.md` + `CLAUDE.md` in the **project folder**, `projects/<folder-name>.md` in Everkeep

Goal: every project has **one** rules file (`AGENTS.md`) that every agent reads. `CLAUDE.md` contains only `@AGENTS.md` so Claude Code reads the same file.

> Why `CLAUDE.md` is still needed: Claude Code reads `CLAUDE.md` first and only falls back to `AGENTS.md` when there is no `CLAUDE.md`. If `CLAUDE.md` exists without `@AGENTS.md`, `AGENTS.md` is **ignored**. Details: `connectors/README.md` → "Claude: which files are read".

## Steps
1. **Make sure this is a project folder.** Never run it in the home folder, the Everkeep root, or a system folder. If unsure, ask the user.
2. **Check the existing files** in the project folder: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.clinerules`.
3. **Act on what you find:**

   | Situation | Action |
   |---|---|
   | No `AGENTS.md`, no `CLAUDE.md` | Draft `AGENTS.md` (step 4), then create `CLAUDE.md` containing `@AGENTS.md` |
   | `CLAUDE.md` but no `AGENTS.md` | Offer to move the contents of `CLAUDE.md` to `AGENTS.md`, then make `CLAUDE.md` just `@AGENTS.md`. If the user says no, leave it |
   | `AGENTS.md` but no `CLAUDE.md` | Create `CLAUDE.md` containing `@AGENTS.md` |
   | Both exist | Check that `CLAUDE.md` references `@AGENTS.md`. If not, show the difference and ask the user. Never merge without permission |
   | `.cursorrules` / `.clinerules` / `GEMINI.md` exist | Use their contents as draft material. Don't delete those files |

4. **Draft `AGENTS.md`** by reading the project (README, `package.json` / `composer.json` / `pyproject.toml`, folder layout). Short, facts only:

   ```markdown
   # <Project name>

   <One sentence: what this project is>

   ## Stack
   - <language, framework, hosting>

   ## Commands
   - Install: `<...>`
   - Dev: `<...>`
   - Build / test: `<...>`

   ## Layout
   - `<folder>/`: <purpose>

   ## Rules
   - <code style, things that are not allowed, the right account/deploy target>
   ```

   Only write things confirmed by the project files or the user. If unsure, leave `<...>` and ask.
5. **Show the draft to the user** and wait for approval before writing. This file is shared with anyone who opens the project.
6. **Optional:** if the user uses Gemini CLI, offer a `GEMINI.md` containing `@AGENTS.md`.
7. **Everkeep memory:** if `projects/<folder-name>.md` doesn't exist yet, create it from `projects/_template.md`. Fill in **only Folder, Project rules (the `AGENTS.md` path) and Status**. Don't copy anything from `AGENTS.md` (what the project is, stack, commands, rules) and don't record "created AGENTS.md" as a decision.
8. Report the files created. **Don't commit the project repo** unless the user asks. The Everkeep repo can be committed through `git.md`.

## Don't
- Don't put personal information, Everkeep memory, secrets or API keys in the project's `AGENTS.md`.
- Don't overwrite an existing `AGENTS.md` or `CLAUDE.md` without permission.
