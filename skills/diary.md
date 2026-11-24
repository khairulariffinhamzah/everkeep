# Skill: diary

**Triggered by:** `save diary`, `write diary`; or at the end of a long, important session (offer first)
**Reads:** today's `diary/YYYY-MM-DD.md`   **Writes:** the same file (append only)

## Steps
1. Get the real date and time from the system, in the user's time zone (`core/user.md`). Never guess.
2. Open `diary/YYYY-MM-DD.md`. If it doesn't exist yet, create it with the heading `# Diary YYYY-MM-DD`.
3. **Append** an entry at the end of the file:

   ```markdown
   ### HH:MM [agent-name] <project or topic>
   **What happened:** <2–5 lines>
   **Decisions:** <if any>
   **Learned about {{USER_NAME}}:** <if any>
   **Next:** <1–3 items>
   ```

   `[agent-name]` is the agent writing the entry (e.g. `[claude-code]`, `[opencode]`), not the companion's name. Write the entry in the conversation language from `core/user.md`.
4. If today is the first day of a new month, move last month's diary files to `diary/archive/YYYY-MM/`.
5. If git is used, run `git.md`.

## Don't
- Don't edit old entries, including entries written by other agents.
- Don't record sensitive things the user doesn't want recorded.
