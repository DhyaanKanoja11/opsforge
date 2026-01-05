import sys
from opsforge.core.commands import handle_command

def main():
    args = sys.argv[1:]
    exit_code = handle_command(args)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
