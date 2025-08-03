# Python Syntax Cheat Sheet

A comprehensive reference guide for Python syntax, built-in functions, and essential programming concepts.

## 1. Variables and Data Types

### Variable Assignment:

```python
# Basic assignment
name = "Alice"
age = 30
height = 5.6
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Swapping variables
x, y = y, x
```

### Basic Data Types:

```python
# Numbers
integer = 42
float_num = 3.14
complex_num = 3 + 4j

# Strings
single_quote = 'Hello'
double_quote = "World"
multiline = """This is a
multiline string"""

# Boolean
is_true = True
is_false = False

# None
empty_value = None
```

### Type Checking and Conversion:

```python
# Type checking
print(type(42))        # <class 'int'>
print(isinstance(42, int))  # True

# Type conversion
str_num = "123"
int_num = int(str_num)     # 123
float_num = float(str_num) # 123.0
str_back = str(int_num)    # "123"
```

## 2. Strings

### String Operations:

```python
# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# String formatting
name = "Alice"
age = 30

# f-strings (Python 3.6+)
message = f"My name is {name} and I'm {age} years old"

# .format() method
message = "My name is {} and I'm {} years old".format(name, age)
message = "My name is {name} and I'm {age} years old".format(name=name, age=age)

# % formatting (older style)
message = "My name is %s and I'm %d years old" % (name, age)
```

### String Methods:

```python
text = "  Hello World  "

# Case methods
print(text.upper())      # "  HELLO WORLD  "
print(text.lower())      # "  hello world  "
print(text.title())      # "  Hello World  "
print(text.capitalize()) # "  hello world  "

# Whitespace methods
print(text.strip())      # "Hello World"
print(text.lstrip())     # "Hello World  "
print(text.rstrip())     # "  Hello World"

# Search and replace
print(text.find("World"))     # 8
print(text.replace("World", "Python"))  # "  Hello Python  "

# Split and join
words = "apple,banana,cherry".split(",")  # ['apple', 'banana', 'cherry']
joined = "-".join(words)  # "apple-banana-cherry"

# Boolean methods
print("hello".isalpha())   # True
print("123".isdigit())     # True
print("hello123".isalnum()) # True
```

### String Slicing:

```python
text = "Hello World"

# Basic slicing
print(text[0])      # "H"
print(text[-1])     # "d"
print(text[0:5])    # "Hello"
print(text[6:])     # "World"
print(text[:5])     # "Hello"
print(text[::2])    # "HloWrd" (every 2nd character)
print(text[::-1])   # "dlroW olleH" (reverse)
```

## 3. Lists

### List Creation and Operations:

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
range_list = list(range(5))  # [0, 1, 2, 3, 4]

# List operations
numbers.append(6)           # Add to end
numbers.insert(0, 0)        # Insert at index
numbers.extend([7, 8])      # Add multiple items
numbers.remove(3)           # Remove first occurrence
popped = numbers.pop()      # Remove and return last item
popped_index = numbers.pop(0)  # Remove and return item at index

# List methods
print(len(numbers))         # Length
print(numbers.count(2))     # Count occurrences
print(numbers.index(4))     # Find index of first occurrence
numbers.reverse()           # Reverse in place
numbers.sort()              # Sort in place
sorted_copy = sorted(numbers)  # Return sorted copy
```

### List Comprehensions:

```python
# Basic list comprehension
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]

# With function
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
```

### List Slicing:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:7])     # [2, 3, 4, 5, 6]
print(numbers[:5])      # [0, 1, 2, 3, 4]
print(numbers[5:])      # [5, 6, 7, 8, 9]
print(numbers[::2])     # [0, 2, 4, 6, 8]
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## 4. Dictionaries

### Dictionary Operations:

```python
# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}
dict_from_keys = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# Accessing values
name = person["name"]           # KeyError if key doesn't exist
age = person.get("age")         # None if key doesn't exist
age = person.get("age", 0)      # Default value if key doesn't exist

# Modifying dictionaries
person["email"] = "alice@email.com"  # Add new key-value pair
person["age"] = 31                   # Update existing value
person.update({"phone": "123-456-7890", "age": 32})  # Update multiple

# Removing items
del person["city"]              # Remove key-value pair
email = person.pop("email")     # Remove and return value
phone = person.pop("phone", "N/A")  # With default if key doesn't exist
```

### Dictionary Methods:

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

# Getting keys, values, items
keys = list(person.keys())      # ['name', 'age', 'city']
values = list(person.values())  # ['Alice', 30, 'New York']
items = list(person.items())    # [('name', 'Alice'), ('age', 30), ('city', 'New York')]

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
filtered = {k: v for k, v in person.items() if isinstance(v, str)}
```

