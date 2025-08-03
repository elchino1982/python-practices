"""Question: Master the fundamentals of exception handling in Python.

Learn how to properly handle errors, create custom exceptions, and implement
robust error handling strategies in your Python applications.

Requirements:
1. Understand basic try-except blocks
2. Learn about different exception types
3. Create custom exception classes
4. Implement proper error logging
5. Use finally blocks for cleanup
6. Handle multiple exceptions appropriately

Example usage:
    try:
        result = divide_numbers(10, 0)
    except ZeroDivisionError as e:
        logger.error(f"Division error: {e}")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what exceptions you might encounter
# - Start with simple try-except blocks
# - Test your code with different error scenarios
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
# - What are the most common exceptions in Python?
# - How do you catch specific vs general exceptions?
# - When should you create custom exceptions?
# - How do you properly log errors?
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


# Step 1: Basic try-except blocks and common exceptions
# ===============================================================================

# Explanation:
# Exception handling starts with understanding basic try-except blocks.
# Let's explore the most common exceptions and how to handle them.

import logging

def basic_exception_handling():
    """Demonstrate basic exception handling patterns."""
    
    # Basic try-except block
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    print("Program continues...")

def handle_file_operations():
    """Handle file operation exceptions."""
    
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except IOError:
        print("Error: I/O operation failed")

def handle_list_operations():
    """Handle list operation exceptions."""
    
    my_list = [1, 2, 3, 4, 5]
    
    try:
        index = int(input("Enter list index: "))
        value = my_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Please enter a valid integer")

# Test basic exception handling
print("=== Step 1: Basic Exception Handling ===")
print("Testing basic exception patterns...")

# What we accomplished in this step:
# - Learned basic try-except syntax
# - Handled common exceptions (ValueError, ZeroDivisionError, FileNotFoundError)
# - Demonstrated that programs continue after handling exceptions


# Step 2: Multiple exception handling and exception information
# ===============================================================================

# Explanation:
# Learn how to handle multiple exceptions in different ways and access
# exception information for better error reporting.

import logging

def basic_exception_handling():
    """Demonstrate basic exception handling patterns."""
    
    # Basic try-except block
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    print("Program continues...")

def handle_file_operations():
    """Handle file operation exceptions."""
    
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except IOError:
        print("Error: I/O operation failed")

def handle_list_operations():
    """Handle list operation exceptions."""
    
    my_list = [1, 2, 3, 4, 5]
    
    try:
        index = int(input("Enter list index: "))
        value = my_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Please enter a valid integer")

def handle_multiple_exceptions_separately():
    """Handle multiple exceptions with detailed error information."""
    
    try:
        data = input("Enter data to process: ")
        number = int(data)
        result = 100 / number
        my_list = [1, 2, 3]
        value = my_list[number]
        print(f"Success: {result}, {value}")
        
    except ValueError as e:
        print(f"ValueError occurred: {e}")
        print(f"Exception type: {type(e).__name__}")
        
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")
        print("Cannot divide by zero!")
        
    except IndexError as e:
        print(f"IndexError occurred: {e}")
        print("List index is out of range")

def handle_multiple_exceptions_together():
    """Handle multiple exceptions with the same handler."""
    
    try:
        data = input("Enter a number: ")
        number = int(data)
        result = 50 / number
        items = ["a", "b", "c"]
        item = items[number]
        print(f"Result: {result}, Item: {item}")
        
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"An error occurred: {type(e).__name__}")
        print(f"Error message: {e}")
        print("Please check your input and try again")

def handle_with_general_exception():
    """Use general exception handler as fallback."""
    
    try:
        # Simulate various operations that might fail
        operation = input("Enter operation (divide/access/convert): ")
        
        if operation == "divide":
            result = 10 / 0  # This will raise ZeroDivisionError
        elif operation == "access":
            my_list = [1, 2, 3]
            value = my_list[10]  # This will raise IndexError
        elif operation == "convert":
            number = int("not_a_number")  # This will raise ValueError
        else:
            raise RuntimeError("Unknown operation")
            
    except ZeroDivisionError:
        print("Specific handler: Cannot divide by zero")
    except IndexError:
        print("Specific handler: Index out of range")
    except Exception as e:
        print(f"General handler caught: {type(e).__name__}")
        print(f"Error message: {e}")

# Test multiple exception handling
print("\n=== Step 2: Multiple Exception Handling ===")
print("Testing multiple exception patterns...")

# What we accomplished in this step:
# - Learned to handle multiple exceptions separately and together
# - Accessed exception information using 'as e' syntax
# - Used general Exception handler as fallback
# - Demonstrated exception type and message access


# Step 3: Custom exceptions and exception hierarchies
# ===============================================================================

# Explanation:
# Create custom exception classes to represent specific error conditions
# in your application. This makes error handling more precise and meaningful.

import logging

def basic_exception_handling():
    """Demonstrate basic exception handling patterns."""
    
    # Basic try-except block
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    print("Program continues...")

def handle_file_operations():
    """Handle file operation exceptions."""
    
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except IOError:
        print("Error: I/O operation failed")

def handle_list_operations():
    """Handle list operation exceptions."""
    
    my_list = [1, 2, 3, 4, 5]
    
    try:
        index = int(input("Enter list index: "))
        value = my_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Please enter a valid integer")

def handle_multiple_exceptions_separately():
    """Handle multiple exceptions with detailed error information."""
    
    try:
        data = input("Enter data to process: ")
        number = int(data)
        result = 100 / number
        my_list = [1, 2, 3]
        value = my_list[number]
        print(f"Success: {result}, {value}")
        
    except ValueError as e:
        print(f"ValueError occurred: {e}")
        print(f"Exception type: {type(e).__name__}")
        
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")
        print("Cannot divide by zero!")
        
    except IndexError as e:
        print(f"IndexError occurred: {e}")
        print("List index is out of range")

def handle_multiple_exceptions_together():
    """Handle multiple exceptions with the same handler."""
    
    try:
        data = input("Enter a number: ")
        number = int(data)
        result = 50 / number
        items = ["a", "b", "c"]
        item = items[number]
        print(f"Result: {result}, Item: {item}")
        
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"An error occurred: {type(e).__name__}")
        print(f"Error message: {e}")
        print("Please check your input and try again")

def handle_with_general_exception():
    """Use general exception handler as fallback."""
    
    try:
        # Simulate various operations that might fail
        operation = input("Enter operation (divide/access/convert): ")
        
        if operation == "divide":
            result = 10 / 0  # This will raise ZeroDivisionError
        elif operation == "access":
            my_list = [1, 2, 3]
            value = my_list[10]  # This will raise IndexError
        elif operation == "convert":
            number = int("not_a_number")  # This will raise ValueError
        else:
            raise RuntimeError("Unknown operation")
            
    except ZeroDivisionError:
        print("Specific handler: Cannot divide by zero")
    except IndexError:
        print("Specific handler: Index out of range")
    except Exception as e:
        print(f"General handler caught: {type(e).__name__}")
        print(f"Error message: {e}")

# Custom Exception Classes
class BankingError(Exception):
    """Base exception for banking operations."""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds."""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance ${balance}, attempted ${amount}")

