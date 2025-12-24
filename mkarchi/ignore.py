"""
Ignore pattern handling for mkarchi
"""
import os
import fnmatch


# Built-in ignore patterns (default)
DEFAULT_IGNORE_PATTERNS = [
    '__pycache__',
    '.git',
    '.gitignore',
    'node_modules',
    '.env',
    '.venv',
    'venv',
    '.pytest_cache',
    '.mypy_cache',
    '*.pyc',
    '*.pyo',
    '*.egg-info',
    'dist',
    'build',
    '.DS_Store',
    'Thumbs.db',
]


def load_mkarchiignore(base_path="."):
    """
    Load ignore patterns from .mkarchiignore file.
    
    Args:
        base_path: Base directory to look for .mkarchiignore
        
    Returns:
        List of ignore patterns from the file
    """
    ignore_file = os.path.join(base_path, ".mkarchiignore")
    patterns = []
    
    if not os.path.exists(ignore_file):
        return patterns
    
    try:
        with open(ignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Remove whitespace
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                patterns.append(line)
    except (IOError, PermissionError):
        # If we can't read the file, just continue without it
        pass
    
    return patterns


def get_ignore_patterns(use_defaults=True, use_mkarchiignore=True, base_path="."):
    """
    Get all ignore patterns to use.
    
    Args:
        use_defaults: Whether to include built-in ignore patterns
        use_mkarchiignore: Whether to load .mkarchiignore file
        base_path: Base directory for .mkarchiignore file
        
    Returns:
        List of all ignore patterns to apply
    """
    patterns = []
    
    if use_defaults:
        patterns.extend(DEFAULT_IGNORE_PATTERNS)
    
    if use_mkarchiignore:
        patterns.extend(load_mkarchiignore(base_path))
    
    return patterns


def should_ignore(path, name, ignore_patterns):
    """
    Check if a file or directory should be ignored based on patterns.
    
    Args:
        path: The full path to check
        name: The name of the file/directory
        ignore_patterns: List of patterns to match against
        
    Returns:
        True if should be ignored, False otherwise
    """
    if not ignore_patterns:
        return False
    
    for pattern in ignore_patterns:
        # Remove trailing slash from pattern if present (for directory patterns)
        pattern = pattern.rstrip('/')
        
        # Check for glob pattern (contains * or ?)
        if '*' in pattern or '?' in pattern:
            # Glob match against name only
            if fnmatch.fnmatch(name, pattern):
                return True
        else:
            # Exact match: pattern must match the filename exactly
            if name == pattern:
                return True
    
    return False