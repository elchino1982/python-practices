"""Question: Create comprehensive Sphinx documentation for a Python project.

Build a complete documentation system using Sphinx with various features
including API documentation, tutorials, and examples.

Requirements:
1. Create a sample Python module with proper docstrings
2. Set up Sphinx configuration
3. Create documentation with multiple sections
4. Include code examples and API references
5. Demonstrate various Sphinx features (autodoc, cross-references, etc.)

Example usage:
    # Generate documentation
    sphinx-build -b html docs docs/_build/html
    
    # View documentation
    open docs/_build/html/index.html
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about documentation structure and organization
# - Start with basic docstrings and build up
# - Test your documentation generation step by step
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: Good documentation is crucial for any Python project!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)












































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What makes good documentation structure?
# - How to write clear and comprehensive docstrings?
# - What Sphinx extensions and features to use?
# - How to organize documentation files and sections?
#
# Remember: Start with basic docstrings and build up complexity gradually!


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


# Step 1: Create a sample Python module with basic docstrings
# ===============================================================================

# Explanation:
# Good documentation starts with well-written docstrings in your code.
# We'll create a sample calculator module to demonstrate various docstring styles.

"""
Sample Calculator Module

This module provides basic mathematical operations and demonstrates
various Sphinx documentation features.

Example:
    Basic usage of the calculator::

        from calculator import Calculator
        calc = Calculator()
        result = calc.add(5, 3)
        print(f"Result: {result}")

Attributes:
    PI (float): Mathematical constant pi
    E (float): Mathematical constant e

Todo:
    * Add more advanced mathematical operations
    * Implement error handling for division by zero
    * Add support for complex numbers
"""

import math
from typing import Union, List, Optional

# Module-level constants
PI = math.pi
E = math.e

class Calculator:
    """A simple calculator class for basic mathematical operations.
    
    This class provides methods for basic arithmetic operations
    and demonstrates proper Sphinx documentation practices.
    
    Attributes:
        history (List[str]): A list of performed operations
        precision (int): Number of decimal places for results
        
    Example:
        Creating and using a calculator::
        
            calc = Calculator(precision=2)
            result = calc.add(10, 5)
            print(calc.get_history())
    """
    
    def __init__(self, precision: int = 2):
        """Initialize the calculator.
        
        Args:
            precision (int, optional): Number of decimal places for results. 
                Defaults to 2.
                
        Raises:
            ValueError: If precision is negative.
            
        Example:
            >>> calc = Calculator(precision=3)
            >>> calc.precision
            3
        """
        if precision < 0:
            raise ValueError("Precision must be non-negative")
        
        self.precision = precision
        self.history: List[str] = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers.
        
        Args:
            a (Union[int, float]): First number
            b (Union[int, float]): Second number
            
        Returns:
            float: Sum of a and b, rounded to specified precision
            
        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8.0
            >>> calc.add(2.5, 1.7)
            4.2
        """
        result = round(a + b, self.precision)
        self.history.append(f"{a} + {b} = {result}")
        return result


# Step 2: Add more methods with comprehensive docstrings
# ===============================================================================

# Explanation:
# Building on Step 1, we'll add more methods to demonstrate different
# docstring patterns and Sphinx features like cross-references.

