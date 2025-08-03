"""Question: Define a class Flyweight that uses the Flyweight pattern
to minimize memory usage by sharing common data between instances.
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
# - What is the Flyweight pattern and when is it useful?
# - How do you use __new__ to control object creation?
# - What's the difference between intrinsic and extrinsic state?
# - How do you store and reuse existing instances?
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


# Step 1: Define the Flyweight class
# ===============================================================================

# Explanation:
# Let's start by creating our Flyweight class. The Flyweight pattern minimizes
# memory usage by sharing instances that have the same intrinsic state.

class Flyweight:
    pass  # We'll add the flyweight mechanism next

# What we accomplished in this step:
# - Created the basic Flyweight class structure


# Step 2: Add instance storage
# ===============================================================================

# Explanation:
# We need a class variable to store existing instances. This dictionary will
# map shared states to their corresponding flyweight instances.

class Flyweight:
    _instances = {}

# What we accomplished in this step:
# - Added class variable to store existing flyweight instances
# - Dictionary will map shared state to instances


# Step 3: Implement the __new__ method
# ===============================================================================

# Explanation:
# The __new__ method controls object creation. We'll check if an instance
# with the same shared state already exists, and return it if it does.

class Flyweight:
    _instances = {}

    def __new__(cls, shared_state):
        if shared_state not in cls._instances:
            cls._instances[shared_state] = super(Flyweight, cls).__new__(cls)
        return cls._instances[shared_state]

# What we accomplished in this step:
# - Added __new__ method to control instance creation
# - Returns existing instance if shared state already exists
# - Creates new instance only if shared state is new


# Step 4: Initialize the shared state
# ===============================================================================

# Explanation:
# We need to store the shared state in the instance. We'll do this in __new__
# to ensure it's only set once when the instance is first created.

class Flyweight:
    _instances = {}

    def __new__(cls, shared_state):
        if shared_state not in cls._instances:
            cls._instances[shared_state] = super(Flyweight, cls).__new__(cls)
            cls._instances[shared_state].shared_state = shared_state
        return cls._instances[shared_state]

# What we accomplished in this step:
# - Added shared state initialization
# - State is only set when instance is first created
# - Subsequent calls return the existing instance with its state


# Step 5: Test our Flyweight implementation
# ===============================================================================

# Explanation:
# Let's test our Flyweight pattern by creating instances with the same and
# different shared states, and verify that instances are reused appropriately.

class Flyweight:
    _instances = {}

    def __new__(cls, shared_state):
        if shared_state not in cls._instances:
            cls._instances[shared_state] = super(Flyweight, cls).__new__(cls)
            cls._instances[shared_state].shared_state = shared_state
        return cls._instances[shared_state]

# Test our Flyweight:
print("=== Testing Flyweight Pattern ===")

print("Creating flyweight instances:")
fw1 = Flyweight("shared")
fw2 = Flyweight("shared")
fw3 = Flyweight("unique")
fw4 = Flyweight("another")
fw5 = Flyweight("shared")  # Should reuse fw1

print(f"fw1 shared_state: {fw1.shared_state}")
print(f"fw2 shared_state: {fw2.shared_state}")
print(f"fw3 shared_state: {fw3.shared_state}")

print(f"\nIdentity checks:")
print(f"fw1 is fw2: {fw1 is fw2}")  # Should be True
print(f"fw1 is fw3: {fw1 is fw3}")  # Should be False
print(f"fw1 is fw5: {fw1 is fw5}")  # Should be True

print(f"\nInstance IDs:")
print(f"fw1 id: {id(fw1)}")
print(f"fw2 id: {id(fw2)}")
print(f"fw3 id: {id(fw3)}")
print(f"fw5 id: {id(fw5)}")

print(f"\nTotal instances created: {len(Flyweight._instances)}")
print(f"Instances: {list(Flyweight._instances.keys())}")

# What we accomplished in this step:
# - Created multiple flyweight instances with same and different states
# - Verified that instances with same state are reused
# - Confirmed that different states create different instances
# - Demonstrated memory efficiency of the pattern


# Step 6: Enhanced Flyweight with intrinsic and extrinsic state
# ===============================================================================

# Explanation:
# Let's create a more realistic example that demonstrates the difference
# between intrinsic state (shared) and extrinsic state (context-specific).

class Character:
    """Flyweight for text characters with shared formatting"""
    _instances = {}

    def __new__(cls, font, size, color):
        # Intrinsic state: font, size, color (shared among similar characters)
        intrinsic_state = (font, size, color)
        if intrinsic_state not in cls._instances:
            instance = super(Character, cls).__new__(cls)
            instance.font = font
            instance.size = size
            instance.color = color
            cls._instances[intrinsic_state] = instance
        return cls._instances[intrinsic_state]

    def display(self, char, position):
        """Display character with extrinsic state (char and position)"""
        return f"Char '{char}' at {position} with {self.font} {self.size}pt {self.color}"

    def get_intrinsic_state(self):
        return (self.font, self.size, self.color)

class TextDocument:
    """Context that uses flyweights with extrinsic state"""
    def __init__(self):
        self.characters = []

    def add_character(self, char, position, font, size, color):
        # Get or create flyweight for this formatting
        flyweight = Character(font, size, color)
        # Store flyweight with extrinsic state
        self.characters.append((flyweight, char, position))

    def display(self):
        result = []
        for flyweight, char, position in self.characters:
            result.append(flyweight.display(char, position))
        return result

# Test enhanced flyweight:
print("\n=== Enhanced Flyweight with Text Characters ===")

doc = TextDocument()

# Add characters with various formatting
doc.add_character('H', (0, 0), 'Arial', 12, 'black')
doc.add_character('e', (1, 0), 'Arial', 12, 'black')
doc.add_character('l', (2, 0), 'Arial', 12, 'black')
doc.add_character('l', (3, 0), 'Arial', 12, 'black')
doc.add_character('o', (4, 0), 'Arial', 12, 'black')
doc.add_character('!', (5, 0), 'Arial', 16, 'red')    # Different formatting
doc.add_character(' ', (6, 0), 'Arial', 12, 'black')
doc.add_character('W', (7, 0), 'Times', 14, 'blue')   # Different font
doc.add_character('o', (8, 0), 'Times', 14, 'blue')
doc.add_character('r', (9, 0), 'Times', 14, 'blue')
doc.add_character('l', (10, 0), 'Times', 14, 'blue')
doc.add_character('d', (11, 0), 'Times', 14, 'blue')

print("Document content:")
for line in doc.display():
    print(f"  {line}")

print(f"\nFlyweight instances created: {len(Character._instances)}")
print("Flyweight states:")
for i, state in enumerate(Character._instances.keys(), 1):
    print(f"  {i}: {state}")

print(f"\nTotal characters in document: {len(doc.characters)}")
print("Memory efficiency: Multiple characters share the same flyweight instances!")

# What we accomplished in this step:
# - Created realistic flyweight example with text characters
# - Demonstrated intrinsic state (font, size, color) vs extrinsic state (char, position)
# - Showed how context (TextDocument) manages extrinsic state
# - Illustrated memory efficiency when many objects share formatting


# Step 7: Flyweight factory for better management
# ===============================================================================

# Explanation:
# Let's create a factory class to better manage flyweight creation and
# provide additional functionality like statistics and cleanup.

class FlyweightFactory:
    """Factory to manage flyweight instances"""
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, intrinsic_state):
        """Get or create a flyweight for the given intrinsic state"""
        if intrinsic_state not in cls._flyweights:
            cls._flyweights[intrinsic_state] = Flyweight(intrinsic_state)
        return cls._flyweights[intrinsic_state]

    @classmethod
    def get_flyweight_count(cls):
        """Get the number of flyweight instances"""
        return len(cls._flyweights)

    @classmethod
    def get_flyweight_states(cls):
        """Get all flyweight states"""
        return list(cls._flyweights.keys())

    @classmethod
    def clear_flyweights(cls):
        """Clear all flyweight instances (for testing/cleanup)"""
        cls._flyweights.clear()

class ManagedFlyweight:
    """Flyweight that works with the factory"""
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        return f"Flyweight with intrinsic '{self.intrinsic_state}' and extrinsic '{extrinsic_state}'"

# Update factory to use ManagedFlyweight
class FlyweightFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, intrinsic_state):
        if intrinsic_state not in cls._flyweights:
            cls._flyweights[intrinsic_state] = ManagedFlyweight(intrinsic_state)
        return cls._flyweights[intrinsic_state]

    @classmethod
    def get_statistics(cls):
        return {
            'flyweight_count': len(cls._flyweights),
            'flyweight_states': list(cls._flyweights.keys()),
            'memory_efficiency': f"{len(cls._flyweights)} instances for potentially unlimited objects"
        }

    @classmethod
    def clear_flyweights(cls):
        cls._flyweights.clear()

# Test factory-managed flyweights:
print("\n=== Factory-Managed Flyweights ===")

# Clear any existing flyweights
FlyweightFactory.clear_flyweights()

# Create flyweights through factory
fw_a1 = FlyweightFactory.get_flyweight("TypeA")
fw_a2 = FlyweightFactory.get_flyweight("TypeA")  # Should reuse
fw_b1 = FlyweightFactory.get_flyweight("TypeB")
fw_c1 = FlyweightFactory.get_flyweight("TypeC")
fw_a3 = FlyweightFactory.get_flyweight("TypeA")  # Should reuse

print("Testing flyweight operations:")
print(fw_a1.operation("context1"))
print(fw_a2.operation("context2"))
print(fw_b1.operation("context3"))

print(f"\nIdentity verification:")
print(f"fw_a1 is fw_a2: {fw_a1 is fw_a2}")
print(f"fw_a1 is fw_a3: {fw_a1 is fw_a3}")
print(f"fw_a1 is fw_b1: {fw_a1 is fw_b1}")

print(f"\nFactory statistics:")
stats = FlyweightFactory.get_statistics()
for key, value in stats.items():
    print(f"  {key}: {value}")

# What we accomplished in this step:
# - Created a factory to manage flyweight creation
# - Added statistics and management capabilities
# - Demonstrated proper flyweight usage patterns
# - Provided cleanup functionality for testing


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Flyweight pattern and its memory benefits
# - Using __new__ to control object creation and reuse
# - Distinguishing between intrinsic and extrinsic state
# - Creating flyweight factories for better management
# - Implementing realistic examples with text formatting
# - Understanding when and why to use the Flyweight pattern
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating flyweights for game objects!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
