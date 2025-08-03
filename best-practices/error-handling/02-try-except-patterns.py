"""Question: Master try-except patterns for robust error handling in Python.

Learn and implement various try-except patterns including:
- Basic exception handling
- Multiple exception types
- Exception chaining and re-raising
- Custom exception handling
- Resource cleanup patterns
- Logging and error recovery

Requirements:
1. Demonstrate basic try-except patterns
2. Show handling of multiple exception types
3. Implement exception chaining and context
4. Create custom exceptions with proper handling
5. Show resource cleanup with finally blocks
6. Demonstrate logging and error recovery patterns

Example usage:
    result = safe_divide(10, 2)
    data = safe_file_read("config.json")
    user = validate_user_input(user_data)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about different error scenarios
# - Start with simple try-except blocks
# - Consider what exceptions might occur
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
# - What are common exceptions in Python?
# - How do you handle multiple exception types?
# - When should you use finally blocks?
# - How do you create custom exceptions?
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


# Step 1: Basic try-except patterns
# ===============================================================================

# Explanation:
# The most fundamental error handling pattern is the basic try-except block.
# This catches exceptions and allows your program to continue running.

def safe_divide(a, b):
    """Basic try-except pattern for division."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def safe_list_access(lst, index):
    """Basic try-except for list access."""
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

# What we accomplished in this step:
# - Created basic try-except blocks
# - Handled specific exception types (ZeroDivisionError, IndexError)
# - Provided fallback return values


# Step 2: Multiple exception handling patterns
# ===============================================================================

# Explanation:
# Often you need to handle multiple types of exceptions differently.
# Python provides several patterns for this.

def safe_divide(a, b):
    """Basic try-except pattern for division."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def safe_list_access(lst, index):
    """Basic try-except for list access."""
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

def safe_type_conversion(value, target_type):
    """Handle multiple exception types separately."""
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        else:
            raise ValueError(f"Unsupported type: {target_type}")
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

def safe_multiple_exceptions(data):
    """Handle multiple exceptions with tuple syntax."""
    try:
        # This could raise multiple types of exceptions
        result = int(data) / len(data)
        return result
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Multiple exception handler: {type(e).__name__}: {e}")
        return None

def safe_with_catch_all(operation, *args):
    """Pattern with specific and general exception handling."""
    try:
        return operation(*args)
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return None
    except TypeError as e:
        print(f"Type error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None

# What we accomplished in this step:
# - Handled multiple exception types separately
# - Used tuple syntax for grouping exceptions
# - Implemented catch-all exception handling
# - Demonstrated proper exception variable usage


# Step 3: Exception chaining and re-raising patterns
# ===============================================================================

# Explanation:
# Sometimes you need to catch an exception, do some cleanup or logging,
# and then re-raise it or chain it with additional context.

def safe_divide(a, b):
    """Basic try-except pattern for division."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def safe_list_access(lst, index):
    """Basic try-except for list access."""
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

def safe_type_conversion(value, target_type):
    """Handle multiple exception types separately."""
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        else:
            raise ValueError(f"Unsupported type: {target_type}")
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

def safe_multiple_exceptions(data):
    """Handle multiple exceptions with tuple syntax."""
    try:
        # This could raise multiple types of exceptions
        result = int(data) / len(data)
        return result
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Multiple exception handler: {type(e).__name__}: {e}")
        return None

