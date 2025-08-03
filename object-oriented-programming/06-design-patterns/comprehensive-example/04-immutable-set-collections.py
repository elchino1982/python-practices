"""Question: Implement a class ImmutableSet that inherits from set
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
# - What methods does set have that can modify its contents?
# - How can you override multiple methods efficiently?
# - What's a good way to prevent modifications after initialization?
# - Which methods need to be blocked: add, remove, discard, pop, clear, update, etc.?
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


# Step 1: Define the ImmutableSet class
# ===============================================================================

# Explanation:
# Let's start by creating our ImmutableSet class that inherits from the built-in set.
# This gives us all the functionality of a regular set, which we'll then restrict.

class ImmutableSet(set):
    pass  # We'll add method overrides next

# What we accomplished in this step:
# - Created ImmutableSet class that inherits from set
# - Inherits all set functionality by default


# Step 2: Add constructor with freezing mechanism
# ===============================================================================

# Explanation:
# The constructor should initialize the set with the given data and then
# "freeze" it to prevent further modifications.

class ImmutableSet(set):
    def __init__(self, *args):
        super().__init__(*args)
        self._frozen = True

# What we accomplished in this step:
# - Added constructor that initializes the set normally
# - Added _frozen flag to track immutable state


# Step 3: Create a helper method for immutable operations
# ===============================================================================

# Explanation:
# Instead of overriding each method individually, let's create a helper method
# that raises an exception when called. We'll use this for all modifying operations.

class ImmutableSet(set):
    def __init__(self, *args):
        super().__init__(*args)
        self._frozen = True

    def _immutable(self, *args, **kwargs):
        if self._frozen:
            raise TypeError("This set is immutable")

# What we accomplished in this step:
# - Created helper method that checks frozen state
# - Raises TypeError with descriptive message when set is frozen


# Step 4: Override modification methods
# ===============================================================================

# Explanation:
# Now let's override all the methods that can modify the set by assigning
# them to our _immutable helper method.

class ImmutableSet(set):
    def __init__(self, *args):
        super().__init__(*args)
        self._frozen = True

    def _immutable(self, *args, **kwargs):
        if self._frozen:
            raise TypeError("This set is immutable")

    add = _immutable
    remove = _immutable
    discard = _immutable
    pop = _immutable
    clear = _immutable

# What we accomplished in this step:
# - Overrode basic modification methods
# - All these methods now raise exceptions when called


# Step 5: Override update methods
# ===============================================================================

# Explanation:
# Let's also override the update methods that can modify the set in bulk.

class ImmutableSet(set):
    def __init__(self, *args):
        super().__init__(*args)
        self._frozen = True

    def _immutable(self, *args, **kwargs):
        if self._frozen:
            raise TypeError("This set is immutable")

    add = _immutable
    remove = _immutable
    discard = _immutable
    pop = _immutable
    clear = _immutable
    update = _immutable
    intersection_update = _immutable
    difference_update = _immutable
    symmetric_difference_update = _immutable

# What we accomplished in this step:
# - Overrode all bulk update methods
# - Ensured comprehensive immutability


# Step 6: Test our ImmutableSet implementation
# ===============================================================================

# Explanation:
# Let's test our ImmutableSet by trying various operations and verifying
# that modifications are blocked while read operations work normally.

class ImmutableSet(set):
    def __init__(self, *args):
        super().__init__(*args)
        self._frozen = True

    def _immutable(self, *args, **kwargs):
        if self._frozen:
            raise TypeError("This set is immutable")

    add = _immutable
    remove = _immutable
    discard = _immutable
    pop = _immutable
    clear = _immutable
    update = _immutable
    intersection_update = _immutable
    difference_update = _immutable
    symmetric_difference_update = _immutable

# Test our ImmutableSet:
print("=== Testing ImmutableSet ===")
immut_set = ImmutableSet([1, 2, 3, 4, 5])
print(f"Created set: {immut_set}")

print("\n=== Testing read operations (should work) ===")
print(f"Length: {len(immut_set)}")
print(f"Contains 3: {3 in immut_set}")
print(f"Union with {6, 7}: {immut_set | {6, 7}}")
print(f"Intersection with {3, 4, 5, 6}: {immut_set & {3, 4, 5, 6}}")

print("\n=== Testing modification attempts (should fail) ===")

# Test add
try:
    immut_set.add(6)
except TypeError as e:
    print(f"✓ Add failed: {e}")

# Test remove
try:
    immut_set.remove(1)
except TypeError as e:
    print(f"✓ Remove failed: {e}")

# Test discard
try:
    immut_set.discard(2)
except TypeError as e:
    print(f"✓ Discard failed: {e}")

# Test pop
try:
    immut_set.pop()
except TypeError as e:
    print(f"✓ Pop failed: {e}")

# Test clear
try:
    immut_set.clear()
except TypeError as e:
    print(f"✓ Clear failed: {e}")

# Test update
try:
    immut_set.update([6, 7])
except TypeError as e:
    print(f"✓ Update failed: {e}")

print(f"\n=== Final state ===")
print(f"Set unchanged: {immut_set}")

# What we accomplished in this step:
# - Created and tested our complete ImmutableSet implementation
# - Verified that read operations work normally
# - Confirmed that all modification attempts are properly blocked
# - Demonstrated that the set remains unchanged


# Step 7: Enhanced version with better error messages
# ===============================================================================

# Explanation:
# Let's create an enhanced version that provides more specific error messages
# for different operations and includes additional safety features.

class EnhancedImmutableSet(set):
    def __init__(self, *args):
        super().__init__(*args)
        self._frozen = True
        self._creation_size = len(self)

    def _raise_immutable_error(self, operation):
        raise TypeError(f"Cannot {operation} on immutable set")

    def add(self, elem):
        self._raise_immutable_error("add element")

    def remove(self, elem):
        self._raise_immutable_error("remove element")

    def discard(self, elem):
        self._raise_immutable_error("discard element")

    def pop(self):
        self._raise_immutable_error("pop element")

    def clear(self):
        self._raise_immutable_error("clear set")

    def update(self, *others):
        self._raise_immutable_error("update set")

    def intersection_update(self, *others):
        self._raise_immutable_error("update intersection")

    def difference_update(self, *others):
        self._raise_immutable_error("update difference")

    def symmetric_difference_update(self, other):
        self._raise_immutable_error("update symmetric difference")

    def get_info(self):
        return {
            'size': len(self),
            'creation_size': self._creation_size,
            'is_frozen': self._frozen,
            'elements': sorted(list(self)) if all(isinstance(x, (int, float, str)) for x in self) else list(self)
        }

# Test enhanced version:
print("\n=== Enhanced ImmutableSet with Better Error Messages ===")

enhanced_set = EnhancedImmutableSet(['apple', 'banana', 'cherry'])
print(f"Created set: {enhanced_set}")
print(f"Set info: {enhanced_set.get_info()}")

print("\nTesting specific error messages:")
try:
    enhanced_set.add('date')
except TypeError as e:
    print(f"✓ {e}")

try:
    enhanced_set.remove('apple')
except TypeError as e:
    print(f"✓ {e}")

try:
    enhanced_set.clear()
except TypeError as e:
    print(f"✓ {e}")

# What we accomplished in this step:
# - Enhanced error messages for better debugging
# - Added individual method overrides for clarity
# - Included metadata about the set
# - Provided better user experience


# Step 8: Comparison with regular set
# ===============================================================================

# Explanation:
# Let's demonstrate the difference between our ImmutableSet and a regular set
# to highlight the benefits of immutability.

print("\n=== Comparing ImmutableSet vs Regular Set ===")

# Regular set
regular_set = {1, 2, 3}
print(f"Regular set: {regular_set}")

print("Modifying regular set:")
regular_set.add(4)
print(f"After add(4): {regular_set}")
regular_set.remove(1)
print(f"After remove(1): {regular_set}")

# Immutable set
immutable_set = ImmutableSet([1, 2, 3])
print(f"\nImmutable set: {immutable_set}")

print("Attempting to modify immutable set:")
try:
    immutable_set.add(4)
    print("ERROR: Should not reach here!")
except TypeError:
    print("✓ add(4) blocked - set remains unchanged")

try:
    immutable_set.remove(1)
    print("ERROR: Should not reach here!")
except TypeError:
    print("✓ remove(1) blocked - set remains unchanged")

print(f"Immutable set still: {immutable_set}")

# Demonstrate safe operations
print(f"\nSafe operations on immutable set:")
print(f"Union: {immutable_set | {4, 5}}")
print(f"Intersection: {immutable_set & {2, 3, 4}}")
print(f"Difference: {immutable_set - {1}}")
print(f"Original set unchanged: {immutable_set}")

# What we accomplished in this step:
# - Demonstrated the difference between mutable and immutable sets
# - Showed that safe operations (union, intersection, etc.) still work
# - Highlighted the benefits of immutability for data integrity


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Inheriting from built-in types like set
# - Overriding methods to change behavior
# - Creating immutable data structures
# - Using helper methods to reduce code duplication
# - Providing clear error messages for better user experience
# - Understanding the difference between mutable and immutable collections
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating an ImmutableList with similar techniques!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
