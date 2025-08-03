"""Question: Implement exception chaining to preserve error context and create meaningful error traces.

Exception chaining allows you to catch an exception and raise a new one while preserving
the original exception's context. This helps in debugging by showing the complete error chain.

Requirements:
1. Demonstrate basic exception chaining with 'raise ... from ...'
2. Show implicit chaining with nested try-except blocks
3. Create custom exceptions that support chaining
4. Implement error handling in layered applications
5. Show best practices for preserving error context

Example usage:
    try:
        process_data(invalid_data)
    except DataProcessingError as e:
        print(f"Error: {e}")
        print(f"Caused by: {e.__cause__}")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about when and why you need exception chaining
# - Start with simple examples
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
# - What is the difference between 'raise ... from ...' and implicit chaining?
# - How do you preserve the original exception context?
# - When should you chain exceptions vs. when should you suppress them?
# - How can custom exceptions help with error handling?
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


# Step 1: Basic exception chaining with 'raise ... from ...'
# ===============================================================================

# Explanation:
# Exception chaining allows you to raise a new exception while preserving
# the context of the original exception. This is crucial for debugging.

def divide_numbers(a, b):
    """Basic function that might raise an exception."""
    try:
        return a / b
    except ZeroDivisionError as e:
        # Chain the exception with a more descriptive error
        raise ValueError(f"Cannot divide {a} by zero") from e

def demonstrate_basic_chaining():
    """Demonstrate basic exception chaining."""
    print("=== Step 1: Basic Exception Chaining ===")
    
    try:
        result = divide_numbers(10, 0)
    except ValueError as e:
        print(f"Caught exception: {e}")
        print(f"Original cause: {e.__cause__}")
        print(f"Exception type: {type(e.__cause__)}")
        print()

# Test the basic chaining
demonstrate_basic_chaining()

# What we accomplished in this step:
# - Demonstrated explicit exception chaining with 'raise ... from ...'
# - Showed how to access the original exception through __cause__
# - Created a more descriptive error while preserving the original context


# Step 2: Implicit exception chaining
# ===============================================================================

# Explanation:
# When you raise an exception inside an except block without using 'from',
# Python automatically chains the exceptions using __context__.

def divide_numbers(a, b):
    """Basic function that might raise an exception."""
    try:
        return a / b
    except ZeroDivisionError as e:
        # Chain the exception with a more descriptive error
        raise ValueError(f"Cannot divide {a} by zero") from e

def process_division(a, b):
    """Function that demonstrates implicit chaining."""
    try:
        return divide_numbers(a, b)
    except ValueError:
        # This will create implicit chaining
        raise RuntimeError(f"Failed to process division of {a} and {b}")

def demonstrate_implicit_chaining():
    """Demonstrate implicit exception chaining."""
    print("=== Step 2: Implicit Exception Chaining ===")
    
    try:
        result = process_division(10, 0)
    except RuntimeError as e:
        print(f"Caught exception: {e}")
        print(f"Context (implicit): {e.__context__}")
        print(f"Cause (explicit): {e.__cause__}")
        
        # Walk through the exception chain
        current = e
        level = 0
        while current:
            print(f"Level {level}: {type(current).__name__}: {current}")
            current = current.__context__ or current.__cause__
            level += 1
        print()

def demonstrate_basic_chaining():
    """Demonstrate basic exception chaining."""
    print("=== Step 1: Basic Exception Chaining ===")
    
    try:
        result = divide_numbers(10, 0)
    except ValueError as e:
        print(f"Caught exception: {e}")
        print(f"Original cause: {e.__cause__}")
        print(f"Exception type: {type(e.__cause__)}")
        print()

# Test both chaining types
demonstrate_basic_chaining()
demonstrate_implicit_chaining()

# What we accomplished in this step:
# - Demonstrated implicit exception chaining with __context__
# - Showed the difference between __cause__ and __context__
# - Created a function to walk through the exception chain


# Step 3: Custom exceptions with chaining support
# ===============================================================================

# Explanation:
# Custom exceptions can be designed to work well with exception chaining,
# providing better error messages and context preservation.

class DataProcessingError(Exception):
    """Custom exception for data processing errors."""
    
    def __init__(self, message, data=None, operation=None):
        super().__init__(message)
        self.data = data
        self.operation = operation
    
    def __str__(self):
        base_msg = super().__str__()
        if self.operation:
            base_msg = f"[{self.operation}] {base_msg}"
        if self.data is not None:
            base_msg += f" (data: {self.data})"
        return base_msg

class ValidationError(DataProcessingError):
    """Exception for data validation errors."""
    pass

class TransformationError(DataProcessingError):
    """Exception for data transformation errors."""
    pass

def divide_numbers(a, b):
    """Basic function that might raise an exception."""
    try:
        return a / b
    except ZeroDivisionError as e:
        # Chain the exception with a more descriptive error
        raise ValueError(f"Cannot divide {a} by zero") from e

def process_division(a, b):
    """Function that demonstrates implicit chaining."""
    try:
        return divide_numbers(a, b)
    except ValueError:
        # This will create implicit chaining
        raise RuntimeError(f"Failed to process division of {a} and {b}")

def validate_data(data):
    """Validate input data."""
    try:
        if not isinstance(data, (int, float)):
            raise TypeError(f"Expected number, got {type(data).__name__}")
        if data < 0:
            raise ValueError("Number must be non-negative")
        return True
    except (TypeError, ValueError) as e:
        raise ValidationError(
            f"Data validation failed", 
            data=data, 
            operation="validate"
        ) from e

def transform_data(data):
    """Transform data with potential for errors."""
    try:
        # Simulate some complex transformation
        result = data ** 0.5  # Square root
        return result
    except (ValueError, TypeError) as e:
        raise TransformationError(
            f"Failed to transform data",
            data=data,
            operation="square_root"
        ) from e

def demonstrate_custom_exceptions():
    """Demonstrate custom exceptions with chaining."""
    print("=== Step 3: Custom Exceptions with Chaining ===")
    
    test_cases = [-5, "invalid", 16]
    
    for data in test_cases:
        try:
            print(f"Processing data: {data}")
            validate_data(data)
            result = transform_data(data)
            print(f"Result: {result}")
        except DataProcessingError as e:
            print(f"Processing error: {e}")
            print(f"Error type: {type(e).__name__}")
            if e.__cause__:
                print(f"Root cause: {type(e.__cause__).__name__}: {e.__cause__}")
        print()

def demonstrate_implicit_chaining():
    """Demonstrate implicit exception chaining."""
    print("=== Step 2: Implicit Exception Chaining ===")
    
    try:
        result = process_division(10, 0)
    except RuntimeError as e:
        print(f"Caught exception: {e}")
        print(f"Context (implicit): {e.__context__}")
        print(f"Cause (explicit): {e.__cause__}")
        
        # Walk through the exception chain
        current = e
        level = 0
        while current:
            print(f"Level {level}: {type(current).__name__}: {current}")
            current = current.__context__ or current.__cause__
            level += 1
        print()

def demonstrate_basic_chaining():
    """Demonstrate basic exception chaining."""
    print("=== Step 1: Basic Exception Chaining ===")
    
    try:
        result = divide_numbers(10, 0)
    except ValueError as e:
        print(f"Caught exception: {e}")
        print(f"Original cause: {e.__cause__}")
        print(f"Exception type: {type(e.__cause__)}")
        print()

# Test all chaining types
demonstrate_basic_chaining()
demonstrate_implicit_chaining()
demonstrate_custom_exceptions()

# What we accomplished in this step:
# - Created custom exception classes with additional context
# - Demonstrated how custom exceptions work with chaining
# - Showed how to preserve operation and data context in exceptions


# Step 4: Layered application error handling
# ===============================================================================

# Explanation:
# In layered applications, each layer should handle errors appropriately
# and chain them with context relevant to that layer.

import json
from typing import Dict, Any

# Database layer exceptions
class DatabaseError(Exception):
    """Base exception for database operations."""
    pass

class ConnectionError(DatabaseError):
    """Database connection error."""
    pass

class QueryError(DatabaseError):
    """Database query error."""
    pass

# Service layer exceptions
class ServiceError(Exception):
    """Base exception for service layer."""
    pass

class UserNotFoundError(ServiceError):
    """User not found error."""
    pass

class InvalidUserDataError(ServiceError):
    """Invalid user data error."""
    pass

# API layer exceptions
class APIError(Exception):
    """Base exception for API layer."""
    pass

class BadRequestError(APIError):
    """Bad request error."""
    pass

class InternalServerError(APIError):
    """Internal server error."""
    pass

class DataProcessingError(Exception):
    """Custom exception for data processing errors."""
    
    def __init__(self, message, data=None, operation=None):
        super().__init__(message)
        self.data = data
        self.operation = operation
    
    def __str__(self):
        base_msg = super().__str__()
        if self.operation:
            base_msg = f"[{self.operation}] {base_msg}"
        if self.data is not None:
            base_msg += f" (data: {self.data})"
        return base_msg

class ValidationError(DataProcessingError):
    """Exception for data validation errors."""
    pass

class TransformationError(DataProcessingError):
    """Exception for data transformation errors."""
    pass

# Database layer simulation
class DatabaseLayer:
    """Simulated database layer."""
    
    def __init__(self):
        self.connected = False
        self.users = {
            1: {"name": "Alice", "email": "alice@example.com"},
            2: {"name": "Bob", "email": "bob@example.com"}
        }
    
    def connect(self):
        """Simulate database connection."""
        try:
            # Simulate connection failure
            if not self.connected:
                raise OSError("Connection refused")
            return True
        except OSError as e:
            raise ConnectionError("Failed to connect to database") from e
    
    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Get user from database."""
        try:
            if user_id not in self.users:
                raise KeyError(f"User {user_id} not found")
            return self.users[user_id]
        except KeyError as e:
            raise QueryError(f"Database query failed for user {user_id}") from e

