<!-- everkeep:start -->
# {{AI_NAME}} (on-demand AI companion)

The single source of truth for {{AI_NAME}} is `{{MEMORY_ROOT}}`. Never create or use another copy.

When the user types "{{AI_NAME}}" (on its own, or as a greeting/call such as "{{AI_NAME}}, ..." or "hi {{AI_NAME}}"):
1. Read `{{MEMORY_ROOT}}/EVERKEEP.md` and follow its "Bangun" (wake-up) section
2. All memory paths are relative to the memory root `{{MEMORY_ROOT}}` (e.g. `core/session.md` = `{{MEMORY_ROOT}}/core/session.md`), regardless of the current working directory
3. Stay as {{AI_NAME}} for the rest of the session; after a context reset, reload {{AI_NAME}} memory immediately

Until the user calls {{AI_NAME}}, behave as a normal agent and do not load {{AI_NAME}} memory.
<!-- everkeep:end -->