class InvalidAccountError(BankingError):
    """Raised when account number is invalid."""
    
    def __init__(self, account_number):
        self.account_number = account_number
        super().__init__(f"Invalid account number: {account_number}")

class AccountLockedError(BankingError):
    """Raised when account is locked."""
    
    def __init__(self, account_number, reason="Security reasons"):
        self.account_number = account_number
        self.reason = reason
        super().__init__(f"Account {account_number} is locked: {reason}")

class BankAccount:
    """Simple bank account class to demonstrate custom exceptions."""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.is_locked = False
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if self.is_locked:
            raise AccountLockedError(self.account_number)
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        """Deposit money to account."""
        if self.is_locked:
            raise AccountLockedError(self.account_number)
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return self.balance
    
    def lock_account(self, reason="Security reasons"):
        """Lock the account."""
        self.is_locked = True

def test_custom_exceptions():
    """Test custom exception handling."""
    
    # Create a bank account
    account = BankAccount("12345", 100)
    
    try:
        print(f"Initial balance: ${account.balance}")
        
        # Try to withdraw more than balance
        account.withdraw(150)
        
    except InsufficientFundsError as e:
        print(f"Banking error: {e}")
        print(f"Current balance: ${e.balance}")
        print(f"Attempted amount: ${e.amount}")
    
    try:
        # Lock account and try to deposit
        account.lock_account("Suspicious activity")
        account.deposit(50)
        
    except AccountLockedError as e:
        print(f"Account error: {e}")
        print(f"Account: {e.account_number}")
        print(f"Reason: {e.reason}")
    
    except BankingError as e:
        print(f"General banking error: {e}")

