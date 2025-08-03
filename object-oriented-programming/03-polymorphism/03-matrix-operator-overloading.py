"""Question: Implement a class Matrix that supports matrix addition and multiplication.
Override the __add__ and __mul__ methods.
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
# - How do you represent a matrix? (list of lists)
# - What is matrix addition? (add corresponding elements)
# - What is matrix multiplication? (row × column dot products)
# - How do you use zip() to work with rows and columns?
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


# Step 1: Define the Matrix class
# ===============================================================================

# Explanation:
# Let's start by creating our Matrix class. We'll represent the matrix
# as a list of lists, where each inner list is a row.

class Matrix:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Matrix class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The __init__ method takes a 2D list (list of lists) to represent the matrix data.
# Each inner list represents a row of the matrix.

class Matrix:
    def __init__(self, data):
        self.data = data

# What we accomplished in this step:
# - Added constructor to store matrix data


# Step 3: Add the __add__ method for matrix addition
# ===============================================================================

# Explanation:
# Matrix addition adds corresponding elements: A[i][j] + B[i][j]
# We use zip() to pair up rows, then zip() again to pair up elements in each row.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []
        for row1, row2 in zip(self.data, other.data):
            result.append([x + y for x, y in zip(row1, row2)])
        return Matrix(result)

# What we accomplished in this step:
# - Added __add__ method for matrix addition using zip()
# - Returns a new Matrix with added elements


# Step 4: Add the __mul__ method for matrix multiplication
# ===============================================================================

# Explanation:
# Matrix multiplication: (A × B)[i][j] = sum of A[i][k] × B[k][j] for all k
# We iterate through rows of first matrix and columns of second matrix.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []
        for row1, row2 in zip(self.data, other.data):
            result.append([x + y for x, y in zip(row1, row2)])
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for row in self.data:
            new_row = []
            for col in zip(*other.data):  # zip(*other.data) transposes the matrix
                new_row.append(sum(x * y for x, y in zip(row, col)))
            result.append(new_row)
        return Matrix(result)

# What we accomplished in this step:
# - Added __mul__ method for matrix multiplication
# - Used zip(*other.data) to transpose and get columns


# Step 5: Add the __str__ method for nice printing
# ===============================================================================

# Explanation:
# The __str__ method formats the matrix nicely for printing.
# We join elements in each row with spaces, then join rows with newlines.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []
        for row1, row2 in zip(self.data, other.data):
            result.append([x + y for x, y in zip(row1, row2)])
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for row in self.data:
            new_row = []
            for col in zip(*other.data):
                new_row.append(sum(x * y for x, y in zip(row, col)))
            result.append(new_row)
        return Matrix(result)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

# What we accomplished in this step:
# - Added __str__ method for readable matrix display


# Step 6: Create instances and test our class
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Matrix class and test both addition
# and multiplication to make sure everything works correctly.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []
        for row1, row2 in zip(self.data, other.data):
            result.append([x + y for x, y in zip(row1, row2)])
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for row in self.data:
            new_row = []
            for col in zip(*other.data):
                new_row.append(sum(x * y for x, y in zip(row, col)))
            result.append(new_row)
        return Matrix(result)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

# Test our class:
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print("Matrix 1:")
print(m1)
print("\nMatrix 2:")
print(m2)

print("\nMatrix Addition (m1 + m2):")
result_add = m1 + m2
print(result_add)

print("\nMatrix Multiplication (m1 * m2):")
result_mul = m1 * m2
print(result_mul)

# Let's verify the multiplication manually:
# [1, 2]   [5, 6]   [1*5+2*7, 1*6+2*8]   [19, 22]
# [3, 4] × [7, 8] = [3*5+4*7, 3*6+4*8] = [43, 50]

# What we accomplished in this step:
# - Created and tested our complete Matrix implementation
# - Demonstrated both addition and multiplication operations


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Matrix mathematics (addition and multiplication)
# - Advanced use of zip() function and unpacking
# - List comprehensions for matrix operations
# - Operator overloading with __add__ and __mul__
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding matrix subtraction or determinant!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================