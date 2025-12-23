"""
Data constants for mkarchi
"""

__version__ = "0.2.0"

HELP_TEXT = """
mkarchi - Create project structure from tree files

Usage:
    mkarchi apply <structure_file>              Create directories and files from structure file
    mkarchi give [options] [output_file]        Generate structure file from current directory
    mkarchi --help                              Show this help message
    mkarchi --version                           Show version number
    mkarchi -v                                  Show version number

Examples:
    mkarchi apply structure.txt                 # Create structure from file
    mkarchi give                                # Generate structure.txt with file contents (max 10 KB)
    mkarchi give -c                             # Generate structure.txt without file contents
    mkarchi give -max=100                       # Include files up to 100 KB
    mkarchi give -max=50 myproject.txt          # Generate myproject.txt with 50 KB max size
    mkarchi give -c myproject.txt               # Generate myproject.txt without contents

Options for 'give' command:
    -c, --no-content                            Don't include file contents (structure only)
    -max=<size_in_kb>                           Maximum file size in KB to include content (default: 10)

Structure file format:
    project/
    ├── src/
    │   ├── main.py(begincontenu)
    │   │   print("Hello World")
    │   │   (endcontenu)
    │   └── utils.py
    ├── README.md(begincontenu)
    │   # My Project
    │   This is a sample project.
    │   (endcontenu)
    └── requirements.txt

Note: 
    - Directories should end with '/'
    - Files without content should not have markers
    - Files with content should use '(begincontenu)' and '(endcontenu)' markers
    - Files larger than max size will be listed without content
    - Progress bar shows scanning progress during 'give' command
"""


def is_empty_line(line):
    """Check if line contains only spaces and tree characters."""
    for char in line:
        if char not in (' ', '|', '│', '├', '└', '─'):
            return False
    return True


def clean_line(line):
    """Remove comments and strip whitespace from line."""
    if "#" in line:
        return line[:line.find("#")].strip()
    return line.strip()