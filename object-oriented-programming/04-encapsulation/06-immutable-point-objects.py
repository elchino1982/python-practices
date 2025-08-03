"""Question: Create a class ImmutablePoint that represents an immutable point in 2D space.
Override the __setattr__ method to prevent modification of attributes after initialization.
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
# - What is the __setattr__ method and when is it called?
# - How can you allow setting attributes during initialization but prevent it afterwards?
# - What is super().__setattr__ and why might you need it?
# - How do you raise an appropriate exception for immutable objects?
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


# Step 1: Define the ImmutablePoint class
# ===============================================================================

# Explanation:
# Let's start by creating our ImmutablePoint class. This class will represent
# a point in 2D space that cannot be modified after creation.

class ImmutablePoint:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic ImmutablePoint class structure


# Step 2: Add the constructor (__init__ method)
# ===============================================================================

# Explanation:
# The __init__ method needs to set the x and y coordinates. However, since we'll
# override __setattr__ to prevent modifications, we need a special way to set
# attributes during initialization.

class ImmutablePoint:
    def __init__(self, x, y):
        # We'll add attribute setting next
        pass

# What we accomplished in this step:
# - Added constructor that accepts x and y coordinates


# Step 3: Set attributes using super().__setattr__
# ===============================================================================

# Explanation:
# We use super().__setattr__ to bypass our custom __setattr__ method during
# initialization. This allows us to set the initial values while still
# preventing future modifications.

class ImmutablePoint:
    def __init__(self, x, y):
        super().__setattr__('x', x)
        super().__setattr__('y', y)

# What we accomplished in this step:
# - Used super().__setattr__ to set initial x and y values
# - Bypassed the custom __setattr__ method during initialization


# Step 4: Override __setattr__ to prevent modifications
# ===============================================================================

# Explanation:
# Now let's override the __setattr__ method to raise an exception whenever
# someone tries to modify any attribute after the object is created.

class ImmutablePoint:
    def __init__(self, x, y):
        super().__setattr__('x', x)
        super().__setattr__('y', y)

    def __setattr__(self, key, value):
        raise AttributeError("Cannot modify immutable point")

# What we accomplished in this step:
# - Added __setattr__ override that prevents any attribute modifications
# - Raises AttributeError with descriptive message


# Step 5: Create an instance and test our class
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our ImmutablePoint class and test it to make sure
# the immutability works correctly. We'll test both normal access and modification attempts.

class ImmutablePoint:
    def __init__(self, x, y):
        super().__setattr__('x', x)
        super().__setattr__('y', y)

    def __setattr__(self, key, value):
        raise AttributeError("Cannot modify immutable point")

# Test our class:
point = ImmutablePoint(1, 2)

# Test reading attributes (should work)
print(f"Point coordinates: ({point.x}, {point.y})")

# Test modifying attributes (should raise exception)
try:
    point.x = 3
    print("ERROR: Modification should have failed!")
except AttributeError as e:
    print(f"Good! Modification prevented: {e}")

# Test adding new attributes (should also fail)
try:
    point.z = 5
    print("ERROR: Adding new attribute should have failed!")
except AttributeError as e:
    print(f"Good! New attribute prevented: {e}")

# What we accomplished in this step:
# - Created and tested our complete ImmutablePoint implementation
# - Verified that reading works but modification fails
# - Tested both existing and new attribute modifications


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the __setattr__ method and when it's called
# - Using super().__setattr__ to bypass custom behavior during initialization
# - Creating immutable objects that prevent modification after creation
# - Proper exception handling for invalid operations
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a distance_from_origin method!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