def safe_with_catch_all(operation, *args):
    """Pattern with specific and general exception handling."""
    try:
        return operation(*args)
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return None
    except TypeError as e:
        print(f"Type error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None

def process_data_with_reraise(data):
    """Re-raise exception after logging."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        print(f"Logging error before re-raising: {e}")
        raise  # Re-raise the same exception

def process_data_with_chaining(data):
    """Chain exceptions to preserve context."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        # Chain the original exception with new context
        raise RuntimeError(f"Failed to process data: {data}") from e

def process_data_suppress_context(data):
    """Suppress exception context when raising new exception."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError:
        # Suppress the original exception context
        raise RuntimeError(f"Data processing failed for: {data}") from None

def complex_data_processing(data):
    """Helper function that might raise exceptions."""
    if not data:
        raise ValueError("Data cannot be empty")
    if not isinstance(data, (list, str)):
        raise TypeError("Data must be list or string")
    return len(data)

# What we accomplished in this step:
# - Demonstrated exception re-raising with 'raise'
# - Showed exception chaining with 'raise ... from e'
# - Implemented context suppression with 'raise ... from None'
# - Preserved original exception information while adding context


# Step 4: Custom exceptions and proper handling
# ===============================================================================

# Explanation:
# Custom exceptions make your code more readable and allow for more specific
# error handling. They should inherit from appropriate base exception classes.

# Custom exception classes
class ValidationError(ValueError):
    """Custom exception for validation errors."""
    pass

class ConfigurationError(Exception):
    """Custom exception for configuration errors."""
    def __init__(self, message, config_key=None):
        super().__init__(message)
        self.config_key = config_key

class DatabaseConnectionError(Exception):
    """Custom exception for database connection issues."""
    def __init__(self, message, host=None, port=None):
        super().__init__(message)
        self.host = host
        self.port = port

def safe_divide(a, b):
    """Basic try-except pattern for division."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def safe_list_access(lst, index):
    """Basic try-except for list access."""
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

def safe_type_conversion(value, target_type):
    """Handle multiple exception types separately."""
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        else:
            raise ValueError(f"Unsupported type: {target_type}")
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

def safe_multiple_exceptions(data):
    """Handle multiple exceptions with tuple syntax."""
    try:
        # This could raise multiple types of exceptions
        result = int(data) / len(data)
        return result
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Multiple exception handler: {type(e).__name__}: {e}")
        return None

def safe_with_catch_all(operation, *args):
    """Pattern with specific and general exception handling."""
    try:
        return operation(*args)
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return None
    except TypeError as e:
        print(f"Type error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None

def process_data_with_reraise(data):
    """Re-raise exception after logging."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        print(f"Logging error before re-raising: {e}")
        raise  # Re-raise the same exception

def process_data_with_chaining(data):
    """Chain exceptions to preserve context."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        # Chain the original exception with new context
        raise RuntimeError(f"Failed to process data: {data}") from e

def process_data_suppress_context(data):
    """Suppress exception context when raising new exception."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError:
        # Suppress the original exception context
        raise RuntimeError(f"Data processing failed for: {data}") from None

def complex_data_processing(data):
    """Helper function that might raise exceptions."""
    if not data:
        raise ValueError("Data cannot be empty")
    if not isinstance(data, (list, str)):
        raise TypeError("Data must be list or string")
    return len(data)

def validate_user_input(user_data):
    """Validate user input with custom exceptions."""
    try:
        if not isinstance(user_data, dict):
            raise ValidationError("User data must be a dictionary")
        
        if 'email' not in user_data:
            raise ValidationError("Email is required")
        
        email = user_data['email']
        if '@' not in email:
            raise ValidationError(f"Invalid email format: {email}")
        
        if 'age' in user_data:
            age = int(user_data['age'])
            if age < 0 or age > 150:
                raise ValidationError(f"Invalid age: {age}")
        
        return True
        
    except ValidationError as e:
        print(f"Validation failed: {e}")
        return False
    except ValueError as e:
        raise ValidationError(f"Invalid data type in user input") from e

def load_configuration(config_dict):
    """Load configuration with custom exception handling."""
    try:
        required_keys = ['database_url', 'api_key', 'debug_mode']
        
        for key in required_keys:
            if key not in config_dict:
                raise ConfigurationError(f"Missing required configuration: {key}", config_key=key)
        
        # Validate specific configurations
        if not config_dict['database_url'].startswith(('http://', 'https://')):
            raise ConfigurationError("Database URL must start with http:// or https://", config_key='database_url')
        
        return config_dict
        
    except ConfigurationError as e:
        print(f"Configuration error: {e}")
        if e.config_key:
            print(f"Problem with key: {e.config_key}")
        return None

def connect_to_database(host, port):
    """Simulate database connection with custom exceptions."""
    try:
        if not host:
            raise DatabaseConnectionError("Host cannot be empty", host=host, port=port)
        
        if not isinstance(port, int) or port <= 0:
            raise DatabaseConnectionError(f"Invalid port: {port}", host=host, port=port)
        
        # Simulate connection logic
        if host == "localhost" and port == 5432:
            return "Connected successfully"
        else:
            raise DatabaseConnectionError(f"Cannot connect to {host}:{port}", host=host, port=port)
            
    except DatabaseConnectionError as e:
        print(f"Database connection failed: {e}")
        print(f"Host: {e.host}, Port: {e.port}")
        return None

# What we accomplished in this step:
# - Created custom exception classes with proper inheritance
# - Added custom attributes to exception classes
# - Demonstrated handling of custom exceptions
# - Showed how to chain custom exceptions with built-in ones


# Step 5: Resource cleanup patterns with finally blocks
# ===============================================================================

# Explanation:
# The finally block ensures cleanup code runs regardless of whether
# an exception occurs. This is crucial for resource management.

import os
import json
from contextlib import contextmanager

# Custom exception classes
class ValidationError(ValueError):
    """Custom exception for validation errors."""
    pass

class ConfigurationError(Exception):
    """Custom exception for configuration errors."""
    def __init__(self, message, config_key=None):
        super().__init__(message)
        self.config_key = config_key

class DatabaseConnectionError(Exception):
    """Custom exception for database connection issues."""
    def __init__(self, message, host=None, port=None):
        super().__init__(message)
        self.host = host
        self.port = port

def safe_divide(a, b):
    """Basic try-except pattern for division."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def safe_list_access(lst, index):
    """Basic try-except for list access."""
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

def safe_type_conversion(value, target_type):
    """Handle multiple exception types separately."""
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        else:
            raise ValueError(f"Unsupported type: {target_type}")
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

def safe_multiple_exceptions(data):
    """Handle multiple exceptions with tuple syntax."""
    try:
        # This could raise multiple types of exceptions
        result = int(data) / len(data)
        return result
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Multiple exception handler: {type(e).__name__}: {e}")
        return None

def safe_with_catch_all(operation, *args):
    """Pattern with specific and general exception handling."""
    try:
        return operation(*args)
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return None
    except TypeError as e:
        print(f"Type error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None

def process_data_with_reraise(data):
    """Re-raise exception after logging."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        print(f"Logging error before re-raising: {e}")
        raise  # Re-raise the same exception

def process_data_with_chaining(data):
    """Chain exceptions to preserve context."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        # Chain the original exception with new context
        raise RuntimeError(f"Failed to process data: {data}") from e

def process_data_suppress_context(data):
    """Suppress exception context when raising new exception."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError:
        # Suppress the original exception context
        raise RuntimeError(f"Data processing failed for: {data}") from None

def complex_data_processing(data):
    """Helper function that might raise exceptions."""
    if not data:
        raise ValueError("Data cannot be empty")
    if not isinstance(data, (list, str)):
        raise TypeError("Data must be list or string")
    return len(data)

def validate_user_input(user_data):
    """Validate user input with custom exceptions."""
    try:
        if not isinstance(user_data, dict):
            raise ValidationError("User data must be a dictionary")
        
        if 'email' not in user_data:
            raise ValidationError("Email is required")
        
        email = user_data['email']
        if '@' not in email:
            raise ValidationError(f"Invalid email format: {email}")
        
        if 'age' in user_data:
            age = int(user_data['age'])
            if age < 0 or age > 150:
                raise ValidationError(f"Invalid age: {age}")
        
        return True
        
    except ValidationError as e:
        print(f"Validation failed: {e}")
        return False
    except ValueError as e:
        raise ValidationError(f"Invalid data type in user input") from e

def load_configuration(config_dict):
    """Load configuration with custom exception handling."""
    try:
        required_keys = ['database_url', 'api_key', 'debug_mode']
        
        for key in required_keys:
            if key not in config_dict:
                raise ConfigurationError(f"Missing required configuration: {key}", config_key=key)
        
        # Validate specific configurations
        if not config_dict['database_url'].startswith(('http://', 'https://')):
            raise ConfigurationError("Database URL must start with http:// or https://", config_key='database_url')
        
        return config_dict
        
    except ConfigurationError as e:
        print(f"Configuration error: {e}")
        if e.config_key:
            print(f"Problem with key: {e.config_key}")
        return None

def connect_to_database(host, port):
    """Simulate database connection with custom exceptions."""
    try:
        if not host:
            raise DatabaseConnectionError("Host cannot be empty", host=host, port=port)
        
        if not isinstance(port, int) or port <= 0:
            raise DatabaseConnectionError(f"Invalid port: {port}", host=host, port=port)
        
        # Simulate connection logic
        if host == "localhost" and port == 5432:
            return "Connected successfully"
        else:
            raise DatabaseConnectionError(f"Cannot connect to {host}:{port}", host=host, port=port)
            
    except DatabaseConnectionError as e:
        print(f"Database connection failed: {e}")
        print(f"Host: {e.host}, Port: {e.port}")
        return None

def safe_file_read(filename):
    """File reading with proper resource cleanup."""
    file_handle = None
    try:
        print(f"Opening file: {filename}")
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"Successfully read {len(content)} characters")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return None
    finally:
        if file_handle:
            print(f"Closing file: {filename}")
            file_handle.close()

def safe_json_processing(filename):
    """JSON processing with cleanup and multiple exception handling."""
    file_handle = None
    temp_data = None
    
    try:
        print(f"Starting JSON processing for: {filename}")
        
        # Open and read file
        file_handle = open(filename, 'r')
        raw_content = file_handle.read()
        
        # Parse JSON
        temp_data = json.loads(raw_content)
        
        # Process data (might raise custom exceptions)
        if not isinstance(temp_data, dict):
            raise ValidationError("JSON must contain an object")
        
        # Simulate some processing
        processed_data = {k: v for k, v in temp_data.items() if v is not None}
        
        print(f"Successfully processed JSON with {len(processed_data)} valid items")
        return processed_data
        
    except FileNotFoundError:
        print(f"Error: JSON file '{filename}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{filename}': {e}")
        return None
    except ValidationError as e:
        print(f"Validation error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during JSON processing: {e}")
        return None
    finally:
        # Cleanup resources
        if file_handle:
            print(f"Closing file handle for: {filename}")
            file_handle.close()
        
        if temp_data:
            print("Cleaning up temporary data")
            temp_data.clear()
        
        print("JSON processing cleanup completed")

def database_transaction_simulation():
    """Simulate database transaction with proper cleanup."""
    connection = None
    transaction = None
    
    try:
        print("Starting database transaction")
        
        # Simulate connection
        connection = "database_connection_object"
        print("Database connected")
        
        # Start transaction
        transaction = "transaction_object"
        print("Transaction started")
        
        # Simulate some database operations that might fail
        operations = ["INSERT user", "UPDATE profile", "DELETE old_data"]
        
        for operation in operations:
            print(f"Executing: {operation}")
            if operation == "DELETE old_data":
                # Simulate an error
                raise DatabaseConnectionError("Connection lost during DELETE operation")
        
        # If we get here, commit transaction
        print("All operations successful, committing transaction")
        return True
        
    except DatabaseConnectionError as e:
        print(f"Database error occurred: {e}")
        if transaction:
            print("Rolling back transaction due to error")
        return False
    except Exception as e:
        print(f"Unexpected error in transaction: {e}")
        if transaction:
            print("Rolling back transaction due to unexpected error")
        return False
    finally:
        # Always cleanup resources
        if transaction:
            print("Cleaning up transaction resources")
        
        if connection:
            print("Closing database connection")
        
        print("Database cleanup completed")

@contextmanager
def managed_resource(resource_name):
    """Context manager for resource management (alternative to try-finally)."""
    print(f"Acquiring resource: {resource_name}")
    resource = f"resource_{resource_name}"
    try:
        yield resource
    finally:
        print(f"Releasing resource: {resource_name}")

def use_context_manager_pattern():
    """Demonstrate context manager as alternative to try-finally."""
    try:
        with managed_resource("database") as db:
            print(f"Using resource: {db}")
            # Simulate work that might raise an exception
            if True:  # Change to False to see normal flow
                raise ValueError("Simulated error during resource usage")
            print("Work completed successfully")
    except ValueError as e:
        print(f"Error occurred: {e}")
        print("Resource was still properly cleaned up by context manager")

# What we accomplished in this step:
# - Implemented proper resource cleanup with finally blocks
# - Showed file handling with guaranteed closure
# - Demonstrated transaction-like patterns with rollback
# - Introduced context managers as an alternative to try-finally
# - Ensured resources are always cleaned up regardless of exceptions


# Step 6: Logging and error recovery patterns
# ===============================================================================

# Explanation:
# Proper logging and error recovery make applications more robust and easier
# to debug. This includes retry mechanisms, fallback strategies, and detailed logging.

import os
import json
import logging
import time
from contextlib import contextmanager
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Custom exception classes
class ValidationError(ValueError):
    """Custom exception for validation errors."""
    pass

class ConfigurationError(Exception):
    """Custom exception for configuration errors."""
    def __init__(self, message, config_key=None):
        super().__init__(message)
        self.config_key = config_key

class DatabaseConnectionError(Exception):
    """Custom exception for database connection issues."""
    def __init__(self, message, host=None, port=None):
        super().__init__(message)
        self.host = host
        self.port = port

class RetryableError(Exception):
    """Exception that indicates an operation can be retried."""
    pass

def safe_divide(a, b):
    """Basic try-except pattern for division."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def safe_list_access(lst, index):
    """Basic try-except for list access."""
    try:
        return lst[index]
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None

def safe_type_conversion(value, target_type):
    """Handle multiple exception types separately."""
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        else:
            raise ValueError(f"Unsupported type: {target_type}")
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

def safe_multiple_exceptions(data):
    """Handle multiple exceptions with tuple syntax."""
    try:
        # This could raise multiple types of exceptions
        result = int(data) / len(data)
        return result
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Multiple exception handler: {type(e).__name__}: {e}")
        return None

def safe_with_catch_all(operation, *args):
    """Pattern with specific and general exception handling."""
    try:
        return operation(*args)
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return None
    except TypeError as e:
        print(f"Type error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None

def process_data_with_reraise(data):
    """Re-raise exception after logging."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        print(f"Logging error before re-raising: {e}")
        raise  # Re-raise the same exception

def process_data_with_chaining(data):
    """Chain exceptions to preserve context."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError as e:
        # Chain the original exception with new context
        raise RuntimeError(f"Failed to process data: {data}") from e

def process_data_suppress_context(data):
    """Suppress exception context when raising new exception."""
    try:
        result = complex_data_processing(data)
        return result
    except ValueError:
        # Suppress the original exception context
        raise RuntimeError(f"Data processing failed for: {data}") from None

def complex_data_processing(data):
    """Helper function that might raise exceptions."""
    if not data:
        raise ValueError("Data cannot be empty")
    if not isinstance(data, (list, str)):
        raise TypeError("Data must be list or string")
    return len(data)

def validate_user_input(user_data):
    """Validate user input with custom exceptions."""
    try:
        if not isinstance(user_data, dict):
            raise ValidationError("User data must be a dictionary")
        
        if 'email' not in user_data:
            raise ValidationError("Email is required")
        
        email = user_data['email']
        if '@' not in email:
            raise ValidationError(f"Invalid email format: {email}")
        
        if 'age' in user_data:
            age = int(user_data['age'])
            if age < 0 or age > 150:
                raise ValidationError(f"Invalid age: {age}")
        
        return True
        
    except ValidationError as e:
        print(f"Validation failed: {e}")
        return False
    except ValueError as e:
        raise ValidationError(f"Invalid data type in user input") from e

def load_configuration(config_dict):
    """Load configuration with custom exception handling."""
    try:
        required_keys = ['database_url', 'api_key', 'debug_mode']
        
        for key in required_keys:
            if key not in config_dict:
                raise ConfigurationError(f"Missing required configuration: {key}", config_key=key)
        
        # Validate specific configurations
        if not config_dict['database_url'].startswith(('http://', 'https://')):
            raise ConfigurationError("Database URL must start with http:// or https://", config_key='database_url')
        
        return config_dict
        
    except ConfigurationError as e:
        print(f"Configuration error: {e}")
        if e.config_key:
            print(f"Problem with key: {e.config_key}")
        return None

def connect_to_database(host, port):
    """Simulate database connection with custom exceptions."""
    try:
        if not host:
            raise DatabaseConnectionError("Host cannot be empty", host=host, port=port)
        
        if not isinstance(port, int) or port <= 0:
            raise DatabaseConnectionError(f"Invalid port: {port}", host=host, port=port)
        
        # Simulate connection logic
        if host == "localhost" and port == 5432:
            return "Connected successfully"
        else:
            raise DatabaseConnectionError(f"Cannot connect to {host}:{port}", host=host, port=port)
            
    except DatabaseConnectionError as e:
        print(f"Database connection failed: {e}")
        print(f"Host: {e.host}, Port: {e.port}")
        return None

def safe_file_read(filename):
    """File reading with proper resource cleanup."""
    file_handle = None
    try:
        print(f"Opening file: {filename}")
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"Successfully read {len(content)} characters")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return None
    finally:
        if file_handle:
            print(f"Closing file: {filename}")
            file_handle.close()

def safe_json_processing(filename):
    """JSON processing with cleanup and multiple exception handling."""
    file_handle = None
    temp_data = None
    
    try:
        print(f"Starting JSON processing for: {filename}")
        
        # Open and read file
        file_handle = open(filename, 'r')
        raw_content = file_handle.read()
        
        # Parse JSON
        temp_data = json.loads(raw_content)
        
        # Process data (might raise custom exceptions)
        if not isinstance(temp_data, dict):
            raise ValidationError("JSON must contain an object")
        
        # Simulate some processing
        processed_data = {k: v for k, v in temp_data.items() if v is not None}
        
        print(f"Successfully processed JSON with {len(processed_data)} valid items")
        return processed_data
        
    except FileNotFoundError:
        print(f"Error: JSON file '{filename}' not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{filename}': {e}")
        return None
    except ValidationError as e:
        print(f"Validation error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during JSON processing: {e}")
        return None
    finally:
        # Cleanup resources
        if file_handle:
            print(f"Closing file handle for: {filename}")
            file_handle.close()
        
        if temp_data:
            print("Cleaning up temporary data")
            temp_data.clear()
        
        print("JSON processing cleanup completed")

def database_transaction_simulation():
    """Simulate database transaction with proper cleanup."""
    connection = None
    transaction = None
    
    try:
        print("Starting database transaction")
        
        # Simulate connection
        connection = "database_connection_object"
        print("Database connected")
        
        # Start transaction
        transaction = "transaction_object"
        print("Transaction started")
        
        # Simulate some database operations that might fail
        operations = ["INSERT user", "UPDATE profile", "DELETE old_data"]
        
        for operation in operations:
            print(f"Executing: {operation}")
            if operation == "DELETE old_data":
                # Simulate an error
                raise DatabaseConnectionError("Connection lost during DELETE operation")
        
        # If we get here, commit transaction
        print("All operations successful, committing transaction")
        return True
        
    except DatabaseConnectionError as e:
        print(f"Database error occurred: {e}")
        if transaction:
            print("Rolling back transaction due to error")
        return False
    except Exception as e:
        print(f"Unexpected error in transaction: {e}")
        if transaction:
            print("Rolling back transaction due to unexpected error")
        return False
    finally:
        # Always cleanup resources
        if transaction:
            print("Cleaning up transaction resources")
        
        if connection:
            print("Closing database connection")
        
        print("Database cleanup completed")

@contextmanager
def managed_resource(resource_name):
    """Context manager for resource management (alternative to try-finally)."""
    print(f"Acquiring resource: {resource_name}")
    resource = f"resource_{resource_name}"
    try:
        yield resource
    finally:
        print(f"Releasing resource: {resource_name}")

def use_context_manager_pattern():
    """Demonstrate context manager as alternative to try-finally."""
    try:
        with managed_resource("database") as db:
            print(f"Using resource: {db}")
            # Simulate work that might raise an exception
            if True:  # Change to False to see normal flow
                raise ValueError("Simulated error during resource usage")
            print("Work completed successfully")
    except ValueError as e:
        print(f"Error occurred: {e}")
        print("Resource was still properly cleaned up by context manager")

def retry_decorator(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """Decorator for automatic retry with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            current_delay = delay
            
            while attempt <= max_attempts:
                try:
                    logger.info(f"Attempting {func.__name__} (attempt {attempt}/{max_attempts})")
                    result = func(*args, **kwargs)
                    logger.info(f"Successfully executed {func.__name__} on attempt {attempt}")
                    return result
                    
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}")
                    logger.info(f"Retrying in {current_delay} seconds...")
                    time.sleep(current_delay)
                    
                    attempt += 1
                    current_delay *= backoff
            
            return None
        return wrapper
    return decorator

@retry_decorator(max_attempts=3, delay=0.5, exceptions=(RetryableError, ConnectionError))
def unreliable_network_operation(success_rate=0.3):
    """Simulate an unreliable network operation."""
    import random
    
    if random.random() < success_rate:
        logger.info("Network operation succeeded")
        return "Success"
    else:
        raise RetryableError("Network operation failed")

def robust_data_processing_with_fallbacks(data, fallback_data=None):
    """Data processing with multiple fallback strategies."""
    logger.info(f"Starting robust data processing for: {data}")
    
    # Strategy 1: Try primary processing
    try:
        result = primary_data_processing(data)
        logger.info("Primary processing succeeded")
        return result
    except ValidationError as e:
        logger.warning(f"Primary processing failed with validation error: {e}")
    except Exception as e:
        logger.error(f"Primary processing failed with unexpected error: {e}")
    
    # Strategy 2: Try alternative processing
    try:
        logger.info("Attempting alternative processing")
        result = alternative_data_processing(data)
        logger.info("Alternative processing succeeded")
        return result
    except Exception as e:
        logger.warning(f"Alternative processing failed: {e}")
    
    # Strategy 3: Use fallback data
    if fallback_data is not None:
        try:
            logger.info("Using fallback data")
            result = primary_data_processing(fallback_data)
            logger.info("Fallback processing succeeded")
            return result
        except Exception as e:
            logger.warning(f"Fallback processing failed: {e}")
    
    # Strategy 4: Return safe default
    logger.warning("All processing strategies failed, returning safe default")
    return {"status": "error", "message": "All processing strategies failed", "data": None}

def primary_data_processing(data):
    """Primary data processing that might fail."""
    if not data:
        raise ValidationError("Data cannot be empty")
    if len(str(data)) < 3:
        raise ValidationError("Data too short")
    return {"status": "success", "processed_data": str(data).upper(), "method": "primary"}

def alternative_data_processing(data):
    """Alternative processing method."""
    if not data:
        raise ValueError("No data provided")
    return {"status": "success", "processed_data": str(data).lower(), "method": "alternative"}

def comprehensive_error_logging_example():
    """Demonstrate comprehensive error logging patterns."""
    logger.info("Starting comprehensive error logging example")
    
    test_cases = [
        {"data": "valid_data", "description": "Valid data"},
        {"data": "", "description": "Empty data"},
        {"data": "ab", "description": "Too short data"},
        {"data": None, "description": "None data"},
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        logger.info(f"Test case {i}: {test_case['description']}")
        
        try:
            result = robust_data_processing_with_fallbacks(
                test_case['data'], 
                fallback_data="fallback_data"
            )
            logger.info(f"Test case {i} result: {result}")
            
        except Exception as e:
            logger.error(f"Test case {i} failed completely: {e}", exc_info=True)

def circuit_breaker_pattern():
    """Implement a simple circuit breaker pattern."""
    class CircuitBreaker:
        def __init__(self, failure_threshold=3, timeout=60):
            self.failure_threshold = failure_threshold
            self.timeout = timeout
            self.failure_count = 0
            self.last_failure_time = None
            self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        
        def call(self, func, *args, **kwargs):
            if self.state == "OPEN":
                if time.time() - self.last_failure_time > self.timeout:
                    self.state = "HALF_OPEN"
                    logger.info("Circuit breaker moving to HALF_OPEN state")
                else:
                    raise Exception("Circuit breaker is OPEN")
            
            try:
                result = func(*args, **kwargs)
                if self.state == "HALF_OPEN":
                    self.state = "CLOSED"
                    self.failure_count = 0
                    logger.info("Circuit breaker reset to CLOSED state")
                return result
                
            except Exception as e:
                self.failure_count += 1
                self.last_failure_time = time.time()
                
                if self.failure_count >= self.failure_threshold:
                    self.state = "OPEN"
                    logger.warning(f"Circuit breaker opened after {self.failure_count} failures")
                
                raise
    
    # Example usage
    breaker = CircuitBreaker(failure_threshold=2, timeout=5)
    
    def failing_service():
        import random
        if random.random() < 0.7:  # 70% failure rate
            raise RetryableError("Service unavailable")
        return "Service response"
    
    # Test the circuit breaker
    for i in range(5):
        try:
            result = breaker.call(failing_service)
            logger.info(f"Call {i+1} succeeded: {result}")
        except Exception as e:
            logger.error(f"Call {i+1} failed: {e}")

# What we accomplished in this step:
# - Implemented comprehensive logging with different levels
# - Created retry mechanisms with exponential backoff
# - Demonstrated fallback strategies for error recovery
# - Showed circuit breaker pattern for fault tolerance
# - Provided detailed error context and debugging information

# ===============================================================================
#                           DEMONSTRATION AND TESTING
# ===============================================================================

def demonstrate_all_patterns():
    """Demonstrate all the error handling patterns we've learned."""
    print("\\n" + "="*80)
    print("DEMONSTRATING ALL ERROR HANDLING PATTERNS")
    print("="*80)
    
    # Test basic patterns
    print("\\n1. Basic try-except patterns:")
    print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
    
    # Test multiple exceptions
    print("\\n2. Multiple exception handling:")
    print(f"safe_type_conversion('123', int) = {safe_type_conversion('123', int)}")
    print(f"safe_type_conversion('abc', int) = {safe_type_conversion('abc', int)}")
    
    # Test custom exceptions
    print("\\n3. Custom exception handling:")
    valid_user = {"email": "user@example.com", "age": "25"}
    invalid_user = {"email": "invalid-email", "age": "200"}
    print(f"validate_user_input(valid_user) = {validate_user_input(valid_user)}")
    print(f"validate_user_input(invalid_user) = {validate_user_input(invalid_user)}")
    
    # Test resource cleanup
    print("\\n4. Resource cleanup patterns:")
    use_context_manager_pattern()
    
    # Test retry and recovery
    print("\\n5. Retry and recovery patterns:")
    try:
        result = unreliable_network_operation(success_rate=0.8)
        print(f"Network operation result: {result}")
    except Exception as e:
        print(f"Network operation failed after retries: {e}")
    
    # Test comprehensive error handling
    print("\\n6. Comprehensive error logging:")
    comprehensive_error_logging_example()
    
    print("\\n" + "="*80)
    print("ERROR HANDLING PATTERNS DEMONSTRATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    demonstrate_all_patterns()
