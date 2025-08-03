"""Question: Demonstrate Python code formatting best practices and tools.

Learn how to format Python code properly using various techniques and tools
like Black, autopep8, and manual formatting guidelines.

Requirements:
1. Show examples of poorly formatted code
2. Demonstrate proper formatting techniques
3. Show usage of formatting tools (Black, autopep8)
4. Demonstrate PEP 8 compliance
5. Show before/after examples

Example usage:
    formatter = CodeFormatter()
    formatted_code = formatter.format_with_black(messy_code)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read PEP 8 style guide
# - Practice with different formatting scenarios
# - Try using Black and autopep8 tools
# - Focus on readability and consistency
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: The best way to learn formatting is by practicing and using tools!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)


















































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What makes code readable?
# - How do formatting tools work?
# - What are the key PEP 8 guidelines?
# - How to handle long lines and complex expressions?
#
# Remember: Consistency is key in code formatting!


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


# Step 1: Import modules and show basic formatting principles
# ===============================================================================

# Explanation:
# Good code formatting starts with proper imports and basic structure.
# We'll demonstrate the fundamental principles of Python formatting.

import subprocess
import sys
from typing import List, Dict, Any, Optional
import textwrap


class CodeFormatter:
    """Demonstrates various code formatting techniques and tools."""
    
    def __init__(self):
        self.examples = []
    
    def add_example(self, title: str, bad_code: str, good_code: str):
        """Add a formatting example."""
        self.examples.append({
            'title': title,
            'bad': bad_code,
            'good': good_code
        })


# Step 1 Complete: Basic structure with proper imports and class definition
print("Step 1: Basic structure created with proper imports")
formatter = CodeFormatter()
print(f"Formatter created: {type(formatter).__name__}")


# Step 2: Add basic formatting examples and PEP 8 demonstrations
# ===============================================================================

# Explanation:
# Now we'll add methods to demonstrate common formatting issues and their fixes.
# This includes line length, spacing, and basic PEP 8 compliance.

# All code from Step 1, plus new additions:

import subprocess
import sys
from typing import List, Dict, Any, Optional
import textwrap


class CodeFormatter:
    """Demonstrates various code formatting techniques and tools."""
    
    def __init__(self):
        self.examples = []
    
    def add_example(self, title: str, bad_code: str, good_code: str):
        """Add a formatting example."""
        self.examples.append({
            'title': title,
            'bad': bad_code,
            'good': good_code
        })
    
    def demonstrate_line_length(self):
        """Show proper line length formatting."""
        bad_code = """
# Bad: Line too long
def calculate_complex_result(param1, param2, param3, param4, param5, param6, param7, param8):
    return param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8
"""
        
        good_code = """
# Good: Proper line breaks
def calculate_complex_result(
    param1, param2, param3, param4,
    param5, param6, param7, param8
):
    return (
        param1 + param2 + param3 + param4 +
        param5 + param6 + param7 + param8
    )
"""
        
        self.add_example("Line Length", bad_code, good_code)
    
    def demonstrate_spacing(self):
        """Show proper spacing around operators and after commas."""
        bad_code = """
# Bad: Inconsistent spacing
x=1+2*3
y=[1,2,3,4]
z={'a':1,'b':2}
if x>5and y<10:
    pass
"""
        
        good_code = """
# Good: Consistent spacing
x = 1 + 2 * 3
y = [1, 2, 3, 4]
z = {'a': 1, 'b': 2}
if x > 5 and y < 10:
    pass
"""
        
        self.add_example("Spacing", bad_code, good_code)


# Step 2 Complete: Added basic formatting demonstrations
print("\nStep 2: Added line length and spacing examples")
formatter.demonstrate_line_length()
formatter.demonstrate_spacing()
print(f"Examples added: {len(formatter.examples)}")


# Step 3: Add import organization and naming conventions
# ===============================================================================

# Explanation:
# Proper import organization and naming conventions are crucial for readable code.
# We'll demonstrate how to organize imports and follow PEP 8 naming guidelines.

# All code from Steps 1-2, plus new additions:

import subprocess
import sys
from typing import List, Dict, Any, Optional
import textwrap


class CodeFormatter:
    """Demonstrates various code formatting techniques and tools."""
    
    def __init__(self):
        self.examples = []
    
    def add_example(self, title: str, bad_code: str, good_code: str):
        """Add a formatting example."""
        self.examples.append({
            'title': title,
            'bad': bad_code,
            'good': good_code
        })
    
    def demonstrate_line_length(self):
        """Show proper line length formatting."""
        bad_code = """
