"""Question: Define a class Person with private attributes _name and _age.
Use properties to get and set these attributes with validation
(e.g., age must be a positive integer).
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
# - What are private attributes? (attributes starting with _)
# - What are properties? (@property decorator)
# - How do you create getters and setters? (@property and @attribute.setter)
# - What validation should you add? (age > 0, name not empty)
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


# Step 1: Define the Person class with private attributes
# ===============================================================================

# Explanation:
# Let's start by creating our Person class with private attributes.
# In Python, attributes starting with _ are considered private by convention.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

# What we accomplished in this step:
# - Created Person class with private attributes _name and _age


# Step 2: Add property getter for name
# ===============================================================================

# Explanation:
# Properties allow us to access private attributes through methods that look like attributes.
# The @property decorator creates a getter method.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

# What we accomplished in this step:
# - Added property getter for name attribute


# Step 3: Add property setter for name with validation
# ===============================================================================

# Explanation:
# The @name.setter decorator creates a setter method that includes validation.
# We'll check that the name is not empty.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

# What we accomplished in this step:
# - Added property setter for name with validation


# Step 4: Add property getter for age
# ===============================================================================

# Explanation:
# Now let's add the property getter for age, similar to what we did for name.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

# What we accomplished in this step:
# - Added property getter for age attribute


# Step 5: Add property setter for age with validation
# ===============================================================================

# Explanation:
# The age setter should validate that the age is a positive integer.
# We'll check both the type and the value.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

# What we accomplished in this step:
# - Added property setter for age with validation


# Step 6: Create instances and test our properties
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Person class and test both the getters
# and setters to make sure validation works correctly.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

# Test our class:
person = Person("Alice", 30)

# Test property getters
print(f"Name: {person.name}")
print(f"Age: {person.age}")

# Test property setters with valid values
person.name = "Bob"
person.age = 25
print(f"Updated name: {person.name}")
print(f"Updated age: {person.age}")

# Test validation (these will raise errors if uncommented)
# try:
#     person.name = ""  # Should raise ValueError
# except ValueError as e:
#     print(f"Name validation error: {e}")

# try:
#     person.age = -5  # Should raise ValueError
# except ValueError as e:
#     print(f"Age validation error: {e}")

print("All property operations completed successfully!")

# What we accomplished in this step:
# - Created and tested our complete Person class with properties
# - Demonstrated both getters and setters with validation


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Private attributes (underscore convention)
# - Property decorators (@property)
# - Getter and setter methods
# - Data validation in setters
# - Encapsulation principles
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding email validation!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================