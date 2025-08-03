"""Question: Implement defensive programming techniques to create robust and error-resistant code.

Create a comprehensive example that demonstrates various defensive programming practices
including input validation, error handling, and fail-safe mechanisms.

Requirements:
1. Create a BankAccount class with defensive validation
2. Implement input sanitization and validation functions
3. Create error handling with graceful degradation
4. Implement logging and monitoring mechanisms
5. Demonstrate contract programming (preconditions/postconditions)

Example usage:
    account = BankAccount("12345", "John Doe", 1000.0)
    account.withdraw(500.0)  # Should work
    account.withdraw(-100.0)  # Should fail gracefully
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what could go wrong in your code
# - Start with basic validation
# - Test your code with invalid inputs
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
# - What inputs could be invalid or malicious?
# - How can you validate data before processing?
# - What should happen when errors occur?
# - How can you log problems for debugging?
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


# Step 1: Import modules and create basic validation functions
# ===============================================================================

# Explanation:
# Defensive programming starts with input validation. We need to check
# that inputs are valid before processing them.

import logging
import re
from typing import Union, Optional, Any
from decimal import Decimal, InvalidOperation
from datetime import datetime

def validate_account_number(account_number: str) -> bool:
    """Validate account number format."""
    if not isinstance(account_number, str):
        return False
    
    # Account number should be 5-12 digits
    pattern = r'^\d{5,12}$'
    return bool(re.match(pattern, account_number))

def validate_name(name: str) -> bool:
    """Validate person name."""
    if not isinstance(name, str):
        return False
    
    # Name should be 2-50 characters, letters, spaces, hyphens, apostrophes
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        return False
    
    pattern = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(pattern, name))

def validate_amount(amount: Union[int, float, Decimal]) -> bool:
    """Validate monetary amount."""
    try:
        decimal_amount = Decimal(str(amount))
        # Amount should be non-negative and have at most 2 decimal places
        return decimal_amount >= 0 and decimal_amount.as_tuple().exponent >= -2
    except (InvalidOperation, ValueError, TypeError):
        return False

# What we accomplished in this step:
# - Created basic validation functions for common inputs
# - Used regular expressions for pattern matching
# - Handled type checking and edge cases


# Step 2: Create custom exceptions and sanitization functions
# ===============================================================================

# Explanation:
# Custom exceptions help us handle specific error cases gracefully.
# Sanitization functions clean and normalize input data.

import logging
import re
from typing import Union, Optional, Any
from decimal import Decimal, InvalidOperation
from datetime import datetime

class BankAccountError(Exception):
    """Base exception for bank account operations."""
    pass

class InvalidAccountNumberError(BankAccountError):
    """Raised when account number is invalid."""
    pass

class InvalidNameError(BankAccountError):
    """Raised when name is invalid."""
    pass

class InvalidAmountError(BankAccountError):
    """Raised when amount is invalid."""
    pass

class InsufficientFundsError(BankAccountError):
    """Raised when there are insufficient funds for withdrawal."""
    pass

def validate_account_number(account_number: str) -> bool:
    """Validate account number format."""
    if not isinstance(account_number, str):
        return False
    
    # Account number should be 5-12 digits
    pattern = r'^\d{5,12}$'
    return bool(re.match(pattern, account_number))

def validate_name(name: str) -> bool:
    """Validate person name."""
    if not isinstance(name, str):
        return False
    
    # Name should be 2-50 characters, letters, spaces, hyphens, apostrophes
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        return False
    
    pattern = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(pattern, name))

def validate_amount(amount: Union[int, float, Decimal]) -> bool:
    """Validate monetary amount."""
    try:
        decimal_amount = Decimal(str(amount))
        # Amount should be non-negative and have at most 2 decimal places
        return decimal_amount >= 0 and decimal_amount.as_tuple().exponent >= -2
    except (InvalidOperation, ValueError, TypeError):
        return False

def sanitize_account_number(account_number: Any) -> str:
    """Sanitize and validate account number."""
    if account_number is None:
        raise InvalidAccountNumberError("Account number cannot be None")
    
    # Convert to string and remove whitespace
    sanitized = str(account_number).strip()
    
    if not validate_account_number(sanitized):
        raise InvalidAccountNumberError(f"Invalid account number format: {sanitized}")
    
    return sanitized

def sanitize_name(name: Any) -> str:
    """Sanitize and validate name."""
    if name is None:
        raise InvalidNameError("Name cannot be None")
    
    # Convert to string, strip whitespace, normalize spaces
    sanitized = re.sub(r'\s+', ' ', str(name).strip())
    
    if not validate_name(sanitized):
        raise InvalidNameError(f"Invalid name format: {sanitized}")
    
    return sanitized

def sanitize_amount(amount: Any) -> Decimal:
    """Sanitize and validate amount."""
    if amount is None:
        raise InvalidAmountError("Amount cannot be None")
    
    try:
        # Convert to Decimal for precise monetary calculations
        decimal_amount = Decimal(str(amount))
        
        if not validate_amount(decimal_amount):
            raise InvalidAmountError(f"Invalid amount: {amount}")
        
        # Round to 2 decimal places for currency
        return decimal_amount.quantize(Decimal('0.01'))
    
    except (InvalidOperation, ValueError, TypeError) as e:
        raise InvalidAmountError(f"Cannot convert to valid amount: {amount}") from e

# What we accomplished in this step:
# - Created custom exception hierarchy for specific error types
# - Added sanitization functions that clean and validate inputs
# - Used Decimal for precise monetary calculations
# - Implemented proper error chaining


# Step 3: Set up logging and create the defensive BankAccount class
# ===============================================================================

# Explanation:
# Logging helps us track what happens in our application, especially errors.
# The BankAccount class will use all our defensive programming techniques.

import logging
import re
from typing import Union, Optional, Any, List
from decimal import Decimal, InvalidOperation
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bank_account.log'),
        logging.StreamHandler()
    ]
)

class BankAccountError(Exception):
    """Base exception for bank account operations."""
    pass

class InvalidAccountNumberError(BankAccountError):
    """Raised when account number is invalid."""
    pass

class InvalidNameError(BankAccountError):
    """Raised when name is invalid."""
    pass

class InvalidAmountError(BankAccountError):
    """Raised when amount is invalid."""
    pass

class InsufficientFundsError(BankAccountError):
    """Raised when there are insufficient funds for withdrawal."""
    pass

def validate_account_number(account_number: str) -> bool:
    """Validate account number format."""
    if not isinstance(account_number, str):
        return False
    
    # Account number should be 5-12 digits
    pattern = r'^\d{5,12}$'
    return bool(re.match(pattern, account_number))

def validate_name(name: str) -> bool:
    """Validate person name."""
    if not isinstance(name, str):
        return False
    
    # Name should be 2-50 characters, letters, spaces, hyphens, apostrophes
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        return False
    
    pattern = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(pattern, name))

def validate_amount(amount: Union[int, float, Decimal]) -> bool:
    """Validate monetary amount."""
    try:
        decimal_amount = Decimal(str(amount))
        # Amount should be non-negative and have at most 2 decimal places
        return decimal_amount >= 0 and decimal_amount.as_tuple().exponent >= -2
    except (InvalidOperation, ValueError, TypeError):
        return False

def sanitize_account_number(account_number: Any) -> str:
    """Sanitize and validate account number."""
    if account_number is None:
        raise InvalidAccountNumberError("Account number cannot be None")
    
    # Convert to string and remove whitespace
    sanitized = str(account_number).strip()
    
    if not validate_account_number(sanitized):
        raise InvalidAccountNumberError(f"Invalid account number format: {sanitized}")
    
    return sanitized

def sanitize_name(name: Any) -> str:
    """Sanitize and validate name."""
    if name is None:
        raise InvalidNameError("Name cannot be None")
    
    # Convert to string, strip whitespace, normalize spaces
    sanitized = re.sub(r'\s+', ' ', str(name).strip())
    
    if not validate_name(sanitized):
        raise InvalidNameError(f"Invalid name format: {sanitized}")
    
    return sanitized

def sanitize_amount(amount: Any) -> Decimal:
    """Sanitize and validate amount."""
    if amount is None:
        raise InvalidAmountError("Amount cannot be None")
    
    try:
        # Convert to Decimal for precise monetary calculations
        decimal_amount = Decimal(str(amount))
        
        if not validate_amount(decimal_amount):
            raise InvalidAmountError(f"Invalid amount: {amount}")
        
        # Round to 2 decimal places for currency
        return decimal_amount.quantize(Decimal('0.01'))
    
    except (InvalidOperation, ValueError, TypeError) as e:
        raise InvalidAmountError(f"Cannot convert to valid amount: {amount}") from e

class BankAccount:
    """A defensive bank account implementation with comprehensive error handling."""
    
    def __init__(self, account_number: Any, account_holder: Any, initial_balance: Any = 0):
        """Initialize bank account with defensive validation.
        
        Args:
            account_number: Account number (will be sanitized)
            account_holder: Account holder name (will be sanitized)
            initial_balance: Initial balance (will be sanitized)
        """
        self.logger = logging.getLogger(f"{__name__}.BankAccount")
        
        try:
            # Defensive initialization with sanitization
            self._account_number = sanitize_account_number(account_number)
            self._account_holder = sanitize_name(account_holder)
            self._balance = sanitize_amount(initial_balance)
            self._transaction_history: List[dict] = []
            self._created_at = datetime.now()
            
            # Log successful account creation
            self.logger.info(f"Account created: {self._account_number} for {self._account_holder}")
            
            # Record initial deposit if any
            if self._balance > 0:
                self._record_transaction("INITIAL_DEPOSIT", self._balance, self._balance)
                
        except (InvalidAccountNumberError, InvalidNameError, InvalidAmountError) as e:
            self.logger.error(f"Failed to create account: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during account creation: {e}")
            raise BankAccountError(f"Account creation failed: {e}") from e

# What we accomplished in this step:
# - Set up comprehensive logging configuration
# - Started the BankAccount class with defensive initialization
# - Added transaction history tracking
# - Implemented proper error logging and handling


# Step 4: Add core BankAccount methods with defensive programming
# ===============================================================================

# Explanation:
# Now we'll add the main functionality with comprehensive error handling,
# precondition/postcondition checking, and transaction recording.

import logging
import re
from typing import Union, Optional, Any, List
from decimal import Decimal, InvalidOperation
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bank_account.log'),
        logging.StreamHandler()
    ]
)

class BankAccountError(Exception):
    """Base exception for bank account operations."""
    pass

class InvalidAccountNumberError(BankAccountError):
    """Raised when account number is invalid."""
    pass

class InvalidNameError(BankAccountError):
    """Raised when name is invalid."""
    pass

class InvalidAmountError(BankAccountError):
    """Raised when amount is invalid."""
    pass

class InsufficientFundsError(BankAccountError):
    """Raised when there are insufficient funds for withdrawal."""
    pass

def validate_account_number(account_number: str) -> bool:
    """Validate account number format."""
    if not isinstance(account_number, str):
        return False
    
    # Account number should be 5-12 digits
    pattern = r'^\d{5,12}$'
    return bool(re.match(pattern, account_number))

def validate_name(name: str) -> bool:
    """Validate person name."""
    if not isinstance(name, str):
        return False
    
    # Name should be 2-50 characters, letters, spaces, hyphens, apostrophes
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        return False
    
    pattern = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(pattern, name))

def validate_amount(amount: Union[int, float, Decimal]) -> bool:
    """Validate monetary amount."""
    try:
        decimal_amount = Decimal(str(amount))
        # Amount should be non-negative and have at most 2 decimal places
        return decimal_amount >= 0 and decimal_amount.as_tuple().exponent >= -2
    except (InvalidOperation, ValueError, TypeError):
        return False

def sanitize_account_number(account_number: Any) -> str:
    """Sanitize and validate account number."""
    if account_number is None:
        raise InvalidAccountNumberError("Account number cannot be None")
    
    # Convert to string and remove whitespace
    sanitized = str(account_number).strip()
    
    if not validate_account_number(sanitized):
        raise InvalidAccountNumberError(f"Invalid account number format: {sanitized}")
    
    return sanitized

def sanitize_name(name: Any) -> str:
    """Sanitize and validate name."""
    if name is None:
        raise InvalidNameError("Name cannot be None")
    
    # Convert to string, strip whitespace, normalize spaces
    sanitized = re.sub(r'\s+', ' ', str(name).strip())
    
    if not validate_name(sanitized):
        raise InvalidNameError(f"Invalid name format: {sanitized}")
    
    return sanitized

def sanitize_amount(amount: Any) -> Decimal:
    """Sanitize and validate amount."""
    if amount is None:
        raise InvalidAmountError("Amount cannot be None")
    
    try:
        # Convert to Decimal for precise monetary calculations
        decimal_amount = Decimal(str(amount))
        
        if not validate_amount(decimal_amount):
            raise InvalidAmountError(f"Invalid amount: {amount}")
        
        # Round to 2 decimal places for currency
        return decimal_amount.quantize(Decimal('0.01'))
    
    except (InvalidOperation, ValueError, TypeError) as e:
        raise InvalidAmountError(f"Cannot convert to valid amount: {amount}") from e

class BankAccount:
    """A defensive bank account implementation with comprehensive error handling."""
    
    def __init__(self, account_number: Any, account_holder: Any, initial_balance: Any = 0):
        """Initialize bank account with defensive validation.
        
        Args:
            account_number: Account number (will be sanitized)
            account_holder: Account holder name (will be sanitized)
            initial_balance: Initial balance (will be sanitized)
        """
        self.logger = logging.getLogger(f"{__name__}.BankAccount")
        
        try:
            # Defensive initialization with sanitization
            self._account_number = sanitize_account_number(account_number)
            self._account_holder = sanitize_name(account_holder)
            self._balance = sanitize_amount(initial_balance)
            self._transaction_history: List[dict] = []
            self._created_at = datetime.now()
            
            # Log successful account creation
            self.logger.info(f"Account created: {self._account_number} for {self._account_holder}")
            
            # Record initial deposit if any
            if self._balance > 0:
                self._record_transaction("INITIAL_DEPOSIT", self._balance, self._balance)
                
        except (InvalidAccountNumberError, InvalidNameError, InvalidAmountError) as e:
            self.logger.error(f"Failed to create account: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during account creation: {e}")
            raise BankAccountError(f"Account creation failed: {e}") from e
    
    def _record_transaction(self, transaction_type: str, amount: Decimal, new_balance: Decimal):
        """Record a transaction in the history."""
        transaction = {
            'timestamp': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance_after': new_balance
        }
        self._transaction_history.append(transaction)
        self.logger.info(f"Transaction recorded: {transaction_type} ${amount} - New balance: ${new_balance}")
    
    def deposit(self, amount: Any) -> bool:
        """Deposit money into the account with defensive validation.
        
        Args:
            amount: Amount to deposit (will be sanitized)
            
        Returns:
            bool: True if deposit successful
            
        Raises:
            InvalidAmountError: If amount is invalid
            BankAccountError: If deposit fails for other reasons
        """
        try:
            # Precondition: Validate and sanitize amount
            sanitized_amount = sanitize_amount(amount)
            
            if sanitized_amount <= 0:
                raise InvalidAmountError("Deposit amount must be positive")
            
            # Store original balance for rollback if needed
            original_balance = self._balance
            
            # Perform the deposit
            self._balance += sanitized_amount
            
            # Postcondition: Verify balance increased correctly
            expected_balance = original_balance + sanitized_amount
            if self._balance != expected_balance:
                # Rollback on postcondition failure
                self._balance = original_balance
                raise BankAccountError("Deposit postcondition failed - balance inconsistency")
            
            # Record successful transaction
            self._record_transaction("DEPOSIT", sanitized_amount, self._balance)
            
            self.logger.info(f"Deposit successful: ${sanitized_amount} to account {self._account_number}")
            return True
            
        except InvalidAmountError as e:
            self.logger.warning(f"Invalid deposit attempt: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during deposit: {e}")
            raise BankAccountError(f"Deposit failed: {e}") from e
    
    def withdraw(self, amount: Any) -> bool:
        """Withdraw money from the account with defensive validation.
        
        Args:
            amount: Amount to withdraw (will be sanitized)
            
        Returns:
            bool: True if withdrawal successful
            
        Raises:
            InvalidAmountError: If amount is invalid
            InsufficientFundsError: If insufficient funds
            BankAccountError: If withdrawal fails for other reasons
        """
        try:
            # Precondition: Validate and sanitize amount
            sanitized_amount = sanitize_amount(amount)
            
            if sanitized_amount <= 0:
                raise InvalidAmountError("Withdrawal amount must be positive")
            
            # Precondition: Check sufficient funds
            if self._balance < sanitized_amount:
                raise InsufficientFundsError(
                    f"Insufficient funds: ${self._balance} available, ${sanitized_amount} requested"
                )
            
            # Store original balance for rollback if needed
            original_balance = self._balance
            
            # Perform the withdrawal
            self._balance -= sanitized_amount
            
            # Postcondition: Verify balance decreased correctly
            expected_balance = original_balance - sanitized_amount
            if self._balance != expected_balance:
                # Rollback on postcondition failure
                self._balance = original_balance
                raise BankAccountError("Withdrawal postcondition failed - balance inconsistency")
            
            # Postcondition: Verify balance is not negative
            if self._balance < 0:
                # Rollback on postcondition failure
                self._balance = original_balance
                raise BankAccountError("Withdrawal postcondition failed - negative balance")
            
            # Record successful transaction
            self._record_transaction("WITHDRAWAL", sanitized_amount, self._balance)
            
            self.logger.info(f"Withdrawal successful: ${sanitized_amount} from account {self._account_number}")
            return True
            
        except (InvalidAmountError, InsufficientFundsError) as e:
            self.logger.warning(f"Invalid withdrawal attempt: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during withdrawal: {e}")
            raise BankAccountError(f"Withdrawal failed: {e}") from e
    
    def get_balance(self) -> Decimal:
        """Get current balance safely."""
        return self._balance
    
    def get_account_info(self) -> dict:
        """Get account information safely."""
        return {
            'account_number': self._account_number,
            'account_holder': self._account_holder,
            'balance': self._balance,
            'created_at': self._created_at,
            'transaction_count': len(self._transaction_history)
        }

# What we accomplished in this step:
# - Added deposit and withdraw methods with comprehensive validation
# - Implemented precondition and postcondition checking
# - Added transaction recording and rollback mechanisms
# - Used defensive programming throughout all operations


# Step 5: Add additional defensive methods and demonstration
# ===============================================================================

# Explanation:
# We'll add more methods and create a comprehensive demonstration that shows
# all defensive programming techniques in action.

import logging
import re
from typing import Union, Optional, Any, List
from decimal import Decimal, InvalidOperation
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bank_account.log'),
        logging.StreamHandler()
    ]
)

class BankAccountError(Exception):
    """Base exception for bank account operations."""
    pass

class InvalidAccountNumberError(BankAccountError):
    """Raised when account number is invalid."""
    pass

class InvalidNameError(BankAccountError):
    """Raised when name is invalid."""
    pass

class InvalidAmountError(BankAccountError):
    """Raised when amount is invalid."""
    pass

class InsufficientFundsError(BankAccountError):
    """Raised when there are insufficient funds for withdrawal."""
    pass

def validate_account_number(account_number: str) -> bool:
    """Validate account number format."""
    if not isinstance(account_number, str):
        return False
    
    # Account number should be 5-12 digits
    pattern = r'^\d{5,12}$'
    return bool(re.match(pattern, account_number))

def validate_name(name: str) -> bool:
    """Validate person name."""
    if not isinstance(name, str):
        return False
    
    # Name should be 2-50 characters, letters, spaces, hyphens, apostrophes
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        return False
    
    pattern = r"^[a-zA-Z\s\-']+$"
    return bool(re.match(pattern, name))

def validate_amount(amount: Union[int, float, Decimal]) -> bool:
    """Validate monetary amount."""
    try:
        decimal_amount = Decimal(str(amount))
        # Amount should be non-negative and have at most 2 decimal places
        return decimal_amount >= 0 and decimal_amount.as_tuple().exponent >= -2
    except (InvalidOperation, ValueError, TypeError):
        return False

def sanitize_account_number(account_number: Any) -> str:
    """Sanitize and validate account number."""
    if account_number is None:
        raise InvalidAccountNumberError("Account number cannot be None")
    
    # Convert to string and remove whitespace
    sanitized = str(account_number).strip()
    
    if not validate_account_number(sanitized):
        raise InvalidAccountNumberError(f"Invalid account number format: {sanitized}")
    
    return sanitized

def sanitize_name(name: Any) -> str:
    """Sanitize and validate name."""
    if name is None:
        raise InvalidNameError("Name cannot be None")
    
    # Convert to string, strip whitespace, normalize spaces
    sanitized = re.sub(r'\s+', ' ', str(name).strip())
    
    if not validate_name(sanitized):
        raise InvalidNameError(f"Invalid name format: {sanitized}")
    
    return sanitized

def sanitize_amount(amount: Any) -> Decimal:
    """Sanitize and validate amount."""
    if amount is None:
        raise InvalidAmountError("Amount cannot be None")
    
    try:
        # Convert to Decimal for precise monetary calculations
        decimal_amount = Decimal(str(amount))
        
        if not validate_amount(decimal_amount):
            raise InvalidAmountError(f"Invalid amount: {amount}")
        
        # Round to 2 decimal places for currency
        return decimal_amount.quantize(Decimal('0.01'))
    
    except (InvalidOperation, ValueError, TypeError) as e:
        raise InvalidAmountError(f"Cannot convert to valid amount: {amount}") from e

class BankAccount:
    """A defensive bank account implementation with comprehensive error handling."""
    
    def __init__(self, account_number: Any, account_holder: Any, initial_balance: Any = 0):
        """Initialize bank account with defensive validation.
        
        Args:
            account_number: Account number (will be sanitized)
            account_holder: Account holder name (will be sanitized)
            initial_balance: Initial balance (will be sanitized)
        """
        self.logger = logging.getLogger(f"{__name__}.BankAccount")
        
        try:
            # Defensive initialization with sanitization
            self._account_number = sanitize_account_number(account_number)
            self._account_holder = sanitize_name(account_holder)
            self._balance = sanitize_amount(initial_balance)
            self._transaction_history: List[dict] = []
            self._created_at = datetime.now()
            
            # Log successful account creation
            self.logger.info(f"Account created: {self._account_number} for {self._account_holder}")
            
            # Record initial deposit if any
            if self._balance > 0:
                self._record_transaction("INITIAL_DEPOSIT", self._balance, self._balance)
                
        except (InvalidAccountNumberError, InvalidNameError, InvalidAmountError) as e:
            self.logger.error(f"Failed to create account: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during account creation: {e}")
            raise BankAccountError(f"Account creation failed: {e}") from e
    
    def _record_transaction(self, transaction_type: str, amount: Decimal, new_balance: Decimal):
        """Record a transaction in the history."""
        transaction = {
            'timestamp': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance_after': new_balance
        }
        self._transaction_history.append(transaction)
        self.logger.info(f"Transaction recorded: {transaction_type} ${amount} - New balance: ${new_balance}")
    
    def deposit(self, amount: Any) -> bool:
        """Deposit money into the account with defensive validation.
        
        Args:
            amount: Amount to deposit (will be sanitized)
            
        Returns:
            bool: True if deposit successful
            
        Raises:
            InvalidAmountError: If amount is invalid
            BankAccountError: If deposit fails for other reasons
        """
        try:
            # Precondition: Validate and sanitize amount
            sanitized_amount = sanitize_amount(amount)
            
            if sanitized_amount <= 0:
                raise InvalidAmountError("Deposit amount must be positive")
            
            # Store original balance for rollback if needed
            original_balance = self._balance
            
            # Perform the deposit
            self._balance += sanitized_amount
            
            # Postcondition: Verify balance increased correctly
            expected_balance = original_balance + sanitized_amount
            if self._balance != expected_balance:
                # Rollback on postcondition failure
                self._balance = original_balance
                raise BankAccountError("Deposit postcondition failed - balance inconsistency")
            
            # Record successful transaction
            self._record_transaction("DEPOSIT", sanitized_amount, self._balance)
            
            self.logger.info(f"Deposit successful: ${sanitized_amount} to account {self._account_number}")
            return True
            
        except InvalidAmountError as e:
            self.logger.warning(f"Invalid deposit attempt: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during deposit: {e}")
            raise BankAccountError(f"Deposit failed: {e}") from e
    
    def withdraw(self, amount: Any) -> bool:
        """Withdraw money from the account with defensive validation.
        
        Args:
            amount: Amount to withdraw (will be sanitized)
            
        Returns:
            bool: True if withdrawal successful
            
        Raises:
            InvalidAmountError: If amount is invalid
            InsufficientFundsError: If insufficient funds
            BankAccountError: If withdrawal fails for other reasons
        """
        try:
            # Precondition: Validate and sanitize amount
            sanitized_amount = sanitize_amount(amount)
            
            if sanitized_amount <= 0:
                raise InvalidAmountError("Withdrawal amount must be positive")
            
            # Precondition: Check sufficient funds
            if self._balance < sanitized_amount:
                raise InsufficientFundsError(
                    f"Insufficient funds: ${self._balance} available, ${sanitized_amount} requested"
                )
            
            # Store original balance for rollback if needed
            original_balance = self._balance
            
            # Perform the withdrawal
            self._balance -= sanitized_amount
            
            # Postcondition: Verify balance decreased correctly
            expected_balance = original_balance - sanitized_amount
            if self._balance != expected_balance:
                # Rollback on postcondition failure
                self._balance = original_balance
                raise BankAccountError("Withdrawal postcondition failed - balance inconsistency")
            
            # Postcondition: Verify balance is not negative
            if self._balance < 0:
                # Rollback on postcondition failure
                self._balance = original_balance
                raise BankAccountError("Withdrawal postcondition failed - negative balance")
            
            # Record successful transaction
            self._record_transaction("WITHDRAWAL", sanitized_amount, self._balance)
            
            self.logger.info(f"Withdrawal successful: ${sanitized_amount} from account {self._account_number}")
            return True
            
        except (InvalidAmountError, InsufficientFundsError) as e:
            self.logger.warning(f"Invalid withdrawal attempt: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during withdrawal: {e}")
            raise BankAccountError(f"Withdrawal failed: {e}") from e
    
    def transfer(self, amount: Any, target_account: 'BankAccount') -> bool:
        """Transfer money to another account with defensive validation.
        
        Args:
            amount: Amount to transfer (will be sanitized)
            target_account: Target BankAccount instance
            
        Returns:
            bool: True if transfer successful
            
        Raises:
            InvalidAmountError: If amount is invalid
            InsufficientFundsError: If insufficient funds
            BankAccountError: If transfer fails for other reasons
        """
        try:
            # Precondition: Validate target account
            if not isinstance(target_account, BankAccount):
                raise BankAccountError("Target must be a valid BankAccount instance")
            
            # Precondition: Validate and sanitize amount
            sanitized_amount = sanitize_amount(amount)
            
            if sanitized_amount <= 0:
                raise InvalidAmountError("Transfer amount must be positive")
            
            # Precondition: Check sufficient funds
            if self._balance < sanitized_amount:
                raise InsufficientFundsError(
                    f"Insufficient funds for transfer: ${self._balance} available, ${sanitized_amount} requested"
                )
            
            # Store original balances for rollback if needed
            original_source_balance = self._balance
            original_target_balance = target_account._balance
            
            try:
                # Perform the transfer (atomic operation)
                self._balance -= sanitized_amount
                target_account._balance += sanitized_amount
                
                # Postcondition: Verify balances are correct
                expected_source_balance = original_source_balance - sanitized_amount
                expected_target_balance = original_target_balance + sanitized_amount
                
                if (self._balance != expected_source_balance or 
                    target_account._balance != expected_target_balance):
                    # Rollback on postcondition failure
                    self._balance = original_source_balance
                    target_account._balance = original_target_balance
                    raise BankAccountError("Transfer postcondition failed - balance inconsistency")
                
                # Record transactions in both accounts
                self._record_transaction("TRANSFER_OUT", sanitized_amount, self._balance)
                target_account._record_transaction("TRANSFER_IN", sanitized_amount, target_account._balance)
                
                self.logger.info(f"Transfer successful: ${sanitized_amount} from {self._account_number} to {target_account._account_number}")
                return True
                
            except Exception as e:
                # Rollback on any error during transfer
                self._balance = original_source_balance
                target_account._balance = original_target_balance
                raise BankAccountError(f"Transfer failed during execution: {e}") from e
            
        except (InvalidAmountError, InsufficientFundsError) as e:
            self.logger.warning(f"Invalid transfer attempt: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error during transfer: {e}")
            raise BankAccountError(f"Transfer failed: {e}") from e
    
    def get_balance(self) -> Decimal:
        """Get current balance safely."""
        return self._balance
    
    def get_account_info(self) -> dict:
        """Get account information safely."""
        return {
            'account_number': self._account_number,
            'account_holder': self._account_holder,
            'balance': self._balance,
            'created_at': self._created_at,
            'transaction_count': len(self._transaction_history)
        }
    
    def get_transaction_history(self, limit: Optional[int] = None) -> List[dict]:
        """Get transaction history with optional limit."""
        try:
            if limit is not None:
                if not isinstance(limit, int) or limit < 0:
                    raise InvalidAmountError("Limit must be a non-negative integer")
                return self._transaction_history[-limit:] if limit > 0 else []
            return self._transaction_history.copy()
        except Exception as e:
            self.logger.error(f"Error retrieving transaction history: {e}")
            return []
    
    def __str__(self) -> str:
        """String representation of the account."""
        return (f"BankAccount(account_number={self._account_number}, "
                f"holder={self._account_holder}, balance=${self._balance})")
    
    def __repr__(self) -> str:
        """Developer representation of the account."""
        return self.__str__()


# Demonstration of defensive programming techniques
def demonstrate_defensive_programming():
    """Comprehensive demonstration of defensive programming in action."""
    print("=" * 80)
    print("DEFENSIVE PROGRAMMING DEMONSTRATION")
    print("=" * 80)
    
    try:
        # Test 1: Valid account creation
        print("\n1. Creating valid accounts...")
        account1 = BankAccount("12345", "John Doe", 1000.0)
        account2 = BankAccount("67890", "Jane Smith", 500.0)
        print(f"✓ Account 1: {account1}")
        print(f"✓ Account 2: {account2}")
        
        # Test 2: Valid operations
        print("\n2. Testing valid operations...")
        account1.deposit(250.0)
        print(f"✓ Deposited $250.0, new balance: ${account1.get_balance()}")
        
        account1.withdraw(100.0)
        print(f"✓ Withdrew $100.0, new balance: ${account1.get_balance()}")
        
        account1.transfer(200.0, account2)
        print(f"✓ Transferred $200.0, account1 balance: ${account1.get_balance()}")
        print(f"✓ Account2 balance after transfer: ${account2.get_balance()}")
        
    except Exception as e:
        print(f"✗ Unexpected error in valid operations: {e}")
    
    # Test 3: Invalid inputs (should fail gracefully)
    print("\n3. Testing invalid inputs (should fail gracefully)...")
    
    test_cases = [
        ("Invalid account number", lambda: BankAccount("abc", "John Doe", 100)),
        ("Invalid name", lambda: BankAccount("12345", "", 100)),
        ("Invalid initial balance", lambda: BankAccount("12345", "John Doe", -100)),
        ("Negative deposit", lambda: account1.deposit(-50)),
        ("Negative withdrawal", lambda: account1.withdraw(-50)),
        ("Insufficient funds", lambda: account1.withdraw(10000)),
        ("Invalid transfer target", lambda: account1.transfer(100, "not_an_account")),
    ]
    
    for test_name, test_func in test_cases:
        try:
            test_func()
            print(f"✗ {test_name}: Should have failed but didn't!")
        except (BankAccountError, InvalidAccountNumberError, InvalidNameError, 
                InvalidAmountError, InsufficientFundsError) as e:
            print(f"✓ {test_name}: Correctly handled - {type(e).__name__}")
        except Exception as e:
            print(f"? {test_name}: Unexpected error type - {type(e).__name__}: {e}")
    
    # Test 4: Edge cases and boundary conditions
    print("\n4. Testing edge cases...")
    try:
        # Test with very small amounts
        account1.deposit(0.01)
        print("✓ Minimum deposit (0.01) handled correctly")
        
        # Test with string numbers
        account1.deposit("50.50")
        print("✓ String number input sanitized correctly")
        
        # Test transaction history
        history = account1.get_transaction_history(3)
        print(f"✓ Retrieved last 3 transactions: {len(history)} items")
        
    except Exception as e:
        print(f"✗ Edge case error: {e}")
    
    print("\n" + "=" * 80)
    print("DEFENSIVE PROGRAMMING DEMONSTRATION COMPLETE")
    print("=" * 80)


# What we accomplished in this step:
# - Added transfer method with atomic operations and rollback
# - Added transaction history retrieval with validation
# - Created comprehensive demonstration showing all defensive techniques
# - Implemented graceful error handling for all edge cases


# Step 6: Final execution and summary
# ===============================================================================

# Explanation:
# This final step runs the demonstration and provides a comprehensive summary
# of all defensive programming techniques implemented.

if __name__ == "__main__":
    # Run the comprehensive demonstration
    demonstrate_defensive_programming()
    
    print("\n" + "=" * 80)
    print("DEFENSIVE PROGRAMMING TECHNIQUES SUMMARY")
    print("=" * 80)
    
    print("""