# Test custom exceptions
print("\n=== Step 3: Custom Exceptions ===")
print("Testing custom exception classes...")
test_custom_exceptions()

# What we accomplished in this step:
# - Created custom exception hierarchy with base and specific exceptions
# - Added custom attributes to exception classes
# - Demonstrated how custom exceptions make error handling more specific
# - Showed exception inheritance and polymorphism


# Step 4: Finally blocks and proper logging
# ===============================================================================

# Explanation:
# Learn to use finally blocks for cleanup operations and implement proper
# error logging for production applications.

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

def basic_exception_handling():
    """Demonstrate basic exception handling patterns."""
    
    # Basic try-except block
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    print("Program continues...")

def handle_file_operations():
    """Handle file operation exceptions."""
    
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except IOError:
        print("Error: I/O operation failed")

def handle_list_operations():
    """Handle list operation exceptions."""
    
    my_list = [1, 2, 3, 4, 5]
    
    try:
        index = int(input("Enter list index: "))
        value = my_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Please enter a valid integer")

def handle_multiple_exceptions_separately():
    """Handle multiple exceptions with detailed error information."""
    
    try:
        data = input("Enter data to process: ")
        number = int(data)
        result = 100 / number
        my_list = [1, 2, 3]
        value = my_list[number]
        print(f"Success: {result}, {value}")
        
    except ValueError as e:
        print(f"ValueError occurred: {e}")
        print(f"Exception type: {type(e).__name__}")
        
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")
        print("Cannot divide by zero!")
        
    except IndexError as e:
        print(f"IndexError occurred: {e}")
        print("List index is out of range")

def handle_multiple_exceptions_together():
    """Handle multiple exceptions with the same handler."""
    
    try:
        data = input("Enter a number: ")
        number = int(data)
        result = 50 / number
        items = ["a", "b", "c"]
        item = items[number]
        print(f"Result: {result}, Item: {item}")
        
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"An error occurred: {type(e).__name__}")
        print(f"Error message: {e}")
        print("Please check your input and try again")

def handle_with_general_exception():
    """Use general exception handler as fallback."""
    
    try:
        # Simulate various operations that might fail
        operation = input("Enter operation (divide/access/convert): ")
        
        if operation == "divide":
            result = 10 / 0  # This will raise ZeroDivisionError
        elif operation == "access":
            my_list = [1, 2, 3]
            value = my_list[10]  # This will raise IndexError
        elif operation == "convert":
            number = int("not_a_number")  # This will raise ValueError
        else:
            raise RuntimeError("Unknown operation")
            
    except ZeroDivisionError:
        print("Specific handler: Cannot divide by zero")
    except IndexError:
        print("Specific handler: Index out of range")
    except Exception as e:
        print(f"General handler caught: {type(e).__name__}")
        print(f"Error message: {e}")

