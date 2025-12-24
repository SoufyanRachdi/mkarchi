"""
Data constants for mkarchi
"""

__version__ = "0.1.7"

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
    mkarchi give --no-ignore                    # Include ALL files (ignore nothing)
    mkarchi give --no-ignore -max=100           # Include all files up to 100 KB

Options for 'give' command:
    -c, --no-content                            Don't include file contents (structure only)
    -max=<size_in_kb>                           Maximum file size in KB to include content (default: 10)
    --no-ignore                                 Disable all ignore patterns (built-in + .mkarchiignore)

Ignore patterns:
    By default, mkarchi ignores common files like node_modules, .git, __pycache__, etc.
    
    You can customize this by creating a .mkarchiignore file in your project root:
        # .mkarchiignore example
        node_modules
        .env*
        *.log
        dist
        build
        temp/
    
    Use --no-ignore to disable all ignoring (useful for complete backups).

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