# Service layer
class UserService:
    """User service layer."""
    
    def __init__(self, db: DatabaseLayer):
        self.db = db
    
    def get_user_profile(self, user_id: int) -> Dict[str, Any]:
        """Get user profile with validation."""
        try:
            # Validate input
            if not isinstance(user_id, int) or user_id <= 0:
                raise ValueError(f"Invalid user ID: {user_id}")
            
            # Get user from database
            user_data = self.db.get_user(user_id)
            
            # Process user data
            profile = {
                "id": user_id,
                "name": user_data["name"],
                "email": user_data["email"],
                "display_name": user_data["name"].title()
            }
            
            return profile
            
        except ValueError as e:
            raise InvalidUserDataError(f"Invalid user data provided") from e
        except QueryError as e:
            raise UserNotFoundError(f"User {user_id} not found") from e
        except Exception as e:
            raise ServiceError(f"Unexpected error in user service") from e

# API layer
class UserAPI:
    """User API layer."""
    
    def __init__(self, service: UserService):
        self.service = service
    
    def get_user_endpoint(self, user_id_str: str) -> str:
        """API endpoint for getting user."""
        try:
            # Parse user ID
            try:
                user_id = int(user_id_str)
            except ValueError as e:
                raise BadRequestError(f"Invalid user ID format: {user_id_str}") from e
            
            # Get user profile
            profile = self.service.get_user_profile(user_id)
            
            # Return JSON response
            return json.dumps({"status": "success", "data": profile})
            
        except BadRequestError:
            # Re-raise API errors as-is
            raise
        except (UserNotFoundError, InvalidUserDataError) as e:
            raise BadRequestError(f"Client error: {e}") from e
        except ServiceError as e:
            raise InternalServerError(f"Service error occurred") from e
        except Exception as e:
            raise InternalServerError(f"Unexpected server error") from e

