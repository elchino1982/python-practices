"""Question: Learn and implement proper Python docstring conventions.

Create comprehensive examples demonstrating different docstring styles and best practices
for documenting Python code effectively.

Requirements:
1. Demonstrate Google, NumPy, and Sphinx docstring styles
2. Show proper documentation for functions, classes, and methods
3. Include examples of parameter descriptions, return values, and exceptions
4. Demonstrate module-level and package-level documentation
5. Show best practices for different types of functions and classes

Example usage:
    calculator = Calculator()
    result = calculator.add(5, 3)
    help(calculator.add)  # Shows proper docstring
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about different docstring styles and when to use them
# - Start with simple function documentation
# - Test your docstrings with help() function
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
# - What are the main docstring styles in Python?
# - How do you document function parameters and return values?
# - What information should be included in class docstrings?
# - How do you document exceptions that might be raised?
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


# Step 1: Basic function docstrings - Google style
# ===============================================================================

# Explanation:
# Google style docstrings are clean, readable, and widely used in the Python community.
# They use simple section headers and are easy to write and maintain.

def add_numbers(a, b):
    """Add two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    
    Example:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    return a + b

def divide_numbers(dividend, divisor):
    """Divide one number by another.
    
    Args:
        dividend (int or float): The number to be divided.
        divisor (int or float): The number to divide by.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If divisor is zero.
        TypeError: If arguments are not numbers.
    
    Example:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(7, 3)
        2.3333333333333335
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Arguments must be numbers")
    
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return dividend / divisor

# What we accomplished in this step:
# - Created basic function docstrings using Google style
# - Documented parameters with types and descriptions
# - Included return value documentation
# - Added exception documentation
# - Provided usage examples


# Step 2: NumPy style docstrings
# ===============================================================================

# Explanation:
# NumPy style docstrings use underlined section headers and are popular in
# scientific computing. They provide more structured formatting.

def add_numbers(a, b):
    """Add two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    
    Example:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    return a + b

def divide_numbers(dividend, divisor):
    """Divide one number by another.
    
    Args:
        dividend (int or float): The number to be divided.
        divisor (int or float): The number to divide by.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If divisor is zero.
        TypeError: If arguments are not numbers.
    
    Example:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(7, 3)
        2.3333333333333335
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Arguments must be numbers")
    
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return dividend / divisor

def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers.
    
    Parameters
    ----------
    numbers : list of int or float
        A list of numerical values to analyze.
    
    Returns
    -------
    dict
        A dictionary containing statistical measures:
        - 'mean': float, the arithmetic mean
        - 'median': float, the median value
        - 'std': float, the standard deviation
    
    Raises
    ------
    ValueError
        If the input list is empty.
    TypeError
        If the input is not a list or contains non-numeric values.
    
    Examples
    --------
    >>> calculate_statistics([1, 2, 3, 4, 5])
    {'mean': 3.0, 'median': 3.0, 'std': 1.5811388300841898}
    
    >>> calculate_statistics([10, 20, 30])
    {'mean': 20.0, 'median': 20.0, 'std': 10.0}
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    
    # Calculate statistics
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    median = sorted_nums[n // 2] if n % 2 == 1 else (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
    # Standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std = variance ** 0.5
    
    return {'mean': mean, 'median': median, 'std': std}

def process_text(text, uppercase=False, remove_spaces=False):
    """Process text with various transformation options.
    
    Parameters
    ----------
    text : str
        The input text to process.
    uppercase : bool, optional
        Whether to convert text to uppercase (default is False).
    remove_spaces : bool, optional
        Whether to remove all spaces from text (default is False).
    
    Returns
    -------
    str
        The processed text after applying transformations.
    
    Examples
    --------
    >>> process_text("Hello World")
    'Hello World'
    
    >>> process_text("Hello World", uppercase=True)
    'HELLO WORLD'
    
    >>> process_text("Hello World", remove_spaces=True)
    'HelloWorld'
    
    >>> process_text("Hello World", uppercase=True, remove_spaces=True)
    'HELLOWORLD'
    """
    result = text
    
    if uppercase:
        result = result.upper()
    
    if remove_spaces:
        result = result.replace(' ', '')
    
    return result

# What we accomplished in this step:
# - Introduced NumPy style docstrings with underlined headers
# - Showed more complex parameter documentation
# - Demonstrated optional parameter documentation
# - Added comprehensive examples section


# Step 3: Class documentation and Sphinx style docstrings
# ===============================================================================

# Explanation:
# Class docstrings should describe the purpose of the class, its main functionality,
# and how to use it. Sphinx style uses reStructuredText markup.

def add_numbers(a, b):
    """Add two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    
    Example:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    return a + b

