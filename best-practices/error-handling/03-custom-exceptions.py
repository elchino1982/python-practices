"""Question: Create custom exception classes for better error handling and debugging.

Create a comprehensive custom exception hierarchy for a banking application
that handles various types of errors with specific information.

Requirements:
1. Create a base custom exception class
2. Create specific exception classes for different error types
3. Add custom attributes and methods to exceptions
4. Implement exception chaining and context
5. Demonstrate proper exception handling patterns

Example usage:
    try:
        account.withdraw(1000)
    except InsufficientFundsError as e:
        print(f"Error: {e}")
        print(f"Available balance: {e.available_balance}")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what exception classes you need
# - Start with a simple base exception
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
# - What is the base exception class you need?
# - What specific banking errors can occur?
# - What additional information should each exception carry?
# - How can you chain exceptions for better debugging?
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


# Step 1: Create the base custom exception class
# ===============================================================================

# Explanation:
# Custom exceptions should inherit from built-in exception classes.
# A base exception class provides common functionality for all custom exceptions.

class BankingError(Exception):
    """Base exception class for all banking-related errors."""
    
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = self._get_timestamp()
    
    def _get_timestamp(self):
        """Get current timestamp for error logging."""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def __str__(self):
        """String representation of the error."""
        if self.error_code:
            return f"[{self.error_code}] {self.message} (at {self.timestamp})"
        return f"{self.message} (at {self.timestamp})"

# What we accomplished in this step:
# - Created base BankingError class with common attributes
# - Added timestamp for error tracking
# - Implemented custom string representation


# Step 2: Create specific exception classes with custom attributes
# ===============================================================================

# Explanation:
# Specific exceptions inherit from our base class and add domain-specific
# attributes and behavior for different types of banking errors.

class BankingError(Exception):
    """Base exception class for all banking-related errors."""
    
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = self._get_timestamp()
    
    def _get_timestamp(self):
        """Get current timestamp for error logging."""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def __str__(self):
        """String representation of the error."""
        if self.error_code:
            return f"[{self.error_code}] {self.message} (at {self.timestamp})"
        return f"{self.message} (at {self.timestamp})"

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds for a transaction."""
    
    def __init__(self, message: str, requested_amount: float, available_balance: float, account_id: str = None):
        super().__init__(message, "INSUFFICIENT_FUNDS")
        self.requested_amount = requested_amount
        self.available_balance = available_balance
        self.account_id = account_id
        self.shortfall = requested_amount - available_balance
    
    def __str__(self):
        base_msg = super().__str__()
        return f"{base_msg} - Requested: ${self.requested_amount:.2f}, Available: ${self.available_balance:.2f}"

class AccountNotFoundError(BankingError):
    """Raised when an account cannot be found."""
    
    def __init__(self, account_id: str, search_criteria: str = None):
        message = f"Account not found: {account_id}"
        super().__init__(message, "ACCOUNT_NOT_FOUND")
        self.account_id = account_id
        self.search_criteria = search_criteria

class InvalidTransactionError(BankingError):
    """Raised when a transaction is invalid."""
    
    def __init__(self, message: str, transaction_type: str, amount: float = None, reason: str = None):
        super().__init__(message, "INVALID_TRANSACTION")
        self.transaction_type = transaction_type
        self.amount = amount
        self.reason = reason

class AccountFrozenError(BankingError):
    """Raised when trying to perform operations on a frozen account."""
    
    def __init__(self, account_id: str, freeze_reason: str = None):
        message = f"Account {account_id} is frozen"
        super().__init__(message, "ACCOUNT_FROZEN")
        self.account_id = account_id
        self.freeze_reason = freeze_reason

# What we accomplished in this step:
# - Created specific exception classes for different banking scenarios
# - Added domain-specific attributes (amounts, account IDs, etc.)
# - Implemented custom string representations with relevant details


# Step 3: Add exception chaining and context handling
# ===============================================================================

# Explanation:
# Exception chaining helps preserve the original error context while raising
# more specific exceptions. This is crucial for debugging complex systems.

