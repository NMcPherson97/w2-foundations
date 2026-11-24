#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
tool_input = payload.get("tool_input", {})
command = str(tool_input.get("command", ""))
normalized = f" {command} "

if " rm " in normalized or command.strip() == "rm" or command.strip().startswith("rm "):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Course hook blocks rm. Use a safer cleanup path or run rm yourself in your own terminal."
        }
    }))

sys.exit(0)