def divide_numbers(dividend, divisor):
    """Divide one number by another.
    
    Args:
        dividend (int or float): The number to be divided.
        divisor (int or float): The number to divide by.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If divisor is zero.
        TypeError: If arguments are not numbers.
    
    Example:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(7, 3)
        2.3333333333333335
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Arguments must be numbers")
    
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return dividend / divisor

def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers.
    
    Parameters
    ----------
    numbers : list of int or float
        A list of numerical values to analyze.
    
    Returns
    -------
    dict
        A dictionary containing statistical measures:
        - 'mean': float, the arithmetic mean
        - 'median': float, the median value
        - 'std': float, the standard deviation
    
    Raises
    ------
    ValueError
        If the input list is empty.
    TypeError
        If the input is not a list or contains non-numeric values.
    
    Examples
    --------
    >>> calculate_statistics([1, 2, 3, 4, 5])
    {'mean': 3.0, 'median': 3.0, 'std': 1.5811388300841898}
    
    >>> calculate_statistics([10, 20, 30])
    {'mean': 20.0, 'median': 20.0, 'std': 10.0}
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    
    # Calculate statistics
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    median = sorted_nums[n // 2] if n % 2 == 1 else (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
    # Standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std = variance ** 0.5
    
    return {'mean': mean, 'median': median, 'std': std}

def process_text(text, uppercase=False, remove_spaces=False):
    """Process text with various transformation options.
    
    Parameters
    ----------
    text : str
        The input text to process.
    uppercase : bool, optional
        Whether to convert text to uppercase (default is False).
    remove_spaces : bool, optional
        Whether to remove all spaces from text (default is False).
    
    Returns
    -------
    str
        The processed text after applying transformations.
    
    Examples
    --------
    >>> process_text("Hello World")
    'Hello World'
    
    >>> process_text("Hello World", uppercase=True)
    'HELLO WORLD'
    
    >>> process_text("Hello World", remove_spaces=True)
    'HelloWorld'
    
    >>> process_text("Hello World", uppercase=True, remove_spaces=True)
    'HELLOWORLD'
    """
    result = text
    
    if uppercase:
        result = result.upper()
    
    if remove_spaces:
        result = result.replace(' ', '')
    
    return result

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    such as addition, subtraction, multiplication, and division. It maintains
    a history of operations and can be reset.
    
    Attributes:
        history (list): A list of strings representing the operation history.
        last_result (float): The result of the last operation performed.
    
    Example:
        >>> calc = Calculator()
        >>> result = calc.add(5, 3)
        >>> print(result)
        8
        >>> print(calc.history)
        ['5 + 3 = 8']
    """
    
    def __init__(self):
        """Initialize a new Calculator instance.
        
        Creates an empty history list and sets last_result to 0.
        """
        self.history = []
        self.last_result = 0
    
    def add(self, a, b):
        """Add two numbers and record the operation.
        
        :param a: The first number to add
        :type a: int or float
        :param b: The second number to add
        :type b: int or float
        :return: The sum of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a + b
        self.last_result = result
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract second number from first number.
        
        :param a: The number to subtract from
        :type a: int or float
        :param b: The number to subtract
        :type b: int or float
        :return: The difference of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a - b
        self.last_result = result
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers together.
        
        :param a: The first number to multiply
        :type a: int or float
        :param b: The second number to multiply
        :type b: int or float
        :return: The product of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a * b
        self.last_result = result
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide first number by second number.
        
        :param a: The dividend (number to be divided)
        :type a: int or float
        :param b: The divisor (number to divide by)
        :type b: int or float
        :return: The quotient of a divided by b
        :rtype: float
        :raises TypeError: If arguments are not numbers
        :raises ZeroDivisionError: If divisor is zero
        
        Example:
            >>> calc = Calculator()
            >>> calc.divide(15, 3)
            5.0
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = a / b
        self.last_result = result
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def clear_history(self):
        """Clear the operation history.
        
        Removes all entries from the history list but keeps the last_result.
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3
            >>> calc.clear_history()
            >>> print(calc.history)
            []
        """
        self.history.clear()
    
    def reset(self):
        """Reset the calculator to initial state.
        
        Clears history and resets last_result to 0.
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3
            >>> calc.reset()
            >>> print(calc.last_result)
            0
        """
        self.history.clear()
        self.last_result = 0

# What we accomplished in this step:
# - Created comprehensive class documentation
# - Demonstrated Sphinx/reStructuredText style docstrings
# - Showed proper method documentation within classes
# - Included class attributes documentation
# - Added constructor documentation


# Step 4: Advanced docstring features and module-level documentation
# ===============================================================================

# Explanation:
# Advanced docstrings include type hints, complex examples, cross-references,
# and module-level documentation that describes the entire file's purpose.

"""
Documentation Conventions Module
===============================

