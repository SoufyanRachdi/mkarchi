"""
Command-line interface for mkarchi
"""
import sys
import os

# Handle both direct execution and package import
if __name__ == "__main__" and __package__ is None:
    # Direct execution: add parent directory to path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from mkarchi import __version__, HELP_TEXT, apply_structure
else:
    # Package import
    from . import __version__, HELP_TEXT, apply_structure


def show_help():
    """Display help information."""
    print(HELP_TEXT)


def show_version():
    """Display version number."""
    print(f"mkarchi version {__version__}")


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) < 2:
        print("Usage: mkarchi apply <structure_file>")
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
        if len(sys.argv) != 3:
            print("Usage: mkarchi apply <structure_file>")
            sys.exit(1)
        
        structure_file = sys.argv[2]
        
        try:
            apply_structure(structure_file)
        except FileNotFoundError as e:
            print(f"❌ {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        print(f"Unknown command: {command}")
        print("Try 'mkarchi --help' for more information.")
        sys.exit(1)


if __name__ == "__main__":
    main()