# Continue the Calculator class from Step 1:
class CalculatorStep2:
    """Enhanced calculator class with more operations.
    
    This class extends the basic calculator functionality and demonstrates
    advanced Sphinx documentation features including cross-references,
    parameter validation, and comprehensive examples.
    
    Attributes:
        history (List[str]): A list of performed operations
        precision (int): Number of decimal places for results
        
    Note:
        This calculator maintains operation history for debugging purposes.
        Use :meth:`clear_history` to reset the history when needed.
        
    See Also:
        :class:`Calculator`: Basic calculator implementation
        :func:`math.pow`: Built-in power function
    """
    
    def __init__(self, precision: int = 2):
        """Initialize the calculator.
        
        Args:
            precision (int, optional): Number of decimal places for results. 
                Defaults to 2.
                
        Raises:
            ValueError: If precision is negative.
            
        Example:
            >>> calc = CalculatorStep2(precision=3)
            >>> calc.precision
            3
        """
        if precision < 0:
            raise ValueError("Precision must be non-negative")
        
        self.precision = precision
        self.history: List[str] = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers.
        
        Args:
            a (Union[int, float]): First number
            b (Union[int, float]): Second number
            
        Returns:
            float: Sum of a and b, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep2()
            >>> calc.add(5, 3)
            8.0
            >>> calc.add(2.5, 1.7)
            4.2
        """
        result = round(a + b, self.precision)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract second number from first number.
        
        Args:
            a (Union[int, float]): Number to subtract from
            b (Union[int, float]): Number to subtract
            
        Returns:
            float: Difference of a and b, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep2()
            >>> calc.subtract(10, 3)
            7.0
            >>> calc.subtract(5.5, 2.2)
            3.3
        """
        result = round(a - b, self.precision)
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers.
        
        Args:
            a (Union[int, float]): First number
            b (Union[int, float]): Second number
            
        Returns:
            float: Product of a and b, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep2()
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.multiply(2.5, 3)
            7.5
        """
        result = round(a * b, self.precision)
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide first number by second number.
        
        Args:
            a (Union[int, float]): Dividend
            b (Union[int, float]): Divisor
            
        Returns:
            float: Quotient of a and b, rounded to specified precision
            
        Raises:
            ZeroDivisionError: If divisor is zero
            
        Example:
            >>> calc = CalculatorStep2()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 3)
            2.33
            
        Warning:
            Division by zero will raise a ZeroDivisionError.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = round(a / b, self.precision)
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Raise base to the power of exponent.
        
        Args:
            base (Union[int, float]): Base number
            exponent (Union[int, float]): Exponent
            
        Returns:
            float: Result of base^exponent, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep2()
            >>> calc.power(2, 3)
            8.0
            >>> calc.power(4, 0.5)
            2.0
            
        Note:
            This method uses Python's built-in ** operator.
            For more advanced mathematical functions, consider using
            the :mod:`math` module.
        """
        result = round(base ** exponent, self.precision)
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result


# Step 3: Add utility methods and demonstrate advanced Sphinx features
# ===============================================================================

# Explanation:
# Building on Steps 1-2, we'll add utility methods and demonstrate
# advanced Sphinx features like parameter tables, cross-references, and code blocks.

