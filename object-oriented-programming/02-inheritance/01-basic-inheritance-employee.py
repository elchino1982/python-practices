"""Question: Define a class named Employee with attributes name and salary.
Create a subclass named Manager that inherits from Employee and adds an attribute
department. Override the __str__ method to print the details of the manager.
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
# - How do you create a subclass that inherits from another class?
# - What is the super() function and how do you use it?
# - How do you override the __str__ method?
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
# Let's start by creating our Employee class. This will be our base class that
# contains the common attributes for all employees.

class Employee:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Employee class structure


# Step 2: Add the constructor to Employee class
# ===============================================================================

# Explanation:
# The __init__ method initializes the Employee with name and salary attributes.
# These will be inherited by any subclass we create.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# What we accomplished in this step:
# - Added constructor to initialize name and salary attributes


# Step 3: Define the Manager subclass
# ===============================================================================

# Explanation:
# Now let's create the Manager class that inherits from Employee. In Python,
# we specify inheritance by putting the parent class name in parentheses.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created Manager class that inherits from Employee


# Step 4: Add constructor to Manager class
# ===============================================================================

# Explanation:
# The Manager constructor needs to accept name, salary, and department.
# We use super().__init__() to call the parent class constructor for name and salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent constructor
        self.department = department    # Add new attribute

# What we accomplished in this step:
# - Added Manager constructor that uses super() to inherit Employee attributes
# - Added department attribute specific to Manager


# Step 5: Override the __str__ method
# ===============================================================================

# Explanation:
# The __str__ method is called when we print an object or convert it to a string.
# We override it to provide a custom string representation for Manager objects.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager: {self.name}, Department: {self.department}, Salary: {self.salary}"

# What we accomplished in this step:
# - Added __str__ method to provide custom string representation


# Step 6: Create an instance and test our classes
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our Manager class and test it to make sure everything works correctly.
# This demonstrates inheritance and method overriding in action.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager: {self.name}, Department: {self.department}, Salary: {self.salary}"

# Test our classes:
manager = Manager("Alice", 75000, "Engineering")
print(manager)

# Let's also test that Manager inherits Employee attributes
print(f"Manager name: {manager.name}")
print(f"Manager salary: {manager.salary}")
print(f"Manager department: {manager.department}")

# What we accomplished in this step:
# - Created and tested our complete Employee and Manager implementation
# - Demonstrated inheritance and method overriding


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Class inheritance using parentheses syntax
# - Using super() to call parent class methods
# - Method overriding (__str__ method)
# - Adding new attributes in subclasses
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications
#
# Remember: The best way to learn is by doing!
# ===============================================================================