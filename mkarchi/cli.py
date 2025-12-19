import os
import sys
import re

__version__ = "0.1.1"

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

def vide(line):
    for i in line:
        if i != " " and i != "|" and i != "│":
            return False
    return True

def clean(line):
    if "#" in line:
        return line[:line.find("#")].strip()
    return line.strip()

def parse_tree(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    stack = []
    
    for line in lines:
        if not line.strip() or vide(line):
            continue
        
        line = clean(line)
        
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
        
        # Replace forward slashes with hyphens or underscores to avoid path issues
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

def main():
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
        
        if not os.path.exists(structure_file):
            print(f"❌ File not found: {structure_file}")
            sys.exit(1)
        
        print(f"🚀 Creating structure from {structure_file}...\n")
        parse_tree(structure_file)
        print("\n✅ Architecture created successfully!")
    else:
        print(f"Unknown command: {command}")
        print("Try 'mkarchi --help' for more information.")
        sys.exit(1)

if __name__ == "__main__":
    main()