# Skill: git

**Triggered by:** finishing `save`, `save diary`, `compact memory`, `log decision`; or the user types `commit memory` / `push memory`
**Scope:** **the memory root repo only** (the folder that contains `EVERKEEP.md`), never any other project's repo

## Steps
1. Check that the memory root is a git repo. If it isn't, stop without any message.
2. Run every command as `git -C <memory root> ...`, whatever the current working directory is.
3. Check `status`. If there is a conflict or anything odd, tell the user and don't commit.
4. `add` the changed files by name. Never run `add -A` blindly.
5. Commit with the message `memory: <short summary> [agent-name]`.
6. **Push only if the user asks** (`push memory`) or has given standing permission.
7. **If the push fails** (e.g. "Repository not found", 403, wrong account): don't retry over and over. Report the error, check the account in `core/user.md` → "Accounts & tools", and suggest pinning the account on the remote (e.g. `https://<account>@github.com/<account>/<repo>.git`). The local commit stays safe.

## Multiple devices
- **Option A, one memory across devices:** one private repo. Before waking up, `git pull --rebase`; after saving, commit + push. Don't use two devices at the same time without pulling first.
- **Option B, a separate memory per device:** each device has its own repo. **Never pull/merge from another device's repo**, or the memories get mixed. Share `skills/` only, one file at a time.
- Ask the user which option during git setup, and record it in `core/user.md` → "Accounts & tools".

## Don't
- Don't commit `.env` files or files that contain secrets.
- Don't use `--force`, `reset --hard` or rewrite history without the user's clear permission.
- Don't push to a public repo. This memory is private.
