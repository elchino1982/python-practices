"""Question: Implement a class Vector that supports
vector addition, subtraction, and dot product.
Override the __add__, __sub__, and __mul__ methods.
Use encapsulation to ensure vectors are of the same length for these operations.
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
# - How do you handle variable-length vectors? (*args in constructor)
# - What is encapsulation? (private attributes with _)
# - How do you validate vector lengths? (check before operations)
# - What should happen with mismatched lengths? (raise ValueError)
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


# Step 1: Define the Vector class with encapsulated components
# ===============================================================================

# Explanation:
# Let's start by creating our Vector class that can handle variable-length vectors.
# We'll use *components to accept any number of components and store them privately.

class Vector:
    def __init__(self, *components):
        self._components = components

# What we accomplished in this step:
# - Created Vector class with private _components attribute
# - Used *components to accept variable-length arguments


# Step 2: Add length validation helper method
# ===============================================================================

# Explanation:
# Let's add a private method to validate that two vectors have the same length.
# This encapsulates the validation logic and makes our code cleaner.

class Vector:
    def __init__(self, *components):
        self._components = components

    def _validate_same_length(self, other):
        if len(self._components) != len(other._components):
            raise ValueError(f"Vectors must be of the same length: {len(self._components)} vs {len(other._components)}")

# What we accomplished in this step:
# - Added private validation method for length checking


# Step 3: Add the __add__ method for vector addition
# ===============================================================================

# Explanation:
# Vector addition adds corresponding components. We validate lengths first,
# then create a new Vector with the summed components.

class Vector:
    def __init__(self, *components):
        self._components = components

    def _validate_same_length(self, other):
        if len(self._components) != len(other._components):
            raise ValueError(f"Vectors must be of the same length: {len(self._components)} vs {len(other._components)}")

    def __add__(self, other):
        self._validate_same_length(other)
        result = [a + b for a, b in zip(self._components, other._components)]
        return Vector(*result)

# What we accomplished in this step:
# - Added __add__ method with length validation
# - Used encapsulated validation method


# Step 4: Add the __sub__ method for vector subtraction
# ===============================================================================

# Explanation:
# Vector subtraction subtracts corresponding components. Similar to addition,
# but we subtract instead of add.

class Vector:
    def __init__(self, *components):
        self._components = components

    def _validate_same_length(self, other):
        if len(self._components) != len(other._components):
            raise ValueError(f"Vectors must be of the same length: {len(self._components)} vs {len(other._components)}")

    def __add__(self, other):
        self._validate_same_length(other)
        result = [a + b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __sub__(self, other):
        self._validate_same_length(other)
        result = [a - b for a, b in zip(self._components, other._components)]
        return Vector(*result)

# What we accomplished in this step:
# - Added __sub__ method for vector subtraction


# Step 5: Add the __mul__ method for dot product
# ===============================================================================

# Explanation:
# The dot product multiplies corresponding components and sums the results.
# This returns a scalar (number), not a vector.

class Vector:
    def __init__(self, *components):
        self._components = components

    def _validate_same_length(self, other):
        if len(self._components) != len(other._components):
            raise ValueError(f"Vectors must be of the same length: {len(self._components)} vs {len(other._components)}")

    def __add__(self, other):
        self._validate_same_length(other)
        result = [a + b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __sub__(self, other):
        self._validate_same_length(other)
        result = [a - b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __mul__(self, other):
        self._validate_same_length(other)
        return sum(a * b for a, b in zip(self._components, other._components))

# What we accomplished in this step:
# - Added __mul__ method for dot product calculation


# Step 6: Add properties for safe access to components
# ===============================================================================

# Explanation:
# Let's add properties to safely access vector information without exposing
# the private _components directly.

class Vector:
    def __init__(self, *components):
        self._components = components

    def _validate_same_length(self, other):
        if len(self._components) != len(other._components):
            raise ValueError(f"Vectors must be of the same length: {len(self._components)} vs {len(other._components)}")

    @property
    def components(self):
        return tuple(self._components)  # Return immutable copy

    @property
    def dimension(self):
        return len(self._components)

    def __add__(self, other):
        self._validate_same_length(other)
        result = [a + b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __sub__(self, other):
        self._validate_same_length(other)
        result = [a - b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __mul__(self, other):
        self._validate_same_length(other)
        return sum(a * b for a, b in zip(self._components, other._components))

# What we accomplished in this step:
# - Added components property for safe access
# - Added dimension property for vector size


# Step 7: Add string representation and additional methods
# ===============================================================================

# Explanation:
# Let's add __str__ and __repr__ methods for better debugging and display.
# We'll also add a magnitude method for completeness.

class Vector:
    def __init__(self, *components):
        self._components = components

    def _validate_same_length(self, other):
        if len(self._components) != len(other._components):
            raise ValueError(f"Vectors must be of the same length: {len(self._components)} vs {len(other._components)}")

    @property
    def components(self):
        return tuple(self._components)

    @property
    def dimension(self):
        return len(self._components)

    def __add__(self, other):
        self._validate_same_length(other)
        result = [a + b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __sub__(self, other):
        self._validate_same_length(other)
        result = [a - b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __mul__(self, other):
        self._validate_same_length(other)
        return sum(a * b for a, b in zip(self._components, other._components))

    def magnitude(self):
        return sum(x ** 2 for x in self._components) ** 0.5

    def __str__(self):
        return f"Vector{self._components}"

    def __repr__(self):
        return f"Vector({', '.join(map(str, self._components))})"

# What we accomplished in this step:
# - Added magnitude method for vector length calculation
# - Added __str__ and __repr__ for better display


# Step 8: Create instances and test our vector operations
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Vector class and test all operations
# including error handling for mismatched vector lengths.

class Vector:
    def __init__(self, *components):
        self._components = components

    def _validate_same_length(self, other):
        if len(self._components) != len(other._components):
            raise ValueError(f"Vectors must be of the same length: {len(self._components)} vs {len(other._components)}")

    @property
    def components(self):
        return tuple(self._components)

    @property
    def dimension(self):
        return len(self._components)

    def __add__(self, other):
        self._validate_same_length(other)
        result = [a + b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __sub__(self, other):
        self._validate_same_length(other)
        result = [a - b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __mul__(self, other):
        self._validate_same_length(other)
        return sum(a * b for a, b in zip(self._components, other._components))

    def magnitude(self):
        return sum(x ** 2 for x in self._components) ** 0.5

    def __str__(self):
        return f"Vector{self._components}"

    def __repr__(self):
        return f"Vector({', '.join(map(str, self._components))})"

# Test our class:
print("Testing 3D vectors:")
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Dimensions: {v1.dimension}, {v2.dimension}")

# Test operations
print(f"Addition: {v1} + {v2} = {v1 + v2}")
print(f"Subtraction: {v1} - {v2} = {v1 - v2}")
print(f"Dot product: {v1} * {v2} = {v1 * v2}")
print(f"Magnitude of v1: {v1.magnitude():.2f}")

print("\nTesting 2D vectors:")
v3 = Vector(1, 2)
v4 = Vector(3, 4)
print(f"2D Addition: {v3} + {v4} = {v3 + v4}")

print("\nTesting error handling:")
try:
    result = v1 + v3  # Different dimensions
except ValueError as e:
    print(f"Error: {e}")

# What we accomplished in this step:
# - Created and tested our complete Vector implementation
# - Demonstrated encapsulation and error handling


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Variable-length argument handling (*args)
# - Encapsulation with private attributes and methods
# - Input validation and error handling
# - Properties for safe data access
# - Advanced operator overloading
# - Vector mathematics with any dimension
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding vector normalization or cross product!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================