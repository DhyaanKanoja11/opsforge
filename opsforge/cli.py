import sys
from core.commands import handle_command

def main():
    if len(sys.argv) < 2:
        print("No command provided")
        return

    command = sys.argv[1]
    flags = sys.argv[2:] if len(sys.argv) > 2 else []

    output = handle_command(command, flags)
    print(output)

if __name__ == "__main__":
    main()
