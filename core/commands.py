def handle_command(args):
    command = args[0]

    if command == "init":
        print("OpsForge initialized")
    else:
        print(f"Unknown command: {command}")
