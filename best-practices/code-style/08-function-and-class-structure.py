"""Best Practices: Function and Class Structure

This module demonstrates best practices for organizing functions and classes
in Python, including proper naming, documentation, structure, and organization.

Requirements:
1. Demonstrate proper function structure and organization
2. Show class design best practices
3. Illustrate proper naming conventions
4. Show documentation standards
5. Demonstrate code organization principles

Example usage:
    calculator = Calculator()
    result = calculator.calculate(10, 5, 'add')
    user_manager = UserManager()
    user = user_manager.create_user("john_doe", "john@example.com")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Think about function naming conventions
# - Consider class organization principles
# - Focus on readability and maintainability
# - Use proper documentation
# - Follow PEP 8 guidelines
#
# Remember: Good code structure makes code easier to read, maintain, and debug!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)


















































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - How should functions be named and organized?
# - What makes a class well-structured?
# - How should methods be ordered in a class?
# - What documentation should be included?
#
# Remember: Start simple and build up complexity gradually!


# ===============================================================================
#                           STEP-BY-STEP SOLUTION
# ===============================================================================
#
# CLASSROOM-STYLE WALKTHROUGH
#
# Let's explore function and class structure best practices step by step!
# Each step builds upon the previous one, so you can follow along and understand
# the complete thought process.
#
# ===============================================================================


# Step 1: Basic function structure and naming conventions
# ===============================================================================

# Explanation:
# Functions should have clear, descriptive names using snake_case.
# They should be small, focused, and do one thing well.

def calculate_area_of_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
        
    Returns:
        The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def format_user_name(first_name: str, last_name: str) -> str:
    """Format a user's full name.
    
    Args:
        first_name: The user's first name
        last_name: The user's last name
        
    Returns:
        Formatted full name
    """
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def validate_email_address(email: str) -> bool:
    """Validate an email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# What we accomplished in this step:
# - Demonstrated clear, descriptive function names
# - Showed proper type hints and documentation
# - Illustrated single responsibility principle


# Step 2: Basic class structure and organization
# ===============================================================================

# Explanation:
# Classes should follow a consistent structure with proper method ordering.
# The typical order is: class docstring, class variables, __init__, 
# special methods, public methods, private methods.

from typing import List, Optional
from datetime import datetime

def calculate_area_of_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
        
    Returns:
        The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def format_user_name(first_name: str, last_name: str) -> str:
    """Format a user's full name.
    
    Args:
        first_name: The user's first name
        last_name: The user's last name
        
    Returns:
        Formatted full name
    """
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def validate_email_address(email: str) -> bool:
    """Validate an email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


class User:
    """Represents a user in the system.
    
    This class demonstrates proper class structure with clear organization
    of attributes and methods.
    
    Attributes:
        username: The user's unique username
        email: The user's email address
        created_at: When the user was created
    """
    
    # Class variable (shared by all instances)
    total_users: int = 0
    
    def __init__(self, username: str, email: str) -> None:
        """Initialize a new user.
        
        Args:
            username: The user's unique username
            email: The user's email address
            
        Raises:
            ValueError: If username or email is invalid
        """
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)
        self.created_at = datetime.now()
        self._is_active = True
        
        # Update class variable
        User.total_users += 1
    
    def __str__(self) -> str:
        """Return string representation of the user."""
        return f"User(username='{self.username}', email='{self.email}')"
    
    def __repr__(self) -> str:
        """Return detailed string representation for debugging."""
        return (f"User(username='{self.username}', email='{self.email}', "
                f"created_at='{self.created_at}', active={self._is_active})")
    
    def get_display_name(self) -> str:
        """Get the user's display name.
        
        Returns:
            Formatted display name
        """
        return self.username.replace('_', ' ').title()
    
    def is_active(self) -> bool:
        """Check if the user is active.
        
        Returns:
            True if user is active, False otherwise
        """
        return self._is_active
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self._is_active = False
    
    def activate(self) -> None:
        """Activate the user account."""
        self._is_active = True
    
    def _validate_username(self, username: str) -> str:
        """Validate and clean username.
        
        Args:
            username: Username to validate
            
        Returns:
            Cleaned username
            
        Raises:
            ValueError: If username is invalid
        """
        if not username or len(username.strip()) < 3:
            raise ValueError("Username must be at least 3 characters long")
        
        cleaned = username.strip().lower()
        if not cleaned.replace('_', '').isalnum():
            raise ValueError("Username can only contain letters, numbers, and underscores")
        
        return cleaned
    
    def _validate_email(self, email: str) -> str:
        """Validate email address.
        
        Args:
            email: Email to validate
            
        Returns:
            Cleaned email
            
        Raises:
            ValueError: If email is invalid
        """
        if not validate_email_address(email):
            raise ValueError("Invalid email address format")
        
        return email.strip().lower()

# What we accomplished in this step:
# - Demonstrated proper class structure and method ordering
# - Showed class and instance variables
# - Illustrated special methods (__str__, __repr__)
# - Used private methods for internal validation


# Step 3: Advanced class design with properties and class methods
# ===============================================================================

# Explanation:
# Advanced classes use properties for controlled access to attributes,
# class methods for alternative constructors, and static methods for utilities.

from typing import List, Optional
from datetime import datetime
import json

def calculate_area_of_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
        
    Returns:
        The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def format_user_name(first_name: str, last_name: str) -> str:
    """Format a user's full name.
    
    Args:
        first_name: The user's first name
        last_name: The user's last name
        
    Returns:
        Formatted full name
    """
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def validate_email_address(email: str) -> bool:
    """Validate an email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


