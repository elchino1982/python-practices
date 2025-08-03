"""Question: Implement context managers for proper resource cleanup and error handling.

Create context managers that handle file operations, database connections, 
and custom resources with proper cleanup in case of exceptions.

Requirements:
1. Create a file manager context manager
2. Create a database connection context manager
3. Create a custom resource manager with cleanup
4. Demonstrate exception handling within context managers
5. Show proper resource cleanup in all scenarios

Example usage:
    with FileManager('data.txt') as file:
        file.write('Hello World')
    
    with DatabaseManager('db.sqlite') as db:
        db.execute('SELECT * FROM users')
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what classes and methods you need
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
# - What are the __enter__ and __exit__ methods for?
# - How do you handle exceptions in __exit__?
# - What resources need cleanup?
# - How do you ensure cleanup happens even with exceptions?
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


# Step 1: Import modules and create a basic file context manager
# ===============================================================================

# Explanation:
# Context managers use the __enter__ and __exit__ methods to manage resources.
# The __enter__ method sets up the resource, __exit__ cleans it up.

import os
import sqlite3
import tempfile
from typing import Optional, Any

class FileManager:
    """Context manager for file operations with automatic cleanup."""
    
    def __init__(self, filename: str, mode: str = 'w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close the file."""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Return False to propagate exceptions
        return False

# What we accomplished in this step:
# - Created a basic file context manager
# - Implemented __enter__ and __exit__ methods
# - Added automatic file cleanup


# Step 2: Add database connection context manager
# ===============================================================================

# Explanation:
# Database connections also need proper cleanup. We'll create a context manager
# that handles database connections and ensures they're closed properly.

import os
import sqlite3
import tempfile
from typing import Optional, Any

