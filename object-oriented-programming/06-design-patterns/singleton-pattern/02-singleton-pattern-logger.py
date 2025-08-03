"""Question: Create a class Logger with a private class attribute _instance
to implement the Singleton pattern.
Ensure that only one instance of the class can be created.
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
# - What is the Singleton pattern? (design pattern ensuring only one instance exists)
# - What is the __new__ method? (controls object creation before __init__)
# - How do you store a class-level instance? (class attribute)
# - How do you check if an instance already exists?
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


# Step 1: Define the Logger class with class attribute
# ===============================================================================

# Explanation:
# Let's start by creating our Logger class with a private class attribute to store the single instance.
# Class attributes are shared by all instances of the class.

class Logger:
    _instance = None

# What we accomplished in this step:
# - Created Logger class with private class attribute _instance


# Step 2: Override the __new__ method
# ===============================================================================

# Explanation:
# The __new__ method is called before __init__ and controls object creation.
# We'll use it to ensure only one instance is ever created.

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# What we accomplished in this step:
# - Overrode __new__ method to implement Singleton pattern


# Step 3: Add initialization method
# ===============================================================================

# Explanation:
# Let's add an __init__ method, but we need to be careful not to reinitialize
# the same instance multiple times.

class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            Logger._initialized = True
            print("Logger instance created")

# What we accomplished in this step:
# - Added __init__ method with initialization guard


# Step 4: Add logging functionality
# ===============================================================================

# Explanation:
# Now let's add the actual logging functionality to make our Logger useful.
# This demonstrates that our Singleton works with real methods.

class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            Logger._initialized = True
            print("Logger instance created")

    def log(self, message):
        print(f"Log: {message}")

    def error(self, message):
        print(f"ERROR: {message}")

    def warning(self, message):
        print(f"WARNING: {message}")

# What we accomplished in this step:
# - Added logging methods (log, error, warning)


# Step 5: Add method to get instance (alternative approach)
# ===============================================================================

# Explanation:
# Let's add a class method that provides an alternative way to get the instance.
# This is a common pattern in Singleton implementations.

class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            Logger._initialized = True
            print("Logger instance created")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")

    def error(self, message):
        print(f"ERROR: {message}")

    def warning(self, message):
        print(f"WARNING: {message}")

# What we accomplished in this step:
# - Added get_instance class method for alternative access


# Step 6: Test the Singleton pattern
# ===============================================================================

# Explanation:
# Finally, let's test our Singleton implementation to make sure it works correctly.
# We'll create multiple "instances" and verify they're actually the same object.

class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            Logger._initialized = True
            print("Logger instance created")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")

    def error(self, message):
        print(f"ERROR: {message}")

    def warning(self, message):
        print(f"WARNING: {message}")

# Test our Singleton:
print("Testing Singleton pattern:")

# Create first instance
logger1 = Logger()

# Create second instance
logger2 = Logger()

# Test if they're the same object
print(f"logger1 is logger2: {logger1 is logger2}")
print(f"logger1 id: {id(logger1)}")
print(f"logger2 id: {id(logger2)}")

# Test using class method
logger3 = Logger.get_instance()
print(f"logger1 is logger3: {logger1 is logger3}")

# Test logging functionality
print("\nTesting logging functionality:")
logger1.log("This is a log message from logger1")
logger2.error("This is an error message from logger2")
logger3.warning("This is a warning message from logger3")

print("\nAll loggers are the same instance!")

# What we accomplished in this step:
# - Created and tested our complete Singleton Logger implementation
# - Verified that only one instance exists regardless of how it's created


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Singleton design pattern implementation
# - __new__ method for controlling object creation
# - Class attributes for shared state
# - Initialization guards to prevent re-initialization
# - Object identity testing with 'is' operator
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding file logging or different log levels!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================