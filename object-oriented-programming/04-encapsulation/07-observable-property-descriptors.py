"""Question: Create a class ObservableProperty that uses the descriptor
protocol to notify observers when a property value changes.
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
# - What are descriptors and what methods do they implement?
# - What are __get__ and __set__ methods used for?
# - How do you store observers and notify them when values change?
# - How do you create a class that uses the descriptor?
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


# Step 1: Define the ObservableProperty class
# ===============================================================================

# Explanation:
# Let's start by creating our ObservableProperty class. This class will implement
# the descriptor protocol, which allows it to control attribute access on other classes.

class ObservableProperty:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic ObservableProperty class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The constructor should initialize the property value and create a list to store
# observers that will be notified when the value changes.

class ObservableProperty:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.observers = []

# What we accomplished in this step:
# - Added constructor that accepts an initial value
# - Created observers list to store callback functions


# Step 3: Add the __get__ method
# ===============================================================================

# Explanation:
# The __get__ method is called when someone tries to read the property value.
# It should return the current value of the property.

class ObservableProperty:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.observers = []

    def __get__(self, instance, owner):
        return self.value

# What we accomplished in this step:
# - Added __get__ method to handle property reading
# - Returns the current stored value


# Step 4: Add the __set__ method
# ===============================================================================

# Explanation:
# The __set__ method is called when someone tries to set the property value.
# It should update the value and notify all observers about the change.

class ObservableProperty:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.observers = []

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        for observer in self.observers:
            observer(value)

# What we accomplished in this step:
# - Added __set__ method to handle property writing
# - Updates the stored value and notifies all observers


# Step 5: Add the add_observer method
# ===============================================================================

# Explanation:
# We need a way to register observers (callback functions) that will be called
# whenever the property value changes.

class ObservableProperty:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.observers = []

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        for observer in self.observers:
            observer(value)

    def add_observer(self, observer):
        self.observers.append(observer)

# What we accomplished in this step:
# - Added method to register observer functions
# - Observers will be called when property value changes


# Step 6: Create a class that uses the descriptor
# ===============================================================================

# Explanation:
# Now let's create a class that uses our ObservableProperty descriptor.
# The descriptor will be a class attribute, not an instance attribute.

class ObservableProperty:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.observers = []

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        for observer in self.observers:
            observer(value)

    def add_observer(self, observer):
        self.observers.append(observer)

class MyClass:
    prop = ObservableProperty()

# What we accomplished in this step:
# - Created MyClass that uses the ObservableProperty descriptor
# - The prop attribute will use our custom get/set behavior


# Step 7: Test our observable property
# ===============================================================================

# Explanation:
# Finally, let's test our ObservableProperty by creating an instance, adding
# observers, and changing the property value to see the notifications.

class ObservableProperty:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.observers = []

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        for observer in self.observers:
            observer(value)

    def add_observer(self, observer):
        self.observers.append(observer)

class MyClass:
    prop = ObservableProperty()

# Test our observable property:
def observer1(value):
    print(f"Observer 1: Property changed to {value}")

def observer2(value):
    print(f"Observer 2: New value is {value}")

# Create an instance and add observers
obj = MyClass()
obj.prop.add_observer(observer1)
obj.prop.add_observer(observer2)

# Test setting values
print("Setting prop to 42:")
obj.prop = 42

print("\nSetting prop to 'hello':")
obj.prop = "hello"

print(f"\nReading prop value: {obj.prop}")

# What we accomplished in this step:
# - Created observer functions that print notifications
# - Tested adding multiple observers
# - Verified that all observers are notified when value changes
# - Tested both setting and getting property values


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the descriptor protocol (__get__ and __set__)
# - Implementing the observer pattern with descriptors
# - Creating reusable property behaviors
# - Managing collections of observer functions
# - Using descriptors as class attributes
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a remove_observer method!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
