# Python Documentation Best Practices - Comprehensive Tutorial

Welcome to the complete guide for Python documentation best practices! This tutorial is designed for developers of all levels, from beginners just starting with Python to experts looking to refine their documentation skills.

## Table of Contents

1. [Introduction to Documentation](#1-introduction-to-documentation)
2. [Types of Documentation](#2-types-of-documentation)
3. [Docstring Conventions](#3-docstring-conventions)
4. [Code Comments Best Practices](#4-code-comments-best-practices)
5. [API Documentation](#5-api-documentation)
6. [Sphinx Documentation](#6-sphinx-documentation)
7. [Type Annotations and Documentation](#7-type-annotations-and-documentation)
8. [Examples and Tutorials](#8-examples-and-tutorials)
9. [README Files](#9-readme-files)
10. [Changelog and Versioning](#10-changelog-and-versioning)
11. [Advanced Documentation Techniques](#11-advanced-documentation-techniques)
12. [Documentation Tools and Automation](#12-documentation-tools-and-automation)
13. [Best Practices Summary](#13-best-practices-summary)
14. [Common Mistakes to Avoid](#14-common-mistakes-to-avoid)
15. [Practical Exercises](#15-practical-exercises)

---

## 1. Introduction to Documentation

### What is Documentation?

Documentation is the practice of creating written explanations of your code, its purpose, how it works, and how to use it. Good documentation serves multiple purposes:

- **For yourself**: Remember what your code does months later
- **For your team**: Help colleagues understand and maintain your code
- **For users**: Enable others to use your libraries and applications
- **For contributors**: Make it easier for others to contribute to your project

### Why Documentation Matters

```python
# Without documentation - unclear purpose
def calc(p, r, n, t):
    return p * (1 + r/n) ** (n*t)

# With documentation - clear purpose and usage
def calculate_compound_interest(principal, annual_rate, compounds_per_year, years):
    """
    Calculate compound interest using the standard formula.
    
    Args:
        principal (float): Initial investment amount
        annual_rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        compounds_per_year (int): Number of times interest compounds per year
        years (float): Investment period in years
    
    Returns:
        float: Final amount after compound interest
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 12, 5)
        1283.36
    """
    return principal * (1 + annual_rate/compounds_per_year) ** (compounds_per_year * years)
```

### Documentation Levels

Documentation exists at different levels:

1. **Inline Comments**: Explain specific lines or blocks of code
2. **Docstrings**: Document functions, classes, and modules
3. **API Documentation**: Comprehensive reference for all public interfaces
4. **User Guides**: Step-by-step instructions for end users
5. **Developer Documentation**: Architecture, setup, and contribution guides

---

## 2. Types of Documentation

### 2.1 Code-Level Documentation

#### Inline Comments
```python
# Calculate the monthly payment using the loan formula
# M = P * [r(1+r)^n] / [(1+r)^n - 1]
monthly_rate = annual_rate / 12  # Convert annual rate to monthly
total_payments = years * 12      # Total number of monthly payments

# Handle edge case for zero-interest loans
if monthly_rate == 0:
    return principal / total_payments
```

#### Docstrings
```python
def validate_email(email):
    """
    Validate email address format using regex.
    
    This function checks if the provided email address follows
    standard email format patterns according to RFC 5322.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if email is valid, False otherwise
    
    Raises:
        TypeError: If email is not a string
    
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    import re
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

### 2.2 Project-Level Documentation

#### README Files
Essential for every project, containing:
- Project description and purpose
- Installation instructions
- Basic usage examples
- Contributing guidelines
- License information

#### API Reference
Comprehensive documentation of all public functions, classes, and methods.

#### User Guides and Tutorials
Step-by-step instructions for common use cases and workflows.

---

## 3. Docstring Conventions

Python supports several docstring formats. Choose one and use it consistently throughout your project.

### 3.1 Google Style (Recommended)

```python
def process_data(data, method="average", weights=None):
    """Process numerical data using specified method.
    
    This function applies various statistical methods to process
    numerical data with optional weighting.
    
    Args:
        data (List[float]): List of numerical values to process
        method (str, optional): Processing method. Options are:
            - "average": Calculate weighted or simple average
            - "median": Calculate median value
            - "sum": Calculate total sum
            Defaults to "average".
        weights (List[float], optional): Weights for each data point.
            Must be same length as data if provided. Defaults to None.
    
    Returns:
        float: Processed result based on the specified method
    
    Raises:
        ValueError: If data is empty or weights length doesn't match data
        TypeError: If data contains non-numeric values
        KeyError: If method is not supported
    
    Example:
        >>> data = [1.0, 2.0, 3.0, 4.0, 5.0]
        >>> process_data(data, "average")
        3.0
        >>> process_data(data, "average", [1, 1, 1, 1, 2])
        3.5
    
    Note:
        When using weighted average, weights are normalized automatically.
        Zero weights are allowed and will exclude those data points.
    """
    # Implementation here...
    pass
```

### 3.2 NumPy Style

```python
def calculate_statistics(dataset):
    """Calculate comprehensive statistics for a dataset.
    
    This function computes various statistical measures including
    central tendency and dispersion metrics.
    
    Parameters
    ----------
    dataset : array_like
        Input data for statistical analysis. Can be a list, tuple,
        or numpy array of numerical values.
    
    Returns
    -------
    dict
        Dictionary containing statistical measures:
        - 'mean': Arithmetic mean
        - 'median': Middle value
        - 'std': Standard deviation
        - 'variance': Variance
        - 'min': Minimum value
        - 'max': Maximum value
    
    Raises
    ------
    ValueError
        If dataset is empty or contains non-numeric values
    TypeError
        If dataset is not array-like
    
    Examples
    --------
    >>> data = [1, 2, 3, 4, 5]
    >>> stats = calculate_statistics(data)
    >>> stats['mean']
    3.0
    >>> stats['std']
    1.5811388300841898
    
    See Also
    --------
    numpy.mean : NumPy mean function
    statistics.mean : Built-in statistics module
    
    Notes
    -----
    This function uses the sample standard deviation formula
    (N-1 denominator) rather than population standard deviation.
    """
    # Implementation here...
    pass
```

### 3.3 Sphinx Style

```python
def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between different units.
    
    This function converts temperature values between Celsius,
    Fahrenheit, and Kelvin scales.
    
    :param value: Temperature value to convert
    :type value: float
    :param from_unit: Source temperature unit ('C', 'F', or 'K')
    :type from_unit: str
    :param to_unit: Target temperature unit ('C', 'F', or 'K')
    :type to_unit: str
    :returns: Converted temperature value
    :rtype: float
    :raises ValueError: If units are invalid or value is below absolute zero
    :raises TypeError: If value is not numeric
    
    .. note::
       Absolute zero temperatures:
       - Celsius: -273.15°C
       - Fahrenheit: -459.67°F
       - Kelvin: 0K
    
    .. example::
       >>> convert_temperature(0, 'C', 'F')
       32.0
       >>> convert_temperature(273.15, 'K', 'C')
       0.0
    
    .. seealso::
       :func:`validate_temperature` for temperature validation
    """
    # Implementation here...
    pass
```

---

## 4. Code Comments Best Practices

### 4.1 When to Comment

**DO Comment:**
- Complex algorithms or business logic
- Non-obvious design decisions
- Workarounds for bugs or limitations
- Performance-critical sections
- Regex patterns and complex expressions

```python
# Use binary search for O(log n) performance on sorted data
index = bisect.bisect_left(sorted_list, target)

# Workaround for Python 3.7 compatibility issue with datetime.fromisoformat
# TODO: Remove when Python 3.6 support is dropped
try:
    date = datetime.fromisoformat(date_string)
except AttributeError:
    date = datetime.strptime(date_string, '%Y-%m-%d')

# Apply exponential backoff: wait 2^attempt seconds between retries
wait_time = 2 ** attempt
time.sleep(wait_time)
```

**DON'T Comment:**
- Obvious code that explains itself
- Redundant information already in variable names
- Bad code instead of fixing it

```python
# BAD: Obvious comments
x = 5  # Set x to 5
i += 1  # Increment i

# BAD: Redundant comments
user_name = get_user_name()  # Get the user name

# BAD: Commenting bad code instead of fixing it
# This is a hack but it works
if x == True and y == False and z != None:
    pass
```

### 4.2 Comment Quality Guidelines

```python
# GOOD: Explains WHY, not WHAT
# Cache results to avoid expensive API calls during user session
cached_results = {}

# GOOD: Explains business logic
# Premium customers get 15% discount on orders over $100
if customer.is_premium and order_total > 100:
    discount = order_total * 0.15

# GOOD: Warns about side effects
# WARNING: This function modifies the original list
data.sort()

# GOOD: Explains complex formulas
# Haversine formula for calculating distance between GPS coordinates
# d = 2r * arcsin(sqrt(sin²(Δφ/2) + cos(φ1) * cos(φ2) * sin²(Δλ/2)))
distance = calculate_haversine_distance(lat1, lon1, lat2, lon2)
```

---

## 5. API Documentation

### 5.1 Comprehensive API Documentation Example

```python
from typing import Dict, List, Optional, Union, Any
from dataclasses import dataclass
from datetime import datetime
import re

@dataclass
class User:
    """User data model with validation and serialization.
    
    Represents a user in the system with all necessary attributes
    and methods for data manipulation.
    
    Attributes:
        user_id (int): Unique identifier for the user
        username (str): Unique username (3-30 characters)
        email (str): Valid email address
        full_name (str): User's display name
        created_at (datetime): Account creation timestamp
        is_active (bool): Account status flag
        metadata (Dict[str, Any]): Additional user data
    
    Example:
        >>> user = User(
        ...     user_id=1,
        ...     username="john_doe",
        ...     email="john@example.com",
        ...     full_name="John Doe"
        ... )
        >>> user.to_dict()
        {'user_id': 1, 'username': 'john_doe', ...}
    """
    user_id: int
    username: str
    email: str
    full_name: str
    created_at: datetime = None
    is_active: bool = True
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        """Initialize default values and validate data."""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.metadata is None:
            self.metadata = {}
        
        # Validate required fields
        self._validate_username()
        self._validate_email()
        self._validate_full_name()
    
    def _validate_username(self) -> None:
        """Validate username format and constraints."""
        if not isinstance(self.username, str):
            raise TypeError("Username must be a string")
        
        if not 3 <= len(self.username) <= 30:
            raise ValueError("Username must be 3-30 characters long")
        
        if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$|^[a-zA-Z0-9]$', self.username):
            raise ValueError("Username contains invalid characters")
    
    def _validate_email(self) -> None:
        """Validate email address format."""
        if not isinstance(self.email, str):
            raise TypeError("Email must be a string")
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, self.email):
            raise ValueError("Invalid email format")
    
    def _validate_full_name(self) -> None:
        """Validate full name format."""
        if not isinstance(self.full_name, str):
            raise TypeError("Full name must be a string")
        
        if not 1 <= len(self.full_name.strip()) <= 100:
            raise ValueError("Full name must be 1-100 characters long")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user object to dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of user data
            
        Example:
            >>> user = User(1, "john", "john@test.com", "John Doe")
            >>> data = user.to_dict()
            >>> data['username']
            'john'
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active,
            'metadata': self.metadata
        }

class UserAPI:
    """Complete user management API with CRUD operations.
    
    This class provides a comprehensive interface for managing users
    with proper validation, error handling, and data persistence.
    
    Attributes:
        users (Dict[int, User]): Internal user storage
        next_id (int): Counter for generating unique IDs
        username_index (Dict[str, int]): Username to ID mapping
        email_index (Dict[str, int]): Email to ID mapping
    
    Example:
        >>> api = UserAPI()
        >>> user = api.create_user("john_doe", "john@example.com", "John Doe")
        >>> all_users = api.get_all_users()
        >>> len(all_users)
        1
    """
    
    def __init__(self):
        """Initialize empty user storage and indexes."""
        self.users: Dict[int, User] = {}
        self.next_id: int = 1
        self.username_index: Dict[str, int] = {}
        self.email_index: Dict[str, int] = {}
    
    def create_user(
        self,
        username: str,
        email: str,
        full_name: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> User:
        """Create a new user with validation.
        
        Creates a new user after validating all input data and
        checking for uniqueness constraints.
        
        Args:
            username (str): Unique username (3-30 characters)
            email (str): Valid email address
            full_name (str): User's display name (1-100 characters)
            metadata (Dict[str, Any], optional): Additional user data
        
        Returns:
            User: The newly created user object
        
        Raises:
            ValueError: If validation fails or user already exists
            TypeError: If arguments have wrong types
        
        Example:
            >>> api = UserAPI()
            >>> user = api.create_user(
            ...     "jane_doe",
            ...     "jane@example.com",
            ...     "Jane Doe",
            ...     {"department": "Engineering"}
            ... )
            >>> user.username
            'jane_doe'
        """
        # Check for existing username
        if username in self.username_index:
            raise ValueError(f"Username '{username}' already exists")
        
        # Check for existing email
        if email in self.email_index:
            raise ValueError(f"Email '{email}' already exists")
        
        # Create user (validation happens in User.__post_init__)
        user = User(
            user_id=self.next_id,
            username=username,
            email=email,
            full_name=full_name,
            metadata=metadata or {}
        )
        
        # Store user and update indexes
        self.users[self.next_id] = user
        self.username_index[username] = self.next_id
        self.email_index[email] = self.next_id
        self.next_id += 1
        
        return user
    
    def get_user_by_id(self, user_id: int) -> User:
        """Retrieve user by ID.
        
        Args:
            user_id (int): User's unique identifier
        
        Returns:
            User: User object with specified ID
        
        Raises:
            ValueError: If user_id is invalid or user not found
            TypeError: If user_id is not an integer
        
        Example:
            >>> api = UserAPI()
            >>> user = api.create_user("john", "john@test.com", "John")
            >>> retrieved = api.get_user_by_id(user.user_id)
            >>> retrieved.username
            'john'
        """
        if not isinstance(user_id, int):
            raise TypeError("User ID must be an integer")
        
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        
        return self.users[user_id]
    
    def get_all_users(self, include_inactive: bool = False) -> List[User]:
        """Get all users with optional filtering.
        
        Args:
            include_inactive (bool): Include inactive users in results
        
        Returns:
            List[User]: List of user objects matching criteria
        
        Example:
            >>> api = UserAPI()
            >>> api.create_user("user1", "user1@test.com", "User One")
            >>> api.create_user("user2", "user2@test.com", "User Two")
            >>> users = api.get_all_users()
            >>> len(users)
            2
        """
        if include_inactive:
            return list(self.users.values())
        else:
            return [user for user in self.users.values() if user.is_active]
```

### 5.2 Error Handling Documentation

```python
class APIError(Exception):
    """Base exception for API-related errors.
    
    Provides consistent error handling across the API with
    structured error information.
    
    Attributes:
        message (str): Human-readable error description
        error_code (str): Machine-readable error identifier
        status_code (int): HTTP status code equivalent
    
    Args:
        message (str): Error description
        error_code (str): Error identifier (default: "API_ERROR")
        status_code (int): HTTP status code (default: 500)
    
    Example:
        >>> try:
        ...     raise APIError("Something went wrong", "GENERIC_ERROR", 500)
        ... except APIError as e:
        ...     print(f"Error {e.error_code}: {e.message}")
        Error GENERIC_ERROR: Something went wrong
    """
    
    def __init__(self, message: str, error_code: str = "API_ERROR", status_code: int = 500):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        super().__init__(self.message)

class UserNotFoundError(APIError):
    """Raised when requested user cannot be found.
    
    This specific exception is raised when attempting to access,
    update, or delete a user that doesn't exist.
    
    Args:
        user_identifier (Union[int, str]): ID or username that wasn't found
    
    Example:
        >>> try:
        ...     raise UserNotFoundError("nonexistent_user")
        ... except UserNotFoundError as e:
        ...     print(e.status_code)
        404
    """
    
    def __init__(self, user_identifier: Union[int, str]):
        message = f"User '{user_identifier}' not found"
        super().__init__(message, "USER_NOT_FOUND", 404)
```

---

## 6. Sphinx Documentation

### 6.1 Setting Up Sphinx

Sphinx is the most popular documentation generator for Python projects. Here's how to set it up:

#### Installation
```bash
pip install sphinx sphinx_rtd_theme
```

#### Basic Configuration (conf.py)
```python
# Configuration file for Sphinx documentation builder

# -- Project information -----------------------------------------------------
project = 'My Python Project'
copyright = '2025, Your Name'
author = 'Your Name'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Auto-generate docs from docstrings
    'sphinx.ext.viewcode',       # Add source code links
    'sphinx.ext.napoleon',       # Support Google/NumPy docstring styles
    'sphinx.ext.intersphinx',    # Link to other documentation
    'sphinx.ext.todo',           # TODO directive support
    'sphinx.ext.coverage',       # Documentation coverage checking
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Read the Docs theme
html_static_path = ['_static']

# -- Extension configuration ------------------------------------------------
# Napoleon settings for Google/NumPy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
}

# Intersphinx mapping to link to other documentation
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'requests': ('https://requests.readthedocs.io/en/latest/', None),
}
```

### 6.2 Creating Documentation Structure

#### Main Index (index.rst)
```rst
Welcome to My Project Documentation
===================================

This is the main documentation for My Python Project, a comprehensive
library for data processing and analysis.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api
   examples
   contributing

Features
--------

* Fast data processing
* Comprehensive API
* Extensive documentation
* Type hints support

Quick Example
-------------

.. code-block:: python

   from myproject import DataProcessor
   
   processor = DataProcessor()
   result = processor.process_data([1, 2, 3, 4, 5])
   print(result)

Installation
------------

.. code-block:: bash

   pip install myproject

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

#### API Reference (api.rst)
```rst
API Reference
=============

This section contains the complete API reference for all public
classes and functions.

Core Module
-----------

.. automodule:: myproject.core
   :members:
   :undoc-members:
   :show-inheritance:

Data Processing
---------------

.. autoclass:: myproject.DataProcessor
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Utility Functions
-----------------

.. autofunction:: myproject.utils.validate_data
.. autofunction:: myproject.utils.format_output
```

### 6.3 Advanced Sphinx Features

#### Cross-References
```python
def process_data(data):
    """Process input data using advanced algorithms.
    
    This function uses the :class:`DataProcessor` class internally
    and applies the algorithm described in :func:`validate_data`.
    
    See also :doc:`examples` for usage examples.
    
    Args:
        data: Input data to process
    
    Returns:
        Processed data
    
    .. seealso::
       :class:`DataProcessor`
          Main processing class
       :func:`validate_data`
          Data validation function
    """
    pass
```

#### Code Examples with Testing
```python
def calculate_average(numbers):
    """Calculate the arithmetic mean of a list of numbers.
    
    Args:
        numbers (List[float]): List of numerical values
    
    Returns:
        float: Arithmetic mean of the input numbers
    
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([10, 20])
        15.0
        >>> calculate_average([])
        Traceback (most recent call last):
            ...
        ValueError: Cannot calculate average of empty list
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

---

## 7. Type Annotations and Documentation

### 7.1 Basic Type Hints

```python
from typing import List, Dict, Optional, Union, Callable, Any

def process_user_data(
    user_id: int,
    user_data: Dict[str, Any],
    processors: List[Callable[[Dict[str, Any]], Dict[str, Any]]],
    validate: bool = True
) -> Optional[Dict[str, Any]]:
    """Process user data through a series of processors.
    
    Args:
        user_id: Unique identifier for the user
        user_data: Dictionary containing user information
        processors: List of functions to apply to user data
        validate: Whether to validate data before processing
    
    Returns:
        Processed user data, or None if validation fails
    """
    if validate and not _validate_user_data(user_data):
        return None
    
    result = user_data.copy()
    for processor in processors:
        result = processor(result)
    
    return result
```

### 7.2 Advanced Type Annotations

```python
from typing import TypeVar, Generic, Protocol, Literal, overload
from dataclasses import dataclass

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class Comparable(Protocol):
    """Protocol for objects that can be compared."""
    def __lt__(self, other: Any) -> bool: ...

@dataclass
class Result(Generic[T]):
    """Generic result container with success/error handling.
    
    Type Parameters:
        T: Type of the successful result value
    
    Attributes:
        success (bool): Whether the operation was successful
        value (T, optional): Result value if successful
        error (str, optional): Error message if failed
    
    Example:
        >>> result = Result.success("Hello, World!")
        >>> result.success
        True
        >>> result.value
        'Hello, World!'
    """
    success: bool
    value: Optional[T] = None
    error: Optional[str] = None
    
    @classmethod
    def success(cls, value: T) -> 'Result[T]':
        """Create a successful result."""
        return cls(success=True, value=value)
    
    @classmethod
    def failure(cls, error: str) -> 'Result[T]':
        """Create a failed result."""
        return cls(success=False, error=error)

def sort_items(items: List[T]) -> List[T]:
    """Sort a list of comparable items.
    
    Type Parameters:
        T: Type of items to sort (must be comparable)
    
    Args:
        items: List of items to sort
    
    Returns:
        New sorted list
    
    Example:
        >>> sort_items([3, 1, 4, 1, 5])
        [1, 1, 3, 4, 5]
        >>> sort_items(['banana', 'apple', 'cherry'])
        ['apple', 'banana', 'cherry']
    """
    return sorted(items)

@overload
def get_item(container: Dict[K, V], key: K) -> V: ...

@overload
def get_item(container: List[T], key: int) -> T: ...

def get_item(container, key):
    """Get item from container with type-safe overloads.
    
    This function provides type-safe access to dictionary and list items
    with proper type inference based on the container type.
    
    Args:
        container: Dictionary or list to access
        key: Key (for dict) or index (for list)
    
    Returns:
        Item from the container
    
    Example:
        >>> data = {'name': 'John', 'age': 30}
        >>> get_item(data, 'name')  # Returns str
        'John'
        >>> numbers = [1, 2, 3, 4, 5]
        >>> get_item(numbers, 2)  # Returns int
        3
    """
    return container[key]
```

---

## 8. Examples and Tutorials

### 8.1 Writing Effective Examples

Examples are crucial for helping users understand how to use your code. Here are best practices:

#### Complete, Runnable Examples
```python
def send_email(to_address, subject, body, attachments=None):
    """Send an email with optional attachments.
    
    Args:
        to_address (str): Recipient email address
        subject (str): Email subject line
        body (str): Email body content
        attachments (List[str], optional): List of file paths to attach
    
    Returns:
        bool: True if email sent successfully
    
    Raises:
        ValueError: If email address is invalid
        FileNotFoundError: If attachment file doesn't exist
    
    Examples:
        Basic email:
        
        >>> send_email(
        ...     "user@example.com",
        ...     "Hello",
        ...     "This is a test email."
        ... )
        True
        
        Email with attachments:
        
        >>> send_email(
        ...     "user@example.com",
        ...     "Report",
        ...     "Please find the report attached.",
        ...     attachments=["report.pdf", "data.xlsx"]
        ... )
        True
        
        Error handling:
        
        >>> try:
        ...     send_email("invalid-email", "Test", "Body")
        ... except ValueError as e:
        ...     print(f"Error: {e}")
        Error: Invalid email address format
    """
    # Implementation would go here
    pass
```

#### Progressive Examples (Beginner to Advanced)
```python
class DataAnalyzer:
    """Analyze datasets with various statistical methods.
    
    Examples:
        Basic usage (Beginner):
        
        >>> analyzer = DataAnalyzer()
        >>> data = [1, 2, 3, 4, 5]
        >>> analyzer.mean(data)
        3.0
        
        With configuration (Intermediate):
        
        >>> analyzer = DataAnalyzer(precision=4)
        >>> data = [1.234, 2.567, 3.891]
        >>> analyzer.mean(data)
        2.564
        
        Advanced usage with custom functions:
        
        >>> def custom_weight(x):
        ...     return x ** 0.5
        >>> analyzer = DataAnalyzer()
        >>> data = [1, 4, 9, 16, 25]
        >>> analyzer.weighted_mean(data, weight_func=custom_weight)
        4.123
        
        Batch processing:
        
        >>> datasets = {
        ...     'group_a': [1, 2, 3],
        ...     'group_b': [4, 5, 6],
        ...     'group_c': [7, 8, 9]
        ... }
        >>> results = analyzer.analyze_multiple(datasets)
        >>> results['group_a']['mean']
        2.0
    """
    pass
```

### 8.2 Tutorial Structure

#### Step-by-Step Tutorials
```markdown
# Getting Started with DataProcessor

## Step 1: Installation and Setup

First, install the package:

```bash
pip install dataprocessor
```

Import the main class:

```python
from dataprocessor import DataProcessor

# Create a processor instance
processor = DataProcessor()
```

## Step 2: Basic Data Processing

Process a simple list of numbers:

```python
# Sample data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic processing
result = processor.process(numbers)
print(f"Processed data: {result}")
# Output: Processed data: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Step 3: Advanced Configuration

Configure the processor for specific needs:

```python
# Create processor with custom settings
processor = DataProcessor(
    multiplier=3,
    filter_odd=True,
    sort_result=True
)

# Process with configuration
data = [5, 2, 8, 1, 9, 3]
result = processor.process(data)
print(f"Advanced result: {result}")
# Output: Advanced result: [6, 15, 24]
```

## Step 4: Error Handling

Handle common errors gracefully:

```python
try:
    # This might raise an error
    result = processor.process("invalid_data")
except TypeError as e:
    print(f"Type error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
```
```

---

## 9. README Files

### 9.1 Essential README Structure

A good README should include:

```markdown
# Project Name

Brief description of what your project does and why it's useful.

[![Build Status](https://travis-ci.org/username/project.svg?branch=main)](https://travis-ci.org/username/project)
[![Coverage Status](https://coveralls.io/repos/github/username/project/badge.svg?branch=main)](https://coveralls.io/github/username/project?branch=main)
[![PyPI version](https://badge.fury.io/py/project.svg)](https://badge.fury.io/py/project)

## Features

- ✨ Feature 1: Brief description
- 🚀 Feature 2: Brief description
- 🛡️ Feature 3: Brief description
- 📊 Feature 4: Brief description

## Quick Start

### Installation

```bash
pip install your-project
```

### Basic Usage

```python
from your_project import MainClass

# Create instance
instance = MainClass()

# Use it
result = instance.do_something("example")
print(result)
```

## Documentation

Full documentation is available at [https://your-project.readthedocs.io/](https://your-project.readthedocs.io/)

## Examples

### Example 1: Basic Usage
```python
# Code example here
```

### Example 2: Advanced Usage
```python
# More complex example here
```

## API Reference

### MainClass

#### Methods

- `do_something(param)`: Description of what it does
- `another_method(param1, param2)`: Description

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

1. Clone the repository
2. Install development dependencies: `pip install -r requirements-dev.txt`
3. Run tests: `pytest`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes.

## Support

- 📧 Email: support@yourproject.com
- 💬 Discord: [Join our server](https://discord.gg/yourserver)
- 🐛 Issues: [GitHub Issues](https://github.com/username/project/issues)
```

### 9.2 README Best Practices

1. **Keep it concise but comprehensive**
2. **Use clear headings and structure**
3. **Include working code examples**
4. **Add badges for build status, coverage, etc.**
5. **Provide multiple ways to get help**
6. **Keep it up to date**

---

## 10. Changelog and Versioning

### 10.1 Semantic Versioning

Follow [Semantic Versioning](https://semver.org/) (SemVer):

- **MAJOR** version: Incompatible API changes
- **MINOR** version: Backward-compatible functionality additions
- **PATCH** version: Backward-compatible bug fixes

### 10.2 Changelog Format

Use [Keep a Changelog](https://keepachangelog.com/) format:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New feature for data validation
- Support for custom processors

### Changed
- Improved error messages
- Updated dependencies

### Deprecated
- Old API methods (will be removed in v3.0.0)

### Removed
- Legacy configuration options

### Fixed
- Bug in data processing pipeline
- Memory leak in large dataset handling

### Security
- Fixed potential SQL injection vulnerability

## [2.1.0] - 2025-01-15

### Added
- New `process_batch()` method for handling multiple datasets
- Configuration validation with helpful error messages
- Support for custom data transformers

### Changed
- Improved performance for large datasets (up to 40% faster)
- Better error handling with more specific exception types

### Fixed
- Issue with empty dataset processing
- Memory usage optimization for streaming data

## [2.0.0] - 2025-12-01

### Added
- Complete rewrite with new architecture
- Type hints for all public APIs
- Comprehensive test suite with 95% coverage

### Changed
- **BREAKING**: New API structure (see migration guide)
- **BREAKING**: Configuration format changed
- Improved documentation with examples

### Removed
- **BREAKING**: Deprecated methods from v1.x
- Legacy configuration support

## [1.2.1] - 2025-10-15

### Fixed
- Critical bug in data serialization
- Documentation typos

## [1.2.0] - 2025-10-01

### Added
- New export formats (JSON, CSV, XML)
- Batch processing capabilities

### Changed
- Improved error messages
- Performance optimizations

## [1.1.0] - 2025-09-01

### Added
- Initial release with basic functionality
- Documentation and examples
```

---

## 11. Advanced Documentation Techniques

### 11.1 Documentation Testing with Doctest

```python
def fibonacci(n):
    """Generate the nth Fibonacci number.
    
    The Fibonacci sequence starts with 0 and 1, and each subsequent
    number is the sum of the two preceding ones.
    
    Args:
        n (int): Position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    
    Examples:
        Basic usage:
        
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
        
        Error cases:
        
        >>> fibonacci(-1)
        Traceback (most recent call last):
            ...
        ValueError: n must be non-negative
        
        >>> fibonacci(3.14)
        Traceback (most recent call last):
            ...
        TypeError: n must be an integer
        
        Edge cases:
        
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Run doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

### 11.2 Interactive Documentation

```python
class InteractiveCalculator:
    """Interactive calculator with step-by-step examples.
    
    This calculator provides detailed explanations of each operation
    and maintains a history for educational purposes.
    
    Examples:
        Create a calculator and perform operations:
        
        >>> calc = InteractiveCalculator()
        >>> calc.add(5, 3)
        Step 1: Adding 5 + 3
        Step 2: Result = 8
        8
        
        >>> calc.multiply(4, 6)
        Step 1: Multiplying 4 * 6
        Step 2: Result = 24
        24
        
        View calculation history:
        
        >>> calc.get_history()
        ['5 + 3 = 8', '4 * 6 = 24']
        
        Chain operations:
        
        >>> calc.add(10, 5).multiply(2).subtract(5)
        Step 1: Adding 10 + 5
        Step 2: Result = 15
        Step 3: Multiplying 15 * 2
        Step 4: Result = 30
        Step 5: Subtracting 30 - 5
        Step 6: Result = 25
        25
    """
    
    def __init__(self, verbose=True):
        """Initialize calculator with optional verbose mode."""
        self.history = []
        self.verbose = verbose
        self.current_value = 0
    
    def add(self, a, b=None):
        """Add two numbers or add to current value."""
        if b is None:
            b = a
            a = self.current_value
        
        if self.verbose:
            print(f"Step 1: Adding {a} + {b}")
        
        result = a + b
        self.current_value = result
        
        if self.verbose:
            print(f"Step 2: Result = {result}")
        
        self.history.append(f"{a} + {b} = {result}")
        return self
    
    def get_history(self):
        """Return calculation history."""
        return self.history.copy()
```

### 11.3 Documentation with Rich Media

```python
def plot_function_example():
    """Example function that generates plots for documentation.
    
    This function demonstrates how to include plots and rich media
    in your documentation using matplotlib and other tools.
    
    Returns:
        matplotlib.figure.Figure: The generated plot
    
    Examples:
        Generate a simple plot:
        
        >>> import matplotlib.pyplot as plt
        >>> fig = plot_function_example()
        >>> plt.show()  # doctest: +SKIP
        
        Save plot to file:
        
        >>> fig = plot_function_example()
        >>> fig.savefig('example_plot.png')  # doctest: +SKIP
    
    Note:
        This function requires matplotlib to be installed:
        
        .. code-block:: bash
        
           pip install matplotlib
        
        The generated plot shows a sine wave with customizable parameters.
        
        .. image:: _static/example_plot.png
           :alt: Example sine wave plot
           :align: center
    """
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        raise ImportError("matplotlib and numpy are required for this function")
    
    # Generate data
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.set_title('Example Sine Wave')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    return fig
```

---

## 12. Documentation Tools and Automation

### 12.1 Automated Documentation Generation

#### Using Sphinx with GitHub Actions

```yaml
# .github/workflows/docs.yml
name: Documentation

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  docs:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install sphinx sphinx_rtd_theme
        pip install -r requirements.txt
    
    - name: Build documentation
      run: |
        cd docs
        make html
    
    - name: Deploy to GitHub Pages
      if: github.ref == 'refs/heads/main'
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./docs/_build/html
```

#### Pre-commit Hooks for Documentation

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: docstring-check
        name: Check docstrings
        entry: python -m pydocstyle
        language: system
        files: \.py$
      
      - id: doc-build
        name: Build documentation
        entry: bash -c 'cd docs && make html'
        language: system
        pass_filenames: false
        files: \.py$|\.rst$|\.md$
```

### 12.2 Documentation Quality Checks

```python
def check_documentation_quality(module_path):
    """Check documentation quality metrics.
    
    This function analyzes Python modules and provides metrics
    about documentation coverage and quality.
    
    Args:
        module_path (str): Path to the Python module to analyze
    
    Returns:
        Dict[str, Any]: Documentation quality metrics
    
    Example:
        >>> metrics = check_documentation_quality("mymodule.py")
        >>> print(f"Coverage: {metrics['coverage']:.1%}")
        Coverage: 85.5%
    """
    import ast
    import inspect
    
    with open(module_path, 'r') as f:
        tree = ast.parse(f.read())
    
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    
    documented_functions = sum(1 for func in functions if ast.get_docstring(func))
    documented_classes = sum(1 for cls in classes if ast.get_docstring(cls))
    
    total_items = len(functions) + len(classes)
    documented_items = documented_functions + documented_classes
    
    coverage = documented_items / total_items if total_items > 0 else 0
    
    return {
        'coverage': coverage,
        'total_functions': len(functions),
        'documented_functions': documented_functions,
        'total_classes': len(classes),
        'documented_classes': documented_classes,
        'suggestions': _generate_suggestions(functions, classes)
    }

def _generate_suggestions(functions, classes):
    """Generate suggestions for improving documentation."""
    suggestions = []
    
    for func in functions:
        if not ast.get_docstring(func):
            suggestions.append(f"Add docstring to function '{func.name}'")
    
    for cls in classes:
        if not ast.get_docstring(cls):
            suggestions.append(f"Add docstring to class '{cls.name}'")
    
    return suggestions
```

---

## 13. Best Practices Summary

### 13.1 The Documentation Pyramid

1. **Code Comments** (Foundation)
   - Explain complex logic
   - Document business rules
   - Warn about side effects

2. **Docstrings** (Core)
   - Document all public functions/classes
   - Include examples and type information
   - Explain parameters and return values

3. **API Documentation** (Structure)
   - Comprehensive reference
   - Consistent formatting
   - Error handling documentation

4. **User Guides** (Application)
   - Step-by-step tutorials
   - Real-world examples
   - Best practices

5. **Project Documentation** (Context)
   - README files
   - Contributing guides
   - Architecture documentation

### 13.2 Key Principles

1. **Write for your audience**
   - Beginners need more explanation
   - Experts need quick reference
   - Provide both levels

2. **Keep it up to date**
   - Update docs with code changes
   - Use automated testing for examples
   - Regular documentation reviews

3. **Make it discoverable**
   - Clear navigation structure
   - Good search functionality
   - Cross-references and links

4. **Test your documentation**
   - Use doctest for examples
   - Verify installation instructions
   - Get feedback from users

5. **Automate what you can**
   - Generate API docs from code
   - Automated building and deployment
   - Quality checks in CI/CD

### 13.3 Documentation Checklist

Before releasing your project, ensure:

- [ ] All public functions have docstrings
- [ ] Examples are tested and working
- [ ] README is comprehensive and up-to-date
- [ ] Installation instructions are clear
- [ ] API documentation is complete
- [ ] Error handling is documented
- [ ] Type hints are provided
- [ ] Changelog is maintained
- [ ] Contributing guidelines exist
- [ ] Documentation builds without errors

---

## 14. Common Mistakes to Avoid

### 14.1 Documentation Anti-Patterns

#### 1. Obvious Comments
```python
# BAD: States the obvious
x = x + 1  # Increment x by 1
user_name = input("Enter name: ")  # Get user name

# GOOD: Explains why
x += 1  # Move to next iteration
user_name = input("Enter name: ").strip()  # Remove whitespace for validation
```

#### 2. Outdated Documentation
```python
# BAD: Comment doesn't match code
# Calculate the square of the number
result = number ** 3  # Actually calculates cube!

# GOOD: Keep comments in sync
# Calculate the cube of the number
result = number ** 3
```

#### 3. Over-Documentation
```python
# BAD: Too much obvious documentation
def add_numbers(a, b):
    """Add two numbers together.
    
    This function takes two numbers as input and returns their sum.
    It uses the + operator to perform addition.
    
    Args:
        a: The first number to add
        b: The second number to add
    
    Returns:
        The sum of a and b
    """
    return a + b  # Return the sum

# GOOD: Concise but complete
def add_numbers(a, b):
    """Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of the two numbers
    """
    return a + b
```

#### 4. Missing Error Documentation
```python
# BAD: No error documentation
def divide(a, b):
    """Divide a by b."""
    return a / b

# GOOD: Document possible errors
def divide(a, b):
    """Divide a by b.
    
    Args:
        a (float): Dividend
        b (float): Divisor
    
    Returns:
        float: Result of division
    
    Raises:
        ZeroDivisionError: If b is zero
        TypeError: If arguments are not numeric
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

### 14.2 Common Documentation Bugs

1. **Inconsistent formatting** across the project
2. **Missing examples** for complex functions
3. **Broken links** in documentation
4. **Untested code examples** that don't work
5. **Missing type information** in docstrings
6. **Poor organization** of documentation structure

---

## 15. Practical Exercises

### Exercise 1: Basic Docstring Writing

Write comprehensive docstrings for these functions:

```python
def calculate_bmi(weight, height):
    # TODO: Add docstring
    return weight / (height ** 2)

def find_max_value(data):
    # TODO: Add docstring
    if not data:
        raise ValueError("Empty data")
    return max(data)

class BankAccount:
    # TODO: Add class docstring
    def __init__(self, initial_balance=0):
        # TODO: Add method docstring
        self.balance = initial_balance
    
    def deposit(self, amount):
        # TODO: Add method docstring
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance
```

### Exercise 2: API Documentation

Create a complete API documentation for a simple library:

```python
# TODO: Document this library completely
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title, description="", priority="medium"):
        task = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                return task
        raise ValueError(f"Task {task_id} not found")
    
    def get_tasks(self, completed=None):
        if completed is None:
            return self.tasks.copy()
        return [t for t in self.tasks if t['completed'] == completed]
```

### Exercise 3: README Creation

Create a comprehensive README for the TaskManager library above, including:
- Project description
- Installation instructions
- Usage examples
- API reference
- Contributing guidelines

### Exercise 4: Error Documentation

Add comprehensive error handling documentation:

```python
def process_file(filename, encoding='utf-8'):
    # TODO: Document all possible errors
    with open(filename, 'r', encoding=encoding) as f:
        data = f.read()
    
    if not data.strip():
        raise ValueError("File is empty")
    
    lines = data.split('\n')
    processed = []
    
    for line in lines:
        if line.startswith('#'):
            continue
        processed.append(line.upper())
    
    return processed
```

---

## Conclusion

Congratulations! You've completed the comprehensive Python documentation tutorial. You now have the knowledge and tools to create professional-quality documentation for your Python projects.

### Key Takeaways

1. **Documentation is code** - Treat it with the same care and attention
2. **Write for humans** - Make it clear, helpful, and accessible
3. **Keep it current** - Outdated docs are worse than no docs
4. **Test everything** - Ensure examples work and links aren't broken
5. **Automate when possible** - Use tools to maintain quality

### Next Steps

1. **Practice** - Apply these techniques to your current projects
2. **Get feedback** - Ask colleagues and users about your documentation
3. **Stay updated** - Follow documentation best practices in the community
4. **Contribute** - Help improve documentation in open source projects
5. **Teach others** - Share your knowledge with fellow developers

### Resources for Further Learning

- [Python Documentation Guide](https://docs.python.org/devguide/documenting.html)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
- [NumPy Documentation Style](https://numpydoc.readthedocs.io/)
- [Write the Docs Community](https://www.writethedocs.org/)

Remember: Great documentation is a gift to your future self and to everyone who will use your code. Invest the time to do it right, and you'll reap the benefits for years to come!

---

*This tutorial is part of the Python Best Practices series. For more tutorials and examples, visit the [python-practices repository](https://github.com/your-username/python-practices).*