TECHNIQUES DEMONSTRATED:

1. INPUT VALIDATION & SANITIZATION:
   ✓ Type checking and conversion
   ✓ Regular expression validation
   ✓ Range and boundary checking
   ✓ Data normalization and cleaning

2. CUSTOM EXCEPTION HIERARCHY:
   ✓ Specific exception types for different errors
   ✓ Exception chaining for debugging
   ✓ Meaningful error messages

3. PRECONDITION & POSTCONDITION CHECKING:
   ✓ Validate inputs before processing
   ✓ Verify results after operations
   ✓ Automatic rollback on failures

4. COMPREHENSIVE LOGGING:
   ✓ Operation tracking
   ✓ Error logging with context
   ✓ Audit trail for debugging

5. FAIL-SAFE MECHANISMS:
   ✓ Graceful degradation
   ✓ Rollback on errors
   ✓ Atomic operations

6. DEFENSIVE CODING PRACTICES:
   ✓ Assume all inputs are potentially invalid
   ✓ Handle unexpected errors gracefully
   ✓ Provide meaningful feedback
   ✓ Maintain system integrity

7. CONTRACT PROGRAMMING:
   ✓ Clear method contracts (docstrings)
   ✓ Explicit preconditions
   ✓ Verified postconditions
   ✓ Invariant maintenance