## 5. Tuples and Sets

### Tuples:

```python
# Creating tuples
coordinates = (3, 4)
single_item = (42,)  # Note the comma for single item
empty_tuple = ()
tuple_from_list = tuple([1, 2, 3])

# Tuple operations
x, y = coordinates  # Unpacking
length = len(coordinates)
index = coordinates.index(3)
count = coordinates.count(4)

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # 3 4
```

### Sets:

```python
# Creating sets
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates an empty dict, not set
set_from_list = set([1, 2, 2, 3, 3])  # {1, 2, 3} - duplicates removed

# Set operations
numbers.add(6)              # Add single item
numbers.update([7, 8, 9])   # Add multiple items
numbers.remove(1)           # Remove item (KeyError if not found)
numbers.discard(10)         # Remove item (no error if not found)

# Set mathematics
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2         # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2  # {3, 4}
difference = set1 - set2    # {1, 2}
symmetric_diff = set1 ^ set2  # {1, 2, 5, 6}
```

## 6. Control Structures

### Conditional Statements:

```python
# if-elif-else
age = 18

if age < 13:
    category = "child"
elif age < 20:
    category = "teenager"
elif age < 60:
    category = "adult"
else:
    category = "senior"

# Ternary operator
status = "adult" if age >= 18 else "minor"

# Multiple conditions
if age >= 18 and age < 65:
    print("Working age")

if name == "Alice" or name == "Bob":
    print("Known person")

# Checking membership
if name in ["Alice", "Bob", "Charlie"]:
    print("Known person")
```

### Loops:

```python
# for loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8

# Iterating over collections
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Enumerate for index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterating over dictionary
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit loop
    print(i)
```

## 7. Functions

### Function Definition:

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Function with multiple parameters
def calculate_area(length, width):
    return length * width

# Function with variable arguments
def sum_all(*args):
    return sum(args)

# Function with keyword arguments
def create_profile(**kwargs):
    return kwargs

# Function with mixed parameters
def process_data(required_param, *args, default_param="default", **kwargs):
    pass
```

### Advanced Function Features:

```python
# Lambda functions
square = lambda x: x**2
add = lambda x, y: x + y

# Higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Function annotations
def add_numbers(a: int, b: int) -> int:
    return a + b

