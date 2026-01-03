from core.status import get_status
from core.health import run_health_check
from utils.logger import log

def handle_command(command, flags):
    if command == "status":
        result = get_status()
        log("Executed status command")
        return result

    if command == "health":
        json_mode = "--json" in flags
        result = run_health_check(json_mode=json_mode)
        log(f"Executed health command (json={json_mode})")
        return result

    return "Unknown command"