# Bad: Line too long
def calculate_complex_result(param1, param2, param3, param4, param5, param6, param7, param8):
    return param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8
"""
        
        good_code = """
# Good: Proper line breaks
def calculate_complex_result(
    param1, param2, param3, param4,
    param5, param6, param7, param8
):
    return (
        param1 + param2 + param3 + param4 +
        param5 + param6 + param7 + param8
    )
"""
        
        self.add_example("Line Length", bad_code, good_code)
    
    def demonstrate_spacing(self):
        """Show proper spacing around operators and after commas."""
        bad_code = """
# Bad: Inconsistent spacing
x=1+2*3
y=[1,2,3,4]
z={'a':1,'b':2}
if x>5and y<10:
    pass
"""
        
        good_code = """
# Good: Consistent spacing
x = 1 + 2 * 3
y = [1, 2, 3, 4]
z = {'a': 1, 'b': 2}
if x > 5 and y < 10:
    pass
"""
        
        self.add_example("Spacing", bad_code, good_code)
    
    def demonstrate_import_organization(self):
        """Show proper import organization."""
        bad_code = """
# Bad: Unorganized imports
from typing import List
import sys
import os
from collections import defaultdict
import json
from typing import Dict
import subprocess
"""
        
        good_code = """
# Good: Organized imports (standard, third-party, local)
import json
import os
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List
"""
        
        self.add_example("Import Organization", bad_code, good_code)
    
    def demonstrate_naming_conventions(self):
        """Show proper naming conventions."""
        bad_code = """
# Bad: Inconsistent naming
class myClass:
    def __init__(self):
        self.MyVariable = 10
        self.another_var = 20
    
    def MyMethod(self):
        LocalVar = 5
        return LocalVar

SOME_FUNCTION = lambda x: x * 2
"""
        
        good_code = """
# Good: Consistent PEP 8 naming
class MyClass:
    def __init__(self):
        self.my_variable = 10
        self.another_var = 20
    
    def my_method(self):
        local_var = 5
        return local_var

def some_function(x):
    return x * 2
"""
        
        self.add_example("Naming Conventions", bad_code, good_code)


# Step 3 Complete: Added import organization and naming conventions
print("\nStep 3: Added import organization and naming examples")
formatter.demonstrate_import_organization()
formatter.demonstrate_naming_conventions()
print(f"Total examples: {len(formatter.examples)}")


# Step 4: Add formatting tools integration (Black, autopep8)
# ===============================================================================

# Explanation:
# Now we'll add methods to demonstrate how to use automated formatting tools
# like Black and autopep8 to automatically format code.

# All code from Steps 1-3, plus new additions:

import subprocess
import sys
from typing import List, Dict, Any, Optional
import textwrap


class CodeFormatter:
    """Demonstrates various code formatting techniques and tools."""
    
    def __init__(self):
        self.examples = []
    
    def add_example(self, title: str, bad_code: str, good_code: str):
        """Add a formatting example."""
        self.examples.append({
            'title': title,
            'bad': bad_code,
            'good': good_code
        })
    
    def demonstrate_line_length(self):
        """Show proper line length formatting."""
        bad_code = """
# Bad: Line too long
def calculate_complex_result(param1, param2, param3, param4, param5, param6, param7, param8):
    return param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8
"""
        
        good_code = """
# Good: Proper line breaks
def calculate_complex_result(
    param1, param2, param3, param4,
    param5, param6, param7, param8
):
    return (
        param1 + param2 + param3 + param4 +
        param5 + param6 + param7 + param8
    )
"""
        
        self.add_example("Line Length", bad_code, good_code)
    
    def demonstrate_spacing(self):
        """Show proper spacing around operators and after commas."""
        bad_code = """
# Bad: Inconsistent spacing
x=1+2*3
y=[1,2,3,4]
z={'a':1,'b':2}
if x>5and y<10:
    pass
"""
        
        good_code = """
# Good: Consistent spacing
x = 1 + 2 * 3
y = [1, 2, 3, 4]
z = {'a': 1, 'b': 2}
if x > 5 and y < 10:
    pass
"""
        
        self.add_example("Spacing", bad_code, good_code)
    
    def demonstrate_import_organization(self):
        """Show proper import organization."""
        bad_code = """
