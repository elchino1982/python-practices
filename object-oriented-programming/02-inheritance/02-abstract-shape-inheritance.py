"""Question: Create a class named Shape with a method area that raises a
NotImplementedError. Create subclasses Circle and Square that implement the area method.
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
# - What is NotImplementedError and when do you use it?
# - How do you create abstract methods that subclasses must implement?
# - What formulas do you need for circle and square areas?
# - How do you import mathematical constants like pi?
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


# Step 1: Import required modules
# ===============================================================================

# Explanation:
# We need the math module to access pi for our circle area calculation.
# It's good practice to put imports at the top of the file.

import math

# What we accomplished in this step:
# - Imported math module for mathematical constants and functions


# Step 2: Define the Shape base class
# ===============================================================================

# Explanation:
# Let's create our Shape class. This will be our abstract base class that
# defines the interface that all shapes must follow.

import math

class Shape:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Shape class structure


# Step 3: Add the abstract area method
# ===============================================================================

# Explanation:
# The area method in Shape should raise NotImplementedError to force subclasses
# to implement their own version. This is a common pattern for abstract methods.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Added abstract area method that raises NotImplementedError


# Step 4: Create the Circle subclass
# ===============================================================================

# Explanation:
# Now let's create the Circle class that inherits from Shape. It needs a constructor
# to accept the radius and an area method that calculates the circle's area.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

# What we accomplished in this step:
# - Created Circle class that inherits from Shape
# - Added constructor to store radius


# Step 5: Implement Circle's area method
# ===============================================================================

# Explanation:
# The area of a circle is π × radius². We override the area method from Shape
# to provide the specific implementation for circles.

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
# - Implemented area method for Circle using the correct formula


# Step 6: Create the Square subclass
# ===============================================================================

# Explanation:
# Now let's create the Square class that also inherits from Shape. It needs a constructor
# to accept the side length and an area method that calculates the square's area.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# What we accomplished in this step:
# - Created Square class that inherits from Shape
# - Implemented area method using side²


# Step 7: Create instances and test our classes
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Circle and Square classes and test them to make sure everything works correctly.
# This demonstrates polymorphism - different classes implementing the same interface.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Test our classes:
circle = Circle(5)
square = Square(4)

print(f"Circle with radius 5 has area: {circle.area():.2f}")
print(f"Square with side 4 has area: {square.area()}")

# Demonstrate polymorphism - treating different shapes the same way
shapes = [Circle(3), Square(6), Circle(2)]
for shape in shapes:
    print(f"Shape area: {shape.area():.2f}")

# What we accomplished in this step:
# - Created and tested our complete Shape hierarchy
# - Demonstrated polymorphism with different shape types


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Abstract base classes with NotImplementedError
# - Method overriding in subclasses
# - Polymorphism - treating different objects the same way
# - Mathematical calculations in Python
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding Rectangle or Triangle!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================