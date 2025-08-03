"""Question: Define a class named Vehicle with attributes make, model, and year.
Create a subclass named ElectricVehicle that adds an attribute battery_capacity
 and a method charge.
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
# - What attributes does the Vehicle class need?
# - How do you create a subclass that inherits from Vehicle?
# - What additional attribute does ElectricVehicle need?
# - What should the charge method do?
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


# Step 1: Define the Vehicle class
# ===============================================================================

# Explanation:
# Let's start by creating our Vehicle class. This will be our base class that
# contains the common attributes for all vehicles.

class Vehicle:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Vehicle class structure


# Step 2: Add the constructor to Vehicle class
# ===============================================================================

# Explanation:
# The __init__ method initializes the Vehicle with make, model, and year attributes.
# These are the basic pieces of information that all vehicles share.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# What we accomplished in this step:
# - Added constructor to initialize make, model, and year attributes


# Step 3: Define the ElectricVehicle subclass
# ===============================================================================

# Explanation:
# Now let's create the ElectricVehicle class that inherits from Vehicle. In Python,
# we specify inheritance by putting the parent class name in parentheses.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created ElectricVehicle class that inherits from Vehicle


# Step 4: Add constructor to ElectricVehicle class
# ===============================================================================

# Explanation:
# The ElectricVehicle constructor needs to accept make, model, year, and battery_capacity.
# We use super().__init__() to call the parent class constructor for the common attributes.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)  # Call parent constructor
        self.battery_capacity = battery_capacity  # Add new attribute

# What we accomplished in this step:
# - Added ElectricVehicle constructor that uses super() to inherit Vehicle attributes
# - Added battery_capacity attribute specific to ElectricVehicle


# Step 5: Add the charge method
# ===============================================================================

# Explanation:
# Now let's add the charge method that is specific to electric vehicles. This method
# will print information about the charging process.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging {self.make} {self.model} with {self.battery_capacity} kWh battery")

# What we accomplished in this step:
# - Added charge method specific to ElectricVehicle class


# Step 6: Create instances and test our classes
# ===============================================================================

# Explanation:
# Finally, let's create instances of our classes and test them to make sure everything works correctly.
# This demonstrates inheritance and how subclasses can add specialized functionality.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging {self.make} {self.model} with {self.battery_capacity} kWh battery")

# Test our classes:
# Create a regular vehicle
regular_car = Vehicle("Toyota", "Camry", 2025)
print(f"Regular vehicle: {regular_car.year} {regular_car.make} {regular_car.model}")

# Create an electric vehicle
ev = ElectricVehicle("Tesla", "Model S", 2025, 100)
print(f"Electric vehicle: {ev.year} {ev.make} {ev.model}")
print(f"Battery capacity: {ev.battery_capacity} kWh")

# Test the charge method
ev.charge()

# What we accomplished in this step:
# - Created and tested our complete Vehicle and ElectricVehicle implementation
# - Demonstrated inheritance and specialized functionality


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Class inheritance and the super() function
# - Adding specialized attributes in subclasses
# - Adding specialized methods in subclasses
# - How electric vehicles extend regular vehicle functionality
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding HybridVehicle or Motorcycle classes!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================