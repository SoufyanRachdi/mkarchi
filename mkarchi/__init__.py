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
    │   ├── main.py{
    │   │   print("Hello World")
    │   │   }
    │   └── utils.py
    ├── README.md{
    │   # My Project
    │   This is a sample project.
    │   }
    └── requirements.txt

Note: 
    - Directories should end with '/'
    - Files without content should not have '{}'
    - Files with content should use '{ }' format:
      filename.ext{
          content line 1
          content line 2
          }
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
    current_file_content = []
    current_file_path = None
    collecting_content = False
    content_base_indent = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if we're collecting content
        if collecting_content:
            # Check for closing brace
            if "}" in line:
                # Save the content to file
                if current_file_path and current_file_content:
                    with open(current_file_path, "w", encoding="utf-8") as f:
                        f.write("\n".join(current_file_content))
                        if current_file_content:  # Add final newline if there's content
                            f.write("\n")
                    print(f"📄 Created file with content: {current_file_path}")
                elif current_file_path:
                    # Empty content block
                    with open(current_file_path, "w", encoding="utf-8") as f:
                        pass
                    print(f"📄 Created file: {current_file_path}")
                    
                collecting_content = False
                current_file_content = []
                current_file_path = None
                content_base_indent = 0
                i += 1
                continue
            else:
                # Remove the tree characters and base indentation
                content_line = line
                
                # Find where actual content starts (after tree chars and spaces)
                actual_start = 0
                for idx, char in enumerate(content_line):
                    if char not in (' ', '│', '├', '└', '─', '|'):
                        actual_start = idx
                        break
                else:
                    # Line is only tree chars/spaces, skip it
                    i += 1
                    continue
                
                # If this is the first content line, set base indent
                if not current_file_content:
                    content_base_indent = actual_start
                
                # Remove base indentation and add to content
                if actual_start >= content_base_indent:
                    relative_content = content_line[content_base_indent:].rstrip()
                    current_file_content.append(relative_content)
                else:
                    # Line has less indentation than expected, just take from actual_start
                    current_file_content.append(content_line[actual_start:].rstrip())
                
                i += 1
                continue
        
        if not line.strip() or is_empty_line(line):
            i += 1
            continue
        
        cleaned = clean_line(line)
        
        if not cleaned:
            i += 1
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
                i += 1
                continue
        else:
            level = 0
            name = cleaned
        
        if not name:
            i += 1
            continue
        
        # Check if file has content block
        has_content = False
        if "{" in name:
            has_content = True
            name = name.split("{")[0].strip()
        
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
            
            if has_content:
                # Start collecting content
                collecting_content = True
                current_file_path = path
                current_file_content = []
                content_base_indent = 0
            else:
                # Create empty file
                with open(path, "w"):
                    pass
                print(f"📄 Created file: {path}")
        
        i += 1


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