class User:
    """Represents a user in the system.
    
    This class demonstrates proper class structure with clear organization
    of attributes and methods.
    
    Attributes:
        username: The user's unique username
        email: The user's email address
        created_at: When the user was created
    """
    
    # Class variable (shared by all instances)
    total_users: int = 0
    
    def __init__(self, username: str, email: str) -> None:
        """Initialize a new user.
        
        Args:
            username: The user's unique username
            email: The user's email address
            
        Raises:
            ValueError: If username or email is invalid
        """
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)
        self.created_at = datetime.now()
        self._is_active = True
        
        # Update class variable
        User.total_users += 1
    
    def __str__(self) -> str:
        """Return string representation of the user."""
        return f"User(username='{self.username}', email='{self.email}')"
    
    def __repr__(self) -> str:
        """Return detailed string representation for debugging."""
        return (f"User(username='{self.username}', email='{self.email}', "
                f"created_at='{self.created_at}', active={self._is_active})")
    
    def get_display_name(self) -> str:
        """Get the user's display name.
        
        Returns:
            Formatted display name
        """
        return self.username.replace('_', ' ').title()
    
    def is_active(self) -> bool:
        """Check if the user is active.
        
        Returns:
            True if user is active, False otherwise
        """
        return self._is_active
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self._is_active = False
    
    def activate(self) -> None:
        """Activate the user account."""
        self._is_active = True
    
    def _validate_username(self, username: str) -> str:
        """Validate and clean username.
        
        Args:
            username: Username to validate
            
        Returns:
            Cleaned username
            
        Raises:
            ValueError: If username is invalid
        """
        if not username or len(username.strip()) < 3:
            raise ValueError("Username must be at least 3 characters long")
        
        cleaned = username.strip().lower()
        if not cleaned.replace('_', '').isalnum():
            raise ValueError("Username can only contain letters, numbers, and underscores")
        
        return cleaned
    
    def _validate_email(self, email: str) -> str:
        """Validate email address.
        
        Args:
            email: Email to validate
            
        Returns:
            Cleaned email
            
        Raises:
            ValueError: If email is invalid
        """
        if not validate_email_address(email):
            raise ValueError("Invalid email address format")
        
        return email.strip().lower()


