"""Question: Define a class Product with private attributes _name and _price.
Use properties to get and set these attributes with validation.
Add a method to apply a discount to the price.
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what classes and methods you need
# - Start with a simple implementation
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
# - What are private attributes? (attributes starting with _)
# - How do you create properties? (@property and @attribute.setter decorators)
# - What validation should price have? (positive number)
# - How do you calculate discount? (percentage of original price)
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


# Step 1: Define the Product class with private attributes
# ===============================================================================

# Explanation:
# Let's start by creating our Product class with private attributes.
# Private attributes start with _ and are meant for internal use.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

# What we accomplished in this step:
# - Created Product class with private attributes _name and _price


# Step 2: Add property getter for name
# ===============================================================================

# Explanation:
# Properties allow us to access private attributes through methods that look like attributes.
# The @property decorator creates a getter method.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

# What we accomplished in this step:
# - Added property getter for name attribute


# Step 3: Add property setter for name with validation
# ===============================================================================

# Explanation:
# The @name.setter decorator creates a setter method that includes validation.
# We'll check that the name is not empty.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

# What we accomplished in this step:
# - Added property setter for name with validation


# Step 4: Add property getter for price
# ===============================================================================

# Explanation:
# Now let's add the property getter for price, similar to what we did for name.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

# What we accomplished in this step:
# - Added property getter for price attribute


# Step 5: Add property setter for price with validation
# ===============================================================================

# Explanation:
# The price setter should validate that the price is a positive number.
# We'll accept both integers and floats.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        self._price = value

# What we accomplished in this step:
# - Added property setter for price with validation


# Step 6: Add discount method
# ===============================================================================

# Explanation:
# The apply_discount method reduces the price by a given percentage.
# We'll validate that the discount is between 0 and 100 percent.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        self._price = value

    def apply_discount(self, discount_percentage):
        if not isinstance(discount_percentage, (int, float)):
            raise ValueError("Discount percentage must be a number")
        if not (0 < discount_percentage < 100):
            raise ValueError("Discount percentage must be between 0 and 100")
        
        discount_amount = self._price * (discount_percentage / 100)
        self._price -= discount_amount
        return discount_amount

# What we accomplished in this step:
# - Added apply_discount method with validation
# - Returns the discount amount for transparency


# Step 7: Add string representation and additional methods
# ===============================================================================

# Explanation:
# Let's add a __str__ method and some additional useful methods to make our Product class more complete.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        self._price = value

    def apply_discount(self, discount_percentage):
        if not isinstance(discount_percentage, (int, float)):
            raise ValueError("Discount percentage must be a number")
        if not (0 < discount_percentage < 100):
            raise ValueError("Discount percentage must be between 0 and 100")
        
        original_price = self._price
        discount_amount = self._price * (discount_percentage / 100)
        self._price -= discount_amount
        print(f"Applied {discount_percentage}% discount: ${discount_amount:.2f} off")
        return discount_amount

    def __str__(self):
        return f"Product(name='{self._name}', price=${self._price:.2f})"

# What we accomplished in this step:
# - Added __str__ method for readable product representation
# - Enhanced apply_discount with user feedback


# Step 8: Create instances and test our product
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Product class and test all the properties
# and methods to make sure everything works correctly.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        self._price = value

    def apply_discount(self, discount_percentage):
        if not isinstance(discount_percentage, (int, float)):
            raise ValueError("Discount percentage must be a number")
        if not (0 < discount_percentage < 100):
            raise ValueError("Discount percentage must be between 0 and 100")
        
        original_price = self._price
        discount_amount = self._price * (discount_percentage / 100)
        self._price -= discount_amount
        print(f"Applied {discount_percentage}% discount: ${discount_amount:.2f} off")
        return discount_amount

    def __str__(self):
        return f"Product(name='{self._name}', price=${self._price:.2f})"

# Test our class:
product = Product("Laptop", 1000)
print(f"Initial product: {product}")

# Test property getters
print(f"Product name: {product.name}")
print(f"Product price: ${product.price}")

# Test property setters
product.name = "Gaming Laptop"
product.price = 1200
print(f"Updated product: {product}")

# Test discount method
product.apply_discount(10)
print(f"After 10% discount: {product}")

product.apply_discount(15)
print(f"After additional 15% discount: {product}")

# Test validation (these would raise errors if uncommented)
# try:
#     product.name = ""  # Should raise ValueError
# except ValueError as e:
#     print(f"Name validation error: {e}")

# try:
#     product.price = -100  # Should raise ValueError
# except ValueError as e:
#     print(f"Price validation error: {e}")

print("All product operations completed successfully!")

# What we accomplished in this step:
# - Created and tested our complete Product implementation
# - Demonstrated properties, validation, and discount functionality


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Private attributes and encapsulation
# - Property decorators for getters and setters
# - Data validation in property setters
# - Business logic implementation (discount calculation)
# - Error handling and user feedback
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding tax calculation or bulk discounts!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================