# Custom Exception Classes
class BankingError(Exception):
    """Base exception for banking operations."""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds."""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance ${balance}, attempted ${amount}")

class InvalidAccountError(BankingError):
    """Raised when account number is invalid."""
    
    def __init__(self, account_number):
        self.account_number = account_number
        super().__init__(f"Invalid account number: {account_number}")

class AccountLockedError(BankingError):
    """Raised when account is locked."""
    
    def __init__(self, account_number, reason="Security reasons"):
        self.account_number = account_number
        self.reason = reason
        super().__init__(f"Account {account_number} is locked: {reason}")

class BankAccount:
    """Simple bank account class to demonstrate custom exceptions."""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.is_locked = False
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if self.is_locked:
            raise AccountLockedError(self.account_number)
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        """Deposit money to account."""
        if self.is_locked:
            raise AccountLockedError(self.account_number)
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return self.balance
    
    def lock_account(self, reason="Security reasons"):
        """Lock the account."""
        self.is_locked = True

def test_custom_exceptions():
    """Test custom exception handling."""
    
    # Create a bank account
    account = BankAccount("12345", 100)
    
    try:
        print(f"Initial balance: ${account.balance}")
        
        # Try to withdraw more than balance
        account.withdraw(150)
        
    except InsufficientFundsError as e:
        print(f"Banking error: {e}")
        print(f"Current balance: ${e.balance}")
        print(f"Attempted amount: ${e.amount}")
    
    try:
        # Lock account and try to deposit
        account.lock_account("Suspicious activity")
        account.deposit(50)
        
    except AccountLockedError as e:
        print(f"Account error: {e}")
        print(f"Account: {e.account_number}")
        print(f"Reason: {e.reason}")
    
    except BankingError as e:
        print(f"General banking error: {e}")

def file_operations_with_finally():
    """Demonstrate finally block with file operations."""
    
    file_handle = None
    try:
        logger.info("Attempting to open file")
        file_handle = open("test_file.txt", "w")
        file_handle.write("Hello, World!")
        
        # Simulate an error
        result = 10 / 0
        
    except ZeroDivisionError as e:
        logger.error(f"Math error occurred: {e}")
        print("Error: Division by zero")
        
    except IOError as e:
        logger.error(f"File operation failed: {e}")
        print("Error: File operation failed")
        
    finally:
        # This always executes, even if an exception occurs
        if file_handle:
            file_handle.close()
            logger.info("File closed successfully")
            print("File has been closed")
        print("Cleanup completed")

def database_connection_simulation():
    """Simulate database connection with proper cleanup."""
    
    connection = None
    transaction_started = False
    
    try:
        logger.info("Establishing database connection")
        connection = "DB_CONNECTION"  # Simulate connection
        print("Database connected")
        
        logger.info("Starting transaction")
        transaction_started = True
        print("Transaction started")
        
        # Simulate database operations
        if True:  # Simulate error condition
            raise RuntimeError("Database operation failed")
        
        logger.info("Committing transaction")
        print("Transaction committed")
        
    except RuntimeError as e:
        logger.error(f"Database error: {e}")
        if transaction_started:
            logger.info("Rolling back transaction")
            print("Transaction rolled back")
        
    finally:
        if connection:
            logger.info("Closing database connection")
            print("Database connection closed")

def comprehensive_logging_example():
    """Demonstrate comprehensive error logging."""
    
    try:
        logger.info("Starting complex operation")
        
        # Simulate various operations
        data = [1, 2, 3, 4, 5]
        index = 10
        
        logger.debug(f"Accessing index {index} in list of length {len(data)}")
        value = data[index]
        
    except IndexError as e:
        logger.error(f"Index error: {e}", exc_info=True)
        logger.warning("Falling back to default value")
        value = 0
        
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        raise  # Re-raise unexpected exceptions
        
    else:
        logger.info(f"Operation completed successfully, value: {value}")
        
    finally:
        logger.info("Operation cleanup completed")

def advanced_error_context():
    """Demonstrate error handling with context information."""
    
    operation_id = f"OP_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    try:
        logger.info(f"Starting operation {operation_id}")
        
        # Simulate operation that might fail
        numbers = [1, 2, 3]
        result = numbers[5]  # This will fail
        
    except IndexError as e:
        logger.error(
            f"Operation {operation_id} failed: {e}",
            extra={
                'operation_id': operation_id,
                'list_length': len(numbers),
                'attempted_index': 5
            }
        )
        
    except Exception as e:
        logger.critical(
            f"Unexpected error in operation {operation_id}: {e}",
            extra={'operation_id': operation_id},
            exc_info=True
        )

# Test finally blocks and logging
print("\n=== Step 4: Finally Blocks and Logging ===")
print("Testing finally blocks and proper logging...")

file_operations_with_finally()
print()
database_connection_simulation()
print()
comprehensive_logging_example()
print()
advanced_error_context()

# What we accomplished in this step:
# - Learned to use finally blocks for guaranteed cleanup
# - Implemented proper logging with different levels
# - Added context information to log messages
# - Demonstrated resource management patterns
# - Showed how to log exceptions with stack traces


# Step 5: Advanced exception handling patterns and best practices
# ===============================================================================

# Explanation:
# Learn advanced patterns like context managers, exception chaining,
# and comprehensive error handling strategies for production applications.

import logging
import sys
from datetime import datetime
from contextlib import contextmanager
import traceback

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

def basic_exception_handling():
    """Demonstrate basic exception handling patterns."""
    
    # Basic try-except block
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    print("Program continues...")

def handle_file_operations():
    """Handle file operation exceptions."""
    
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except IOError:
        print("Error: I/O operation failed")

def handle_list_operations():
    """Handle list operation exceptions."""
    
    my_list = [1, 2, 3, 4, 5]
    
    try:
        index = int(input("Enter list index: "))
        value = my_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print("Error: Index out of range")
    except ValueError:
        print("Error: Please enter a valid integer")

def handle_multiple_exceptions_separately():
    """Handle multiple exceptions with detailed error information."""
    
    try:
        data = input("Enter data to process: ")
        number = int(data)
        result = 100 / number
        my_list = [1, 2, 3]
        value = my_list[number]
        print(f"Success: {result}, {value}")
        
    except ValueError as e:
        print(f"ValueError occurred: {e}")
        print(f"Exception type: {type(e).__name__}")
        
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")
        print("Cannot divide by zero!")
        
    except IndexError as e:
        print(f"IndexError occurred: {e}")
        print("List index is out of range")

def handle_multiple_exceptions_together():
    """Handle multiple exceptions with the same handler."""
    
    try:
        data = input("Enter a number: ")
        number = int(data)
        result = 50 / number
        items = ["a", "b", "c"]
        item = items[number]
        print(f"Result: {result}, Item: {item}")
        
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(f"An error occurred: {type(e).__name__}")
        print(f"Error message: {e}")
        print("Please check your input and try again")

def handle_with_general_exception():
    """Use general exception handler as fallback."""
    
    try:
        # Simulate various operations that might fail
        operation = input("Enter operation (divide/access/convert): ")
        
        if operation == "divide":
            result = 10 / 0  # This will raise ZeroDivisionError
        elif operation == "access":
            my_list = [1, 2, 3]
            value = my_list[10]  # This will raise IndexError
        elif operation == "convert":
            number = int("not_a_number")  # This will raise ValueError
        else:
            raise RuntimeError("Unknown operation")
            
    except ZeroDivisionError:
        print("Specific handler: Cannot divide by zero")
    except IndexError:
        print("Specific handler: Index out of range")
    except Exception as e:
        print(f"General handler caught: {type(e).__name__}")
        print(f"Error message: {e}")

# Custom Exception Classes
class BankingError(Exception):
    """Base exception for banking operations."""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds."""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance ${balance}, attempted ${amount}")