class BankAccount:
    """Represents a bank account with proper encapsulation.
    
    This class demonstrates advanced features like properties, class methods,
    static methods, and proper data validation.
    """
    
    # Class variables
    _account_counter: int = 0
    minimum_balance: float = 0.0
    
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        """Initialize a new bank account.
        
        Args:
            owner: The account owner's name
            initial_balance: Initial account balance
            
        Raises:
            ValueError: If initial balance is negative
        """
        self._owner = owner
        self._balance = 0.0
        self.balance = initial_balance  # Use property setter for validation
        
        BankAccount._account_counter += 1
        self._account_number = f"ACC{BankAccount._account_counter:06d}"
        self._transaction_history: List[str] = []
        
        self._add_transaction(f"Account opened with balance: ${initial_balance:.2f}")
    
    @property
    def balance(self) -> float:
        """Get the current account balance."""
        return self._balance
    
    @balance.setter
    def balance(self, amount: float) -> None:
        """Set the account balance with validation.
        
        Args:
            amount: New balance amount
            
        Raises:
            ValueError: If amount is below minimum balance
        """
        if amount < self.minimum_balance:
            raise ValueError(f"Balance cannot be below ${self.minimum_balance:.2f}")
        self._balance = amount
    
    @property
    def owner(self) -> str:
        """Get the account owner's name."""
        return self._owner
    
    @property
    def account_number(self) -> str:
        """Get the account number."""
        return self._account_number
    
    @property
    def transaction_history(self) -> List[str]:
        """Get a copy of the transaction history."""
        return self._transaction_history.copy()
    
    @classmethod
    def create_savings_account(cls, owner: str, initial_balance: float = 100.0) -> 'BankAccount':
        """Create a savings account with higher minimum balance.
        
        Args:
            owner: The account owner's name
            initial_balance: Initial balance (default $100)
            
        Returns:
            New savings account instance
        """
        account = cls(owner, initial_balance)
        account.minimum_balance = 100.0
        account._add_transaction("Converted to savings account")
        return account
    
    @classmethod
    def from_json(cls, json_data: str) -> 'BankAccount':
        """Create account from JSON data.
        
        Args:
            json_data: JSON string containing account data
            
        Returns:
            New account instance
        """
        data = json.loads(json_data)
        return cls(data['owner'], data['balance'])
    
    @staticmethod
    def calculate_interest(principal: float, rate: float, time: float) -> float:
        """Calculate simple interest.
        
        Args:
            principal: Principal amount
            rate: Interest rate (as decimal)
            time: Time period in years
            
        Returns:
            Interest amount
        """
        return principal * rate * time
    
    def deposit(self, amount: float) -> None:
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._add_transaction(f"Deposited: ${amount:.2f}")
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            
        Raises:
            ValueError: If amount is invalid or insufficient funds
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if self._balance - amount < self.minimum_balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._add_transaction(f"Withdrew: ${amount:.2f}")
    
    def transfer(self, other_account: 'BankAccount', amount: float) -> None:
        """Transfer money to another account.
        
        Args:
            other_account: Destination account
            amount: Amount to transfer
        """
        self.withdraw(amount)
        other_account.deposit(amount)
        self._add_transaction(f"Transferred ${amount:.2f} to {other_account.account_number}")
        other_account._add_transaction(f"Received ${amount:.2f} from {self.account_number}")
    
    def _add_transaction(self, description: str) -> None:
        """Add a transaction to the history.
        
        Args:
            description: Transaction description
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transaction_history.append(f"[{timestamp}] {description}")
    
    def __str__(self) -> str:
        """Return string representation of the account."""
        return f"BankAccount({self.account_number}, Owner: {self.owner}, Balance: ${self.balance:.2f})"

# What we accomplished in this step:
# - Demonstrated property decorators for controlled attribute access
# - Showed class methods for alternative constructors
# - Illustrated static methods for utility functions
# - Used proper encapsulation with private attributes


# Step 4: Inheritance and composition patterns
# ===============================================================================

# Explanation:
# Good class design often involves inheritance for "is-a" relationships
# and composition for "has-a" relationships. This step shows both patterns.

from typing import List, Optional, Dict, Any
from datetime import datetime
from abc import ABC, abstractmethod
import json

def calculate_area_of_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
        
    Returns:
        The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def format_user_name(first_name: str, last_name: str) -> str:
    """Format a user's full name.
    
    Args:
        first_name: The user's first name
        last_name: The user's last name
        
    Returns:
        Formatted full name
    """
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def validate_email_address(email: str) -> bool:
    """Validate an email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


class User:
    """Represents a user in the system.
    
    This class demonstrates proper class structure with clear organization
    of attributes and methods.
    
    Attributes:
        username: The user's unique username
        email: The user's email address
        created_at: When the user was created
    """
    
    # Class variable (shared by all instances)
    total_users: int = 0
    
    def __init__(self, username: str, email: str) -> None:
        """Initialize a new user.
        
        Args:
            username: The user's unique username
            email: The user's email address
            
        Raises:
            ValueError: If username or email is invalid
        """
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)
        self.created_at = datetime.now()
        self._is_active = True
        
        # Update class variable
        User.total_users += 1
    
    def __str__(self) -> str:
        """Return string representation of the user."""
        return f"User(username='{self.username}', email='{self.email}')"
    
    def __repr__(self) -> str:
        """Return detailed string representation for debugging."""
        return (f"User(username='{self.username}', email='{self.email}', "
                f"created_at='{self.created_at}', active={self._is_active})")
    
    def get_display_name(self) -> str:
        """Get the user's display name.
        
        Returns:
            Formatted display name
        """
        return self.username.replace('_', ' ').title()
    
    def is_active(self) -> bool:
        """Check if the user is active.
        
        Returns:
            True if user is active, False otherwise
        """
        return self._is_active
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self._is_active = False
    
    def activate(self) -> None:
        """Activate the user account."""
        self._is_active = True
    
    def _validate_username(self, username: str) -> str:
        """Validate and clean username.
        
        Args:
            username: Username to validate
            
        Returns:
            Cleaned username
            
        Raises:
            ValueError: If username is invalid
        """
        if not username or len(username.strip()) < 3:
            raise ValueError("Username must be at least 3 characters long")
        
        cleaned = username.strip().lower()
        if not cleaned.replace('_', '').isalnum():
            raise ValueError("Username can only contain letters, numbers, and underscores")
        
        return cleaned
    
    def _validate_email(self, email: str) -> str:
        """Validate email address.
        
        Args:
            email: Email to validate
            
        Returns:
            Cleaned email
            
        Raises:
            ValueError: If email is invalid
        """
        if not validate_email_address(email):
            raise ValueError("Invalid email address format")
        
        return email.strip().lower()


