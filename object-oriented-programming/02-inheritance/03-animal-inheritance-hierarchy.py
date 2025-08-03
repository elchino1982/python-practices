"""Question: Define a class named Animal with attributes name and species.
Create a subclass named Dog that adds an attribute breed and a method bark.
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
# - What attributes does the Animal class need?
# - How do you create a subclass that inherits from Animal?
# - How do you add new attributes and methods to a subclass?
# - What should the bark method do?
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


# Step 1: Define the Animal class
# ===============================================================================

# Explanation:
# Let's start by creating our Animal class. This will be our base class that
# contains the common attributes for all animals.

class Animal:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Animal class structure


# Step 2: Add the constructor to Animal class
# ===============================================================================

# Explanation:
# The __init__ method initializes the Animal with name and species attributes.
# These will be inherited by any subclass we create.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

# What we accomplished in this step:
# - Added constructor to initialize name and species attributes


# Step 3: Define the Dog subclass
# ===============================================================================

# Explanation:
# Now let's create the Dog class that inherits from Animal. In Python,
# we specify inheritance by putting the parent class name in parentheses.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created Dog class that inherits from Animal


# Step 4: Add constructor to Dog class
# ===============================================================================

# Explanation:
# The Dog constructor needs to accept name, species, and breed.
# We use super().__init__() to call the parent class constructor for name and species.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)  # Call parent constructor
        self.breed = breed               # Add new attribute

# What we accomplished in this step:
# - Added Dog constructor that uses super() to inherit Animal attributes
# - Added breed attribute specific to Dog


# Step 5: Add the bark method
# ===============================================================================

# Explanation:
# Now let's add the bark method that is specific to dogs. This method
# will print or return a barking sound.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print("Woof!")

# What we accomplished in this step:
# - Added bark method specific to Dog class


# Step 6: Create an instance and test our classes
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our Dog class and test it to make sure everything works correctly.
# This demonstrates inheritance and how subclasses can add new functionality.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print("Woof!")

# Test our classes:
dog = Dog("Buddy", "Canine", "Golden Retriever")

# Test inherited attributes
print(f"Dog name: {dog.name}")
print(f"Dog species: {dog.species}")

# Test new attribute
print(f"Dog breed: {dog.breed}")

# Test new method
print("Dog says:", end=" ")
dog.bark()

# What we accomplished in this step:
# - Created and tested our complete Animal and Dog implementation
# - Demonstrated inheritance and adding new functionality in subclasses


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Class inheritance and the super() function
# - Adding new attributes in subclasses
# - Adding new methods in subclasses
# - How subclasses extend parent class functionality
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding Cat or Bird classes!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================