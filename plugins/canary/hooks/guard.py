import json,sys
d=json.load(sys.stdin); c=d.get("tool_input",{}).get("command","")
if "plugin-canary" in c:
    print(json.dumps({"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"PLUGIN GUARD v3 refused (managed-settings test)"}}))