class BankAccount:
    """Represents a bank account with proper encapsulation.
    
    This class demonstrates advanced features like properties, class methods,
    static methods, and proper data validation.
    """
    
    # Class variables
    _account_counter: int = 0
    minimum_balance: float = 0.0
    
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        """Initialize a new bank account.
        
        Args:
            owner: The account owner's name
            initial_balance: Initial account balance
            
        Raises:
            ValueError: If initial balance is negative
        """
        self._owner = owner
        self._balance = 0.0
        self.balance = initial_balance  # Use property setter for validation
        
        BankAccount._account_counter += 1
        self._account_number = f"ACC{BankAccount._account_counter:06d}"
        self._transaction_history: List[str] = []
        
        self._add_transaction(f"Account opened with balance: ${initial_balance:.2f}")
    
    @property
    def balance(self) -> float:
        """Get the current account balance."""
        return self._balance
    
    @balance.setter
    def balance(self, amount: float) -> None:
        """Set the account balance with validation.
        
        Args:
            amount: New balance amount
            
        Raises:
            ValueError: If amount is below minimum balance
        """
        if amount < self.minimum_balance:
            raise ValueError(f"Balance cannot be below ${self.minimum_balance:.2f}")
        self._balance = amount
    
    @property
    def owner(self) -> str:
        """Get the account owner's name."""
        return self._owner
    
    @property
    def account_number(self) -> str:
        """Get the account number."""
        return self._account_number
    
    @property
    def transaction_history(self) -> List[str]:
        """Get a copy of the transaction history."""
        return self._transaction_history.copy()
    
    @classmethod
    def create_savings_account(cls, owner: str, initial_balance: float = 100.0) -> 'BankAccount':
        """Create a savings account with higher minimum balance.
        
        Args:
            owner: The account owner's name
            initial_balance: Initial balance (default $100)
            
        Returns:
            New savings account instance
        """
        account = cls(owner, initial_balance)
        account.minimum_balance = 100.0
        account._add_transaction("Converted to savings account")
        return account
    
    @classmethod
    def from_json(cls, json_data: str) -> 'BankAccount':
        """Create account from JSON data.
        
        Args:
            json_data: JSON string containing account data
            
        Returns:
            New account instance
        """
        data = json.loads(json_data)
        return cls(data['owner'], data['balance'])
    
    @staticmethod
    def calculate_interest(principal: float, rate: float, time: float) -> float:
        """Calculate simple interest.
        
        Args:
            principal: Principal amount
            rate: Interest rate (as decimal)
            time: Time period in years
            
        Returns:
            Interest amount
        """
        return principal * rate * time
    
    def deposit(self, amount: float) -> None:
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._add_transaction(f"Deposited: ${amount:.2f}")
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            
        Raises:
            ValueError: If amount is invalid or insufficient funds
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if self._balance - amount < self.minimum_balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._add_transaction(f"Withdrew: ${amount:.2f}")
    
    def transfer(self, other_account: 'BankAccount', amount: float) -> None:
        """Transfer money to another account.
        
        Args:
            other_account: Destination account
            amount: Amount to transfer
        """
        self.withdraw(amount)
        other_account.deposit(amount)
        self._add_transaction(f"Transferred ${amount:.2f} to {other_account.account_number}")
        other_account._add_transaction(f"Received ${amount:.2f} from {self.account_number}")
    
    def _add_transaction(self, description: str) -> None:
        """Add a transaction to the history.
        
        Args:
            description: Transaction description
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transaction_history.append(f"[{timestamp}] {description}")
    
    def __str__(self) -> str:
        """Return string representation of the account."""
        return f"BankAccount({self.account_number}, Owner: {self.owner}, Balance: ${self.balance:.2f})"


# Abstract base class for shapes (inheritance example)
class Shape(ABC):
    """Abstract base class for geometric shapes."""
    
    def __init__(self, name: str) -> None:
        """Initialize shape with a name.
        
        Args:
            name: Name of the shape
        """
        self.name = name
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape.
        
        Returns:
            Area of the shape
        """
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape.
        
        Returns:
            Perimeter of the shape
        """
        pass
    
    def __str__(self) -> str:
        """Return string representation of the shape."""
        return f"{self.name} (Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f})"


class Rectangle(Shape):
    """Rectangle implementation of Shape."""
    
    def __init__(self, length: float, width: float) -> None:
        """Initialize rectangle.
        
        Args:
            length: Length of the rectangle
            width: Width of the rectangle
        """
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """Calculate rectangle area."""
        return self.length * self.width
    
    def perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return 2 * (self.length + self.width)


class Circle(Shape):
    """Circle implementation of Shape."""
    
    def __init__(self, radius: float) -> None:
        """Initialize circle.
        
        Args:
            radius: Radius of the circle
        """
        super().__init__("Circle")
        self.radius = radius
    
    def area(self) -> float:
        """Calculate circle area."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circle circumference."""
        import math
        return 2 * math.pi * self.radius