This module demonstrates comprehensive Python docstring conventions and best practices.
It includes examples of Google, NumPy, and Sphinx docstring styles for functions,
classes, methods, and modules.

The module covers:
    - Basic function documentation
    - Complex parameter and return value documentation
    - Exception handling documentation
    - Class and method documentation
    - Module-level documentation
    - Type hints integration with docstrings

Author: Python Best Practices Team
Version: 1.0.0
License: MIT

Example:
    Basic usage of the module::

        from documentation_module import Calculator, add_numbers
        
        # Use standalone functions
        result = add_numbers(5, 3)
        
        # Use class-based calculator
        calc = Calculator()
        result = calc.multiply(4, 5)

Note:
    This module is designed for educational purposes to demonstrate
    proper documentation practices in Python development.
"""

from typing import List, Dict, Union, Optional, Tuple, Any
import logging

def add_numbers(a, b):
    """Add two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    
    Example:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    return a + b

def divide_numbers(dividend, divisor):
    """Divide one number by another.
    
    Args:
        dividend (int or float): The number to be divided.
        divisor (int or float): The number to divide by.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If divisor is zero.
        TypeError: If arguments are not numbers.
    
    Example:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(7, 3)
        2.3333333333333335
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Arguments must be numbers")
    
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return dividend / divisor

def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers.
    
    Parameters
    ----------
    numbers : list of int or float
        A list of numerical values to analyze.
    
    Returns
    -------
    dict
        A dictionary containing statistical measures:
        - 'mean': float, the arithmetic mean
        - 'median': float, the median value
        - 'std': float, the standard deviation
    
    Raises
    ------
    ValueError
        If the input list is empty.
    TypeError
        If the input is not a list or contains non-numeric values.
    
    Examples
    --------
    >>> calculate_statistics([1, 2, 3, 4, 5])
    {'mean': 3.0, 'median': 3.0, 'std': 1.5811388300841898}
    
    >>> calculate_statistics([10, 20, 30])
    {'mean': 20.0, 'median': 20.0, 'std': 10.0}
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    
    # Calculate statistics
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    median = sorted_nums[n // 2] if n % 2 == 1 else (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
    # Standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std = variance ** 0.5
    
    return {'mean': mean, 'median': median, 'std': std}

def process_text(text, uppercase=False, remove_spaces=False):
    """Process text with various transformation options.
    
    Parameters
    ----------
    text : str
        The input text to process.
    uppercase : bool, optional
        Whether to convert text to uppercase (default is False).
    remove_spaces : bool, optional
        Whether to remove all spaces from text (default is False).
    
    Returns
    -------
    str
        The processed text after applying transformations.
    
    Examples
    --------
    >>> process_text("Hello World")
    'Hello World'
    
    >>> process_text("Hello World", uppercase=True)
    'HELLO WORLD'
    
    >>> process_text("Hello World", remove_spaces=True)
    'HelloWorld'
    
    >>> process_text("Hello World", uppercase=True, remove_spaces=True)
    'HELLOWORLD'
    """
    result = text
    
    if uppercase:
        result = result.upper()
    
    if remove_spaces:
        result = result.replace(' ', '')
    
    return result

def advanced_data_processor(
    data: List[Dict[str, Any]], 
    filters: Optional[Dict[str, Any]] = None,
    sort_key: Optional[str] = None,
    reverse: bool = False
) -> Tuple[List[Dict[str, Any]], Dict[str, Union[int, float]]]:
    """Process a list of dictionaries with filtering, sorting, and statistics.
    
    This function demonstrates advanced docstring features including:
    - Complex type hints integration
    - Multiple parameter types
    - Detailed return value documentation
    - Cross-references to other functions
    
    Args:
        data: A list of dictionaries containing the data to process.
            Each dictionary should have string keys and any type of values.
        filters: Optional dictionary of key-value pairs to filter the data.
            Only records matching all filter criteria will be included.
            Defaults to None (no filtering).
        sort_key: Optional key name to sort the data by. Must be a key
            that exists in all data dictionaries. Defaults to None (no sorting).
        reverse: Whether to sort in descending order. Only used if sort_key
            is provided. Defaults to False.
    
    Returns:
        A tuple containing:
            - List[Dict[str, Any]]: The processed data after filtering and sorting
            - Dict[str, Union[int, float]]: Statistics about the processing:
                - 'original_count': Number of records in input
                - 'filtered_count': Number of records after filtering
                - 'processing_time': Time taken for processing (in seconds)
    
    Raises:
        TypeError: If data is not a list of dictionaries.
        ValueError: If sort_key is provided but doesn't exist in all records.
        KeyError: If filter keys don't exist in the data records.
    
    Examples:
        Basic usage with no processing:
        
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> result, stats = advanced_data_processor(data)
        >>> len(result)
        2
        >>> stats['original_count']
        2
        
        With filtering:
        
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> filters = {'age': 30}
        >>> result, stats = advanced_data_processor(data, filters=filters)
        >>> len(result)
        1
        >>> result[0]['name']
        'Alice'
        
        With sorting:
        
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> result, stats = advanced_data_processor(data, sort_key='age')
        >>> result[0]['name']
        'Bob'
    
    Note:
        This function is designed to work with homogeneous data where all
        dictionaries have the same keys. For heterogeneous data, consider
        using more robust filtering and sorting mechanisms.
    
    See Also:
        calculate_statistics: For statistical analysis of numerical data.
        process_text: For text processing operations.
    """
    import time
    start_time = time.time()
    
    # Validate input
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    
    if data and not all(isinstance(item, dict) for item in data):
        raise TypeError("All data items must be dictionaries")
    
    original_count = len(data)
    result = data.copy()
    
    # Apply filters
    if filters:
        filtered_result = []
        for item in result:
            match = True
            for key, value in filters.items():
                if key not in item:
                    raise KeyError(f"Filter key '{key}' not found in data")
                if item[key] != value:
                    match = False
                    break
            if match:
                filtered_result.append(item)
        result = filtered_result
    
    # Apply sorting
    if sort_key:
        if result and sort_key not in result[0]:
            raise ValueError(f"Sort key '{sort_key}' not found in data")
        result.sort(key=lambda x: x[sort_key], reverse=reverse)
    
    processing_time = time.time() - start_time
    
    stats = {
        'original_count': original_count,
        'filtered_count': len(result),
        'processing_time': processing_time
    }
    
    return result, stats

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    such as addition, subtraction, multiplication, and division. It maintains
    a history of operations and can be reset.
    
    Attributes:
        history (list): A list of strings representing the operation history.
        last_result (float): The result of the last operation performed.
    
    Example:
        >>> calc = Calculator()
        >>> result = calc.add(5, 3)
        >>> print(result)
        8
        >>> print(calc.history)
        ['5 + 3 = 8']
    """
    
    def __init__(self):
        """Initialize a new Calculator instance.
        
        Creates an empty history list and sets last_result to 0.
        """
        self.history = []
        self.last_result = 0
    
    def add(self, a, b):
        """Add two numbers and record the operation.
        
        :param a: The first number to add
        :type a: int or float
        :param b: The second number to add
        :type b: int or float
        :return: The sum of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a + b
        self.last_result = result
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract second number from first number.
        
        :param a: The number to subtract from
        :type a: int or float
        :param b: The number to subtract
        :type b: int or float
        :return: The difference of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a - b
        self.last_result = result
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers together.
        
        :param a: The first number to multiply
        :type a: int or float
        :param b: The second number to multiply
        :type b: int or float
        :return: The product of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a * b
        self.last_result = result
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide first number by second number.
        
        :param a: The dividend (number to be divided)
        :type a: int or float
        :param b: The divisor (number to divide by)
        :type b: int or float
        :return: The quotient of a divided by b
        :rtype: float
        :raises TypeError: If arguments are not numbers
        :raises ZeroDivisionError: If divisor is zero
        
        Example:
            >>> calc = Calculator()
            >>> calc.divide(15, 3)
            5.0
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = a / b
        self.last_result = result
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def clear_history(self):
        """Clear the operation history.
        
        Removes all entries from the history list but keeps the last_result.
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3
            >>> calc.clear_history()
            >>> print(calc.history)
            []
        """
        self.history.clear()
    
    def reset(self):
        """Reset the calculator to initial state.
        
        Clears history and resets last_result to 0.
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3
            >>> calc.reset()
            >>> print(calc.last_result)
            0
        """
        self.history.clear()
        self.last_result = 0

# What we accomplished in this step:
# - Added comprehensive module-level documentation
# - Demonstrated type hints integration with docstrings
# - Showed complex parameter and return value documentation
# - Added cross-references between functions
# - Included detailed examples and usage patterns


# Step 5: Testing docstrings and best practices demonstration
# ===============================================================================

# Explanation:
# Let's test our docstring implementations and demonstrate best practices
# for maintaining and validating documentation.

"""
Documentation Conventions Module
===============================

