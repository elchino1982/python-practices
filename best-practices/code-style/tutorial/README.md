# Python Code Style Best Practices - Comprehensive Tutorial

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started - Beginner Level](#getting-started---beginner-level)
3. [PEP 8 Fundamentals](#pep-8-fundamentals)
4. [Naming Conventions](#naming-conventions)
5. [Code Formatting](#code-formatting)
6. [Import Organization](#import-organization)
7. [Comments and Documentation](#comments-and-documentation)
8. [Line Length and Wrapping](#line-length-and-wrapping)
9. [Whitespace and Indentation](#whitespace-and-indentation)
10. [String Formatting](#string-formatting)
11. [Function and Class Structure](#function-and-class-structure)
12. [Type Hints - Intermediate Level](#type-hints---intermediate-level)
13. [Code Organization - Advanced Level](#code-organization---advanced-level)
14. [Tools and Automation](#tools-and-automation)
15. [Expert Tips and Best Practices](#expert-tips-and-best-practices)
16. [Common Mistakes and How to Avoid Them](#common-mistakes-and-how-to-avoid-them)
17. [Real-World Examples](#real-world-examples)
18. [Resources and Further Reading](#resources-and-further-reading)

---

## Introduction

Welcome to the comprehensive Python Code Style Best Practices tutorial! This guide is designed to take you from a complete beginner to an expert in Python code styling, following industry standards and best practices.

### Why Code Style Matters

Good code style is not just about making your code look pretty. It serves several critical purposes:

1. **Readability**: Clean, consistent code is easier to read and understand
2. **Maintainability**: Well-styled code is easier to modify and extend
3. **Collaboration**: Consistent style makes it easier for teams to work together
4. **Professionalism**: Good style demonstrates attention to detail and professionalism
5. **Debugging**: Clean code makes it easier to spot and fix bugs
6. **Performance**: Some style choices can impact code performance

### What You'll Learn

By the end of this tutorial, you'll be able to:

- Write Python code that follows PEP 8 standards
- Use proper naming conventions for all Python constructs
- Format your code for maximum readability
- Organize imports and modules effectively
- Write clear, helpful comments and documentation
- Use type hints to improve code quality
- Structure functions and classes professionally
- Apply advanced code organization principles
- Use tools to automate code style checking and formatting

### Prerequisites

- Basic Python knowledge (variables, functions, classes)
- A text editor or IDE
- Python 3.6+ installed on your system

---

## Getting Started - Beginner Level

### What is PEP 8?

PEP 8 is the official style guide for Python code. PEP stands for "Python Enhancement Proposal," and PEP 8 specifically addresses how Python code should be formatted and styled.

### Your First Style Rule: Indentation

Python uses indentation to define code blocks. Always use **4 spaces** for indentation, never tabs.

```python
# ❌ Bad - inconsistent indentation
def bad_function():
  if True:
      print("This is confusing")
    print("Inconsistent indentation")

# ✅ Good - consistent 4-space indentation
def good_function():
    if True:
        print("This is clear")
        print("Consistent indentation")
```

### Basic Naming Rules

1. **Variables and functions**: Use lowercase with underscores
2. **Classes**: Use CapitalizedWords (PascalCase)
3. **Constants**: Use UPPERCASE with underscores

```python
# ❌ Bad naming
MyVariable = "hello"
def MyFunction():
    pass
class myclass:
    pass

# ✅ Good naming
my_variable = "hello"
def my_function():
    pass
class MyClass:
    pass
MY_CONSTANT = 42
```

### Basic Line Length

Keep lines under 79 characters when possible. This makes code readable on various screen sizes.

```python
# ❌ Bad - too long
really_long_variable_name = some_function_with_long_name(parameter_one, parameter_two, parameter_three, parameter_four)

# ✅ Good - broken into multiple lines
really_long_variable_name = some_function_with_long_name(
    parameter_one, 
    parameter_two, 
    parameter_three, 
    parameter_four
)
```

---

## PEP 8 Fundamentals

### The Philosophy Behind PEP 8

PEP 8 is based on the principle that "code is read much more often than it is written." This means we should optimize for readability over brevity.

### Key Principles

1. **Consistency**: Be consistent within a project, module, or function
2. **Readability**: Code should be easy to read and understand
3. **Simplicity**: Prefer simple, clear solutions over complex ones
4. **Explicit**: Be explicit rather than implicit when possible

### When to Break PEP 8 Rules

Sometimes it's okay to break PEP 8 rules:

1. When following the rule would make code less readable
2. When maintaining consistency with existing code that doesn't follow PEP 8
3. When the code needs to be compatible with older Python versions
4. When working with external APIs that use different conventions

```python
# Sometimes breaking the line length rule makes sense
# if it improves readability
if (this_condition and that_condition and 
    another_very_long_condition_name):
    # This might be more readable than:
    # if (this_condition and 
    #     that_condition and 
    #     another_very_long_condition_name):
    pass
```

---

## Naming Conventions

### Variables and Functions

Use lowercase letters with underscores to separate words (snake_case).

```python
# ✅ Good variable names
user_name = "john_doe"
total_count = 42
is_valid = True
user_list = []

# ✅ Good function names
def calculate_total():
    pass

def get_user_data():
    pass

def is_email_valid(email):
    pass

# ❌ Bad examples
userName = "john_doe"  # camelCase not recommended
totalcount = 42        # hard to read
IsValid = True         # should be lowercase
userList = []          # camelCase not recommended

def calculateTotal():  # camelCase not recommended
    pass
```

### Classes

Use CapitalizedWords (PascalCase) for class names.

```python
# ✅ Good class names
class UserManager:
    pass

class DatabaseConnection:
    pass

class EmailValidator:
    pass

# ❌ Bad class names
class userManager:     # should be capitalized
    pass

class database_connection:  # should use PascalCase
    pass

class emailvalidator:  # hard to read
    pass
```

### Constants

Use uppercase letters with underscores for constants.

```python
# ✅ Good constants
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432
}

# ❌ Bad constants
maxConnections = 100   # should be uppercase
default_timeout = 30   # should be uppercase
apiBaseUrl = "https://api.example.com"  # should be uppercase
```

### Private and Protected Members

Use leading underscores to indicate privacy levels.

```python
class MyClass:
    def __init__(self):
        self.public_var = "everyone can access"
        self._protected_var = "subclasses can access"
        self.__private_var = "only this class can access"
    
    def public_method(self):
        """Anyone can call this method."""
        pass
    
    def _protected_method(self):
        """Subclasses should be able to call this."""
        pass
    
    def __private_method(self):
        """Only this class should call this."""
        pass
```

### Special Methods

Special methods (dunder methods) use double underscores.

```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass({self.value})"
    
    def __len__(self):
        return len(self.value)
    
    def __eq__(self, other):
        return self.value == other.value
```

### Module and Package Names

Use short, lowercase names for modules and packages.

```python
# ✅ Good module names
import json
import datetime
import user_manager
import email_utils

# ❌ Bad module names
import JSON           # should be lowercase
import DateTime       # should be lowercase
import UserManager    # should be lowercase
import emailUtils     # should use underscores
```

---

## Code Formatting

### Blank Lines

Use blank lines to separate logical sections of your code.

#### Top-level Functions and Classes

Surround top-level function and class definitions with two blank lines.

```python
import os
import sys


def first_function():
    """First function with proper spacing."""
    pass


def second_function():
    """Second function with proper spacing."""
    pass


class MyClass:
    """Class with proper spacing."""
    pass


class AnotherClass:
    """Another class with proper spacing."""
    pass
```

#### Method Definitions

Use a single blank line to separate method definitions inside a class.

```python
class MyClass:
    """Example class showing method spacing."""
    
    def __init__(self):
        """Constructor method."""
        self.value = 0
    
    def method_one(self):
        """First method."""
        return self.value
    
    def method_two(self):
        """Second method."""
        self.value += 1
    
    def method_three(self):
        """Third method."""
        return self.value * 2
```

#### Logical Sections

Use blank lines sparingly inside functions to separate logical sections.

```python
def process_user_data(users):
    """Process user data with logical sections."""
    # Input validation
    if not users:
        return []
    
    # Data processing
    processed_users = []
    for user in users:
        if user.is_active:
            processed_users.append(user)
    
    # Result formatting
    result = {
        'total': len(processed_users),
        'users': processed_users
    }
    
    return result
```

### Whitespace in Expressions

#### Operators

Use spaces around operators for better readability.

```python
# ✅ Good spacing around operators
x = 1 + 2
y = x * 3
z = (x + y) / 2
is_valid = x > 0 and y < 10

# ❌ Bad spacing
x=1+2
y=x*3
z=(x+y)/2
is_valid=x>0and y<10
```

#### Function Calls

Don't use spaces around the parentheses of function calls.

```python
# ✅ Good function call spacing
result = my_function(arg1, arg2, arg3)
data = process_data(input_data, format='json')

# ❌ Bad function call spacing
result = my_function( arg1, arg2, arg3 )
data = process_data (input_data, format = 'json')
```

#### Lists, Tuples, and Dictionaries

Use spaces after commas, but not before.

```python
# ✅ Good collection spacing
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3)
my_dict = {'key1': 'value1', 'key2': 'value2'}

# ❌ Bad collection spacing
my_list = [1,2,3,4]
my_tuple = (1 , 2 , 3)
my_dict = {'key1':'value1','key2':'value2'}
```

#### Slicing

Don't use spaces around the colon in slicing.

```python
# ✅ Good slicing
my_list[1:3]
my_string[::2]
my_array[start:end]

# ❌ Bad slicing
my_list[1 : 3]
my_string[: : 2]
my_array[start : end]
```

### Trailing Commas

Use trailing commas in multi-line collections for easier version control.

```python
# ✅ Good - trailing comma makes diffs cleaner
COLORS = [
    'red',
    'green',
    'blue',
    'yellow',  # Easy to add more colors
]

CONFIG = {
    'database_url': 'localhost:5432',
    'timeout': 30,
    'retries': 3,  # Easy to add more config
}

# ❌ Acceptable but less maintainable
COLORS = [
    'red',
    'green',
    'blue',
    'yellow'
]
```

---

## Import Organization

### Import Order

Organize imports in the following order, with blank lines between each group:

1. Standard library imports
2. Related third-party imports
3. Local application/library imports

```python
# ✅ Good import organization

# Standard library imports
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Third-party imports
import requests
import pandas as pd
from flask import Flask, request

# Local application imports
from myapp.models import User
from myapp.utils import validate_email
from . import config
```

### Absolute vs Relative Imports

Prefer absolute imports over relative imports for clarity.

```python
# ✅ Good - absolute imports (preferred)
from mypackage.subpackage import module
from mypackage.utils import helper_function

# ✅ Acceptable - relative imports (use sparingly)
from .subpackage import module
from ..utils import helper_function

# ❌ Bad - avoid wildcard imports
from mypackage import *
```

### Import Formatting

#### Multiple Imports from Same Module

```python
# ✅ Good - multiple imports on one line (if short)
from datetime import date, datetime, timedelta

# ✅ Good - multiple imports on separate lines (if long)
from mymodule import (
    very_long_function_name,
    another_long_function_name,
    yet_another_function_name,
)

# ❌ Bad - too many imports on one line
from mymodule import func1, func2, func3, func4, func5, func6, func7
```

#### Aliasing Imports

Use aliases for commonly used modules or to avoid naming conflicts.

```python
# ✅ Good aliasing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

# ✅ Good for avoiding conflicts
from mypackage import config as my_config
from thirdparty import config as third_config
```

#### Conditional Imports

Place conditional imports inside functions when possible.

```python
# ✅ Good - conditional import inside function
def process_data_with_pandas():
    """Process data using pandas if available."""
    try:
        import pandas as pd
        return pd.DataFrame(data)
    except ImportError:
        return process_data_without_pandas()

# ❌ Less preferred - conditional import at module level
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
```

---

## Comments and Documentation

### When to Write Comments

Write comments to explain **why**, not **what**. The code should be self-explanatory for the "what."

```python
# ❌ Bad - explains what the code does (obvious)
x = x + 1  # Increment x by 1

# ✅ Good - explains why
x = x + 1  # Compensate for border width in calculation

# ❌ Bad - obvious comment
if user.is_active:  # Check if user is active
    send_email(user)

# ✅ Good - explains business logic
if user.is_active:  # Only send promotional emails to active users
    send_email(user)
```

### Inline Comments

Use inline comments sparingly and ensure they're separated by at least two spaces.

```python
# ✅ Good inline comments
x = x + 1    # Compensate for border
y = y * 2    # Double the height for retina displays

# ❌ Bad inline comments
x = x + 1# No space before comment
y = y * 2 # Only one space
```

### Block Comments

Use block comments to explain complex algorithms or business logic.

```python
# ✅ Good block comment
# The following algorithm implements a binary search
# to find the optimal price point. We use binary search
# because the profit function is unimodal in this range.
def find_optimal_price(min_price, max_price, profit_function):
    left, right = min_price, max_price
    while right - left > 0.01:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        
        if profit_function(mid1) < profit_function(mid2):
            left = mid1
        else:
            right = mid2
    
    return (left + right) / 2
```

### Docstrings

Use docstrings to document modules, classes, and functions.

#### Function Docstrings

```python
def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    """Calculate compound interest.
    
    Args:
        principal (float): The initial amount of money.
        rate (float): Annual interest rate as a decimal (e.g., 0.05 for 5%).
        time (float): Time period in years.
        compound_frequency (int, optional): Number of times interest is 
            compounded per year. Defaults to 1.
    
    Returns:
        float: The final amount after compound interest.
    
    Raises:
        ValueError: If any of the numeric arguments are negative.
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 2)
        1102.5
    """
    if principal < 0 or rate < 0 or time < 0 or compound_frequency < 0:
        raise ValueError("All arguments must be non-negative")
    
    return principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
```

#### Class Docstrings

```python
class BankAccount:
    """A simple bank account class.
    
    This class represents a bank account with basic operations
    like deposit, withdrawal, and balance inquiry.
    
    Attributes:
        account_number (str): Unique identifier for the account.
        balance (float): Current account balance.
        owner (str): Name of the account owner.
    
    Example:
        >>> account = BankAccount("12345", "John Doe", 1000.0)
        >>> account.deposit(500.0)
        >>> print(account.balance)
        1500.0
    """
    
    def __init__(self, account_number, owner, initial_balance=0.0):
        """Initialize a new bank account.
        
        Args:
            account_number (str): Unique identifier for the account.
            owner (str): Name of the account owner.
            initial_balance (float, optional): Starting balance. Defaults to 0.0.
        """
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
```

#### Module Docstrings

```python
"""User management utilities.

This module provides utilities for managing user accounts,
including creation, authentication, and profile management.

Example:
    Basic usage of the user management system:
    
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com", "John Doe")
"""

import hashlib
from typing import Dict, List, Optional
```

---

## Line Length and Wrapping

### Maximum Line Length

Keep lines under 79 characters for code and 72 characters for comments and docstrings.

```python
# ❌ Bad - line too long
def very_long_function_name_that_exceeds_line_limit(parameter_one, parameter_two, parameter_three):
    return parameter_one + parameter_two + parameter_three

# ✅ Good - properly wrapped
def very_long_function_name_that_exceeds_line_limit(
    parameter_one, 
    parameter_two, 
    parameter_three
):
    return parameter_one + parameter_two + parameter_three
```

### Breaking Long Lines

#### Function Definitions

```python
# ✅ Good ways to break function definitions

# Method 1: Hanging indent
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Method 2: Aligned with opening delimiter
def long_function_name(var_one, var_two,
                       var_three, var_four):
    print(var_one)

# Method 3: Extra indentation to distinguish arguments
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

#### Function Calls

```python
# ✅ Good ways to break function calls

# Method 1: Each argument on its own line
result = some_function_with_a_long_name(
    argument_one,
    argument_two,
    argument_three,
    argument_four
)

# Method 2: Grouped arguments
result = some_function_with_a_long_name(
    argument_one, argument_two,
    argument_three, argument_four
)

# Method 3: Aligned with opening parenthesis
result = some_function_with_a_long_name(argument_one,
                                        argument_two,
                                        argument_three)
```

#### Lists and Dictionaries

```python
# ✅ Good ways to break collections

# Lists
my_list = [
    'item_one', 'item_two', 'item_three',
    'item_four', 'item_five', 'item_six'
]

# Dictionaries
my_dict = {
    'key_one': 'value_one',
    'key_two': 'value_two',
    'key_three': 'value_three',
}

# Complex nested structures
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'myapp'
    },
    'cache': {
        'backend': 'redis',
        'timeout': 300
    }
}
```

#### Conditional Statements

```python
# ✅ Good ways to break long conditionals

# Method 1: Parentheses for grouping
if (condition_one and condition_two and 
    condition_three and condition_four):
    do_something()

# Method 2: Each condition on its own line
if (condition_one and 
    condition_two and 
    condition_three and 
    condition_four):
    do_something()

# Method 3: Extra indentation
if (condition_one and condition_two and
        condition_three and condition_four):
    do_something()
```

#### String Concatenation

```python
# ✅ Good ways to handle long strings

# Method 1: Implicit string concatenation
message = ("This is a very long message that needs to be "
           "split across multiple lines for readability.")

# Method 2: Using parentheses
message = (
    "This is a very long message that needs to be "
    "split across multiple lines for readability."
)

# Method 3: Using format strings
message = (
    f"Hello {user_name}, this is a long message "
    f"with variables that spans multiple lines."
)

# ❌ Bad - using backslash continuation
message = "This is a very long message that needs to be " \
          "split across multiple lines for readability."
```

---

## Whitespace and Indentation

### Indentation Rules

Always use 4 spaces per indentation level. Never mix tabs and spaces.

```python
# ✅ Good indentation
def my_function():
    if True:
        for i in range(10):
            if i % 2 == 0:
                print(f"Even number: {i}")
            else:
                print(f"Odd number: {i}")

# ❌ Bad - inconsistent indentation
def my_function():
  if True:
      for i in range(10):
        if i % 2 == 0:
            print(f"Even number: {i}")
          else:
              print(f"Odd number: {i}")
```

### Continuation Lines

Use hanging indents for continuation lines.

```python
# ✅ Good continuation line indentation
result = some_function(
    argument_one,
    argument_two,
    argument_three
)

# ✅ Good - aligned with opening delimiter
result = some_function(argument_one,
                       argument_two,
                       argument_three)

# ❌ Bad - arguments not distinguished from next line
def long_function_name(
    var_one, var_two, var_three,
    var_four):
print("This line is confusing")
```

### Whitespace Around Operators

#### Binary Operators

```python
# ✅ Good spacing
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# ❌ Bad spacing
i=i+1
submitted +=1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

#### Assignment Operators

```python
# ✅ Good - aligned assignments for readability
x = 1
y = 2
long_variable = 3

# ❌ Bad - don't align with extra spaces
x             = 1
y             = 2
long_variable = 3
```

#### Function Annotations

```python
# ✅ Good spacing in annotations
def munge(input: str) -> str:
    return input.upper()

def munge(sep: str = ' ') -> str:
    return sep.join(['hello', 'world'])

# ❌ Bad spacing in annotations
def munge(input:str)->str:
    return input.upper()

def munge(sep:str=' ')->str:
    return sep.join(['hello', 'world'])
```

---

## String Formatting

### Modern String Formatting

Use f-strings (Python 3.6+) for most string formatting needs.

```python
# ✅ Good - f-strings (preferred)
name = "Alice"
age = 30
message = f"Hello, {name}! You are {age} years old."

# ✅ Good - format method (when f-strings aren't suitable)
template = "Hello, {}! You are {} years old."
message = template.format(name, age)

# ✅ Good - named placeholders
template = "Hello, {name}! You are {age} years old."
message = template.format(name=name, age=age)

# ❌ Bad - old % formatting (avoid)
message = "Hello, %s! You are %d years old." % (name, age)
```

### Complex String Formatting

```python
# ✅ Good - complex f-string formatting
price = 19.99
tax_rate = 0.08
total = price * (1 + tax_rate)

message = f"Price: ${price:.2f}, Tax: {tax_rate:.1%}, Total: ${total:.2f}"

# ✅ Good - multiline f-strings
user = {"name": "John", "email": "john@example.com", "age": 25}
message = (
    f"User: {user['name']}\n"
    f"Email: {user['email']}\n"
    f"Age: {user['age']}"
)

# ✅ Good - expressions in f-strings
numbers = [1, 2, 3, 4, 5]
result = f"Sum: {sum(numbers)}, Average: {sum(numbers) / len(numbers):.2f}"
```

### String Formatting Best Practices

```python
# ✅ Good - readable formatting for complex expressions
def format_user_info(user):
    """Format user information for display."""
    full_name = f"{user.first_name} {user.last_name}"
    account_age = (datetime.now() - user.created_at).days
    
    return (
        f"Name: {full_name}\n"
        f"Email: {user.email}\n"
        f"Account Age: {account_age} days\n"
        f"Status: {'Active' if user.is_active else 'Inactive'}"
    )

# ✅ Good - using format for templates
EMAIL_TEMPLATE = """
Dear {customer_name},

Thank you for your order #{order_id}.
Your total is ${total:.2f}.

Best regards,
The Team
"""

def send_order_confirmation(customer, order):
    """Send order confirmation email."""
    message = EMAIL_TEMPLATE.format(
        customer_name=customer.name,
        order_id=order.id,
        total=order.total
    )
    send_email(customer.email, "Order Confirmation", message)
```

---

## Function and Class Structure

### Function Organization

Structure functions with a clear, consistent pattern.

```python
def process_user_data(users: List[User], filters: Dict[str, Any]) -> List[User]:
    """Process user data with given filters.
    
    Args:
        users: List of user objects to process.
        filters: Dictionary of filter criteria.
    
    Returns:
        List of filtered and processed users.
    
    Raises:
        ValueError: If filters contain invalid criteria.
    """
    # Input validation
    if not users:
        return []
    
    if not isinstance(filters, dict):
        raise ValueError("Filters must be a dictionary")
    
    # Main processing logic
    filtered_users = []
    for user in users:
        if _meets_criteria(user, filters):
            processed_user = _process_single_user(user)
            filtered_users.append(processed_user)
    
    # Post-processing
    filtered_users.sort(key=lambda u: u.last_name)
    
    return filtered_users


def _meets_criteria(user: User, filters: Dict[str, Any]) -> bool:
    """Check if user meets filter criteria (private helper)."""
    for key, value in filters.items():
        if not hasattr(user, key):
            continue
        if getattr(user, key) != value:
            return False
    return True


def _process_single_user(user: User) -> User:
    """Process a single user (private helper)."""
    # Processing logic here
    return user
```

### Class Organization

Organize class members in a consistent order:

1. Class variables
2. `__init__` method
3. Properties
4. Public methods
5. Private methods
6. Special methods (`__str__`, `__repr__`, etc.)

```python
class UserManager:
    """Manages user accounts and operations.
    
    This class provides a comprehensive interface for user management
    including creation, authentication, and profile updates.
    """
    
    # Class variables
    DEFAULT_ROLE = "user"
    MAX_LOGIN_ATTEMPTS = 3
    
    def __init__(self, database_url: str):
        """Initialize the user manager.
        
        Args:
            database_url: Connection string for the database.
        """
        self._database_url = database_url
        self._users: Dict[str, User] = {}
        self._login_attempts: Dict[str, int] = {}
    
    # Properties
    @property
    def user_count(self) -> int:
        """Get the total number of users."""
        return len(self._users)
    
    @property
    def active_users(self) -> List[User]:
        """Get list of active users."""
        return [user for user in self._users.values() if user.is_active]
    
    # Public methods
    def create_user(self, email: str, password: str, **kwargs) -> User:
        """Create a new user account.
        
        Args:
            email: User's email address.
            password: User's password.
            **kwargs: Additional user attributes.
        
        Returns:
            The created user object.
        
        Raises:
            ValueError: If email is already in use.
        """
        if email in self._users:
            raise ValueError(f"User with email {email} already exists")
        
        user = User(
            email=email,
            password=self._hash_password(password),
            role=kwargs.get('role', self.DEFAULT_ROLE),
            **kwargs
        )
        
        self._users[email] = user
        return user
    
    def authenticate(self, email: str, password: str) -> Optional[User]:
        """Authenticate a user.
        
        Args:
            email: User's email address.
            password: User's password.
        
        Returns:
            User object if authentication successful, None otherwise.
        """
        if email not in self._users:
            return None
        
        if self._is_locked_out(email):
            return None
        
        user = self._users[email]
        if self._verify_password(password, user.password):
            self._reset_login_attempts(email)
            return user
        else:
            self._increment_login_attempts(email)
            return None
    
    # Private methods
    def _hash_password(self, password: str) -> str:
        """Hash a password for secure storage."""
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _verify_password(self, password: str, hashed: str) -> bool:
        """Verify a password against its hash."""
        return self._hash_password(password) == hashed
    
    def _is_locked_out(self, email: str) -> bool:
        """Check if user is locked out due to failed attempts."""
        return self._login_attempts.get(email, 0) >= self.MAX_LOGIN_ATTEMPTS
    
    def _increment_login_attempts(self, email: str) -> None:
        """Increment failed login attempts for user."""
        self._login_attempts[email] = self._login_attempts.get(email, 0) + 1
    
    def _reset_login_attempts(self, email: str) -> None:
        """Reset failed login attempts for user."""
        self._login_attempts.pop(email, None)
    
    # Special methods
    def __len__(self) -> int:
        """Return the number of users."""
        return len(self._users)
    
    def __contains__(self, email: str) -> bool:
        """Check if a user with given email exists."""
        return email in self._users
    
    def __str__(self) -> str:
        """Return string representation of UserManager."""
        return f"UserManager(users={len(self._users)})"
    
    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"UserManager(database_url='{self._database_url}', users={len(self._users)})"
```

### Method Naming and Structure

```python
class DataProcessor:
    """Example of good method naming and structure."""
    
    def process_data(self, data: List[Dict]) -> List[Dict]:
        """Main public method - verb that describes action."""
        validated_data = self.validate_data(data)
        transformed_data = self.transform_data(validated_data)
        return self.finalize_data(transformed_data)
    
    def validate_data(self, data: List[Dict]) -> List[Dict]:
        """Public method - clear, descriptive name."""
        return [item for item in data if self._is_valid_item(item)]
    
    def transform_data(self, data: List[Dict]) -> List[Dict]:
        """Public method - describes what it does."""
        return [self._transform_item(item) for item in data]
    
    def finalize_data(self, data: List[Dict]) -> List[Dict]:
        """Public method - clear purpose."""
        return sorted(data, key=lambda x: x.get('priority', 0))
    
    def _is_valid_item(self, item: Dict) -> bool:
        """Private helper - starts with underscore."""
        required_fields = ['id', 'name', 'type']
        return all(field in item for field in required_fields)
    
    def _transform_item(self, item: Dict) -> Dict:
        """Private helper - specific, focused purpose."""
        transformed = item.copy()
        transformed['processed_at'] = datetime.now().isoformat()
        transformed['name'] = transformed['name'].strip().title()
        return transformed
```

---

## Type Hints - Intermediate Level

### Basic Type Hints

Use type hints to improve code clarity and enable better IDE support.

```python
from typing import Dict, List, Optional, Union, Tuple, Any

# ✅ Good - basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

def get_user_data(user_id: int) -> Optional[Dict[str, Any]]:
    # Returns user data or None if not found
    pass

# ✅ Good - variable type hints
user_count: int = 0
user_names: List[str] = []
user_data: Dict[str, Union[str, int]] = {}
```

### Advanced Type Hints

```python
from typing import (
    Dict, List, Optional, Union, Tuple, Any, Callable, 
    TypeVar, Generic, Protocol
)

# Generic types
T = TypeVar('T')

def first_item(items: List[T]) -> Optional[T]:
    """Get the first item from a list."""
    return items[0] if items else None

# Callable types
def apply_function(func: Callable[[int], str], value: int) -> str:
    """Apply a function to a value."""
    return func(value)

# Protocol for structural typing
class Drawable(Protocol):
    """Protocol for objects that can be drawn."""
    
    def draw(self) -> None:
        """Draw the object."""
        ...

def render_objects(objects: List[Drawable]) -> None:
    """Render a list of drawable objects."""
    for obj in objects:
        obj.draw()

# Generic classes
class Container(Generic[T]):
    """A generic container class."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        """Add an item to the container."""
        self._items.append(item)
    
    def get_all(self) -> List[T]:
        """Get all items from the container."""
        return self._items.copy()
```

### Type Hints Best Practices

```python
from typing import Dict, List, Optional, Union
from dataclasses import dataclass

# ✅ Good - comprehensive type hints
@dataclass
class User:
    """User data class with proper type hints."""
    id: int
    name: str
    email: str
    age: Optional[int] = None
    is_active: bool = True
    metadata: Dict[str, str] = None
    
    def __post_init__(self) -> None:
        if self.metadata is None:
            self.metadata = {}

class UserService:
    """User service with comprehensive type hints."""
    
    def __init__(self, database_url: str) -> None:
        self._users: Dict[int, User] = {}
        self._database_url = database_url
    
    def create_user(
        self, 
        name: str, 
        email: str, 
        age: Optional[int] = None
    ) -> User:
        """Create a new user with proper type hints."""
        user_id = len(self._users) + 1
        user = User(id=user_id, name=name, email=email, age=age)
        self._users[user_id] = user
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID, return None if not found."""
        return self._users.get(user_id)
    
    def list_users(
        self, 
        active_only: bool = False
    ) -> List[User]:
        """List users with optional filtering."""
        users = list(self._users.values())
        if active_only:
            users = [user for user in users if user.is_active]
        return users
    
    def update_user(
        self, 
        user_id: int, 
        **updates: Union[str, int, bool]
    ) -> Optional[User]:
        """Update user with flexible field updates."""
        user = self.get_user(user_id)
        if user is None:
            return None
        
        for field, value in updates.items():
            if hasattr(user, field):
                setattr(user, field, value)
        
        return user
```

---

## Code Organization - Advanced Level

### Module Structure

Organize your modules with a clear, consistent structure:

```python
"""
user_management.py - User management module

This module provides comprehensive user management functionality
including user creation, authentication, and profile management.
"""

# Standard library imports
import hashlib
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

# Third-party imports
import bcrypt
from sqlalchemy import create_engine

# Local imports
from .models import User, UserProfile
from .exceptions import UserError, ValidationError
from .config import DATABASE_URL, SECRET_KEY

# Module constants
DEFAULT_USER_ROLE = "user"
MAX_LOGIN_ATTEMPTS = 3
PASSWORD_MIN_LENGTH = 8

# Module-level logger
logger = logging.getLogger(__name__)

# Exception classes
class UserManagementError(Exception):
    """Base exception for user management operations."""
    pass

# Utility functions
def validate_email(email: str) -> bool:
    """Validate email format."""
    # Implementation here
    pass

# Main classes
class UserManager:
    """Main user management class."""
    # Implementation here
    pass

# Module initialization
def setup_logging():
    """Setup module logging."""
    # Implementation here
    pass

# Call setup when module is imported
setup_logging()
```

### Package Structure

Organize larger projects into packages:

```
myproject/
├── __init__.py
├── config.py
├── exceptions.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── base.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   └── auth_service.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   └── helpers.py
└── tests/
    ├── __init__.py
    ├── test_user_service.py
    └── test_auth_service.py
```

### Configuration Management

```python
# config.py
"""Application configuration management."""

import os
from typing import Dict, Any

class Config:
    """Base configuration class."""
    
    # Database settings
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    DATABASE_POOL_SIZE = int(os.getenv('DATABASE_POOL_SIZE', '5'))
    
    # Security settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    PASSWORD_MIN_LENGTH = int(os.getenv('PASSWORD_MIN_LENGTH', '8'))
    
    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @classmethod
    def get_database_config(cls) -> Dict[str, Any]:
        """Get database configuration."""
        return {
            'url': cls.DATABASE_URL,
            'pool_size': cls.DATABASE_POOL_SIZE,
            'echo': cls.DEBUG
        }

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    LOG_LEVEL = 'WARNING'

# Configuration factory
def get_config() -> Config:
    """Get configuration based on environment."""
    env = os.getenv('ENVIRONMENT', 'development')
    
    if env == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()
```

---

## Tools and Automation

### Code Formatting Tools

#### Black - The Uncompromising Code Formatter

```bash
# Install black
pip install black

# Format a file
black my_script.py

# Format entire project
black .

# Check what would be formatted (dry run)
black --check .

# Configuration in pyproject.toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.tox
  | build
  | dist
)/
'''
```

#### isort - Import Sorting

```bash
# Install isort
pip install isort

# Sort imports in a file
isort my_script.py

# Sort imports in entire project
isort .

# Configuration in pyproject.toml
[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["myproject"]
known_third_party = ["requests", "pandas"]
```

### Code Quality Tools

#### flake8 - Style Guide Enforcement

```bash
# Install flake8
pip install flake8

# Check a file
flake8 my_script.py

# Check entire project
flake8 .

# Configuration in .flake8 or setup.cfg
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,build,dist
```

#### pylint - Comprehensive Code Analysis

```bash
# Install pylint
pip install pylint

# Analyze a file
pylint my_script.py

# Generate configuration file
pylint --generate-rcfile > .pylintrc
```

#### mypy - Static Type Checking

```bash
# Install mypy
pip install mypy

# Type check a file
mypy my_script.py

# Configuration in mypy.ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3.8

  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.950
    hooks:
      - id: mypy
```

### IDE Configuration

#### VS Code Settings

```json
{
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.sortImports.args": ["--profile", "black"],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

---

## Expert Tips and Best Practices

### Performance Considerations

```python
# ✅ Good - efficient string operations
def build_query(conditions: List[str]) -> str:
    """Build SQL query efficiently."""
    return " AND ".join(conditions)  # Efficient for small lists

def build_large_string(items: List[str]) -> str:
    """Build large strings efficiently."""
    return "".join(items)  # More efficient than repeated concatenation

# ❌ Bad - inefficient string concatenation
def build_query_bad(conditions: List[str]) -> str:
    query = ""
    for condition in conditions:
        query += condition + " AND "  # Creates new string each time
    return query.rstrip(" AND ")
```

### Memory Management

```python
# ✅ Good - memory-efficient iteration
def process_large_file(filename: str):
    """Process large file line by line."""
    with open(filename, 'r') as file:
        for line in file:  # Reads one line at a time
            process_line(line)

# ✅ Good - using generators for memory efficiency
def get_even_numbers(max_num: int):
    """Generate even numbers efficiently."""
    for i in range(0, max_num, 2):
        yield i  # Yields one number at a time

# ❌ Bad - loads entire file into memory
def process_large_file_bad(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Loads entire file
        for line in lines:
            process_line(line)
```

### Error Handling Patterns

```python
# ✅ Good - specific exception handling
def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        logger.warning(f"Division by zero attempted: {a} / {b}")
        return None
    except TypeError as e:
        logger.error(f"Type error in division: {e}")
        raise ValueError(f"Invalid types for division: {type(a)}, {type(b)}")

# ✅ Good - context manager for resource management
class DatabaseConnection:
    """Database connection with proper resource management."""
    
    def __enter__(self):
        self.connection = create_connection()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        return False  # Don't suppress exceptions

# Usage
with DatabaseConnection() as conn:
    # Connection is automatically closed
    result = conn.execute("SELECT * FROM users")
```

### Advanced Code Organization

```python
# ✅ Good - using protocols for flexible interfaces
from typing import Protocol

class Serializable(Protocol):
    """Protocol for objects that can be serialized."""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert object to dictionary."""
        ...
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Serializable':
        """Create object from dictionary."""
        ...

def save_object(obj: Serializable, filename: str) -> None:
    """Save any serializable object to file."""
    import json
    with open(filename, 'w') as f:
        json.dump(obj.to_dict(), f)

# ✅ Good - using dataclasses for data containers
from dataclasses import dataclass, field
from typing import List

@dataclass
class UserStats:
    """User statistics with automatic methods."""
    user_id: int
    login_count: int = 0
    last_login: Optional[datetime] = None
    permissions: List[str] = field(default_factory=list)
    
    def add_permission(self, permission: str) -> None:
        """Add permission if not already present."""
        if permission not in self.permissions:
            self.permissions.append(permission)
```

---

## Common Mistakes and How to Avoid Them

### Naming Mistakes

```python
# ❌ Bad - unclear, abbreviated names
def calc(x, y):
    return x * y * 0.1

# ✅ Good - clear, descriptive names
def calculate_tax(price: float, tax_rate: float) -> float:
    """Calculate tax amount for given price and rate."""
    return price * tax_rate

# ❌ Bad - misleading names
def get_users():
    """Actually creates and returns new users."""
    return [User() for _ in range(10)]

# ✅ Good - accurate names
def create_sample_users() -> List[User]:
    """Create and return sample user objects."""
    return [User() for _ in range(10)]
```

### Structure Mistakes

```python
# ❌ Bad - god class with too many responsibilities
class UserManager:
    def create_user(self): pass
    def authenticate_user(self): pass
    def send_email(self): pass
    def generate_report(self): pass
    def backup_database(self): pass
    def process_payments(self): pass

# ✅ Good - single responsibility classes
class UserManager:
    """Handles user creation and management."""
    def create_user(self): pass
    def update_user(self): pass

class AuthenticationService:
    """Handles user authentication."""
    def authenticate_user(self): pass
    def logout_user(self): pass

class EmailService:
    """Handles email operations."""
    def send_email(self): pass
    def send_bulk_email(self): pass
```

### Performance Mistakes

```python
# ❌ Bad - inefficient loops
def find_user_by_email(users: List[User], email: str) -> Optional[User]:
    for user in users:
        if user.email == email:
            return user
    return None

# Multiple calls = O(n) each time
user1 = find_user_by_email(users, "user1@example.com")
user2 = find_user_by_email(users, "user2@example.com")

# ✅ Good - use appropriate data structures
class UserManager:
    def __init__(self):
        self._users_by_email: Dict[str, User] = {}
    
    def add_user(self, user: User) -> None:
        self._users_by_email[user.email] = user
    
    def find_user_by_email(self, email: str) -> Optional[User]:
        return self._users_by_email.get(email)  # O(1) lookup
```

---

## Real-World Examples

### Complete Module Example

```python
"""
email_service.py - Professional email service implementation

This module demonstrates all the code style best practices covered
in this tutorial in a real-world context.
"""

import logging
import smtplib
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, List, Optional, Protocol
from datetime import datetime

# Module constants
DEFAULT_SMTP_PORT = 587
MAX_RETRY_ATTEMPTS = 3
EMAIL_TIMEOUT = 30

# Configure logging
logger = logging.getLogger(__name__)


# Custom exceptions
class EmailServiceError(Exception):
    """Base exception for email service operations."""
    pass


class EmailValidationError(EmailServiceError):
    """Raised when email validation fails."""
    pass


class EmailDeliveryError(EmailServiceError):
    """Raised when email delivery fails."""
    pass


# Data classes
@dataclass
class EmailConfig:
    """Email server configuration."""
    smtp_server: str
    smtp_port: int = DEFAULT_SMTP_PORT
    username: str = ""
    password: str = ""
    use_tls: bool = True
    timeout: int = EMAIL_TIMEOUT


@dataclass
class EmailMessage:
    """Email message data."""
    to_addresses: List[str]
    subject: str
    body: str
    from_address: str = ""
    cc_addresses: List[str] = None
    bcc_addresses: List[str] = None
    is_html: bool = False
    
    def __post_init__(self):
        """Initialize optional fields."""
        if self.cc_addresses is None:
            self.cc_addresses = []
        if self.bcc_addresses is None:
            self.bcc_addresses = []


# Protocols
class EmailProvider(Protocol):
    """Protocol for email providers."""
    
    def send_email(self, message: EmailMessage) -> bool:
        """Send an email message."""
        ...


# Utility functions
def validate_email_address(email: str) -> bool:
    """Validate email address format.
    
    Args:
        email: Email address to validate.
        
    Returns:
        True if email is valid, False otherwise.
        
    Raises:
        EmailValidationError: If email format is invalid.
    """
    import re
    
    if not email or not isinstance(email, str):
        raise EmailValidationError("Email must be a non-empty string")
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        raise EmailValidationError(f"Invalid email format: {email}")
    
    return True


def sanitize_email_content(content: str) -> str:
    """Sanitize email content for security.
    
    Args:
        content: Raw email content.
        
    Returns:
        Sanitized email content.
    """
    # Remove potentially dangerous content
    import html
    return html.escape(content)


# Main service class
class EmailService:
    """Professional email service with comprehensive functionality.
    
    This class demonstrates proper code organization, error handling,
    logging, and documentation practices.
    """
    
    def __init__(self, config: EmailConfig):
        """Initialize email service.
        
        Args:
            config: Email server configuration.
        """
        self._config = config
        self._sent_count = 0
        self._failed_count = 0
        
        logger.info(f"EmailService initialized with server: {config.smtp_server}")
    
    # Properties
    @property
    def sent_count(self) -> int:
        """Get number of successfully sent emails."""
        return self._sent_count
    
    @property
    def failed_count(self) -> int:
        """Get number of failed email attempts."""
        return self._failed_count
    
    @property
    def success_rate(self) -> float:
        """Get email delivery success rate."""
        total = self._sent_count + self._failed_count
        return self._sent_count / total if total > 0 else 0.0
    
    # Public methods
    def send_email(self, message: EmailMessage) -> bool:
        """Send a single email message.
        
        Args:
            message: Email message to send.
            
        Returns:
            True if email was sent successfully, False otherwise.
            
        Raises:
            EmailValidationError: If message validation fails.
            EmailDeliveryError: If email delivery fails after retries.
        """
        # Validate message
        self._validate_message(message)
        
        # Attempt delivery with retries
        for attempt in range(MAX_RETRY_ATTEMPTS):
            try:
                success = self._attempt_send(message)
                if success:
                    self._sent_count += 1
                    logger.info(f"Email sent successfully to {message.to_addresses}")
                    return True
                    
            except Exception as e:
                logger.warning(f"Send attempt {attempt + 1} failed: {e}")
                
                if attempt == MAX_RETRY_ATTEMPTS - 1:
                    self._failed_count += 1
                    raise EmailDeliveryError(f"Failed to send email after {MAX_RETRY_ATTEMPTS} attempts")
        
        return False
    
    def send_bulk_emails(self, messages: List[EmailMessage]) -> Dict[str, int]:
        """Send multiple email messages.
        
        Args:
            messages: List of email messages to send.
            
        Returns:
            Dictionary with send statistics.
        """
        results = {'sent': 0, 'failed': 0}
        
        for message in messages:
            try:
                if self.send_email(message):
                    results['sent'] += 1
                else:
                    results['failed'] += 1
            except EmailServiceError:
                results['failed'] += 1
        
        logger.info(f"Bulk send completed: {results}")
        return results
    
    def get_statistics(self) -> Dict[str, float]:
        """Get email service statistics.
        
        Returns:
            Dictionary containing service statistics.
        """
        return {
            'sent_count': self._sent_count,
            'failed_count': self._failed_count,
            'success_rate': self.success_rate,
            'total_attempts': self._sent_count + self._failed_count
        }
    
    # Private methods
    def _validate_message(self, message: EmailMessage) -> None:
        """Validate email message."""
        if not message.to_addresses:
            raise EmailValidationError("Message must have at least one recipient")
        
        for email in message.to_addresses:
            validate_email_address(email)
        
        if not message.subject.strip():
            raise EmailValidationError("Message must have a subject")
        
        if not message.body.strip():
            raise EmailValidationError("Message must have a body")
    
    def _attempt_send(self, message: EmailMessage) -> bool:
        """Attempt to send email message."""
        try:
            with smtplib.SMTP(self._config.smtp_server, self._config.smtp_port) as server:
                if self._config.use_tls:
                    server.starttls()
                
                if self._config.username and self._config.password:
                    server.login(self._config.username, self._config.password)
                
                mime_message = self._create_mime_message(message)
                server.send_message(mime_message)
                
                return True
                
        except Exception as e:
            logger.error(f"SMTP error: {e}")
            return False
    
    def _create_mime_message(self, message: EmailMessage) -> MIMEMultipart:
        """Create MIME message from EmailMessage."""
        mime_msg = MIMEMultipart()
        mime_msg['From'] = message.from_address or self._config.username
        mime_msg['To'] = ', '.join(message.to_addresses)
        mime_msg['Subject'] = message.subject
        
        if message.cc_addresses:
            mime_msg['Cc'] = ', '.join(message.cc_addresses)
        
        # Sanitize content
        safe_body = sanitize_email_content(message.body)
        
        if message.is_html:
            mime_msg.attach(MIMEText(safe_body, 'html'))
        else:
            mime_msg.attach(MIMEText(safe_body, 'plain'))
        
        return mime_msg
    
    # Special methods
    def __str__(self) -> str:
        """String representation of EmailService."""
        return f"EmailService(server={self._config.smtp_server}, sent={self._sent_count})"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return (f"EmailService(smtp_server='{self._config.smtp_server}', "
                f"sent_count={self._sent_count}, failed_count={self._failed_count})")


# Factory function
def create_email_service(smtp_server: str, username: str, password: str) -> EmailService:
    """Create email service with common configuration.
    
    Args:
        smtp_server: SMTP server address.
        username: SMTP username.
        password: SMTP password.
        
    Returns:
        Configured EmailService instance.
    """
    config = EmailConfig(
        smtp_server=smtp_server,
        username=username,
        password=password
    )
    
    return EmailService(config)


# Example usage
if __name__ == "__main__":
    # This demonstrates proper module organization
    # with example usage at the bottom
    
    config = EmailConfig(
        smtp_server="smtp.gmail.com",
        username="your_email@gmail.com",
        password="your_password"
    )
    
    service = EmailService(config)
    
    message = EmailMessage(
        to_addresses=["recipient@example.com"],
        subject="Test Email",
        body="This is a test email message."
    )
    
    try:
        success = service.send_email(message)
        print(f"Email sent: {success}")
        print(f"Statistics: {service.get_statistics()}")
    except EmailServiceError as e:
        print(f"Email error: {e}")
```

---

## Resources and Further Reading

### Official Documentation

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)

### Essential Tools

- **Black**: https://black.readthedocs.io/
- **isort**: https://pycqa.github.io/isort/
- **flake8**: https://flake8.pycqa.org/
- **pylint**: https://pylint.org/
- **mypy**: https://mypy.readthedocs.io/

### Books

- "Clean Code" by Robert C. Martin
- "Effective Python" by Brett Slatkin
- "Python Tricks" by Dan Bader
- "Architecture Patterns with Python" by Harry Percival and Bob Gregory

### Online Resources

- **Real Python**: https://realpython.com/
- **Python.org Style Guide**: https://www.python.org/dev/peps/pep-0008/
- **Google Python Style Guide**: https://google.github.io/styleguide/pyguide.html

### Practice Exercises

1. **Refactor Legacy Code**: Take poorly formatted code and apply all the principles from this tutorial
2. **Code Review Practice**: Review code samples and identify style issues
3. **Tool Integration**: Set up a complete development environment with all the tools mentioned
4. **Style Guide Creation**: Create a custom style guide for your team or project

### Next Steps

1. **Start Small**: Begin by applying basic formatting rules to your current projects
2. **Use Tools**: Integrate automated tools into your development workflow
3. **Practice Consistently**: Make good style a habit in all your Python code
4. **Code Reviews**: Participate in code reviews focusing on style and readability
5. **Teach Others**: Share your knowledge with other developers

---

## Conclusion

Congratulations! You've completed the comprehensive Python Code Style Best Practices tutorial. You now have the knowledge and tools to write clean, readable, and maintainable Python code that follows industry standards.

Remember:
- **Consistency is key** - Apply these principles consistently across all your code
- **Tools are your friends** - Use automated tools to enforce and maintain good style
- **Readability matters** - Always prioritize code readability over cleverness
- **Practice makes perfect** - The more you apply these principles, the more natural they become

Good code style is not just about following rules—it's about writing code that other developers (including your future self) can easily understand, maintain, and extend. Keep practicing, keep learning, and keep writing beautiful Python code!

---

*This tutorial is part of the Python Best Practices series. For more advanced topics, check out the other tutorials in this collection.*
