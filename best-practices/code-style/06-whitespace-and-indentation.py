"""Question: Demonstrate proper whitespace and indentation practices in Python.

Learn and practice Python's whitespace and indentation conventions following PEP 8
guidelines for clean, readable, and maintainable code.

Requirements:
1. Proper indentation levels (4 spaces)
2. Consistent spacing around operators
3. Appropriate blank lines between functions and classes
4. Proper spacing in function calls and definitions
5. Line continuation best practices

Example usage:
    # Good indentation
    def calculate_area(length, width):
        return length * width
    
    # Good spacing
    result = calculate_area(10, 5)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read PEP 8 guidelines for whitespace
# - Practice consistent indentation
# - Use 4 spaces, not tabs
# - Be consistent with spacing around operators
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
# - How many spaces should you use for indentation?
# - Where should you put spaces around operators?
# - How many blank lines between functions and classes?
# - How to handle long lines and line continuation?
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


# Step 1: Basic indentation rules (4 spaces)
# ===============================================================================

# Explanation:
# Python uses indentation to define code blocks. PEP 8 recommends 4 spaces
# per indentation level. Never mix tabs and spaces.

def basic_indentation_example():
    """Demonstrates proper 4-space indentation."""
    # This is indented 4 spaces from the function definition
    message = "Hello, World!"
    
    # Nested blocks get additional 4 spaces
    if True:
        print(message)  # 8 spaces total
        
        # Even deeper nesting
        for i in range(3):
            print(f"Number: {i}")  # 12 spaces total


# Step 2: Spacing around operators
# ===============================================================================

# Explanation:
# Use single spaces around binary operators (=, +, -, *, /, ==, !=, etc.)
# but be consistent and consider readability.

def spacing_around_operators():
    """Demonstrates proper spacing around operators."""
    # Good: Single space around assignment and arithmetic operators
    x = 5
    y = 10
    result = x + y
    
    # Good: Spacing in comparisons
    if x == 5 and y != 0:
        quotient = y / x
        
    # Good: Spacing in complex expressions
    total = (x * 2) + (y * 3) - 1
    
    # Good: No space around = in keyword arguments
    print("Result:", result, sep=" = ")
    
    # Good: No space around = in default parameters
    def calculate(base=10, multiplier=2):
        return base * multiplier
    
    return calculate()


# Step 3: Blank lines between functions and classes
# ===============================================================================

# Explanation:
# Use 2 blank lines before top-level function and class definitions.
# Use 1 blank line before method definitions inside classes.

class ExampleClass:
    """Demonstrates proper blank line usage in classes."""
    
    def __init__(self, name):
        """Initialize with name."""
        self.name = name
    
    def method_one(self):
        """First method - note single blank line above."""
        return f"Hello from {self.name}"
    
    def method_two(self):
        """Second method - note single blank line above."""
        return self.name.upper()


def top_level_function_one():
    """First top-level function - note 2 blank lines above."""
    return "Function one"


def top_level_function_two():
    """Second top-level function - note 2 blank lines above."""
    return "Function two"


# Step 4: Spacing in function calls and definitions
# ===============================================================================

# Explanation:
# No spaces around parentheses, brackets, or braces.
# Single space after commas in parameter lists.

def some_function(a, b):
    """Helper function for demonstration."""
    return f"{a} + {b}"


def function_spacing_examples(param1, param2, param3=None):
    """Demonstrates proper spacing in function definitions."""
    # Good: No space before opening parenthesis
    result = some_function(param1, param2)
    
    # Good: Space after commas in function calls
    data = [1, 2, 3, 4, 5]
    
    # Good: No space inside brackets/parentheses
    item = data[0]
    subset = data[1:3]
    
    # Good: Dictionary spacing
    config = {'key1': 'value1', 'key2': 'value2'}
    
    # Good: Multiple arguments with proper spacing
    formatted = format_string(
        template="Hello {name}",
        name=param1,
        uppercase=True
    )
    
    return formatted


def format_string(template, name, uppercase=False):
    """Helper function for demonstration."""
    result = template.format(name=name)
    return result.upper() if uppercase else result


# Step 5: Line continuation best practices
# ===============================================================================

# Explanation:
# When lines are too long (>79 characters), use proper line continuation.
# Prefer implicit line continuation over explicit backslashes.

def line_continuation_examples():
    """Demonstrates proper line continuation techniques."""
    # Define some variables for demonstration
    some_very_long_variable_name = 10
    another_very_long_variable_name = 20
    yet_another_long_variable = 30
    first_parameter = "param1"
    second_parameter = "param2"
    third_parameter = "param3"
    fourth_parameter = "param4"
    condition_one = True
    condition_two = True
    condition_three = True
    condition_four = True
    
    # Good: Implicit continuation with parentheses
    long_calculation = (
        some_very_long_variable_name +
        another_very_long_variable_name +
        yet_another_long_variable
    )
    
    # Good: Function call continuation
    def some_function_with_long_name(*args):
        return f"Called with {len(args)} parameters"
    
    def do_something():
        print("Doing something...")
    
    result = some_function_with_long_name(
        first_parameter,
        second_parameter,
        third_parameter,
        fourth_parameter
    )
    
    # Good: List continuation
    long_list = [
        'first_item',
        'second_item', 
        'third_item',
        'fourth_item'
    ]
    
    # Good: Dictionary continuation
    config = {
        'database_host': 'localhost',
        'database_port': 5432,
        'database_name': 'myapp',
        'database_user': 'admin'
    }
    
    # Good: Conditional continuation
    if (condition_one and condition_two and
            condition_three and condition_four):
        do_something()
    
    return result


# Step 6: Common whitespace and indentation mistakes (what NOT to do)
# ===============================================================================

# Explanation:
# Here are common mistakes to avoid when dealing with whitespace and indentation.

def bad_examples_to_avoid():
    """Examples of poor whitespace and indentation practices."""
    
    # BAD: Inconsistent indentation (mixing spaces and tabs)
    # if True:
    #     print("4 spaces")
    # 	print("tab character")  # Don't mix!
    
    # BAD: Wrong number of spaces for indentation
    # if True:
    #   print("Only 2 spaces")  # Should be 4
    #       print("6 spaces")   # Inconsistent
    
    # BAD: No spaces around operators
    x=5+10*2  # Hard to read
    
    # BAD: Too many spaces around operators
    y  =  10  +  5  # Excessive spacing
    
    # BAD: Spaces inside parentheses/brackets
    result = some_function( x, y )  # Don't do this
    data = [ 1, 2, 3 ]  # Don't do this
    
    # BAD: No space after commas
    items = [1,2,3,4,5]  # Hard to read
    
    # BAD: Space before function parentheses
    # result = some_function (x, y)  # Don't do this
    
    return x, y


# Step 7: Complete example with all best practices combined
# ===============================================================================

# Explanation:
# This example demonstrates all the whitespace and indentation best practices
# working together in a realistic code scenario.

class DataProcessor:
    """A class that demonstrates proper whitespace and indentation."""
    
    def __init__(self, data_source, output_format='json'):
        """Initialize the data processor."""
        self.data_source = data_source
        self.output_format = output_format
        self.processed_data = []
    
    def process_data(self, filters=None, sort_key=None):
        """Process data with optional filters and sorting."""
        # Proper spacing in variable assignments
        raw_data = self._load_data()
        filtered_data = raw_data
        
        # Proper spacing in conditionals
        if filters is not None and len(filters) > 0:
            filtered_data = self._apply_filters(raw_data, filters)
        
        # Proper spacing in function calls
        if sort_key is not None:
            filtered_data = sorted(
                filtered_data,
                key=lambda x: x.get(sort_key, 0),
                reverse=True
            )
        
        # Proper list comprehension spacing
        self.processed_data = [
            self._transform_item(item)
            for item in filtered_data
            if self._is_valid_item(item)
        ]
        
        return self.processed_data
    
    def _load_data(self):
        """Load data from source."""
        # Simulated data loading with proper spacing
        return [
            {'id': 1, 'name': 'Item 1', 'value': 100},
            {'id': 2, 'name': 'Item 2', 'value': 200},
            {'id': 3, 'name': 'Item 3', 'value': 150}
        ]
    
    def _apply_filters(self, data, filters):
        """Apply filters to data."""
        result = data
        
        for filter_key, filter_value in filters.items():
            result = [
                item for item in result
                if item.get(filter_key) == filter_value
            ]
        
        return result
    
    def _transform_item(self, item):
        """Transform a single data item."""
        return {
            'id': item['id'],
            'display_name': item['name'].upper(),
            'formatted_value': f"${item['value']:,.2f}"
        }
    
    def _is_valid_item(self, item):
        """Check if item is valid."""
        return (
            item is not None and
            'id' in item and
            'name' in item and
            'value' in item and
            item['value'] > 0
        )


def demonstrate_usage():
    """Demonstrate the proper usage with good whitespace practices."""
    # Proper spacing in object creation
    processor = DataProcessor(
        data_source='database',
        output_format='json'
    )
    
    # Proper spacing in method calls
    results = processor.process_data(
        filters={'name': 'Item 1'},
        sort_key='value'
    )
    
    # Proper spacing in loops and conditionals
    for item in results:
        if item['id'] > 0:
            print(f"Processing: {item['display_name']}")
    
    return results


# ===============================================================================
#                              TESTING SECTION
# ===============================================================================

def test_whitespace_examples():
    """Test all the whitespace and indentation examples."""
    print("Testing whitespace and indentation examples...")
    
    # Test basic indentation
    print("\n1. Testing basic indentation:")
    basic_indentation_example()
    
    # Test operator spacing
    print("\n2. Testing operator spacing:")
    result = spacing_around_operators()
    print(f"Operator spacing result: {result}")
    
    # Test class and function spacing
    print("\n3. Testing class instantiation:")
    example = ExampleClass("Test")
    print(example.method_one())
    print(example.method_two())
    
    # Test function spacing
    print("\n4. Testing function spacing:")
    func_result = function_spacing_examples("World", "Python")
    print(f"Function spacing result: {func_result}")
    
    # Test line continuation
    print("\n5. Testing line continuation:")
    line_result = line_continuation_examples()
    print(f"Line continuation result: {line_result}")
    
    # Test complete example
    print("\n6. Testing complete DataProcessor example:")
    demo_results = demonstrate_usage()
    print(f"Demo results: {demo_results}")
    
    print("\nAll whitespace and indentation examples completed!")


# ===============================================================================
#                              SUMMARY SECTION
# ===============================================================================

"""
WHITESPACE AND INDENTATION BEST PRACTICES SUMMARY:

1. INDENTATION:
   - Use 4 spaces per indentation level
   - Never mix tabs and spaces
   - Be consistent throughout your codebase

2. OPERATOR SPACING:
   - Single space around binary operators (=, +, -, *, /, ==, !=)
   - No space around = in keyword arguments and default parameters
   - Be consistent and prioritize readability

3. BLANK LINES:
   - 2 blank lines before top-level function and class definitions
   - 1 blank line before method definitions inside classes
   - Use blank lines sparingly inside functions to separate logical sections

4. FUNCTION/METHOD SPACING:
   - No spaces around parentheses, brackets, or braces
   - Single space after commas in parameter lists
   - No space before opening parenthesis in function calls

5. LINE CONTINUATION:
   - Prefer implicit line continuation over explicit backslashes
   - Use parentheses for long expressions
   - Align continuation lines appropriately
   - Keep lines under 79 characters when possible

6. CONSISTENCY:
   - Be consistent with your spacing choices
   - Follow PEP 8 guidelines
   - Use tools like black, autopep8, or flake8 to enforce consistency

Remember: Good whitespace and indentation make your code more readable,
maintainable, and professional. These practices become second nature with
practice and help create code that other developers can easily understand.
"""


if __name__ == "__main__":
    test_whitespace_examples()


