"""Question: Implement the Bridge pattern to separate abstraction from implementation.

Create a drawing application where shapes (Circle, Rectangle) can be drawn
using different rendering engines (Vector, Raster) without tight coupling.

Requirements:
1. Create DrawingAPI interface for rendering implementations
2. Implement concrete drawing APIs (VectorRenderer, RasterRenderer)
3. Create abstract Shape class that uses DrawingAPI
4. Implement concrete shapes (Circle, Rectangle)
5. Demonstrate how shapes and renderers can vary independently
6. Show how new shapes or renderers can be added easily

Example usage:
    vector_api = VectorRenderer()
    circle = Circle(vector_api, 5, 10, 15)
    circle.draw()
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
# - What is the abstraction (shapes) and what is the implementation (renderers)?
# - How can you separate them so they can vary independently?
# - What interface do you need for the implementation side?
# - How does the abstraction use the implementation?
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


# Step 1: Import modules and create the implementation interface
# ===============================================================================

# Explanation:
# The Bridge pattern starts with defining the implementation interface.
# This interface will be used by different concrete implementations (renderers).

from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    """Abstract interface for drawing implementations."""
    
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle at given position with given radius."""
        pass
    
    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle at given position with given dimensions."""
        pass

# What we accomplished in this step:
# - Created the implementation interface (DrawingAPI)
# - Defined abstract methods for drawing operations


# Step 2: Create concrete implementations (renderers)
# ===============================================================================

# Explanation:
# Concrete implementations provide specific ways to render shapes.
# Each renderer can have its own unique approach and features.

from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    """Abstract interface for drawing implementations."""
    
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle at given position with given radius."""
        pass
    
    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle at given position with given dimensions."""
        pass

class VectorRenderer(DrawingAPI):
    """Vector-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using vector graphics."""
        print(f"Vector: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Vector: Using smooth curves and scalable graphics")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using vector graphics."""
        print(f"Vector: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Vector: Using crisp edges and infinite scalability")

class RasterRenderer(DrawingAPI):
    """Raster-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using raster graphics."""
        print(f"Raster: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Raster: Using pixel-based rendering with anti-aliasing")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using raster graphics."""
        print(f"Raster: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Raster: Using bitmap graphics with texture support")

# What we accomplished in this step:
# - Created VectorRenderer for vector-based graphics
# - Created RasterRenderer for pixel-based graphics
# - Each renderer has its own unique characteristics


# Step 3: Create the abstraction base class
# ===============================================================================

# Explanation:
# The abstraction defines the interface that clients use.
# It maintains a reference to an implementation object and delegates work to it.

from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    """Abstract interface for drawing implementations."""
    
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle at given position with given radius."""
        pass
    
    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle at given position with given dimensions."""
        pass

class VectorRenderer(DrawingAPI):
    """Vector-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using vector graphics."""
        print(f"Vector: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Vector: Using smooth curves and scalable graphics")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using vector graphics."""
        print(f"Vector: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Vector: Using crisp edges and infinite scalability")

class RasterRenderer(DrawingAPI):
    """Raster-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using raster graphics."""
        print(f"Raster: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Raster: Using pixel-based rendering with anti-aliasing")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using raster graphics."""
        print(f"Raster: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Raster: Using bitmap graphics with texture support")

class Shape(ABC):
    """Abstract shape class that uses DrawingAPI."""
    
    def __init__(self, drawing_api: DrawingAPI):
        """Initialize shape with a drawing API implementation."""
        self.drawing_api = drawing_api
    
    @abstractmethod
    def draw(self):
        """Draw the shape using the drawing API."""
        pass
    
    @abstractmethod
    def resize(self, factor: float):
        """Resize the shape by given factor."""
        pass

# What we accomplished in this step:
# - Created abstract Shape class that holds a DrawingAPI reference
# - Defined abstract methods for shape operations
# - Established the bridge between abstraction and implementation


# Step 4: Create concrete shape implementations
# ===============================================================================

# Explanation:
# Concrete shapes implement the abstraction interface and use the
# implementation (DrawingAPI) to perform actual drawing operations.

from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    """Abstract interface for drawing implementations."""
    
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle at given position with given radius."""
        pass
    
    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle at given position with given dimensions."""
        pass

class VectorRenderer(DrawingAPI):
    """Vector-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using vector graphics."""
        print(f"Vector: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Vector: Using smooth curves and scalable graphics")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using vector graphics."""
        print(f"Vector: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Vector: Using crisp edges and infinite scalability")

