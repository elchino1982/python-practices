"""Question: Define a class Shape with a method area.
Create subclasses Circle and Rectangle that implement the area method.
Ensure the classes are open for extension but closed for modification.
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
# - What is the Open/Closed Principle (OCP)?
# - How do you create a base class that can be extended but not modified?
# - What role does inheritance play in OCP?
# - How does polymorphism support the Open/Closed Principle?
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


# Step 1: Create the abstract base Shape class
# ===============================================================================

# Explanation:
# Let's start by creating the Shape base class that defines the interface
# for all shapes. This class is "closed for modification" but provides
# a foundation for extension.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created abstract base class that defines the interface
# - Used NotImplementedError to enforce implementation in subclasses
# - This class is now "closed for modification" - we won't change it


# Step 2: Create Circle class that extends Shape
# ===============================================================================

# Explanation:
# Now let's create a Circle class that inherits from Shape and implements
# its own area calculation. This demonstrates "open for extension".

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# What we accomplished in this step:
# - Extended Shape without modifying it (open for extension)
# - Implemented specific area calculation for circles
# - Followed the contract defined by the base class


# Step 3: Create Rectangle class that extends Shape
# ===============================================================================

# Explanation:
# Let's add a Rectangle class that also extends Shape. Notice how we can
# add new functionality without modifying existing code.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# What we accomplished in this step:
# - Added Rectangle without modifying Shape or Circle
# - Demonstrated how OCP enables easy extension
# - Each shape has its own specific implementation


# Step 4: Test our OCP-compliant design
# ===============================================================================

# Explanation:
# Let's test our design to see how polymorphism works with our
# OCP-compliant shape hierarchy.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Test our OCP-compliant design:
print("=== Testing OCP-Compliant Shape Design ===")

shapes = [Circle(5), Rectangle(4, 6)]

print("Calculating areas using polymorphism:")
for i, shape in enumerate(shapes, 1):
    shape_name = shape.__class__.__name__
    area = shape.area()
    print(f"Shape {i} ({shape_name}): Area = {area}")

# What we accomplished in this step:
# - Demonstrated polymorphism with different shape types
# - Showed how the same interface works for all shapes
# - Verified that our OCP design works correctly


# Step 5: Demonstrate extension by adding Triangle
# ===============================================================================

# Explanation:
# Let's prove that our design follows OCP by adding a new Triangle class
# without modifying any existing code.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Adding Triangle without modifying existing code (OCP in action!)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

print("\n=== Demonstrating Extension (Adding Triangle) ===")

# Test with all shapes including the new Triangle
all_shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

print("All shapes working together:")
for shape in all_shapes:
    shape_name = shape.__class__.__name__
    area = shape.area()
    print(f"{shape_name}: Area = {area}")

# What we accomplished in this step:
# - Added Triangle without modifying Shape, Circle, or Rectangle
# - Demonstrated "open for extension, closed for modification"
# - Showed how new functionality integrates seamlessly


# Step 6: Enhanced example with additional methods
# ===============================================================================

# Explanation:
# Let's create a more comprehensive example that shows how OCP works
# with multiple methods and more complex functionality.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_info(self):
        return f"{self.__class__.__name__}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Adding Square as a special case of Rectangle (inheritance hierarchy)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Shape processor that works with any shape (OCP benefit)
class ShapeProcessor:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def calculate_total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def calculate_total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)

    def generate_report(self):
        print("Shape Analysis Report")
        print("=" * 40)
        
        for i, shape in enumerate(self.shapes, 1):
            print(f"{i}. {shape.get_info()}")
        
        print("=" * 40)
        print(f"Total Area: {self.calculate_total_area():.2f}")
        print(f"Total Perimeter: {self.calculate_total_perimeter():.2f}")
        print(f"Number of Shapes: {len(self.shapes)}")

# Test enhanced OCP design:
print("\n=== Enhanced OCP Design with Shape Processor ===")

processor = ShapeProcessor()

# Add various shapes
processor.add_shape(Circle(5))
processor.add_shape(Rectangle(4, 6))
processor.add_shape(Triangle(3, 4, 5))
processor.add_shape(Square(7))

# Generate comprehensive report
processor.generate_report()

# Demonstrate adding a new shape type
class Pentagon(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Regular pentagon area formula
        return (1.720477 * self.side ** 2)

    def perimeter(self):
        return 5 * self.side

print("\n=== Adding Pentagon without modifying existing code ===")
processor.add_shape(Pentagon(4))
processor.generate_report()

# What we accomplished in this step:
# - Extended the system with multiple methods (area, perimeter, get_info)
# - Created a processor that works with any shape type
# - Added inheritance hierarchy (Square extends Rectangle)
# - Demonstrated how OCP enables complex system extension
# - Showed that new shapes integrate seamlessly with existing processors


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the Open/Closed Principle solution!
#
# Key concepts learned:
# - Understanding the Open/Closed Principle (OCP)
# - Creating abstract base classes that define interfaces
# - Using inheritance to extend functionality without modification
# - Benefits of polymorphism in OCP-compliant design
# - How OCP enables easy system extension and maintenance
# - Creating processors that work with any conforming type
#
# OCP Benefits demonstrated:
# - New shape types can be added without changing existing code
# - Existing shapes continue to work when new ones are added
# - System processors work with any shape type automatically
# - Code is more maintainable and less prone to bugs
# - Follows "open for extension, closed for modification" principle
#
# Real-world applications:
# - Plugin architectures (add new plugins without changing core)
# - Payment processing systems (add new payment methods)
# - File format handlers (add new formats without changing existing code)
# - Game entities (add new character types, weapons, etc.)
# - Reporting systems (add new report types)
# - Drawing applications (add new shape tools)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY inheritance enables extension without modification
# 4. Experiment with adding new shape types (Hexagon, Octagon, etc.)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
