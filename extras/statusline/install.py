#!/usr/bin/env python3
"""Install (or remove) the Everkeep status line in Claude Code.

  python install.py            install; refuses to replace a different status line
  python install.py --force    install, replacing any existing status line
  python install.py --remove   remove the Everkeep status line (restores the one --force replaced)

Edits ~/.claude/settings.json in place: keeps every other setting and writes a
backup (settings.json.bak-everkeep) first. Safe to run more than once.
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "everkeep_statusline.py").replace("\\", "/")
PYTHON = sys.executable.replace("\\", "/")
COMMAND = f'"{PYTHON}" -I "{SCRIPT}"'
SETTINGS = os.path.join(os.path.expanduser("~"), ".claude", "settings.json")
PREVIOUS = os.path.join(os.path.expanduser("~"), ".claude", "everkeep-statusline-previous.json")


def load():
    if not os.path.exists(SETTINGS):
        return {}
    try:
        with open(SETTINGS, encoding="utf-8") as f:
            return json.load(f) or {}
    except json.JSONDecodeError:
        sys.exit(f"STOP: {SETTINGS} is not valid JSON. Fix it first; nothing was changed.")


def save(data):
    os.makedirs(os.path.dirname(SETTINGS), exist_ok=True)
    if os.path.exists(SETTINGS):
        shutil.copy2(SETTINGS, SETTINGS + ".bak-everkeep")
    with open(SETTINGS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    args = set(sys.argv[1:])
    data = load()
    current = (data.get("statusLine") or {}).get("command", "")
    ours = "everkeep_statusline.py" in current

    if "--remove" in args:
        if not ours:
            print("OK: The Everkeep status line is not installed. Nothing to do.")
            return
        data.pop("statusLine", None)
        restored = ""
        if os.path.exists(PREVIOUS):
            with open(PREVIOUS, encoding="utf-8") as f:
                data["statusLine"] = json.load(f)
            os.remove(PREVIOUS)
            restored = " Your previous status line was restored."
        save(data)
        print("OK: Everkeep status line removed." + restored + " Backup: settings.json.bak-everkeep")
        return

    if current == COMMAND:
        print("OK: Already installed. Nothing changed.")
        return
    if current and not ours and "--force" not in args:
        print("STOP: Claude Code already has another status line:")
        print(f"    {current}")
        print("  Nothing was changed. Run with --force to replace it (a backup is kept).")
        sys.exit(1)

    if current and not ours:
        with open(PREVIOUS, "w", encoding="utf-8") as f:
            json.dump(data["statusLine"], f, indent=2)
    data["statusLine"] = {"type": "command", "command": COMMAND}
    save(data)
    print(f"OK: Everkeep status line installed:\n    {COMMAND}")
    print("  Open a new Claude Code session to see it. Backup: settings.json.bak-everkeep")


if __name__ == "__main__":
    main()
