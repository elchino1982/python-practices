# Python Error Handling: Complete Tutorial Guide

## Table of Contents

1. [Introduction to Error Handling](#introduction)
2. [Beginner Level](#beginner-level)
   - [Understanding Exceptions](#understanding-exceptions)
   - [Basic Try-Except Blocks](#basic-try-except)
   - [Common Exception Types](#common-exceptions)
   - [Exception Hierarchy](#exception-hierarchy)
3. [Intermediate Level](#intermediate-level)
   - [Advanced Try-Except Patterns](#advanced-patterns)
   - [Custom Exception Classes](#custom-exceptions)
   - [Exception Chaining](#exception-chaining)
   - [Error Logging](#error-logging)
4. [Advanced Level](#advanced-level)
   - [Context Managers for Cleanup](#context-managers)
   - [Defensive Programming](#defensive-programming)
   - [Error Recovery Strategies](#error-recovery)
   - [Performance Considerations](#performance)
5. [Expert Level](#expert-level)
   - [Advanced Exception Handling Patterns](#expert-patterns)
   - [Testing Exception Scenarios](#testing-exceptions)
   - [Production Error Handling](#production-handling)
   - [Best Practices Summary](#best-practices)

---

## Introduction to Error Handling {#introduction}

Error handling is a critical aspect of writing robust, maintainable Python applications. Proper error handling helps you:

- **Prevent crashes**: Handle unexpected situations gracefully
- **Improve user experience**: Provide meaningful error messages
- **Debug effectively**: Preserve error context and stack traces
- **Maintain application stability**: Recover from errors when possible
- **Follow best practices**: Write professional, production-ready code

### Why Error Handling Matters

```python
# Bad: Program crashes on invalid input
def divide_numbers(a, b):
    return a / b

result = divide_numbers(10, 0)  # ZeroDivisionError crashes the program
```

```python
# Good: Graceful error handling
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

result = divide_numbers(10, 0)  # Returns None, program continues
```

---

## Beginner Level {#beginner-level}

### Understanding Exceptions {#understanding-exceptions}

An **exception** is an event that occurs during program execution that disrupts the normal flow of instructions. When Python encounters an error, it "raises" an exception.

#### What Happens When an Exception Occurs?

1. **Exception is raised**: Python creates an exception object
2. **Stack unwinding**: Python looks for an exception handler
3. **Handler found**: Exception is caught and handled
4. **No handler**: Program terminates with an error message

#### Basic Exception Example

```python
# This will raise a NameError
print(undefined_variable)  # NameError: name 'undefined_variable' is not defined
```

### Basic Try-Except Blocks {#basic-try-except}

The `try-except` block is the fundamental error handling mechanism in Python.

#### Basic Syntax

```python
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType:
    # Code to handle the exception
    handle_error()
```

#### Simple Examples

```python
# Example 1: Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    result = None
```

```python
# Example 2: Handling file not found
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
    content = ""
```

```python
# Example 3: Handling type conversion errors
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")
```

#### Multiple Exception Types

```python
try:
    filename = input("Enter filename: ")
    with open(filename, 'r') as file:
        number = int(file.read().strip())
        result = 100 / number
        print(f"Result: {result}")
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("File doesn't contain a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

#### Catching Multiple Exceptions Together

```python
try:
    # Some risky operation
    risky_operation()
except (ValueError, TypeError, KeyError) as e:
    print(f"An error occurred: {e}")
```

### Common Exception Types {#common-exceptions}

Understanding common exception types helps you write more specific and effective error handling code.

#### Built-in Exception Types

| Exception | Description | Common Causes |
|-----------|-------------|---------------|
| `ValueError` | Invalid value for operation | `int("abc")`, `math.sqrt(-1)` |
| `TypeError` | Wrong data type | `"hello" + 5`, `len(42)` |
| `KeyError` | Dictionary key not found | `dict["missing_key"]` |
| `IndexError` | List index out of range | `list[100]` when list has 5 items |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `AttributeError` | Object has no attribute | `"hello".nonexistent_method()` |
| `ImportError` | Module import failed | `import nonexistent_module` |
| `NameError` | Variable not defined | Using undefined variable |
| `SyntaxError` | Invalid Python syntax | Missing colons, parentheses |

#### Practical Examples

```python
# ValueError Example
def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
    except ValueError as e:
        print(f"Invalid age: {e}")
        return None

# TypeError Example
def calculate_area(length, width):
    try:
        return length * width
    except TypeError:
        print("Length and width must be numbers")
        return None

# KeyError Example
def get_user_info(user_dict, key):
    try:
        return user_dict[key]
    except KeyError:
        print(f"Key '{key}' not found in user information")
        return None

# IndexError Example
def get_list_item(items, index):
    try:
        return items[index]
    except IndexError:
        print(f"Index {index} is out of range")
        return None
```

### Exception Hierarchy {#exception-hierarchy}

Python exceptions follow a hierarchy. Understanding this helps you catch exceptions at the right level.

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

#### Using Exception Hierarchy

```python
# Catching parent exceptions
try:
    # Some operation that might fail
    result = risky_operation()
except LookupError:  # Catches both IndexError and KeyError
    print("Lookup failed")
except ArithmeticError:  # Catches ZeroDivisionError, OverflowError, etc.
    print("Math operation failed")

# More specific to general
try:
    process_data()
except FileNotFoundError:
    print("Specific: File not found")
except OSError:
    print("General: OS-related error")
except Exception:
    print("Catch-all: Any other exception")
```

#### Best Practices for Exception Hierarchy

1. **Catch specific exceptions first**: More specific handlers should come before general ones
2. **Don't catch BaseException**: Usually catch Exception or more specific types
3. **Use parent classes wisely**: When you want to handle multiple related exceptions

```python
# Good: Specific to general
try:
    process_file()
except FileNotFoundError:
    handle_missing_file()
except PermissionError:
    handle_permission_denied()
except OSError:
    handle_other_os_errors()
except Exception:
    handle_unexpected_errors()

# Bad: General exception catches everything
try:
    process_file()
except Exception:  # This catches everything, making specific handlers unreachable
    handle_any_error()
except FileNotFoundError:  # This will never be reached!
    handle_missing_file()
```

---

## Intermediate Level {#intermediate-level}

### Advanced Try-Except Patterns {#advanced-patterns}

Beyond basic exception handling, Python offers powerful patterns for more sophisticated error management.

#### The `else` Clause

The `else` clause runs only if no exception was raised in the `try` block.

```python
def read_file_safely(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    else:
        # This runs only if no exception occurred
        print(f"Successfully opened {filename}")
        content = file.read()
        file.close()
        return content

# Example usage
content = read_file_safely("data.txt")
if content:
    print("File content:", content)
```

#### The `finally` Clause

The `finally` clause always executes, whether an exception occurred or not. Perfect for cleanup operations.

```python
def process_file_with_cleanup(filename):
    file = None
    try:
        file = open(filename, 'r')
        data = file.read()
        # Process data (might raise exceptions)
        result = process_data(data)
        return result
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
    finally:
        # This always runs, even if an exception occurred
        if file:
            file.close()
            print("File closed")

# Better approach using context managers (we'll cover this later)
def process_file_better(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return process_data(data)
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
```

#### Complete Try-Except-Else-Finally Pattern

```python
def comprehensive_file_processing(filename):
    print(f"Starting to process {filename}")
    
    try:
        # Attempt the risky operation
        with open(filename, 'r') as file:
            data = file.read()
            
        # Validate data
        if not data.strip():
            raise ValueError("File is empty")
            
        # Process data
        result = complex_data_processing(data)
        
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None
    except ValueError as e:
        print(f"Data validation error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    else:
        # Success case - no exceptions raised
        print("File processed successfully")
        return result
    finally:
        # Cleanup code that always runs
        print(f"Finished processing {filename}")
```

#### Exception Information Access

```python
import sys
import traceback

def detailed_error_handling():
    try:
        # Some risky operation
        result = 10 / 0
    except ZeroDivisionError as e:
        # Access exception details
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        print(f"Exception args: {e.args}")
        
        # Get detailed traceback information
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("\nDetailed traceback:")
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        
        # Get traceback as string
        tb_str = traceback.format_exc()
        print(f"\nTraceback as string:\n{tb_str}")
```

#### Re-raising Exceptions

Sometimes you want to handle an exception partially and then re-raise it.

```python
def log_and_reraise():
    try:
        risky_operation()
    except Exception as e:
        # Log the error
        print(f"Error logged: {e}")
        
        # Re-raise the same exception
        raise  # Don't use 'raise e' as it loses traceback info

def transform_exception():
    try:
        risky_operation()
    except ValueError as e:
        # Transform into a more specific exception
        raise CustomError(f"Custom handling: {e}") from e
```

### Custom Exception Classes {#custom-exceptions}

Creating custom exceptions makes your code more readable and allows for more specific error handling.

#### Basic Custom Exceptions

```python
# Simple custom exception
class ValidationError(Exception):
    """Raised when data validation fails"""
    pass

class DatabaseError(Exception):
    """Raised when database operations fail"""
    pass

class AuthenticationError(Exception):
    """Raised when authentication fails"""
    pass

# Usage
def validate_email(email):
    if '@' not in email:
        raise ValidationError("Invalid email format")
    return True

try:
    validate_email("invalid-email")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

#### Advanced Custom Exceptions

```python
class APIError(Exception):
    """Base exception for API-related errors"""
    
    def __init__(self, message, status_code=None, response_data=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data
        
    def __str__(self):
        if self.status_code:
            return f"API Error {self.status_code}: {super().__str__()}"
        return super().__str__()

class APITimeoutError(APIError):
    """Raised when API request times out"""
    
    def __init__(self, message="API request timed out", timeout_duration=None):
        super().__init__(message)
        self.timeout_duration = timeout_duration

class APIRateLimitError(APIError):
    """Raised when API rate limit is exceeded"""
    
    def __init__(self, message="API rate limit exceeded", retry_after=None):
        super().__init__(message, status_code=429)
        self.retry_after = retry_after

# Usage example
def make_api_request(url, timeout=30):
    try:
        # Simulate API request
        if "timeout" in url:
            raise APITimeoutError(timeout_duration=timeout)
        elif "ratelimit" in url:
            raise APIRateLimitError(retry_after=60)
        # Normal processing...
        return {"status": "success"}
        
    except APITimeoutError as e:
        print(f"Request timed out after {e.timeout_duration} seconds")
        raise
    except APIRateLimitError as e:
        print(f"Rate limited. Retry after {e.retry_after} seconds")
        raise
    except APIError as e:
        print(f"API error: {e}")
        raise
```

#### Exception Hierarchies

```python
# Create a hierarchy of related exceptions
class ApplicationError(Exception):
    """Base exception for application-specific errors"""
    pass

class ConfigurationError(ApplicationError):
    """Raised when configuration is invalid"""
    pass

class DataError(ApplicationError):
    """Base class for data-related errors"""
    pass

class DataValidationError(DataError):
    """Raised when data validation fails"""
    pass

class DataProcessingError(DataError):
    """Raised when data processing fails"""
    pass

class ExternalServiceError(ApplicationError):
    """Base class for external service errors"""
    pass

class DatabaseConnectionError(ExternalServiceError):
    """Raised when database connection fails"""
    pass

class APIServiceError(ExternalServiceError):
    """Raised when external API service fails"""
    pass

# Usage with hierarchy
def process_user_data(data):
    try:
        validate_data(data)
        process_data(data)
        save_to_database(data)
    except DataValidationError:
        print("Data validation failed")
        # Handle validation errors specifically
    except DataError:
        print("General data error occurred")
        # Handle any data-related error
    except ExternalServiceError:
        print("External service unavailable")
        # Handle any external service error
    except ApplicationError:
        print("Application error occurred")
        # Handle any application-specific error
```

### Exception Chaining {#exception-chaining}

Exception chaining allows you to preserve the original exception context while raising a new one. This is crucial for debugging and maintaining error context.

#### Basic Exception Chaining with `from`

```python
def process_user_input(user_input):
    try:
        # Convert input to integer
        number = int(user_input)
        return number
    except ValueError as e:
        # Chain the original exception with a more descriptive one
        raise ValidationError(f"Invalid input '{user_input}': must be a number") from e

def calculate_square_root(value):
    try:
        result = process_user_input(value)
        if result < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return result ** 0.5
    except ValidationError as e:
        # Chain with context about what we were trying to do
        raise CalculationError(f"Failed to calculate square root: {e}") from e

# Usage
try:
    result = calculate_square_root("abc")
except CalculationError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")
    
    # Print full chain
    import traceback
    traceback.print_exc()
```

#### Suppressing Exception Chaining

Sometimes you want to raise a new exception without showing the chain:

```python
def clean_error_message(user_input):
    try:
        return int(user_input)
    except ValueError:
        # Suppress the original exception chain
        raise ValidationError("Please enter a valid number") from None

# This will only show ValidationError, not the original ValueError
try:
    result = clean_error_message("abc")
except ValidationError as e:
    print(f"Clean error: {e}")  # No mention of ValueError
```

#### Implicit Exception Chaining

When an exception is raised inside an exception handler, Python automatically chains them:

```python
def implicit_chaining_example():
    try:
        # First exception
        result = 10 / 0
    except ZeroDivisionError:
        # Second exception raised while handling the first
        undefined_variable  # NameError
        
try:
    implicit_chaining_example()
except NameError as e:
    print(f"Final exception: {e}")
    print(f"Context (what we were handling): {e.__context__}")
```

#### Advanced Exception Chaining Patterns

```python
class DataProcessor:
    def __init__(self, config_file):
        self.config = self._load_config(config_file)
    
    def _load_config(self, config_file):
        try:
            with open(config_file, 'r') as f:
                import json
                return json.load(f)
        except FileNotFoundError as e:
            raise ConfigurationError(
                f"Configuration file '{config_file}' not found"
            ) from e
        except json.JSONDecodeError as e:
            raise ConfigurationError(
                f"Invalid JSON in configuration file '{config_file}'"
            ) from e
    
    def process_data(self, data_file):
        try:
            # Load data
            with open(data_file, 'r') as f:
                data = f.read()
            
            # Process according to config
            return self._apply_processing_rules(data)
            
        except FileNotFoundError as e:
            raise DataProcessingError(
                f"Data file '{data_file}' not found"
            ) from e
        except Exception as e:
            raise DataProcessingError(
                f"Failed to process data from '{data_file}'"
            ) from e
    
    def _apply_processing_rules(self, data):
        try:
            # Apply complex processing rules
            if not self.config.get('enabled', True):
                raise ValueError("Processing is disabled in configuration")
            
            # More processing...
            return processed_data
            
        except KeyError as e:
            raise ConfigurationError(
                f"Missing required configuration key: {e}"
            ) from e
        except ValueError as e:
            raise DataProcessingError(
                f"Processing rule validation failed: {e}"
            ) from e
```

### Error Logging {#error-logging}

Proper logging is essential for debugging and monitoring applications in production.

#### Basic Logging Setup

```python
import logging
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def divide_with_logging(a, b):
    try:
        logger.info(f"Attempting to divide {a} by {b}")
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"Division by zero error: {a} / {b}", exc_info=True)
        raise
    except Exception as e:
        logger.error(f"Unexpected error in division: {e}", exc_info=True)
        raise
```

#### Advanced Logging Patterns

```python
import logging
import functools
import time
from typing import Any, Callable

class ApplicationLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self._setup_logger()
    
    def _setup_logger(self):
        """Setup logger with multiple handlers and formatters"""
        self.logger.setLevel(logging.DEBUG)
        
        # File handler for all logs
        file_handler = logging.FileHandler('application.log')
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler for warnings and above
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        
        # Error file handler for errors only
        error_handler = logging.FileHandler('errors.log')
        error_handler.setLevel(logging.ERROR)
        
        # Formatters
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        simple_formatter = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        
        file_handler.setFormatter(detailed_formatter)
        console_handler.setFormatter(simple_formatter)
        error_handler.setFormatter(detailed_formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        self.logger.addHandler(error_handler)
    
    def log_exception(self, operation: str, exception: Exception, **context):
        """Log exception with context information"""
        context_str = ", ".join(f"{k}={v}" for k, v in context.items())
        self.logger.error(
            f"Exception in {operation}: {type(exception).__name__}: {exception}. "
            f"Context: {context_str}",
            exc_info=True
        )
    
    def log_function_call(self, func: Callable) -> Callable:
        """Decorator to log function calls and exceptions"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            self.logger.debug(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            
            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time
                self.logger.debug(f"{func.__name__} completed successfully in {duration:.3f}s")
                return result
            except Exception as e:
                duration = time.time() - start_time
                self.log_exception(
                    f"{func.__name__}",
                    e,
                    args=args,
                    kwargs=kwargs,
                    duration=f"{duration:.3f}s"
                )
                raise
        return wrapper

# Usage example
app_logger = ApplicationLogger("MyApp")

@app_logger.log_function_call
def risky_database_operation(user_id: int, data: dict):
    try:
        # Simulate database operation
        if user_id < 0:
            raise ValueError("Invalid user ID")
        if not data:
            raise ValueError("No data provided")
        
        # Simulate processing
        time.sleep(0.1)
        return {"status": "success", "user_id": user_id}
        
    except ValueError as e:
        app_logger.log_exception("data_validation", e, user_id=user_id, data=data)
        raise
    except Exception as e:
        app_logger.log_exception("database_operation", e, user_id=user_id)
        raise
```

#### Structured Logging

```python
import json
import logging
from datetime import datetime
from typing import Dict, Any

class StructuredLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self._setup_structured_logging()
    
    def _setup_structured_logging(self):
        """Setup logger for structured JSON output"""
        handler = logging.StreamHandler()
        handler.setFormatter(self.JSONFormatter())
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    class JSONFormatter(logging.Formatter):
        def format(self, record):
            log_entry = {
                'timestamp': datetime.utcnow().isoformat(),
                'level': record.levelname,
                'logger': record.name,
                'message': record.getMessage(),
                'module': record.module,
                'function': record.funcName,
                'line': record.lineno
            }
            
            # Add exception info if present
            if record.exc_info:
                log_entry['exception'] = self.formatException(record.exc_info)
            
            # Add extra fields
            for key, value in record.__dict__.items():
                if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 
                              'pathname', 'filename', 'module', 'lineno', 
                              'funcName', 'created', 'msecs', 'relativeCreated', 
                              'thread', 'threadName', 'processName', 'process',
                              'getMessage', 'exc_info', 'exc_text', 'stack_info']:
                    log_entry[key] = value
            
            return json.dumps(log_entry)
    
    def log_error(self, message: str, error: Exception = None, **context):
        """Log error with structured context"""
        extra = {
            'error_type': type(error).__name__ if error else None,
            'error_message': str(error) if error else None,
            **context
        }
        self.logger.error(message, exc_info=error is not None, extra=extra)
    
    def log_operation(self, operation: str, status: str, **context):
        """Log operation with structured context"""
        extra = {
            'operation': operation,
            'status': status,
            **context
        }
        self.logger.info(f"Operation {operation} {status}", extra=extra)

# Usage
structured_logger = StructuredLogger("StructuredApp")

def process_user_request(user_id: int, request_data: dict):
    try:
        structured_logger.log_operation(
            "user_request_start",
            "started",
            user_id=user_id,
            request_size=len(str(request_data))
        )
        
        # Process request
        result = complex_processing(request_data)
        
        structured_logger.log_operation(
            "user_request_complete",
            "success",
            user_id=user_id,
            result_size=len(str(result))
        )
        
        return result
        
    except Exception as e:
        structured_logger.log_error(
            "User request processing failed",
            error=e,
            user_id=user_id,
            request_data=request_data
        )
        raise
```

---

## Advanced Level {#advanced-level}

### Context Managers for Cleanup {#context-managers}

Context managers ensure proper resource cleanup and error handling using the `with` statement.

#### Understanding Context Managers

Context managers implement the context management protocol with `__enter__` and `__exit__` methods.

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
            # Return False to propagate the exception
            return False
        return True

# Usage
try:
    with FileManager("test.txt", "w") as f:
        f.write("Hello, World!")
        # File is automatically closed even if an exception occurs
        raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"Caught: {e}")
```

#### Using `contextlib` for Simple Context Managers

```python
from contextlib import contextmanager
import time
import logging

@contextmanager
def timer_context(operation_name):
    """Context manager to time operations"""
    start_time = time.time()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info(f"Starting {operation_name}")
        yield
    except Exception as e:
        logger.error(f"Error in {operation_name}: {e}")
        raise
    finally:
        duration = time.time() - start_time
        logger.info(f"Completed {operation_name} in {duration:.3f} seconds")

# Usage
with timer_context("data processing"):
    # Your code here
    time.sleep(1)
    process_data()
```

#### Database Connection Context Manager

```python
import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("BEGIN")
            yield conn
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            raise DatabaseError(f"Database operation failed: {e}") from e
        finally:
            if conn:
                conn.close()
    
    def execute_query(self, query, params=None):
        """Execute query with proper error handling"""
        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
            except sqlite3.Error as e:
                raise DatabaseError(f"Query execution failed: {e}") from e

# Usage
db = DatabaseManager("example.db")

try:
    results = db.execute_query("SELECT * FROM users WHERE id = ?", (1,))
    print(results)
except DatabaseError as e:
    print(f"Database error: {e}")
```

#### Advanced Context Manager Patterns

```python
from contextlib import contextmanager, ExitStack
import tempfile
import shutil
import os

class ResourceManager:
    """Advanced resource management with multiple resources"""
    
    @contextmanager
    def temporary_directory(self, prefix="tmp_"):
        """Create and cleanup temporary directory"""
        temp_dir = tempfile.mkdtemp(prefix=prefix)
        try:
            yield temp_dir
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
    
    @contextmanager
    def file_lock(self, lock_file):
        """Simple file-based locking mechanism"""
        if os.path.exists(lock_file):
            raise ResourceError(f"Resource is locked: {lock_file}")
        
        try:
            # Create lock file
            with open(lock_file, 'w') as f:
                f.write(str(os.getpid()))
            yield
        finally:
            # Remove lock file
            try:
                os.remove(lock_file)
            except OSError:
                pass
    
    @contextmanager
    def multiple_resources(self, *resource_contexts):
        """Manage multiple resources with ExitStack"""
        with ExitStack() as stack:
            resources = []
            for context in resource_contexts:
                resource = stack.enter_context(context)
                resources.append(resource)
            yield resources

# Usage
rm = ResourceManager()

# Single resource
with rm.temporary_directory("data_") as temp_dir:
    print(f"Working in: {temp_dir}")
    # Do work with temporary directory

# Multiple resources
with rm.multiple_resources(
    rm.temporary_directory("input_"),
    rm.temporary_directory("output_"),
    rm.file_lock("process.lock")
) as (input_dir, output_dir, _):
    print(f"Input: {input_dir}, Output: {output_dir}")
    # Process data safely
```

### Defensive Programming {#defensive-programming}

Defensive programming involves writing code that anticipates and handles potential problems before they occur.

#### Input Validation and Sanitization

```python
from typing import Union, List, Dict, Any
import re

class InputValidator:
    """Comprehensive input validation utilities"""
    
    @staticmethod
    def validate_email(email: str) -> str:
        """Validate and normalize email address"""
        if not isinstance(email, str):
            raise ValidationError("Email must be a string")
        
        email = email.strip().lower()
        
        if not email:
            raise ValidationError("Email cannot be empty")
        
        # Basic email regex
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValidationError(f"Invalid email format: {email}")
        
        return email
    
    @staticmethod
    def validate_age(age: Union[int, str]) -> int:
        """Validate age input"""
        try:
            age_int = int(age)
        except (ValueError, TypeError):
            raise ValidationError(f"Age must be a number, got: {type(age).__name__}")
        
        if age_int < 0:
            raise ValidationError("Age cannot be negative")
        if age_int > 150:
            raise ValidationError("Age seems unrealistic")
        
        return age_int
    
    @staticmethod
    def validate_password(password: str) -> str:
        """Validate password strength"""
        if not isinstance(password, str):
            raise ValidationError("Password must be a string")
        
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter")
        
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter")
        
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit")
        
        return password
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Sanitize filename for safe file operations"""
        if not isinstance(filename, str):
            raise ValidationError("Filename must be a string")
        
        # Remove dangerous characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        
        # Remove leading/trailing whitespace and dots
        filename = filename.strip(' .')
        
        if not filename:
            raise ValidationError("Filename cannot be empty after sanitization")
        
        # Prevent reserved names on Windows
        reserved_names = ['CON', 'PRN', 'AUX', 'NUL'] + \
                        [f'COM{i}' for i in range(1, 10)] + \
                        [f'LPT{i}' for i in range(1, 10)]
        
        if filename.upper() in reserved_names:
            filename = f"_{filename}"
        
        return filename

def safe_user_registration(user_data: Dict[str, Any]) -> Dict[str, Any]:
    """Safely register a user with comprehensive validation"""
    validator = InputValidator()
    
    try:
        # Validate required fields
        required_fields = ['email', 'password', 'age', 'username']
        for field in required_fields:
            if field not in user_data:
                raise ValidationError(f"Missing required field: {field}")
        
        # Validate and sanitize each field
        validated_data = {
            'email': validator.validate_email(user_data['email']),
            'password': validator.validate_password(user_data['password']),
            'age': validator.validate_age(user_data['age']),
            'username': validator.sanitize_filename(user_data['username'])
        }
        
        return validated_data
        
    except ValidationError as e:
        raise UserRegistrationError(f"User registration failed: {e}") from e
    except Exception as e:
        raise UserRegistrationError(f"Unexpected error during registration: {e}") from e
```

#### Precondition and Postcondition Checks

```python
import functools
from typing import Callable, Any

def precondition(condition_func: Callable, message: str = "Precondition failed"):
    """Decorator to check preconditions"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not condition_func(*args, **kwargs):
                raise PreconditionError(f"{message} in {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def postcondition(condition_func: Callable, message: str = "Postcondition failed"):
    """Decorator to check postconditions"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not condition_func(result, *args, **kwargs):
                raise PostconditionError(f"{message} in {func.__name__}")
            return result
        return wrapper
    return decorator

# Usage examples
@precondition(lambda x, y: y != 0, "Divisor cannot be zero")
@postcondition(lambda result, x, y: abs(result * y - x) < 1e-10, "Division result is incorrect")
def safe_divide(x: float, y: float) -> float:
    """Safely divide two numbers with pre/post conditions"""
    return x / y

@precondition(lambda items: len(items) > 0, "List cannot be empty")
@postcondition(lambda result, items: result in items, "Result must be from the input list")
def get_maximum(items: List[float]) -> float:
    """Get maximum value from a list"""
    return max(items)

# Advanced defensive programming patterns
class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self._balance = self._validate_amount(initial_balance)
    
    def _validate_amount(self, amount: float) -> float:
        """Validate monetary amounts"""
        if not isinstance(amount, (int, float)):
            raise ValidationError("Amount must be a number")
        
        if amount < 0:
            raise ValidationError("Amount cannot be negative")
        
        # Round to 2 decimal places for currency
        return round(float(amount), 2)
    
    @precondition(lambda self, amount: amount > 0, "Deposit amount must be positive")
    def deposit(self, amount: float) -> None:
        """Deposit money with validation"""
        amount = self._validate_amount(amount)
        old_balance = self._balance
        self._balance += amount
        
        # Postcondition check
        if self._balance != old_balance + amount:
            # Rollback and raise error
            self._balance = old_balance
            raise PostconditionError("Balance update failed")
    
    @precondition(lambda self, amount: amount > 0, "Withdrawal amount must be positive")
    @precondition(lambda self, amount: amount <= self._balance, "Insufficient funds")
    def withdraw(self, amount: float) -> None:
        """Withdraw money with validation"""
        amount = self._validate_amount(amount)
        old_balance = self._balance
        self._balance -= amount
        
        # Postcondition check
        if self._balance != old_balance - amount:
            # Rollback and raise error
            self._balance = old_balance
            raise PostconditionError("Balance update failed")
    
    @property
    def balance(self) -> float:
        return self._balance
```

### Error Recovery Strategies {#error-recovery}

Error recovery involves implementing strategies to gracefully handle failures and continue operation when possible.

#### Retry Mechanisms

```python
import time
import random
from typing import Callable, Any, Optional
from functools import wraps

class RetryError(Exception):
    """Raised when all retry attempts fail"""
    pass

def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple = (Exception,),
    jitter: bool = True
):
    """Decorator for automatic retry with exponential backoff"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == max_attempts - 1:
                        # Last attempt failed
                        break
                    
                    # Calculate delay with exponential backoff
                    current_delay = delay * (backoff ** attempt)
                    
                    # Add jitter to prevent thundering herd
                    if jitter:
                        current_delay *= (0.5 + random.random() * 0.5)
                    
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay:.2f}s...")
                    time.sleep(current_delay)
            
            # All attempts failed
            raise RetryError(f"All {max_attempts} attempts failed. Last error: {last_exception}") from last_exception
        
        return wrapper
    return decorator

# Usage examples
@retry(max_attempts=3, delay=0.5, exceptions=(ConnectionError, TimeoutError))
def unreliable_api_call(url: str) -> dict:
    """Simulate an unreliable API call"""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network connection failed")
    return {"status": "success", "data": "API response"}

@retry(max_attempts=5, delay=1.0, backoff=1.5, exceptions=(DatabaseError,))
def database_operation(query: str) -> list:
    """Simulate unreliable database operation"""
    if random.random() < 0.6:  # 60% chance of failure
        raise DatabaseError("Database temporarily unavailable")
    return [{"id": 1, "name": "John"}]
```

#### Circuit Breaker Pattern

```python
import time
from enum import Enum
from typing import Callable, Any
import threading

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreaker:
    """Circuit breaker pattern implementation"""
    
    def __init__(
        self,
        failure_threshold: int = 5,
        timeout: float = 60.0,
        expected_exception: type = Exception
    ):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
        self._lock = threading.Lock()
    
    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with self._lock:
                if self.state == CircuitState.OPEN:
                    if self._should_attempt_reset():
                        self.state = CircuitState.HALF_OPEN
                        print("Circuit breaker: Attempting reset (HALF_OPEN)")
                    else:
                        raise CircuitBreakerOpenError(
                            f"Circuit breaker is OPEN. Service unavailable."
                        )
                
                try:
                    result = func(*args, **kwargs)
                    self._on_success()
                    return result
                    
                except self.expected_exception as e:
                    self._on_failure()
                    raise
        
        return wrapper
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset"""
        return (
            self.last_failure_time and
            time.time() - self.last_failure_time >= self.timeout
        )
    
    def _on_success(self):
        """Handle successful operation"""
        if self.state == CircuitState.HALF_OPEN:
            print("Circuit breaker: Service recovered (CLOSED)")
        
        self.failure_count = 0
        self.state = CircuitState.CLOSED
    
    def _on_failure(self):
        """Handle failed operation"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            print(f"Circuit breaker: Too many failures ({self.failure_count}) - OPEN")

# Usage
@CircuitBreaker(failure_threshold=3, timeout=30.0, expected_exception=APIError)
def external_service_call(data: dict) -> dict:
    """Call to external service that might fail"""
    if random.random() < 0.8:  # 80% failure rate for demo
        raise APIError("External service unavailable")
    return {"status": "success"}
```

#### Graceful Degradation

```python
from typing import Optional, Union, Dict, Any
import logging

class ServiceRegistry:
    """Registry for managing service dependencies and fallbacks"""
    
    def __init__(self):
        self.services = {}
        self.fallbacks = {}
        self.logger = logging.getLogger(__name__)
    
    def register_service(self, name: str, service: Any, fallback: Optional[Any] = None):
        """Register a service with optional fallback"""
        self.services[name] = service
        if fallback:
            self.fallbacks[name] = fallback
    
    def get_service(self, name: str, use_fallback: bool = True) -> Any:
        """Get service, optionally falling back to alternative"""
        try:
            return self.services[name]
        except KeyError:
            if use_fallback and name in self.fallbacks:
                self.logger.warning(f"Using fallback for service: {name}")
                return self.fallbacks[name]
            raise ServiceNotFoundError(f"Service not found: {name}")

class UserService:
    """Main user service with graceful degradation"""
    
    def __init__(self, registry: ServiceRegistry):
        self.registry = registry
        self.logger = logging.getLogger(__name__)
    
    def get_user_profile(self, user_id: int) -> Dict[str, Any]:
        """Get user profile with graceful degradation"""
        profile = {"id": user_id}
        
        # Try to get basic user info (critical)
        try:
            db_service = self.registry.get_service("database")
            basic_info = db_service.get_user_basic_info(user_id)
            profile.update(basic_info)
        except Exception as e:
            self.logger.error(f"Failed to get basic user info: {e}")
            raise UserServiceError("Cannot retrieve user profile") from e
        
        # Try to get user preferences (non-critical)
        try:
            prefs_service = self.registry.get_service("preferences")
            preferences = prefs_service.get_user_preferences(user_id)
            profile["preferences"] = preferences
        except Exception as e:
            self.logger.warning(f"Failed to get user preferences: {e}")
            profile["preferences"] = self._get_default_preferences()
        
        # Try to get user avatar (non-critical)
        try:
            avatar_service = self.registry.get_service("avatar")
            avatar_url = avatar_service.get_avatar_url(user_id)
            profile["avatar_url"] = avatar_url
        except Exception as e:
            self.logger.warning(f"Failed to get user avatar: {e}")
            profile["avatar_url"] = "/static/default_avatar.png"
        
        # Try to get social data (non-critical, has fallback)
        try:
            social_service = self.registry.get_service("social", use_fallback=True)
            social_data = social_service.get_social_data(user_id)
            profile["social"] = social_data
        except Exception as e:
            self.logger.warning(f"Failed to get social data: {e}")
            profile["social"] = {"friends_count": 0, "posts_count": 0}
        
        return profile
    
    def _get_default_preferences(self) -> Dict[str, Any]:
        """Return default user preferences"""
        return {
            "theme": "light",
            "language": "en",
            "notifications": True
        }

# Usage example
registry = ServiceRegistry()

# Register services with fallbacks
registry.register_service("database", DatabaseService())
registry.register_service("preferences", PreferencesService())
registry.register_service("avatar", AvatarService())
registry.register_service("social", SocialService(), fallback=MockSocialService())

user_service = UserService(registry)

try:
    profile = user_service.get_user_profile(123)
    print("User profile retrieved successfully")
except UserServiceError as e:
    print(f"Failed to get user profile: {e}")
```

#### Bulkhead Pattern

```python
import asyncio
import concurrent.futures
from typing import List, Callable, Any
import threading

class ResourcePool:
    """Resource pool with isolation (bulkhead pattern)"""
    
    def __init__(self, pool_name: str, max_workers: int = 5):
        self.pool_name = pool_name
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=max_workers,
            thread_name_prefix=f"{pool_name}_worker"
        )
        self.active_tasks = 0
        self.max_workers = max_workers
        self._lock = threading.Lock()
        self.logger = logging.getLogger(__name__)
    
    def submit_task(self, func: Callable, *args, **kwargs) -> concurrent.futures.Future:
        """Submit task to isolated resource pool"""
        with self._lock:
            if self.active_tasks >= self.max_workers:
                raise ResourcePoolExhaustedError(
                    f"Resource pool '{self.pool_name}' is at capacity"
                )
            
            self.active_tasks += 1
        
        def wrapped_task():
            try:
                return func(*args, **kwargs)
            finally:
                with self._lock:
                    self.active_tasks -= 1
        
        future = self.executor.submit(wrapped_task)
        self.logger.info(f"Task submitted to pool '{self.pool_name}' ({self.active_tasks}/{self.max_workers})")
        return future
    
    def shutdown(self, wait: bool = True):
        """Shutdown the resource pool"""
        self.executor.shutdown(wait=wait)

class IsolatedServiceManager:
    """Manage services with isolated resource pools"""
    
    def __init__(self):
        self.pools = {}
        self.logger = logging.getLogger(__name__)
    
    def create_pool(self, name: str, max_workers: int = 5) -> ResourcePool:
        """Create an isolated resource pool"""
        pool = ResourcePool(name, max_workers)
        self.pools[name] = pool
        return pool
    
    def execute_in_pool(self, pool_name: str, func: Callable, *args, **kwargs) -> Any:
        """Execute function in specified pool with timeout"""
        if pool_name not in self.pools:
            raise ValueError(f"Pool '{pool_name}' not found")
        
        pool = self.pools[pool_name]
        
        try:
            future = pool.submit_task(func, *args, **kwargs)
            # Wait for result with timeout
            return future.result(timeout=30.0)
        except concurrent.futures.TimeoutError:
            self.logger.error(f"Task in pool '{pool_name}' timed out")
            raise TaskTimeoutError(f"Task in pool '{pool_name}' timed out")
        except ResourcePoolExhaustedError as e:
            self.logger.error(f"Pool '{pool_name}' exhausted: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Task in pool '{pool_name}' failed: {e}")
            raise

# Usage example
service_manager = IsolatedServiceManager()

# Create isolated pools for different services
db_pool = service_manager.create_pool("database", max_workers=10)
api_pool = service_manager.create_pool("external_api", max_workers=3)
email_pool = service_manager.create_pool("email", max_workers=2)

def process_user_request(user_id: int):
    """Process user request using isolated resource pools"""
    try:
        # Database operations in isolated pool
        user_data = service_manager.execute_in_pool(
            "database",
            fetch_user_data,
            user_id
        )
        
        # External API calls in isolated pool
        external_data = service_manager.execute_in_pool(
            "external_api",
            fetch_external_data,
            user_data["external_id"]
        )
        
        # Email operations in isolated pool
        service_manager.execute_in_pool(
            "email",
            send_notification_email,
            user_data["email"],
            external_data
        )
        
        return {"status": "success", "user_id": user_id}
        
    except ResourcePoolExhaustedError as e:
        # Handle resource exhaustion gracefully
        logger.warning(f"Resource pool exhausted: {e}")
        return {"status": "degraded", "message": "Service temporarily limited"}
    except TaskTimeoutError as e:
        # Handle timeouts
        logger.error(f"Task timeout: {e}")
        return {"status": "timeout", "message": "Request timed out"}
    except Exception as e:
        # Handle other errors
        logger.error(f"Request processing failed: {e}")
        return {"status": "error", "message": "Request failed"}
```

### Performance Considerations {#performance}

Error handling can impact performance. Here are strategies to minimize overhead while maintaining robustness.

#### Efficient Exception Handling

```python
import time
from typing import Dict, Any, Optional

class PerformantErrorHandler:
    """Error handler optimized for performance"""
    
    def __init__(self):
        self.error_cache = {}
        self.cache_ttl = 300  # 5 minutes
    
    def is_cached_error(self, error_key: str) -> bool:
        """Check if error is recently cached to avoid repeated processing"""
        if error_key in self.error_cache:
            cached_time = self.error_cache[error_key]
            if time.time() - cached_time < self.cache_ttl:
                return True
            else:
                # Remove expired cache entry
                del self.error_cache[error_key]
        return False
    
    def cache_error(self, error_key: str):
        """Cache error to avoid repeated processing"""
        self.error_cache[error_key] = time.time()
    
    def fast_validation(self, data: Dict[str, Any]) -> Optional[str]:
        """Fast validation with early returns"""
        # Use EAFP (Easier to Ask for Forgiveness than Permission)
        # instead of LBYL (Look Before You Leap)
        
        try:
            # Fast checks first
            if not data:
                return "Data is empty"
            
            # Check required fields efficiently
            required = {"id", "name", "email"}
            if not required.issubset(data.keys()):
                missing = required - data.keys()
                return f"Missing required fields: {missing}"
            
            # Type checks with early exit
            if not isinstance(data["id"], int):
                return "ID must be integer"
            
            if not isinstance(data["name"], str) or len(data["name"]) < 2:
                return "Name must be string with at least 2 characters"
            
            # Email validation (simplified for performance)
            email = data["email"]
            if not isinstance(email, str) or "@" not in email:
                return "Invalid email format"
            
            return None  # No errors
            
        except KeyError as e:
            return f"Missing key: {e}"
        except Exception as e:
            return f"Validation error: {e}"

# Performance comparison examples
def slow_validation_lbyl(data: Dict[str, Any]) -> bool:
    """Slow validation using Look Before You Leap"""
    # Check if data exists
    if data is None:
        raise ValidationError("Data is None")
    
    # Check if it's a dictionary
    if not isinstance(data, dict):
        raise ValidationError("Data must be dictionary")
    
    # Check each field existence before accessing
    if "id" not in data:
        raise ValidationError("Missing ID")
    if "name" not in data:
        raise ValidationError("Missing name")
    if "email" not in data:
        raise ValidationError("Missing email")
    
    # Check types
    if not isinstance(data["id"], int):
        raise ValidationError("ID must be integer")
    if not isinstance(data["name"], str):
        raise ValidationError("Name must be string")
    if not isinstance(data["email"], str):
        raise ValidationError("Email must be string")
    
    return True

def fast_validation_eafp(data: Dict[str, Any]) -> bool:
    """Fast validation using Easier to Ask for Forgiveness than Permission"""
    try:
        # Direct access, let exceptions handle errors
        id_val = data["id"]
        name_val = data["name"]
        email_val = data["email"]
        
        # Quick type and value checks
        if not isinstance(id_val, int) or id_val <= 0:
            raise ValidationError("Invalid ID")
        
        if not isinstance(name_val, str) or len(name_val) < 2:
            raise ValidationError("Invalid name")
        
        if not isinstance(email_val, str) or "@" not in email_val:
            raise ValidationError("Invalid email")
        
        return True
        
    except KeyError as e:
        raise ValidationError(f"Missing field: {e}") from e
    except TypeError as e:
        raise ValidationError(f"Type error: {e}") from e

# Benchmark example
def benchmark_validation_approaches():
    """Benchmark different validation approaches"""
    import timeit
    
    valid_data = {"id": 123, "name": "John Doe", "email": "john@example.com"}
    
    # Benchmark LBYL approach
    lbyl_time = timeit.timeit(
        lambda: slow_validation_lbyl(valid_data),
        number=100000
    )
    
    # Benchmark EAFP approach
    eafp_time = timeit.timeit(
        lambda: fast_validation_eafp(valid_data),
        number=100000
    )
    
    print(f"LBYL approach: {lbyl_time:.4f} seconds")
    print(f"EAFP approach: {eafp_time:.4f} seconds")
    print(f"EAFP is {lbyl_time/eafp_time:.2f}x faster")
```

---

## Expert Level {#expert-level}

### Advanced Exception Handling Patterns {#expert-patterns}

Expert-level patterns for sophisticated error handling in complex applications.

#### Exception Aggregation Pattern

```python
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
import traceback

@dataclass
class ErrorDetail:
    """Detailed error information"""
    exception_type: str
    message: str
    traceback: str
    context: Dict[str, Any]
    timestamp: float
    severity: str = "ERROR"

class ErrorAggregator:
    """Aggregate multiple errors for batch processing"""
    
    def __init__(self, max_errors: int = 100):
        self.errors: List[ErrorDetail] = []
        self.max_errors = max_errors
        self.error_counts: Dict[str, int] = {}
    
    def add_error(
        self, 
        exception: Exception, 
        context: Dict[str, Any] = None,
        severity: str = "ERROR"
    ):
        """Add error to aggregation"""
        import time
        
        error_detail = ErrorDetail(
            exception_type=type(exception).__name__,
            message=str(exception),
            traceback=traceback.format_exc(),
            context=context or {},
            timestamp=time.time(),
            severity=severity
        )
        
        self.errors.append(error_detail)
        
        # Track error frequency
        error_key = f"{error_detail.exception_type}:{error_detail.message}"
        self.error_counts[error_key] = self.error_counts.get(error_key, 0) + 1
        
        # Prevent memory overflow
        if len(self.errors) > self.max_errors:
            self.errors.pop(0)  # Remove oldest error
    
    def get_error_summary(self) -> Dict[str, Any]:
        """Get summary of aggregated errors"""
        if not self.errors:
            return {"total_errors": 0, "error_types": {}, "most_common": []}
        
        error_types = {}
        for error in self.errors:
            error_types[error.exception_type] = error_types.get(error.exception_type, 0) + 1
        
        most_common = sorted(
            self.error_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        return {
            "total_errors": len(self.errors),
            "error_types": error_types,
            "most_common": most_common,
            "recent_errors": self.errors[-5:] if len(self.errors) >= 5 else self.errors
        }
    
    def clear_errors(self):
        """Clear all aggregated errors"""
        self.errors.clear()
        self.error_counts.clear()

class BatchProcessor:
    """Process items in batches with error aggregation"""
    
    def __init__(self, batch_size: int = 10):
        self.batch_size = batch_size
        self.error_aggregator = ErrorAggregator()
    
    def process_batch(
        self, 
        items: List[Any], 
        processor: Callable[[Any], Any],
        continue_on_error: bool = True
    ) -> Dict[str, Any]:
        """Process items in batches with error handling"""
        results = []
        failed_items = []
        
        for i in range(0, len(items), self.batch_size):
            batch = items[i:i + self.batch_size]
            batch_results, batch_failures = self._process_single_batch(
                batch, processor, continue_on_error
            )
            results.extend(batch_results)
            failed_items.extend(batch_failures)
        
        return {
            "successful_results": results,
            "failed_items": failed_items,
            "error_summary": self.error_aggregator.get_error_summary(),
            "success_rate": len(results) / len(items) if items else 0
        }
    
    def _process_single_batch(
        self, 
        batch: List[Any], 
        processor: Callable[[Any], Any],
        continue_on_error: bool
    ) -> tuple:
        """Process a single batch"""
        results = []
        failures = []
        
        for item in batch:
            try:
                result = processor(item)
                results.append(result)
            except Exception as e:
                self.error_aggregator.add_error(
                    e, 
                    context={"item": str(item), "batch_size": len(batch)}
                )
                failures.append(item)
                
                if not continue_on_error:
                    raise BatchProcessingError(
                        f"Batch processing failed on item: {item}"
                    ) from e
        
        return results, failures

# Usage example
def risky_data_processor(item: Dict[str, Any]) -> Dict[str, Any]:
    """Simulate processing that might fail"""
    if item.get("id", 0) % 7 == 0:  # Fail on multiples of 7
        raise ValueError(f"Processing failed for item {item['id']}")
    
    return {"processed_id": item["id"], "status": "success"}

# Process data with error aggregation
processor = BatchProcessor(batch_size=5)
test_data = [{"id": i} for i in range(1, 21)]

results = processor.process_batch(
    test_data, 
    risky_data_processor, 
    continue_on_error=True
)

print(f"Success rate: {results['success_rate']:.2%}")
print(f"Error summary: {results['error_summary']}")
```

#### Async Exception Handling

```python
import asyncio
import aiohttp
from typing import List, Dict, Any, Optional, Coroutine
import logging

class AsyncErrorHandler:
    """Advanced async error handling patterns"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.semaphore = asyncio.Semaphore(10)  # Limit concurrent operations
    
    async def gather_with_error_handling(
        self, 
        coroutines: List[Coroutine],
        return_exceptions: bool = True,
        max_retries: int = 3
    ) -> List[Any]:
        """Gather coroutines with comprehensive error handling"""
        
        async def safe_execute(coro, retry_count=0):
            try:
                async with self.semaphore:
                    return await coro
            except Exception as e:
                if retry_count < max_retries:
                    self.logger.warning(f"Retry {retry_count + 1}/{max_retries} for {coro}")
                    await asyncio.sleep(2 ** retry_count)  # Exponential backoff
                    return await safe_execute(coro, retry_count + 1)
                else:
                    self.logger.error(f"Failed after {max_retries} retries: {e}")
                    if return_exceptions:
                        return e
                    raise
        
        # Execute all coroutines with error handling
        safe_coroutines = [safe_execute(coro) for coro in coroutines]
        return await asyncio.gather(*safe_coroutines, return_exceptions=return_exceptions)
    
    async def timeout_wrapper(
        self, 
        coro: Coroutine, 
        timeout: float,
        fallback_value: Any = None
    ) -> Any:
        """Wrap coroutine with timeout and fallback"""
        try:
            return await asyncio.wait_for(coro, timeout=timeout)
        except asyncio.TimeoutError:
            self.logger.warning(f"Operation timed out after {timeout}s")
            if fallback_value is not None:
                return fallback_value
            raise
    
    async def circuit_breaker_async(
        self,
        func: Callable,
        *args,
        failure_threshold: int = 5,
        timeout: float = 60.0,
        **kwargs
    ) -> Any:
        """Async circuit breaker implementation"""
        # This would integrate with the CircuitBreaker class from earlier
        # but adapted for async operations
        pass

class AsyncAPIClient:
    """Example async API client with robust error handling"""
    
    def __init__(self, base_url: str, timeout: float = 30.0):
        self.base_url = base_url
        self.timeout = timeout
        self.error_handler = AsyncErrorHandler()
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout)
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def fetch_data(self, endpoint: str) -> Dict[str, Any]:
        """Fetch data with comprehensive error handling"""
        if not self.session:
            raise RuntimeError("Client not initialized. Use async context manager.")
        
        url = f"{self.base_url}/{endpoint}"
        
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 404:
                    raise NotFoundError(f"Resource not found: {endpoint}")
                elif response.status == 429:
                    retry_after = response.headers.get('Retry-After', '60')
                    raise RateLimitError(f"Rate limited. Retry after {retry_after}s")
                elif response.status >= 500:
                    raise ServerError(f"Server error: {response.status}")
                else:
                    raise APIError(f"HTTP {response.status}: {await response.text()}")
                    
        except aiohttp.ClientError as e:
            raise ConnectionError(f"Network error: {e}") from e
        except asyncio.TimeoutError as e:
            raise TimeoutError(f"Request timeout: {url}") from e
    
    async def fetch_multiple(self, endpoints: List[str]) -> List[Dict[str, Any]]:
        """Fetch multiple endpoints concurrently"""
        coroutines = [self.fetch_data(endpoint) for endpoint in endpoints]
        results = await self.error_handler.gather_with_error_handling(coroutines)
        
        # Separate successful results from errors
        successful_results = []
        errors = []
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                errors.append({"endpoint": endpoints[i], "error": result})
            else:
                successful_results.append(result)
        
        if errors:
            self.error_handler.logger.warning(f"Failed to fetch {len(errors)} endpoints")
        
        return successful_results

# Usage example
async def main():
    async with AsyncAPIClient("https://api.example.com") as client:
        try:
            # Fetch single endpoint
            data = await client.fetch_data("users/123")
            print(f"User data: {data}")
            
            # Fetch multiple endpoints
            endpoints = ["users/1", "users/2", "users/3", "nonexistent"]
            results = await client.fetch_multiple(endpoints)
            print(f"Fetched {len(results)} successful results")
            
        except APIError as e:
            print(f"API error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the async example
# asyncio.run(main())
```

### Testing Exception Scenarios {#testing-exceptions}

Comprehensive testing strategies for exception handling code.

#### Unit Testing Exceptions

```python
import unittest
from unittest.mock import Mock, patch, MagicMock
import pytest
from typing import Any, Callable

class ExceptionTestCase(unittest.TestCase):
    """Base class for testing exception scenarios"""
    
    def setUp(self):
        self.validator = InputValidator()
        self.bank_account = BankAccount(100.0)
    
    def test_specific_exception_raised(self):
        """Test that specific exceptions are raised"""
        with self.assertRaises(ValidationError):
            self.validator.validate_email("invalid-email")
        
        with self.assertRaises(ValidationError) as context:
            self.validator.validate_age(-5)
        
        self.assertIn("negative", str(context.exception))
    
    def test_exception_chaining(self):
        """Test exception chaining is preserved"""
        with self.assertRaises(UserRegistrationError) as context:
            safe_user_registration({"email": "invalid"})
        
        # Check that original exception is chained
        self.assertIsInstance(context.exception.__cause__, ValidationError)
    
    def test_exception_message_content(self):
        """Test exception message contains expected information"""
        try:
            self.bank_account.withdraw(200.0)  # More than balance
            self.fail("Expected PreconditionError")
        except PreconditionError as e:
            self.assertIn("Insufficient funds", str(e))
    
    def test_no_exception_raised(self):
        """Test that no exception is raised in valid scenarios"""
        try:
            result = self.validator.validate_email("test@example.com")
            self.assertEqual(result, "test@example.com")
        except Exception:
            self.fail("validate_email raised an exception unexpectedly")
    
    def test_exception_with_mock(self):
        """Test exception handling with mocked dependencies"""
        with patch('builtins.open', side_effect=FileNotFoundError("File not found")):
            with self.assertRaises(ConfigurationError):
                DataProcessor("nonexistent.json")

class ParametrizedExceptionTests:
    """Pytest-style parametrized exception tests"""
    
    @pytest.mark.parametrize("invalid_email,expected_error", [
        ("", "cannot be empty"),
        ("invalid", "Invalid email format"),
        ("@example.com", "Invalid email format"),
        ("test@", "Invalid email format"),
        (123, "must be a string"),
        (None, "must be a string"),
    ])
    def test_email_validation_errors(self, invalid_email, expected_error):
        """Test various email validation scenarios"""
        validator = InputValidator()
        with pytest.raises(ValidationError, match=expected_error):
            validator.validate_email(invalid_email)
    
    @pytest.mark.parametrize("age,expected_error", [
        (-1, "cannot be negative"),
        (200, "unrealistic"),
        ("abc", "must be a number"),
        (None, "must be a number"),
    ])
    def test_age_validation_errors(self, age, expected_error):
        """Test various age validation scenarios"""
        validator = InputValidator()
        with pytest.raises(ValidationError, match=expected_error):
            validator.validate_age(age)

class MockExceptionTesting:
    """Advanced mocking for exception testing"""
    
    def test_retry_mechanism(self):
        """Test retry mechanism with mocked failures"""
        mock_func = Mock()
        mock_func.side_effect = [
            ConnectionError("First failure"),
            ConnectionError("Second failure"),
            {"status": "success"}  # Third attempt succeeds
        ]
        
        @retry(max_attempts=3, delay=0.1)
        def test_function():
            return mock_func()
        
        result = test_function()
        self.assertEqual(result, {"status": "success"})
        self.assertEqual(mock_func.call_count, 3)
    
    def test_circuit_breaker_behavior(self):
        """Test circuit breaker state transitions"""
        mock_service = Mock()
        mock_service.side_effect = APIError("Service unavailable")
        
        @CircuitBreaker(failure_threshold=2, timeout=1.0)
        def failing_service():
            return mock_service()
        
        # First two calls should fail and trigger circuit breaker
        with self.assertRaises(APIError):
            failing_service()
        with self.assertRaises(APIError):
            failing_service()
        
        # Third call should raise CircuitBreakerOpenError
        with self.assertRaises(CircuitBreakerOpenError):
            failing_service()
    
    def test_error_aggregation(self):
        """Test error aggregation functionality"""
        aggregator = ErrorAggregator()
        
        # Add various errors
        errors = [
            ValueError("Error 1"),
            TypeError("Error 2"),
            ValueError("Error 1"),  # Duplicate
        ]
        
        for error in errors:
            aggregator.add_error(error)
        
        summary = aggregator.get_error_summary()
        self.assertEqual(summary["total_errors"], 3)
        self.assertEqual(summary["error_types"]["ValueError"], 2)
        self.assertEqual(summary["error_types"]["TypeError"], 1)

# Property-based testing for exception scenarios
class PropertyBasedExceptionTests:
    """Property-based testing using hypothesis"""
    
    @pytest.mark.parametrize("test_input", [
        pytest.param("", id="empty_string"),
        pytest.param("a", id="too_short"),
        pytest.param("no_at_symbol", id="missing_at"),
        pytest.param("@domain.com", id="missing_local"),
        pytest.param("user@", id="missing_domain"),
    ])
    def test_email_validation_properties(self, test_input):
        """Property-based test for email validation"""
        validator = InputValidator()
        
        # Property: Invalid emails should always raise ValidationError
        with pytest.raises(ValidationError):
            validator.validate_email(test_input)
    
    def test_bank_account_invariants(self):
        """Test bank account invariants under various operations"""
        account = BankAccount(100.0)
        initial_balance = account.balance
        
        # Property: Balance should never go negative
        with pytest.raises(PreconditionError):
            account.withdraw(initial_balance + 1)
        
        # Property: Balance should remain unchanged after failed operation
        self.assertEqual(account.balance, initial_balance)
```

### Production Error Handling {#production-handling}

Strategies for handling errors in production environments.

#### Monitoring and Alerting

```python
import logging
import json
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ProductionErrorHandler:
    """Production-ready error handling with monitoring"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = self._setup_production_logging()
        self.alert_thresholds = config.get("alert_thresholds", {})
        self.error_counts = {}
        self.last_alert_times = {}
    
    def _setup_production_logging(self) -> logging.Logger:
        """Setup production logging configuration"""
        logger = logging.getLogger("production")
        logger.setLevel(logging.INFO)
        
        # File handler with rotation
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler(
            "production.log",
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        
        # Syslog handler for centralized logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler(address=('localhost', 514))
        
        # JSON formatter for structured logging
        class JSONFormatter(logging.Formatter):
            def format(self, record):
                log_entry = {
                    'timestamp': datetime.utcnow().isoformat(),
                    'level': record.levelname,
                    'message': record.getMessage(),
                    'module': record.module,
                    'function': record.funcName,
                    'line': record.lineno,
                    'process': record.process,
                    'thread': record.thread
                }
                
                if record.exc_info:
                    log_entry['exception'] = self.formatException(record.exc_info)
                
                return json.dumps(log_entry)
        
        formatter = JSONFormatter()
        file_handler.setFormatter(formatter)
        syslog_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(syslog_handler)
        
        return logger
    
    def handle_error(
        self, 
        error: Exception, 
        context: Dict[str, Any] = None,
        severity: str = "ERROR",
        should_alert: bool = True
    ):
        """Handle production errors with monitoring and alerting"""
        
        error_key = f"{type(error).__name__}:{str(error)}"
        current_time = datetime.utcnow()
        
        # Track error frequency
        if error_key not in self.error_counts:
            self.error_counts[error_key] = {"count": 0, "first_seen": current_time}
        
        self.error_counts[error_key]["count"] += 1
        self.error_counts[error_key]["last_seen"] = current_time
        
        # Log the error
        self.logger.error(
            f"Production error: {error}",
            extra={
                "error_type": type(error).__name__,
                "error_message": str(error),
                "context": context or {},
                "severity": severity,
                "error_count": self.error_counts[error_key]["count"]
            },
            exc_info=True
        )
        
        # Check if alerting is needed
        if should_alert and self._should_send_alert(error_key, severity):
            self._send_alert(error, context, severity)
    
    def _should_send_alert(self, error_key: str, severity: str) -> bool:
        """Determine if an alert should be sent"""
        # Check error frequency threshold
        error_info = self.error_counts[error_key]
        threshold = self.alert_thresholds.get(severity, {"count": 5, "window": 300})
        
        time_window = timedelta(seconds=threshold["window"])
        if (error_info["count"] >= threshold["count"] and 
            error_info["last_seen"] - error_info["first_seen"] <= time_window):
            
            # Check if we've already alerted recently
            last_alert = self.last_alert_times.get(error_key)
            alert_cooldown = timedelta(minutes=30)
            
            if not last_alert or datetime.utcnow() - last_alert > alert_cooldown:
                self.last_alert_times[error_key] = datetime.utcnow()
                return True
        
        return False
    
    def _send_alert(self, error: Exception, context: Dict[str, Any], severity: str):
        """Send alert notification"""
        try:
            # Email alert
            self._send_email_alert(error, context, severity)
            
            # Slack/webhook alert (if configured)
            if "webhook_url" in self.config:
                self._send_webhook_alert(error, context, severity)
                
        except Exception as e:
            self.logger.error(f"Failed to send alert: {e}")
    
    def _send_email_alert(self, error: Exception, context: Dict[str, Any], severity: str):
        """Send email alert"""
        email_config = self.config.get("email", {})
        if not email_config:
            return
        
        msg = MIMEMultipart()
        msg['From'] = email_config['from']
        msg['To'] = ', '.join(email_config['to'])
        msg['Subject'] = f"[{severity}] Production Error Alert"
        
        body = f"""
        Production Error Alert
        
        Error Type: {type(error).__name__}
        Error Message: {str(error)}
        Severity: {severity}
        Timestamp: {datetime.utcnow().isoformat()}
        
        Context:
        {json.dumps(context, indent=2)}
        
        Error Count: {self.error_counts.get(f"{type(error).__name__}:{str(error)}", {}).get("count", 1)}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
            if email_config.get('use_tls'):
                server.starttls()
            if email_config.get('username'):
                server.login(email_config['username'], email_config['password'])
            server.send_message(msg)
    
    def get_error_metrics(self) -> Dict[str, Any]:
        """Get error metrics for monitoring dashboard"""
        current_time = datetime.utcnow()
        
        # Calculate error rates
        recent_errors = {}
        for error_key, info in self.error_counts.items():
            if current_time - info["last_seen"] <= timedelta(hours=1):
                recent_errors[error_key] = info
        
        return {
            "total_unique_errors": len(self.error_counts),
            "recent_errors_1h": len(recent_errors),
            "top_errors": sorted(
                self.error_counts.items(),
                key=lambda x: x[1]["count"],
                reverse=True
            )[:10],
            "error_rate_1h": sum(info["count"] for info in recent_errors.values())
        }

# Health check endpoint for monitoring
class HealthCheckHandler:
    """Health check handler for production monitoring"""
    
    def __init__(self, error_handler: ProductionErrorHandler):
        self.error_handler = error_handler
        self.start_time = datetime.utcnow()
    
    def get_health_status(self) -> Dict[str, Any]:
        """Get application health status"""
        try:
            # Check critical dependencies
            db_status = self._check_database()
            cache_status = self._check_cache()
            external_api_status = self._check_external_apis()
            
            # Get error metrics
            error_metrics = self.error_handler.get_error_metrics()
            
            # Determine overall health
            is_healthy = all([
                db_status["healthy"],
                cache_status["healthy"],
                external_api_status["healthy"],
                error_metrics["recent_errors_1h"] < 100  # Threshold
            ])
            
            return {
                "status": "healthy" if is_healthy else "unhealthy",
                "timestamp": datetime.utcnow().isoformat(),
                "uptime": str(datetime.utcnow() - self.start_time),
                "dependencies": {
                    "database": db_status,
                    "cache": cache_status,
                    "external_apis": external_api_status
                },
                "error_metrics": error_metrics
            }
            
        except Exception as e:
            self.error_handler.handle_error(e, {"component": "health_check"})
            return {
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
    
    def _check_database(self) -> Dict[str, Any]:
        """Check database connectivity"""
        try:
            # Implement actual database check
            return {"healthy": True, "response_time_ms": 50}
        except Exception as e:
            return {"healthy": False, "error": str(e)}
    
    def _check_cache(self) -> Dict[str, Any]:
        """Check cache connectivity"""
        try:
            # Implement actual cache check
            return {"healthy": True, "response_time_ms": 10}
        except Exception as e:
            return {"healthy": False, "error": str(e)}
    
    def _check_external_apis(self) -> Dict[str, Any]:
        """Check external API connectivity"""
        try:
            # Implement actual API checks
            return {"healthy": True, "apis_checked": 3, "all_responding": True}
        except Exception as e:
            return {"healthy": False, "error": str(e)}
```

### Best Practices Summary {#best-practices}

A comprehensive summary of Python error handling best practices for all skill levels.

#### Core Principles

1. **Fail Fast, Fail Clearly**
   ```python
   # Good: Clear, immediate failure
   def process_user_data(user_data):
       if not user_data:
           raise ValueError("User data cannot be empty")
       if "email" not in user_data:
           raise ValueError("Email is required")
       # Continue processing...
   
   # Bad: Silent failure or unclear error
   def process_user_data(user_data):
       try:
           email = user_data.get("email", "")
           if email:
               # Process email...
               pass
       except:
           pass  # Silent failure
   ```

2. **Use Specific Exception Types**
   ```python
   # Good: Specific exceptions
   try:
       user_id = int(user_input)
       user = database.get_user(user_id)
   except ValueError:
       print("Invalid user ID format")
   except UserNotFoundError:
       print("User does not exist")
   except DatabaseError:
       print("Database connection failed")
   
   # Bad: Generic exception catching
   try:
       user_id = int(user_input)
       user = database.get_user(user_id)
   except Exception as e:
       print(f"Something went wrong: {e}")
   ```

3. **Preserve Exception Context**
   ```python
   # Good: Preserve context with chaining
   try:
       data = json.loads(json_string)
   except json.JSONDecodeError as e:
       raise ConfigurationError("Invalid configuration format") from e
   
   # Bad: Lose original context
   try:
       data = json.loads(json_string)
   except json.JSONDecodeError:
       raise ConfigurationError("Invalid configuration format")
   ```

#### Error Handling Patterns by Use Case

| Use Case | Recommended Pattern | Example |
|----------|-------------------|---------|
| **Input Validation** | Specific validation exceptions | `ValidationError`, `ValueError` |
| **External APIs** | Retry with circuit breaker | `@retry`, `@CircuitBreaker` |
| **File Operations** | Context managers | `with open()`, custom context managers |
| **Database Operations** | Transaction rollback | Database context managers |
| **Async Operations** | Timeout and cancellation | `asyncio.wait_for()`, `asyncio.gather()` |
| **Batch Processing** | Error aggregation | Collect errors, continue processing |
| **Production Systems** | Monitoring and alerting | Structured logging, health checks |

#### Exception Hierarchy Design

```python
# Well-designed exception hierarchy
class ApplicationError(Exception):
    """Base application exception"""
    pass

class ValidationError(ApplicationError):
    """Data validation failed"""
    pass

class BusinessLogicError(ApplicationError):
    """Business rule violation"""
    pass

class ExternalServiceError(ApplicationError):
    """External service failure"""
    pass

class DatabaseError(ExternalServiceError):
    """Database operation failed"""
    pass

class APIError(ExternalServiceError):
    """External API failure"""
    pass

# Usage allows granular handling
try:
    process_business_logic()
except ValidationError:
    # Handle validation specifically
    pass
except BusinessLogicError:
    # Handle business logic specifically
    pass
except ExternalServiceError:
    # Handle any external service error
    pass
except ApplicationError:
    # Handle any application error
    pass
```

#### Performance Guidelines

1. **Use EAFP over LBYL**
   ```python
   # Good: Easier to Ask for Forgiveness than Permission
   try:
       return my_dict[key]
   except KeyError:
       return default_value
   
   # Less efficient: Look Before You Leap
   if key in my_dict:
       return my_dict[key]
   else:
       return default_value
   ```

2. **Avoid Exceptions in Hot Paths**
   ```python
   # Good: Use return values for expected conditions
   def find_user(user_id):
       user = database.query(user_id)
       if user is None:
           return None, "User not found"
       return user, None
   
   # Bad: Exceptions for control flow
   def find_user(user_id):
       try:
           return database.get_user(user_id)  # Raises if not found
       except UserNotFoundError:
           return None
   ```

3. **Cache Exception Information**
   ```python
   class ErrorCache:
       def __init__(self, ttl=300):
           self.cache = {}
           self.ttl = ttl
       
       def should_process_error(self, error_key):
           now = time.time()
           if error_key in self.cache:
               if now - self.cache[error_key] < self.ttl:
                   return False  # Skip processing
           self.cache[error_key] = now
           return True
   ```

#### Logging Best Practices

```python
import logging
import json
from datetime import datetime

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def log_error_properly(error, context=None):
    """Proper error logging with context"""
    logger.error(
        f"Error occurred: {type(error).__name__}: {error}",
        extra={
            'error_type': type(error).__name__,
            'error_message': str(error),
            'context': context or {},
            'timestamp': datetime.utcnow().isoformat()
        },
        exc_info=True  # Include stack trace
    )

# Usage
try:
    risky_operation()
except Exception as e:
    log_error_properly(e, {'user_id': 123, 'operation': 'data_processing'})
    raise  # Re-raise if needed
```

#### Testing Guidelines

```python
import pytest
from unittest.mock import Mock, patch

class TestErrorHandling:
    """Comprehensive error handling tests"""
    
    def test_specific_exceptions(self):
        """Test specific exception types are raised"""
        with pytest.raises(ValidationError, match="Invalid email"):
            validate_email("invalid")
    
    def test_exception_chaining(self):
        """Test exception chaining is preserved"""
        with pytest.raises(ProcessingError) as exc_info:
            process_invalid_data()
        
        assert isinstance(exc_info.value.__cause__, ValidationError)
    
    def test_error_recovery(self):
        """Test error recovery mechanisms"""
        mock_service = Mock(side_effect=[
            ConnectionError("Failed"),
            ConnectionError("Failed"),
            {"status": "success"}
        ])
        
        @retry(max_attempts=3)
        def test_function():
            return mock_service()
        
        result = test_function()
        assert result == {"status": "success"}
        assert mock_service.call_count == 3
    
    @patch('external_service.api_call')
    def test_external_service_failure(self, mock_api):
        """Test handling of external service failures"""
        mock_api.side_effect = TimeoutError("Service timeout")
        
        with pytest.raises(ExternalServiceError):
            call_external_service()
```

#### Production Checklist

- [ ] **Logging**: Structured logging with appropriate levels
- [ ] **Monitoring**: Error rate and frequency monitoring
- [ ] **Alerting**: Automated alerts for critical errors
- [ ] **Health Checks**: Endpoint for service health monitoring
- [ ] **Graceful Degradation**: Fallback mechanisms for non-critical features
- [ ] **Circuit Breakers**: Protection against cascading failures
- [ ] **Retry Logic**: Exponential backoff for transient failures
- [ ] **Error Aggregation**: Batch error processing for performance
- [ ] **Documentation**: Clear error handling documentation
- [ ] **Testing**: Comprehensive exception scenario testing

#### Common Anti-Patterns to Avoid

1. **Bare Except Clauses**
   ```python
   # Bad
   try:
       risky_operation()
   except:  # Catches everything, including KeyboardInterrupt
       pass
   
   # Good
   try:
       risky_operation()
   except SpecificError:
       handle_specific_error()
   ```

2. **Swallowing Exceptions**
   ```python
   # Bad
   try:
       important_operation()
   except Exception:
       pass  # Silent failure
   
   # Good
   try:
       important_operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise  # Or handle appropriately
   ```

3. **Using Exceptions for Control Flow**
   ```python
   # Bad
   try:
       while True:
           item = iterator.next()
           process(item)
   except StopIteration:
       pass
   
   # Good
   for item in iterator:
       process(item)
   ```

4. **Not Cleaning Up Resources**
   ```python
   # Bad
   file = open("data.txt")
   try:
       process_file(file)
   except Exception:
       handle_error()
   # File might not be closed
   
   # Good
   try:
       with open("data.txt") as file:
           process_file(file)
   except Exception:
       handle_error()
   # File is always closed
   ```

---

## Conclusion

Effective error handling is crucial for building robust, maintainable Python applications. This tutorial covered:

- **Beginner Level**: Basic exception handling, common exception types, and exception hierarchy
- **Intermediate Level**: Advanced patterns, custom exceptions, exception chaining, and logging
- **Advanced Level**: Context managers, defensive programming, and error recovery strategies
- **Expert Level**: Advanced patterns, async handling, testing, and production considerations

### Key Takeaways

1. **Start Simple**: Begin with basic try-except blocks and gradually adopt more sophisticated patterns
2. **Be Specific**: Use specific exception types and provide meaningful error messages
3. **Preserve Context**: Use exception chaining to maintain error context
4. **Plan for Production**: Implement monitoring, alerting, and graceful degradation
5. **Test Thoroughly**: Write comprehensive tests for exception scenarios
6. **Document Well**: Clearly document error handling behavior and recovery strategies

### Next Steps

1. **Practice**: Implement error handling in your current projects
2. **Review**: Audit existing code for error handling improvements
3. **Monitor**: Set up error monitoring and alerting in production
4. **Learn**: Stay updated with Python error handling best practices
5. **Share**: Teach others and contribute to error handling discussions

Remember: Good error handling is not just about preventing crashes—it's about creating applications that are resilient, debuggable, and provide excellent user experiences even when things go wrong.

### Additional Resources

- [Python Official Documentation - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [PEP 3134 - Exception Chaining and Embedded Tracebacks](https://www.python.org/dev/peps/pep-3134/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Testing with pytest](https://docs.pytest.org/)
- [Async Programming in Python](https://docs.python.org/3/library/asyncio.html)

---

*This tutorial is part of the Python Best Practices series. For more tutorials and examples, explore the other sections in this repository.*
