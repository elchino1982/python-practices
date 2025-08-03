"""Question: Create an abstract interface Drawable with an abstract method draw().
Implement classes Circle, Rectangle, and Text that implement this interface.
Create a Canvas class that can draw multiple drawable objects.
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
# - How do you create an interface using ABC?
# - What should the draw() method return or do?
# - How can a Canvas store and manage multiple drawable objects?
# - What is the benefit of programming to an interface?
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


# Step 1: Create the Drawable interface
# ===============================================================================

# Explanation:
# An interface defines a contract that implementing classes must follow.
# In Python, we use abstract base classes to create interfaces.

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        """Draw the object and return a string representation"""
        pass

# What we accomplished in this step:
# - Created the Drawable interface with an abstract draw() method


# Step 2: Implement the Circle class
# ===============================================================================

# Explanation:
# The Circle class implements the Drawable interface by providing
# a concrete implementation of the draw() method.

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        """Draw the object and return a string representation"""
        pass

class Circle(Drawable):
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Circle: radius={self.radius} at ({self.x}, {self.y})"

# What we accomplished in this step:
# - Created Circle class that implements Drawable interface
# - Added position coordinates for more realistic drawing


# Step 3: Implement the Rectangle class
# ===============================================================================

# Explanation:
# The Rectangle class also implements the Drawable interface with
# its own specific draw() implementation.

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        """Draw the object and return a string representation"""
        pass

class Circle(Drawable):
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Circle: radius={self.radius} at ({self.x}, {self.y})"

class Rectangle(Drawable):
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Rectangle: {self.width}x{self.height} at ({self.x}, {self.y})"

# What we accomplished in this step:
# - Created Rectangle class that implements Drawable interface


# Step 4: Implement the Text class
# ===============================================================================

# Explanation:
# The Text class shows how different types of objects can implement
# the same interface in their own unique way.

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        """Draw the object and return a string representation"""
        pass

class Circle(Drawable):
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Circle: radius={self.radius} at ({self.x}, {self.y})"

class Rectangle(Drawable):
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Rectangle: {self.width}x{self.height} at ({self.x}, {self.y})"

class Text(Drawable):
    def __init__(self, content, font_size=12, x=0, y=0):
        self.content = content
        self.font_size = font_size
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Text: '{self.content}' (size {self.font_size}) at ({self.x}, {self.y})"

# What we accomplished in this step:
# - Created Text class that implements Drawable interface
# - Added font size for more realistic text rendering


# Step 5: Create the Canvas class
# ===============================================================================

# Explanation:
# The Canvas class manages a collection of drawable objects and can
# render them all. This demonstrates the power of programming to interfaces.

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        """Draw the object and return a string representation"""
        pass

class Circle(Drawable):
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Circle: radius={self.radius} at ({self.x}, {self.y})"

class Rectangle(Drawable):
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Rectangle: {self.width}x{self.height} at ({self.x}, {self.y})"

class Text(Drawable):
    def __init__(self, content, font_size=12, x=0, y=0):
        self.content = content
        self.font_size = font_size
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Text: '{self.content}' (size {self.font_size}) at ({self.x}, {self.y})"

class Canvas:
    def __init__(self):
        self.objects = []
    
    def add_object(self, drawable_object):
        if not isinstance(drawable_object, Drawable):
            raise TypeError("Object must implement Drawable interface")
        self.objects.append(drawable_object)
    
    def draw_all(self):
        print("=== Canvas Rendering ===")
        for i, obj in enumerate(self.objects):
            print(f"{i+1}. {obj.draw()}")
        print("=== End Rendering ===")
    
    def clear(self):
        self.objects.clear()
        print("Canvas cleared")

# What we accomplished in this step:
# - Created Canvas class that works with any Drawable object
# - Added type checking to ensure objects implement the interface
# - Demonstrated polymorphism through the draw_all() method


# Step 6: Test our interface design
# ===============================================================================

# Explanation:
# Let's create various drawable objects and use them with our Canvas
# to demonstrate the power of interface-based design.

from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        """Draw the object and return a string representation"""
        pass

class Circle(Drawable):
    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Circle: radius={self.radius} at ({self.x}, {self.y})"

class Rectangle(Drawable):
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Rectangle: {self.width}x{self.height} at ({self.x}, {self.y})"

class Text(Drawable):
    def __init__(self, content, font_size=12, x=0, y=0):
        self.content = content
        self.font_size = font_size
        self.x = x
        self.y = y
    
    def draw(self):
        return f"Drawing Text: '{self.content}' (size {self.font_size}) at ({self.x}, {self.y})"

class Canvas:
    def __init__(self):
        self.objects = []
    
    def add_object(self, drawable_object):
        if not isinstance(drawable_object, Drawable):
            raise TypeError("Object must implement Drawable interface")
        self.objects.append(drawable_object)
    
    def draw_all(self):
        print("=== Canvas Rendering ===")
        for i, obj in enumerate(self.objects):
            print(f"{i+1}. {obj.draw()}")
        print("=== End Rendering ===")
    
    def clear(self):
        self.objects.clear()
        print("Canvas cleared")

# Test our interface design:
canvas = Canvas()

# Create various drawable objects
circle = Circle(5, 10, 20)
rectangle = Rectangle(15, 8, 5, 15)
title = Text("My Drawing", 24, 50, 5)
subtitle = Text("Created with Python", 14, 55, 30)

# Add objects to canvas
canvas.add_object(circle)
canvas.add_object(rectangle)
canvas.add_object(title)
canvas.add_object(subtitle)

# Draw everything
canvas.draw_all()

print("\nAdding more objects:")
canvas.add_object(Circle(3, 100, 100))
canvas.add_object(Text("Bottom text", 10, 0, 200))

canvas.draw_all()

# Test error handling
print("\nTesting error handling:")
try:
    canvas.add_object("Not a drawable object")
except TypeError as e:
    print(f"Error caught: {e}")

# What we accomplished in this step:
# - Created and tested various drawable objects
# - Demonstrated polymorphism with the Canvas class
# - Showed error handling for invalid objects


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Interface design using abstract base classes
# - Programming to interfaces, not implementations
# - Polymorphism through common interfaces
# - Type checking with isinstance()
# - The benefits of loose coupling through interfaces
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding Line or Polygon classes!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================