# Composition example: Car has-a Engine
class Engine:
    """Represents a car engine."""
    
    def __init__(self, horsepower: int, fuel_type: str) -> None:
        """Initialize engine.
        
        Args:
            horsepower: Engine horsepower
            fuel_type: Type of fuel (gas, diesel, electric)
        """
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self._is_running = False
    
    def start(self) -> None:
        """Start the engine."""
        self._is_running = True
    
    def stop(self) -> None:
        """Stop the engine."""
        self._is_running = False
    
    def is_running(self) -> bool:
        """Check if engine is running."""
        return self._is_running
    
    def __str__(self) -> str:
        """Return string representation of engine."""
        status = "Running" if self._is_running else "Stopped"
        return f"{self.horsepower}HP {self.fuel_type.title()} Engine ({status})"


class Car:
    """Represents a car using composition."""
    
    def __init__(self, make: str, model: str, year: int, engine: Engine) -> None:
        """Initialize car.
        
        Args:
            make: Car manufacturer
            model: Car model
            year: Manufacturing year
            engine: Car engine (composition)
        """
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine  # Composition: Car has-a Engine
        self._speed = 0
    
    def start(self) -> None:
        """Start the car."""
        self.engine.start()
    
    def stop(self) -> None:
        """Stop the car."""
        self.engine.stop()
        self._speed = 0
    
    def accelerate(self, speed_increase: int) -> None:
        """Accelerate the car.
        
        Args:
            speed_increase: Speed increase amount
        """
        if not self.engine.is_running():
            raise RuntimeError("Cannot accelerate: engine is not running")
        
        self._speed += speed_increase
    
    def get_speed(self) -> int:
        """Get current speed."""
        return self._speed
    
    def __str__(self) -> str:
        """Return string representation of car."""
        return f"{self.year} {self.make} {self.model} (Speed: {self._speed} mph, Engine: {self.engine})"

# What we accomplished in this step:
# - Demonstrated inheritance with abstract base classes
# - Showed composition with Car has-a Engine relationship
# - Illustrated proper use of super() in inheritance
# - Used abstract methods to enforce interface contracts


# Step 5: Complete example with demonstration and best practices summary
# ===============================================================================

# Explanation:
# This final step brings everything together with a comprehensive example
# that demonstrates all the best practices we've covered.

from typing import List, Optional, Dict, Any
from datetime import datetime
from abc import ABC, abstractmethod
import json

def calculate_area_of_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
        
    Returns:
        The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    
    return length * width


