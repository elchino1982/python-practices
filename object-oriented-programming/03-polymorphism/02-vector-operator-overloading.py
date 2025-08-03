"""Question: Implement a class Vector that supports vector addition,
subtraction, and dot product. Override the __add__, __sub__, and __mul__ methods.
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
# - What attributes does a Vector need? (x and y coordinates)
# - What is vector addition? (add corresponding components)
# - What is vector subtraction? (subtract corresponding components)
# - What is dot product? (x1*x2 + y1*y2, returns a scalar, not a vector)
# - Which magic methods correspond to +, -, and * operators?
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


# Step 1: Define the Vector class
# ===============================================================================

# Explanation:
# Let's start by creating our Vector class. This class will represent
# a 2D vector with x and y components and support mathematical operations.

class Vector:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Vector class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The __init__ method initializes the Vector with x and y coordinates.
# These represent the vector's components in 2D space.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# What we accomplished in this step:
# - Added constructor to initialize x and y components


# Step 3: Add the __add__ method for vector addition
# ===============================================================================

# Explanation:
# Vector addition adds corresponding components: (x1, y1) + (x2, y2) = (x1+x2, y1+y2)
# The __add__ method is called when we use the + operator.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# What we accomplished in this step:
# - Added __add__ method to support the + operator
# - Returns a new Vector with added components


# Step 4: Add the __sub__ method for vector subtraction
# ===============================================================================

# Explanation:
# Vector subtraction subtracts corresponding components: (x1, y1) - (x2, y2) = (x1-x2, y1-y2)
# The __sub__ method is called when we use the - operator.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

# What we accomplished in this step:
# - Added __sub__ method to support the - operator
# - Returns a new Vector with subtracted components


# Step 5: Add the __mul__ method for dot product
# ===============================================================================

# Explanation:
# The dot product of two vectors is: (x1, y1) · (x2, y2) = x1*x2 + y1*y2
# Note: This returns a scalar (number), not a vector!

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

# What we accomplished in this step:
# - Added __mul__ method to support the * operator for dot product
# - Returns a scalar value, not a Vector


# Step 6: Add the __str__ method for nice printing
# ===============================================================================

# Explanation:
# The __str__ method defines how our Vector looks when printed.
# This makes debugging and testing much easier.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# What we accomplished in this step:
# - Added __str__ method for readable string representation


# Step 7: Create instances and test our class
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Vector class and test all the operations
# to make sure everything works correctly.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Test our class:
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")

# Test addition
result_add = v1 + v2
print(f"Addition: {v1} + {v2} = {result_add}")

# Test subtraction
result_sub = v1 - v2
print(f"Subtraction: {v1} - {v2} = {result_sub}")

# Test dot product
result_dot = v1 * v2
print(f"Dot product: {v1} * {v2} = {result_dot}")

# What we accomplished in this step:
# - Created and tested our complete Vector implementation
# - Demonstrated all mathematical operations working correctly


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Magic methods (__add__, __sub__, __mul__, __str__)
# - Operator overloading in Python
# - Vector mathematics (addition, subtraction, dot product)
# - Returning different types (Vector vs scalar) from methods
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding magnitude calculation or cross product!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================