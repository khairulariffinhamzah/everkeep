# Skill: save

**Triggered by:** `save`, `save memory`, `remember ...`
**Reads:** `core/*`, `projects/<name>.md`   **Writes:** the same files

## Steps: full save
1. Look back over the conversation and list what is **new and useful for future sessions**: progress, decisions, open tasks, things learned about the user.
2. **Re-read** every target file before writing it, because another agent may have changed it.
3. **If the active project has changed** (the working folder differs from "Active project" in `session.md`): move the old project's open tasks, decisions and pitfalls to `projects/<old-project>.md` first, then rewrite `session.md` for the new project. `session.md` never holds more than one project.
4. Write to the right files:
   - `core/session.md`: **rewrite** (don't append) "Where we left off", "Open tasks" and "Don't forget", then update the `Updated` line with the time in the user's time zone (`core/user.md`).
   - `projects/<folder-name>.md`: add decisions and update open tasks. If the file doesn't exist yet, copy it from `projects/_template.md`.
   - `core/user.md`: lasting facts only (preferences, rules, new focus), summarised. Update the existing line when a fact changes. Never write session logs here.
   - `core/identity.md`: change only if the user asks, or after they agree to your suggestion.
5. If `core/session.md` is over 150 lines, or `core/user.md` is over 250 lines, run `compact.md`.
6. If git is used, run `git.md`.
7. Report to the user in 2–4 lines: which files were written and the gist.

## Steps: single fact ("remember ...")
1. Decide where the fact lives: about the user → `user.md`; project progress/decision → `projects/<name>.md`; **project rule** (stack, build commands, code style) → `AGENTS.md` in the project folder (show the text and ask permission first, since that file is shared); about how the AI talks → `identity.md` (ask permission first).
2. Add one dated line. If an old fact conflicts, replace the old fact; don't keep both.
3. Confirm in one sentence.

## Don't
- Don't copy the conversation word for word. Write the gist only.
- Don't store secrets.
- Don't duplicate rules already in the project's `AGENTS.md` / `CLAUDE.md` into Everkeep.
- Don't delete facts about the user without a clear reason.
