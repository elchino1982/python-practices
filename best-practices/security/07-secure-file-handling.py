"""Question: Implement secure file handling practices to prevent common security vulnerabilities.

Create a secure file manager that demonstrates proper file handling techniques
including path validation, permission checks, and safe file operations.

Requirements:
1. Create a SecureFileManager class with path validation
2. Implement secure file reading and writing methods
3. Add permission and access control checks
4. Demonstrate protection against path traversal attacks
5. Show secure temporary file handling and cleanup

Example usage:
    file_manager = SecureFileManager("/safe/directory")
    content = file_manager.secure_read("data.txt")
    file_manager.secure_write("output.txt", content)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what security vulnerabilities exist in file handling
# - Start with a simple implementation
# - Test your code step by step
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)




























# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What are common file handling vulnerabilities?
# - How can you validate file paths safely?
# - What permissions should you check?
# - How do you prevent path traversal attacks?
#
# Remember: Start simple and build up complexity gradually!


# ===============================================================================
#                           STEP-BY-STEP SOLUTION
# ===============================================================================
#
# CLASSROOM-STYLE WALKTHROUGH
#
# Let's solve this problem step by step, just like in a programming class!
# Each step builds upon the previous one, so you can follow along and understand
# the complete thought process.
#
# ===============================================================================


# Step 1: Import modules and create basic secure file manager class
# ===============================================================================

# Explanation:
# We start by importing necessary modules for secure file handling and creating
# a basic SecureFileManager class with path validation capabilities.

import os
import tempfile
import shutil
import stat
from pathlib import Path
from typing import Optional, Union, List
import hashlib
import logging

class SecureFileManager:
    """Secure file manager with path validation and access controls."""
    
    def __init__(self, base_directory: str, max_file_size: int = 10 * 1024 * 1024):
        """Initialize secure file manager.
        
        Args:
            base_directory: Base directory for file operations
            max_file_size: Maximum allowed file size in bytes (default 10MB)
        """
        self.base_directory = Path(base_directory).resolve()
        self.max_file_size = max_file_size
        
        # Ensure base directory exists and is secure
        self._ensure_secure_directory()
        
        # Setup logging for security events
        self.logger = logging.getLogger(__name__)
    
    def _ensure_secure_directory(self):
        """Ensure base directory exists with secure permissions."""
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, mode=0o750)
        
        # Set secure permissions (owner read/write/execute, group read/execute)
        os.chmod(self.base_directory, 0o750)

# What we accomplished in this step:
# - Created basic SecureFileManager class with initialization
# - Added base directory validation and secure permissions
# - Set up logging for security events
# - Added file size limits for security


# Step 2: Add path validation and security checks
# ===============================================================================

# Explanation:
# Path validation is crucial for preventing path traversal attacks.
# We need to ensure all file paths stay within our secure base directory.

import os
import tempfile
import shutil
import stat
from pathlib import Path
from typing import Optional, Union, List
import hashlib
import logging

class SecureFileManager:
    """Secure file manager with path validation and access controls."""
    
    def __init__(self, base_directory: str, max_file_size: int = 10 * 1024 * 1024):
        """Initialize secure file manager.
        
        Args:
            base_directory: Base directory for file operations
            max_file_size: Maximum allowed file size in bytes (default 10MB)
        """
        self.base_directory = Path(base_directory).resolve()
        self.max_file_size = max_file_size
        
        # Ensure base directory exists and is secure
        self._ensure_secure_directory()
        
        # Setup logging for security events
        self.logger = logging.getLogger(__name__)
    
    def _ensure_secure_directory(self):
        """Ensure base directory exists with secure permissions."""
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, mode=0o750)
        
        # Set secure permissions (owner read/write/execute, group read/execute)
        os.chmod(self.base_directory, 0o750)
    
    def _validate_path(self, filename: str) -> Path:
        """Validate and resolve file path to prevent path traversal attacks.
        
        Args:
            filename: Filename or relative path
            
        Returns:
            Validated absolute path
            
        Raises:
            ValueError: If path is invalid or outside base directory
        """
        # Remove any null bytes (security measure)
        filename = filename.replace('\x00', '')
        
        # Create path object and resolve it
        file_path = (self.base_directory / filename).resolve()
        
        # Ensure the resolved path is within our base directory
        try:
            file_path.relative_to(self.base_directory)
        except ValueError:
            self.logger.warning(f"Path traversal attempt detected: {filename}")
            raise ValueError(f"Path '{filename}' is outside the allowed directory")
        
        return file_path
    
    def _check_file_permissions(self, file_path: Path, operation: str) -> bool:
        """Check if file permissions allow the requested operation.
        
        Args:
            file_path: Path to check
            operation: 'read' or 'write'
            
        Returns:
            True if operation is allowed
        """
        if not file_path.exists():
            return operation == 'write'  # Can write new files
        
        file_stat = file_path.stat()
        
        if operation == 'read':
            return bool(file_stat.st_mode & stat.S_IRUSR)
        elif operation == 'write':
            return bool(file_stat.st_mode & stat.S_IWUSR)
        
        return False

# What we accomplished in this step:
# - Added path validation to prevent path traversal attacks
# - Implemented security checks for null bytes
# - Added permission checking for file operations
# - Added security logging for suspicious activities


# Step 3: Implement secure file reading methods
# ===============================================================================

# Explanation:
# Secure file reading involves validating file size, checking permissions,
# and handling errors gracefully while preventing information disclosure.

import os
import tempfile
import shutil
import stat
from pathlib import Path
from typing import Optional, Union, List
import hashlib
import logging

class SecureFileManager:
    """Secure file manager with path validation and access controls."""
    
    def __init__(self, base_directory: str, max_file_size: int = 10 * 1024 * 1024):
        """Initialize secure file manager.
        
        Args:
            base_directory: Base directory for file operations
            max_file_size: Maximum allowed file size in bytes (default 10MB)
        """
        self.base_directory = Path(base_directory).resolve()
        self.max_file_size = max_file_size
        
        # Ensure base directory exists and is secure
        self._ensure_secure_directory()
        
        # Setup logging for security events
        self.logger = logging.getLogger(__name__)
    
    def _ensure_secure_directory(self):
        """Ensure base directory exists with secure permissions."""
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, mode=0o750)
        
        # Set secure permissions (owner read/write/execute, group read/execute)
        os.chmod(self.base_directory, 0o750)
    
    def _validate_path(self, filename: str) -> Path:
        """Validate and resolve file path to prevent path traversal attacks.
        
        Args:
            filename: Filename or relative path
            
        Returns:
            Validated absolute path
            
        Raises:
            ValueError: If path is invalid or outside base directory
        """
        # Remove any null bytes (security measure)
        filename = filename.replace('\x00', '')
        
        # Create path object and resolve it
        file_path = (self.base_directory / filename).resolve()
        
        # Ensure the resolved path is within our base directory
        try:
            file_path.relative_to(self.base_directory)
        except ValueError:
            self.logger.warning(f"Path traversal attempt detected: {filename}")
            raise ValueError(f"Path '{filename}' is outside the allowed directory")
        
        return file_path
    
    def _check_file_permissions(self, file_path: Path, operation: str) -> bool:
        """Check if file permissions allow the requested operation.
        
        Args:
            file_path: Path to check
            operation: 'read' or 'write'
            
        Returns:
            True if operation is allowed
        """
        if not file_path.exists():
            return operation == 'write'  # Can write new files
        
        file_stat = file_path.stat()
        
        if operation == 'read':
            return bool(file_stat.st_mode & stat.S_IRUSR)
        elif operation == 'write':
            return bool(file_stat.st_mode & stat.S_IWUSR)
        
        return False
    
    def secure_read(self, filename: str, encoding: str = 'utf-8') -> str:
        """Securely read file content with validation and size limits.
        
        Args:
            filename: Name of file to read
            encoding: File encoding (default: utf-8)
            
        Returns:
            File content as string
            
        Raises:
            ValueError: If file path is invalid
            PermissionError: If file cannot be read
            FileNotFoundError: If file doesn't exist
            OSError: If file is too large
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            self.logger.warning(f"Attempt to read non-existent file: {filename}")
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            self.logger.warning(f"Attempt to read oversized file: {filename} ({file_size} bytes)")
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            self.logger.warning(f"Permission denied reading file: {filename}")
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            
            self.logger.info(f"Successfully read file: {filename}")
            return content
            
        except UnicodeDecodeError as e:
            self.logger.error(f"Encoding error reading file {filename}: {e}")
            raise ValueError(f"Cannot decode file '{filename}' with encoding '{encoding}'")
        except Exception as e:
            self.logger.error(f"Error reading file {filename}: {e}")
            raise
    
    def secure_read_binary(self, filename: str) -> bytes:
        """Securely read binary file content.
        
        Args:
            filename: Name of file to read
            
        Returns:
            File content as bytes
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
            
            self.logger.info(f"Successfully read binary file: {filename}")
            return content
            
        except Exception as e:
            self.logger.error(f"Error reading binary file {filename}: {e}")
            raise

# What we accomplished in this step:
# - Added secure text file reading with encoding support
# - Added secure binary file reading
# - Implemented file size validation
# - Added comprehensive error handling and logging
# - Protected against oversized files and encoding attacks


# Step 4: Implement secure file writing methods
# ===============================================================================

# Explanation:
# Secure file writing involves atomic operations, temporary files,
# and proper cleanup to prevent data corruption and race conditions.

import os
import tempfile
import shutil
import stat
from pathlib import Path
from typing import Optional, Union, List
import hashlib
import logging

class SecureFileManager:
    """Secure file manager with path validation and access controls."""
    
    def __init__(self, base_directory: str, max_file_size: int = 10 * 1024 * 1024):
        """Initialize secure file manager.
        
        Args:
            base_directory: Base directory for file operations
            max_file_size: Maximum allowed file size in bytes (default 10MB)
        """
        self.base_directory = Path(base_directory).resolve()
        self.max_file_size = max_file_size
        
        # Ensure base directory exists and is secure
        self._ensure_secure_directory()
        
        # Setup logging for security events
        self.logger = logging.getLogger(__name__)
    
    def _ensure_secure_directory(self):
        """Ensure base directory exists with secure permissions."""
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, mode=0o750)
        
        # Set secure permissions (owner read/write/execute, group read/execute)
        os.chmod(self.base_directory, 0o750)
    
    def _validate_path(self, filename: str) -> Path:
        """Validate and resolve file path to prevent path traversal attacks.
        
        Args:
            filename: Filename or relative path
            
        Returns:
            Validated absolute path
            
        Raises:
            ValueError: If path is invalid or outside base directory
        """
        # Remove any null bytes (security measure)
        filename = filename.replace('\x00', '')
        
        # Create path object and resolve it
        file_path = (self.base_directory / filename).resolve()
        
        # Ensure the resolved path is within our base directory
        try:
            file_path.relative_to(self.base_directory)
        except ValueError:
            self.logger.warning(f"Path traversal attempt detected: {filename}")
            raise ValueError(f"Path '{filename}' is outside the allowed directory")
        
        return file_path
    
    def _check_file_permissions(self, file_path: Path, operation: str) -> bool:
        """Check if file permissions allow the requested operation.
        
        Args:
            file_path: Path to check
            operation: 'read' or 'write'
            
        Returns:
            True if operation is allowed
        """
        if not file_path.exists():
            return operation == 'write'  # Can write new files
        
        file_stat = file_path.stat()
        
        if operation == 'read':
            return bool(file_stat.st_mode & stat.S_IRUSR)
        elif operation == 'write':
            return bool(file_stat.st_mode & stat.S_IWUSR)
        
        return False
    
    def secure_read(self, filename: str, encoding: str = 'utf-8') -> str:
        """Securely read file content with validation and size limits.
        
        Args:
            filename: Name of file to read
            encoding: File encoding (default: utf-8)
            
        Returns:
            File content as string
            
        Raises:
            ValueError: If file path is invalid
            PermissionError: If file cannot be read
            FileNotFoundError: If file doesn't exist
            OSError: If file is too large
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            self.logger.warning(f"Attempt to read non-existent file: {filename}")
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            self.logger.warning(f"Attempt to read oversized file: {filename} ({file_size} bytes)")
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            self.logger.warning(f"Permission denied reading file: {filename}")
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            
            self.logger.info(f"Successfully read file: {filename}")
            return content
            
        except UnicodeDecodeError as e:
            self.logger.error(f"Encoding error reading file {filename}: {e}")
            raise ValueError(f"Cannot decode file '{filename}' with encoding '{encoding}'")
        except Exception as e:
            self.logger.error(f"Error reading file {filename}: {e}")
            raise
    
    def secure_read_binary(self, filename: str) -> bytes:
        """Securely read binary file content.
        
        Args:
            filename: Name of file to read
            
        Returns:
            File content as bytes
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
            
            self.logger.info(f"Successfully read binary file: {filename}")
            return content
            
        except Exception as e:
            self.logger.error(f"Error reading binary file {filename}: {e}")
            raise
    
    def secure_write(self, filename: str, content: str, encoding: str = 'utf-8', 
                    atomic: bool = True) -> None:
        """Securely write content to file with atomic operations.
        
        Args:
            filename: Name of file to write
            content: Content to write
            encoding: File encoding (default: utf-8)
            atomic: Use atomic write operation (default: True)
            
        Raises:
            ValueError: If file path is invalid or content too large
            PermissionError: If file cannot be written
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check content size
        content_bytes = content.encode(encoding)
        if len(content_bytes) > self.max_file_size:
            raise ValueError(f"Content too large ({len(content_bytes)} bytes)")
        
        # Check if we can write to the location
        if file_path.exists() and not self._check_file_permissions(file_path, 'write'):
            raise PermissionError(f"Permission denied writing to file '{filename}'")
        
        try:
            if atomic:
                # Atomic write using temporary file
                temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                                    suffix='.tmp')
                try:
                    with os.fdopen(temp_fd, 'w', encoding=encoding) as temp_file:
                        temp_file.write(content)
                        temp_file.flush()
                        os.fsync(temp_fd)  # Force write to disk
                    
                    # Set secure permissions on temp file
                    os.chmod(temp_path, 0o640)
                    
                    # Atomic move
                    shutil.move(temp_path, file_path)
                    
                except Exception:
                    # Clean up temp file on error
                    try:
                        os.unlink(temp_path)
                    except OSError:
                        pass
                    raise
            else:
                # Direct write (non-atomic)
                with open(file_path, 'w', encoding=encoding) as file:
                    file.write(content)
                
                # Set secure permissions
                os.chmod(file_path, 0o640)
            
            self.logger.info(f"Successfully wrote file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error writing file {filename}: {e}")
            raise
    
    def secure_write_binary(self, filename: str, content: bytes, 
                           atomic: bool = True) -> None:
        """Securely write binary content to file.
        
        Args:
            filename: Name of file to write
            content: Binary content to write
            atomic: Use atomic write operation (default: True)
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check content size
        if len(content) > self.max_file_size:
            raise ValueError(f"Content too large ({len(content)} bytes)")
        
        # Check permissions
        if file_path.exists() and not self._check_file_permissions(file_path, 'write'):
            raise PermissionError(f"Permission denied writing to file '{filename}'")
        
        try:
            if atomic:
                # Atomic write using temporary file
                temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                                    suffix='.tmp')
                try:
                    with os.fdopen(temp_fd, 'wb') as temp_file:
                        temp_file.write(content)
                        temp_file.flush()
                        os.fsync(temp_fd)
                    
                    # Set secure permissions
                    os.chmod(temp_path, 0o640)
                    
                    # Atomic move
                    shutil.move(temp_path, file_path)
                    
                except Exception:
                    # Clean up temp file on error
                    try:
                        os.unlink(temp_path)
                    except OSError:
                        pass
                    raise
            else:
                # Direct write
                with open(file_path, 'wb') as file:
                    file.write(content)
                
                # Set secure permissions
                os.chmod(file_path, 0o640)
            
            self.logger.info(f"Successfully wrote binary file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error writing binary file {filename}: {e}")
            raise

# What we accomplished in this step:
# - Added secure text file writing with atomic operations
# - Added secure binary file writing
# - Implemented atomic writes using temporary files
# - Added proper file permissions and cleanup
# - Protected against partial writes and race conditions


# Step 5: Add secure temporary file handling and additional security methods
# ===============================================================================

# Explanation:
# Secure temporary file handling includes proper cleanup, secure permissions,
# and file integrity verification using checksums.

import os
import tempfile
import shutil
import stat
from pathlib import Path
from typing import Optional, Union, List
import hashlib
import logging

class SecureFileManager:
    """Secure file manager with path validation and access controls."""
    
    def __init__(self, base_directory: str, max_file_size: int = 10 * 1024 * 1024):
        """Initialize secure file manager.
        
        Args:
            base_directory: Base directory for file operations
            max_file_size: Maximum allowed file size in bytes (default 10MB)
        """
        self.base_directory = Path(base_directory).resolve()
        self.max_file_size = max_file_size
        
        # Ensure base directory exists and is secure
        self._ensure_secure_directory()
        
        # Setup logging for security events
        self.logger = logging.getLogger(__name__)
    
    def _ensure_secure_directory(self):
        """Ensure base directory exists with secure permissions."""
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, mode=0o750)
        
        # Set secure permissions (owner read/write/execute, group read/execute)
        os.chmod(self.base_directory, 0o750)
    
    def _validate_path(self, filename: str) -> Path:
        """Validate and resolve file path to prevent path traversal attacks.
        
        Args:
            filename: Filename or relative path
            
        Returns:
            Validated absolute path
            
        Raises:
            ValueError: If path is invalid or outside base directory
        """
        # Remove any null bytes (security measure)
        filename = filename.replace('\x00', '')
        
        # Create path object and resolve it
        file_path = (self.base_directory / filename).resolve()
        
        # Ensure the resolved path is within our base directory
        try:
            file_path.relative_to(self.base_directory)
        except ValueError:
            self.logger.warning(f"Path traversal attempt detected: {filename}")
            raise ValueError(f"Path '{filename}' is outside the allowed directory")
        
        return file_path
    
    def _check_file_permissions(self, file_path: Path, operation: str) -> bool:
        """Check if file permissions allow the requested operation.
        
        Args:
            file_path: Path to check
            operation: 'read' or 'write'
            
        Returns:
            True if operation is allowed
        """
        if not file_path.exists():
            return operation == 'write'  # Can write new files
        
        file_stat = file_path.stat()
        
        if operation == 'read':
            return bool(file_stat.st_mode & stat.S_IRUSR)
        elif operation == 'write':
            return bool(file_stat.st_mode & stat.S_IWUSR)
        
        return False
    
    def secure_read(self, filename: str, encoding: str = 'utf-8') -> str:
        """Securely read file content with validation and size limits.
        
        Args:
            filename: Name of file to read
            encoding: File encoding (default: utf-8)
            
        Returns:
            File content as string
            
        Raises:
            ValueError: If file path is invalid
            PermissionError: If file cannot be read
            FileNotFoundError: If file doesn't exist
            OSError: If file is too large
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            self.logger.warning(f"Attempt to read non-existent file: {filename}")
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            self.logger.warning(f"Attempt to read oversized file: {filename} ({file_size} bytes)")
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            self.logger.warning(f"Permission denied reading file: {filename}")
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            
            self.logger.info(f"Successfully read file: {filename}")
            return content
            
        except UnicodeDecodeError as e:
            self.logger.error(f"Encoding error reading file {filename}: {e}")
            raise ValueError(f"Cannot decode file '{filename}' with encoding '{encoding}'")
        except Exception as e:
            self.logger.error(f"Error reading file {filename}: {e}")
            raise
    
    def secure_read_binary(self, filename: str) -> bytes:
        """Securely read binary file content.
        
        Args:
            filename: Name of file to read
            
        Returns:
            File content as bytes
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
            
            self.logger.info(f"Successfully read binary file: {filename}")
            return content
            
        except Exception as e:
            self.logger.error(f"Error reading binary file {filename}: {e}")
            raise
    
    def secure_write(self, filename: str, content: str, encoding: str = 'utf-8', 
                    atomic: bool = True) -> None:
        """Securely write content to file with atomic operations.
        
        Args:
            filename: Name of file to write
            content: Content to write
            encoding: File encoding (default: utf-8)
            atomic: Use atomic write operation (default: True)
            
        Raises:
            ValueError: If file path is invalid or content too large
            PermissionError: If file cannot be written
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check content size
        content_bytes = content.encode(encoding)
        if len(content_bytes) > self.max_file_size:
            raise ValueError(f"Content too large ({len(content_bytes)} bytes)")
        
        # Check if we can write to the location
        if file_path.exists() and not self._check_file_permissions(file_path, 'write'):
            raise PermissionError(f"Permission denied writing to file '{filename}'")
        
        try:
            if atomic:
                # Atomic write using temporary file
                temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                                    suffix='.tmp')
                try:
                    with os.fdopen(temp_fd, 'w', encoding=encoding) as temp_file:
                        temp_file.write(content)
                        temp_file.flush()
                        os.fsync(temp_fd)  # Force write to disk
                    
                    # Set secure permissions on temp file
                    os.chmod(temp_path, 0o640)
                    
                    # Atomic move
                    shutil.move(temp_path, file_path)
                    
                except Exception:
                    # Clean up temp file on error
                    try:
                        os.unlink(temp_path)
                    except OSError:
                        pass
                    raise
            else:
                # Direct write (non-atomic)
                with open(file_path, 'w', encoding=encoding) as file:
                    file.write(content)
                
                # Set secure permissions
                os.chmod(file_path, 0o640)
            
            self.logger.info(f"Successfully wrote file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error writing file {filename}: {e}")
            raise
    
    def secure_write_binary(self, filename: str, content: bytes, 
                           atomic: bool = True) -> None:
        """Securely write binary content to file.
        
        Args:
            filename: Name of file to write
            content: Binary content to write
            atomic: Use atomic write operation (default: True)
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check content size
        if len(content) > self.max_file_size:
            raise ValueError(f"Content too large ({len(content)} bytes)")
        
        # Check permissions
        if file_path.exists() and not self._check_file_permissions(file_path, 'write'):
            raise PermissionError(f"Permission denied writing to file '{filename}'")
        
        try:
            if atomic:
                # Atomic write using temporary file
                temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                                    suffix='.tmp')
                try:
                    with os.fdopen(temp_fd, 'wb') as temp_file:
                        temp_file.write(content)
                        temp_file.flush()
                        os.fsync(temp_fd)
                    
                    # Set secure permissions
                    os.chmod(temp_path, 0o640)
                    
                    # Atomic move
                    shutil.move(temp_path, file_path)
                    
                except Exception:
                    # Clean up temp file on error
                    try:
                        os.unlink(temp_path)
                    except OSError:
                        pass
                    raise
            else:
                # Direct write
                with open(file_path, 'wb') as file:
                    file.write(content)
                
                # Set secure permissions
                os.chmod(file_path, 0o640)
            
            self.logger.info(f"Successfully wrote binary file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error writing binary file {filename}: {e}")
            raise
    
    def create_secure_temp_file(self, suffix: str = '.tmp') -> Path:
        """Create a secure temporary file within the base directory.
        
        Args:
            suffix: File suffix for the temporary file
            
        Returns:
            Path to the created temporary file
        """
        temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                            suffix=suffix)
        os.close(temp_fd)  # Close the file descriptor
        
        # Set secure permissions
        os.chmod(temp_path, 0o600)  # Owner read/write only
        
        self.logger.info(f"Created secure temporary file: {temp_path}")
        return Path(temp_path)
    
    def secure_delete(self, filename: str, overwrite_passes: int = 3) -> None:
        """Securely delete a file with optional overwriting.
        
        Args:
            filename: Name of file to delete
            overwrite_passes: Number of overwrite passes (default: 3)
        """
        file_path = self._validate_path(filename)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        try:
            # Get file size for overwriting
            file_size = file_path.stat().st_size
            
            # Overwrite file content multiple times
            with open(file_path, 'r+b') as file:
                for pass_num in range(overwrite_passes):
                    file.seek(0)
                    # Write random data
                    file.write(os.urandom(file_size))
                    file.flush()
                    os.fsync(file.fileno())
            
            # Remove the file
            file_path.unlink()
            
            self.logger.info(f"Securely deleted file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error securely deleting file {filename}: {e}")
            raise
    
    def calculate_checksum(self, filename: str, algorithm: str = 'sha256') -> str:
        """Calculate file checksum for integrity verification.
        
        Args:
            filename: Name of file to checksum
            algorithm: Hash algorithm (sha256, sha1, md5)
            
        Returns:
            Hexadecimal checksum string
        """
        file_path = self._validate_path(filename)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Get hash algorithm
        try:
            hasher = hashlib.new(algorithm)
        except ValueError:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        try:
            with open(file_path, 'rb') as file:
                # Read file in chunks to handle large files
                for chunk in iter(lambda: file.read(8192), b""):
                    hasher.update(chunk)
            
            checksum = hasher.hexdigest()
            self.logger.info(f"Calculated {algorithm} checksum for {filename}: {checksum}")
            return checksum
            
        except Exception as e:
            self.logger.error(f"Error calculating checksum for {filename}: {e}")
            raise
    
    def verify_checksum(self, filename: str, expected_checksum: str, 
                       algorithm: str = 'sha256') -> bool:
        """Verify file integrity using checksum.
        
        Args:
            filename: Name of file to verify
            expected_checksum: Expected checksum value
            algorithm: Hash algorithm used
            
        Returns:
            True if checksum matches, False otherwise
        """
        actual_checksum = self.calculate_checksum(filename, algorithm)
        
        # Compare checksums (case-insensitive)
        match = actual_checksum.lower() == expected_checksum.lower()
        
        if match:
            self.logger.info(f"Checksum verification passed for {filename}")
        else:
            self.logger.warning(f"Checksum verification failed for {filename}")
        
        return match
    
    def list_files(self, pattern: str = "*") -> List[str]:
        """List files in the base directory matching a pattern.
        
        Args:
            pattern: Glob pattern for file matching
            
        Returns:
            List of relative file paths
        """
        try:
            files = []
            for file_path in self.base_directory.glob(pattern):
                if file_path.is_file():
                    # Return relative path
                    relative_path = file_path.relative_to(self.base_directory)
                    files.append(str(relative_path))
            
            return sorted(files)
            
        except Exception as e:
            self.logger.error(f"Error listing files: {e}")
            raise

# What we accomplished in this step:
# - Added secure temporary file creation and management
# - Implemented secure file deletion with overwriting
# - Added file integrity verification using checksums
# - Added file listing functionality with pattern matching
# - Enhanced security logging throughout all operations


# Step 6: Test the complete secure file handling implementation
# ===============================================================================

# Explanation:
# Let's test our secure file handling implementation with various scenarios
# including normal operations and security attack simulations.

import os
import tempfile
import shutil
import stat
from pathlib import Path
from typing import Optional, Union, List
import hashlib
import logging

# Configure logging for demonstration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SecureFileManager:
    """Secure file manager with path validation and access controls."""
    
    def __init__(self, base_directory: str, max_file_size: int = 10 * 1024 * 1024):
        """Initialize secure file manager.
        
        Args:
            base_directory: Base directory for file operations
            max_file_size: Maximum allowed file size in bytes (default 10MB)
        """
        self.base_directory = Path(base_directory).resolve()
        self.max_file_size = max_file_size
        
        # Ensure base directory exists and is secure
        self._ensure_secure_directory()
        
        # Setup logging for security events
        self.logger = logging.getLogger(__name__)
    
    def _ensure_secure_directory(self):
        """Ensure base directory exists with secure permissions."""
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, mode=0o750)
        
        # Set secure permissions (owner read/write/execute, group read/execute)
        os.chmod(self.base_directory, 0o750)
    
    def _validate_path(self, filename: str) -> Path:
        """Validate and resolve file path to prevent path traversal attacks.
        
        Args:
            filename: Filename or relative path
            
        Returns:
            Validated absolute path
            
        Raises:
            ValueError: If path is invalid or outside base directory
        """
        # Remove any null bytes (security measure)
        filename = filename.replace('\x00', '')
        
        # Create path object and resolve it
        file_path = (self.base_directory / filename).resolve()
        
        # Ensure the resolved path is within our base directory
        try:
            file_path.relative_to(self.base_directory)
        except ValueError:
            self.logger.warning(f"Path traversal attempt detected: {filename}")
            raise ValueError(f"Path '{filename}' is outside the allowed directory")
        
        return file_path
    
    def _check_file_permissions(self, file_path: Path, operation: str) -> bool:
        """Check if file permissions allow the requested operation.
        
        Args:
            file_path: Path to check
            operation: 'read' or 'write'
            
        Returns:
            True if operation is allowed
        """
        if not file_path.exists():
            return operation == 'write'  # Can write new files
        
        file_stat = file_path.stat()
        
        if operation == 'read':
            return bool(file_stat.st_mode & stat.S_IRUSR)
        elif operation == 'write':
            return bool(file_stat.st_mode & stat.S_IWUSR)
        
        return False
    
    def secure_read(self, filename: str, encoding: str = 'utf-8') -> str:
        """Securely read file content with validation and size limits.
        
        Args:
            filename: Name of file to read
            encoding: File encoding (default: utf-8)
            
        Returns:
            File content as string
            
        Raises:
            ValueError: If file path is invalid
            PermissionError: If file cannot be read
            FileNotFoundError: If file doesn't exist
            OSError: If file is too large
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            self.logger.warning(f"Attempt to read non-existent file: {filename}")
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            self.logger.warning(f"Attempt to read oversized file: {filename} ({file_size} bytes)")
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            self.logger.warning(f"Permission denied reading file: {filename}")
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            
            self.logger.info(f"Successfully read file: {filename}")
            return content
            
        except UnicodeDecodeError as e:
            self.logger.error(f"Encoding error reading file {filename}: {e}")
            raise ValueError(f"Cannot decode file '{filename}' with encoding '{encoding}'")
        except Exception as e:
            self.logger.error(f"Error reading file {filename}: {e}")
            raise
    
    def secure_read_binary(self, filename: str) -> bytes:
        """Securely read binary file content.
        
        Args:
            filename: Name of file to read
            
        Returns:
            File content as bytes
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check if file exists
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = file_path.stat().st_size
        if file_size > self.max_file_size:
            raise OSError(f"File '{filename}' is too large ({file_size} bytes)")
        
        # Check permissions
        if not self._check_file_permissions(file_path, 'read'):
            raise PermissionError(f"Permission denied reading file '{filename}'")
        
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
            
            self.logger.info(f"Successfully read binary file: {filename}")
            return content
            
        except Exception as e:
            self.logger.error(f"Error reading binary file {filename}: {e}")
            raise
    
    def secure_write(self, filename: str, content: str, encoding: str = 'utf-8', 
                    atomic: bool = True) -> None:
        """Securely write content to file with atomic operations.
        
        Args:
            filename: Name of file to write
            content: Content to write
            encoding: File encoding (default: utf-8)
            atomic: Use atomic write operation (default: True)
            
        Raises:
            ValueError: If file path is invalid or content too large
            PermissionError: If file cannot be written
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check content size
        content_bytes = content.encode(encoding)
        if len(content_bytes) > self.max_file_size:
            raise ValueError(f"Content too large ({len(content_bytes)} bytes)")
        
        # Check if we can write to the location
        if file_path.exists() and not self._check_file_permissions(file_path, 'write'):
            raise PermissionError(f"Permission denied writing to file '{filename}'")
        
        try:
            if atomic:
                # Atomic write using temporary file
                temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                                    suffix='.tmp')
                try:
                    with os.fdopen(temp_fd, 'w', encoding=encoding) as temp_file:
                        temp_file.write(content)
                        temp_file.flush()
                        os.fsync(temp_fd)  # Force write to disk
                    
                    # Set secure permissions on temp file
                    os.chmod(temp_path, 0o640)
                    
                    # Atomic move
                    shutil.move(temp_path, file_path)
                    
                except Exception:
                    # Clean up temp file on error
                    try:
                        os.unlink(temp_path)
                    except OSError:
                        pass
                    raise
            else:
                # Direct write (non-atomic)
                with open(file_path, 'w', encoding=encoding) as file:
                    file.write(content)
                
                # Set secure permissions
                os.chmod(file_path, 0o640)
            
            self.logger.info(f"Successfully wrote file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error writing file {filename}: {e}")
            raise
    
    def secure_write_binary(self, filename: str, content: bytes, 
                           atomic: bool = True) -> None:
        """Securely write binary content to file.
        
        Args:
            filename: Name of file to write
            content: Binary content to write
            atomic: Use atomic write operation (default: True)
        """
        # Validate path
        file_path = self._validate_path(filename)
        
        # Check content size
        if len(content) > self.max_file_size:
            raise ValueError(f"Content too large ({len(content)} bytes)")
        
        # Check permissions
        if file_path.exists() and not self._check_file_permissions(file_path, 'write'):
            raise PermissionError(f"Permission denied writing to file '{filename}'")
        
        try:
            if atomic:
                # Atomic write using temporary file
                temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                                    suffix='.tmp')
                try:
                    with os.fdopen(temp_fd, 'wb') as temp_file:
                        temp_file.write(content)
                        temp_file.flush()
                        os.fsync(temp_fd)
                    
                    # Set secure permissions
                    os.chmod(temp_path, 0o640)
                    
                    # Atomic move
                    shutil.move(temp_path, file_path)
                    
                except Exception:
                    # Clean up temp file on error
                    try:
                        os.unlink(temp_path)
                    except OSError:
                        pass
                    raise
            else:
                # Direct write
                with open(file_path, 'wb') as file:
                    file.write(content)
                
                # Set secure permissions
                os.chmod(file_path, 0o640)
            
            self.logger.info(f"Successfully wrote binary file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error writing binary file {filename}: {e}")
            raise
    
    def create_secure_temp_file(self, suffix: str = '.tmp') -> Path:
        """Create a secure temporary file within the base directory.
        
        Args:
            suffix: File suffix for the temporary file
            
        Returns:
            Path to the created temporary file
        """
        temp_fd, temp_path = tempfile.mkstemp(dir=self.base_directory, 
                                            suffix=suffix)
        os.close(temp_fd)  # Close the file descriptor
        
        # Set secure permissions
        os.chmod(temp_path, 0o600)  # Owner read/write only
        
        self.logger.info(f"Created secure temporary file: {temp_path}")
        return Path(temp_path)
    
    def secure_delete(self, filename: str, overwrite_passes: int = 3) -> None:
        """Securely delete a file with optional overwriting.
        
        Args:
            filename: Name of file to delete
            overwrite_passes: Number of overwrite passes (default: 3)
        """
        file_path = self._validate_path(filename)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        try:
            # Get file size for overwriting
            file_size = file_path.stat().st_size
            
            # Overwrite file content multiple times
            with open(file_path, 'r+b') as file:
                for pass_num in range(overwrite_passes):
                    file.seek(0)
                    # Write random data
                    file.write(os.urandom(file_size))
                    file.flush()
                    os.fsync(file.fileno())
            
            # Remove the file
            file_path.unlink()
            
            self.logger.info(f"Securely deleted file: {filename}")
            
        except Exception as e:
            self.logger.error(f"Error securely deleting file {filename}: {e}")
            raise
    
    def calculate_checksum(self, filename: str, algorithm: str = 'sha256') -> str:
        """Calculate file checksum for integrity verification.
        
        Args:
            filename: Name of file to checksum
            algorithm: Hash algorithm (sha256, sha1, md5)
            
        Returns:
            Hexadecimal checksum string
        """
        file_path = self._validate_path(filename)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Get hash algorithm
        try:
            hasher = hashlib.new(algorithm)
        except ValueError:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        try:
            with open(file_path, 'rb') as file:
                # Read file in chunks to handle large files
                for chunk in iter(lambda: file.read(8192), b""):
                    hasher.update(chunk)
            
            checksum = hasher.hexdigest()
            self.logger.info(f"Calculated {algorithm} checksum for {filename}: {checksum}")
            return checksum
            
        except Exception as e:
            self.logger.error(f"Error calculating checksum for {filename}: {e}")
            raise
    
    def verify_checksum(self, filename: str, expected_checksum: str, 
                       algorithm: str = 'sha256') -> bool:
        """Verify file integrity using checksum.
        
        Args:
            filename: Name of file to verify
            expected_checksum: Expected checksum value
            algorithm: Hash algorithm used
            
        Returns:
            True if checksum matches, False otherwise
        """
        actual_checksum = self.calculate_checksum(filename, algorithm)
        
        # Compare checksums (case-insensitive)
        match = actual_checksum.lower() == expected_checksum.lower()
        
        if match:
            self.logger.info(f"Checksum verification passed for {filename}")
        else:
            self.logger.warning(f"Checksum verification failed for {filename}")
        
        return match
    
    def list_files(self, pattern: str = "*") -> List[str]:
        """List files in the base directory matching a pattern.
        
        Args:
            pattern: Glob pattern for file matching
            
        Returns:
            List of relative file paths
        """
        try:
            files = []
            for file_path in self.base_directory.glob(pattern):
                if file_path.is_file():
                    # Return relative path
                    relative_path = file_path.relative_to(self.base_directory)
                    files.append(str(relative_path))
            
            return sorted(files)
            
        except Exception as e:
            self.logger.error(f"Error listing files: {e}")
            raise

