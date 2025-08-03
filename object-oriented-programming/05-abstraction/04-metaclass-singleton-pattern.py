"""Question: Implement a class MetaSingleton using metaclasses to ensure
only one instance of the class can be created.
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
# - What are metaclasses? (classes that create classes)
# - What is the __call__ method in metaclasses? (controls instance creation)
# - How do you store instances? (class attribute dictionary)
# - How is this different from the __new__ method approach?
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


# Step 1: Understanding metaclasses
# ===============================================================================

# Explanation:
# Metaclasses are "classes that create classes". In Python, when you define a class,
# Python uses a metaclass to create that class object. We can customize this process.

# First, let's see how normal class creation works:
print("Step 1: Understanding normal class creation")

class NormalClass:
    pass

print(f"Type of NormalClass: {type(NormalClass)}")
print(f"NormalClass is an instance of: {type(NormalClass).__name__}")

# What we accomplished in this step:
# - Demonstrated that classes are objects created by metaclasses
# - Showed that the default metaclass is 'type'


# Step 2: Define the MetaSingleton metaclass
# ===============================================================================

# Explanation:
# A metaclass inherits from 'type' and can control how classes are created and instantiated.
# We'll use a class attribute to store instances.

print("\nStep 2: Creating MetaSingleton metaclass")

class MetaSingleton(type):
    _instances = {}

print("MetaSingleton metaclass defined")

# What we accomplished in this step:
# - Created a metaclass that inherits from 'type'
# - Added a class attribute to store instances


# Step 3: Override the __call__ method
# ===============================================================================

# Explanation:
# The __call__ method in a metaclass is called when someone tries to create
# an instance of a class that uses this metaclass.

print("\nStep 3: Adding __call__ method to control instance creation")

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(f"MetaSingleton.__call__ called for {cls.__name__}")
        if cls not in cls._instances:
            print(f"Creating new instance of {cls.__name__}")
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        else:
            print(f"Returning existing instance of {cls.__name__}")
        return cls._instances[cls]

# What we accomplished in this step:
# - Added __call__ method to control instance creation
# - Added logging to see when instances are created vs reused


# Step 4: Create a class that uses the metaclass
# ===============================================================================

# Explanation:
# Now let's create a class that uses our MetaSingleton metaclass.
# This class will automatically have singleton behavior.

print("\nStep 4: Creating a class with MetaSingleton metaclass")

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(f"MetaSingleton.__call__ called for {cls.__name__}")
        if cls not in cls._instances:
            print(f"Creating new instance of {cls.__name__}")
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        else:
            print(f"Returning existing instance of {cls.__name__}")
        return cls._instances[cls]

class Singleton(metaclass=MetaSingleton):
    def __init__(self):
        print("Singleton.__init__ called")
        self.value = None

print("Singleton class defined with MetaSingleton metaclass")

# What we accomplished in this step:
# - Created a class that uses our metaclass
# - Added initialization logging


# Step 5: Add useful methods to the Singleton class
# ===============================================================================

# Explanation:
# Let's add some methods to our Singleton class to make it more useful
# and demonstrate that it maintains state across "instances".

print("\nStep 5: Adding methods to Singleton class")

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=MetaSingleton):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.value = None
            self.initialized = True
            print("Singleton initialized")

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return f"Singleton(value={self.value}, id={id(self)})"

# What we accomplished in this step:
# - Added initialization guard to prevent re-initialization
# - Added methods to set and get values
# - Added string representation


# Step 6: Test the metaclass singleton implementation
# ===============================================================================

# Explanation:
# Finally, let's test our metaclass-based singleton to make sure it works correctly
# and compare it with multiple "instances".

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=MetaSingleton):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.value = None
            self.initialized = True
            print("Singleton initialized")

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return f"Singleton(value={self.value}, id={id(self)})"

# Test our metaclass singleton:
print("\nTesting MetaSingleton implementation:")

print("Creating first 'instance':")
s1 = Singleton()

print("Creating second 'instance':")
s2 = Singleton()

print(f"s1 is s2: {s1 is s2}")
print(f"s1 id: {id(s1)}")
print(f"s2 id: {id(s2)}")

print("\nTesting shared state:")
s1.set_value("Hello from s1")
print(f"s1 value: {s1.get_value()}")
print(f"s2 value: {s2.get_value()}")

s2.set_value("Modified by s2")
print(f"s1 value after s2 modification: {s1.get_value()}")

print(f"\ns1: {s1}")
print(f"s2: {s2}")

# Test with another class using the same metaclass
class AnotherSingleton(metaclass=MetaSingleton):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = "Another singleton"
            self.initialized = True

print("\nTesting multiple classes with same metaclass:")
a1 = AnotherSingleton()
a2 = AnotherSingleton()
print(f"a1 is a2: {a1 is a2}")
print(f"s1 is a1: {s1 is a1}")  # Should be False - different classes

# What we accomplished in this step:
# - Created and tested our complete metaclass singleton implementation
# - Demonstrated that each class gets its own singleton instance
# - Showed shared state between "instances" of the same class


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Metaclasses and how they control class creation
# - The __call__ method in metaclasses
# - Advanced singleton implementation using metaclasses
# - Class-level instance management
# - The difference between metaclass and __new__ approaches
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding thread safety or instance counting!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================