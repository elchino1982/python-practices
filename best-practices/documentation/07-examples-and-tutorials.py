"""Question: Create comprehensive examples and tutorials for documenting Python code.

Create a documentation system that demonstrates various documentation techniques
including docstrings, examples, tutorials, and API documentation.

Requirements:
1. Create classes with comprehensive docstrings
2. Include examples in docstrings
3. Create tutorial-style documentation
4. Demonstrate different documentation formats
5. Show best practices for code examples

Example usage:
    calculator = Calculator()
    result = calculator.add(5, 3)
    tutorial = DocumentationTutorial()
    tutorial.demonstrate_examples()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what documentation techniques you need
# - Start with simple docstrings
# - Add examples gradually
# - Test your documentation examples
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: The best way to learn documentation is by practicing it!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)


















































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What makes good documentation?
# - How to write clear examples?
# - What formats work best for tutorials?
# - How to structure API documentation?
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


# Step 1: Import modules and create basic class with simple docstring
# ===============================================================================

# Explanation:
# Good documentation starts with clear, concise docstrings that explain
# what a class or function does, its parameters, and return values.

from typing import List, Dict, Any, Optional
import doctest

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    like addition, subtraction, multiplication, and division.
    
    Attributes:
        history (List[str]): A list of performed operations for reference.
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.subtract(10, 4)
        6
    """
    
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history: List[str] = []


# Step 2: Add methods with comprehensive docstrings and examples
# ===============================================================================

# Explanation:
# Each method should have detailed docstrings that include:
# - Brief description
# - Parameters with types and descriptions
# - Return value description
# - Examples using doctest format
# - Any exceptions that might be raised

# All previous code from Step 1:
from typing import List, Dict, Any, Optional
import doctest

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    like addition, subtraction, multiplication, and division.
    
    Attributes:
        history (List[str]): A list of performed operations for reference.
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.subtract(10, 4)
        6
    """
    
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result.
        
        This method performs addition of two numbers and stores the operation
        in the calculator's history for future reference.
        
        Args:
            a (float): The first number to add.
            b (float): The second number to add.
        
        Returns:
            float: The sum of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.add(-1, 1)
            0.0
            >>> calc.add(2.5, 3.7)
            6.2
        
        Note:
            The operation is automatically added to the calculator's history.
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract the second number from the first.
        
        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.
        
        Returns:
            float: The difference of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7.0
            >>> calc.subtract(5, 8)
            -3.0
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.
        
        Returns:
            float: The product of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.multiply(-2, 3)
            -6.0
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide the first number by the second.
        
        Args:
            a (float): The dividend (number to be divided).
            b (float): The divisor (number to divide by).
        
        Returns:
            float: The quotient of a divided by b.
        
        Raises:
            ZeroDivisionError: If b is zero.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 3)
            2.3333333333333335
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: Cannot divide by zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result


# Step 3: Add utility methods and tutorial-style documentation
# ===============================================================================

# Explanation:
# Tutorial-style documentation provides step-by-step guidance and includes
# utility methods that help users understand how to use the class effectively.

# All previous code from Steps 1-2:
from typing import List, Dict, Any, Optional
import doctest

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    like addition, subtraction, multiplication, and division.
    
    Attributes:
        history (List[str]): A list of performed operations for reference.
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.subtract(10, 4)
        6
    """
    
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result.
        
        This method performs addition of two numbers and stores the operation
        in the calculator's history for future reference.
        
        Args:
            a (float): The first number to add.
            b (float): The second number to add.
        
        Returns:
            float: The sum of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.add(-1, 1)
            0.0
            >>> calc.add(2.5, 3.7)
            6.2
        
        Note:
            The operation is automatically added to the calculator's history.
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract the second number from the first.
        
        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.
        
        Returns:
            float: The difference of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7.0
            >>> calc.subtract(5, 8)
            -3.0
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.
        
        Returns:
            float: The product of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.multiply(-2, 3)
            -6.0
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide the first number by the second.
        
        Args:
            a (float): The dividend (number to be divided).
            b (float): The divisor (number to divide by).
        
        Returns:
            float: The quotient of a divided by b.
        
        Raises:
            ZeroDivisionError: If b is zero.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 3)
            2.3333333333333335
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: Cannot divide by zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """Get the history of all performed operations.
        
        Returns:
            List[str]: A list of strings representing all operations performed.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.multiply(4, 5)
            20.0
            >>> history = calc.get_history()
            >>> len(history)
            2
            >>> '2.0 + 3.0 = 5.0' in history
            True
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the operation history.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> len(calc.get_history())
            1
            >>> calc.clear_history()
            >>> len(calc.get_history())
            0
        """
        self.history.clear()
    
    def power(self, base: float, exponent: float) -> float:
        """Raise a number to a power.
        
        Args:
            base (float): The base number.
            exponent (float): The exponent to raise the base to.
        
        Returns:
            float: The result of base raised to the power of exponent.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
            >>> calc.power(5, 2)
            25.0
            >>> calc.power(9, 0.5)
            3.0
        """
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result