class InvalidAccountError(BankingError):
    """Raised when account number is invalid."""
    
    def __init__(self, account_number):
        self.account_number = account_number
        super().__init__(f"Invalid account number: {account_number}")

class AccountLockedError(BankingError):
    """Raised when account is locked."""
    
    def __init__(self, account_number, reason="Security reasons"):
        self.account_number = account_number
        self.reason = reason
        super().__init__(f"Account {account_number} is locked: {reason}")

class BankAccount:
    """Simple bank account class to demonstrate custom exceptions."""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.is_locked = False
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if self.is_locked:
            raise AccountLockedError(self.account_number)
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        """Deposit money to account."""
        if self.is_locked:
            raise AccountLockedError(self.account_number)
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return self.balance
    
    def lock_account(self, reason="Security reasons"):
        """Lock the account."""
        self.is_locked = True

def test_custom_exceptions():
    """Test custom exception handling."""
    
    # Create a bank account
    account = BankAccount("12345", 100)
    
    try:
        print(f"Initial balance: ${account.balance}")
        
        # Try to withdraw more than balance
        account.withdraw(150)
        
    except InsufficientFundsError as e:
        print(f"Banking error: {e}")
        print(f"Current balance: ${e.balance}")
        print(f"Attempted amount: ${e.amount}")
    
    try:
        # Lock account and try to deposit
        account.lock_account("Suspicious activity")
        account.deposit(50)
        
    except AccountLockedError as e:
        print(f"Account error: {e}")
        print(f"Account: {e.account_number}")
        print(f"Reason: {e.reason}")
    
    except BankingError as e:
        print(f"General banking error: {e}")