class RasterRenderer(DrawingAPI):
    """Raster-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using raster graphics."""
        print(f"Raster: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Raster: Using pixel-based rendering with anti-aliasing")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using raster graphics."""
        print(f"Raster: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Raster: Using bitmap graphics with texture support")

class Shape(ABC):
    """Abstract shape class that uses DrawingAPI."""
    
    def __init__(self, drawing_api: DrawingAPI):
        """Initialize shape with a drawing API implementation."""
        self.drawing_api = drawing_api
    
    @abstractmethod
    def draw(self):
        """Draw the shape using the drawing API."""
        pass
    
    @abstractmethod
    def resize(self, factor: float):
        """Resize the shape by given factor."""
        pass

class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, drawing_api: DrawingAPI, x: float, y: float, radius: float):
        """Initialize circle with position and radius."""
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        """Draw the circle using the drawing API."""
        print(f"Circle: Preparing to draw at ({self.x}, {self.y}) with radius {self.radius}")
        self.drawing_api.draw_circle(self.x, self.y, self.radius)
    
    def resize(self, factor: float):
        """Resize the circle by changing its radius."""
        self.radius *= factor
        print(f"Circle: Resized to radius {self.radius}")

class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, drawing_api: DrawingAPI, x: float, y: float, width: float, height: float):
        """Initialize rectangle with position and dimensions."""
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        """Draw the rectangle using the drawing API."""
        print(f"Rectangle: Preparing to draw at ({self.x}, {self.y}) with size {self.width}x{self.height}")
        self.drawing_api.draw_rectangle(self.x, self.y, self.width, self.height)
    
    def resize(self, factor: float):
        """Resize the rectangle by scaling its dimensions."""
        self.width *= factor
        self.height *= factor
        print(f"Rectangle: Resized to {self.width}x{self.height}")

# What we accomplished in this step:
# - Created Circle class with position and radius
# - Created Rectangle class with position and dimensions
# - Both shapes use the DrawingAPI to perform actual rendering


# Step 5: Add advanced renderer with additional features
# ===============================================================================

# Explanation:
# Let's add a more advanced renderer to show how easily new implementations
# can be added without affecting existing shapes or other renderers.

from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    """Abstract interface for drawing implementations."""
    
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle at given position with given radius."""
        pass
    
    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle at given position with given dimensions."""
        pass

class VectorRenderer(DrawingAPI):
    """Vector-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using vector graphics."""
        print(f"Vector: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Vector: Using smooth curves and scalable graphics")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using vector graphics."""
        print(f"Vector: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Vector: Using crisp edges and infinite scalability")

class RasterRenderer(DrawingAPI):
    """Raster-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using raster graphics."""
        print(f"Raster: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Raster: Using pixel-based rendering with anti-aliasing")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using raster graphics."""
        print(f"Raster: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Raster: Using bitmap graphics with texture support")

class OpenGLRenderer(DrawingAPI):
    """OpenGL-based 3D rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using OpenGL."""
        print(f"OpenGL: Rendering 3D circle at ({x}, {y}) with radius {radius}")
        print(f"OpenGL: Using hardware acceleration and shaders")
        print(f"OpenGL: Applying lighting and shadow effects")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using OpenGL."""
        print(f"OpenGL: Rendering 3D rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"OpenGL: Using GPU-accelerated rendering pipeline")
        print(f"OpenGL: Applying advanced material properties")

class Shape(ABC):
    """Abstract shape class that uses DrawingAPI."""
    
    def __init__(self, drawing_api: DrawingAPI):
        """Initialize shape with a drawing API implementation."""
        self.drawing_api = drawing_api
    
    @abstractmethod
    def draw(self):
        """Draw the shape using the drawing API."""
        pass
    
    @abstractmethod
    def resize(self, factor: float):
        """Resize the shape by given factor."""
        pass

class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, drawing_api: DrawingAPI, x: float, y: float, radius: float):
        """Initialize circle with position and radius."""
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        """Draw the circle using the drawing API."""
        print(f"Circle: Preparing to draw at ({self.x}, {self.y}) with radius {self.radius}")
        self.drawing_api.draw_circle(self.x, self.y, self.radius)
    
    def resize(self, factor: float):
        """Resize the circle by changing its radius."""
        self.radius *= factor
        print(f"Circle: Resized to radius {self.radius}")

class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, drawing_api: DrawingAPI, x: float, y: float, width: float, height: float):
        """Initialize rectangle with position and dimensions."""
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        """Draw the rectangle using the drawing API."""
        print(f"Rectangle: Preparing to draw at ({self.x}, {self.y}) with size {self.width}x{self.height}")
        self.drawing_api.draw_rectangle(self.x, self.y, self.width, self.height)
    
    def resize(self, factor: float):
        """Resize the rectangle by scaling its dimensions."""
        self.width *= factor
        self.height *= factor
        print(f"Rectangle: Resized to {self.width}x{self.height}")

# What we accomplished in this step:
# - Added OpenGLRenderer with advanced 3D capabilities
# - Showed how new implementations can be added easily
# - Existing shapes work with new renderer without modification


# Step 6: Test the complete Bridge pattern implementation
# ===============================================================================

# Explanation:
# Let's test our Bridge pattern implementation to show how shapes and
# renderers can vary independently and be combined in any way.

from abc import ABC, abstractmethod

class DrawingAPI(ABC):
    """Abstract interface for drawing implementations."""
    
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle at given position with given radius."""
        pass
    
    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle at given position with given dimensions."""
        pass

