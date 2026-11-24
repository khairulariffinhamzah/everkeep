# Skills

Each skill is **one markdown file of steps**. Any agent can read and follow it without a plugin system. Claude Code can also install the auto-trigger wrappers in `plugins/everkeep-skills/`.

| File | Triggered by | Result |
|---|---|---|
| `save.md` | `save`, `remember ...` | Updates `core/session.md`, the project and the user |
| `diary.md` | `save diary` | Today's diary entry |
| `recall.md` | `do you remember ...`, `when did we ...` | Searches the diary/projects and tells the story back |
| `decision.md` | `log decision`, `why did we choose ...` | Logs the decision in the project file |
| `compact.md` | `compact memory`, or `session.md` over 150 lines | Summarises and moves old details out |
| `git.md` | after every save (if git is used), `commit memory`, `push memory` | Commits the memory |
| `new-skill.md` | `new skill` | Creates a new skill file |
| `init-project.md` | `init project` | Creates `AGENTS.md` + `CLAUDE.md` (`@AGENTS.md`) in the project, and the Everkeep project file |

Commands in the user's own language are understood too (e.g. Malay `simpan`, `simpan diari`, `kau ingat tak`).

## Skill file format

```markdown
# Skill: <name>
**Triggered by:** <standard English phrase> (phrases with the same meaning in other languages are accepted too)
**Reads:** <files>   **Writes:** <files>

## Steps
1. ...

## Don't
- ...
```
