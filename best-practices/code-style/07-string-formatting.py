"""Question: Master Python string formatting techniques and best practices.

Learn and implement various string formatting methods including:
- % formatting (old style)
- .format() method
- f-strings (formatted string literals)
- Template strings
- Best practices for each method

Requirements:
1. Demonstrate % formatting with examples
2. Show .format() method usage
3. Implement f-string formatting
4. Use Template strings for user input
5. Show performance comparisons
6. Demonstrate best practices and when to use each method

Example usage:
    formatter = StringFormatter()
    result = formatter.format_user_info("John", 25, "Engineer")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about different string formatting methods
# - Start with simple examples
# - Test your code step by step
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
# - What are the different string formatting methods in Python?
# - When should you use % formatting vs .format() vs f-strings?
# - How do you handle special characters and escaping?
# - What about performance considerations?
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


# Step 1: Basic % formatting (old style)
# ===============================================================================

# Explanation:
# % formatting is the oldest string formatting method in Python.
# It uses % operator with format specifiers like %s, %d, %f, etc.

def demonstrate_percent_formatting():
    """Demonstrate % formatting with various examples."""
    
    # Basic string substitution
    name = "Alice"
    greeting = "Hello, %s!" % name
    print("Basic substitution:", greeting)
    
    # Multiple values with tuple
    name = "Bob"
    age = 30
    message = "Name: %s, Age: %d" % (name, age)
    print("Multiple values:", message)
    
    # Different format specifiers
    price = 19.99
    quantity = 3
    item = "book"
    
    # %s - string, %d - integer, %f - float
    summary = "Item: %s, Price: $%.2f, Quantity: %d" % (item, price, quantity)
    print("Format specifiers:", summary)
    
    # Named placeholders with dictionary
    data = {"product": "laptop", "price": 999.99, "discount": 10}
    offer = "%(product)s for $%(price).2f with %(discount)d%% discount" % data
    print("Named placeholders:", offer)

# Test Step 1
print("=== Step 1: % Formatting ===")
demonstrate_percent_formatting()
print()


# Step 2: .format() method (Python 2.7+)
# ===============================================================================

# Explanation:
# The .format() method is more powerful and flexible than % formatting.
# It uses {} placeholders and provides better readability and functionality.

# All code from Step 1:
def demonstrate_percent_formatting_step2():
    """Demonstrate % formatting with various examples."""
    
    # Basic string substitution
    name = "Alice"
    greeting = "Hello, %s!" % name
    print("Basic substitution:", greeting)
    
    # Multiple values with tuple
    name = "Bob"
    age = 30
    message = "Name: %s, Age: %d" % (name, age)
    print("Multiple values:", message)
    
    # Different format specifiers
    price = 19.99
    quantity = 3
    item = "book"
    
    # %s - string, %d - integer, %f - float
    summary = "Item: %s, Price: $%.2f, Quantity: %d" % (item, price, quantity)
    print("Format specifiers:", summary)
    
    # Named placeholders with dictionary
    data = {"product": "laptop", "price": 999.99, "discount": 10}
    offer = "%(product)s for $%(price).2f with %(discount)d%% discount" % data
    print("Named placeholders:", offer)

# New Step 2 content:
def demonstrate_format_method():
    """Demonstrate .format() method with various examples."""
    
    # Basic positional arguments
    name = "Charlie"
    greeting = "Hello, {}!".format(name)
    print("Basic format:", greeting)
    
    # Multiple positional arguments
    name = "Diana"
    age = 28
    message = "Name: {}, Age: {}".format(name, age)
    print("Multiple arguments:", message)
    
    # Positional arguments with indices
    item = "phone"
    price = 599.99
    quantity = 2
    summary = "Item: {0}, Price: ${1:.2f}, Quantity: {2}".format(item, price, quantity)
    print("With indices:", summary)
    
    # Named arguments
    data = {"product": "tablet", "price": 299.99, "discount": 15}
    offer = "{product} for ${price:.2f} with {discount}% discount".format(**data)
    print("Named arguments:", offer)
    
    # Mixed positional and named
    template = "{0} costs ${price:.2f} and we have {1} in stock"
    result = template.format("Headphones", 89, price=89.99)
    print("Mixed arguments:", result)
    
    # Format specifications
    number = 1234.5678
    formatted = "Number: {:.2f}, Padded: {:>10.2f}, Percentage: {:.1%}".format(
        number, number, 0.85
    )
    print("Format specs:", formatted)

# Test Step 2
print("=== Step 2: .format() Method ===")
demonstrate_percent_formatting_step2()
print()
demonstrate_format_method()
print()


# Step 3: f-strings (Python 3.6+) - The Modern Way
# ===============================================================================

# Explanation:
# f-strings (formatted string literals) are the most modern and efficient
# string formatting method. They're readable, fast, and support expressions.

# All code from Steps 1-2:
def demonstrate_percent_formatting_step3():
    """Demonstrate % formatting with various examples."""
    
    # Basic string substitution
    name = "Alice"
    greeting = "Hello, %s!" % name
    print("Basic substitution:", greeting)
    
    # Multiple values with tuple
    name = "Bob"
    age = 30
    message = "Name: %s, Age: %d" % (name, age)
    print("Multiple values:", message)
    
    # Different format specifiers
    price = 19.99
    quantity = 3
    item = "book"
    
    # %s - string, %d - integer, %f - float
    summary = "Item: %s, Price: $%.2f, Quantity: %d" % (item, price, quantity)
    print("Format specifiers:", summary)
    
    # Named placeholders with dictionary
    data = {"product": "laptop", "price": 999.99, "discount": 10}
    offer = "%(product)s for $%(price).2f with %(discount)d%% discount" % data
    print("Named placeholders:", offer)

def demonstrate_format_method_step3():
    """Demonstrate .format() method with various examples."""
    
    # Basic positional arguments
    name = "Charlie"
    greeting = "Hello, {}!".format(name)
    print("Basic format:", greeting)
    
    # Multiple positional arguments
    name = "Diana"
    age = 28
    message = "Name: {}, Age: {}".format(name, age)
    print("Multiple arguments:", message)
    
    # Positional arguments with indices
    item = "phone"
    price = 599.99
    quantity = 2
    summary = "Item: {0}, Price: ${1:.2f}, Quantity: {2}".format(item, price, quantity)
    print("With indices:", summary)
    
    # Named arguments
    data = {"product": "tablet", "price": 299.99, "discount": 15}
    offer = "{product} for ${price:.2f} with {discount}% discount".format(**data)
    print("Named arguments:", offer)
    
    # Mixed positional and named
    template = "{0} costs ${price:.2f} and we have {1} in stock"
    result = template.format("Headphones", 89, price=89.99)
    print("Mixed arguments:", result)
    
    # Format specifications
    number = 1234.5678
    formatted = "Number: {:.2f}, Padded: {:>10.2f}, Percentage: {:.1%}".format(
        number, number, 0.85
    )
    print("Format specs:", formatted)

# New Step 3 content:
def demonstrate_f_strings():
    """Demonstrate f-strings with various examples."""
    
    # Basic f-string usage
    name = "Eve"
    greeting = f"Hello, {name}!"
    print("Basic f-string:", greeting)
    
    # Multiple variables
    name = "Frank"
    age = 35
    message = f"Name: {name}, Age: {age}"
    print("Multiple variables:", message)
    
    # Expressions inside f-strings
    x = 10
    y = 20
    result = f"The sum of {x} and {y} is {x + y}"
    print("With expressions:", result)
    
    # Format specifications
    price = 1234.5678
    formatted = f"Price: ${price:.2f}, Padded: {price:>10.2f}"
    print("Format specs:", formatted)
    
    # Method calls and complex expressions
    items = ["apple", "banana", "cherry"]
    message = f"We have {len(items)} items: {', '.join(items)}"
    print("Method calls:", message)
    
    # Dictionary access
    person = {"name": "Grace", "age": 42, "job": "Developer"}
    info = f"Employee: {person['name']}, Age: {person['age']}, Job: {person['job']}"
    print("Dictionary access:", info)
    
    # Multiline f-strings
    product = "laptop"
    price = 999.99
    discount = 10
    description = f"""
    Product: {product}
    Original Price: ${price:.2f}
    Discount: {discount}%
    Final Price: ${price * (1 - discount/100):.2f}
    """
    print("Multiline f-string:", description.strip())

# Test Step 3
print("=== Step 3: f-strings (Modern Way) ===")
demonstrate_percent_formatting_step3()
print()
demonstrate_format_method_step3()
print()
demonstrate_f_strings()
print()


# Step 4: Template strings (for user input safety)
# ===============================================================================

# Explanation:
# Template strings are safer for user-provided templates because they don't
# allow arbitrary code execution. They're ideal for internationalization.

from string import Template

# All code from Steps 1-3:
def demonstrate_percent_formatting_step4():
    """Demonstrate % formatting with various examples."""
    
    # Basic string substitution
    name = "Alice"
    greeting = "Hello, %s!" % name
    print("Basic substitution:", greeting)
    
    # Multiple values with tuple
    name = "Bob"
    age = 30
    message = "Name: %s, Age: %d" % (name, age)
    print("Multiple values:", message)
    
    # Different format specifiers
    price = 19.99
    quantity = 3
    item = "book"
    
    # %s - string, %d - integer, %f - float
    summary = "Item: %s, Price: $%.2f, Quantity: %d" % (item, price, quantity)
    print("Format specifiers:", summary)
    
    # Named placeholders with dictionary
    data = {"product": "laptop", "price": 999.99, "discount": 10}
    offer = "%(product)s for $%(price).2f with %(discount)d%% discount" % data
    print("Named placeholders:", offer)

def demonstrate_format_method_step4():
    """Demonstrate .format() method with various examples."""
    
    # Basic positional arguments
    name = "Charlie"
    greeting = "Hello, {}!".format(name)
    print("Basic format:", greeting)
    
    # Multiple positional arguments
    name = "Diana"
    age = 28
    message = "Name: {}, Age: {}".format(name, age)
    print("Multiple arguments:", message)
    
    # Positional arguments with indices
    item = "phone"
    price = 599.99
    quantity = 2
    summary = "Item: {0}, Price: ${1:.2f}, Quantity: {2}".format(item, price, quantity)
    print("With indices:", summary)
    
    # Named arguments
    data = {"product": "tablet", "price": 299.99, "discount": 15}
    offer = "{product} for ${price:.2f} with {discount}% discount".format(**data)
    print("Named arguments:", offer)
    
    # Mixed positional and named
    template = "{0} costs ${price:.2f} and we have {1} in stock"
    result = template.format("Headphones", 89, price=89.99)
    print("Mixed arguments:", result)
    
    # Format specifications
    number = 1234.5678
    formatted = "Number: {:.2f}, Padded: {:>10.2f}, Percentage: {:.1%}".format(
        number, number, 0.85
    )
    print("Format specs:", formatted)

def demonstrate_f_strings_step4():
    """Demonstrate f-strings with various examples."""
    
    # Basic f-string usage
    name = "Eve"
    greeting = f"Hello, {name}!"
    print("Basic f-string:", greeting)
    
    # Multiple variables
    name = "Frank"
    age = 35
    message = f"Name: {name}, Age: {age}"
    print("Multiple variables:", message)
    
    # Expressions inside f-strings
    x = 10
    y = 20
    result = f"The sum of {x} and {y} is {x + y}"
    print("With expressions:", result)
    
    # Format specifications
    price = 1234.5678
    formatted = f"Price: ${price:.2f}, Padded: {price:>10.2f}"
    print("Format specs:", formatted)
    
    # Method calls and complex expressions
    items = ["apple", "banana", "cherry"]
    message = f"We have {len(items)} items: {', '.join(items)}"
    print("Method calls:", message)
    
    # Dictionary access
    person = {"name": "Grace", "age": 42, "job": "Developer"}
    info = f"Employee: {person['name']}, Age: {person['age']}, Job: {person['job']}"
    print("Dictionary access:", info)
    
    # Multiline f-strings
    product = "laptop"
    price = 999.99
    discount = 10
    description = f"""
    Product: {product}
    Original Price: ${price:.2f}
    Discount: {discount}%
    Final Price: ${price * (1 - discount/100):.2f}
    """
    print("Multiline f-string:", description.strip())

# New Step 4 content:
def demonstrate_template_strings():
    """Demonstrate Template strings for safe user input."""
    
    # Basic Template usage
    template = Template("Hello, $name!")
    greeting = template.substitute(name="Henry")
    print("Basic template:", greeting)
    
    # Multiple placeholders
    template = Template("Name: $name, Age: $age, Job: $job")
    message = template.substitute(name="Iris", age=29, job="Designer")
    print("Multiple placeholders:", message)
    
    # Using dictionary for substitution
    user_data = {"username": "john_doe", "email": "john@example.com", "role": "admin"}
    template = Template("User: $username, Email: $email, Role: $role")
    result = template.substitute(user_data)
    print("Dictionary substitution:", result)
    
    # Safe substitution (won't raise KeyError for missing keys)
    template = Template("Welcome $name! Your score is $score.")
    partial_data = {"name": "Kate"}
    try:
        # This would raise KeyError
        # result = template.substitute(partial_data)
        pass
    except KeyError as e:
        print(f"KeyError with substitute: {e}")
    
    # safe_substitute doesn't raise errors for missing keys
    result = template.safe_substitute(partial_data)
    print("Safe substitution:", result)
    
    # Template for internationalization
    messages = {
        "en": Template("Welcome $user! You have $count new messages."),
        "es": Template("¡Bienvenido $user! Tienes $count mensajes nuevos."),
        "fr": Template("Bienvenue $user! Vous avez $count nouveaux messages.")
    }
    
    data = {"user": "Maria", "count": 5}
    for lang, template in messages.items():
        localized = template.substitute(data)
        print(f"{lang.upper()}: {localized}")

# Test Step 4
print("=== Step 4: Template Strings (Safe User Input) ===")
demonstrate_percent_formatting_step4()
print()
demonstrate_format_method_step4()
print()
demonstrate_f_strings_step4()
print()
demonstrate_template_strings()
print()


# Step 5: Performance comparison and best practices
# ===============================================================================

# Explanation:
# Different formatting methods have different performance characteristics.
# Let's compare them and establish best practices for when to use each.

import time
from string import Template

# All code from Steps 1-4:
def demonstrate_percent_formatting_step5():
    """Demonstrate % formatting with various examples."""
    
    # Basic string substitution
    name = "Alice"
    greeting = "Hello, %s!" % name
    print("Basic substitution:", greeting)
    
    # Multiple values with tuple
    name = "Bob"
    age = 30
    message = "Name: %s, Age: %d" % (name, age)
    print("Multiple values:", message)
    
    # Different format specifiers
    price = 19.99
    quantity = 3
    item = "book"
    
    # %s - string, %d - integer, %f - float
    summary = "Item: %s, Price: $%.2f, Quantity: %d" % (item, price, quantity)
    print("Format specifiers:", summary)
    
    # Named placeholders with dictionary
    data = {"product": "laptop", "price": 999.99, "discount": 10}
    offer = "%(product)s for $%(price).2f with %(discount)d%% discount" % data
    print("Named placeholders:", offer)

def demonstrate_format_method_step5():
    """Demonstrate .format() method with various examples."""
    
    # Basic positional arguments
    name = "Charlie"
    greeting = "Hello, {}!".format(name)
    print("Basic format:", greeting)
    
    # Multiple positional arguments
    name = "Diana"
    age = 28
    message = "Name: {}, Age: {}".format(name, age)
    print("Multiple arguments:", message)
    
    # Positional arguments with indices
    item = "phone"
    price = 599.99
    quantity = 2
    summary = "Item: {0}, Price: ${1:.2f}, Quantity: {2}".format(item, price, quantity)
    print("With indices:", summary)
    
    # Named arguments
    data = {"product": "tablet", "price": 299.99, "discount": 15}
    offer = "{product} for ${price:.2f} with {discount}% discount".format(**data)
    print("Named arguments:", offer)
    
    # Mixed positional and named
    template = "{0} costs ${price:.2f} and we have {1} in stock"
    result = template.format("Headphones", 89, price=89.99)
    print("Mixed arguments:", result)
    
    # Format specifications
    number = 1234.5678
    formatted = "Number: {:.2f}, Padded: {:>10.2f}, Percentage: {:.1%}".format(
        number, number, 0.85
    )
    print("Format specs:", formatted)

def demonstrate_f_strings_step5():
    """Demonstrate f-strings with various examples."""
    
    # Basic f-string usage
    name = "Eve"
    greeting = f"Hello, {name}!"
    print("Basic f-string:", greeting)
    
    # Multiple variables
    name = "Frank"
    age = 35
    message = f"Name: {name}, Age: {age}"
    print("Multiple variables:", message)
    
    # Expressions inside f-strings
    x = 10
    y = 20
    result = f"The sum of {x} and {y} is {x + y}"
    print("With expressions:", result)
    
    # Format specifications
    price = 1234.5678
    formatted = f"Price: ${price:.2f}, Padded: {price:>10.2f}"
    print("Format specs:", formatted)
    
    # Method calls and complex expressions
    items = ["apple", "banana", "cherry"]
    message = f"We have {len(items)} items: {', '.join(items)}"
    print("Method calls:", message)
    
    # Dictionary access
    person = {"name": "Grace", "age": 42, "job": "Developer"}
    info = f"Employee: {person['name']}, Age: {person['age']}, Job: {person['job']}"
    print("Dictionary access:", info)
    
    # Multiline f-strings
    product = "laptop"
    price = 999.99
    discount = 10
    description = f"""
    Product: {product}
    Original Price: ${price:.2f}
    Discount: {discount}%
    Final Price: ${price * (1 - discount/100):.2f}
    """
    print("Multiline f-string:", description.strip())

def demonstrate_template_strings_step5():
    """Demonstrate Template strings for safe user input."""
    
    # Basic Template usage
    template = Template("Hello, $name!")
    greeting = template.substitute(name="Henry")
    print("Basic template:", greeting)
    
    # Multiple placeholders
    template = Template("Name: $name, Age: $age, Job: $job")
    message = template.substitute(name="Iris", age=29, job="Designer")
    print("Multiple placeholders:", message)
    
    # Using dictionary for substitution
    user_data = {"username": "john_doe", "email": "john@example.com", "role": "admin"}
    template = Template("User: $username, Email: $email, Role: $role")
    result = template.substitute(user_data)
    print("Dictionary substitution:", result)
    
    # Safe substitution (won't raise KeyError for missing keys)
    template = Template("Welcome $name! Your score is $score.")
    partial_data = {"name": "Kate"}
    try:
        # This would raise KeyError
        # result = template.substitute(partial_data)
        pass
    except KeyError as e:
        print(f"KeyError with substitute: {e}")
    
    # safe_substitute doesn't raise errors for missing keys
    result = template.safe_substitute(partial_data)
    print("Safe substitution:", result)
    
    # Template for internationalization
    messages = {
        "en": Template("Welcome $user! You have $count new messages."),
        "es": Template("¡Bienvenido $user! Tienes $count mensajes nuevos."),
        "fr": Template("Bienvenue $user! Vous avez $count nouveaux messages.")
    }
    
    data = {"user": "Maria", "count": 5}
    for lang, template in messages.items():
        localized = template.substitute(data)
        print(f"{lang.upper()}: {localized}")

# New Step 5 content:
def performance_comparison():
    """Compare performance of different string formatting methods."""
    
    # Test data
    name = "Performance"
    age = 25
    price = 99.99
    iterations = 100000
    
    print("Performance Comparison (100,000 iterations):")
    print("-" * 50)
    
    # Test % formatting
    start_time = time.time()
    for _ in range(iterations):
        result = "Name: %s, Age: %d, Price: $%.2f" % (name, age, price)
    percent_time = time.time() - start_time
    print(f"% formatting: {percent_time:.4f} seconds")
    
    # Test .format() method
    start_time = time.time()
    for _ in range(iterations):
        result = "Name: {}, Age: {}, Price: ${:.2f}".format(name, age, price)
    format_time = time.time() - start_time
    print(f".format() method: {format_time:.4f} seconds")
    
    # Test f-strings
    start_time = time.time()
    for _ in range(iterations):
        result = f"Name: {name}, Age: {age}, Price: ${price:.2f}"
    fstring_time = time.time() - start_time
    print(f"f-strings: {fstring_time:.4f} seconds")
    
    # Test Template strings
    template = Template("Name: $name, Age: $age, Price: $$price")
    start_time = time.time()
    for _ in range(iterations):
        result = template.substitute(name=name, age=age, price=f"{price:.2f}")
    template_time = time.time() - start_time
    print(f"Template strings: {template_time:.4f} seconds")
    
    print(f"\nFastest to slowest:")
    methods = [
        ("f-strings", fstring_time),
        ("% formatting", percent_time),
        (".format() method", format_time),
        ("Template strings", template_time)
    ]
    methods.sort(key=lambda x: x[1])
    for i, (method, time_taken) in enumerate(methods, 1):
        print(f"{i}. {method}: {time_taken:.4f}s")

def best_practices_guide():
    """Demonstrate best practices for string formatting."""
    
    print("STRING FORMATTING BEST PRACTICES:")
    print("=" * 50)
    
    print("\n1. USE F-STRINGS FOR MOST CASES (Python 3.6+)")
    print("   - Fastest and most readable")
    print("   - Great for simple to complex formatting")
    
    name = "Alice"
    age = 30
    print(f"   Example: f'Hello {name}, you are {age} years old'")
    
    print("\n2. USE .format() FOR COMPLEX FORMATTING")
    print("   - Better for complex format specifications")
    print("   - Good for reusable templates")
    
    template = "Product: {product:>15} | Price: ${price:>8.2f} | Stock: {stock:>3d}"
    print("   Example:", template.format(product="Laptop", price=999.99, stock=5))
    
    print("\n3. USE TEMPLATE STRINGS FOR USER INPUT")
    print("   - Safer for user-provided templates")
    print("   - Prevents code injection")
    print("   - Good for internationalization")
    
    user_template = Template("Welcome $username to $site_name!")
    print("   Example:", user_template.substitute(username="Bob", site_name="MyApp"))
    
    print("\n4. AVOID % FORMATTING IN NEW CODE")
    print("   - Legacy method, less readable")
    print("   - Use only for compatibility with old Python versions")
    
    print("\n5. FORMAT SPECIFICATIONS BEST PRACTICES:")
    
    # Number formatting
    number = 1234.5678
    print(f"   Decimal places: {number:.2f}")
    print(f"   Padding: {number:>10.2f}")
    print(f"   Zero padding: {number:010.2f}")
    print(f"   Percentage: {0.85:.1%}")
    print(f"   Scientific: {number:.2e}")
    
    # String formatting
    text = "hello"
    print(f"   Uppercase: {text.upper()}")
    print(f"   Centered: '{text:^20}'")
    print(f"   Left aligned: '{text:<20}'")
    print(f"   Right aligned: '{text:>20}'")

class StringFormatter:
    """A comprehensive string formatter class demonstrating all methods."""
    
    def format_user_info(self, name, age, job):
        """Format user information using f-strings (recommended)."""
        return f"User: {name}, Age: {age}, Job: {job}"
    
    def format_product_info(self, **kwargs):
        """Format product info using .format() for flexibility."""
        template = "Product: {name} | Price: ${price:.2f} | Stock: {stock}"
        return template.format(**kwargs)
    
    def format_safe_message(self, template_str, **kwargs):
        """Format message safely using Template strings."""
        template = Template(template_str)
        return template.safe_substitute(**kwargs)
    
    def format_legacy(self, name, value):
        """Legacy formatting using % (avoid in new code)."""
        return "Name: %s, Value: %.2f" % (name, value)

# Test Step 5
print("=== Step 5: Performance & Best Practices ===")
demonstrate_percent_formatting_step5()
print()
demonstrate_format_method_step5()
print()
demonstrate_f_strings_step5()
print()
demonstrate_template_strings_step5()
print()
performance_comparison()
print()
best_practices_guide()
print()

# Test the StringFormatter class
formatter = StringFormatter()
print("=== StringFormatter Class Demo ===")
print(formatter.format_user_info("John", 25, "Engineer"))
print(formatter.format_product_info(name="Laptop", price=999.99, stock=10))
print(formatter.format_safe_message("Hello $name!", name="World"))
print(formatter.format_legacy("Test", 42.5))
print()