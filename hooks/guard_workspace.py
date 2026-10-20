#!/usr/bin/env python3
"""PreToolUse guard for Hard Constraint 9: never browse workspace/applications/.

Registered by the plugin (hooks/hooks.json) and, for sessions in this repo
without the plugin loaded, by .claude/settings.json. Reads the hook JSON on stdin
and denies any Bash/Read/Write/Edit/Glob/Grep call that references the
applications/ output tree, unless EVERY reference points inside one concrete
<Company>/<Role> folder (two wildcard-free path segments after "applications").

Allowed:  workspace/applications/Acme/ml-engineer/resume.tex
          ls "workspace/applications/Acme Corp/data-scientist/"
Denied:   ls workspace/applications/
          find workspace/applications -maxdepth 2
          Glob pattern workspace/applications/**
          Read of workspace/applications/<Company>  (company level, no role)

Batch operations across folders belong in engine/scripts/ (e.g.
check_resume.py), which this guard does not inspect the internals of.

Keep this file at hooks/guard_workspace.py: hooks/hooks.json and
.claude/settings.json run it by path before every matched tool call, so
moving or renaming it without updating both first blocks every tool in the
session.
"""

import json
import re
import shlex
import sys

# tool -> which tool_input fields hold paths/commands worth checking.
# Grep's "pattern" is deliberately excluded: searching file CONTENT for the
# word "applications" (e.g. in a SKILL.md) is not a folder access.
FIELDS = {
    "Bash": ["command"],
    "Read": ["file_path"],
    "Write": ["file_path"],
    "Edit": ["file_path"],
    "Glob": ["pattern", "path"],
    "Grep": ["path", "glob"],
}

APPLICATIONS_DIR = "workspace/applications"

# a concrete segment: no glob chars, not empty (spaces allowed for
# companies like "Acme Corp")
SEGMENT = r"[^/*?\[\]{}]+"
APPLICATIONS_REF = re.compile(re.escape(APPLICATIONS_DIR) + r"(?![A-Za-z0-9_-])")
CONCRETE = re.compile(rf"^/{SEGMENT}/{SEGMENT}")


def refs_ok(text: str) -> bool:
    """Every 'applications' path reference must continue with /<Company>/<Role>."""
    for m in APPLICATIONS_REF.finditer(text):
        if not CONCRETE.match(text[m.end():]):
            return False
    return True


def bash_ok(command: str) -> bool:
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        tokens = command.split()
    return all(refs_ok(t) for t in tokens if APPLICATIONS_DIR in t)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input", {}) or {}
    for field in FIELDS.get(tool, []):
        value = tool_input.get(field)
        if not isinstance(value, str) or APPLICATIONS_DIR not in value:
            continue
        ok = bash_ok(value) if tool == "Bash" else refs_ok(value)
        if not ok:
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        "Hard Constraint 9: workspace/applications/ is write-once "
                        "output, not reference material. Access it only via a full "
                        "applications/<Company>/<Role>/ path (no listing, globbing, or "
                        "browsing). If the target is ambiguous, ask the user. Batch "
                        "operations belong in engine/scripts/."
                    ),
                }
            }))
            return


if __name__ == "__main__":
    main()
