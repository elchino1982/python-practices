"""Question: Implement a class LazyProperty that uses the descriptor protocol
to implement a property that is computed on first access and then cached.
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
# - What is the descriptor protocol and what methods does it use?
# - How do you cache a computed value to avoid recomputation?
# - How can you use a decorator to make this easy to use?
# - What happens on the first access vs subsequent accesses?
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


# Step 1: Define the LazyProperty class
# ===============================================================================

# Explanation:
# Let's start by creating our LazyProperty class. This class will implement
# the descriptor protocol to create properties that are computed only once.

class LazyProperty:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic LazyProperty class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The constructor should store the function that will compute the property value
# and initialize a cache to store the computed result.

class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.value = None

# What we accomplished in this step:
# - Added constructor that stores the computation function
# - Initialized value cache to None (indicating not computed yet)


# Step 3: Add the __get__ method
# ===============================================================================

# Explanation:
# The __get__ method is part of the descriptor protocol. It's called when
# the property is accessed. We'll check if the value is cached, and if not,
# compute and cache it.

class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.value = None

    def __get__(self, instance, owner):
        if self.value is None:
            self.value = self.func(instance)
        return self.value

# What we accomplished in this step:
# - Added __get__ method to handle property access
# - Implemented lazy evaluation: compute only on first access
# - Cache the result for subsequent accesses


# Step 4: Create a class that uses LazyProperty
# ===============================================================================

# Explanation:
# Now let's create a class that uses our LazyProperty descriptor.
# We'll use it as a decorator on a method that performs an expensive computation.

class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.value = None

    def __get__(self, instance, owner):
        if self.value is None:
            self.value = self.func(instance)
        return self.value

class MyClass:
    @LazyProperty
    def expensive_computation(self):
        print("Computing value")
        return 42

# What we accomplished in this step:
# - Created MyClass that uses LazyProperty as a decorator
# - Added a method that simulates expensive computation


# Step 5: Test our LazyProperty implementation
# ===============================================================================

# Explanation:
# Let's test our LazyProperty by accessing it multiple times and observing
# that the computation only happens once.

class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.value = None

    def __get__(self, instance, owner):
        if self.value is None:
            self.value = self.func(instance)
        return self.value

class MyClass:
    @LazyProperty
    def expensive_computation(self):
        print("Computing value")
        return 42

# Test our LazyProperty:
print("=== Testing LazyProperty ===")
obj = MyClass()

print("First access:")
result1 = obj.expensive_computation
print(f"Result: {result1}")

print("\nSecond access:")
result2 = obj.expensive_computation
print(f"Result: {result2}")

print("\nThird access:")
result3 = obj.expensive_computation
print(f"Result: {result3}")

# What we accomplished in this step:
# - Created an instance and accessed the lazy property multiple times
# - Verified that computation only happens on first access
# - Confirmed that cached value is returned on subsequent accesses


# Step 6: Enhanced version with per-instance caching
# ===============================================================================

# Explanation:
# The previous version has a problem: the cache is shared across all instances.
# Let's fix this by using per-instance caching.

class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.attr_name = f"_lazy_{func.__name__}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check if value is already cached for this instance
        if not hasattr(instance, self.attr_name):
            # Compute and cache the value
            value = self.func(instance)
            setattr(instance, self.attr_name, value)
        
        return getattr(instance, self.attr_name)

class Calculator:
    def __init__(self, base_value):
        self.base_value = base_value

    @LazyProperty
    def expensive_calculation(self):
        print(f"Computing expensive calculation for base_value={self.base_value}")
        import time
        time.sleep(0.1)  # Simulate expensive computation
        return self.base_value ** 2 + self.base_value * 10

    @LazyProperty
    def another_calculation(self):
        print(f"Computing another calculation for base_value={self.base_value}")
        return self.base_value * 3 + 100

# Test enhanced version:
print("\n=== Enhanced LazyProperty with Per-Instance Caching ===")

calc1 = Calculator(5)
calc2 = Calculator(10)

print("Testing calc1 (base_value=5):")
print(f"First access: {calc1.expensive_calculation}")
print(f"Second access: {calc1.expensive_calculation}")

print("\nTesting calc2 (base_value=10):")
print(f"First access: {calc2.expensive_calculation}")
print(f"Second access: {calc2.expensive_calculation}")

print("\nTesting another property on calc1:")
print(f"First access: {calc1.another_calculation}")
print(f"Second access: {calc1.another_calculation}")

# What we accomplished in this step:
# - Fixed the shared cache problem by using per-instance caching
# - Used dynamic attribute names to store cached values
# - Demonstrated multiple lazy properties on the same class
# - Showed that different instances have independent caches


# Step 7: Advanced version with cache invalidation
# ===============================================================================

# Explanation:
# Let's create an advanced version that allows cache invalidation and
# provides more control over the lazy property behavior.

class AdvancedLazyProperty:
    def __init__(self, func, invalidate_on=None):
        self.func = func
        self.attr_name = f"_lazy_{func.__name__}"
        self.computed_attr = f"_lazy_computed_{func.__name__}"
        self.invalidate_on = invalidate_on or []

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check if we need to invalidate cache
        if self._should_invalidate(instance):
            self._invalidate_cache(instance)
        
        # Check if value is already cached
        if not getattr(instance, self.computed_attr, False):
            # Compute and cache the value
            value = self.func(instance)
            setattr(instance, self.attr_name, value)
            setattr(instance, self.computed_attr, True)
        
        return getattr(instance, self.attr_name)

    def _should_invalidate(self, instance):
        # Check if any of the invalidation attributes have changed
        for attr in self.invalidate_on:
            if hasattr(instance, f"_last_{attr}"):
                if getattr(instance, attr) != getattr(instance, f"_last_{attr}"):
                    return True
        return False

    def _invalidate_cache(self, instance):
        setattr(instance, self.computed_attr, False)
        # Update last known values
        for attr in self.invalidate_on:
            setattr(instance, f"_last_{attr}", getattr(instance, attr))

    def invalidate(self, instance):
        """Manually invalidate the cache for this instance"""
        setattr(instance, self.computed_attr, False)

class SmartCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @AdvancedLazyProperty(invalidate_on=['x', 'y'])
    def complex_calculation(self):
        print(f"Computing complex calculation for x={self.x}, y={self.y}")
        return self.x ** 2 + self.y ** 2 + self.x * self.y

    def update_values(self, x, y):
        self.x = x
        self.y = y

# Test advanced version:
print("\n=== Advanced LazyProperty with Cache Invalidation ===")

smart_calc = SmartCalculator(3, 4)

print("First calculation:")
result1 = smart_calc.complex_calculation
print(f"Result: {result1}")

print("\nSecond calculation (should use cache):")
result2 = smart_calc.complex_calculation
print(f"Result: {result2}")

print("\nUpdating values and recalculating:")
smart_calc.update_values(5, 6)
result3 = smart_calc.complex_calculation  # Should recompute
print(f"Result: {result3}")

print("\nAccessing again (should use new cache):")
result4 = smart_calc.complex_calculation
print(f"Result: {result4}")

# What we accomplished in this step:
# - Added automatic cache invalidation based on dependent attributes
# - Provided manual cache invalidation method
# - Demonstrated more sophisticated lazy property behavior
# - Showed how to handle dependencies between properties and attributes


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the descriptor protocol (__get__ method)
# - Implementing lazy evaluation and caching
# - Using descriptors as decorators
# - Per-instance vs shared caching strategies
# - Cache invalidation techniques
# - Advanced descriptor features
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding cache size limits!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
