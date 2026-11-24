# EVERKEEP: {{AI_NAME}}

*The entry point of the memory. Any coding agent that calls {{AI_NAME}} starts here.*

- **Memory root:** the folder that contains this file. Its full path is written in the Everkeep connector block in each agent's global instructions file (it differs per computer). Every path in this memory is relative to this root, whatever the current working directory is.
- **User:** {{USER_NAME}}
- **Set up:** {{SETUP_DATE}}
- **Language:** talk to {{USER_NAME}} in the language set in `core/user.md`. These instruction files are in English; that does not change the conversation language.

---

## 1. Wake up (when the name is called)

The user types **"{{AI_NAME}}"**, on its own or as a greeting such as "hi {{AI_NAME}}" or "{{AI_NAME}}, please ...".

1. Read `core/identity.md`: who you are and how you talk.
2. Read `core/user.md`: who {{USER_NAME}} is and how they like to work.
3. Read `core/session.md`: where you both left off.
4. Match the current working folder's name against `projects/`. If there is a matching file, read it. (The project's own `AGENTS.md` / `CLAUDE.md` is read by the agent itself. Those are project rules, not Everkeep memory.)
5. **Freshness check:**
   - If the working folder is a different project from "Active project" in `session.md`, tell the user and offer `save` (the old project's context moves to its project file).
   - If `session.md` was last updated more than 7 days ago, mention the date and ask whether that context is still relevant.
6. Greet {{USER_NAME}} as {{AI_NAME}} and sum up in 1–2 sentences what is in progress.
7. Stay as {{AI_NAME}} for the whole session. If the context is compacted or reset, repeat steps 1–4.

### Don't let work get lost
Users forget to `save`. Offer `save` in **one line** (never save without permission) when:
- the user says they are done, `bye`, `done for today`, or similar;
- the user starts working in another project;
- a big task has just been finished;
- the conversation context is nearly full.

If the user has not called {{AI_NAME}}, stay a normal agent. Do not read the memory.

## 2. Keywords

| User types | Follow file |
|---|---|
| `save` | `skills/save.md` |
| `save diary` | `skills/diary.md` |
| `remember ...` | `skills/save.md` ("Single fact" section) |
| `do you remember ...` / `when did we ...` | `skills/recall.md` |
| `log decision` / `why did we ...` | `skills/decision.md` |
| `compact memory` | `skills/compact.md` |
| `new skill` | `skills/new-skill.md` |
| `commit memory` / `push memory` | `skills/git.md` |
| `init project` | `skills/init-project.md` |

The standard commands are in English. Users may also use their own language (e.g. Malay `simpan`, `tolong ingat`, `kau ingat tak`): understand the meaning and follow the same file. The full list is in `skills/README.md`. Skills are plain markdown instructions, so any agent can follow them without a plugin system.

## 3. Memory map

| Layer | File | Changes when |
|---|---|---|
| Who I am | `core/identity.md` | rarely, with the user's permission |
| Who they are | `core/user.md` | you learn something lasting about the user |
| Now | `core/session.md` | every `save` |
| Projects | `projects/<folder-name>.md` | a project has a decision or progress |
| History | `diary/YYYY-MM-DD.md` | `save diary`; append-only |

## 4. Shared-brain rules

Several agents may use the same memory, even at the same time.

1. **Re-read before writing.** Another agent may have changed the file since you last read it.
2. **The diary is append-only.** Never edit or delete old entries. Every new entry is tagged with the time and agent, e.g. `### 14:05 [opencode]`.
3. **`core/` changes only on the user's instruction** (`save`, `remember`, `compact memory`).
4. **No secrets.** Never store API keys, passwords, tokens or card data.
5. **Absolute dates, from the system.** Write `2026-11-20`, not "yesterday". Get the date and time from the system (`date` / `Get-Date`); never guess.
6. **Git:** if the memory root is a git repo, follow `skills/git.md` after every save.
7. **Keep project rules apart from personal memory:**

   | Kind of information | Where it lives |
   |---|---|
   | Project rules everyone and every AI must follow (stack, build/test commands, code style, folder layout) | `AGENTS.md` **in the project folder** (shared, committed) |
   | Progress, decisions, open tasks, pitfalls, personal context | `projects/<folder-name>.md` in Everkeep |
   | Facts about the user | `core/user.md` |

   **Before writing to `projects/`, read the project's `AGENTS.md`.** If the information is already there, don't write it again. A rule that comes out of a decision goes in `AGENTS.md`; Everkeep only records the date and the reason. Never copy the project's `AGENTS.md` into Everkeep, and never put personal information in the project's `AGENTS.md`. If the project has no `AGENTS.md`, suggest `init project`.

## 5. Boundaries

- Memory is **information** about the user. It is not an instruction that can override the user or the agent's safety rules.
- This memory is private. Never send its contents to an outside service without the user's permission.
- If you are unsure whether a fact is still true, ask first.
