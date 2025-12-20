"""
mkarchi - Create project structure from tree files
"""
import os
import re

__version__ = "0.1.4"

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
    - Files with content should use '(begincontenu)' and '(endcontenu)' markers:
      filename.ext(begincontenu)
          content line 1
          content line 2
          (endcontenu)
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


def extract_content_from_line(line, base_indent):
    """
    Extract content from a line, removing tree characters and base indentation.
    
    Args:
        line: The line to process
        base_indent: The base indentation level to remove
        
    Returns:
        The extracted content, or None if line is empty/only tree chars
    """
    # Find where actual content starts (after tree chars and spaces)
    actual_start = 0
    for idx, char in enumerate(line):
        if char not in (' ', '│', '├', '└', '─', '|'):
            actual_start = idx
            break
    else:
        # Line is only tree chars/spaces
        return None
    
    # Remove base indentation and return content
    if actual_start >= base_indent:
        return line[base_indent:].rstrip()
    else:
        # Line has less indentation than expected
        return line[actual_start:].rstrip()


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
    content_base_indent = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if we're collecting content
        if collecting_content:
            # Check for end marker
            if "(endcontenu)" in line:
                # Save the content to file
                if current_file_path:
                    with open(current_file_path, "w", encoding="utf-8") as f:
                        if current_file_content:
                            f.write("\n".join(current_file_content))
                            f.write("\n")
                    print(f"📄 Created file with content: {current_file_path}")
                    
                collecting_content = False
                current_file_content = []
                current_file_path = None
                content_base_indent = None
                i += 1
                continue
            else:
                # This is a content line
                if content_base_indent is None:
                    # First content line - determine base indent
                    for idx, char in enumerate(line):
                        if char not in (' ', '│', '├', '└', '─', '|'):
                            content_base_indent = idx
                            break
                    
                    if content_base_indent is None:
                        # Empty line
                        i += 1
                        continue
                
                # Extract content
                content = extract_content_from_line(line, content_base_indent)
                if content is not None:
                    current_file_content.append(content)
                elif content is None and line.strip():
                    # Line has some content but was all tree chars - might be blank line in content
                    current_file_content.append("")
                
                i += 1
                continue
        
        # Not collecting content - parse structure
        
        # Skip empty lines or lines with only tree characters
        if not line.strip() or is_empty_line(line):
            i += 1
            continue
        
        cleaned = clean_line(line)
        
        if not cleaned:
            i += 1
            continue
        
        # Look for tree structure markers (├ or └)
        tree_match = re.search(r'[├└]', line)
        
        if tree_match:
            indent = tree_match.start()
            if indent == 0:
                level = 0
            else:
                level = (indent // 4)
            
            # Extract the name after the tree characters
            name_match = re.search(r'[├└]\s*─+\s*(.+)', line)
            if name_match:
                name = name_match.group(1).strip()
            else:
                i += 1
                continue
        else:
            # No tree characters, could be root level
            level = 0
            name = cleaned
        
        # Validate the name - it should have alphanumeric characters
        # Skip if it's just tree characters or symbols
        if not name or not re.search(r'[a-zA-Z0-9_\-.]', name):
            i += 1
            continue
        
        # Check if file has content block
        has_content = False
        if "(begincontenu)" in name:
            has_content = True
            name = name.split("(begincontenu)")[0].strip()
        
        # After splitting, check again if name is valid
        if not name or not re.search(r'[a-zA-Z0-9_\-.]', name):
            i += 1
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
            
            if has_content:
                # Start collecting content
                collecting_content = True
                current_file_path = path
                current_file_content = []
                content_base_indent = None
            else:
                # Create empty file
                with open(path, "w", encoding="utf-8"):
                    pass
                print(f"📄 Created file: {path}")
        
        i += 1
    
    # Handle case where file ends while still collecting content
    if collecting_content and current_file_path:
        with open(current_file_path, "w", encoding="utf-8") as f:
            if current_file_content:
                f.write("\n".join(current_file_content))
                f.write("\n")
        print(f"📄 Created file with content: {current_file_path}")


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