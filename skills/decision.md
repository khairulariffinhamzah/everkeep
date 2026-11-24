# Skill: decision

**Triggered by:** `log decision`, `why did we choose ...`; or when a big choice is made in the conversation (offer to record it)
**Reads/Writes:** `projects/<name>.md` → "Decisions" section

## Steps: record
1. Sum up the decision in one sentence and the reason in one sentence. Also mention the rejected alternatives, if any.
2. If the decision is really a **project rule** (e.g. "all UI text in Malay"), offer to write the rule in the project's `AGENTS.md` (ask permission). In Everkeep, record only the date and the **reason**, not the rule itself again.
3. Re-read the project file, then add this line at the **top** of the "Decisions" list:
   `- YYYY-MM-DD <decision> (reason: <...>; rejected: <...>) [agent-name]`
4. If a new decision overrides an old one, mark the old line with `~~...~~ → replaced YYYY-MM-DD`. Don't delete it.

## Steps: "why did we choose ...?"
1. Search the project file's "Decisions" section, then the diary.
2. Answer with the date and the reason. If there is no record, tell the user.