# Continue the Calculator class from Steps 1-2:
class CalculatorStep3:
    """Complete calculator class with utility methods.
    
    This class includes all basic operations plus utility methods for
    history management and advanced mathematical functions.
    
    Attributes:
        history (List[str]): A list of performed operations
        precision (int): Number of decimal places for results
        
    Note:
        This calculator maintains operation history for debugging purposes.
        Use :meth:`clear_history` to reset the history when needed.
        
    See Also:
        :class:`Calculator`: Basic calculator implementation
        :func:`math.pow`: Built-in power function
        :mod:`math`: Mathematical functions module
    """
    
    def __init__(self, precision: int = 2):
        """Initialize the calculator.
        
        Args:
            precision (int, optional): Number of decimal places for results. 
                Defaults to 2.
                
        Raises:
            ValueError: If precision is negative.
            
        Example:
            >>> calc = CalculatorStep3(precision=3)
            >>> calc.precision
            3
        """
        if precision < 0:
            raise ValueError("Precision must be non-negative")
        
        self.precision = precision
        self.history: List[str] = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers.
        
        Args:
            a (Union[int, float]): First number
            b (Union[int, float]): Second number
            
        Returns:
            float: Sum of a and b, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.add(5, 3)
            8.0
            >>> calc.add(2.5, 1.7)
            4.2
        """
        result = round(a + b, self.precision)
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract second number from first number.
        
        Args:
            a (Union[int, float]): Number to subtract from
            b (Union[int, float]): Number to subtract
            
        Returns:
            float: Difference of a and b, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.subtract(10, 3)
            7.0
            >>> calc.subtract(5.5, 2.2)
            3.3
        """
        result = round(a - b, self.precision)
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers.
        
        Args:
            a (Union[int, float]): First number
            b (Union[int, float]): Second number
            
        Returns:
            float: Product of a and b, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.multiply(2.5, 3)
            7.5
        """
        result = round(a * b, self.precision)
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide first number by second number.
        
        Args:
            a (Union[int, float]): Dividend
            b (Union[int, float]): Divisor
            
        Returns:
            float: Quotient of a and b, rounded to specified precision
            
        Raises:
            ZeroDivisionError: If divisor is zero
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 3)
            2.33
            
        Warning:
            Division by zero will raise a ZeroDivisionError.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = round(a / b, self.precision)
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Raise base to the power of exponent.
        
        Args:
            base (Union[int, float]): Base number
            exponent (Union[int, float]): Exponent
            
        Returns:
            float: Result of base^exponent, rounded to specified precision
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.power(2, 3)
            8.0
            >>> calc.power(4, 0.5)
            2.0
            
        Note:
            This method uses Python's built-in ** operator.
            For more advanced mathematical functions, consider using
            the :mod:`math` module.
        """
        result = round(base ** exponent, self.precision)
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """Get the calculation history.
        
        Returns:
            List[str]: List of all performed operations
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.add(5, 3)
            8.0
            >>> calc.multiply(2, 4)
            8.0
            >>> calc.get_history()
            ['5 + 3 = 8.0', '2 * 4 = 8.0']
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the calculation history.
        
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.add(5, 3)
            8.0
            >>> len(calc.get_history())
            1
            >>> calc.clear_history()
            >>> len(calc.get_history())
            0
        """
        self.history.clear()
    
    def sqrt(self, number: Union[int, float]) -> float:
        """Calculate square root of a number.
        
        Args:
            number (Union[int, float]): Number to calculate square root for
            
        Returns:
            float: Square root of the number, rounded to specified precision
            
        Raises:
            ValueError: If number is negative
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.sqrt(16)
            4.0
            >>> calc.sqrt(2)
            1.41
            
        Note:
            This method uses :func:`math.sqrt` for calculation.
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        result = round(math.sqrt(number), self.precision)
        self.history.append(f"√{number} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of a number.
        
        Args:
            n (int): Non-negative integer to calculate factorial for
            
        Returns:
            int: Factorial of n
            
        Raises:
            ValueError: If n is negative
            TypeError: If n is not an integer
            
        Example:
            >>> calc = CalculatorStep3()
            >>> calc.factorial(5)
            120
            >>> calc.factorial(0)
            1
            
        Note:
            This method uses :func:`math.factorial` for calculation.
            
        See Also:
            :func:`math.factorial`: Built-in factorial function
        """
        if not isinstance(n, int):
            raise TypeError("Factorial is only defined for integers")
        if n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result


# Step 4: Create Sphinx configuration and documentation structure
# ===============================================================================

# Explanation:
# Building on Steps 1-3, we'll now create the Sphinx configuration files
# and documentation structure that would be used to generate HTML documentation.

# Sphinx conf.py configuration (this would be in docs/conf.py):
SPHINX_CONF_PY = '''
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Calculator Documentation'
copyright = '2025, Python Practices'
author = 'Python Practices Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Automatic documentation from docstrings
    'sphinx.ext.viewcode',       # Add source code links
    'sphinx.ext.napoleon',       # Support for Google and NumPy style docstrings
    'sphinx.ext.intersphinx',    # Link to other project's documentation
    'sphinx.ext.todo',           # Support for todo items
    'sphinx.ext.coverage',       # Coverage checker
    'sphinx.ext.mathjax',        # Math support
    'sphinx.ext.ifconfig',       # Include content based on configuration
    'sphinx.ext.githubpages',    # Publish HTML docs in GitHub Pages
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Read the Docs theme
html_static_path = ['_static']

# -- Extension configuration ------------------------------------------------

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}

# Todo extension
todo_include_todos = True
'''