def format_user_name(first_name: str, last_name: str) -> str:
    """Format a user's full name.
    
    Args:
        first_name: The user's first name
        last_name: The user's last name
        
    Returns:
        Formatted full name
    """
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def validate_email_address(email: str) -> bool:
    """Validate an email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email format is valid, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


class User:
    """Represents a user in the system.
    
    This class demonstrates proper class structure with clear organization
    of attributes and methods.
    
    Attributes:
        username: The user's unique username
        email: The user's email address
        created_at: When the user was created
    """
    
    # Class variable (shared by all instances)
    total_users: int = 0
    
    def __init__(self, username: str, email: str) -> None:
        """Initialize a new user.
        
        Args:
            username: The user's unique username
            email: The user's email address
            
        Raises:
            ValueError: If username or email is invalid
        """
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)
        self.created_at = datetime.now()
        self._is_active = True
        
        # Update class variable
        User.total_users += 1
    
    def __str__(self) -> str:
        """Return string representation of the user."""
        return f"User(username='{self.username}', email='{self.email}')"
    
    def __repr__(self) -> str:
        """Return detailed string representation for debugging."""
        return (f"User(username='{self.username}', email='{self.email}', "
                f"created_at='{self.created_at}', active={self._is_active})")
    
    def get_display_name(self) -> str:
        """Get the user's display name.
        
        Returns:
            Formatted display name
        """
        return self.username.replace('_', ' ').title()
    
    def is_active(self) -> bool:
        """Check if the user is active.
        
        Returns:
            True if user is active, False otherwise
        """
        return self._is_active
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self._is_active = False
    
    def activate(self) -> None:
        """Activate the user account."""
        self._is_active = True
    
    def _validate_username(self, username: str) -> str:
        """Validate and clean username.
        
        Args:
            username: Username to validate
            
        Returns:
            Cleaned username
            
        Raises:
            ValueError: If username is invalid
        """
        if not username or len(username.strip()) < 3:
            raise ValueError("Username must be at least 3 characters long")
        
        cleaned = username.strip().lower()
        if not cleaned.replace('_', '').isalnum():
            raise ValueError("Username can only contain letters, numbers, and underscores")
        
        return cleaned
    
    def _validate_email(self, email: str) -> str:
        """Validate email address.
        
        Args:
            email: Email to validate
            
        Returns:
            Cleaned email
            
        Raises:
            ValueError: If email is invalid
        """
        if not validate_email_address(email):
            raise ValueError("Invalid email address format")
        
        return email.strip().lower()


class BankAccount:
    """Represents a bank account with proper encapsulation.
    
    This class demonstrates advanced features like properties, class methods,
    static methods, and proper data validation.
    """
    
    # Class variables
    _account_counter: int = 0
    minimum_balance: float = 0.0
    
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        """Initialize a new bank account.
        
        Args:
            owner: The account owner's name
            initial_balance: Initial account balance
            
        Raises:
            ValueError: If initial balance is negative
        """
        self._owner = owner
        self._balance = 0.0
        self.balance = initial_balance  # Use property setter for validation
        
        BankAccount._account_counter += 1
        self._account_number = f"ACC{BankAccount._account_counter:06d}"
        self._transaction_history: List[str] = []
        
        self._add_transaction(f"Account opened with balance: ${initial_balance:.2f}")
    
    @property
    def balance(self) -> float:
        """Get the current account balance."""
        return self._balance
    
    @balance.setter
    def balance(self, amount: float) -> None:
        """Set the account balance with validation.
        
        Args:
            amount: New balance amount
            
        Raises:
            ValueError: If amount is below minimum balance
        """
        if amount < self.minimum_balance:
            raise ValueError(f"Balance cannot be below ${self.minimum_balance:.2f}")
        self._balance = amount
    
    @property
    def owner(self) -> str:
        """Get the account owner's name."""
        return self._owner
    
    @property
    def account_number(self) -> str:
        """Get the account number."""
        return self._account_number
    
    @property
    def transaction_history(self) -> List[str]:
        """Get a copy of the transaction history."""
        return self._transaction_history.copy()
    
    @classmethod
    def create_savings_account(cls, owner: str, initial_balance: float = 100.0) -> 'BankAccount':
        """Create a savings account with higher minimum balance.
        
        Args:
            owner: The account owner's name
            initial_balance: Initial balance (default $100)
            
        Returns:
            New savings account instance
        """
        account = cls(owner, initial_balance)
        account.minimum_balance = 100.0
        account._add_transaction("Converted to savings account")
        return account
    
    @classmethod
    def from_json(cls, json_data: str) -> 'BankAccount':
        """Create account from JSON data.
        
        Args:
            json_data: JSON string containing account data
            
        Returns:
            New account instance
        """
        data = json.loads(json_data)
        return cls(data['owner'], data['balance'])
    
    @staticmethod
    def calculate_interest(principal: float, rate: float, time: float) -> float:
        """Calculate simple interest.
        
        Args:
            principal: Principal amount
            rate: Interest rate (as decimal)
            time: Time period in years
            
        Returns:
            Interest amount
        """
        return principal * rate * time
    
    def deposit(self, amount: float) -> None:
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._add_transaction(f"Deposited: ${amount:.2f}")
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            
        Raises:
            ValueError: If amount is invalid or insufficient funds
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if self._balance - amount < self.minimum_balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._add_transaction(f"Withdrew: ${amount:.2f}")
    
    def transfer(self, other_account: 'BankAccount', amount: float) -> None:
        """Transfer money to another account.
        
        Args:
            other_account: Destination account
            amount: Amount to transfer
        """
        self.withdraw(amount)
        other_account.deposit(amount)
        self._add_transaction(f"Transferred ${amount:.2f} to {other_account.account_number}")
        other_account._add_transaction(f"Received ${amount:.2f} from {self.account_number}")
    
    def _add_transaction(self, description: str) -> None:
        """Add a transaction to the history.
        
        Args:
            description: Transaction description
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transaction_history.append(f"[{timestamp}] {description}")
    
    def __str__(self) -> str:
        """Return string representation of the account."""
        return f"BankAccount({self.account_number}, Owner: {self.owner}, Balance: ${self.balance:.2f})"


# Abstract base class for shapes (inheritance example)
class Shape(ABC):
    """Abstract base class for geometric shapes."""
    
    def __init__(self, name: str) -> None:
        """Initialize shape with a name.
        
        Args:
            name: Name of the shape
        """
        self.name = name
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape.
        
        Returns:
            Area of the shape
        """
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape.
        
        Returns:
            Perimeter of the shape
        """
        pass
    
    def __str__(self) -> str:
        """Return string representation of the shape."""
        return f"{self.name} (Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f})"


class Rectangle(Shape):
    """Rectangle implementation of Shape."""
    
    def __init__(self, length: float, width: float) -> None:
        """Initialize rectangle.
        
        Args:
            length: Length of the rectangle
            width: Width of the rectangle
        """
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """Calculate rectangle area."""
        return self.length * self.width
    
    def perimeter(self) -> float:
        """Calculate rectangle perimeter."""
        return 2 * (self.length + self.width)


class Circle(Shape):
    """Circle implementation of Shape."""
    
    def __init__(self, radius: float) -> None:
        """Initialize circle.
        
        Args:
            radius: Radius of the circle
        """
        super().__init__("Circle")
        self.radius = radius
    
    def area(self) -> float:
        """Calculate circle area."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circle circumference."""
        import math
        return 2 * math.pi * self.radius


