"""Question: Create an abstract base class Shape with abstract methods area() and perimeter().
Implement concrete subclasses Circle and Rectangle that provide implementations for these methods.
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
# - What is the ABC module and how do you import it?
# - How do you create an abstract base class?
# - What is the @abstractmethod decorator?
# - How do concrete classes implement abstract methods?
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


# Step 1: Import the ABC module
# ===============================================================================

# Explanation:
# The ABC (Abstract Base Class) module provides the infrastructure for defining
# abstract base classes in Python. We need to import ABC and abstractmethod.

from abc import ABC, abstractmethod

# What we accomplished in this step:
# - Imported the necessary components for creating abstract classes


# Step 2: Create the abstract Shape class
# ===============================================================================

# Explanation:
# An abstract base class inherits from ABC and contains one or more abstract methods.
# Abstract methods are declared but not implemented in the base class.

from abc import ABC, abstractmethod

class Shape(ABC):
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the abstract Shape class that inherits from ABC


# Step 3: Add abstract methods to Shape
# ===============================================================================

# Explanation:
# Abstract methods are decorated with @abstractmethod and typically contain
# only a pass statement or raise NotImplementedError.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# What we accomplished in this step:
# - Added abstract area() and perimeter() methods
# - Used @abstractmethod decorator to mark them as abstract


# Step 4: Create the Circle subclass
# ===============================================================================

# Explanation:
# Concrete subclasses must implement all abstract methods from their parent class.
# The Circle class needs a radius and formulas for area and perimeter.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# What we accomplished in this step:
# - Created Circle class that inherits from Shape
# - Implemented both abstract methods with circle formulas


# Step 5: Create the Rectangle subclass
# ===============================================================================

# Explanation:
# The Rectangle class also needs to implement the abstract methods,
# but with formulas appropriate for rectangles.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# What we accomplished in this step:
# - Created Rectangle class that inherits from Shape
# - Implemented both abstract methods with rectangle formulas


# Step 6: Test our abstract classes
# ===============================================================================

# Explanation:
# Let's create instances and test our implementation. Note that we cannot
# instantiate the abstract Shape class directly.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Test our classes:
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle with radius 5:")
print(f"  Area: {circle.area():.2f}")
print(f"  Perimeter: {circle.perimeter():.2f}")

print(f"\nRectangle 4x6:")
print(f"  Area: {rectangle.area()}")
print(f"  Perimeter: {rectangle.perimeter()}")

# Demonstrate polymorphism:
shapes = [Circle(3), Rectangle(5, 8), Circle(2)]
print(f"\nCalculating areas for multiple shapes:")
for i, shape in enumerate(shapes):
    print(f"  Shape {i+1} area: {shape.area():.2f}")

# Try to create abstract class instance (this will fail):
try:
    shape = Shape()
except TypeError as e:
    print(f"\nCannot instantiate abstract class: {e}")

# What we accomplished in this step:
# - Created and tested concrete instances
# - Demonstrated polymorphism with different shapes
# - Showed that abstract classes cannot be instantiated


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Abstract base classes using ABC
# - The @abstractmethod decorator
# - Implementing abstract methods in concrete subclasses
# - Polymorphism with abstract classes
# - Why abstract classes cannot be instantiated
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a Triangle class!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================