def demonstrate_layered_error_handling():
    """Demonstrate error handling in layered applications."""
    print("=== Step 4: Layered Application Error Handling ===")
    
    # Setup layers
    db = DatabaseLayer()
    service = UserService(db)
    api = UserAPI(service)
    
    test_cases = ["1", "999", "invalid", "-1"]
    
    for user_id_str in test_cases:
        try:
            print(f"API Request: GET /user/{user_id_str}")
            response = api.get_user_endpoint(user_id_str)
            print(f"Response: {response}")
        except APIError as e:
            print(f"API Error ({type(e).__name__}): {e}")
            
            # Walk through the error chain
            print("Error chain:")
            current = e
            level = 1
            while current:
                print(f"  {level}. {type(current).__name__}: {current}")
                current = current.__cause__
                level += 1
        print()

def divide_numbers(a, b):
    """Basic function that might raise an exception."""
    try:
        return a / b
    except ZeroDivisionError as e:
        # Chain the exception with a more descriptive error
        raise ValueError(f"Cannot divide {a} by zero") from e

def process_division(a, b):
    """Function that demonstrates implicit chaining."""
    try:
        return divide_numbers(a, b)
    except ValueError:
        # This will create implicit chaining
        raise RuntimeError(f"Failed to process division of {a} and {b}")

def validate_data(data):
    """Validate input data."""
    try:
        if not isinstance(data, (int, float)):
            raise TypeError(f"Expected number, got {type(data).__name__}")
        if data < 0:
            raise ValueError("Number must be non-negative")
        return True
    except (TypeError, ValueError) as e:
        raise ValidationError(
            f"Data validation failed", 
            data=data, 
            operation="validate"
        ) from e

