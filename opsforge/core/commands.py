from opsforge.core.health import run_health_check
from opsforge.core.env import get_env_info

def handle_command(args):
    if not args:
        print("No command provided")
        return 1

    command = args[0]
    strict = "--strict" in args
    json_mode = "--json" in args

    if command == "health":
        status, output = run_health_check(json_mode=json_mode, strict=strict)
        print(output)

        if status == "FAIL":
            return 1
        return 0
    elif command == "env":
        info = get_env_info()
        for k, v in info.items():
            print(f"{k}: {v}")
        return 0


    print(f"Unknown command: {command}")
    return 1
