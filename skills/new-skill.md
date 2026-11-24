# Skill: new skill

**Triggered by:** `new skill`, `create skill`
**Writes:** `skills/<name>.md`, `skills/README.md`

## Steps
1. Ask the user, one question at a time, only what isn't clear yet:
   - What does this skill do? (one sentence)
   - Which phrases trigger it?
   - Which files does it read and write?
2. Choose a lowercase, hyphenated name (e.g. `check-budget`). If a file with that name already exists, stop and ask the user.
3. Write `skills/<name>.md` following the format in `skills/README.md`.
4. Add a row for the skill to the table in `skills/README.md` and to the "Keywords" table in `EVERKEEP.md`.
5. Show the result to the user. If git is used, run `git.md`.
6. Optional for Claude Code: create an auto-trigger wrapper in `plugins/everkeep-skills/skills/<name>/SKILL.md`, following the existing wrappers.

## Don't
- Don't invent the skill's purpose. If it isn't clear, ask the user.