# Bad: Unorganized imports
from typing import List
import sys
import os
from collections import defaultdict
import json
from typing import Dict
import subprocess
"""
        
        good_code = """
# Good: Organized imports (standard, third-party, local)
import json
import os
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List
"""
        
        self.add_example("Import Organization", bad_code, good_code)
    
    def demonstrate_naming_conventions(self):
        """Show proper naming conventions."""
        bad_code = """
# Bad: Inconsistent naming
class myClass:
    def __init__(self):
        self.MyVariable = 10
        self.another_var = 20
    
    def MyMethod(self):
        LocalVar = 5
        return LocalVar

SOME_FUNCTION = lambda x: x * 2
"""
        
        good_code = """
# Good: Consistent PEP 8 naming
class MyClass:
    def __init__(self):
        self.my_variable = 10
        self.another_var = 20
    
    def my_method(self):
        local_var = 5
        return local_var

def some_function(x):
    return x * 2
"""
        
        self.add_example("Naming Conventions", bad_code, good_code)
    
    def format_with_black(self, code: str) -> str:
        """Format code using Black (simulated)."""
        # In real usage: pip install black, then use black.format_str()
        # Here we simulate the formatting process
        formatted_lines = []
        for line in code.strip().split('\n'):
            # Simulate basic Black formatting rules
            line = line.strip()
            if line:
                # Add proper spacing around operators
                line = line.replace('=', ' = ')
                line = line.replace('  =  ', ' = ')  # Fix double spaces
                line = line.replace('+', ' + ')
                line = line.replace('  +  ', ' + ')
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def format_with_autopep8(self, code: str) -> str:
        """Format code using autopep8 (simulated)."""
        # In real usage: pip install autopep8, then use autopep8.fix_code()
        # Here we simulate basic autopep8 functionality
        lines = code.strip().split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Fix spacing issues
                line = line.replace(',', ', ')
                line = line.replace('  ,  ', ', ')  # Fix double spaces
                line = line.replace(':', ': ')
                line = line.replace('  :  ', ': ')
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def demonstrate_tool_usage(self):
        """Show how formatting tools work."""
        messy_code = "x=1+2;y=[1,2,3];z={'a':1,'b':2}"
        
        black_formatted = self.format_with_black(messy_code)
        autopep8_formatted = self.format_with_autopep8(messy_code)
        
        tool_example = f"""
Original: {messy_code}
Black:    {black_formatted}
autopep8: {autopep8_formatted}
"""
        
        self.add_example("Tool Usage", messy_code, tool_example)


# Step 4 Complete: Added formatting tools integration
print("\nStep 4: Added formatting tools (Black, autopep8)")
formatter.demonstrate_tool_usage()
print(f"Tool formatting demonstrated")
print(f"Total examples: {len(formatter.examples)}")


# Step 5: Add complex formatting scenarios and best practices
# ===============================================================================

# Explanation:
# Now we'll demonstrate more complex formatting scenarios including
# function definitions, class structures, and advanced PEP 8 compliance.

# All code from Steps 1-4, plus new additions:

import subprocess
import sys
from typing import List, Dict, Any, Optional
import textwrap


class CodeFormatter:
    """Demonstrates various code formatting techniques and tools."""
    
    def __init__(self):
        self.examples = []
    
    def add_example(self, title: str, bad_code: str, good_code: str):
        """Add a formatting example."""
        self.examples.append({
            'title': title,
            'bad': bad_code,
            'good': good_code
        })
    
    def demonstrate_line_length(self):
        """Show proper line length formatting."""
        bad_code = """
# Bad: Line too long
def calculate_complex_result(param1, param2, param3, param4, param5, param6, param7, param8):
    return param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8
"""
        
        good_code = """
# Good: Proper line breaks
def calculate_complex_result(
    param1, param2, param3, param4,
    param5, param6, param7, param8
):
    return (
        param1 + param2 + param3 + param4 +
        param5 + param6 + param7 + param8
    )
"""
        
        self.add_example("Line Length", bad_code, good_code)
    
    def demonstrate_spacing(self):
        """Show proper spacing around operators and after commas."""
        bad_code = """
# Bad: Inconsistent spacing
x=1+2*3
y=[1,2,3,4]
z={'a':1,'b':2}
if x>5and y<10:
    pass
"""
        
        good_code = """
# Good: Consistent spacing
x = 1 + 2 * 3
y = [1, 2, 3, 4]
z = {'a': 1, 'b': 2}
if x > 5 and y < 10:
    pass