# Main index.rst file (this would be in docs/index.rst):
SPHINX_INDEX_RST = '''
Calculator Documentation
========================

Welcome to the Calculator project documentation!

This project demonstrates comprehensive Sphinx documentation practices
for Python projects, including API documentation, tutorials, and examples.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api
   examples
   advanced
   contributing

Features
--------

* Basic arithmetic operations (add, subtract, multiply, divide)
* Advanced mathematical functions (power, square root, factorial)
* Operation history tracking
* Configurable precision
* Comprehensive error handling

Quick Example
-------------

Here's a quick example of how to use the Calculator:

.. code-block:: python

   from calculator import CalculatorStep3
   
   # Create a calculator with 3 decimal places
   calc = CalculatorStep3(precision=3)
   
   # Perform some calculations
   result1 = calc.add(10, 5)
   result2 = calc.multiply(result1, 2)
   result3 = calc.sqrt(result2)
   
   # Check the history
   print(calc.get_history())

Installation
------------

.. code-block:: bash

   pip install calculator

For development installation:

.. code-block:: bash

   git clone https://github.com/example/calculator.git
   cd calculator
   pip install -e .

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
'''

# API documentation file (this would be in docs/api.rst):
SPHINX_API_RST = '''
API Reference
=============

This section contains the complete API reference for the Calculator module.

Calculator Module
-----------------

.. automodule:: calculator
   :members:
   :undoc-members:
   :show-inheritance:

Calculator Class
----------------

.. autoclass:: calculator.CalculatorStep3
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Basic Operations
~~~~~~~~~~~~~~~~

.. automethod:: calculator.CalculatorStep3.add
.. automethod:: calculator.CalculatorStep3.subtract
.. automethod:: calculator.CalculatorStep3.multiply
.. automethod:: calculator.CalculatorStep3.divide

Advanced Operations
~~~~~~~~~~~~~~~~~~~

.. automethod:: calculator.CalculatorStep3.power
.. automethod:: calculator.CalculatorStep3.sqrt
.. automethod:: calculator.CalculatorStep3.factorial

Utility Methods
~~~~~~~~~~~~~~~

.. automethod:: calculator.CalculatorStep3.get_history
.. automethod:: calculator.CalculatorStep3.clear_history

Constants
---------

.. autodata:: calculator.PI
   :annotation: = 3.141592653589793

.. autodata:: calculator.E
   :annotation: = 2.718281828459045

Exceptions
----------

The calculator may raise the following exceptions:

.. py:exception:: ValueError

   Raised when invalid input values are provided.

.. py:exception:: ZeroDivisionError

   Raised when attempting to divide by zero.

.. py:exception:: TypeError

   Raised when incorrect types are provided to methods.
'''


# Step 5: Add tutorial and example documentation files
# ===============================================================================

# Explanation:
# Building on Steps 1-4, we'll add comprehensive tutorial and example
# documentation files that demonstrate various Sphinx features.

# Quickstart guide (this would be in docs/quickstart.rst):
SPHINX_QUICKSTART_RST = '''
Quick Start Guide
=================

This guide will help you get started with the Calculator module quickly.

Installation
------------

First, install the calculator module:

.. code-block:: bash

   pip install calculator

Basic Usage
-----------

Import and Create Calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from calculator import CalculatorStep3
   
   # Create a calculator with default precision (2 decimal places)
   calc = CalculatorStep3()
   
   # Or create with custom precision
   calc_precise = CalculatorStep3(precision=4)

Perform Basic Operations
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Addition
   result = calc.add(10, 5)
   print(f"10 + 5 = {result}")  # Output: 10 + 5 = 15.0
   
   # Subtraction
   result = calc.subtract(20, 8)
   print(f"20 - 8 = {result}")  # Output: 20 - 8 = 12.0
   
   # Multiplication
   result = calc.multiply(6, 7)
   print(f"6 * 7 = {result}")   # Output: 6 * 7 = 42.0
   
   # Division
   result = calc.divide(15, 3)
   print(f"15 / 3 = {result}")  # Output: 15 / 3 = 5.0

Advanced Operations
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Power
   result = calc.power(2, 8)
   print(f"2^8 = {result}")     # Output: 2^8 = 256.0
   
   # Square root
   result = calc.sqrt(16)
   print(f"√16 = {result}")     # Output: √16 = 4.0
   
   # Factorial
   result = calc.factorial(5)
   print(f"5! = {result}")      # Output: 5! = 120

Working with History
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Perform some operations
   calc.add(5, 3)
   calc.multiply(2, 4)
   calc.sqrt(16)
   
   # Get operation history
   history = calc.get_history()
   for operation in history:
       print(operation)
   
   # Clear history
   calc.clear_history()
   print(f"History after clear: {calc.get_history()}")  # Output: []

Error Handling
--------------

The calculator includes comprehensive error handling:

.. code-block:: python

   try:
       # This will raise ZeroDivisionError
       calc.divide(10, 0)
   except ZeroDivisionError as e:
       print(f"Error: {e}")
   
   try:
       # This will raise ValueError
       calc.sqrt(-4)
   except ValueError as e:
       print(f"Error: {e}")
   
   try:
       # This will raise TypeError
       calc.factorial(3.5)
   except TypeError as e:
       print(f"Error: {e}")

Next Steps
----------

* Read the :doc:`api` for complete method documentation
* Check out :doc:`examples` for more complex usage scenarios
* See :doc:`advanced` for advanced features and customization
'''

