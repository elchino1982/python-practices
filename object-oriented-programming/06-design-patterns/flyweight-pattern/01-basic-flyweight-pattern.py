"""Question: Implement the Flyweight pattern to minimize memory usage with large numbers of objects.

Create a text editor that efficiently handles large documents by sharing
character formatting objects (font, size, color) among multiple characters.

Requirements:
1. Create CharacterFlyweight interface
2. Implement concrete flyweights for different character formats
3. Create FlyweightFactory to manage and reuse flyweights
4. Implement Context class to store extrinsic state
5. Demonstrate memory savings with large numbers of characters
6. Show intrinsic vs extrinsic state separation

Example usage:
    factory = CharacterFlyweightFactory()
    doc = Document()
    doc.add_character('H', 0, "Arial", 12, "Black")
    doc.add_character('e', 1, "Arial", 12, "Black")  # Reuses flyweight
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
# - What is intrinsic vs extrinsic state?
# - How can you share objects to save memory?
# - What is the role of a factory in this pattern?
# - How do you separate shared state from context-specific state?
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


# Step 1: Define the Flyweight Interface
# ===============================================================================

# Explanation:
# The Flyweight pattern separates intrinsic state (shared) from extrinsic state.
# We start by defining the interface that all flyweights must implement.

from abc import ABC, abstractmethod

class Flyweight(ABC):
    """Abstract flyweight interface."""
    
    @abstractmethod
    def operation(self, extrinsic_state):
        """Perform operation using extrinsic state."""
        pass

# What we accomplished in this step:
# - Created abstract flyweight interface
# - Defined operation method that accepts extrinsic state


# Step 2: Implement Concrete Flyweight
# ===============================================================================

# Explanation:
# Concrete flyweights store intrinsic state and implement the operation.
# They should be immutable and shareable.

from abc import ABC, abstractmethod

class Flyweight(ABC):
    """Abstract flyweight interface."""
    
    @abstractmethod
    def operation(self, extrinsic_state):
        """Perform operation using extrinsic state."""
        pass

class CharacterFlyweight(Flyweight):
    """Concrete flyweight for characters."""
    
    def __init__(self, font, size, color):
        # Intrinsic state - shared among all instances with same values
        self._font = font
        self._size = size
        self._color = color
    
    def operation(self, extrinsic_state):
        """Render character at specific position."""
        char, x, y = extrinsic_state
        return f"Rendering '{char}' at ({x}, {y}) with {self._font} {self._size}pt in {self._color}"
    
    def get_intrinsic_state(self):
        """Get the intrinsic state for debugging."""
        return f"{self._font}-{self._size}-{self._color}"

# What we accomplished in this step:
# - Implemented concrete flyweight with intrinsic state
# - Created operation method that uses extrinsic state
# - Ensured flyweight is immutable


# Step 3: Create Flyweight Factory
# ===============================================================================

# Explanation:
# The factory manages flyweight instances and ensures sharing.
# It creates new flyweights only when necessary.

from abc import ABC, abstractmethod

class Flyweight(ABC):
    """Abstract flyweight interface."""
    
    @abstractmethod
    def operation(self, extrinsic_state):
        """Perform operation using extrinsic state."""
        pass

class CharacterFlyweight(Flyweight):
    """Concrete flyweight for characters."""
    
    def __init__(self, font, size, color):
        # Intrinsic state - shared among all instances with same values
        self._font = font
        self._size = size
        self._color = color
    
    def operation(self, extrinsic_state):
        """Render character at specific position."""
        char, x, y = extrinsic_state
        return f"Rendering '{char}' at ({x}, {y}) with {self._font} {self._size}pt in {self._color}"
    
    def get_intrinsic_state(self):
        """Get the intrinsic state for debugging."""
        return f"{self._font}-{self._size}-{self._color}"

class FlyweightFactory:
    """Factory to manage and share flyweight instances."""
    
    def __init__(self):
        self._flyweights = {}
    
    def get_flyweight(self, font, size, color):
        """Get or create flyweight with given intrinsic state."""
        key = f"{font}-{size}-{color}"
        
        if key not in self._flyweights:
            print(f"Creating new flyweight: {key}")
            self._flyweights[key] = CharacterFlyweight(font, size, color)
        else:
            print(f"Reusing existing flyweight: {key}")
        
        return self._flyweights[key]
    
    def get_flyweight_count(self):
        """Get total number of flyweight instances."""
        return len(self._flyweights)
    
    def list_flyweights(self):
        """List all flyweight keys."""
        return list(self._flyweights.keys())

# What we accomplished in this step:
# - Created factory to manage flyweight instances
# - Implemented sharing mechanism to reuse flyweights
# - Added debugging methods to track flyweight usage


# Step 4: Create Context Class
# ===============================================================================

# Explanation:
# The context class stores extrinsic state and uses flyweights.
# It maintains the relationship between flyweights and their context.

from abc import ABC, abstractmethod

class Flyweight(ABC):
    """Abstract flyweight interface."""
    
    @abstractmethod
    def operation(self, extrinsic_state):
        """Perform operation using extrinsic state."""
        pass

class CharacterFlyweight(Flyweight):
    """Concrete flyweight for characters."""
    
    def __init__(self, font, size, color):
        # Intrinsic state - shared among all instances with same values
        self._font = font
        self._size = size
        self._color = color
    
    def operation(self, extrinsic_state):
        """Render character at specific position."""
        char, x, y = extrinsic_state
        return f"Rendering '{char}' at ({x}, {y}) with {self._font} {self._size}pt in {self._color}"
    
    def get_intrinsic_state(self):
        """Get the intrinsic state for debugging."""
        return f"{self._font}-{self._size}-{self._color}"

class FlyweightFactory:
    """Factory to manage and share flyweight instances."""
    
    def __init__(self):
        self._flyweights = {}
    
    def get_flyweight(self, font, size, color):
        """Get or create flyweight with given intrinsic state."""
        key = f"{font}-{size}-{color}"
        
        if key not in self._flyweights:
            print(f"Creating new flyweight: {key}")
            self._flyweights[key] = CharacterFlyweight(font, size, color)
        else:
            print(f"Reusing existing flyweight: {key}")
        
        return self._flyweights[key]
    
    def get_flyweight_count(self):
        """Get total number of flyweight instances."""
        return len(self._flyweights)
    
    def list_flyweights(self):
        """List all flyweight keys."""
        return list(self._flyweights.keys())

class Character:
    """Context class that stores extrinsic state."""
    
    def __init__(self, char, x, y, flyweight):
        # Extrinsic state - specific to this character instance
        self.char = char
        self.x = x
        self.y = y
        # Reference to shared flyweight
        self.flyweight = flyweight
    
    def render(self):
        """Render this character using its flyweight."""
        extrinsic_state = (self.char, self.x, self.y)
        return self.flyweight.operation(extrinsic_state)
    
    def move(self, new_x, new_y):
        """Move character to new position."""
        self.x = new_x
        self.y = new_y

class Document:
    """Document that contains many characters."""
    
    def __init__(self):
        self.characters = []
        self.factory = FlyweightFactory()
    
    def add_character(self, char, x, y, font="Arial", size=12, color="Black"):
        """Add a character to the document."""
        flyweight = self.factory.get_flyweight(font, size, color)
        character = Character(char, x, y, flyweight)
        self.characters.append(character)
    
    def render_document(self):
        """Render all characters in the document."""
        print("Rendering document:")
        for char in self.characters:
            print(f"  {char.render()}")
    
    def get_statistics(self):
        """Get document statistics."""
        return {
            'total_characters': len(self.characters),
            'unique_flyweights': self.factory.get_flyweight_count(),
            'memory_saved': len(self.characters) - self.factory.get_flyweight_count()
        }

# What we accomplished in this step:
# - Created Character context class with extrinsic state
# - Implemented Document class to manage multiple characters
# - Demonstrated separation of intrinsic and extrinsic state
# - Added statistics to show memory savings


# Step 5: Advanced Flyweight Example
# ===============================================================================

# Explanation:
# Let's create a more complex example with different types of flyweights
# and demonstrate the pattern's effectiveness with large datasets.

from abc import ABC, abstractmethod
import random

class Flyweight(ABC):
    """Abstract flyweight interface."""
    
    @abstractmethod
    def operation(self, extrinsic_state):
        """Perform operation using extrinsic state."""
        pass

class CharacterFlyweight(Flyweight):
    """Concrete flyweight for characters."""
    
    def __init__(self, font, size, color):
        # Intrinsic state - shared among all instances with same values
        self._font = font
        self._size = size
        self._color = color
    
    def operation(self, extrinsic_state):
        """Render character at specific position."""
        char, x, y = extrinsic_state
        return f"Rendering '{char}' at ({x}, {y}) with {self._font} {self._size}pt in {self._color}"
    
    def get_intrinsic_state(self):
        """Get the intrinsic state for debugging."""
        return f"{self._font}-{self._size}-{self._color}"

class IconFlyweight(Flyweight):
    """Concrete flyweight for icons."""
    
    def __init__(self, icon_type, size):
        self._icon_type = icon_type
        self._size = size
    
    def operation(self, extrinsic_state):
        """Render icon at specific position."""
        x, y, tooltip = extrinsic_state
        return f"Rendering {self._icon_type} icon ({self._size}px) at ({x}, {y}) with tooltip: '{tooltip}'"
    
    def get_intrinsic_state(self):
        """Get the intrinsic state for debugging."""
        return f"{self._icon_type}-{self._size}"

class FlyweightFactory:
    """Factory to manage and share flyweight instances."""
    
    def __init__(self):
        self._flyweights = {}
    
    def get_character_flyweight(self, font, size, color):
        """Get or create character flyweight."""
        key = f"char-{font}-{size}-{color}"
        
        if key not in self._flyweights:
            self._flyweights[key] = CharacterFlyweight(font, size, color)
        
        return self._flyweights[key]
    
    def get_icon_flyweight(self, icon_type, size):
        """Get or create icon flyweight."""
        key = f"icon-{icon_type}-{size}"
        
        if key not in self._flyweights:
            self._flyweights[key] = IconFlyweight(icon_type, size)
        
        return self._flyweights[key]
    
    def get_flyweight_count(self):
        """Get total number of flyweight instances."""
        return len(self._flyweights)
    
    def list_flyweights(self):
        """List all flyweight keys."""
        return list(self._flyweights.keys())

class UIElement:
    """Base class for UI elements."""
    
    def __init__(self, x, y, flyweight):
        self.x = x
        self.y = y
        self.flyweight = flyweight
    
    def move(self, new_x, new_y):
        """Move element to new position."""
        self.x = new_x
        self.y = new_y

class TextCharacter(UIElement):
    """Text character UI element."""
    
    def __init__(self, char, x, y, flyweight):
        super().__init__(x, y, flyweight)
        self.char = char
    
    def render(self):
        """Render this character."""
        extrinsic_state = (self.char, self.x, self.y)
        return self.flyweight.operation(extrinsic_state)

class Icon(UIElement):
    """Icon UI element."""
    
    def __init__(self, x, y, tooltip, flyweight):
        super().__init__(x, y, flyweight)
        self.tooltip = tooltip
    
    def render(self):
        """Render this icon."""
        extrinsic_state = (self.x, self.y, self.tooltip)
        return self.flyweight.operation(extrinsic_state)

class RichDocument:
    """Rich document with text and icons."""
    
    def __init__(self):
        self.elements = []
        self.factory = FlyweightFactory()
    
    def add_text(self, text, x, y, font="Arial", size=12, color="Black"):
        """Add text to the document."""
        for i, char in enumerate(text):
            flyweight = self.factory.get_character_flyweight(font, size, color)
            element = TextCharacter(char, x + i * 8, y, flyweight)
            self.elements.append(element)
    
    def add_icon(self, icon_type, x, y, tooltip, size=16):
        """Add icon to the document."""
        flyweight = self.factory.get_icon_flyweight(icon_type, size)
        element = Icon(x, y, tooltip, flyweight)
        self.elements.append(element)
    
    def render_document(self):
        """Render all elements in the document."""
        print("Rendering rich document:")
        for element in self.elements:
            print(f"  {element.render()}")
    
    def get_statistics(self):
        """Get document statistics."""
        return {
            'total_elements': len(self.elements),
            'unique_flyweights': self.factory.get_flyweight_count(),
            'flyweight_types': self.factory.list_flyweights(),
            'memory_efficiency': f"{(1 - self.factory.get_flyweight_count() / len(self.elements)) * 100:.1f}%"
        }

# What we accomplished in this step:
# - Extended pattern to support multiple flyweight types
# - Created rich document with text and icons
# - Demonstrated scalability with different UI elements
# - Added comprehensive statistics tracking


# Step 6: Testing and Performance Demonstration
# ===============================================================================

# Explanation:
# Let's test our Flyweight implementation and demonstrate the memory savings
# and performance benefits with large numbers of objects.

print("=== Testing Flyweight Pattern ===\n")

# Test 1: Basic Character Flyweight
print("--- Test 1: Basic Character Document ---")
doc = Document()

# Add some text with repeated formatting
doc.add_character('H', 0, 0, "Arial", 12, "Black")
doc.add_character('e', 8, 0, "Arial", 12, "Black")
doc.add_character('l', 16, 0, "Arial", 12, "Black")
doc.add_character('l', 24, 0, "Arial", 12, "Black")
doc.add_character('o', 32, 0, "Arial", 12, "Black")

print(f"Statistics: {doc.get_statistics()}")
doc.render_document()
print()

# Test 2: Rich Document with Mixed Content
print("--- Test 2: Rich Document ---")
rich_doc = RichDocument()

rich_doc.add_text("Hello World!", 0, 0, "Arial", 12, "Black")
rich_doc.add_text("Python", 0, 20, "Arial", 14, "Blue")
rich_doc.add_text("Flyweight", 0, 40, "Times", 12, "Red")

rich_doc.add_icon("save", 100, 0, "Save document")
rich_doc.add_icon("open", 120, 0, "Open document")
rich_doc.add_icon("save", 140, 0, "Save as...")  # Reuses save icon flyweight

print(f"Statistics: {rich_doc.get_statistics()}")
print()

# Test 3: Large Scale Performance Test
print("--- Test 3: Large Scale Performance ---")
large_doc = RichDocument()

# Simulate a large document
fonts = ["Arial", "Times", "Helvetica"]
colors = ["Black", "Blue", "Red", "Green"]
sizes = [10, 12, 14, 16]
icon_types = ["save", "open", "edit", "delete", "copy"]

# Add 1000 characters with random but limited formatting
print("Adding 1000 characters...")
for i in range(1000):
    char = chr(65 + (i % 26))  # A-Z cycling
    x = (i % 50) * 10
    y = (i // 50) * 20
    font = random.choice(fonts)
    size = random.choice(sizes)
    color = random.choice(colors)
    
    large_doc.add_text(char, x, y, font, size, color)

# Add 100 icons
print("Adding 100 icons...")
for i in range(100):
    icon_type = random.choice(icon_types)
    x = random.randint(0, 500)
    y = random.randint(0, 200)
    tooltip = f"Tooltip {i}"
    size = random.choice([16, 24, 32])
    
    large_doc.add_icon(icon_type, x, y, tooltip, size)

stats = large_doc.get_statistics()
print(f"Large document statistics:")
print(f"  Total elements: {stats['total_elements']}")
print(f"  Unique flyweights: {stats['unique_flyweights']}")
print(f"  Memory efficiency: {stats['memory_efficiency']}")
print(f"  Flyweight types: {len(stats['flyweight_types'])}")
print()

# Test 4: Memory Comparison
print("--- Test 4: Memory Usage Comparison ---")

# Without flyweight (hypothetical)
without_flyweight = 1100  # Each element would be a separate object
with_flyweight = stats['unique_flyweights']
memory_saved = without_flyweight - with_flyweight

print(f"Without Flyweight pattern: {without_flyweight} objects")
print(f"With Flyweight pattern: {with_flyweight} shared objects")
print(f"Memory objects saved: {memory_saved}")
print(f"Memory reduction: {(memory_saved / without_flyweight) * 100:.1f}%")

# What we accomplished in this step:
# - Tested flyweight pattern with various scenarios
# - Demonstrated memory efficiency with large datasets
# - Showed reuse of flyweight objects
# - Compared memory usage with and without the pattern


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Flyweight pattern structure and implementation
# - Separation of intrinsic and extrinsic state
# - Factory pattern for managing flyweight instances
# - Memory efficiency through object sharing
# - Scalability with large numbers of similar objects
# - Performance benefits in memory-constrained environments
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY intrinsic state should be immutable
# 4. Experiment with different flyweight types
#
# Remember: The best way to learn is by doing!
# ===============================================================================