# Composition example: Car has-a Engine
class Engine:
    """Represents a car engine."""
    
    def __init__(self, horsepower: int, fuel_type: str) -> None:
        """Initialize engine.
        
        Args:
            horsepower: Engine horsepower
            fuel_type: Type of fuel (gas, diesel, electric)
        """
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self._is_running = False
    
    def start(self) -> None:
        """Start the engine."""
        self._is_running = True
    
    def stop(self) -> None:
        """Stop the engine."""
        self._is_running = False
    
    def is_running(self) -> bool:
        """Check if engine is running."""
        return self._is_running
    
    def __str__(self) -> str:
        """Return string representation of engine."""
        status = "Running" if self._is_running else "Stopped"
        return f"{self.horsepower}HP {self.fuel_type.title()} Engine ({status})"


class Car:
    """Represents a car using composition."""
    
    def __init__(self, make: str, model: str, year: int, engine: Engine) -> None:
        """Initialize car.
        
        Args:
            make: Car manufacturer
            model: Car model
            year: Manufacturing year
            engine: Car engine (composition)
        """
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine  # Composition: Car has-a Engine
        self._speed = 0
    
    def start(self) -> None:
        """Start the car."""
        self.engine.start()
    
    def stop(self) -> None:
        """Stop the car."""
        self.engine.stop()
        self._speed = 0
    
    def accelerate(self, speed_increase: int) -> None:
        """Accelerate the car.
        
        Args:
            speed_increase: Speed increase amount
        """
        if not self.engine.is_running():
            raise RuntimeError("Cannot accelerate: engine is not running")
        
        self._speed += speed_increase
    
    def get_speed(self) -> int:
        """Get current speed."""
        return self._speed
    
    def __str__(self) -> str:
        """Return string representation of car."""
        return f"{self.year} {self.make} {self.model} (Speed: {self._speed} mph, Engine: {self.engine})"


# Comprehensive example: UserManager with all best practices
class UserManager:
    """Manages users with proper structure and organization.
    
    This class demonstrates all the best practices we've covered:
    - Clear naming and documentation
    - Proper method organization
    - Type hints and error handling
    - Encapsulation and validation
    """
    
    def __init__(self) -> None:
        """Initialize the user manager."""
        self._users: Dict[str, User] = {}
        self._user_accounts: Dict[str, BankAccount] = {}
    
    def create_user(self, username: str, email: str) -> User:
        """Create a new user.
        
        Args:
            username: Unique username
            email: User's email address
            
        Returns:
            Created user instance
            
        Raises:
            ValueError: If user already exists or invalid data
        """
        if username.lower() in self._users:
            raise ValueError(f"User '{username}' already exists")
        
        user = User(username, email)
        self._users[user.username] = user
        return user
    
    def get_user(self, username: str) -> Optional[User]:
        """Get a user by username.
        
        Args:
            username: Username to search for
            
        Returns:
            User instance if found, None otherwise
        """
        return self._users.get(username.lower())
    
    def create_user_account(self, username: str, initial_balance: float = 0.0) -> BankAccount:
        """Create a bank account for a user.
        
        Args:
            username: Username of the account owner
            initial_balance: Initial account balance
            
        Returns:
            Created bank account
            
        Raises:
            ValueError: If user doesn't exist or already has an account
        """
        user = self.get_user(username)
        if not user:
            raise ValueError(f"User '{username}' not found")
        
        if username in self._user_accounts:
            raise ValueError(f"User '{username}' already has an account")
        
        account = BankAccount(user.get_display_name(), initial_balance)
        self._user_accounts[username] = account
        return account
    
    def get_user_account(self, username: str) -> Optional[BankAccount]:
        """Get a user's bank account.
        
        Args:
            username: Username to search for
            
        Returns:
            Bank account if found, None otherwise
        """
        return self._user_accounts.get(username.lower())
    
    def get_all_users(self) -> List[User]:
        """Get all users.
        
        Returns:
            List of all users
        """
        return list(self._users.values())
    
    def get_user_count(self) -> int:
        """Get total number of users.
        
        Returns:
            Number of users
        """
        return len(self._users)


