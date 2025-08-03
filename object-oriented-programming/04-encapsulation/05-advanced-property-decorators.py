"""Question: Define a class Employee with a private attribute _salary.
Use a property to get and set the salary with validation.
Add a class method from_dict to create an instance from a dictionary and
a static method is_valid_employee_data to validate the dictionary data.
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
# - How do you combine properties with class/static methods?
# - What should the dictionary structure look like? ({'name': ..., 'salary': ...})
# - How do you validate dictionary data? (check keys exist and types are correct)
# - When should you use static vs class methods?
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


# Step 1: Define the Employee class with private attribute
# ===============================================================================

# Explanation:
# Let's start by creating our Employee class with a private _salary attribute.
# We'll also include a name attribute for completeness.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

# What we accomplished in this step:
# - Created Employee class with name and private _salary attributes


# Step 2: Add property getter for salary
# ===============================================================================

# Explanation:
# Properties allow us to access private attributes through methods that look like attributes.
# The @property decorator creates a getter method.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

# What we accomplished in this step:
# - Added property getter for salary attribute


# Step 3: Add property setter for salary with validation
# ===============================================================================

# Explanation:
# The @salary.setter decorator creates a setter method that includes validation.
# We'll check that the salary is a positive number.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Salary must be a positive number")
        self._salary = value

# What we accomplished in this step:
# - Added property setter for salary with validation


# Step 4: Add static method for data validation
# ===============================================================================

# Explanation:
# Static methods don't need access to the class or instance. This method
# validates dictionary data independently of any specific instance.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Salary must be a positive number")
        self._salary = value

    @staticmethod
    def is_valid_employee_data(data):
        if not isinstance(data, dict):
            return False
        
        required_keys = ['name', 'salary']
        if not all(key in data for key in required_keys):
            return False
        
        if not isinstance(data['name'], str) or not data['name'].strip():
            return False
        
        if not isinstance(data['salary'], (int, float)) or data['salary'] <= 0:
            return False
        
        return True

# What we accomplished in this step:
# - Added static method to validate dictionary data
# - Comprehensive validation for all required fields


# Step 5: Add class method to create instance from dictionary
# ===============================================================================

# Explanation:
# Class methods take 'cls' as the first parameter and can create new instances.
# This method uses our static validation method before creating an instance.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Salary must be a positive number")
        self._salary = value

    @staticmethod
    def is_valid_employee_data(data):
        if not isinstance(data, dict):
            return False
        
        required_keys = ['name', 'salary']
        if not all(key in data for key in required_keys):
            return False
        
        if not isinstance(data['name'], str) or not data['name'].strip():
            return False
        
        if not isinstance(data['salary'], (int, float)) or data['salary'] <= 0:
            return False
        
        return True

    @classmethod
    def from_dict(cls, data):
        if not cls.is_valid_employee_data(data):
            raise ValueError("Invalid employee data")
        return cls(data['name'], data['salary'])

# What we accomplished in this step:
# - Added class method to create Employee from dictionary
# - Used static method for validation before creation


# Step 6: Add string representation and additional methods
# ===============================================================================

# Explanation:
# Let's add a __str__ method and some additional useful methods to make our Employee class more complete.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Salary must be a positive number")
        self._salary = value

    @staticmethod
    def is_valid_employee_data(data):
        if not isinstance(data, dict):
            return False
        
        required_keys = ['name', 'salary']
        if not all(key in data for key in required_keys):
            return False
        
        if not isinstance(data['name'], str) or not data['name'].strip():
            return False
        
        if not isinstance(data['salary'], (int, float)) or data['salary'] <= 0:
            return False
        
        return True

    @classmethod
    def from_dict(cls, data):
        if not cls.is_valid_employee_data(data):
            raise ValueError("Invalid employee data")
        return cls(data['name'], data['salary'])

    def to_dict(self):
        return {'name': self.name, 'salary': self._salary}

    def __str__(self):
        return f"Employee(name='{self.name}', salary=${self._salary})"

# What we accomplished in this step:
# - Added to_dict method for serialization
# - Added __str__ method for readable representation


# Step 7: Create instances and test all functionality
# ===============================================================================

# Explanation:
# Finally, let's create instances using different methods and test all the functionality
# to make sure everything works correctly.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Salary must be a positive number")
        self._salary = value

    @staticmethod
    def is_valid_employee_data(data):
        if not isinstance(data, dict):
            return False
        
        required_keys = ['name', 'salary']
        if not all(key in data for key in required_keys):
            return False
        
        if not isinstance(data['name'], str) or not data['name'].strip():
            return False
        
        if not isinstance(data['salary'], (int, float)) or data['salary'] <= 0:
            return False
        
        return True

    @classmethod
    def from_dict(cls, data):
        if not cls.is_valid_employee_data(data):
            raise ValueError("Invalid employee data")
        return cls(data['name'], data['salary'])

    def to_dict(self):
        return {'name': self.name, 'salary': self._salary}

    def __str__(self):
        return f"Employee(name='{self.name}', salary=${self._salary})"

# Test our class:
print("Testing regular constructor:")
emp1 = Employee("Alice", 75000)
print(emp1)

print("\nTesting property access:")
print(f"Name: {emp1.name}")
print(f"Salary: ${emp1.salary}")

print("\nTesting property setter:")
emp1.salary = 80000
print(f"Updated salary: ${emp1.salary}")

print("\nTesting static method validation:")
valid_data = {'name': 'Bob', 'salary': 60000}
invalid_data1 = {'name': 'Charlie'}  # Missing salary
invalid_data2 = {'name': 'David', 'salary': -1000}  # Invalid salary

print(f"Valid data: {Employee.is_valid_employee_data(valid_data)}")
print(f"Invalid data 1: {Employee.is_valid_employee_data(invalid_data1)}")
print(f"Invalid data 2: {Employee.is_valid_employee_data(invalid_data2)}")

print("\nTesting class method from_dict:")
emp2 = Employee.from_dict(valid_data)
print(emp2)

print("\nTesting to_dict method:")
print(f"Employee as dict: {emp2.to_dict()}")

print("\nTesting error handling:")
try:
    emp3 = Employee.from_dict(invalid_data1)
except ValueError as e:
    print(f"Error creating from invalid data: {e}")

try:
    emp1.salary = -5000
except ValueError as e:
    print(f"Error setting invalid salary: {e}")

# What we accomplished in this step:
# - Created and tested our complete Employee implementation
# - Demonstrated properties, class methods, static methods, and validation


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Combining properties with class and static methods
# - Dictionary-based object creation and validation
# - Comprehensive data validation strategies
# - Method interaction (class method using static method)
# - Serialization and deserialization (to_dict/from_dict)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding department or hire_date fields!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================