class BankingError(Exception):
    """Base exception class for all banking-related errors."""
    
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = self._get_timestamp()
    
    def _get_timestamp(self):
        """Get current timestamp for error logging."""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def __str__(self):
        """String representation of the error."""
        if self.error_code:
            return f"[{self.error_code}] {self.message} (at {self.timestamp})"
        return f"{self.message} (at {self.timestamp})"

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds for a transaction."""
    
    def __init__(self, message: str, requested_amount: float, available_balance: float, account_id: str = None):
        super().__init__(message, "INSUFFICIENT_FUNDS")
        self.requested_amount = requested_amount
        self.available_balance = available_balance
        self.account_id = account_id
        self.shortfall = requested_amount - available_balance
    
    def __str__(self):
        base_msg = super().__str__()
        return f"{base_msg} - Requested: ${self.requested_amount:.2f}, Available: ${self.available_balance:.2f}"

class AccountNotFoundError(BankingError):
    """Raised when an account cannot be found."""
    
    def __init__(self, account_id: str, search_criteria: str = None):
        message = f"Account not found: {account_id}"
        super().__init__(message, "ACCOUNT_NOT_FOUND")
        self.account_id = account_id
        self.search_criteria = search_criteria

class InvalidTransactionError(BankingError):
    """Raised when a transaction is invalid."""
    
    def __init__(self, message: str, transaction_type: str, amount: float = None, reason: str = None):
        super().__init__(message, "INVALID_TRANSACTION")
        self.transaction_type = transaction_type
        self.amount = amount
        self.reason = reason

class AccountFrozenError(BankingError):
    """Raised when trying to perform operations on a frozen account."""
    
    def __init__(self, account_id: str, freeze_reason: str = None):
        message = f"Account {account_id} is frozen"
        super().__init__(message, "ACCOUNT_FROZEN")
        self.account_id = account_id
        self.freeze_reason = freeze_reason

class DatabaseConnectionError(BankingError):
    """Raised when database operations fail."""
    
    def __init__(self, operation: str, original_error: Exception = None):
        message = f"Database operation failed: {operation}"
        super().__init__(message, "DATABASE_ERROR")
        self.operation = operation
        self.original_error = original_error

class ValidationError(BankingError):
    """Raised when input validation fails."""
    
    def __init__(self, field: str, value: any, validation_rule: str):
        message = f"Validation failed for {field}: {validation_rule}"
        super().__init__(message, "VALIDATION_ERROR")
        self.field = field
        self.value = value
        self.validation_rule = validation_rule

# Exception chaining utility functions
def chain_exception(new_exception: BankingError, original_exception: Exception) -> BankingError:
    """Chain a new exception with the original exception for better debugging."""
    new_exception.__cause__ = original_exception
    return new_exception

def wrap_database_error(operation: str, original_error: Exception) -> DatabaseConnectionError:
    """Wrap database errors with banking-specific context."""
    db_error = DatabaseConnectionError(operation, original_error)
    db_error.__cause__ = original_error
    return db_error

# What we accomplished in this step:
# - Added more specific exception types
# - Implemented exception chaining with __cause__
# - Created utility functions for exception wrapping
# - Added context preservation for debugging


# Step 4: Create a banking system to demonstrate exception usage
# ===============================================================================

# Explanation:
# Now we'll create a simple banking system that uses our custom exceptions
# to show how they work in practice with proper error handling patterns.

class BankingError(Exception):
    """Base exception class for all banking-related errors."""
    
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = self._get_timestamp()
    
    def _get_timestamp(self):
        """Get current timestamp for error logging."""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def __str__(self):
        """String representation of the error."""
        if self.error_code:
            return f"[{self.error_code}] {self.message} (at {self.timestamp})"
        return f"{self.message} (at {self.timestamp})"

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds for a transaction."""
    
    def __init__(self, message: str, requested_amount: float, available_balance: float, account_id: str = None):
        super().__init__(message, "INSUFFICIENT_FUNDS")
        self.requested_amount = requested_amount
        self.available_balance = available_balance
        self.account_id = account_id
        self.shortfall = requested_amount - available_balance
    
    def __str__(self):
        base_msg = super().__str__()
        return f"{base_msg} - Requested: ${self.requested_amount:.2f}, Available: ${self.available_balance:.2f}"