def file_operations_with_finally():
    """Demonstrate finally block with file operations."""
    
    file_handle = None
    try:
        logger.info("Attempting to open file")
        file_handle = open("test_file.txt", "w")
        file_handle.write("Hello, World!")
        
        # Simulate an error
        result = 10 / 0
        
    except ZeroDivisionError as e:
        logger.error(f"Math error occurred: {e}")
        print("Error: Division by zero")
        
    except IOError as e:
        logger.error(f"File operation failed: {e}")
        print("Error: File operation failed")
        
    finally:
        # This always executes, even if an exception occurs
        if file_handle:
            file_handle.close()
            logger.info("File closed successfully")
            print("File has been closed")
        print("Cleanup completed")

def database_connection_simulation():
    """Simulate database connection with proper cleanup."""
    
    connection = None
    transaction_started = False
    
    try:
        logger.info("Establishing database connection")
        connection = "DB_CONNECTION"  # Simulate connection
        print("Database connected")
        
        logger.info("Starting transaction")
        transaction_started = True
        print("Transaction started")
        
        # Simulate database operations
        if True:  # Simulate error condition
            raise RuntimeError("Database operation failed")
        
        logger.info("Committing transaction")
        print("Transaction committed")
        
    except RuntimeError as e:
        logger.error(f"Database error: {e}")
        if transaction_started:
            logger.info("Rolling back transaction")
            print("Transaction rolled back")
        
    finally:
        if connection:
            logger.info("Closing database connection")
            print("Database connection closed")

def comprehensive_logging_example():
    """Demonstrate comprehensive error logging."""
    
    try:
        logger.info("Starting complex operation")
        
        # Simulate various operations
        data = [1, 2, 3, 4, 5]
        index = 10
        
        logger.debug(f"Accessing index {index} in list of length {len(data)}")
        value = data[index]
        
    except IndexError as e:
        logger.error(f"Index error: {e}", exc_info=True)
        logger.warning("Falling back to default value")
        value = 0
        
    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        raise  # Re-raise unexpected exceptions
        
    else:
        logger.info(f"Operation completed successfully, value: {value}")
        
    finally:
        logger.info("Operation cleanup completed")

def advanced_error_context():
    """Demonstrate error handling with context information."""
    
    operation_id = f"OP_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    try:
        logger.info(f"Starting operation {operation_id}")
        
        # Simulate operation that might fail
        numbers = [1, 2, 3]
        result = numbers[5]  # This will fail
        
    except IndexError as e:
        logger.error(
            f"Operation {operation_id} failed: {e}",
            extra={
                'operation_id': operation_id,
                'list_length': len(numbers),
                'attempted_index': 5
            }
        )
        
    except Exception as e:
        logger.critical(
            f"Unexpected error in operation {operation_id}: {e}",
            extra={'operation_id': operation_id},
            exc_info=True
        )

