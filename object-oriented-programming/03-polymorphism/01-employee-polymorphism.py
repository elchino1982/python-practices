"""Question: Create a class named Employee with attributes name and salary.
Add a method to give a raise (increase the salary by a given percentage).
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
# - What attributes does the Employee class need?
# - How do you calculate a percentage increase?
# - Should the method modify the existing salary or return a new value?
# - How do you handle the percentage calculation (10% = 10 or 0.1)?
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


# Step 1: Define the Employee class
# ===============================================================================

# Explanation:
# Let's start by creating our Employee class. This class will represent
# an employee with basic information and salary management capabilities.

class Employee:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Employee class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The __init__ method initializes the Employee with name and salary attributes.
# These are the basic pieces of information we need for each employee.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# What we accomplished in this step:
# - Added constructor to initialize name and salary attributes


# Step 3: Add the give_raise method
# ===============================================================================

# Explanation:
# Now let's add the give_raise method that increases the salary by a given percentage.
# We'll modify the existing salary directly.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)

# What we accomplished in this step:
# - Added give_raise method that calculates and applies percentage increase


# Step 4: Create an instance and test our class
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our Employee class and test it to make sure everything works correctly.
# This demonstrates how salary calculations work in practice.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)

# Test our class:
employee = Employee("Alice", 50000)

print(f"Employee: {employee.name}")
print(f"Initial salary: ${employee.salary}")

# Give a 10% raise
employee.give_raise(10)
print(f"Salary after 10% raise: ${employee.salary}")

# Give another 5% raise
employee.give_raise(5)
print(f"Salary after additional 5% raise: ${employee.salary}")

# What we accomplished in this step:
# - Created and tested our complete Employee implementation
# - Demonstrated how percentage calculations work


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Basic class design with attributes and methods
# - Percentage calculations in programming
# - Modifying object state through methods
# - Testing with multiple operations
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a method to give a fixed amount raise!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================