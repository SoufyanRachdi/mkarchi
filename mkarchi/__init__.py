__version__ = "0.1.0"

def show_help():
    help_text = """
mkarchi - Create project structure from tree files

Usage:
    mkarchi apply <structure_file>    Create directories and files from structure file
    mkarchi --help                    Show this help message
    mkarchi --version                 Show version number
    mkarchi -v                        Show version number

Example:
    mkarchi apply structure.txt

Structure file format:
    project/
    ├── src/
    │   ├── main.py
    │   └── utils.py
    ├── README.md
    └── requirements.txt

Note: Directories should end with '/', files should not.
"""
    print(help_text)

def show_version():
    print(f"mkarchi version {__version__}")