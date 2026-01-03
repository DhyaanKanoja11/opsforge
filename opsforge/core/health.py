import os
import json

BASE_PATH = "opsforge"
REQUIRED_DIRS = ["core", "utils", "storage"]
CONFIG_PATH = os.path.join("opsforge", "storage", "config.json")
LOG_PATH = os.path.join("opsforge", "storage", "logs.txt")

def run_health_check(json_mode=False):
    results = []
    status = "OK"

    def add(level, message):
        nonlocal status
        results.append({"level": level, "message": message})
        if level == "FAIL":
            status = "FAIL"
        elif level == "WARN" and status != "FAIL":
            status = "WARN"

    # Directory checks
    for d in REQUIRED_DIRS:
        if os.path.isdir(os.path.join(BASE_PATH, d)):
            add("OK", f"Directory present: {d}")
        else:
            add("FAIL", f"Missing directory: {d}")

    # Config check
    if not os.path.exists(CONFIG_PATH):
        add("FAIL", "config.json missing")
    else:
        try:
            with open(CONFIG_PATH, "r") as f:
                config = json.load(f)
            if not config:
                add("WARN", "config.json is empty")
            else:
                add("OK", "config.json loaded")
        except:
            add("FAIL", "config.json unreadable or invalid")

    # Logs check
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH, "a"):
                pass
            add("OK", "logs.txt writable")
        except:
            add("WARN", "logs.txt not writable")
    else:
        add("WARN", "logs.txt missing")

    if json_mode:
        return json.dumps({
            "status": status,
            "checks": results
        }, indent=2)

    # Human-readable output
    lines = [f"Health Status: {status}"]
    for r in results:
        lines.append(f"[{r['level']}] {r['message']}")

    return "\n".join(lines)