"""
        
        self.add_example("Spacing", bad_code, good_code)
    
    def demonstrate_import_organization(self):
        """Show proper import organization."""
        bad_code = """
# Bad: Unorganized imports
from typing import List
import sys
import os
from collections import defaultdict
import json
from typing import Dict
import subprocess
"""
        
        good_code = """
# Good: Organized imports (standard, third-party, local)
import json
import os
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List
"""
        
        self.add_example("Import Organization", bad_code, good_code)
    
    def demonstrate_naming_conventions(self):
        """Show proper naming conventions."""
        bad_code = """
# Bad: Inconsistent naming
class myClass:
    def __init__(self):
        self.MyVariable = 10
        self.another_var = 20
    
    def MyMethod(self):
        LocalVar = 5
        return LocalVar

SOME_FUNCTION = lambda x: x * 2
"""
        
        good_code = """
# Good: Consistent PEP 8 naming
class MyClass:
    def __init__(self):
        self.my_variable = 10
        self.another_var = 20
    
    def my_method(self):
        local_var = 5
        return local_var

def some_function(x):
    return x * 2
"""
        
        self.add_example("Naming Conventions", bad_code, good_code)
    
    def format_with_black(self, code: str) -> str:
        """Format code using Black (simulated)."""
        # In real usage: pip install black, then use black.format_str()
        # Here we simulate the formatting process
        formatted_lines = []
        for line in code.strip().split('\n'):
            # Simulate basic Black formatting rules
            line = line.strip()
            if line:
                # Add proper spacing around operators
                line = line.replace('=', ' = ')
                line = line.replace('  =  ', ' = ')  # Fix double spaces
                line = line.replace('+', ' + ')
                line = line.replace('  +  ', ' + ')
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def format_with_autopep8(self, code: str) -> str:
        """Format code using autopep8 (simulated)."""
        # In real usage: pip install autopep8, then use autopep8.fix_code()
        # Here we simulate basic autopep8 functionality
        lines = code.strip().split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Fix spacing issues
                line = line.replace(',', ', ')
                line = line.replace('  ,  ', ', ')  # Fix double spaces
                line = line.replace(':', ': ')
                line = line.replace('  :  ', ': ')
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def demonstrate_tool_usage(self):
        """Show how formatting tools work."""
        messy_code = "x=1+2;y=[1,2,3];z={'a':1,'b':2}"
        
        black_formatted = self.format_with_black(messy_code)
        autopep8_formatted = self.format_with_autopep8(messy_code)
        
        tool_example = f"""
Original: {messy_code}
Black:    {black_formatted}
autopep8: {autopep8_formatted}
"""
        
        self.add_example("Tool Usage", messy_code, tool_example)
    
    def demonstrate_complex_structures(self):
        """Show formatting for complex code structures."""
        bad_code = """
# Bad: Poor structure formatting
class DataProcessor:
    def __init__(self,data,config=None):
        self.data=data;self.config=config or {}
    def process(self,items,filters=[],transform=lambda x:x):
        result=[]
        for item in items:
            if all(f(item)for f in filters):result.append(transform(item))
        return result
"""
        
        good_code = """
# Good: Well-structured formatting
class DataProcessor:
    def __init__(self, data, config=None):
        self.data = data
        self.config = config or {}
    
    def process(self, items, filters=None, transform=None):
        if filters is None:
            filters = []
        if transform is None:
            transform = lambda x: x
        
        result = []
        for item in items:
            if all(f(item) for f in filters):
                result.append(transform(item))
        return result