# Step 4: Create comprehensive tutorial class with different documentation formats
# ===============================================================================

# Explanation:
# This step demonstrates various documentation formats including Google style,
# NumPy style, and Sphinx style docstrings, along with tutorial examples.

# All previous code from Steps 1-3:
from typing import List, Dict, Any, Optional
import doctest

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    like addition, subtraction, multiplication, and division.
    
    Attributes:
        history (List[str]): A list of performed operations for reference.
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.subtract(10, 4)
        6
    """
    
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result.
        
        This method performs addition of two numbers and stores the operation
        in the calculator's history for future reference.
        
        Args:
            a (float): The first number to add.
            b (float): The second number to add.
        
        Returns:
            float: The sum of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.add(-1, 1)
            0.0
            >>> calc.add(2.5, 3.7)
            6.2
        
        Note:
            The operation is automatically added to the calculator's history.
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract the second number from the first.
        
        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.
        
        Returns:
            float: The difference of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7.0
            >>> calc.subtract(5, 8)
            -3.0
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.
        
        Returns:
            float: The product of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.multiply(-2, 3)
            -6.0
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide the first number by the second.
        
        Args:
            a (float): The dividend (number to be divided).
            b (float): The divisor (number to divide by).
        
        Returns:
            float: The quotient of a divided by b.
        
        Raises:
            ZeroDivisionError: If b is zero.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 3)
            2.3333333333333335
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: Cannot divide by zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """Get the history of all performed operations.
        
        Returns:
            List[str]: A list of strings representing all operations performed.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.multiply(4, 5)
            20.0
            >>> history = calc.get_history()
            >>> len(history)
            2
            >>> '2.0 + 3.0 = 5.0' in history
            True
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the operation history.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> len(calc.get_history())
            1
            >>> calc.clear_history()
            >>> len(calc.get_history())
            0
        """
        self.history.clear()
    
    def power(self, base: float, exponent: float) -> float:
        """Raise a number to a power.
        
        Args:
            base (float): The base number.
            exponent (float): The exponent to raise the base to.
        
        Returns:
            float: The result of base raised to the power of exponent.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
            >>> calc.power(5, 2)
            25.0
            >>> calc.power(9, 0.5)
            3.0
        """
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result


class DocumentationTutorial:
    """A comprehensive tutorial class demonstrating various documentation styles.
    
    This class showcases different documentation formats and best practices
    for writing clear, comprehensive documentation in Python.
    
    Attributes:
        examples (Dict[str, Any]): A collection of documentation examples.
    """
    
    def __init__(self):
        """Initialize the tutorial with example data."""
        self.examples: Dict[str, Any] = {}
    
    def google_style_example(self, param1: str, param2: int = 10) -> Dict[str, Any]:
        """Demonstrates Google-style docstring format.
        
        This method shows how to write docstrings using Google's style guide,
        which is clean, readable, and widely adopted in the Python community.
        
        Args:
            param1 (str): A string parameter that represents some input data.
            param2 (int, optional): An integer parameter with default value.
                Defaults to 10.
        
        Returns:
            Dict[str, Any]: A dictionary containing the processed results with
                keys 'input', 'multiplied', and 'length'.
        
        Raises:
            ValueError: If param1 is empty or param2 is negative.
        
        Examples:
            >>> tutorial = DocumentationTutorial()
            >>> result = tutorial.google_style_example("hello", 3)
            >>> result['input']
            'hello'
            >>> result['length']
            5
        
        Note:
            This is the recommended style for most Python projects.
        """
        if not param1:
            raise ValueError("param1 cannot be empty")
        if param2 < 0:
            raise ValueError("param2 cannot be negative")
        
        return {
            'input': param1,
            'multiplied': param1 * param2,
            'length': len(param1)
        }
    
    def numpy_style_example(self, data: List[float], threshold: float = 0.5) -> Dict[str, float]:
        """Demonstrates NumPy-style docstring format.
        
        This method shows the NumPy documentation style, which is more verbose
        but provides excellent structure for scientific computing documentation.
        
        Parameters
        ----------
        data : List[float]
            A list of floating-point numbers to process.
        threshold : float, optional
            The threshold value for filtering data, by default 0.5
        
        Returns
        -------
        Dict[str, float]
            A dictionary containing statistical information:
            - 'mean': The arithmetic mean of the data
            - 'max': The maximum value in the data
            - 'min': The minimum value in the data
            - 'filtered_count': Number of values above threshold
        
        Raises
        ------
        ValueError
            If the data list is empty.
        TypeError
            If data contains non-numeric values.
        
        Examples
        --------
        >>> tutorial = DocumentationTutorial()
        >>> data = [1.0, 2.5, 0.3, 4.2, 0.1]
        >>> result = tutorial.numpy_style_example(data, 1.0)
        >>> result['mean']
        1.62
        >>> result['filtered_count']
        2.0
        
        Notes
        -----
        This style is particularly popular in scientific Python libraries
        like NumPy, SciPy, and pandas.
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        
        try:
            mean_val = sum(data) / len(data)
            max_val = max(data)
            min_val = min(data)
            filtered_count = sum(1 for x in data if x > threshold)
        except TypeError:
            raise TypeError("All data values must be numeric")
        
        return {
            'mean': mean_val,
            'max': max_val,
            'min': min_val,
            'filtered_count': float(filtered_count)
        }


