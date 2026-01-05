import json
import os

BASE_PATH = os.path.join("opsforge", "storage")
CONFIG_PATH = os.path.join(BASE_PATH, "config.json")
LOG_PATH = os.path.join(BASE_PATH, "logs.txt")

def run_health_check(json_mode=False, strict=False):
    issues = []

    if not os.path.exists(CONFIG_PATH):
        issues.append("config_missing")

    if not os.path.exists(LOG_PATH):
        issues.append("logs_missing")

    if not issues:
        status = "OK"
    elif "config_missing" in issues:
        status = "FAIL"
    else:
        status = "WARN"

    if strict and status != "OK":
        status = "FAIL"

    if json_mode:
        output = json.dumps({
            "status": status,
            "issues": issues
        })
    else:
        output = f"Health status: {status}"

    return status, output