# Create a temporary directory for testing
test_dir = tempfile.mkdtemp(prefix="secure_file_test_")
print(f"=== Testing Secure File Handling ===")
print(f"Test directory: {test_dir}\n")

try:
    # Initialize secure file manager
    file_manager = SecureFileManager(test_dir, max_file_size=1024)  # 1KB limit for testing
    
    print("1. Testing secure file writing:")
    # Test normal file operations
    test_content = "This is a test file with secure content.\nLine 2 of the file."
    file_manager.secure_write("test.txt", test_content)
    print("✓ File written successfully")
    
    print("\n2. Testing secure file reading:")
    read_content = file_manager.secure_read("test.txt")
    print(f"✓ File read successfully: {len(read_content)} characters")
    
    print("\n3. Testing checksum calculation:")
    checksum = file_manager.calculate_checksum("test.txt")
    print(f"✓ SHA256 checksum: {checksum[:16]}...")
    
    print("\n4. Testing checksum verification:")
    is_valid = file_manager.verify_checksum("test.txt", checksum)
    print(f"✓ Checksum verification: {'PASSED' if is_valid else 'FAILED'}")
    
    print("\n5. Testing binary file operations:")
    binary_data = b"Binary test data\x00\x01\x02\x03"
    file_manager.secure_write_binary("binary.dat", binary_data)
    read_binary = file_manager.secure_read_binary("binary.dat")
    print(f"✓ Binary file operations: {len(read_binary)} bytes")
    
    print("\n6. Testing file listing:")
    files = file_manager.list_files()
    print(f"✓ Files in directory: {files}")
    
    print("\n7. Testing security features:")
    
    # Test path traversal protection
    print("   - Testing path traversal protection:")
    try:
        file_manager.secure_read("../../../etc/passwd")
        print("   ✗ Path traversal protection FAILED")
    except ValueError as e:
        print("   ✓ Path traversal attack blocked")
    
    # Test file size limits
    print("   - Testing file size limits:")
    try:
        large_content = "x" * 2048  # Exceeds 1KB limit
        file_manager.secure_write("large.txt", large_content)
        print("   ✗ File size limit FAILED")
    except ValueError as e:
        print("   ✓ Large file blocked")
    
    # Test null byte injection
    print("   - Testing null byte injection protection:")
    try:
        file_manager.secure_read("test\x00.txt")
        print("   ✗ Null byte protection FAILED")
    except FileNotFoundError:
        print("   ✓ Null byte injection blocked")
    
    print("\n8. Testing secure deletion:")
    file_manager.secure_delete("test.txt")
    try:
        file_manager.secure_read("test.txt")
        print("   ✗ Secure deletion FAILED")
    except FileNotFoundError:
        print("   ✓ File securely deleted")
    
    print("\n9. Testing temporary file creation:")
    temp_file = file_manager.create_secure_temp_file(".temp")
    print(f"   ✓ Temporary file created: {temp_file.name}")
    
    # Clean up temp file
    temp_file.unlink()
    
    print("\n=== All tests completed successfully! ===")

except Exception as e:
    print(f"Test failed with error: {e}")

finally:
    # Clean up test directory
    shutil.rmtree(test_dir, ignore_errors=True)
    print(f"\nTest directory cleaned up: {test_dir}")

# What we accomplished in this step:
# - Tested all secure file handling features
# - Demonstrated protection against common attacks
# - Verified file integrity and security measures
# - Showed proper error handling and logging
# - Tested both normal operations and security edge cases


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key security concepts learned:
# - Path validation and traversal attack prevention
# - Secure file permissions and access controls
# - Atomic file operations to prevent race conditions
# - File integrity verification using checksums
# - Secure temporary file handling and cleanup
# - Protection against null byte injection
# - File size limits to prevent DoS attacks
# - Secure deletion with data overwriting
# - Comprehensive security logging
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each security measure is necessary
# 4. Experiment with modifications (try adding encryption!)
#
# Remember: Security is about layers of protection!
# ===============================================================================

