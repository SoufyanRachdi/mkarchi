"""
Command-line interface for mkarchi
"""
import sys
import os

# Handle both direct execution and package import
if __name__ == "__main__" and __package__ is None:
    # Direct execution: add parent directory to path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from mkarchi import __version__, HELP_TEXT, apply_structure, give_structure
    from mkarchi.error import handle_cli_error, InvalidArgumentError
else:
    # Package import
    from . import __version__, HELP_TEXT, apply_structure, give_structure
    from .error import handle_cli_error, InvalidArgumentError


def show_help():
    """Display help information."""
    print(HELP_TEXT)


def show_version():
    """Display version number."""
    print(f"mkarchi version {__version__}")


@handle_cli_error
def cmd_apply(args):
    """
    Handle 'apply' command.
    
    Args:
        args: Command arguments
    """
    if len(args) != 1:
        raise InvalidArgumentError("Usage: mkarchi apply <structure_file>")
    
    structure_file = args[0]
    apply_structure(structure_file)


@handle_cli_error
def cmd_give(args):
    """
    Handle 'give' command.
    
    Args:
        args: Command arguments
    """
    # Parse options
    include_content = True
    output_file = "structure.txt"
    max_size_kb = 10  # Default 10 KB
    use_ignore = True  # Default: use ignore patterns
    
    # Parse arguments
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == "-c" or arg == "--no-content":
            include_content = False
        elif arg == "--no-max":
            max_size_kb = float('inf')  # No limit
        elif arg == "--no-ignore":
            use_ignore = False  # Disable all ignore patterns
        elif arg.startswith("-max="):
            try:
                max_size_kb = int(arg.split("=")[1])
                if max_size_kb < 0:
                    raise ValueError("Size must be positive")
            except (ValueError, IndexError):
                raise InvalidArgumentError(
                    f"Invalid max size: {arg}\n   Usage: -max=<size_in_kb> (e.g., -max=100)"
                )
        elif not arg.startswith("-"):
            output_file = arg
        else:
            raise InvalidArgumentError(f"Unknown option: {arg}")
        
        i += 1
    
    give_structure(output_file, include_content, max_size_kb, use_ignore)


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) < 2:
        print("Usage: mkarchi <command> [options]")
        print("Try 'mkarchi --help' for more information.")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "--help":
        show_help()
        sys.exit(0)
    
    if command == "--version" or command == "-v":
        show_version()
        sys.exit(0)
    
    if command == "apply":
        cmd_apply(sys.argv[2:])
    
    elif command == "give":
        cmd_give(sys.argv[2:])
    
    else:
        print(f"❌ Unknown command: {command}")
        print("Try 'mkarchi --help' for more information.")
        sys.exit(1)


if __name__ == "__main__":
    main()