"""
        
        self.add_example("Complex Structures", bad_code, good_code)
    
    def demonstrate_docstring_formatting(self):
        """Show proper docstring formatting."""
        bad_code = '''
# Bad: Poor docstring formatting
def calculate_area(length,width):
    """calculates area"""
    return length*width
'''
        
        good_code = '''
# Good: Proper docstring formatting
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    
    Returns:
        The area of the rectangle.
    
    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width
'''
        
        self.add_example("Docstring Formatting", bad_code, good_code)
    
    def show_all_examples(self):
        """Display all formatting examples."""
        print("\n" + "="*60)
        print("CODE FORMATTING EXAMPLES")
        print("="*60)
        
        for i, example in enumerate(self.examples, 1):
            print(f"\n{i}. {example['title']}")
            print("-" * 40)
            print("BAD:")
            print(example['bad'])
            print("\nGOOD:")
            print(example['good'])
            print("-" * 40)


# Step 5 Complete: Added complex formatting scenarios
print("\nStep 5: Added complex structures and docstring formatting")
formatter.demonstrate_complex_structures()
formatter.demonstrate_docstring_formatting()
print(f"Complex examples added")
print(f"Total examples: {len(formatter.examples)}")


# Step 6: Final demonstration and comprehensive example
# ===============================================================================

# Explanation:
# In this final step, we'll create a comprehensive demonstration that shows
# all formatting techniques together and provides a complete working example.

# All code from Steps 1-5, plus final demonstration:

import subprocess
import sys
from typing import List, Dict, Any, Optional
import textwrap


class CodeFormatter:
    """Demonstrates various code formatting techniques and tools."""
    
    def __init__(self):
        self.examples = []
    
    def add_example(self, title: str, bad_code: str, good_code: str):
        """Add a formatting example."""
        self.examples.append({
            'title': title,
            'bad': bad_code,
            'good': good_code
        })
    
    def demonstrate_line_length(self):
        """Show proper line length formatting."""
        bad_code = """
# Bad: Line too long
def calculate_complex_result(param1, param2, param3, param4, param5, param6, param7, param8):
    return param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8
"""
        
        good_code = """
# Good: Proper line breaks
def calculate_complex_result(
    param1, param2, param3, param4,
    param5, param6, param7, param8
):
    return (
        param1 + param2 + param3 + param4 +
        param5 + param6 + param7 + param8
    )
"""
        
        self.add_example("Line Length", bad_code, good_code)
    
    def demonstrate_spacing(self):
        """Show proper spacing around operators and after commas."""
        bad_code = """
# Bad: Inconsistent spacing
x=1+2*3
y=[1,2,3,4]
z={'a':1,'b':2}
if x>5and y<10:
    pass
"""
        
        good_code = """
# Good: Consistent spacing
x = 1 + 2 * 3
y = [1, 2, 3, 4]
z = {'a': 1, 'b': 2}
if x > 5 and y < 10:
    pass
"""
        
        self.add_example("Spacing", bad_code, good_code)
    
    def demonstrate_import_organization(self):
        """Show proper import organization."""
        bad_code = """
# Bad: Unorganized imports
from typing import List
import sys
import os
from collections import defaultdict
import json
from typing import Dict
import subprocess
"""
        
        good_code = """
# Good: Organized imports (standard, third-party, local)
import json
import os
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List
"""
        
        self.add_example("Import Organization", bad_code, good_code)
    
    def demonstrate_naming_conventions(self):
        """Show proper naming conventions."""
        bad_code = """
# Bad: Inconsistent naming
class myClass:
    def __init__(self):
        self.MyVariable = 10
        self.another_var = 20
    
    def MyMethod(self):
        LocalVar = 5
        return LocalVar

SOME_FUNCTION = lambda x: x * 2
"""
        
        good_code = """
# Good: Consistent PEP 8 naming
class MyClass:
    def __init__(self):
        self.my_variable = 10
        self.another_var = 20
    
    def my_method(self):
        local_var = 5
        return local_var

def some_function(x):
    return x * 2
"""
        
        self.add_example("Naming Conventions", bad_code, good_code)
    
    def format_with_black(self, code: str) -> str:
        """Format code using Black (simulated)."""
        # In real usage: pip install black, then use black.format_str()
        # Here we simulate the formatting process
        formatted_lines = []
        for line in code.strip().split('\n'):
            # Simulate basic Black formatting rules
            line = line.strip()
            if line:
                # Add proper spacing around operators
                line = line.replace('=', ' = ')
                line = line.replace('  =  ', ' = ')  # Fix double spaces
                line = line.replace('+', ' + ')
                line = line.replace('  +  ', ' + ')
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def format_with_autopep8(self, code: str) -> str:
        """Format code using autopep8 (simulated)."""
        # In real usage: pip install autopep8, then use autopep8.fix_code()
        # Here we simulate basic autopep8 functionality
        lines = code.strip().split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Fix spacing issues
                line = line.replace(',', ', ')
                line = line.replace('  ,  ', ', ')  # Fix double spaces
                line = line.replace(':', ': ')
                line = line.replace('  :  ', ': ')
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def demonstrate_tool_usage(self):
        """Show how formatting tools work."""
        messy_code = "x=1+2;y=[1,2,3];z={'a':1,'b':2}"
        
        black_formatted = self.format_with_black(messy_code)
        autopep8_formatted = self.format_with_autopep8(messy_code)
        
        tool_example = f"""
