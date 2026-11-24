# Skill: recall

**Triggered by:** `do you remember ...`, `when did we ...`, `what happened with ...`
**Reads:** `diary/`, `diary/archive/`, `projects/`, `core/`   **Writes:** nothing

## Steps
1. Take 2–4 keywords from the question, including synonyms in the languages the memory is written in (e.g. "payment", Malay "bayaran").
2. Search in this order and stop when you have enough:
   1. `projects/` and `core/session.md`
   2. `diary/` (newest first)
   3. `diary/archive/`
3. Read the matching entries in full, not just the matching lines.
4. Answer **as a short story**: when (date), what happened, what was decided, where it is written (file path).
5. If you find several possibilities, list them and ask the user which one they mean.
6. If nothing is found, say so honestly. Never make it up. Ask whether the user wants to save that information now.

## Don't
- Don't dump raw grep output.
- Don't assume old memories are still true. Give the date so the user can judge.
