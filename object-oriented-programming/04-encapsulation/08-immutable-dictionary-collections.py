"""Question: Implement a class ImmutableDict that inherits from dict
and overrides methods to make it immutable.
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
# - What methods does dict have that can modify its contents?
# - How do you override methods to prevent modifications?
# - What exception should you raise for immutable objects?
# - Which methods need to be overridden: __setitem__, __delitem__, clear, pop, etc.?
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


# Step 1: Define the ImmutableDict class
# ===============================================================================

# Explanation:
# Let's start by creating our ImmutableDict class that inherits from dict.
# This gives us all the functionality of a regular dictionary, which we'll then restrict.

class ImmutableDict(dict):
    pass  # We'll add method overrides next

# What we accomplished in this step:
# - Created ImmutableDict class that inherits from dict
# - Inherits all dict functionality by default


# Step 2: Override __setitem__ to prevent item assignment
# ===============================================================================

# Explanation:
# The __setitem__ method is called when you use dict[key] = value syntax.
# We need to override it to raise an exception instead of allowing modifications.

class ImmutableDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("This dictionary is immutable")

# What we accomplished in this step:
# - Overrode __setitem__ to prevent setting new values
# - Raises TypeError with descriptive message


# Step 3: Override __delitem__ to prevent item deletion
# ===============================================================================

# Explanation:
# The __delitem__ method is called when you use del dict[key] syntax.
# We need to override it to prevent deletions.

class ImmutableDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("This dictionary is immutable")

    def __delitem__(self, key):
        raise TypeError("This dictionary is immutable")

# What we accomplished in this step:
# - Overrode __delitem__ to prevent deleting items
# - Maintains immutability for deletion operations


# Step 4: Override clear method
# ===============================================================================

# Explanation:
# The clear method removes all items from the dictionary.
# We need to override it to prevent clearing the dictionary.

class ImmutableDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("This dictionary is immutable")

    def __delitem__(self, key):
        raise TypeError("This dictionary is immutable")

    def clear(self):
        raise TypeError("This dictionary is immutable")

# What we accomplished in this step:
# - Overrode clear method to prevent removing all items
# - Prevents bulk modifications to the dictionary


# Step 5: Override pop and popitem methods
# ===============================================================================

# Explanation:
# The pop and popitem methods remove and return items from the dictionary.
# We need to override both to prevent any removal operations.

class ImmutableDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("This dictionary is immutable")

    def __delitem__(self, key):
        raise TypeError("This dictionary is immutable")

    def clear(self):
        raise TypeError("This dictionary is immutable")

    def pop(self, key, default=None):
        raise TypeError("This dictionary is immutable")

    def popitem(self):
        raise TypeError("This dictionary is immutable")

# What we accomplished in this step:
# - Overrode pop method to prevent removing specific items
# - Overrode popitem method to prevent removing arbitrary items


# Step 6: Override update method
# ===============================================================================

# Explanation:
# The update method adds multiple key-value pairs to the dictionary.
# We need to override it to prevent bulk updates.

class ImmutableDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("This dictionary is immutable")

    def __delitem__(self, key):
        raise TypeError("This dictionary is immutable")

    def clear(self):
        raise TypeError("This dictionary is immutable")

    def pop(self, key, default=None):
        raise TypeError("This dictionary is immutable")

    def popitem(self):
        raise TypeError("This dictionary is immutable")

    def update(self, *args, **kwargs):
        raise TypeError("This dictionary is immutable")

# What we accomplished in this step:
# - Overrode update method to prevent bulk modifications
# - Completed all major modification methods


# Step 7: Test our immutable dictionary
# ===============================================================================

# Explanation:
# Now let's test our ImmutableDict to make sure it properly prevents all
# modification attempts while still allowing read operations.

class ImmutableDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("This dictionary is immutable")

    def __delitem__(self, key):
        raise TypeError("This dictionary is immutable")

    def clear(self):
        raise TypeError("This dictionary is immutable")

    def pop(self, key, default=None):
        raise TypeError("This dictionary is immutable")

    def popitem(self):
        raise TypeError("This dictionary is immutable")

    def update(self, *args, **kwargs):
        raise TypeError("This dictionary is immutable")

# Test our immutable dictionary:
print("=== Creating ImmutableDict ===")
immut_dict = ImmutableDict(a=1, b=2, c=3)
print(f"Created dictionary: {immut_dict}")

print("\n=== Testing read operations (should work) ===")
print(f"Value of 'a': {immut_dict['a']}")
print(f"Keys: {list(immut_dict.keys())}")
print(f"Values: {list(immut_dict.values())}")
print(f"Items: {list(immut_dict.items())}")

print("\n=== Testing modification attempts (should fail) ===")

# Test __setitem__
try:
    immut_dict['d'] = 4
except TypeError as e:
    print(f"✓ Setting new item failed: {e}")

# Test __delitem__
try:
    del immut_dict['a']
except TypeError as e:
    print(f"✓ Deleting item failed: {e}")

# Test clear
try:
    immut_dict.clear()
except TypeError as e:
    print(f"✓ Clearing failed: {e}")

# Test pop
try:
    immut_dict.pop('b')
except TypeError as e:
    print(f"✓ Pop failed: {e}")

# Test popitem
try:
    immut_dict.popitem()
except TypeError as e:
    print(f"✓ Popitem failed: {e}")

# Test update
try:
    immut_dict.update({'x': 10})
except TypeError as e:
    print(f"✓ Update failed: {e}")

print(f"\n=== Final state ===")
print(f"Dictionary unchanged: {immut_dict}")

# What we accomplished in this step:
# - Created and tested our complete ImmutableDict implementation
# - Verified that read operations work normally
# - Confirmed that all modification attempts are properly blocked
# - Demonstrated that the dictionary remains unchanged


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Inheriting from built-in types like dict
# - Overriding methods to change behavior
# - Creating immutable data structures
# - Understanding all the ways a dictionary can be modified
# - Proper exception handling for invalid operations
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating an ImmutableList!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