class VectorRenderer(DrawingAPI):
    """Vector-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using vector graphics."""
        print(f"Vector: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Vector: Using smooth curves and scalable graphics")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using vector graphics."""
        print(f"Vector: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Vector: Using crisp edges and infinite scalability")

class RasterRenderer(DrawingAPI):
    """Raster-based rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using raster graphics."""
        print(f"Raster: Drawing circle at ({x}, {y}) with radius {radius}")
        print(f"Raster: Using pixel-based rendering with anti-aliasing")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using raster graphics."""
        print(f"Raster: Drawing rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"Raster: Using bitmap graphics with texture support")

class OpenGLRenderer(DrawingAPI):
    """OpenGL-based 3D rendering implementation."""
    
    def draw_circle(self, x: float, y: float, radius: float):
        """Draw a circle using OpenGL."""
        print(f"OpenGL: Rendering 3D circle at ({x}, {y}) with radius {radius}")
        print(f"OpenGL: Using hardware acceleration and shaders")
        print(f"OpenGL: Applying lighting and shadow effects")
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float):
        """Draw a rectangle using OpenGL."""
        print(f"OpenGL: Rendering 3D rectangle at ({x}, {y}) with size {width}x{height}")
        print(f"OpenGL: Using GPU-accelerated rendering pipeline")
        print(f"OpenGL: Applying advanced material properties")

class Shape(ABC):
    """Abstract shape class that uses DrawingAPI."""
    
    def __init__(self, drawing_api: DrawingAPI):
        """Initialize shape with a drawing API implementation."""
        self.drawing_api = drawing_api
    
    @abstractmethod
    def draw(self):
        """Draw the shape using the drawing API."""
        pass
    
    @abstractmethod
    def resize(self, factor: float):
        """Resize the shape by given factor."""
        pass

class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, drawing_api: DrawingAPI, x: float, y: float, radius: float):
        """Initialize circle with position and radius."""
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        """Draw the circle using the drawing API."""
        print(f"Circle: Preparing to draw at ({self.x}, {self.y}) with radius {self.radius}")
        self.drawing_api.draw_circle(self.x, self.y, self.radius)
    
    def resize(self, factor: float):
        """Resize the circle by changing its radius."""
        self.radius *= factor
        print(f"Circle: Resized to radius {self.radius}")

class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, drawing_api: DrawingAPI, x: float, y: float, width: float, height: float):
        """Initialize rectangle with position and dimensions."""
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        """Draw the rectangle using the drawing API."""
        print(f"Rectangle: Preparing to draw at ({self.x}, {self.y}) with size {self.width}x{self.height}")
        self.drawing_api.draw_rectangle(self.x, self.y, self.width, self.height)
    
    def resize(self, factor: float):
        """Resize the rectangle by scaling its dimensions."""
        self.width *= factor
        self.height *= factor
        print(f"Rectangle: Resized to {self.width}x{self.height}")

print("=== Testing Bridge Pattern ===\n")

# Create different renderers
vector_api = VectorRenderer()
raster_api = RasterRenderer()
opengl_api = OpenGLRenderer()

print("1. Circle with Vector Renderer:")
circle1 = Circle(vector_api, 10, 20, 5)
circle1.draw()
print()

print("2. Circle with Raster Renderer:")
circle2 = Circle(raster_api, 15, 25, 8)
circle2.draw()
print()

print("3. Rectangle with OpenGL Renderer:")
rect1 = Rectangle(opengl_api, 0, 0, 100, 50)
rect1.draw()
print()

print("4. Rectangle with Vector Renderer:")
rect2 = Rectangle(vector_api, 30, 40, 80, 60)
rect2.draw()
print()

print("5. Testing resize functionality:")
print("Before resize:")
circle1.draw()
print("\nAfter resize (factor 2.0):")
circle1.resize(2.0)
circle1.draw()
print()

print("6. Demonstrating independence - same shape, different renderers:")
shapes_with_different_renderers = [
    Circle(vector_api, 50, 50, 10),
    Circle(raster_api, 50, 50, 10),
    Circle(opengl_api, 50, 50, 10)
]

for i, shape in enumerate(shapes_with_different_renderers, 1):
    print(f"Same circle with renderer {i}:")
    shape.draw()
    print()

# What we accomplished in this step:
# - Tested all combinations of shapes and renderers
# - Demonstrated independent variation of abstractions and implementations
# - Showed how the same shape can use different renderers
# - Verified that resize functionality works correctly


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step Bridge pattern solution!
#
# Key concepts learned:
# - Bridge pattern structure and purpose
# - Separation of abstraction from implementation
# - Implementation interface (DrawingAPI) and concrete implementations
# - Abstract shape class and concrete shape implementations
# - Independent variation of abstractions and implementations
# - Easy extensibility for new shapes or renderers
#
# Benefits of the Bridge pattern:
# - Decouples abstraction from implementation
# - Both can vary independently
# - Easy to add new shapes or renderers
# - Promotes composition over inheritance
# - Reduces the number of classes needed
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a Triangle shape or SVG renderer!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