Original: {messy_code}
Black:    {black_formatted}
autopep8: {autopep8_formatted}
"""
        
        self.add_example("Tool Usage", messy_code, tool_example)
    
    def demonstrate_complex_structures(self):
        """Show formatting for complex code structures."""
        bad_code = """
# Bad: Poor structure formatting
class DataProcessor:
    def __init__(self,data,config=None):
        self.data=data;self.config=config or {}
    def process(self,items,filters=[],transform=lambda x:x):
        result=[]
        for item in items:
            if all(f(item)for f in filters):result.append(transform(item))
        return result
"""
        
        good_code = """
# Good: Well-structured formatting
class DataProcessor:
    def __init__(self, data, config=None):
        self.data = data
        self.config = config or {}
    
    def process(self, items, filters=None, transform=None):
        if filters is None:
            filters = []
        if transform is None:
            transform = lambda x: x
        
        result = []
        for item in items:
            if all(f(item) for f in filters):
                result.append(transform(item))
        return result
"""
        
        self.add_example("Complex Structures", bad_code, good_code)
    
    def demonstrate_docstring_formatting(self):
        """Show proper docstring formatting."""
        bad_code = '''
# Bad: Poor docstring formatting
def calculate_area(length,width):
    """calculates area"""
    return length*width
'''
        
        good_code = '''
# Good: Proper docstring formatting
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    
    Returns:
        The area of the rectangle.
    
    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width
'''
        
        self.add_example("Docstring Formatting", bad_code, good_code)
    
    def show_all_examples(self):
        """Display all formatting examples."""
        print("\n" + "="*60)
        print("CODE FORMATTING EXAMPLES")
        print("="*60)
        
        for i, example in enumerate(self.examples, 1):
            print(f"\n{i}. {example['title']}")
            print("-" * 40)
            print("BAD:")
            print(example['bad'])
            print("\nGOOD:")
            print(example['good'])
            print("-" * 40)
    
    def run_comprehensive_demo(self):
        """Run a comprehensive demonstration of all formatting techniques."""
        print("\n" + "="*70)
        print("COMPREHENSIVE CODE FORMATTING DEMONSTRATION")
        print("="*70)
        
        # Populate all examples
        self.demonstrate_line_length()
        self.demonstrate_spacing()
        self.demonstrate_import_organization()
        self.demonstrate_naming_conventions()
        self.demonstrate_tool_usage()
        self.demonstrate_complex_structures()
        self.demonstrate_docstring_formatting()
        
        # Show summary
        print(f"\nTotal formatting examples: {len(self.examples)}")
        print("\nFormatting tools demonstrated:")
        print("- Black (automated formatting)")
        print("- autopep8 (PEP 8 compliance)")
        print("- Manual formatting techniques")
        
        # Show all examples
        self.show_all_examples()
        
        print("\n" + "="*70)
        print("FORMATTING BEST PRACTICES SUMMARY")
        print("="*70)
        print("1. Use consistent spacing around operators")
        print("2. Follow PEP 8 naming conventions")
        print("3. Organize imports properly")
        print("4. Keep lines under 79-88 characters")
        print("5. Use proper docstring formatting")
        print("6. Leverage automated tools like Black")
        print("7. Be consistent throughout your codebase")
        print("="*70)


# Step 6 Complete: Final comprehensive demonstration
print("\nStep 6: Final comprehensive demonstration")
print("="*50)

# Create final formatter instance and run complete demo
final_formatter = CodeFormatter()
final_formatter.run_comprehensive_demo()

print("\n🎉 CODE FORMATTING TUTORIAL COMPLETE! 🎉")
print("You now have a comprehensive understanding of Python code formatting!")

# ===============================================================================
#                               FINAL SUMMARY
# ===============================================================================
#
# Congratulations! You've completed the comprehensive code formatting tutorial.
#
# What you've learned:
# 1. Basic formatting principles (spacing, line length)
# 2. Import organization and naming conventions
# 3. How to use formatting tools (Black, autopep8)
# 4. Complex structure formatting
# 5. Proper docstring formatting
# 6. Best practices for maintainable code
#
# Next steps:
# - Install and use Black: pip install black
# - Install and use autopep8: pip install autopep8
# - Set up your IDE with formatting on save
# - Practice these techniques in your own projects
#
# Remember: Consistent formatting makes code more readable and maintainable!
#
# ===============================================================================