class AccountNotFoundError(BankingError):
    """Raised when an account cannot be found."""
    
    def __init__(self, account_id: str, search_criteria: str = None):
        message = f"Account not found: {account_id}"
        super().__init__(message, "ACCOUNT_NOT_FOUND")
        self.account_id = account_id
        self.search_criteria = search_criteria

class InvalidTransactionError(BankingError):
    """Raised when a transaction is invalid."""
    
    def __init__(self, message: str, transaction_type: str, amount: float = None, reason: str = None):
        super().__init__(message, "INVALID_TRANSACTION")
        self.transaction_type = transaction_type
        self.amount = amount
        self.reason = reason

class AccountFrozenError(BankingError):
    """Raised when trying to perform operations on a frozen account."""
    
    def __init__(self, account_id: str, freeze_reason: str = None):
        message = f"Account {account_id} is frozen"
        super().__init__(message, "ACCOUNT_FROZEN")
        self.account_id = account_id
        self.freeze_reason = freeze_reason

class DatabaseConnectionError(BankingError):
    """Raised when database operations fail."""
    
    def __init__(self, operation: str, original_error: Exception = None):
        message = f"Database operation failed: {operation}"
        super().__init__(message, "DATABASE_ERROR")
        self.operation = operation
        self.original_error = original_error

class ValidationError(BankingError):
    """Raised when input validation fails."""
    
    def __init__(self, field: str, value: any, validation_rule: str):
        message = f"Validation failed for {field}: {validation_rule}"
        super().__init__(message, "VALIDATION_ERROR")
        self.field = field
        self.value = value
        self.validation_rule = validation_rule

# Exception chaining utility functions
def chain_exception(new_exception: BankingError, original_exception: Exception) -> BankingError:
    """Chain a new exception with the original exception for better debugging."""
    new_exception.__cause__ = original_exception
    return new_exception

def wrap_database_error(operation: str, original_error: Exception) -> DatabaseConnectionError:
    """Wrap database errors with banking-specific context."""
    db_error = DatabaseConnectionError(operation, original_error)
    db_error.__cause__ = original_error
    return db_error

# Banking system implementation
class BankAccount:
    """Simple bank account class to demonstrate exception usage."""
    
    def __init__(self, account_id: str, initial_balance: float = 0.0):
        self.account_id = self._validate_account_id(account_id)
        self.balance = self._validate_amount(initial_balance, "initial_balance")
        self.is_frozen = False
        self.freeze_reason = None
    
    def _validate_account_id(self, account_id: str) -> str:
        """Validate account ID format."""
        if not account_id or not isinstance(account_id, str):
            raise ValidationError("account_id", account_id, "must be a non-empty string")
        if len(account_id) < 5:
            raise ValidationError("account_id", account_id, "must be at least 5 characters long")
        return account_id
    
    def _validate_amount(self, amount: float, field_name: str) -> float:
        """Validate monetary amounts."""
        if not isinstance(amount, (int, float)):
            raise ValidationError(field_name, amount, "must be a number")
        if amount < 0:
            raise ValidationError(field_name, amount, "must be non-negative")
        return float(amount)
    
    def _check_account_status(self):
        """Check if account is available for transactions."""
        if self.is_frozen:
            raise AccountFrozenError(self.account_id, self.freeze_reason)
    
    def deposit(self, amount: float) -> float:
        """Deposit money into the account."""
        try:
            self._check_account_status()
            amount = self._validate_amount(amount, "deposit_amount")
            
            if amount == 0:
                raise InvalidTransactionError(
                    "Cannot deposit zero amount", 
                    "deposit", 
                    amount, 
                    "Amount must be greater than zero"
                )
            
            self.balance += amount
            return self.balance
            
        except Exception as e:
            if isinstance(e, BankingError):
                raise
            # Wrap unexpected errors
            raise chain_exception(
                InvalidTransactionError(f"Deposit failed: {str(e)}", "deposit", amount),
                e
            )
    
    def withdraw(self, amount: float) -> float:
        """Withdraw money from the account."""
        try:
            self._check_account_status()
            amount = self._validate_amount(amount, "withdrawal_amount")
            
            if amount == 0:
                raise InvalidTransactionError(
                    "Cannot withdraw zero amount", 
                    "withdrawal", 
                    amount, 
                    "Amount must be greater than zero"
                )
            
            if amount > self.balance:
                raise InsufficientFundsError(
                    f"Insufficient funds for withdrawal of ${amount:.2f}",
                    amount,
                    self.balance,
                    self.account_id
                )
            
            self.balance -= amount
            return self.balance
            
        except Exception as e:
            if isinstance(e, BankingError):
                raise
            # Wrap unexpected errors
            raise chain_exception(
                InvalidTransactionError(f"Withdrawal failed: {str(e)}", "withdrawal", amount),
                e
            )
    
    def freeze_account(self, reason: str = "Administrative hold"):
        """Freeze the account."""
        self.is_frozen = True
        self.freeze_reason = reason
    
    def unfreeze_account(self):
        """Unfreeze the account."""
        self.is_frozen = False
        self.freeze_reason = None

