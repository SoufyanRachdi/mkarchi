"""
mkarchi - Create project structure from tree files
"""
import os
import re

__version__ = "0.1.1"

HELP_TEXT = """
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


def is_empty_line(line):
    """Check if line contains only spaces and tree characters."""
    for char in line:
        if char not in (' ', '|', '│'):
            return False
    return True


def clean_line(line):
    """Remove comments and strip whitespace from line."""
    if "#" in line:
        return line[:line.find("#")].strip()
    return line.strip()


def parse_tree(file_path):
    """
    Parse a tree structure file and create directories and files.
    
    Args:
        file_path: Path to the structure file to parse
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    stack = []
    
    for line in lines:
        if not line.strip() or is_empty_line(line):
            continue
        
        line = clean_line(line)
        
        if not line:
            continue
        
        tree_match = re.search(r'[├└]', line)
        
        if tree_match:
            indent = tree_match.start()
            if indent == 0:
                level = 0
            else:
                level = (indent // 4)
            
            name_match = re.search(r'[├└]\s*─+\s*(.+)', line)
            if name_match:
                name = name_match.group(1).strip()
            else:
                continue
        else:
            level = 0
            name = line.strip()
        
        if not name:
            continue
        
        is_dir = name.endswith("/")
        name = name.rstrip("/")
        
        # Replace forward slashes with hyphens to avoid path issues
        name = name.replace(" / ", "-")
        
        stack = stack[:level + 1]
        stack.append(name)
        path = os.path.join(*stack)
        
        if is_dir:
            os.makedirs(path, exist_ok=True)
            print(f"📁 Created directory: {path}")
        else:
            dir_path = os.path.dirname(path)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
            with open(path, "a"):
                pass
            print(f"📄 Created file: {path}")


def apply_structure(structure_file):
    """
    Apply a structure file to create directories and files.
    
    Args:
        structure_file: Path to the structure file
        
    Raises:
        FileNotFoundError: If the structure file doesn't exist
    """
    if not os.path.exists(structure_file):
        raise FileNotFoundError(f"File not found: {structure_file}")
    
    print(f"🚀 Creating structure from {structure_file}...\n")
    parse_tree(structure_file)
    print("\n✅ Architecture created successfully!")