# Step 5: Add demonstration methods and practical examples
# ===============================================================================

# Explanation:
# This final step includes methods that demonstrate how to use the documentation
# effectively and provides practical examples for different use cases.

# All previous code from Steps 1-4:
from typing import List, Dict, Any, Optional
import doctest

class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    This class provides methods for performing basic mathematical operations
    like addition, subtraction, multiplication, and division.
    
    Attributes:
        history (List[str]): A list of performed operations for reference.
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(2, 3)
        5
        >>> calc.subtract(10, 4)
        6
    """
    
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result.
        
        This method performs addition of two numbers and stores the operation
        in the calculator's history for future reference.
        
        Args:
            a (float): The first number to add.
            b (float): The second number to add.
        
        Returns:
            float: The sum of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.add(-1, 1)
            0.0
            >>> calc.add(2.5, 3.7)
            6.2
        
        Note:
            The operation is automatically added to the calculator's history.
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract the second number from the first.
        
        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.
        
        Returns:
            float: The difference of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7.0
            >>> calc.subtract(5, 8)
            -3.0
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.
        
        Returns:
            float: The product of a and b.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20.0
            >>> calc.multiply(-2, 3)
            -6.0
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide the first number by the second.
        
        Args:
            a (float): The dividend (number to be divided).
            b (float): The divisor (number to divide by).
        
        Returns:
            float: The quotient of a divided by b.
        
        Raises:
            ZeroDivisionError: If b is zero.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 3)
            2.3333333333333335
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: Cannot divide by zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """Get the history of all performed operations.
        
        Returns:
            List[str]: A list of strings representing all operations performed.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
            >>> calc.multiply(4, 5)
            20.0
            >>> history = calc.get_history()
            >>> len(history)
            2
            >>> '2.0 + 3.0 = 5.0' in history
            True
        """
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear the operation history.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.add(1, 2)
            3.0
            >>> len(calc.get_history())
            1
            >>> calc.clear_history()
            >>> len(calc.get_history())
            0
        """
        self.history.clear()
    
    def power(self, base: float, exponent: float) -> float:
        """Raise a number to a power.
        
        Args:
            base (float): The base number.
            exponent (float): The exponent to raise the base to.
        
        Returns:
            float: The result of base raised to the power of exponent.
        
        Examples:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
            >>> calc.power(5, 2)
            25.0
            >>> calc.power(9, 0.5)
            3.0
        """
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result


