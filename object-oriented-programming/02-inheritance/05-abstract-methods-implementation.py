"""Question: Implement a class Shape with a method area that raises a NotImplementedError.
Create subclasses Circle and Rectangle that implement the area method.
Demonstrate polymorphism by creating a list of shapes and calculating their areas.
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
# - What is an abstract base class? (class with methods that must be implemented by subclasses)
# - What is polymorphism? (treating different objects the same way through common interface)
# - How do you calculate circle area? (π × radius²)
# - How do you calculate rectangle area? (length × width)
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


# Step 1: Import required modules and define Shape base class
# ===============================================================================

# Explanation:
# We need the math module for π (pi) in circle calculations.
# The Shape class will be our abstract base class with an area method that raises NotImplementedError.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Imported math module for mathematical constants
# - Created abstract Shape base class with area method


# Step 2: Create Circle subclass
# ===============================================================================

# Explanation:
# The Circle class inherits from Shape and implements the area method.
# Circle area formula: π × radius²

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# What we accomplished in this step:
# - Created Circle class that inherits from Shape
# - Implemented area method using circle formula


# Step 3: Create Rectangle subclass
# ===============================================================================

# Explanation:
# The Rectangle class also inherits from Shape and implements the area method.
# Rectangle area formula: length × width

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# What we accomplished in this step:
# - Created Rectangle class that inherits from Shape
# - Implemented area method using rectangle formula


# Step 4: Add string representations for better output
# ===============================================================================

# Explanation:
# Let's add __str__ methods to make our shapes more readable when printed.
# This will help us understand what we're working with.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

# What we accomplished in this step:
# - Added __str__ methods for readable shape descriptions


# Step 5: Demonstrate polymorphism with a list of shapes
# ===============================================================================

# Explanation:
# Now let's create different shapes and put them in a list.
# We'll iterate through the list and call area() on each shape, demonstrating polymorphism.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

# Demonstrate polymorphism:
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 8)
]

print("Demonstrating polymorphism with different shapes:")
for shape in shapes:
    area = shape.area()
    print(f"{shape} has area: {area:.2f}")

# What we accomplished in this step:
# - Created a list of different shape objects
# - Demonstrated polymorphism by treating all shapes the same way


# Step 6: Calculate total area and demonstrate more polymorphism
# ===============================================================================

# Explanation:
# Let's add more functionality to show how polymorphism makes code flexible.
# We'll calculate the total area of all shapes and find the largest shape.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

# Demonstrate polymorphism:
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 8)
]

print("Demonstrating polymorphism with different shapes:")
for shape in shapes:
    area = shape.area()
    print(f"{shape} has area: {area:.2f}")

# Calculate total area using polymorphism
total_area = sum(shape.area() for shape in shapes)
print(f"\nTotal area of all shapes: {total_area:.2f}")

# Find the shape with the largest area
largest_shape = max(shapes, key=lambda shape: shape.area())
print(f"Largest shape: {largest_shape} with area: {largest_shape.area():.2f}")

# What we accomplished in this step:
# - Calculated total area using polymorphism
# - Found the largest shape using polymorphism
# - Demonstrated how polymorphism makes code flexible and reusable


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Abstract base classes with NotImplementedError
# - Inheritance and method overriding
# - Polymorphism - treating different objects the same way
# - Mathematical calculations in object-oriented programming
# - Code flexibility through common interfaces
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding Triangle or Square classes!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================