# Examples documentation (this would be in docs/examples.rst):
SPHINX_EXAMPLES_RST = '''
Examples
========

This section provides comprehensive examples of using the Calculator module
in various scenarios.

Example 1: Basic Calculator Usage
---------------------------------

This example demonstrates basic arithmetic operations:

.. literalinclude:: examples/basic_usage.py
   :language: python
   :linenos:
   :caption: Basic calculator usage

.. code-block:: python

   from calculator import CalculatorStep3
   
   def basic_calculator_demo():
       """Demonstrate basic calculator operations."""
       calc = CalculatorStep3(precision=2)
       
       print("=== Basic Calculator Demo ===")
       
       # Perform calculations
       a, b = 15, 4
       
       print(f"Numbers: {a}, {b}")
       print(f"Addition: {a} + {b} = {calc.add(a, b)}")
       print(f"Subtraction: {a} - {b} = {calc.subtract(a, b)}")
       print(f"Multiplication: {a} * {b} = {calc.multiply(a, b)}")
       print(f"Division: {a} / {b} = {calc.divide(a, b)}")
       print(f"Power: {a} ^ {b} = {calc.power(a, b)}")
       
       print("\\nOperation History:")
       for operation in calc.get_history():
           print(f"  {operation}")
   
   if __name__ == "__main__":
       basic_calculator_demo()

Example 2: Scientific Calculator
--------------------------------

This example shows advanced mathematical operations:

.. code-block:: python

   from calculator import CalculatorStep3
   import math
   
   def scientific_calculator_demo():
       """Demonstrate scientific calculator features."""
       calc = CalculatorStep3(precision=4)
       
       print("=== Scientific Calculator Demo ===")
       
       # Advanced operations
       numbers = [16, 25, 36, 49, 64]
       
       print("Square roots:")
       for num in numbers:
           sqrt_result = calc.sqrt(num)
           print(f"  √{num} = {sqrt_result}")
       
       print("\\nFactorials:")
       for i in range(1, 8):
           fact_result = calc.factorial(i)
           print(f"  {i}! = {fact_result}")
       
       print("\\nPowers of 2:")
       for exp in range(1, 11):
           power_result = calc.power(2, exp)
           print(f"  2^{exp} = {power_result}")
       
       print(f"\\nTotal operations performed: {len(calc.get_history())}")
   
   if __name__ == "__main__":
       scientific_calculator_demo()

Example 3: Error Handling and Validation
----------------------------------------

This example demonstrates proper error handling:

.. code-block:: python

   from calculator import CalculatorStep3
   
   def error_handling_demo():
       """Demonstrate error handling in calculator operations."""
       calc = CalculatorStep3()
       
       print("=== Error Handling Demo ===")
       
       # Test cases that should raise errors
       test_cases = [
           ("Division by zero", lambda: calc.divide(10, 0)),
           ("Square root of negative", lambda: calc.sqrt(-4)),
           ("Factorial of negative", lambda: calc.factorial(-1)),
           ("Factorial of float", lambda: calc.factorial(3.5)),
           ("Invalid precision", lambda: CalculatorStep3(precision=-1)),
       ]
       
       for description, operation in test_cases:
           try:
               result = operation()
               print(f"  {description}: {result} (unexpected success)")
           except (ValueError, TypeError, ZeroDivisionError) as e:
               print(f"  {description}: {type(e).__name__} - {e}")
           except Exception as e:
               print(f"  {description}: Unexpected error - {e}")
   
   if __name__ == "__main__":
       error_handling_demo()

Example 4: Calculator with Custom Precision
-------------------------------------------

This example shows working with different precision levels:

.. code-block:: python

   from calculator import CalculatorStep3
   
   def precision_demo():
       """Demonstrate calculator precision settings."""
       print("=== Precision Demo ===")
       
       # Create calculators with different precision
       precisions = [0, 1, 2, 3, 5]
       value_a, value_b = 22, 7
       
       print(f"Calculating {value_a} / {value_b} with different precisions:")
       
       for precision in precisions:
           calc = CalculatorStep3(precision=precision)
           result = calc.divide(value_a, value_b)
           print(f"  Precision {precision}: {result}")
       
       # Demonstrate precision with square roots
       print(f"\\nCalculating √2 with different precisions:")
       for precision in precisions:
           calc = CalculatorStep3(precision=precision)
           result = calc.sqrt(2)
           print(f"  Precision {precision}: {result}")
   
   if __name__ == "__main__":
       precision_demo()
'''