def demonstrate_best_practices() -> None:
    """Demonstrate all the best practices in action."""
    print("=== Function and Class Structure Best Practices Demo ===\\n")
    
    # Test utility functions
    print("1. Testing utility functions:")
    area = calculate_area_of_rectangle(5.0, 3.0)
    print(f"   Rectangle area (5x3): {area}")
    
    name = format_user_name("  john  ", "  DOE  ")
    print(f"   Formatted name: {name}")
    
    is_valid = validate_email_address("john.doe@example.com")
    print(f"   Email validation: {is_valid}\\n")
    
    # Test User class
    print("2. Testing User class:")
    user1 = User("john_doe", "john@example.com")
    print(f"   Created user: {user1}")
    print(f"   Display name: {user1.get_display_name()}")
    print(f"   Total users: {User.total_users}\\n")
    
    # Test BankAccount class with properties
    print("3. Testing BankAccount class:")
    account = BankAccount("John Doe", 1000.0)
    print(f"   Created account: {account}")
    
    account.deposit(500.0)
    print(f"   After deposit: Balance = ${account.balance:.2f}")
    
    account.withdraw(200.0)
    print(f"   After withdrawal: Balance = ${account.balance:.2f}")
    
    # Test class methods
    savings = BankAccount.create_savings_account("Jane Smith", 500.0)
    print(f"   Savings account: {savings}\\n")
    
    # Test inheritance
    print("4. Testing inheritance:")
    rectangle = Rectangle(4.0, 6.0)
    circle = Circle(3.0)
    
    shapes: List[Shape] = [rectangle, circle]
    for shape in shapes:
        print(f"   {shape}")
    print()
    
    # Test composition
    print("5. Testing composition:")
    engine = Engine(300, "gas")
    car = Car("Toyota", "Camry", 2025, engine)
    
    print(f"   Created car: {car}")
    car.start()
    car.accelerate(30)
    print(f"   After starting and accelerating: {car}\\n")
    
    # Test comprehensive example
    print("6. Testing UserManager (comprehensive example):")
    manager = UserManager()
    
    # Create users
    user1 = manager.create_user("alice_smith", "alice@example.com")
    user2 = manager.create_user("bob_jones", "bob@example.com")
    
    # Create accounts
    account1 = manager.create_user_account("alice_smith", 1500.0)
    account2 = manager.create_user_account("bob_jones", 800.0)
    
    print(f"   Created {manager.get_user_count()} users")
    print(f"   Alice's account: {account1}")
    print(f"   Bob's account: {account2}")
    
    # Transfer money
    account1.transfer(account2, 300.0)
    print(f"   After transfer - Alice: ${account1.balance:.2f}, Bob: ${account2.balance:.2f}")


# What we accomplished in this final step:
# - Created a comprehensive UserManager class demonstrating all best practices
# - Added a complete demonstration function showing everything in action
# - Showed how all the concepts work together in a real-world scenario
# - Provided a practical example of well-structured, maintainable code


# ===============================================================================
#                           BEST PRACTICES SUMMARY
# ===============================================================================
#
# Key takeaways for function and class structure:
#
# 1. FUNCTION BEST PRACTICES:
#    - Use clear, descriptive names (snake_case)
#    - Keep functions small and focused (single responsibility)
#    - Use type hints for parameters and return values
#    - Write comprehensive docstrings
#    - Handle errors appropriately
#
# 2. CLASS STRUCTURE:
#    - Follow consistent method ordering:
#      * Class docstring
#      * Class variables
#      * __init__ method
#      * Special methods (__str__, __repr__, etc.)
#      * Public methods
#      * Private methods
#    - Use proper naming conventions
#    - Group related functionality together
#
# 3. ADVANCED FEATURES:
#    - Use properties for controlled attribute access
#    - Implement class methods for alternative constructors
#    - Use static methods for utility functions
#    - Apply inheritance for "is-a" relationships
#    - Use composition for "has-a" relationships
#
# 4. DOCUMENTATION AND TYPE HINTS:
#    - Write clear docstrings for all public methods
#    - Use type hints consistently
#    - Document parameters, return values, and exceptions
#    - Include usage examples when helpful
#
# 5. ENCAPSULATION:
#    - Use private attributes (leading underscore) for internal data
#    - Provide public interfaces for accessing private data
#    - Validate input data in setters and methods
#    - Maintain object invariants
#
# Remember: Good structure makes code easier to read, understand, maintain,
# and extend. These practices become even more important as projects grow!
#
# ===============================================================================


if __name__ == "__main__":
    demonstrate_best_practices()