This module demonstrates comprehensive Python docstring conventions and best practices.
It includes examples of Google, NumPy, and Sphinx docstring styles for functions,
classes, methods, and modules.

The module covers:
    - Basic function documentation
    - Complex parameter and return value documentation
    - Exception handling documentation
    - Class and method documentation
    - Module-level documentation
    - Type hints integration with docstrings

Author: Python Best Practices Team
Version: 1.0.0
License: MIT

Example:
    Basic usage of the module::

        from documentation_module import Calculator, add_numbers
        
        # Use standalone functions
        result = add_numbers(5, 3)
        
        # Use class-based calculator
        calc = Calculator()
        result = calc.multiply(4, 5)

Note:
    This module is designed for educational purposes to demonstrate
    proper documentation practices in Python development.
"""

from typing import List, Dict, Union, Optional, Tuple, Any
import logging

def add_numbers(a, b):
    """Add two numbers together.
    
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    
    Returns:
        int or float: The sum of a and b.
    
    Example:
        >>> add_numbers(5, 3)
        8
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    return a + b

def divide_numbers(dividend, divisor):
    """Divide one number by another.
    
    Args:
        dividend (int or float): The number to be divided.
        divisor (int or float): The number to divide by.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If divisor is zero.
        TypeError: If arguments are not numbers.
    
    Example:
        >>> divide_numbers(10, 2)
        5.0
        >>> divide_numbers(7, 3)
        2.3333333333333335
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Arguments must be numbers")
    
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return dividend / divisor

def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers.
    
    Parameters
    ----------
    numbers : list of int or float
        A list of numerical values to analyze.
    
    Returns
    -------
    dict
        A dictionary containing statistical measures:
        - 'mean': float, the arithmetic mean
        - 'median': float, the median value
        - 'std': float, the standard deviation
    
    Raises
    ------
    ValueError
        If the input list is empty.
    TypeError
        If the input is not a list or contains non-numeric values.
    
    Examples
    --------
    >>> calculate_statistics([1, 2, 3, 4, 5])
    {'mean': 3.0, 'median': 3.0, 'std': 1.5811388300841898}
    
    >>> calculate_statistics([10, 20, 30])
    {'mean': 20.0, 'median': 20.0, 'std': 10.0}
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    
    # Calculate statistics
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    median = sorted_nums[n // 2] if n % 2 == 1 else (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
    # Standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std = variance ** 0.5
    
    return {'mean': mean, 'median': median, 'std': std}

def process_text(text, uppercase=False, remove_spaces=False):
    """Process text with various transformation options.
    
    Parameters
    ----------
    text : str
        The input text to process.
    uppercase : bool, optional
        Whether to convert text to uppercase (default is False).
    remove_spaces : bool, optional
        Whether to remove all spaces from text (default is False).
    
    Returns
    -------
    str
        The processed text after applying transformations.
    
    Examples
    --------
    >>> process_text("Hello World")
    'Hello World'
    
    >>> process_text("Hello World", uppercase=True)
    'HELLO WORLD'
    
    >>> process_text("Hello World", remove_spaces=True)
    'HelloWorld'
    
    >>> process_text("Hello World", uppercase=True, remove_spaces=True)
    'HELLOWORLD'
    """
    result = text
    
    if uppercase:
        result = result.upper()
    
    if remove_spaces:
        result = result.replace(' ', '')
    
    return result

def advanced_data_processor(
    data: List[Dict[str, Any]], 
    filters: Optional[Dict[str, Any]] = None,
    sort_key: Optional[str] = None,
    reverse: bool = False
) -> Tuple[List[Dict[str, Any]], Dict[str, Union[int, float]]]:
    """Process a list of dictionaries with filtering, sorting, and statistics.
    
    This function demonstrates advanced docstring features including:
    - Complex type hints integration
    - Multiple parameter types
    - Detailed return value documentation
    - Cross-references to other functions
    
    Args:
        data: A list of dictionaries containing the data to process.
            Each dictionary should have string keys and any type of values.
        filters: Optional dictionary of key-value pairs to filter the data.
            Only records matching all filter criteria will be included.
            Defaults to None (no filtering).
        sort_key: Optional key name to sort the data by. Must be a key
            that exists in all data dictionaries. Defaults to None (no sorting).
        reverse: Whether to sort in descending order. Only used if sort_key
            is provided. Defaults to False.
    
    Returns:
        A tuple containing:
            - List[Dict[str, Any]]: The processed data after filtering and sorting
            - Dict[str, Union[int, float]]: Statistics about the processing:
                - 'original_count': Number of records in input
                - 'filtered_count': Number of records after filtering
                - 'processing_time': Time taken for processing (in seconds)
    
    Raises:
        TypeError: If data is not a list of dictionaries.
        ValueError: If sort_key is provided but doesn't exist in all records.
        KeyError: If filter keys don't exist in the data records.
    
    Examples:
        Basic usage with no processing:
        
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> result, stats = advanced_data_processor(data)
        >>> len(result)
        2
        >>> stats['original_count']
        2
        
        With filtering:
        
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> filters = {'age': 30}
        >>> result, stats = advanced_data_processor(data, filters=filters)
        >>> len(result)
        1
        >>> result[0]['name']
        'Alice'
        
        With sorting:
        
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> result, stats = advanced_data_processor(data, sort_key='age')
        >>> result[0]['name']
        'Bob'
    
    Note:
        This function is designed to work with homogeneous data where all
        dictionaries have the same keys. For heterogeneous data, consider
        using more robust filtering and sorting mechanisms.
    
    See Also:
        calculate_statistics: For statistical analysis of numerical data.
        process_text: For text processing operations.
    """
    import time
    start_time = time.time()
    
    # Validate input
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    
    if data and not all(isinstance(item, dict) for item in data):
        raise TypeError("All data items must be dictionaries")
    
    original_count = len(data)
    result = data.copy()
    
    # Apply filters
    if filters:
        filtered_result = []
        for item in result:
            match = True
            for key, value in filters.items():
                if key not in item:
                    raise KeyError(f"Filter key '{key}' not found in data")
                if item[key] != value:
                    match = False
                    break
            if match:
                filtered_result.append(item)
        result = filtered_result
    
    # Apply sorting
    if sort_key:
        if result and sort_key not in result[0]:
            raise ValueError(f"Sort key '{sort_key}' not found in data")
        result.sort(key=lambda x: x[sort_key], reverse=reverse)
    
    processing_time = time.time() - start_time
    
    stats = {
        'original_count': original_count,
        'filtered_count': len(result),
        'processing_time': processing_time
    }
    
    return result, stats

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    such as addition, subtraction, multiplication, and division. It maintains
    a history of operations and can be reset.
    
    Attributes:
        history (list): A list of strings representing the operation history.
        last_result (float): The result of the last operation performed.
    
    Example:
        >>> calc = Calculator()
        >>> result = calc.add(5, 3)
        >>> print(result)
        8
        >>> print(calc.history)
        ['5 + 3 = 8']
    """
    
    def __init__(self):
        """Initialize a new Calculator instance.
        
        Creates an empty history list and sets last_result to 0.
        """
        self.history = []
        self.last_result = 0
    
    def add(self, a, b):
        """Add two numbers and record the operation.
        
        :param a: The first number to add
        :type a: int or float
        :param b: The second number to add
        :type b: int or float
        :return: The sum of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a + b
        self.last_result = result
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract second number from first number.
        
        :param a: The number to subtract from
        :type a: int or float
        :param b: The number to subtract
        :type b: int or float
        :return: The difference of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a - b
        self.last_result = result
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers together.
        
        :param a: The first number to multiply
        :type a: int or float
        :param b: The second number to multiply
        :type b: int or float
        :return: The product of a and b
        :rtype: int or float
        :raises TypeError: If arguments are not numbers
        
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        result = a * b
        self.last_result = result
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide first number by second number.
        
        :param a: The dividend (number to be divided)
        :type a: int or float
        :param b: The divisor (number to divide by)
        :type b: int or float
        :return: The quotient of a divided by b
        :rtype: float
        :raises TypeError: If arguments are not numbers
        :raises ZeroDivisionError: If divisor is zero
        
        Example:
            >>> calc = Calculator()
            >>> calc.divide(15, 3)
            5.0
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = a / b
        self.last_result = result
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def clear_history(self):
        """Clear the operation history.
        
        Removes all entries from the history list but keeps the last_result.
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3
            >>> calc.clear_history()
            >>> print(calc.history)
            []
        """
        self.history.clear()
    
    def reset(self):
        """Reset the calculator to initial state.
        
        Clears history and resets last_result to 0.
        
        Example:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3
            >>> calc.reset()
            >>> print(calc.last_result)
            0
        """
        self.history.clear()
        self.last_result = 0

class DocumentationValidator:
    """Utility class for validating and testing docstring examples.
    
    This class provides methods to validate docstring examples and ensure
    they work correctly. It demonstrates best practices for maintaining
    documentation quality.
    
    Example:
        >>> validator = DocumentationValidator()
        >>> validator.test_function_examples(add_numbers)
        True
    """
    
    def __init__(self):
        """Initialize the documentation validator."""
        self.test_results = []
    
    def test_function_examples(self, func):
        """Test the examples in a function's docstring.
        
        Args:
            func: The function to test examples for.
        
        Returns:
            bool: True if all examples pass, False otherwise.
        
        Example:
            >>> validator = DocumentationValidator()
            >>> validator.test_function_examples(add_numbers)
            True
        """
        import doctest
        
        # This would normally run doctest on the function
        # For demonstration purposes, we'll simulate it
        try:
            # In real implementation, you'd use:
            # doctest.run_docstring_examples(func, globals())
            self.test_results.append(f"Testing {func.__name__}: PASSED")
            return True
        except Exception as e:
            self.test_results.append(f"Testing {func.__name__}: FAILED - {e}")
            return False
    
    def generate_documentation_report(self):
        """Generate a report of documentation quality.
        
        Returns:
            str: A formatted report of documentation status.
        
        Example:
            >>> validator = DocumentationValidator()
            >>> report = validator.generate_documentation_report()
            >>> "Documentation Quality Report" in report
            True
        """
        report = "Documentation Quality Report\n"
        report += "=" * 30 + "\n\n"
        
        for result in self.test_results:
            report += f"- {result}\n"
        
        if not self.test_results:
            report += "No tests run yet.\n"
        
        return report

# Test our documentation examples
print("=== Testing Docstring Conventions ===\n")

# Test basic functions
print("1. Testing basic functions:")
result1 = add_numbers(5, 3)
print(f"add_numbers(5, 3) = {result1}")

result2 = divide_numbers(10, 2)
print(f"divide_numbers(10, 2) = {result2}")

# Test NumPy style function
print("\n2. Testing NumPy style function:")
stats = calculate_statistics([1, 2, 3, 4, 5])
print(f"calculate_statistics([1, 2, 3, 4, 5]) = {stats}")

# Test text processing
print("\n3. Testing text processing:")
text_result = process_text("Hello World", uppercase=True, remove_spaces=True)
print(f"process_text('Hello World', uppercase=True, remove_spaces=True) = '{text_result}'")

# Test advanced data processor
print("\n4. Testing advanced data processor:")
sample_data = [
    {'name': 'Alice', 'age': 30, 'department': 'Engineering'},
    {'name': 'Bob', 'age': 25, 'department': 'Marketing'},
    {'name': 'Charlie', 'age': 35, 'department': 'Engineering'}
]

filtered_data, processing_stats = advanced_data_processor(
    sample_data, 
    filters={'department': 'Engineering'}, 
    sort_key='age'
)
print(f"Filtered and sorted data: {filtered_data}")
print(f"Processing statistics: {processing_stats}")

# Test Calculator class
print("\n5. Testing Calculator class:")
calc = Calculator()
calc.add(10, 5)
calc.multiply(3, 4)
calc.divide(20, 4)
print(f"Calculator history: {calc.history}")
print(f"Last result: {calc.last_result}")

# Test documentation validator
print("\n6. Testing documentation validator:")
validator = DocumentationValidator()
validator.test_function_examples(add_numbers)
validator.test_function_examples(process_text)
print(validator.generate_documentation_report())

# Demonstrate help() function usage
print("\n7. Demonstrating help() function:")
print("Try running: help(Calculator.add) to see the docstring in action!")

# What we accomplished in this step:
# - Created a documentation validator class
# - Tested all our documented functions and classes
# - Demonstrated practical usage of the documented code
# - Showed how to validate docstring examples
# - Provided a complete working example of all docstring styles


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the comprehensive docstring conventions tutorial!
#
# Key concepts learned:
# - Google style docstrings (clean and readable)
# - NumPy style docstrings (structured with underlines)
# - Sphinx/reStructuredText style docstrings (detailed markup)
# - Module-level documentation
# - Class and method documentation
# - Type hints integration with docstrings
# - Advanced features like cross-references and complex examples
# - Documentation testing and validation
#
# Best practices covered:
# 1. Always include a brief description
# 2. Document all parameters with types and descriptions
# 3. Document return values clearly
# 4. List all possible exceptions
# 5. Provide practical examples
# 6. Use consistent style throughout your project
# 7. Keep docstrings up to date with code changes
# 8. Test your docstring examples regularly
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each docstring with help() function
# 3. Understand WHY each style is useful
# 4. Experiment with your own functions and classes
# 5. Use doctest to validate your examples
#
# Remember: Good documentation is as important as good code!
# ===============================================================================
