import os
import stat
from pathlib import Path
from typing import List, Union

def create_dockerfile(path: Union[str, os.PathLike], content_lines: List[str]) -> str:
    """
    Create a Dockerfile in the specified directory with the given content.

    Args:
        path: Directory path where the Dockerfile will be created
        content_lines: List of strings representing the Dockerfile content

    Returns:
        str: Success message with the path to the created Dockerfile

    Raises:
        ValueError: If the path is invalid or content is empty
        PermissionError: If there are insufficient permissions
        IOError: If there's an error writing the file
    """
    # Input validation
    if not content_lines:
        raise ValueError("Dockerfile content cannot be empty")

    # Check if all lines are empty or whitespace
    if not any(line.strip() for line in content_lines):
        raise ValueError("Dockerfile content cannot be empty or contain only whitespace")

    # Convert to Path object for better path handling
    path = Path(path).resolve()
    
    # Check if path exists and is a directory
    if not path.exists():
        raise ValueError(f"Directory does not exist: {path}")
    if not path.is_dir():
        raise ValueError(f"Path is not a directory: {path}")

    # Check write permissions
    if not os.access(path, os.W_OK):
        raise PermissionError(f"No write permission in directory: {path}")

    dockerfile_path = path / "Dockerfile"
    
    try:
        # Check if Dockerfile already exists and is not writable
        if dockerfile_path.exists() and not os.access(dockerfile_path, os.W_OK):
            raise PermissionError(f"Cannot overwrite {dockerfile_path}: Permission denied")
            
        # Write content to file with proper error handling
        with open(dockerfile_path, 'w', encoding='utf-8') as f:
            # Remove any empty lines at the end and ensure proper newlines
            content = '\n'.join(line for line in content_lines if line is not None)
            f.write(content)
            
            # Ensure file ends with a newline
            if not content.endswith('\n'):
                f.write('\n')
                
        # Set appropriate permissions (read/write for owner, read for others)
        os.chmod(dockerfile_path, 0o644)
        
        return f"Dockerfile created at: {dockerfile_path}"

    except (IOError, OSError) as e:
        # Clean up partially written file if it exists
        if dockerfile_path.exists():
            try:
                dockerfile_path.unlink()
            except OSError:
                pass  # If we can't delete it, just continue with the original error
        raise IOError(f"Failed to create Dockerfile: {str(e)}")

    except Exception as e:
        # Catch any other unexpected errors
        if dockerfile_path.exists():
            try:
                dockerfile_path.unlink()
            except OSError:
                pass
        raise IOError(f"Unexpected error while creating Dockerfile: {str(e)}")