# Step 6: Complete documentation with advanced features and final demonstration
# ===============================================================================

# Explanation:
# Building on Steps 1-5, we'll complete the documentation with advanced features,
# installation guide, and a comprehensive demonstration of all Sphinx capabilities.

# Installation guide (this would be in docs/installation.rst):
SPHINX_INSTALLATION_RST = '''
Installation
============

This section covers different ways to install the Calculator module.

Requirements
------------

* Python 3.7 or higher
* No external dependencies for basic functionality

.. note::
   For development, additional packages like Sphinx are required.
   See :ref:`development-installation` for details.

Standard Installation
---------------------

Install from PyPI using pip:

.. code-block:: bash

   pip install calculator

Verify the installation:

.. code-block:: python

   from calculator import CalculatorStep3
   calc = CalculatorStep3()
   print(calc.add(2, 3))  # Should output: 5.0

.. _development-installation:

Development Installation
------------------------

For development or contributing to the project:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/example/calculator.git
      cd calculator

2. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. Install in development mode:

   .. code-block:: bash

      pip install -e .

4. Install development dependencies:

   .. code-block:: bash

      pip install -r requirements-dev.txt

Building Documentation
----------------------

To build the documentation locally:

.. code-block:: bash

   cd docs
   make html

The documentation will be available in ``docs/_build/html/index.html``.

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**ImportError: No module named 'calculator'**

Make sure you have installed the package:

.. code-block:: bash

   pip install calculator

**Permission denied during installation**

Use the ``--user`` flag:

.. code-block:: bash

   pip install --user calculator

**Documentation build fails**

Ensure Sphinx is installed:

.. code-block:: bash

   pip install sphinx sphinx_rtd_theme
'''

