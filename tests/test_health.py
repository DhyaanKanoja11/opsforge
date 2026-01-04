import os
import json
from opsforge.core.health import run_health_check

CONFIG_PATH = os.path.join("opsforge", "storage", "config.json")
LOG_PATH = os.path.join("opsforge", "storage", "logs.txt")

def setup_valid_state():
    os.makedirs("opsforge/storage", exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump({"project": "opsforge"}, f)
    with open(LOG_PATH, "a"):
        pass

def test_health_ok():
    setup_valid_state()
    output = run_health_check(json_mode=True)
    assert '"status": "OK"' in output

def test_health_warn_logs_missing():
    setup_valid_state()
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)
    output = run_health_check(json_mode=True)
    assert '"status": "WARN"' in output

def test_health_fail_config_missing():
    setup_valid_state()
    if os.path.exists(CONFIG_PATH):
        os.remove(CONFIG_PATH)
    output = run_health_check(json_mode=True)
    assert '"status": "FAIL"' in output