# Docstrings
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    """
    return length * width
```

## 8. Exception Handling

### Try-Except Blocks:

```python
# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching multiple exceptions
try:
    # some code
    pass
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Generic exception handling
try:
    # some code
    pass
except Exception as e:
    print(f"An error occurred: {e}")

# Finally block
try:
    file = open("data.txt", "r")
    # process file
except FileNotFoundError:
    print("File not found!")
finally:
    if 'file' in locals():
        file.close()

# Else block
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result: {result}")  # Runs if no exception
```

### Raising Exceptions:

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Custom exceptions
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def risky_function():
    raise CustomError("Something went wrong!")
```

## 9. File Operations

### Reading Files:

```python
# Reading entire file
with open("file.txt", "r") as file:
    content = file.read()

# Reading line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Reading all lines into a list
with open("file.txt", "r") as file:
    lines = file.readlines()

# Reading with encoding
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Writing Files:

```python
# Writing to file (overwrites existing)
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Appending to file
with open("output.txt", "a") as file:
    file.write("\nNew line")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

## 10. Modules and Packages

### Importing Modules:

```python
# Import entire module
import math
print(math.pi)

# Import specific functions
from math import pi, sqrt
print(pi)

# Import with alias
import numpy as np
import pandas as pd

# Import all (not recommended)
from math import *

# Conditional import
try:
    import numpy as np
except ImportError:
    print("NumPy not available")
```

### Creating Modules:

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, a, b):
        return a + b

# Using the module
# main.py
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.PI)
calc = mymodule.Calculator()
```

## 11. Built-in Functions

### Common Built-in Functions:

```python
# Type and length functions
len([1, 2, 3])          # 3
type(42)                # <class 'int'>
isinstance(42, int)     # True

# Math functions
abs(-5)                 # 5
min(1, 2, 3)           # 1
max(1, 2, 3)           # 3
sum([1, 2, 3])         # 6
round(3.14159, 2)      # 3.14

# Conversion functions
int("123")             # 123
float("3.14")          # 3.14
str(123)               # "123"
list("hello")          # ['h', 'e', 'l', 'l', 'o']
tuple([1, 2, 3])       # (1, 2, 3)
set([1, 2, 2, 3])      # {1, 2, 3}

# Iteration functions
range(5)               # 0, 1, 2, 3, 4
enumerate(['a', 'b'])  # (0, 'a'), (1, 'b')
zip([1, 2], ['a', 'b']) # (1, 'a'), (2, 'b')

# Filtering and mapping
filter(lambda x: x > 0, [-1, 0, 1, 2])  # [1, 2]
map(lambda x: x**2, [1, 2, 3])          # [1, 4, 9]

# Boolean functions
all([True, True, False])  # False
any([True, False, False]) # True

# Input/Output
input("Enter your name: ")  # Get user input
print("Hello", "World", sep="-")  # Hello-World
```

## 12. Comprehensions

### List Comprehensions:

```python
# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]

# With condition: [expression for item in iterable if condition]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]

# Multiple iterables
pairs = [(x, y) for x in range(3) for y in range(3)]
```

### Dictionary Comprehensions:

```python
# Basic syntax: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# From existing dictionary
person = {"name": "Alice", "age": 30, "city": "NY"}
string_values = {k: v for k, v in person.items() if isinstance(v, str)}
```

### Set Comprehensions:

```python
# Basic syntax: {expression for item in iterable}
unique_squares = {x**2 for x in range(-5, 6)}

# With condition
positive_squares = {x**2 for x in range(-5, 6) if x > 0}
```

## 13. Decorators

### Basic Decorators:

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```

### Built-in Decorators:

```python
class MyClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
    @staticmethod
    def static_method():
        return "This is a static method"
    
    @classmethod
    def class_method(cls):
        return "This is a class method"
```

## 14. Context Managers

### Using Context Managers:

```python
# File handling
with open("file.txt", "r") as file:
    content = file.read()
# File automatically closed

# Multiple context managers
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())
```

### Creating Context Managers:

```python
# Using contextlib
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    try:
        yield "resource"
    finally:
        print("Exiting context")

with my_context() as resource:
    print(f"Using {resource}")

# Class-based context manager
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        return False  # Don't suppress exceptions
```

## 15. Regular Expressions

### Basic Regex Operations:

```python
import re

# Pattern matching
text = "The quick brown fox jumps over the lazy dog"
pattern = r"fox"

# Search functions
match = re.search(pattern, text)      # First match
matches = re.findall(pattern, text)   # All matches
iterator = re.finditer(pattern, text) # Iterator of match objects

# String operations
result = re.sub(r"fox", "cat", text)  # Replace
parts = re.split(r"\s+", text)        # Split on whitespace

# Common patterns
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
phone_pattern = r"\d{3}-\d{3}-\d{4}"
url_pattern = r"https?://[^\s]+"

# Compiled patterns (for reuse)
compiled_pattern = re.compile(r"\d+")
numbers = compiled_pattern.findall("I have 5 apples and 3 oranges")
```

## Quick Reference

### Python Keywords:
```python
# Control flow
if, elif, else, for, while, break, continue, pass

# Functions and classes
def, class, return, yield, lambda

# Exception handling
try, except, finally, raise, assert

# Imports
import, from, as

# Boolean and None
True, False, None, and, or, not, is, in

# Variable scope
global, nonlocal

# Async programming
async, await

# Context management
with
```

### Operator Precedence (highest to lowest):
```python
()                    # Parentheses
**                    # Exponentiation
+x, -x, ~x           # Unary plus, minus, bitwise NOT
*, /, //, %          # Multiplication, division, floor division, modulo
+, -                 # Addition, subtraction
<<, >>               # Bitwise shifts
&                    # Bitwise AND
^                    # Bitwise XOR
|                    # Bitwise OR
==, !=, <, <=, >, >=, is, is not, in, not in  # Comparisons
not                  # Boolean NOT
and                  # Boolean AND
or                   # Boolean OR
```

### String Formatting Quick Reference:
```python
name = "Alice"
age = 30
pi = 3.14159

# f-strings (recommended)
f"Name: {name}, Age: {age}"
f"Pi to 2 decimal places: {pi:.2f}"
f"Uppercase name: {name.upper()}"

# .format() method
"Name: {}, Age: {}".format(name, age)
"Name: {name}, Age: {age}".format(name=name, age=age)
"Pi: {:.2f}".format(pi)

# % formatting (legacy)
"Name: %s, Age: %d" % (name, age)
"Pi: %.2f" % pi
```

---

*This comprehensive cheat sheet covers essential Python syntax and concepts. Bookmark it for quick reference while coding!*