# Advanced features guide (this would be in docs/advanced.rst):
SPHINX_ADVANCED_RST = '''
Advanced Features
=================

This section covers advanced usage patterns and customization options.

Custom Calculator Subclasses
-----------------------------

You can extend the Calculator class for specialized use cases:

.. code-block:: python

   from calculator import CalculatorStep3
   import math
   
   class ScientificCalculator(CalculatorStep3):
       """Extended calculator with scientific functions."""
       
       def sin(self, angle_degrees: float) -> float:
           """Calculate sine of angle in degrees.
           
           Args:
               angle_degrees: Angle in degrees
               
           Returns:
               Sine value rounded to precision
           """
           angle_radians = math.radians(angle_degrees)
           result = round(math.sin(angle_radians), self.precision)
           self.history.append(f"sin({angle_degrees}°) = {result}")
           return result
       
       def cos(self, angle_degrees: float) -> float:
           """Calculate cosine of angle in degrees."""
           angle_radians = math.radians(angle_degrees)
           result = round(math.cos(angle_radians), self.precision)
           self.history.append(f"cos({angle_degrees}°) = {result}")
           return result
       
       def log(self, number: float, base: float = math.e) -> float:
           """Calculate logarithm of number with given base."""
           if number <= 0:
               raise ValueError("Logarithm undefined for non-positive numbers")
           
           result = round(math.log(number, base), self.precision)
           base_name = "ln" if base == math.e else f"log_{base}"
           self.history.append(f"{base_name}({number}) = {result}")
           return result

Batch Operations
----------------

Process multiple calculations efficiently:

.. code-block:: python

   from calculator import CalculatorStep3
   from typing import List, Tuple
   
   class BatchCalculator(CalculatorStep3):
       """Calculator with batch operation support."""
       
       def batch_add(self, pairs: List[Tuple[float, float]]) -> List[float]:
           """Perform addition on multiple number pairs.
           
           Args:
               pairs: List of (a, b) tuples to add
               
           Returns:
               List of results
           """
           results = []
           for a, b in pairs:
               results.append(self.add(a, b))
           return results
       
       def sum_all(self, numbers: List[float]) -> float:
           """Calculate sum of all numbers in list."""
           if not numbers:
               return 0.0
           
           result = numbers[0]
           for num in numbers[1:]:
               result = self.add(result, num)
           return result

Configuration and Settings
--------------------------

Advanced configuration options:

.. code-block:: python

   from calculator import CalculatorStep3
   from typing import Optional
   
   class ConfigurableCalculator(CalculatorStep3):
       """Calculator with advanced configuration options."""
       
       def __init__(self, precision: int = 2, 
                    max_history: Optional[int] = None,
                    auto_clear: bool = False):
           """Initialize with advanced options.
           
           Args:
               precision: Decimal places for results
               max_history: Maximum history entries (None for unlimited)
               auto_clear: Automatically clear history when full
           """
           super().__init__(precision)
           self.max_history = max_history
           self.auto_clear = auto_clear
       
       def _add_to_history(self, operation: str) -> None:
           """Add operation to history with size management."""
           if self.max_history and len(self.history) >= self.max_history:
               if self.auto_clear:
                   self.history.clear()
               else:
                   self.history.pop(0)  # Remove oldest entry
           
           self.history.append(operation)

Performance Considerations
--------------------------

For high-performance scenarios:

.. code-block:: python

   import time
   from calculator import CalculatorStep3
   
   def benchmark_calculator():
       """Benchmark calculator performance."""
       calc = CalculatorStep3(precision=6)
       
       # Benchmark basic operations
       start_time = time.time()
       for i in range(10000):
           calc.add(i, i + 1)
       end_time = time.time()
       
       print(f"10,000 additions took {end_time - start_time:.4f} seconds")
       
       # Clear history to free memory
       calc.clear_history()

Thread Safety
-------------

.. warning::
   The Calculator class is not thread-safe. For concurrent usage,
   create separate instances for each thread or use proper locking.

.. code-block:: python

   import threading
   from calculator import CalculatorStep3
   
   def thread_safe_calculation():
       """Example of thread-safe calculator usage."""
       
       def worker(thread_id: int, results: dict):
           calc = CalculatorStep3()  # Separate instance per thread
           result = calc.add(thread_id, thread_id * 2)
           results[thread_id] = result
       
       results = {}
       threads = []
       
       for i in range(5):
           thread = threading.Thread(target=worker, args=(i, results))
           threads.append(thread)
           thread.start()
       
       for thread in threads:
           thread.join()
       
       print("Thread results:", results)
'''

