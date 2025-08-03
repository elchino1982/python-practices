"""Question: Implement a class Polynomial that supports polynomial addition,
subtraction, and evaluation. Override the __add__, __sub__, and __call__ methods.
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
# - How do you represent a polynomial? (list of coefficients)
# - What is polynomial addition? (add corresponding coefficients)
# - What is polynomial evaluation? (substitute x and calculate result)
# - What does the __call__ method do? (makes objects callable like functions)
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


# Step 1: Define the Polynomial class
# ===============================================================================

# Explanation:
# Let's start by creating our Polynomial class. We'll represent polynomials
# using a list of coefficients, where index represents the power of x.

class Polynomial:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Polynomial class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The __init__ method takes a list of coefficients. For example,
# [1, 2, 3] represents 1 + 2x + 3x^2.

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

# What we accomplished in this step:
# - Added constructor to store polynomial coefficients


# Step 3: Add the __add__ method for polynomial addition
# ===============================================================================

# Explanation:
# Polynomial addition adds corresponding coefficients.
# (a + bx + cx^2) + (d + ex + fx^2) = (a+d) + (b+e)x + (c+f)x^2

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

# What we accomplished in this step:
# - Added __add__ method for polynomial addition using zip()


# Step 4: Add the __sub__ method for polynomial subtraction
# ===============================================================================

# Explanation:
# Polynomial subtraction subtracts corresponding coefficients.
# (a + bx + cx^2) - (d + ex + fx^2) = (a-d) + (b-e)x + (c-f)x^2

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __sub__(self, other):
        result = [a - b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

# What we accomplished in this step:
# - Added __sub__ method for polynomial subtraction


# Step 5: Add the __call__ method for polynomial evaluation
# ===============================================================================

# Explanation:
# The __call__ method makes our polynomial callable like a function.
# To evaluate: substitute x and calculate sum of coef * x^power for each term.

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __sub__(self, other):
        result = [a - b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

# What we accomplished in this step:
# - Added __call__ method to evaluate polynomial at given x value


# Step 6: Add the __str__ method for nice printing
# ===============================================================================

# Explanation:
# The __str__ method formats the polynomial nicely for display.
# We'll show it in standard mathematical notation.

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __sub__(self, other):
        result = [a - b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(str(coef))
                elif i == 1:
                    terms.append(f"{coef}x")
                else:
                    terms.append(f"{coef}x^{i}")
        return " + ".join(terms) if terms else "0"

# What we accomplished in this step:
# - Added __str__ method for readable polynomial display


# Step 7: Create instances and test our class
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Polynomial class and test all operations
# to make sure everything works correctly.

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __sub__(self, other):
        result = [a - b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def __str__(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(str(coef))
                elif i == 1:
                    terms.append(f"{coef}x")
                else:
                    terms.append(f"{coef}x^{i}")
        return " + ".join(terms) if terms else "0"

# Test our class:
p1 = Polynomial([1, 2, 3])  # Represents 1 + 2x + 3x^2
p2 = Polynomial([3, 2, 1])  # Represents 3 + 2x + 1x^2

print(f"Polynomial 1: {p1}")
print(f"Polynomial 2: {p2}")

# Test addition
result_add = p1 + p2
print(f"Addition: ({p1}) + ({p2}) = {result_add}")

# Test subtraction
result_sub = p1 - p2
print(f"Subtraction: ({p1}) - ({p2}) = {result_sub}")

# Test evaluation
x_value = 2
result_eval = p1(x_value)
print(f"Evaluation: p1({x_value}) = {result_eval}")
# Manual check: 1 + 2*2 + 3*2^2 = 1 + 4 + 12 = 17

# What we accomplished in this step:
# - Created and tested our complete Polynomial implementation
# - Demonstrated all mathematical operations working correctly


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Polynomial mathematics and representation
# - Advanced operator overloading (__add__, __sub__, __call__)
# - Making objects callable with __call__ method
# - Mathematical computation with enumerate() and sum()
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding polynomial multiplication!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================