class Bank:
    """Simple bank class to manage multiple accounts."""
    
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id: str, initial_balance: float = 0.0) -> BankAccount:
        """Create a new bank account."""
        if account_id in self.accounts:
            raise InvalidTransactionError(
                f"Account {account_id} already exists",
                "account_creation",
                reason="Duplicate account ID"
            )
        
        account = BankAccount(account_id, initial_balance)
        self.accounts[account_id] = account
        return account
    
    def get_account(self, account_id: str) -> BankAccount:
        """Get an existing account."""
        if account_id not in self.accounts:
            raise AccountNotFoundError(account_id)
        return self.accounts[account_id]
    
    def transfer(self, from_account_id: str, to_account_id: str, amount: float):
        """Transfer money between accounts."""
        try:
            from_account = self.get_account(from_account_id)
            to_account = self.get_account(to_account_id)
            
            # Withdraw from source account
            from_account.withdraw(amount)
            
            try:
                # Deposit to destination account
                to_account.deposit(amount)
            except Exception as deposit_error:
                # Rollback the withdrawal if deposit fails
                from_account.deposit(amount)
                raise chain_exception(
                    InvalidTransactionError(
                        f"Transfer failed during deposit phase",
                        "transfer",
                        amount,
                        "Deposit to destination account failed"
                    ),
                    deposit_error
                )
                
        except Exception as e:
            if isinstance(e, BankingError):
                raise
            # Wrap unexpected errors
            raise chain_exception(
                InvalidTransactionError(f"Transfer failed: {str(e)}", "transfer", amount),
                e
            )

# What we accomplished in this step:
# - Created BankAccount class with proper validation
# - Implemented Bank class for account management
# - Added comprehensive error handling with custom exceptions
# - Demonstrated exception chaining and rollback scenarios


# Step 5: Comprehensive demonstration and testing examples
# ===============================================================================

# Explanation:
# This final step shows how to use all our custom exceptions in practice
# with proper error handling patterns and comprehensive testing scenarios.

from datetime import datetime