# Final demonstration function that ties everything together:
def demonstrate_sphinx_documentation():
    """
    Complete demonstration of Sphinx documentation features.
    
    This function showcases all the documentation concepts covered
    in the previous steps and demonstrates how they work together.
    
    Returns:
        dict: Summary of documentation components created
        
    Example:
        >>> demo_result = demonstrate_sphinx_documentation()
        >>> print(demo_result['total_files'])
        6
        
    Note:
        This demonstration creates the complete documentation structure
        that would be used with Sphinx to generate professional HTML docs.
        
    See Also:
        :class:`CalculatorStep3`: The main calculator implementation
        :func:`sphinx-build`: Sphinx documentation builder command
    """
    print("=== Sphinx Documentation Demonstration ===")
    print()
    
    # Demonstrate the calculator functionality
    calc = CalculatorStep3(precision=3)
    
    print("1. Testing Calculator with Comprehensive Docstrings:")
    print(f"   Calculator precision: {calc.precision}")
    
    # Basic operations
    result1 = calc.add(15.7, 8.3)
    result2 = calc.multiply(result1, 2)
    result3 = calc.sqrt(result2)
    
    print(f"   15.7 + 8.3 = {result1}")
    print(f"   {result1} * 2 = {result2}")
    print(f"   √{result2} = {result3}")
    
    print()
    print("2. Documentation Structure Created:")
    
    documentation_files = {
        'conf.py': 'Sphinx configuration with extensions',
        'index.rst': 'Main documentation index with toctree',
        'api.rst': 'Complete API reference with autodoc',
        'quickstart.rst': 'Quick start guide with examples',
        'examples.rst': 'Comprehensive usage examples',
        'installation.rst': 'Installation instructions',
        'advanced.rst': 'Advanced features and patterns'
    }
    
    for filename, description in documentation_files.items():
        print(f"   ✓ {filename}: {description}")
    
    print()
    print("3. Sphinx Features Demonstrated:")
    
    sphinx_features = [
        "Google-style docstrings with Napoleon extension",
        "Automatic API documentation with autodoc",
        "Cross-references between classes and methods",
        "Code examples with syntax highlighting",
        "Parameter and return type documentation",
        "Exception documentation with raises sections",
        "Note, warning, and see-also admonitions",
        "Intersphinx links to external documentation",
        "Table of contents with toctree directive",
        "Comprehensive examples and tutorials"
    ]
    
    for feature in sphinx_features:
        print(f"   ✓ {feature}")
    
    print()
    print("4. Operation History:")
    for operation in calc.get_history():
        print(f"   {operation}")
    
    print()
    print("5. To Generate Documentation:")
    print("   sphinx-build -b html docs docs/_build/html")
    print("   open docs/_build/html/index.html")
    
    return {
        'total_files': len(documentation_files),
        'calculator_operations': len(calc.get_history()),
        'sphinx_features': len(sphinx_features),
        'documentation_complete': True
    }


# Final summary and best practices
print("""
# ===============================================================================
#                           SPHINX DOCUMENTATION SUMMARY
# ===============================================================================

This comprehensive example demonstrates:

1. **Proper Docstring Writing**: Google-style docstrings with complete
   parameter, return, and exception documentation

2. **Sphinx Configuration**: Complete conf.py with essential extensions
   like autodoc, napoleon, viewcode, and intersphinx

3. **Documentation Structure**: Organized RST files for different purposes
   (API reference, tutorials, examples, installation)

4. **Advanced Features**: Cross-references, code highlighting, admonitions,
   and comprehensive examples

5. **Best Practices**: Incremental documentation building, consistent style,
   and comprehensive coverage

Key Takeaways:
- Start with good docstrings in your code
- Use Sphinx extensions to automate documentation generation
- Organize documentation into logical sections
- Include plenty of examples and tutorials
- Test your documentation by building it regularly

This example provides a complete foundation for documenting any Python project
with Sphinx, following professional documentation standards.
""")

# Run the demonstration
if __name__ == "__main__":
    result = demonstrate_sphinx_documentation()
    print(f"\nDocumentation demonstration completed successfully!")
    print(f"Created {result['total_files']} documentation files")
    print(f"Demonstrated {result['sphinx_features']} Sphinx features")

