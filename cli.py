import sys
from core.commands import handle_command

def main():
    if len(sys.argv) < 2:
        print("Usage: opsforge <command>")
        return

    handle_command(sys.argv[1:])

if __name__ == "__main__":
    main()