class BankingError(Exception):
    """Base exception class for all banking-related errors."""
    
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = self._get_timestamp()
    
    def _get_timestamp(self):
        """Get current timestamp for error logging."""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def __str__(self):
        """String representation of the error."""
        if self.error_code:
            return f"[{self.error_code}] {self.message} (at {self.timestamp})"
        return f"{self.message} (at {self.timestamp})"

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds for a transaction."""
    
    def __init__(self, message: str, requested_amount: float, available_balance: float, account_id: str = None):
        super().__init__(message, "INSUFFICIENT_FUNDS")
        self.requested_amount = requested_amount
        self.available_balance = available_balance
        self.account_id = account_id
        self.shortfall = requested_amount - available_balance
    
    def __str__(self):
        base_msg = super().__str__()
        return f"{base_msg} - Requested: ${self.requested_amount:.2f}, Available: ${self.available_balance:.2f}"

class AccountNotFoundError(BankingError):
    """Raised when an account cannot be found."""
    
    def __init__(self, account_id: str, search_criteria: str = None):
        message = f"Account not found: {account_id}"
        super().__init__(message, "ACCOUNT_NOT_FOUND")
        self.account_id = account_id
        self.search_criteria = search_criteria

class InvalidTransactionError(BankingError):
    """Raised when a transaction is invalid."""
    
    def __init__(self, message: str, transaction_type: str, amount: float = None, reason: str = None):
        super().__init__(message, "INVALID_TRANSACTION")
        self.transaction_type = transaction_type
        self.amount = amount
        self.reason = reason

class AccountFrozenError(BankingError):
    """Raised when trying to perform operations on a frozen account."""
    
    def __init__(self, account_id: str, freeze_reason: str = None):
        message = f"Account {account_id} is frozen"
        super().__init__(message, "ACCOUNT_FROZEN")
        self.account_id = account_id
        self.freeze_reason = freeze_reason

class DatabaseConnectionError(BankingError):
    """Raised when database operations fail."""
    
    def __init__(self, operation: str, original_error: Exception = None):
        message = f"Database operation failed: {operation}"
        super().__init__(message, "DATABASE_ERROR")
        self.operation = operation
        self.original_error = original_error

class ValidationError(BankingError):
    """Raised when input validation fails."""
    
    def __init__(self, field: str, value: any, validation_rule: str):
        message = f"Validation failed for {field}: {validation_rule}"
        super().__init__(message, "VALIDATION_ERROR")
        self.field = field
        self.value = value
        self.validation_rule = validation_rule

# Exception chaining utility functions
def chain_exception(new_exception: BankingError, original_exception: Exception) -> BankingError:
    """Chain a new exception with the original exception for better debugging."""
    new_exception.__cause__ = original_exception
    return new_exception

def wrap_database_error(operation: str, original_error: Exception) -> DatabaseConnectionError:
    """Wrap database errors with banking-specific context."""
    db_error = DatabaseConnectionError(operation, original_error)
    db_error.__cause__ = original_error
    return db_error

# Banking system implementation
class BankAccount:
    """Simple bank account class to demonstrate exception usage."""
    
    def __init__(self, account_id: str, initial_balance: float = 0.0):
        self.account_id = self._validate_account_id(account_id)
        self.balance = self._validate_amount(initial_balance, "initial_balance")
        self.is_frozen = False
        self.freeze_reason = None
    
    def _validate_account_id(self, account_id: str) -> str:
        """Validate account ID format."""
        if not account_id or not isinstance(account_id, str):
            raise ValidationError("account_id", account_id, "must be a non-empty string")
        if len(account_id) < 5:
            raise ValidationError("account_id", account_id, "must be at least 5 characters long")
        return account_id
    
    def _validate_amount(self, amount: float, field_name: str) -> float:
        """Validate monetary amounts."""
        if not isinstance(amount, (int, float)):
            raise ValidationError(field_name, amount, "must be a number")
        if amount < 0:
            raise ValidationError(field_name, amount, "must be non-negative")
        return float(amount)
    
    def _check_account_status(self):
        """Check if account is available for transactions."""
        if self.is_frozen:
            raise AccountFrozenError(self.account_id, self.freeze_reason)
    
    def deposit(self, amount: float) -> float:
        """Deposit money into the account."""
        try:
            self._check_account_status()
            amount = self._validate_amount(amount, "deposit_amount")
            
            if amount == 0:
                raise InvalidTransactionError(
                    "Cannot deposit zero amount", 
                    "deposit", 
                    amount, 
                    "Amount must be greater than zero"
                )
            
            self.balance += amount
            return self.balance
            
        except Exception as e:
            if isinstance(e, BankingError):
                raise
            # Wrap unexpected errors
            raise chain_exception(
                InvalidTransactionError(f"Deposit failed: {str(e)}", "deposit", amount),
                e
            )
    
    def withdraw(self, amount: float) -> float:
        """Withdraw money from the account."""
        try:
            self._check_account_status()
            amount = self._validate_amount(amount, "withdrawal_amount")
            
            if amount == 0:
                raise InvalidTransactionError(
                    "Cannot withdraw zero amount", 
                    "withdrawal", 
                    amount, 
                    "Amount must be greater than zero"
                )
            
            if amount > self.balance:
                raise InsufficientFundsError(
                    f"Insufficient funds for withdrawal of ${amount:.2f}",
                    amount,
                    self.balance,
                    self.account_id
                )
            
            self.balance -= amount
            return self.balance
            
        except Exception as e:
            if isinstance(e, BankingError):
                raise
            # Wrap unexpected errors
            raise chain_exception(
                InvalidTransactionError(f"Withdrawal failed: {str(e)}", "withdrawal", amount),
                e
            )
    
    def freeze_account(self, reason: str = "Administrative hold"):
        """Freeze the account."""
        self.is_frozen = True
        self.freeze_reason = reason
    
    def unfreeze_account(self):
        """Unfreeze the account."""
        self.is_frozen = False
        self.freeze_reason = None

class Bank:
    """Simple bank class to manage multiple accounts."""
    
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id: str, initial_balance: float = 0.0) -> BankAccount:
        """Create a new bank account."""
        if account_id in self.accounts:
            raise InvalidTransactionError(
                f"Account {account_id} already exists",
                "account_creation",
                reason="Duplicate account ID"
            )
        
        account = BankAccount(account_id, initial_balance)
        self.accounts[account_id] = account
        return account
    
    def get_account(self, account_id: str) -> BankAccount:
        """Get an existing account."""
        if account_id not in self.accounts:
            raise AccountNotFoundError(account_id)
        return self.accounts[account_id]
    
    def transfer(self, from_account_id: str, to_account_id: str, amount: float):
        """Transfer money between accounts."""
        try:
            from_account = self.get_account(from_account_id)
            to_account = self.get_account(to_account_id)
            
            # Withdraw from source account
            from_account.withdraw(amount)
            
            try:
                # Deposit to destination account
                to_account.deposit(amount)
            except Exception as deposit_error:
                # Rollback the withdrawal if deposit fails
                from_account.deposit(amount)
                raise chain_exception(
                    InvalidTransactionError(
                        f"Transfer failed during deposit phase",
                        "transfer",
                        amount,
                        "Deposit to destination account failed"
                    ),
                    deposit_error
                )
                
        except Exception as e:
            if isinstance(e, BankingError):
                raise
            # Wrap unexpected errors
            raise chain_exception(
                InvalidTransactionError(f"Transfer failed: {str(e)}", "transfer", amount),
                e
            )

# Error handling utilities
class ErrorLogger:
    """Utility class for logging banking errors."""
    
    @staticmethod
    def log_error(error: BankingError, context: str = ""):
        """Log banking errors with full context."""
        print(f"ERROR LOG - {context}")
        print(f"Error Type: {type(error).__name__}")
        print(f"Error Code: {error.error_code}")
        print(f"Message: {error.message}")
        print(f"Timestamp: {error.timestamp}")
        
        # Log specific attributes based on error type
        if isinstance(error, InsufficientFundsError):
            print(f"Account ID: {error.account_id}")
            print(f"Requested Amount: ${error.requested_amount:.2f}")
            print(f"Available Balance: ${error.available_balance:.2f}")
            print(f"Shortfall: ${error.shortfall:.2f}")
        
        elif isinstance(error, AccountNotFoundError):
            print(f"Account ID: {error.account_id}")
            if error.search_criteria:
                print(f"Search Criteria: {error.search_criteria}")
        
        elif isinstance(error, ValidationError):
            print(f"Field: {error.field}")
            print(f"Value: {error.value}")
            print(f"Validation Rule: {error.validation_rule}")
        
        # Log chained exceptions
        if error.__cause__:
            print(f"Caused by: {type(error.__cause__).__name__}: {error.__cause__}")
        
        print("-" * 50)

def safe_banking_operation(operation_func, *args, **kwargs):
    """Safely execute banking operations with comprehensive error handling."""
    try:
        return operation_func(*args, **kwargs)
    
    except InsufficientFundsError as e:
        ErrorLogger.log_error(e, "Insufficient Funds")
        print(f"Transaction declined: {e}")
        return None
    
    except AccountNotFoundError as e:
        ErrorLogger.log_error(e, "Account Lookup")
        print(f"Account error: {e}")
        return None
    
    except AccountFrozenError as e:
        ErrorLogger.log_error(e, "Account Status")
        print(f"Account frozen: {e}")
        print(f"Reason: {e.freeze_reason}")
        return None
    
    except ValidationError as e:
        ErrorLogger.log_error(e, "Input Validation")
        print(f"Validation error: {e}")
        return None
    
    except InvalidTransactionError as e:
        ErrorLogger.log_error(e, "Transaction Processing")
        print(f"Transaction error: {e}")
        return None
    
    except BankingError as e:
        ErrorLogger.log_error(e, "General Banking")
        print(f"Banking system error: {e}")
        return None
    
    except Exception as e:
        # Handle unexpected errors
        wrapped_error = chain_exception(
            BankingError(f"Unexpected error: {str(e)}", "SYSTEM_ERROR"),
            e
        )
        ErrorLogger.log_error(wrapped_error, "System Error")
        print(f"System error: {wrapped_error}")
        return None

# Demonstration and testing
def demonstrate_custom_exceptions():
    """Comprehensive demonstration of custom exception usage."""
    print("=== Custom Exception Demonstration ===\n")
    
    # Create a bank and accounts
    bank = Bank()
    
    print("1. Testing successful operations:")
    try:
        account1 = bank.create_account("ACC12345", 1000.0)
        account2 = bank.create_account("ACC67890", 500.0)
        print(f"Created account {account1.account_id} with balance ${account1.balance:.2f}")
        print(f"Created account {account2.account_id} with balance ${account2.balance:.2f}")
    except BankingError as e:
        ErrorLogger.log_error(e, "Account Creation")
    
    print("\n2. Testing validation errors:")
    # Test invalid account ID
    safe_banking_operation(bank.create_account, "123", 100.0)  # Too short
    
    # Test negative balance
    safe_banking_operation(BankAccount, "ACC99999", -100.0)
    
    print("\n3. Testing insufficient funds:")
    account = bank.get_account("ACC12345")
    safe_banking_operation(account.withdraw, 2000.0)  # More than balance
    
    print("\n4. Testing account not found:")
    safe_banking_operation(bank.get_account, "NONEXISTENT")
    
    print("\n5. Testing frozen account:")
    account.freeze_account("Suspicious activity detected")
    safe_banking_operation(account.withdraw, 100.0)
    
    print("\n6. Testing transfer with rollback:")
    account.unfreeze_account()
    account2 = bank.get_account("ACC67890")
    account2.freeze_account("Account under review")
    safe_banking_operation(bank.transfer, "ACC12345", "ACC67890", 200.0)
    
    print("\n7. Testing exception chaining:")
    try:
        # Simulate a database error during withdrawal
        original_error = ConnectionError("Database connection lost")
        raise wrap_database_error("account_withdrawal", original_error)
    except DatabaseConnectionError as e:
        ErrorLogger.log_error(e, "Database Operation")
    
    print("\n8. Testing successful operations after fixes:")
    account2.unfreeze_account()
    result = safe_banking_operation(bank.transfer, "ACC12345", "ACC67890", 200.0)
    if result is not None:
        print(f"Transfer successful!")
        print(f"Account 1 balance: ${bank.get_account('ACC12345').balance:.2f}")
        print(f"Account 2 balance: ${bank.get_account('ACC67890').balance:.2f}")

# Run the demonstration
if __name__ == "__main__":
    demonstrate_custom_exceptions()

# What we accomplished in this step:
# - Created comprehensive error logging system
# - Implemented safe operation wrapper with specific error handling
# - Added complete demonstration with all exception types
# - Showed proper exception chaining and context preservation
# - Demonstrated rollback scenarios and error recovery patterns

# ===============================================================================
#                              FINAL SUMMARY
# ===============================================================================
#
# This comprehensive example demonstrates:
#
# 1. **Custom Exception Hierarchy**: Base BankingError with specific subclasses
# 2. **Rich Error Information**: Custom attributes for debugging and user feedback
# 3. **Exception Chaining**: Preserving original error context with __cause__
# 4. **Proper Error Handling**: Specific catch blocks for different error types
# 5. **Error Logging**: Comprehensive logging with context and details
# 6. **Rollback Scenarios**: Transaction safety with proper error recovery
# 7. **Validation Patterns**: Input validation with descriptive error messages
# 8. **Real-world Usage**: Practical banking system demonstrating all concepts
#
# Key Benefits:
# - Better debugging with rich error context
# - Improved user experience with specific error messages
# - Maintainable code with clear error handling patterns
# - Robust systems with proper error recovery
# - Professional error logging and monitoring capabilities
#
# ===============================================================================
