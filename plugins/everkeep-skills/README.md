# everkeep-skills (Claude Code only, optional)

Thin wrappers that let Claude Code trigger the Everkeep skills automatically. Each wrapper only points to `skills/<name>.md`, so the logic stays in one place, shared by every agent.

Other agents don't need this plugin. They follow the "Keywords" table in `EVERKEEP.md` directly.

## Install
```bash
claude plugin marketplace add <memory root path>
claude plugin install everkeep-skills@everkeep --scope user
```