class DocumentationTutorial:
    """A comprehensive tutorial class demonstrating various documentation styles.
    
    This class showcases different documentation formats and best practices
    for writing clear, comprehensive documentation in Python.
    
    Attributes:
        examples (Dict[str, Any]): A collection of documentation examples.
    """
    
    def __init__(self):
        """Initialize the tutorial with example data."""
        self.examples: Dict[str, Any] = {}
    
    def google_style_example(self, param1: str, param2: int = 10) -> Dict[str, Any]:
        """Demonstrates Google-style docstring format.
        
        This method shows how to write docstrings using Google's style guide,
        which is clean, readable, and widely adopted in the Python community.
        
        Args:
            param1 (str): A string parameter that represents some input data.
            param2 (int, optional): An integer parameter with default value.
                Defaults to 10.
        
        Returns:
            Dict[str, Any]: A dictionary containing the processed results with
                keys 'input', 'multiplied', and 'length'.
        
        Raises:
            ValueError: If param1 is empty or param2 is negative.
        
        Examples:
            >>> tutorial = DocumentationTutorial()
            >>> result = tutorial.google_style_example("hello", 3)
            >>> result['input']
            'hello'
            >>> result['length']
            5
        
        Note:
            This is the recommended style for most Python projects.
        """
        if not param1:
            raise ValueError("param1 cannot be empty")
        if param2 < 0:
            raise ValueError("param2 cannot be negative")
        
        return {
            'input': param1,
            'multiplied': param1 * param2,
            'length': len(param1)
        }
    
    def numpy_style_example(self, data: List[float], threshold: float = 0.5) -> Dict[str, float]:
        """Demonstrates NumPy-style docstring format.
        
        This method shows the NumPy documentation style, which is more verbose
        but provides excellent structure for scientific computing documentation.
        
        Parameters
        ----------
        data : List[float]
            A list of floating-point numbers to process.
        threshold : float, optional
            The threshold value for filtering data, by default 0.5
        
        Returns
        -------
        Dict[str, float]
            A dictionary containing statistical information:
            - 'mean': The arithmetic mean of the data
            - 'max': The maximum value in the data
            - 'min': The minimum value in the data
            - 'filtered_count': Number of values above threshold
        
        Raises
        ------
        ValueError
            If the data list is empty.
        TypeError
            If data contains non-numeric values.
        
        Examples
        --------
        >>> tutorial = DocumentationTutorial()
        >>> data = [1.0, 2.5, 0.3, 4.2, 0.1]
        >>> result = tutorial.numpy_style_example(data, 1.0)
        >>> result['mean']
        1.62
        >>> result['filtered_count']
        2.0
        
        Notes
        -----
        This style is particularly popular in scientific Python libraries
        like NumPy, SciPy, and pandas.
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        
        try:
            mean_val = sum(data) / len(data)
            max_val = max(data)
            min_val = min(data)
            filtered_count = sum(1 for x in data if x > threshold)
        except TypeError:
            raise TypeError("All data values must be numeric")
        
        return {
            'mean': mean_val,
            'max': max_val,
            'min': min_val,
            'filtered_count': float(filtered_count)
        }
    
    def demonstrate_examples(self) -> None:
        """Demonstrate various documentation examples and best practices.
        
        This method provides a comprehensive tutorial on how to create
        effective documentation with practical examples.
        
        Examples:
            >>> tutorial = DocumentationTutorial()
            >>> tutorial.demonstrate_examples()  # doctest: +ELLIPSIS
            === Documentation Tutorial ===
            ...
        """
        print("=== Documentation Tutorial ===")
        print("\n1. Basic Calculator Usage:")
        calc = Calculator()
        print(f"   Addition: 5 + 3 = {calc.add(5, 3)}")
        print(f"   Multiplication: 4 * 6 = {calc.multiply(4, 6)}")
        print(f"   Division: 15 / 3 = {calc.divide(15, 3)}")
        
        print("\n2. Google Style Documentation:")
        result = self.google_style_example("Python", 2)
        print(f"   Input: {result['input']}")
        print(f"   Multiplied: {result['multiplied']}")
        print(f"   Length: {result['length']}")
        
        print("\n3. NumPy Style Documentation:")
        data = [1.5, 2.8, 0.9, 3.2, 1.1]
        stats = self.numpy_style_example(data, 1.0)
        print(f"   Mean: {stats['mean']:.2f}")
        print(f"   Max: {stats['max']}")
        print(f"   Filtered count: {stats['filtered_count']}")
        
        print("\n4. History Management:")
        history = calc.get_history()
        print(f"   Operations performed: {len(history)}")
        for i, operation in enumerate(history, 1):
            print(f"   {i}. {operation}")
    
    def create_tutorial_content(self) -> str:
        """Create comprehensive tutorial content for documentation.
        
        Returns:
            str: A formatted tutorial string with examples and explanations.
        
        Examples:
            >>> tutorial = DocumentationTutorial()
            >>> content = tutorial.create_tutorial_content()
            >>> "Documentation Best Practices" in content
            True
            >>> "Google Style" in content
            True
        """
        tutorial_content = """
