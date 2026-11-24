# Skill: compact

**Triggered by:** `compact memory`; or automatically when `core/session.md` is over 150 lines or another `core/` file is over 250 lines
**Reads/Writes:** `core/*`, `projects/*`, `diary/`

## Steps
1. Read the file that is too long.
2. Sort every part of that file:
   - **Still active:** keep it.
   - **Done / old but historically useful:** move it to today's diary as a `[compact]` entry, then remove it from the original file.
   - **Lasting facts about the user** that strayed into `session.md`: move them to `user.md`.
   - **Project details:** move them to `projects/<name>.md`.
   - **Session logs in `user.md`** (e.g. "Session 5: ..."): boil them down to lasting traits/preferences, and move the story to the diary.
   - **Another project's context in `session.md`:** move it to `projects/<name>.md`.
   - **Duplicates or no longer true:** remove.
3. Show the user a summary of the changes **before** writing, e.g. "Move 40 lines to the diary, remove 12 duplicates". Wait for the user to agree.
4. Write the changes, then run `git.md` if git is used.

## Don't
- Don't remove anything that doesn't exist somewhere else without the user's permission.
- Don't compact the diary. The diary is the historical record.