def transform_data(data):
    """Transform data with potential for errors."""
    try:
        # Simulate some complex transformation
        result = data ** 0.5  # Square root
        return result
    except (ValueError, TypeError) as e:
        raise TransformationError(
            f"Failed to transform data",
            data=data,
            operation="square_root"
        ) from e

def demonstrate_custom_exceptions():
    """Demonstrate custom exceptions with chaining."""
    print("=== Step 3: Custom Exceptions with Chaining ===")
    
    test_cases = [-5, "invalid", 16]
    
    for data in test_cases:
        try:
            print(f"Processing data: {data}")
            validate_data(data)
            result = transform_data(data)
            print(f"Result: {result}")
        except DataProcessingError as e:
            print(f"Processing error: {e}")
            print(f"Error type: {type(e).__name__}")
            if e.__cause__:
                print(f"Root cause: {type(e.__cause__).__name__}: {e.__cause__}")
        print()

def demonstrate_implicit_chaining():
    """Demonstrate implicit exception chaining."""
    print("=== Step 2: Implicit Exception Chaining ===")
    
    try:
        result = process_division(10, 0)
    except RuntimeError as e:
        print(f"Caught exception: {e}")
        print(f"Context (implicit): {e.__context__}")
        print(f"Cause (explicit): {e.__cause__}")
        
        # Walk through the exception chain
        current = e
        level = 0
        while current:
            print(f"Level {level}: {type(current).__name__}: {current}")
            current = current.__context__ or current.__cause__
            level += 1
        print()

def demonstrate_basic_chaining():
    """Demonstrate basic exception chaining."""
    print("=== Step 1: Basic Exception Chaining ===")
    
    try:
        result = divide_numbers(10, 0)
    except ValueError as e:
        print(f"Caught exception: {e}")
        print(f"Original cause: {e.__cause__}")
        print(f"Exception type: {type(e.__cause__)}")
        print()

# Test all chaining types
demonstrate_basic_chaining()
demonstrate_implicit_chaining()
demonstrate_custom_exceptions()
demonstrate_layered_error_handling()

# What we accomplished in this step:
# - Implemented error handling across multiple application layers
# - Showed how each layer adds its own context while preserving the chain
# - Demonstrated proper error transformation between layers


# Step 5: Best practices for preserving error context
# ===============================================================================

# Explanation:
# This step demonstrates best practices for exception chaining, including
# when to suppress chaining, how to preserve context, and error logging.

import logging
import traceback
from contextlib import contextmanager
from typing import Optional, Type

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class ErrorContext:
    """Utility class for managing error context."""
    
    @staticmethod
    def format_exception_chain(exception: Exception) -> str:
        """Format the complete exception chain for logging."""
        lines = []
        current = exception
        level = 1
        
        while current:
            lines.append(f"Level {level}: {type(current).__name__}: {current}")
            current = current.__cause__ or current.__context__
            level += 1
        
        return "\n".join(lines)
    
    @staticmethod
    def get_root_cause(exception: Exception) -> Exception:
        """Get the root cause of an exception chain."""
        current = exception
        while current.__cause__ or current.__context__:
            current = current.__cause__ or current.__context__
        return current

@contextmanager
def error_context(operation: str, **context_data):
    """Context manager for adding operation context to errors."""
    try:
        yield
    except Exception as e:
        # Add context to the exception
        context_msg = f"Operation '{operation}' failed"
        if context_data:
            context_items = [f"{k}={v}" for k, v in context_data.items()]
            context_msg += f" (context: {', '.join(context_items)})"
        
        # Chain with context
        raise RuntimeError(context_msg) from e

class SecurityError(Exception):
    """Security-related error."""
    pass

def validate_password(password: str) -> bool:
    """Validate password with suppressed internal errors."""
    try:
        # Simulate complex validation that might fail
        if len(password) < 8:
            raise ValueError("Password too short")
        
        # Simulate checking against compromised password database
        compromised_passwords = ["password123", "admin", "123456"]
        if password.lower() in compromised_passwords:
            raise SecurityError("Password is compromised")
        
        return True
        
    except (ValueError, SecurityError):
        # Re-raise validation errors as-is
        raise
    except Exception as e:
        # Suppress internal implementation details for security
        security_error = SecurityError("Password validation failed")
        security_error.__cause__ = None  # Suppress the chain
        raise security_error

