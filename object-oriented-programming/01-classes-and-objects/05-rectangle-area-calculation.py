"""Question: Define a class named Rectangle with attributes length and width.
Add methods to calculate the area and perimeter of the rectangle.
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
# - What attributes does the class need?
# - What methods should you implement?
# - How do the methods interact with the attributes?
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


# Step 1: Define the Rectangle class
# ===============================================================================

# Explanation:
# Let's start by creating our Rectangle class. In Python, we use the 'class' keyword 
# followed by the class name. Class names should follow PascalCase convention.

class Rectangle:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Rectangle class structure


# Step 2: Add the constructor (__init__ method)
# ===============================================================================

# Explanation:
# The __init__ method is called when we create a new instance of the class.
# It's where we initialize the object's attributes. The 'self' parameter refers to the instance being created.

class Rectangle:
    def __init__(self, length, width):
        # We'll add attribute assignments next
        pass

# What we accomplished in this step:
# - Added the constructor method to initialize new instances


# Step 3: Initialize the attributes
# ===============================================================================

# Explanation:
# Now let's assign the parameters to instance attributes. Each attribute will store 
# the data for this specific instance of the class.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

# What we accomplished in this step:
# - Initialized all necessary attributes for the class


# Step 4: Add the area method
# ===============================================================================

# Explanation:
# Now let's add the area method that calculates and returns the area of the rectangle.
# This method will use the attributes we defined earlier (length * width).

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# What we accomplished in this step:
# - Added the area method with its calculation


# Step 5: Add the perimeter method
# ===============================================================================

# Explanation:
# Now let's add the perimeter method that calculates and returns the perimeter of the rectangle.
# This method will also use the attributes we defined earlier (2 * (length + width)).

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# What we accomplished in this step:
# - Added the perimeter method with its calculation


# Step 6: Create an instance and test our class
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our class and test it to make sure everything works correctly.
# This demonstrates how to use the class we just created.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Test our class:
rectangle = Rectangle(5, 3)
print(rectangle.area())       # Output: 15
print(rectangle.perimeter())  # Output: 16

# What we accomplished in this step:
# - Created and tested our complete Rectangle implementation


# ===============================================================================
# CONGRATULATIONS! 
# 
# You've successfully completed the step-by-step solution!
# 
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications
# 
# Remember: The best way to learn is by doing!
# ===============================================================================