KEY BENEFITS:
- Robust error handling
- Better debugging capabilities
- Improved system reliability
- Enhanced security
- Easier maintenance
- Better user experience

BEST PRACTICES APPLIED:
- Never trust external input
- Validate early and often
- Fail fast with clear messages
- Log everything important
- Design for failure scenarios
- Use type hints for clarity
- Implement proper exception hierarchies
- Test edge cases thoroughly
""")
    
    print("=" * 80)
    print("DEFENSIVE PROGRAMMING IMPLEMENTATION COMPLETE!")
    print("=" * 80)


# ===============================================================================
#                              FINAL SUMMARY
# ===============================================================================
#
# COMPREHENSIVE DEFENSIVE PROGRAMMING IMPLEMENTATION
#
# This implementation demonstrates all major defensive programming techniques:
#
# 1. INPUT VALIDATION: Every input is validated and sanitized before use
# 2. ERROR HANDLING: Comprehensive exception hierarchy with specific error types
# 3. LOGGING: Complete audit trail of all operations and errors
# 4. CONTRACTS: Preconditions and postconditions ensure method contracts
# 5. ROLLBACK: Failed operations are rolled back to maintain consistency
# 6. FAIL-SAFE: System degrades gracefully under error conditions
# 7. ATOMIC OPERATIONS: Complex operations (like transfers) are atomic
#
# The BankAccount class serves as a real-world example showing how defensive
# programming creates robust, maintainable, and secure code that handles
# errors gracefully while providing excellent debugging capabilities.
#
# Key Learning Points:
# - Always validate inputs before processing
# - Use specific exception types for different error conditions
# - Implement comprehensive logging for debugging and auditing
# - Design operations to be atomic and reversible
# - Test thoroughly with invalid inputs and edge cases
# - Provide clear error messages for better user experience
#
# This approach results in code that is:
# - More reliable and robust
# - Easier to debug and maintain
# - More secure against malicious inputs
# - Better at handling unexpected conditions
# - More professional and production-ready
#
# ===============================================================================