class FileManager:
    """Context manager for file operations with automatic cleanup."""
    
    def __init__(self, filename: str, mode: str = 'w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close the file."""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Return False to propagate exceptions
        return False

class DatabaseManager:
    """Context manager for database connections with automatic cleanup."""
    
    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        """Enter the context - establish database connection."""
        print(f"Connecting to database: {self.database_path}")
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close database connection."""
        if exc_type is None:
            # No exception occurred, commit the transaction
            print("Committing database transaction")
            self.connection.commit()
        else:
            # Exception occurred, rollback the transaction
            print(f"Exception occurred: {exc_value}")
            print("Rolling back database transaction")
            self.connection.rollback()
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            print("Closing database connection")
            self.connection.close()
        
        # Return False to propagate exceptions
        return False
    
    def execute(self, query: str, params: tuple = ()):
        """Execute a database query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.execute(query, params)
    
    def fetchall(self):
        """Fetch all results from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchall()
    
    def fetchone(self):
        """Fetch one result from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchone()

# What we accomplished in this step:
# - Added DatabaseManager context manager
# - Implemented transaction handling (commit/rollback)
# - Added database operation methods
# - Proper cleanup of database resources


# Step 3: Create custom resource manager with advanced cleanup
# ===============================================================================

# Explanation:
# Custom resources might need complex cleanup logic. We'll create a resource
# manager that handles multiple resources and demonstrates advanced cleanup.

import os
import sqlite3
import tempfile
import time
from typing import Optional, Any, List

class FileManager:
    """Context manager for file operations with automatic cleanup."""
    
    def __init__(self, filename: str, mode: str = 'w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close the file."""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Return False to propagate exceptions
        return False

class DatabaseManager:
    """Context manager for database connections with automatic cleanup."""
    
    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        """Enter the context - establish database connection."""
        print(f"Connecting to database: {self.database_path}")
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close database connection."""
        if exc_type is None:
            # No exception occurred, commit the transaction
            print("Committing database transaction")
            self.connection.commit()
        else:
            # Exception occurred, rollback the transaction
            print(f"Exception occurred: {exc_value}")
            print("Rolling back database transaction")
            self.connection.rollback()
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            print("Closing database connection")
            self.connection.close()
        
        # Return False to propagate exceptions
        return False
    
    def execute(self, query: str, params: tuple = ()):
        """Execute a database query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.execute(query, params)
    
    def fetchall(self):
        """Fetch all results from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchall()
    
    def fetchone(self):
        """Fetch one result from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchone()

class CustomResourceManager:
    """Context manager for custom resources with complex cleanup logic."""
    
    def __init__(self, resource_name: str, cleanup_delay: float = 0.1):
        self.resource_name = resource_name
        self.cleanup_delay = cleanup_delay
        self.resources: List[str] = []
        self.is_active = False
        self.start_time = None
    
    def __enter__(self):
        """Enter the context - acquire resources."""
        print(f"Acquiring resource: {self.resource_name}")
        self.start_time = time.time()
        self.is_active = True
        
        # Simulate acquiring multiple sub-resources
        self.resources = [
            f"{self.resource_name}_connection",
            f"{self.resource_name}_buffer",
            f"{self.resource_name}_lock"
        ]
        
        for resource in self.resources:
            print(f"  - Acquired: {resource}")
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - release resources with proper cleanup."""
        duration = time.time() - self.start_time if self.start_time else 0
        
        print(f"Releasing resource: {self.resource_name} (used for {duration:.2f}s)")
        
        if exc_type is not None:
            print(f"Exception during resource usage: {exc_type.__name__}: {exc_value}")
            print("Performing emergency cleanup...")
        
        # Clean up resources in reverse order (LIFO)
        for resource in reversed(self.resources):
            try:
                print(f"  - Releasing: {resource}")
                # Simulate cleanup delay
                time.sleep(self.cleanup_delay)
            except Exception as cleanup_error:
                print(f"  - Error releasing {resource}: {cleanup_error}")
        
        self.is_active = False
        self.resources.clear()
        print(f"Resource cleanup completed: {self.resource_name}")
        
        # Return False to propagate exceptions
        return False
    
    def use_resource(self, operation: str):
        """Simulate using the resource."""
        if not self.is_active:
            raise RuntimeError(f"Resource {self.resource_name} is not active")
        
        print(f"Using {self.resource_name} for: {operation}")
        return f"Result of {operation} on {self.resource_name}"
    
    def get_status(self):
        """Get the current status of the resource."""
        return {
            'name': self.resource_name,
            'active': self.is_active,
            'resources_count': len(self.resources),
            'uptime': time.time() - self.start_time if self.start_time else 0
        }

# What we accomplished in this step:
# - Created CustomResourceManager with complex cleanup logic
# - Added multiple sub-resource management
# - Implemented proper cleanup order (LIFO)
# - Added resource status tracking and timing


# Step 4: Demonstrate context managers with exception handling
# ===============================================================================

# Explanation:
# Let's create demonstration functions that show how context managers handle
# both normal operations and exception scenarios.

import os
import sqlite3
import tempfile
import time
from typing import Optional, Any, List

class FileManager:
    """Context manager for file operations with automatic cleanup."""
    
    def __init__(self, filename: str, mode: str = 'w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close the file."""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Return False to propagate exceptions
        return False

class DatabaseManager:
    """Context manager for database connections with automatic cleanup."""
    
    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        """Enter the context - establish database connection."""
        print(f"Connecting to database: {self.database_path}")
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close database connection."""
        if exc_type is None:
            # No exception occurred, commit the transaction
            print("Committing database transaction")
            self.connection.commit()
        else:
            # Exception occurred, rollback the transaction
            print(f"Exception occurred: {exc_value}")
            print("Rolling back database transaction")
            self.connection.rollback()
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            print("Closing database connection")
            self.connection.close()
        
        # Return False to propagate exceptions
        return False
    
    def execute(self, query: str, params: tuple = ()):
        """Execute a database query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.execute(query, params)
    
    def fetchall(self):
        """Fetch all results from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchall()
    
    def fetchone(self):
        """Fetch one result from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchone()

class CustomResourceManager:
    """Context manager for custom resources with complex cleanup logic."""
    
    def __init__(self, resource_name: str, cleanup_delay: float = 0.1):
        self.resource_name = resource_name
        self.cleanup_delay = cleanup_delay
        self.resources: List[str] = []
        self.is_active = False
        self.start_time = None
    
    def __enter__(self):
        """Enter the context - acquire resources."""
        print(f"Acquiring resource: {self.resource_name}")
        self.start_time = time.time()
        self.is_active = True
        
        # Simulate acquiring multiple sub-resources
        self.resources = [
            f"{self.resource_name}_connection",
            f"{self.resource_name}_buffer",
            f"{self.resource_name}_lock"
        ]
        
        for resource in self.resources:
            print(f"  - Acquired: {resource}")
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - release resources with proper cleanup."""
        duration = time.time() - self.start_time if self.start_time else 0
        
        print(f"Releasing resource: {self.resource_name} (used for {duration:.2f}s)")
        
        if exc_type is not None:
            print(f"Exception during resource usage: {exc_type.__name__}: {exc_value}")
            print("Performing emergency cleanup...")
        
        # Clean up resources in reverse order (LIFO)
        for resource in reversed(self.resources):
            try:
                print(f"  - Releasing: {resource}")
                # Simulate cleanup delay
                time.sleep(self.cleanup_delay)
            except Exception as cleanup_error:
                print(f"  - Error releasing {resource}: {cleanup_error}")
        
        self.is_active = False
        self.resources.clear()
        print(f"Resource cleanup completed: {self.resource_name}")
        
        # Return False to propagate exceptions
        return False
    
    def use_resource(self, operation: str):
        """Simulate using the resource."""
        if not self.is_active:
            raise RuntimeError(f"Resource {self.resource_name} is not active")
        
        print(f"Using {self.resource_name} for: {operation}")
        return f"Result of {operation} on {self.resource_name}"
    
    def get_status(self):
        """Get the current status of the resource."""
        return {
            'name': self.resource_name,
            'active': self.is_active,
            'resources_count': len(self.resources),
            'uptime': time.time() - self.start_time if self.start_time else 0
        }

def demonstrate_file_manager():
    """Demonstrate FileManager with normal and exception scenarios."""
    print("=" * 60)
    print("DEMONSTRATING FILE MANAGER")
    print("=" * 60)
    
    # Normal operation
    print("\n1. Normal file operation:")
    try:
        with FileManager("test_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")
        print("File operation completed successfully")
    except Exception as e:
        print(f"Error: {e}")
    
    # Exception during file operation
    print("\n2. File operation with exception:")
    try:
        with FileManager("test_file2.txt", "w") as file:
            file.write("Starting to write...\n")
            # Simulate an error
            raise ValueError("Simulated error during file operation")
            file.write("This won't be written\n")
    except Exception as e:
        print(f"Caught exception: {e}")
    
    # Clean up test files
    for filename in ["test_file.txt", "test_file2.txt"]:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Cleaned up: {filename}")

def demonstrate_database_manager():
    """Demonstrate DatabaseManager with normal and exception scenarios."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING DATABASE MANAGER")
    print("=" * 60)
    
    db_path = "test_database.db"
    
    # Normal database operation
    print("\n1. Normal database operation:")
    try:
        with DatabaseManager(db_path) as db:
            # Create table
            db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE
                )
            """)
            
            # Insert data
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                      ("Alice", "alice@example.com"))
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                      ("Bob", "bob@example.com"))
            
            # Query data
            db.execute("SELECT * FROM users")
            users = db.fetchall()
            print(f"Users in database: {users}")
        
        print("Database operation completed successfully")
    except Exception as e:
        print(f"Error: {e}")
    
    # Exception during database operation
    print("\n2. Database operation with exception:")
    try:
        with DatabaseManager(db_path) as db:
            # Try to insert duplicate email (should cause rollback)
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                      ("Charlie", "alice@example.com"))  # Duplicate email
    except Exception as e:
        print(f"Caught exception: {e}")
    
    # Verify rollback worked
    print("\n3. Verifying rollback:")
    try:
        with DatabaseManager(db_path) as db:
            db.execute("SELECT COUNT(*) FROM users")
            count = db.fetchone()[0]
            print(f"Number of users after rollback: {count}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Clean up
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Cleaned up: {db_path}")

def demonstrate_custom_resource_manager():
    """Demonstrate CustomResourceManager with normal and exception scenarios."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING CUSTOM RESOURCE MANAGER")
    print("=" * 60)
    
    # Normal resource operation
    print("\n1. Normal resource operation:")
    try:
        with CustomResourceManager("WebService", cleanup_delay=0.05) as resource:
            result1 = resource.use_resource("fetch_data")
            print(f"Operation result: {result1}")
            
            status = resource.get_status()
            print(f"Resource status: {status}")
            
            result2 = resource.use_resource("process_data")
            print(f"Operation result: {result2}")
        
        print("Resource operation completed successfully")
    except Exception as e:
        print(f"Error: {e}")
    
    # Exception during resource operation
    print("\n2. Resource operation with exception:")
    try:
        with CustomResourceManager("APIClient", cleanup_delay=0.05) as resource:
            resource.use_resource("authenticate")
            # Simulate an error
            raise ConnectionError("Network connection lost")
            resource.use_resource("fetch_data")  # This won't execute
    except Exception as e:
        print(f"Caught exception: {e}")