# Advanced Exception Handling Patterns

class DataProcessingError(Exception):
    """Custom exception for data processing errors."""
    pass

def exception_chaining_example():
    """Demonstrate exception chaining with 'raise from'."""
    
    try:
        # Simulate a low-level error
        data = {"key": "value"}
        result = data["missing_key"]
        
    except KeyError as e:
        # Chain the exception to provide more context
        raise DataProcessingError("Failed to process user data") from e

@contextmanager
def error_handling_context(operation_name):
    """Context manager for consistent error handling."""
    
    start_time = datetime.now()
    logger.info(f"Starting {operation_name}")
    
    try:
        yield
    except Exception as e:
        duration = datetime.now() - start_time
        logger.error(
            f"{operation_name} failed after {duration.total_seconds():.2f}s: {e}",
            exc_info=True
        )
        raise
    else:
        duration = datetime.now() - start_time
        logger.info(f"{operation_name} completed successfully in {duration.total_seconds():.2f}s")

def retry_with_exponential_backoff(func, max_retries=3, base_delay=1):
    """Retry function with exponential backoff."""
    
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                logger.error(f"Final attempt failed: {e}")
                raise
            
            delay = base_delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
            # In real code, you would use time.sleep(delay)

def safe_divide(a, b):
    """Safe division with comprehensive error handling."""
    
    try:
        # Input validation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
        
    except (TypeError, ZeroDivisionError) as e:
        logger.error(f"Division error: {e}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error in division: {e}", exc_info=True)
        raise

def comprehensive_error_handler(func):
    """Decorator for comprehensive error handling."""
    
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(
                f"Error in {func.__name__}: {e}",
                extra={
                    'function': func.__name__,
                    'args': str(args),
                    'kwargs': str(kwargs)
                },
                exc_info=True
            )
            raise
    return wrapper

@comprehensive_error_handler
def risky_operation(value):
    """Function that might fail."""
    if value < 0:
        raise ValueError("Value must be positive")
    return value * 2

def test_advanced_patterns():
    """Test advanced exception handling patterns."""
    
    print("Testing exception chaining...")
    try:
        exception_chaining_example()
    except DataProcessingError as e:
        print(f"Caught chained exception: {e}")
        print(f"Original cause: {e.__cause__}")
    
    print("\nTesting context manager...")
    try:
        with error_handling_context("data processing"):
            # Simulate work that might fail
            result = 10 / 0
    except ZeroDivisionError:
        print("Error handled by context manager")
    
    print("\nTesting retry mechanism...")
    def failing_function():
        raise ConnectionError("Network unavailable")
    
    try:
        retry_with_exponential_backoff(failing_function)
    except ConnectionError:
        print("All retry attempts failed")
    
    print("\nTesting safe division...")
    try:
        result = safe_divide(10, 2)
        print(f"Safe division result: {result}")
        
        safe_divide(10, 0)
    except ZeroDivisionError:
        print("Division by zero handled safely")
    
    print("\nTesting decorator...")
    try:
        result = risky_operation(5)
        print(f"Risky operation result: {result}")
        
        risky_operation(-1)
    except ValueError:
        print("Risky operation error handled")

# Test all advanced patterns
print("\n=== Step 5: Advanced Exception Handling ===")
print("Testing advanced exception handling patterns...")
test_advanced_patterns()

# What we accomplished in this step:
# - Learned exception chaining with 'raise from'
# - Created context managers for consistent error handling
# - Implemented retry mechanisms with exponential backoff
# - Built comprehensive error handling decorators
# - Demonstrated production-ready error handling patterns


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Basic try-except blocks and common exceptions
# - Multiple exception handling strategies
# - Custom exception classes and hierarchies
# - Finally blocks for cleanup operations
# - Proper logging with different levels and context
# - Advanced patterns: chaining, context managers, retries
# - Production-ready error handling best practices
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each pattern is useful
# 4. Experiment with your own exception scenarios
#
# Remember: Good error handling makes your code robust and maintainable!
# ===============================================================================