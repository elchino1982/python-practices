"""Question: Define a class MetaLogger using a metaclass to automatically log
the creation of any instance of classes that use this metaclass.
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
# - What is a metaclass and how does it control class creation?
# - What method in a metaclass is called when creating instances?
# - How do you inherit from the 'type' metaclass?
# - How do you use the metaclass parameter in a class definition?
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


# Step 1: Define the MetaLogger metaclass
# ===============================================================================

# Explanation:
# Let's start by creating our MetaLogger metaclass. A metaclass is a class whose
# instances are classes themselves. We inherit from 'type' which is the default metaclass.

class MetaLogger(type):
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created MetaLogger class that inherits from type
# - This makes it a metaclass that can control class behavior


# Step 2: Override the __call__ method
# ===============================================================================

# Explanation:
# The __call__ method in a metaclass is invoked when an instance of a class
# (that uses this metaclass) is created. This is where we'll add our logging.

class MetaLogger(type):
    def __call__(cls, *args, **kwargs):
        # We'll add logging and instance creation next
        pass

# What we accomplished in this step:
# - Added __call__ method that will be called during instance creation
# - Accepts cls (the class), *args and **kwargs (constructor arguments)


# Step 3: Add logging and instance creation
# ===============================================================================

# Explanation:
# Now we'll add the actual logging and create the instance by calling the
# parent metaclass's __call__ method.

class MetaLogger(type):
    def __call__(cls, *args, **kwargs):
        instance = super(MetaLogger, cls).__call__(*args, **kwargs)
        print(f"Created instance of {cls.__name__}")
        return instance

# What we accomplished in this step:
# - Called super() to create the instance normally
# - Added logging after instance creation
# - Returned the created instance


# Step 4: Create a class that uses the metaclass
# ===============================================================================

# Explanation:
# Now let's create a class that uses our MetaLogger metaclass. We specify
# the metaclass using the metaclass parameter in the class definition.

class MetaLogger(type):
    def __call__(cls, *args, **kwargs):
        instance = super(MetaLogger, cls).__call__(*args, **kwargs)
        print(f"Created instance of {cls.__name__}")
        return instance

class MyClass(metaclass=MetaLogger):
    def __init__(self, value):
        self.value = value

# What we accomplished in this step:
# - Created MyClass that uses MetaLogger as its metaclass
# - Added a simple constructor that accepts a value


# Step 5: Test our metaclass implementation
# ===============================================================================

# Explanation:
# Let's test our MetaLogger by creating instances and observing the automatic logging.

class MetaLogger(type):
    def __call__(cls, *args, **kwargs):
        instance = super(MetaLogger, cls).__call__(*args, **kwargs)
        print(f"Created instance of {cls.__name__}")
        return instance

class MyClass(metaclass=MetaLogger):
    def __init__(self, value):
        self.value = value

# Test our metaclass:
print("=== Testing MetaLogger Metaclass ===")
print("Creating first instance:")
obj1 = MyClass(10)
print(f"obj1.value = {obj1.value}")

print("\nCreating second instance:")
obj2 = MyClass(20)
print(f"obj2.value = {obj2.value}")

print("\nCreating third instance:")
obj3 = MyClass("hello")
print(f"obj3.value = {obj3.value}")

# What we accomplished in this step:
# - Created multiple instances to test the logging
# - Verified that each instance creation is automatically logged
# - Confirmed that the instances work normally


# Step 6: Enhanced version with more detailed logging
# ===============================================================================

# Explanation:
# Let's create an enhanced version that provides more detailed logging information
# including timestamps and constructor arguments.

import datetime

class EnhancedMetaLogger(type):
    def __call__(cls, *args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Creating instance of {cls.__name__}")
        
        if args:
            print(f"  Arguments: {args}")
        if kwargs:
            print(f"  Keyword arguments: {kwargs}")
        
        instance = super(EnhancedMetaLogger, cls).__call__(*args, **kwargs)
        print(f"[{timestamp}] Successfully created {cls.__name__} instance")
        return instance

class Person(metaclass=EnhancedMetaLogger):
    def __init__(self, name, age, city="Unknown"):
        self.name = name
        self.age = age
        self.city = city

class Product(metaclass=EnhancedMetaLogger):
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Test enhanced version:
print("\n=== Enhanced MetaLogger with Detailed Logging ===")

print("Creating Person instances:")
person1 = Person("Alice", 30)
person2 = Person("Bob", 25, city="New York")

print("\nCreating Product instances:")
product1 = Product("Laptop", 999.99)
product2 = Product(name="Mouse", price=29.99)

# What we accomplished in this step:
# - Enhanced logging with timestamps
# - Added logging of constructor arguments
# - Demonstrated metaclass working with multiple different classes
# - Showed both positional and keyword arguments


# Step 7: Metaclass with instance counting
# ===============================================================================

# Explanation:
# Let's create a final version that also counts how many instances of each
# class have been created.

class CountingMetaLogger(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._instance_count = 0

    def __call__(cls, *args, **kwargs):
        cls._instance_count += 1
        instance = super(CountingMetaLogger, cls).__call__(*args, **kwargs)
        print(f"Created instance #{cls._instance_count} of {cls.__name__}")
        return instance

    def get_instance_count(cls):
        return cls._instance_count

class Counter(metaclass=CountingMetaLogger):
    def __init__(self, initial_value=0):
        self.value = initial_value

class Timer(metaclass=CountingMetaLogger):
    def __init__(self, duration):
        self.duration = duration

# Test counting version:
print("\n=== Counting MetaLogger ===")

print("Creating Counter instances:")
c1 = Counter()
c2 = Counter(10)
c3 = Counter(5)

print("Creating Timer instances:")
t1 = Timer(60)
t2 = Timer(120)

print(f"\nTotal Counter instances created: {Counter.get_instance_count()}")
print(f"Total Timer instances created: {Timer.get_instance_count()}")

# What we accomplished in this step:
# - Added instance counting functionality
# - Used __init__ method in metaclass to initialize class attributes
# - Demonstrated how metaclasses can add methods to classes
# - Showed independent counting for different classes


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding metaclasses and how they control class behavior
# - Using the __call__ method to intercept instance creation
# - Inheriting from the 'type' metaclass
# - Specifying metaclasses in class definitions
# - Adding automatic logging and counting functionality
# - Working with *args and **kwargs in metaclasses
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding automatic method logging!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
