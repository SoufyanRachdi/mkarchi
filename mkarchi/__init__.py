"""
mkarchi - Create project structure from tree files
"""
import os
import re

__version__ = "0.1.6"

HELP_TEXT = """
mkarchi - Create project structure from tree files

Usage:
    mkarchi apply <structure_file>    Create directories and files from structure file
    mkarchi give [options] [output_file]        Generate structure file from current directory
    mkarchi --help                    Show this help message
    mkarchi --version                 Show version number
    mkarchi -v                        Show version number

Examples:
    mkarchi apply structure.txt       # Create structure from file
    mkarchi give                      # Generate structure.txt with file contents
    mkarchi give -c                   # Generate structure.txt without file contents
    mkarchi give myproject.txt        # Generate myproject.txt with contents
    mkarchi give -c myproject.txt     # Generate myproject.txt without contents

Options for 'give' command:
    -c, --no-content                  Don't include file contents (structure only)

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
            
            # Count the number of │ or | characters before ├ or └ to determine level
            level = 0
            for char in line[:indent]:
                if char in ('│', '|'):
                    level += 1
            
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


def should_ignore(path, name):
    """
    Check if a file or directory should be ignored.
    
    Args:
        path: The full path to check
        name: The name of the file/directory
        
    Returns:
        True if should be ignored, False otherwise
    """
    ignore_patterns = [
        '__pycache__',
        '.git',
        '.gitignore',
        'node_modules',
        '.env',
        '.venv',
        'venv',
        '.pytest_cache',
        '.mypy_cache',
        '__pycache__',
        '*.pyc',
        '*.pyo',
        '*.egg-info',
        'dist',
        'build',
        '.DS_Store',
        'Thumbs.db',
    ]
    
    for pattern in ignore_patterns:
        if pattern.startswith('*.'):
            # Pattern match
            if name.endswith(pattern[1:]):
                return True
        else:
            # Exact match
            if name == pattern:
                return True
    
    return False


def generate_tree(directory=".", prefix="", output_lines=None, is_last=True, base_dir=None, include_content=True):
    """
    Generate a tree structure of the directory in mkarchi format.
    
    Args:
        directory: Directory to scan
        prefix: Prefix for tree drawing
        output_lines: List to collect output lines
        is_last: Whether this is the last item in current level
        base_dir: Base directory for relative paths
        include_content: Whether to include file contents
        
    Returns:
        List of output lines
    """
    if output_lines is None:
        output_lines = []
    
    if base_dir is None:
        base_dir = directory
        # Add root directory name
        root_name = os.path.basename(os.path.abspath(directory))
        if not root_name:
            root_name = "project"
        output_lines.append(f"{root_name}/")
    
    try:
        items = sorted(os.listdir(directory))
        # Filter out ignored items
        items = [item for item in items if not should_ignore(os.path.join(directory, item), item)]
    except PermissionError:
        return output_lines
    
    # Separate directories and files
    dirs = [item for item in items if os.path.isdir(os.path.join(directory, item))]
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
    
    all_items = dirs + files
    
    for i, item in enumerate(all_items):
        is_last_item = (i == len(all_items) - 1)
        item_path = os.path.join(directory, item)
        
        # Determine the connector
        if is_last_item:
            connector = "└─"
            new_prefix = prefix + "   "
        else:
            connector = "├─"
            new_prefix = prefix + "│  "
        
        if os.path.isdir(item_path):
            # Directory
            output_lines.append(f"{prefix}{connector} {item}/")
            generate_tree(item_path, new_prefix, output_lines, is_last_item, base_dir, include_content)
        else:
            # File
            if include_content:
                try:
                    # Try to read file content
                    with open(item_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Only include content for text files under 10KB
                    if len(content) < 10240:
                        output_lines.append(f"{prefix}{connector} {item}(begincontenu)")
                        # Add content with proper indentation
                        for line in content.split('\n'):
                            if line or content:  # Include empty lines
                                output_lines.append(f"{new_prefix}{line}")
                        output_lines.append(f"{new_prefix}(endcontenu)")
                    else:
                        # File too large, skip content
                        output_lines.append(f"{prefix}{connector} {item}")
                except (UnicodeDecodeError, PermissionError):
                    # Binary file or no permission, skip content
                    output_lines.append(f"{prefix}{connector} {item}")
            else:
                output_lines.append(f"{prefix}{connector} {item}")
    
    return output_lines


def give_structure(output_file="structure.txt", include_content=True):
    """
    Generate a structure file from the current directory.
    
    Args:
        output_file: Output file name (default: structure.txt)
        include_content: Whether to include file contents
    """
    print(f"🔍 Scanning current directory...\n")
    
    output_lines = generate_tree(".", include_content=include_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"✅ Structure file created: {output_file}")
    print(f"📊 Total items: {len(output_lines)} lines")
    print(f"\n💡 You can now share this file with ChatGPT or use 'mkarchi apply {output_file}' to recreate the structure.")