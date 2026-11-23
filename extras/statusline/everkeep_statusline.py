#!/usr/bin/env python3
"""Everkeep status line for Claude Code.

One line, for example:
  🔒 Mira · 💾 12m ago · session 34/150 · diary ✓ · ⬆ 2  |  Sonnet 5.5 · 📁 kedai-kek · ctx 41% · ⎇ main*3 · $0.42

The memory part appears only after the AI companion has been woken in this
session (the transcript has read core/identity.md). It never crashes: any
error falls back to a shorter line.

Claude Code pipes a JSON object on stdin and shows the first line we print.
The memory root is two folders above this file (extras/statusline/..).
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SESSION_LIMIT = 150

RESET, DIM, RED, GREEN, YELLOW, CYAN, MAGENTA = (
    "\033[0m", "\033[2m", "\033[31m", "\033[32m", "\033[33m", "\033[36m", "\033[35m")


def get(d, *keys):
    for k in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def git(cwd, *args):
    try:
        r = subprocess.run(["git", "-C", cwd, *args], capture_output=True, text=True, timeout=2)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def ai_name():
    try:
        with open(os.path.join(ROOT, "EVERKEEP.md"), encoding="utf-8") as f:
            for line in f:
                m = re.match(r"#\s*EVERKEEP:\s*(.+)", line)
                if m:
                    name = m.group(1).strip()
                    return None if "{{" in name else name
    except Exception:
        pass
    return None


def is_awake(transcript):
    """Awake when this session's transcript has read the memory's identity file."""
    if not transcript or not os.path.isfile(transcript):
        return False
    try:
        with open(transcript, "rb") as f:
            data = f.read()
        return b"core/identity.md" in data or b"core\\\\identity.md" in data
    except Exception:
        return False


def ago(seconds):
    m = int(seconds // 60)
    if m < 1:
        return "now"
    if m < 60:
        return f"{m}m ago"
    h = m // 60
    return f"{h}h ago" if h < 48 else f"{h // 24}d ago"


def memory_part(name):
    bits = [f"{MAGENTA}🔒 {name}{RESET}"]

    session = os.path.join(ROOT, "core", "session.md")
    if os.path.isfile(session):
        age = time.time() - os.path.getmtime(session)
        colour = GREEN if age < 3600 else YELLOW if age < 6 * 3600 else RED
        bits.append(f"{colour}💾 {ago(age)}{RESET}")
        try:
            with open(session, encoding="utf-8") as f:
                n = sum(1 for _ in f)
            colour = GREEN if n <= 80 else YELLOW if n <= SESSION_LIMIT else RED
            bits.append(f"{colour}session {n}/{SESSION_LIMIT}{RESET}")
        except Exception:
            pass

    today = time.strftime("%Y-%m-%d")
    if os.path.isfile(os.path.join(ROOT, "diary", f"{today}.md")):
        bits.append(f"{GREEN}diary ✓{RESET}")
    else:
        bits.append(f"{DIM}diary –{RESET}")

    if os.path.isdir(os.path.join(ROOT, ".git")):
        changed = git(ROOT, "status", "--porcelain")
        if changed:
            bits.append(f"{YELLOW}⬆ {len(changed.splitlines())}{RESET}")

    return " · ".join(bits)


def context_pct(data):
    pct = get(data, "context_window", "used_percentage")
    return int(pct) if isinstance(pct, (int, float)) else None


def work_part(data):
    bits = []
    model = get(data, "model", "display_name")
    if model:
        bits.append(f"{CYAN}{model}{RESET}")

    cwd = get(data, "workspace", "current_dir") or data.get("cwd") or os.getcwd()
    folder = os.path.basename(cwd.rstrip("/\\")) or cwd
    bits.append(f"📁 {folder}")

    pct = context_pct(data)
    if pct is not None:
        colour = GREEN if pct < 50 else YELLOW if pct < 80 else RED
        bits.append(f"{colour}ctx {pct}%{RESET}")

    branch = git(cwd, "branch", "--show-current")
    if branch:
        dirty = git(cwd, "status", "--porcelain")
        n = len(dirty.splitlines()) if dirty else 0
        bits.append(f"⎇ {branch}" + (f"{YELLOW}*{n}{RESET}" if n else ""))

    cost = get(data, "cost", "total_cost_usd")
    if isinstance(cost, (int, float)):
        bits.append(f"{DIM}${cost:.2f}{RESET}")

    return " · ".join(bits)


def main():
    for stream in (sys.stdin, sys.stdout):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}

    try:
        work = work_part(data)
    except Exception:
        work = ""

    try:
        name = ai_name()
        memory = memory_part(name) if name and is_awake(data.get("transcript_path")) else ""
    except Exception:
        memory = ""

    print(f"{memory}  {DIM}|{RESET}  {work}" if memory and work else (memory or work or "Everkeep"))


if __name__ == "__main__":
    main()
