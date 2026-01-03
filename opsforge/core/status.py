import json
import os

CONFIG_PATH = os.path.join("opsforge", "storage", "config.json")

def get_status():
    if not os.path.exists(CONFIG_PATH):
        return "OpsForge not initialized"

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    return f"Project: {config['project']} | Version: {config['version']} | Initialized: {config['initialized']}"
