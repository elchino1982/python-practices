"""Question: Create a class CustomList that inherits from list and 
overrides the __getitem__ and __setitem__ methods to add custom behavior
(e.g., logging access and modifications).
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
# - How do you inherit from the built-in list class?
# - What are __getitem__ and __setitem__ methods used for?
# - How do you call the parent class methods using super()?
# - What kind of logging or custom behavior would be useful?
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


# Step 1: Define the CustomList class
# ===============================================================================

# Explanation:
# Let's start by creating our CustomList class that inherits from the built-in list.
# This gives us all the functionality of a regular list, which we can then enhance.

class CustomList(list):
    pass  # We'll add method overrides next

# What we accomplished in this step:
# - Created CustomList class that inherits from list
# - Inherits all list functionality by default


# Step 2: Override __getitem__ for custom access behavior
# ===============================================================================

# Explanation:
# The __getitem__ method is called when you use list[index] syntax to access items.
# We'll override it to add logging while still returning the actual value.

class CustomList(list):
    def __getitem__(self, index):
        print(f"Accessing index {index}")
        return super().__getitem__(index)

# What we accomplished in this step:
# - Overrode __getitem__ to log access operations
# - Used super() to call the original list behavior
# - Added custom logging before returning the value


# Step 3: Override __setitem__ for custom modification behavior
# ===============================================================================

# Explanation:
# The __setitem__ method is called when you use list[index] = value syntax.
# We'll override it to add logging while still setting the actual value.

class CustomList(list):
    def __getitem__(self, index):
        print(f"Accessing index {index}")
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        print(f"Setting index {index} to {value}")
        super().__setitem__(index, value)

# What we accomplished in this step:
# - Overrode __setitem__ to log modification operations
# - Used super() to call the original list behavior
# - Added custom logging before setting the value


# Step 4: Test basic functionality
# ===============================================================================

# Explanation:
# Let's test our CustomList with basic operations to see the logging in action.

class CustomList(list):
    def __getitem__(self, index):
        print(f"Accessing index {index}")
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        print(f"Setting index {index} to {value}")
        super().__setitem__(index, value)

# Test basic functionality:
print("=== Creating CustomList ===")
custom_list = CustomList([1, 2, 3, 4, 5])
print(f"Created list: {custom_list}")

print("\n=== Testing access operations ===")
value = custom_list[1]
print(f"Retrieved value: {value}")

value = custom_list[3]
print(f"Retrieved value: {value}")

print("\n=== Testing modification operations ===")
custom_list[1] = 42
print(f"List after modification: {custom_list}")

custom_list[3] = 99
print(f"List after modification: {custom_list}")

# What we accomplished in this step:
# - Created and tested our basic CustomList implementation
# - Verified that logging works for both access and modification
# - Confirmed that the underlying list functionality is preserved


# Step 5: Enhanced version with more detailed logging
# ===============================================================================

# Explanation:
# Let's create an enhanced version that provides more detailed logging information
# and handles edge cases like negative indices and slicing.

class CustomList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.access_count = 0
        self.modification_count = 0

    def __getitem__(self, index):
        self.access_count += 1
        if isinstance(index, slice):
            print(f"Accessing slice {index} (access #{self.access_count})")
        else:
            print(f"Accessing index {index} (access #{self.access_count})")
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        self.modification_count += 1
        if isinstance(index, slice):
            print(f"Setting slice {index} to {value} (modification #{self.modification_count})")
        else:
            print(f"Setting index {index} to {value} (modification #{self.modification_count})")
        super().__setitem__(index, value)

    def get_stats(self):
        return {
            'access_count': self.access_count,
            'modification_count': self.modification_count,
            'length': len(self)
        }

# Test enhanced version:
print("\n=== Enhanced CustomList with Statistics ===")
enhanced_list = CustomList([10, 20, 30, 40, 50])

# Test various operations
print("Testing access operations:")
print(f"Item at index 0: {enhanced_list[0]}")
print(f"Item at index -1: {enhanced_list[-1]}")
print(f"Slice [1:3]: {enhanced_list[1:3]}")

print("\nTesting modification operations:")
enhanced_list[0] = 100
enhanced_list[-1] = 500
enhanced_list[1:3] = [200, 300]

print(f"\nFinal list: {enhanced_list}")
print(f"Statistics: {enhanced_list.get_stats()}")

# What we accomplished in this step:
# - Enhanced CustomList with access and modification counters
# - Added support for slice operations
# - Provided statistics about list usage
# - Demonstrated more sophisticated logging


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Inheriting from built-in types like list
# - Overriding special methods (__getitem__, __setitem__)
# - Using super() to call parent class methods
# - Adding custom behavior while preserving original functionality
# - Handling different types of indices (integers, slices)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding logging for append, insert, etc.!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
