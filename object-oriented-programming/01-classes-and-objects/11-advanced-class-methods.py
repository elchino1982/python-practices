"""Question: Define a class Employee with a class method from_string that creates
an instance from a string in the format "name-salary".
Also, add a static method is_valid_salary to check if a salary is a positive number.
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
# - What is a class method? (@classmethod decorator, takes cls as first parameter)
# - What is a static method? (@staticmethod decorator, no special first parameter)
# - How do you parse "name-salary" string? (split method)
# - When would you use class methods vs static methods?
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


# Step 1: Define the Employee class with basic constructor
# ===============================================================================

# Explanation:
# Let's start by creating our Employee class with a basic constructor.
# This will be the foundation for our class and static methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# What we accomplished in this step:
# - Created Employee class with name and salary attributes


# Step 2: Add static method for salary validation
# ===============================================================================

# Explanation:
# Static methods don't need access to the class or instance, they're just utility functions.
# The @staticmethod decorator creates a method that belongs to the class but doesn't need cls or self.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

# What we accomplished in this step:
# - Added static method to validate salary values


# Step 3: Add class method for creating instances from strings
# ===============================================================================

# Explanation:
# Class methods take 'cls' as the first parameter and can create new instances.
# The @classmethod decorator is perfect for alternative constructors.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

    @classmethod
    def from_string(cls, emp_str):
        name, salary_str = emp_str.split('-')
        salary = int(salary_str)
        return cls(name, salary)

# What we accomplished in this step:
# - Added class method to create Employee from string format


# Step 4: Add string representation method
# ===============================================================================

# Explanation:
# Let's add a __str__ method to make our Employee objects more readable.
# This will help us see what we're working with when testing.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

    @classmethod
    def from_string(cls, emp_str):
        name, salary_str = emp_str.split('-')
        salary = int(salary_str)
        return cls(name, salary)

    def __str__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

# What we accomplished in this step:
# - Added __str__ method for readable employee representation


# Step 5: Enhance the class method with validation
# ===============================================================================

# Explanation:
# Let's improve our from_string method to use the static method for validation.
# This demonstrates how static and class methods can work together.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

    @classmethod
    def from_string(cls, emp_str):
        try:
            name, salary_str = emp_str.split('-')
            salary = int(salary_str)
            
            if not cls.is_valid_salary(salary):
                raise ValueError(f"Invalid salary: {salary}")
            
            return cls(name, salary)
        except ValueError as e:
            print(f"Error creating employee from string '{emp_str}': {e}")
            return None

    def __str__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

# What we accomplished in this step:
# - Enhanced from_string method with validation using static method
# - Added error handling for invalid input


# Step 6: Create instances and test our methods
# ===============================================================================

# Explanation:
# Finally, let's create instances using both the regular constructor and the class method,
# and test our static method to make sure everything works correctly.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

    @classmethod
    def from_string(cls, emp_str):
        try:
            name, salary_str = emp_str.split('-')
            salary = int(salary_str)
            
            if not cls.is_valid_salary(salary):
                raise ValueError(f"Invalid salary: {salary}")
            
            return cls(name, salary)
        except ValueError as e:
            print(f"Error creating employee from string '{emp_str}': {e}")
            return None

    def __str__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

# Test our class:
print("Testing regular constructor:")
emp1 = Employee("Alice", 75000)
print(emp1)

print("\nTesting class method from_string:")
emp2 = Employee.from_string("Bob-60000")
print(emp2)

emp3 = Employee.from_string("Charlie-85000")
print(emp3)

print("\nTesting static method is_valid_salary:")
print(f"Is 50000 a valid salary? {Employee.is_valid_salary(50000)}")
print(f"Is -1000 a valid salary? {Employee.is_valid_salary(-1000)}")
print(f"Is 0 a valid salary? {Employee.is_valid_salary(0)}")
print(f"Is 75000.50 a valid salary? {Employee.is_valid_salary(75000.50)}")

print("\nTesting error handling:")
emp4 = Employee.from_string("David--5000")  # Invalid format
emp5 = Employee.from_string("Eve-invalid")  # Invalid salary

# What we accomplished in this step:
# - Created and tested our complete Employee implementation
# - Demonstrated class methods, static methods, and error handling


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Static methods (@staticmethod) - utility functions that belong to the class
# - Class methods (@classmethod) - alternative constructors that take cls parameter
# - String parsing and data conversion
# - Method interaction (class method using static method)
# - Error handling in class methods
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding more validation or parsing formats!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================