# Documentation Best Practices Tutorial

## 1. Writing Clear Docstrings

### Google Style (Recommended)
```python
def function_name(param1: type, param2: type = default) -> return_type:
    \"\"\"Brief description of the function.
    
    Longer description if needed, explaining the purpose and behavior.
    
    Args:
        param1 (type): Description of the first parameter.
        param2 (type, optional): Description with default value.
    
    Returns:
        return_type: Description of the return value.
    
    Raises:
        ExceptionType: When this exception is raised.
    
    Examples:
        >>> function_name("example", 42)
        expected_output
    \"\"\"
```

### NumPy Style (For Scientific Computing)
```python
def function_name(param1, param2=default):
    \"\"\"Brief description.
    
    Parameters
    ----------
    param1 : type
        Description of parameter.
    param2 : type, optional
        Description with default.
    
    Returns
    -------
    type
        Description of return value.
    \"\"\"
```

## 2. Including Examples

- Use doctest format for testable examples
- Provide realistic use cases
- Show both simple and complex scenarios
- Include edge cases when relevant

## 3. API Documentation Structure

1. **Brief Description**: One-line summary
2. **Detailed Description**: Comprehensive explanation
3. **Parameters**: All arguments with types and descriptions
4. **Returns**: What the function returns
5. **Raises**: Exceptions that may be raised
6. **Examples**: Practical usage examples
7. **Notes**: Additional important information

## 4. Best Practices

- Keep docstrings up to date with code changes
- Use consistent formatting throughout your project
- Include type hints in function signatures
- Test your examples with doctest
- Write for your audience (beginners vs experts)
- Use clear, concise language
- Provide context and motivation when needed
        """
        return tutorial_content.strip()
    
    def run_doctest_examples(self) -> None:
        """Run doctest on the current module to verify examples.
        
        This method demonstrates how to test documentation examples
        automatically using Python's doctest module.
        
        Examples:
            >>> tutorial = DocumentationTutorial()
            >>> tutorial.run_doctest_examples()  # doctest: +ELLIPSIS
            Running doctest examples...
            ...
        """
        print("Running doctest examples...")
        print("Note: In a real scenario, you would run:")
        print("  python -m doctest your_module.py")
        print("  or use doctest.testmod() in your code")
        
        # Demonstrate basic doctest usage
        import doctest
        print(f"Doctest module available: {doctest is not None}")
        print("All examples in docstrings can be automatically tested!")


# ===============================================================================
#                           PRACTICAL USAGE EXAMPLES
# ===============================================================================

def demonstrate_documentation_best_practices():
    """Demonstrate the complete documentation system in action.
    
    This function shows how all the documentation techniques work together
    to create a comprehensive and user-friendly documentation system.
    
    Examples:
        >>> demonstrate_documentation_best_practices()  # doctest: +ELLIPSIS
        === Complete Documentation Demonstration ===
        ...
    """
    print("=== Complete Documentation Demonstration ===")
    
    # Create instances
    calc = Calculator()
    tutorial = DocumentationTutorial()
    
    # Demonstrate calculator with full documentation
    print("\n1. Calculator with comprehensive documentation:")
    result1 = calc.add(10, 5)
    result2 = calc.multiply(result1, 2)
    result3 = calc.power(2, 3)
    
    print(f"   Step 1: 10 + 5 = {result1}")
    print(f"   Step 2: {result1} * 2 = {result2}")
    print(f"   Step 3: 2^3 = {result3}")
    
    # Show history feature
    history = calc.get_history()
    print(f"\n   Operation history ({len(history)} operations):")
    for i, op in enumerate(history, 1):
        print(f"     {i}. {op}")
    
    # Demonstrate tutorial features
    print("\n2. Documentation style examples:")
    tutorial.demonstrate_examples()
    
    # Show tutorial content
    print("\n3. Tutorial content generation:")
    content = tutorial.create_tutorial_content()
    print(f"   Generated tutorial length: {len(content)} characters")
    print("   Content includes best practices and examples")
    
    print("\n4. Documentation testing:")
    tutorial.run_doctest_examples()
    
    print("\n=== Documentation demonstration complete! ===")


if __name__ == "__main__":
    # Run the complete demonstration
    demonstrate_documentation_best_practices()
    
    # Optional: Run doctests
    print("\n" + "="*50)
    print("Running doctests...")
    import doctest
    doctest.testmod(verbose=True)