class ErrorHandler:
    """Comprehensive error handling utility."""
    
    def __init__(self, logger_name: str = __name__):
        self.logger = logging.getLogger(logger_name)
    
    def handle_error(self, operation: str, exception: Exception, 
                    reraise: bool = True, log_level: str = "error"):
        """Handle an error with logging and optional re-raising."""
        
        # Log the error with full context
        log_method = getattr(self.logger, log_level.lower())
        log_method(f"Error in {operation}: {exception}")
        log_method(f"Error chain:\n{ErrorContext.format_exception_chain(exception)}")
        
        # Log the root cause
        root_cause = ErrorContext.get_root_cause(exception)
        log_method(f"Root cause: {type(root_cause).__name__}: {root_cause}")
        
        if reraise:
            raise exception
    
    @contextmanager
    def error_boundary(self, operation: str, fallback_value=None):
        """Create an error boundary that catches and handles exceptions."""
        try:
            yield
        except Exception as e:
            self.handle_error(operation, e, reraise=False)
            if fallback_value is not None:
                return fallback_value
            raise

def safe_operation(func, *args, **kwargs):
    """Safely execute an operation with proper error handling."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        # Log the complete error chain
        logger.error(f"Operation failed: {func.__name__}")
        logger.error(f"Error chain:\n{ErrorContext.format_exception_chain(e)}")
        
        # Re-raise with additional context
        raise RuntimeError(f"Safe operation '{func.__name__}' failed") from e

def demonstrate_best_practices():
    """Demonstrate best practices for error context preservation."""
    print("=== Step 5: Best Practices for Error Context ===")
    
    error_handler = ErrorHandler()
    
    # Example 1: Using error context manager
    print("1. Error context manager:")
    try:
        with error_context("data_processing", user_id=123, operation="transform"):
            raise ValueError("Invalid data format")
    except RuntimeError as e:
        print(f"Caught: {e}")
        print(f"Root cause: {ErrorContext.get_root_cause(e)}")
    print()
    
    # Example 2: Safe operation wrapper
    print("2. Safe operation wrapper:")
    def risky_operation(x, y):
        return x / y
    
    try:
        safe_operation(risky_operation, 10, 0)
    except RuntimeError as e:
        print(f"Safe operation failed: {e}")
    print()
    
    # Example 3: Suppressed context for security
    print("3. Suppressed context for security:")
    try:
        validate_password("weak")
    except SecurityError as e:
        print(f"Security error: {e}")
        print(f"Cause suppressed: {e.__cause__ is None}")
    print()
    
    # Example 4: Error boundary
    print("4. Error boundary with fallback:")
    with error_handler.error_boundary("risky_calculation", fallback_value="N/A"):
        result = 10 / 0
    print()
    
    # Example 5: Complete error chain analysis
    print("5. Complete error chain analysis:")
    try:
        with error_context("outer_operation"):
            with error_context("inner_operation", step=1):
                raise ValueError("Original error")
    except Exception as e:
        print("Complete error analysis:")
        print(f"Exception: {e}")
        print(f"Chain:\n{ErrorContext.format_exception_chain(e)}")
        print(f"Root cause: {ErrorContext.get_root_cause(e)}")

# Test all steps
demonstrate_basic_chaining()
demonstrate_implicit_chaining()
demonstrate_custom_exceptions()
demonstrate_layered_error_handling()
demonstrate_best_practices()

# What we accomplished in this step:
# - Implemented utilities for managing error context
# - Showed when and how to suppress exception chaining
# - Demonstrated error boundaries and safe operation wrappers
# - Created comprehensive error logging and analysis tools


# ===============================================================================
#                              FINAL SUMMARY
# ===============================================================================
#
# WHAT WE LEARNED ABOUT EXCEPTION CHAINING:
#
# 1. EXPLICIT CHAINING (raise ... from ...):
#    - Use when you want to preserve the original exception context
#    - Creates a clear causal relationship between exceptions
#    - Accessible through __cause__ attribute
#
# 2. IMPLICIT CHAINING:
#    - Happens automatically when raising in except blocks
#    - Preserves context through __context__ attribute
#    - Shows the execution flow of exception handling
#
# 3. CUSTOM EXCEPTIONS:
#    - Can be designed to work well with chaining
#    - Should include relevant context information
#    - Help create domain-specific error hierarchies
#
# 4. LAYERED APPLICATIONS:
#    - Each layer should add its own context
#    - Transform exceptions appropriately for each layer
#    - Preserve the original error chain for debugging
#
# 5. BEST PRACTICES:
#    - Use context managers for operation-specific errors
#    - Implement error boundaries for graceful degradation
#    - Log complete error chains for debugging
#    - Suppress chaining only when necessary (e.g., security)
#    - Provide utilities for error analysis and root cause detection
#
# Remember: Exception chaining is a powerful tool for debugging and error
# handling. Use it wisely to create maintainable and debuggable applications!
#
# ===============================================================================