# What we accomplished in this step:
# - Created demonstration functions for all context managers
# - Showed normal operation scenarios
# - Demonstrated exception handling and cleanup
# - Added proper cleanup of test files and databases


# Step 5: Advanced context manager patterns and complete demonstration
# ===============================================================================

# Explanation:
# Let's add advanced patterns like nested context managers, contextlib usage,
# and a complete demonstration that shows all features working together.

import os
import sqlite3
import tempfile
import time
from contextlib import contextmanager, ExitStack
from typing import Optional, Any, List

class FileManager:
    """Context manager for file operations with automatic cleanup."""
    
    def __init__(self, filename: str, mode: str = 'w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter the context - open the file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close the file."""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Return False to propagate exceptions
        return False

class DatabaseManager:
    """Context manager for database connections with automatic cleanup."""
    
    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        """Enter the context - establish database connection."""
        print(f"Connecting to database: {self.database_path}")
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - close database connection."""
        if exc_type is None:
            # No exception occurred, commit the transaction
            print("Committing database transaction")
            self.connection.commit()
        else:
            # Exception occurred, rollback the transaction
            print(f"Exception occurred: {exc_value}")
            print("Rolling back database transaction")
            self.connection.rollback()
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            print("Closing database connection")
            self.connection.close()
        
        # Return False to propagate exceptions
        return False
    
    def execute(self, query: str, params: tuple = ()):
        """Execute a database query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.execute(query, params)
    
    def fetchall(self):
        """Fetch all results from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchall()
    
    def fetchone(self):
        """Fetch one result from the last query."""
        if not self.cursor:
            raise RuntimeError("Database connection not established")
        return self.cursor.fetchone()

class CustomResourceManager:
    """Context manager for custom resources with complex cleanup logic."""
    
    def __init__(self, resource_name: str, cleanup_delay: float = 0.1):
        self.resource_name = resource_name
        self.cleanup_delay = cleanup_delay
        self.resources: List[str] = []
        self.is_active = False
        self.start_time = None
    
    def __enter__(self):
        """Enter the context - acquire resources."""
        print(f"Acquiring resource: {self.resource_name}")
        self.start_time = time.time()
        self.is_active = True
        
        # Simulate acquiring multiple sub-resources
        self.resources = [
            f"{self.resource_name}_connection",
            f"{self.resource_name}_buffer",
            f"{self.resource_name}_lock"
        ]
        
        for resource in self.resources:
            print(f"  - Acquired: {resource}")
        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context - release resources with proper cleanup."""
        duration = time.time() - self.start_time if self.start_time else 0
        
        print(f"Releasing resource: {self.resource_name} (used for {duration:.2f}s)")
        
        if exc_type is not None:
            print(f"Exception during resource usage: {exc_type.__name__}: {exc_value}")
            print("Performing emergency cleanup...")
        
        # Clean up resources in reverse order (LIFO)
        for resource in reversed(self.resources):
            try:
                print(f"  - Releasing: {resource}")
                # Simulate cleanup delay
                time.sleep(self.cleanup_delay)
            except Exception as cleanup_error:
                print(f"  - Error releasing {resource}: {cleanup_error}")
        
        self.is_active = False
        self.resources.clear()
        print(f"Resource cleanup completed: {self.resource_name}")
        
        # Return False to propagate exceptions
        return False
    
    def use_resource(self, operation: str):
        """Simulate using the resource."""
        if not self.is_active:
            raise RuntimeError(f"Resource {self.resource_name} is not active")
        
        print(f"Using {self.resource_name} for: {operation}")
        return f"Result of {operation} on {self.resource_name}"
    
    def get_status(self):
        """Get the current status of the resource."""
        return {
            'name': self.resource_name,
            'active': self.is_active,
            'resources_count': len(self.resources),
            'uptime': time.time() - self.start_time if self.start_time else 0
        }

@contextmanager
def temporary_directory():
    """Context manager using @contextmanager decorator."""
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")
    try:
        yield temp_dir
    finally:
        import shutil
        shutil.rmtree(temp_dir)
        print(f"Cleaned up temporary directory: {temp_dir}")

@contextmanager
def timer_context(operation_name: str):
    """Context manager to time operations."""
    print(f"Starting timer for: {operation_name}")
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        print(f"Operation '{operation_name}' took {duration:.3f} seconds")

def demonstrate_file_manager():
    """Demonstrate FileManager with normal and exception scenarios."""
    print("=" * 60)
    print("DEMONSTRATING FILE MANAGER")
    print("=" * 60)
    
    # Normal operation
    print("\n1. Normal file operation:")
    try:
        with FileManager("test_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is a test file.\n")
        print("File operation completed successfully")
    except Exception as e:
        print(f"Error: {e}")
    
    # Exception during file operation
    print("\n2. File operation with exception:")
    try:
        with FileManager("test_file2.txt", "w") as file:
            file.write("Starting to write...\n")
            # Simulate an error
            raise ValueError("Simulated error during file operation")
            file.write("This won't be written\n")
    except Exception as e:
        print(f"Caught exception: {e}")
    
    # Clean up test files
    for filename in ["test_file.txt", "test_file2.txt"]:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Cleaned up: {filename}")

def demonstrate_database_manager():
    """Demonstrate DatabaseManager with normal and exception scenarios."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING DATABASE MANAGER")
    print("=" * 60)
    
    db_path = "test_database.db"
    
    # Normal database operation
    print("\n1. Normal database operation:")
    try:
        with DatabaseManager(db_path) as db:
            # Create table
            db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE
                )
            """)
            
            # Insert data
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                      ("Alice", "alice@example.com"))
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                      ("Bob", "bob@example.com"))
            
            # Query data
            db.execute("SELECT * FROM users")
            users = db.fetchall()
            print(f"Users in database: {users}")
        
        print("Database operation completed successfully")
    except Exception as e:
        print(f"Error: {e}")
    
    # Exception during database operation
    print("\n2. Database operation with exception:")
    try:
        with DatabaseManager(db_path) as db:
            # Try to insert duplicate email (should cause rollback)
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                      ("Charlie", "alice@example.com"))  # Duplicate email
    except Exception as e:
        print(f"Caught exception: {e}")
    
    # Verify rollback worked
    print("\n3. Verifying rollback:")
    try:
        with DatabaseManager(db_path) as db:
            db.execute("SELECT COUNT(*) FROM users")
            count = db.fetchone()[0]
            print(f"Number of users after rollback: {count}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Clean up
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Cleaned up: {db_path}")

def demonstrate_custom_resource_manager():
    """Demonstrate CustomResourceManager with normal and exception scenarios."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING CUSTOM RESOURCE MANAGER")
    print("=" * 60)
    
    # Normal resource operation
    print("\n1. Normal resource operation:")
    try:
        with CustomResourceManager("WebService", cleanup_delay=0.05) as resource:
            result1 = resource.use_resource("fetch_data")
            print(f"Operation result: {result1}")
            
            status = resource.get_status()
            print(f"Resource status: {status}")
            
            result2 = resource.use_resource("process_data")
            print(f"Operation result: {result2}")
        
        print("Resource operation completed successfully")
    except Exception as e:
        print(f"Error: {e}")
    
    # Exception during resource operation
    print("\n2. Resource operation with exception:")
    try:
        with CustomResourceManager("APIClient", cleanup_delay=0.05) as resource:
            resource.use_resource("authenticate")
            # Simulate an error
            raise ConnectionError("Network connection lost")
            resource.use_resource("fetch_data")  # This won't execute
    except Exception as e:
        print(f"Caught exception: {e}")

def demonstrate_advanced_patterns():
    """Demonstrate advanced context manager patterns."""
    print("\n" + "=" * 60)
    print("DEMONSTRATING ADVANCED PATTERNS")
    print("=" * 60)
    
    # Using @contextmanager decorator
    print("\n1. Using @contextmanager decorator:")
    try:
        with temporary_directory() as temp_dir:
            test_file = os.path.join(temp_dir, "test.txt")
            with open(test_file, "w") as f:
                f.write("Temporary file content")
            print(f"Created file in temporary directory: {test_file}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Using timer context manager
    print("\n2. Using timer context manager:")
    try:
        with timer_context("File processing"):
            with temporary_directory() as temp_dir:
                for i in range(3):
                    filename = os.path.join(temp_dir, f"file_{i}.txt")
                    with open(filename, "w") as f:
                        f.write(f"Content for file {i}")
                    time.sleep(0.1)  # Simulate processing time
    except Exception as e:
        print(f"Error: {e}")
    
    # Nested context managers
    print("\n3. Nested context managers:")
    try:
        with timer_context("Complex operation"):
            with temporary_directory() as temp_dir:
                db_path = os.path.join(temp_dir, "nested_test.db")
                with DatabaseManager(db_path) as db:
                    db.execute("CREATE TABLE test (id INTEGER, value TEXT)")
                    db.execute("INSERT INTO test VALUES (1, 'nested test')")
                    
                    log_file = os.path.join(temp_dir, "operation.log")
                    with FileManager(log_file, "w") as log:
                        log.write("Database operation completed\n")
                        
                        with CustomResourceManager("NestedResource", 0.01) as resource:
                            result = resource.use_resource("final_operation")
                            log.write(f"Resource operation: {result}\n")
    except Exception as e:
        print(f"Error: {e}")
    
    # Using ExitStack for dynamic context managers
    print("\n4. Using ExitStack for dynamic context managers:")
    try:
        with ExitStack() as stack:
            # Add multiple context managers dynamically
            temp_dir = stack.enter_context(temporary_directory())
            timer = stack.enter_context(timer_context("ExitStack demo"))
            
            files = []
            for i in range(2):
                filename = os.path.join(temp_dir, f"dynamic_{i}.txt")
                file_manager = stack.enter_context(FileManager(filename, "w"))
                file_manager.write(f"Dynamic file {i} content\n")
                files.append(filename)
            
            print(f"Created {len(files)} files dynamically")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to demonstrate all context manager patterns."""
    print("CONTEXT MANAGERS FOR RESOURCE CLEANUP AND ERROR HANDLING")
    print("=" * 80)
    print("This demonstration shows various context manager patterns for:")
    print("- Automatic resource cleanup")
    print("- Exception handling")
    print("- Transaction management")
    print("- Advanced patterns with contextlib")
    print("=" * 80)
    
    try:
        # Run all demonstrations
        demonstrate_file_manager()
        demonstrate_database_manager()
        demonstrate_custom_resource_manager()
        demonstrate_advanced_patterns()
        
        print("\n" + "=" * 80)
        print("ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
        print("=" * 80)
        
    except Exception as e:
        print(f"\nUnexpected error in main: {e}")
        import traceback
        traceback.print_exc()

# What we accomplished in this step:
# - Added @contextmanager decorator examples
# - Created timer and temporary directory context managers
# - Demonstrated nested context managers
# - Added ExitStack for dynamic context management
# - Created comprehensive main function

if __name__ == "__main__":
    main()
