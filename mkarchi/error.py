"""
Centralized error handling for mkarchi
"""
import sys


class MkarchiError(Exception):
    """Base exception for all mkarchi errors"""
    def __init__(self, message, tip=None):
        self.message = message
        self.tip = tip
        super().__init__(message)


class FileNotFoundError(MkarchiError):
    """Raised when a structure file is not found"""
    def __init__(self, filepath):
        super().__init__(
            f"File not found: {filepath}",
            "Check that the file path is correct and the file exists."
        )


class InvalidStructureError(MkarchiError):
    """Raised when structure file has invalid syntax"""
    def __init__(self, details=None):
        message = "Invalid structure syntax"
        if details:
            message += f": {details}"
        super().__init__(
            message,
            "Run `mkarchi --help` to learn the correct syntax."
        )


class PermissionError(MkarchiError):
    """Raised when there's a permission issue"""
    def __init__(self, path):
        super().__init__(
            f"Permission denied: {path}",
            "Check that you have the necessary permissions to access this location."
        )


class InvalidArgumentError(MkarchiError):
    """Raised when invalid arguments are provided"""
    def __init__(self, message):
        super().__init__(
            message,
            "Run `mkarchi --help` for usage information."
        )


def display_error(error):
    """
    Display a user-friendly error message.
    
    Args:
        error: MkarchiError instance or generic Exception
    """
    print("\n❌ mkarchi error:")
    
    if isinstance(error, MkarchiError):
        print(f"   {error.message}")
        if error.tip:
            print(f"\n💡 Tip:")
            print(f"   {error.tip}")
    else:
        # Generic error fallback
        print(f"   {str(error)}")
        print(f"\n💡 Tip:")
        print(f"   Run `mkarchi --help` for usage information.")
    
    print()  # Extra newline for readability


def handle_cli_error(func):
    """
    Decorator to catch and display errors in CLI functions.
    
    Args:
        func: Function to wrap
        
    Returns:
        Wrapped function with error handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except MkarchiError as e:
            display_error(e)
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled by user.")
            sys.exit(130)
        except Exception as e:
            # Catch-all for unexpected errors
            display_error(e)
            sys.exit(1)
    
    return wrapper