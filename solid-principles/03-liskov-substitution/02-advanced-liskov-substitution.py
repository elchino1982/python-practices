"""Question: Create a class Vehicle with a method start_engine.
Implement subclasses Car and Bicycle.
Ensure that substituting a Bicycle for a Vehicle does not violate
the Liskov Substitution Principle.
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
# - What is the Liskov Substitution Principle (LSP)?
# - How does the original Vehicle hierarchy violate LSP?
# - What happens when you substitute a Bicycle for a Vehicle?
# - How can you redesign the hierarchy to follow LSP?
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


# Step 1: Identify the LSP violation in the original design
# ===============================================================================

# Explanation:
# Let's examine the original Vehicle hierarchy that violates LSP by having
# a Bicycle that cannot start an engine, breaking the expected behavior of Vehicle.

class Vehicle:
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Bicycle(Vehicle):
    def start_engine(self):
        raise Exception("Bicycles do not have engines")

# What we can observe:
# - The Vehicle class defines a start_engine() method that all vehicles should implement
# - Car implements start_engine() correctly
# - Bicycle violates LSP by throwing an exception instead of starting an engine
# - Code that expects any Vehicle to start an engine will break with Bicycle

print("=== Original Design (LSP Violation) ===")
vehicles = [Car(), Bicycle()]

print("Testing vehicle engine starting:")
for i, vehicle in enumerate(vehicles, 1):
    vehicle_type = vehicle.__class__.__name__
    try:
        result = vehicle.start_engine()
        print(f"Vehicle {i} ({vehicle_type}): {result}")
    except Exception as e:
        print(f"Vehicle {i} ({vehicle_type}): ERROR - {e}")

print("LSP Violation: Bicycle cannot be substituted for Vehicle without breaking functionality!")


# Step 2: Redesign with proper abstraction
# ===============================================================================

# Explanation:
# Let's redesign the hierarchy to follow LSP by creating more specific
# abstractions that don't force all vehicles to have engines.

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_type(self):
        raise NotImplementedError("Subclasses must implement this method")

class MotorizedVehicle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")

class NonMotorizedVehicle(Vehicle):
    def pedal(self):
        raise NotImplementedError("Non-motorized vehicles must implement this method")

# What we accomplished in this step:
# - Created Vehicle base class with common behaviors (move, get_type)
# - Separated motorized and non-motorized vehicles into different hierarchies
# - Each hierarchy only defines methods that make sense for that type


# Step 3: Implement Car as a MotorizedVehicle
# ===============================================================================

# Explanation:
# Now let's implement Car as a MotorizedVehicle, which naturally supports
# engine operations.

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_type(self):
        raise NotImplementedError("Subclasses must implement this method")

class MotorizedVehicle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")

class NonMotorizedVehicle(Vehicle):
    def pedal(self):
        raise NotImplementedError("Non-motorized vehicles must implement this method")

class Car(MotorizedVehicle):
    def __init__(self):
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return "Car engine started"
        return "Car engine is already running"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return "Car engine stopped"
        return "Car engine is already stopped"

    def move(self):
        if self.engine_running:
            return "Car is driving on the road"
        return "Car cannot move - engine is not running"

    def get_type(self):
        return "Motorized Vehicle"

# What we accomplished in this step:
# - Implemented Car as a MotorizedVehicle
# - Car naturally supports engine operations
# - Follows LSP: Car can be substituted for MotorizedVehicle or Vehicle


# Step 4: Implement Bicycle as a NonMotorizedVehicle
# ===============================================================================

# Explanation:
# Let's implement Bicycle as a NonMotorizedVehicle, which naturally supports
# pedaling instead of engine operations.

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_type(self):
        raise NotImplementedError("Subclasses must implement this method")

class MotorizedVehicle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")

class NonMotorizedVehicle(Vehicle):
    def pedal(self):
        raise NotImplementedError("Non-motorized vehicles must implement this method")

class Car(MotorizedVehicle):
    def __init__(self):
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return "Car engine started"
        return "Car engine is already running"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return "Car engine stopped"
        return "Car engine is already stopped"

    def move(self):
        if self.engine_running:
            return "Car is driving on the road"
        return "Car cannot move - engine is not running"

    def get_type(self):
        return "Motorized Vehicle"

class Bicycle(NonMotorizedVehicle):
    def __init__(self):
        self.is_pedaling = False

    def pedal(self):
        self.is_pedaling = True
        return "Bicycle is being pedaled"

    def stop_pedaling(self):
        self.is_pedaling = False
        return "Bicycle stopped pedaling"

    def move(self):
        if self.is_pedaling:
            return "Bicycle is moving by pedaling"
        return "Bicycle is stationary"

    def get_type(self):
        return "Non-Motorized Vehicle"

# What we accomplished in this step:
# - Implemented Bicycle as a NonMotorizedVehicle
# - Bicycle naturally supports pedaling behavior
# - Follows LSP: Bicycle can be substituted for NonMotorizedVehicle or Vehicle


# Step 5: Test our LSP-compliant design
# ===============================================================================

# Explanation:
# Let's test our redesigned hierarchy to verify that it follows LSP
# and all substitutions work correctly.

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_type(self):
        raise NotImplementedError("Subclasses must implement this method")

class MotorizedVehicle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")

class NonMotorizedVehicle(Vehicle):
    def pedal(self):
        raise NotImplementedError("Non-motorized vehicles must implement this method")

class Car(MotorizedVehicle):
    def __init__(self):
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return "Car engine started"
        return "Car engine is already running"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return "Car engine stopped"
        return "Car engine is already stopped"

    def move(self):
        if self.engine_running:
            return "Car is driving on the road"
        return "Car cannot move - engine is not running"

    def get_type(self):
        return "Motorized Vehicle"

class Bicycle(NonMotorizedVehicle):
    def __init__(self):
        self.is_pedaling = False

    def pedal(self):
        self.is_pedaling = True
        return "Bicycle is being pedaled"

    def stop_pedaling(self):
        self.is_pedaling = False
        return "Bicycle stopped pedaling"

    def move(self):
        if self.is_pedaling:
            return "Bicycle is moving by pedaling"
        return "Bicycle is stationary"

    def get_type(self):
        return "Non-Motorized Vehicle"

# Test our LSP-compliant design:
print("\n=== LSP-Compliant Design ===")

# Test with all vehicles using common Vehicle interface
all_vehicles = [Car(), Bicycle()]

print("Testing common Vehicle behaviors:")
for i, vehicle in enumerate(all_vehicles, 1):
    vehicle_type = vehicle.__class__.__name__
    print(f"Vehicle {i} ({vehicle_type}):")
    print(f"  Type: {vehicle.get_type()}")
    print(f"  Initial movement: {vehicle.move()}")

# Test motorized vehicles specifically
motorized_vehicles = [Car()]
print("\nTesting MotorizedVehicle behaviors:")
for vehicle in motorized_vehicles:
    vehicle_type = vehicle.__class__.__name__
    print(f"{vehicle_type}:")
    print(f"  {vehicle.start_engine()}")
    print(f"  Movement: {vehicle.move()}")
    print(f"  {vehicle.stop_engine()}")

# Test non-motorized vehicles specifically
non_motorized_vehicles = [Bicycle()]
print("\nTesting NonMotorizedVehicle behaviors:")
for vehicle in non_motorized_vehicles:
    vehicle_type = vehicle.__class__.__name__
    print(f"{vehicle_type}:")
    print(f"  {vehicle.pedal()}")
    print(f"  Movement: {vehicle.move()}")
    print(f"  {vehicle.stop_pedaling()}")

print("\nLSP Success: All substitutions work correctly without breaking functionality!")

# What we accomplished in this step:
# - Verified that all vehicles can be used through the Vehicle interface
# - Demonstrated that specific vehicle types work with their appropriate interfaces
# - Confirmed that no exceptions are thrown during substitution


# Step 6: Enhanced example with more vehicle types
# ===============================================================================

# Explanation:
# Let's add more vehicle types to demonstrate how our LSP-compliant design
# scales and accommodates different vehicle behaviors.

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_type(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_info(self):
        return f"{self.__class__.__name__}: {self.get_type()}, {self.move()}"

class MotorizedVehicle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Motorized vehicles must implement this method")

class NonMotorizedVehicle(Vehicle):
    def pedal(self):
        raise NotImplementedError("Non-motorized vehicles must implement this method")

class ElectricVehicle(Vehicle):
    def start_motor(self):
        raise NotImplementedError("Electric vehicles must implement this method")
    
    def stop_motor(self):
        raise NotImplementedError("Electric vehicles must implement this method")

# Motorized vehicles
class Car(MotorizedVehicle):
    def __init__(self):
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return "Car engine started"
        return "Car engine is already running"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return "Car engine stopped"
        return "Car engine is already stopped"

    def move(self):
        if self.engine_running:
            return "driving on roads"
        return "stationary (engine off)"

    def get_type(self):
        return "Motorized Vehicle"

class Motorcycle(MotorizedVehicle):
    def __init__(self):
        self.engine_running = False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return "Motorcycle engine started"
        return "Motorcycle engine is already running"

    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return "Motorcycle engine stopped"
        return "Motorcycle engine is already stopped"

    def move(self):
        if self.engine_running:
            return "riding on roads"
        return "stationary (engine off)"

    def get_type(self):
        return "Motorized Vehicle"

# Non-motorized vehicles
class Bicycle(NonMotorizedVehicle):
    def __init__(self):
        self.is_pedaling = False

    def pedal(self):
        self.is_pedaling = True
        return "Bicycle is being pedaled"

    def stop_pedaling(self):
        self.is_pedaling = False
        return "Bicycle stopped pedaling"

    def move(self):
        if self.is_pedaling:
            return "moving by pedaling"
        return "stationary"

    def get_type(self):
        return "Non-Motorized Vehicle"

class Skateboard(NonMotorizedVehicle):
    def __init__(self):
        self.is_pedaling = False

    def pedal(self):
        # For skateboard, "pedaling" means pushing with foot
        self.is_pedaling = True
        return "Skateboard is being pushed"

    def stop_pedaling(self):
        self.is_pedaling = False
        return "Skateboard stopped being pushed"

    def move(self):
        if self.is_pedaling:
            return "rolling by foot pushing"
        return "stationary"

    def get_type(self):
        return "Non-Motorized Vehicle"

# Electric vehicles
class ElectricCar(ElectricVehicle):
    def __init__(self):
        self.motor_running = False

    def start_motor(self):
        if not self.motor_running:
            self.motor_running = True
            return "Electric car motor started"
        return "Electric car motor is already running"

    def stop_motor(self):
        if self.motor_running:
            self.motor_running = False
            return "Electric car motor stopped"
        return "Electric car motor is already stopped"

    def move(self):
        if self.motor_running:
            return "driving silently on roads"
        return "stationary (motor off)"

    def get_type(self):
        return "Electric Vehicle"

# Vehicle management system that works with any vehicle type
class VehicleFleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_fleet_status(self):
        status = {}
        for vehicle in self.vehicles:
            vehicle_type = vehicle.get_type()
            if vehicle_type not in status:
                status[vehicle_type] = []
            status[vehicle_type].append(vehicle)
        return status

    def move_all_vehicles(self):
        """Demonstrate LSP: all vehicles can move regardless of type"""
        results = []
        for vehicle in self.vehicles:
            vehicle_name = vehicle.__class__.__name__
            movement = vehicle.move()
            results.append(f"{vehicle_name}: {movement}")
        return results

    def generate_fleet_report(self):
        if not self.vehicles:
            return "No vehicles in fleet."
        
        report = "Vehicle Fleet Report\n"
        report += "=" * 40 + "\n"
        
        status = self.get_fleet_status()
        for vehicle_type, vehicles in status.items():
            report += f"\n{vehicle_type}s ({len(vehicles)}):\n"
            report += "-" * (len(vehicle_type) + 10) + "\n"
            for vehicle in vehicles:
                report += f"• {vehicle.__class__.__name__}: {vehicle.move()}\n"
        
        report += f"\nTotal vehicles: {len(self.vehicles)}\n"
        return report

# Test enhanced LSP design:
print("\n=== Enhanced LSP Design with Multiple Vehicle Types ===")

fleet = VehicleFleet()

# Create various vehicles
vehicles = [
    Car(), Motorcycle(),           # Motorized vehicles
    Bicycle(), Skateboard(),       # Non-motorized vehicles
    ElectricCar()                  # Electric vehicles
]

# Add vehicles to fleet
for vehicle in vehicles:
    fleet.add_vehicle(vehicle)

print("Fleet composition:")
status = fleet.get_fleet_status()
for vehicle_type, vehicles in status.items():
    print(f"  {vehicle_type}s: {len(vehicles)}")

print("\n" + fleet.generate_fleet_report())

# Demonstrate LSP compliance with different collections
print("=== Demonstrating LSP Compliance ===")

# All vehicles can be treated as Vehicle objects
print("\nAll vehicles using Vehicle interface:")
for vehicle in vehicles:
    print(f"  {vehicle.__class__.__name__}: {vehicle.move()}")

# Motorized vehicles can be treated as MotorizedVehicle objects
motorized_vehicles = [v for v in vehicles if isinstance(v, MotorizedVehicle)]
print(f"\nMotorized vehicles using MotorizedVehicle interface ({len(motorized_vehicles)} vehicles):")
for vehicle in motorized_vehicles:
    print(f"  {vehicle.__class__.__name__}: {vehicle.start_engine()}")

# Non-motorized vehicles can be treated as NonMotorizedVehicle objects
non_motorized_vehicles = [v for v in vehicles if isinstance(v, NonMotorizedVehicle)]
print(f"\nNon-motorized vehicles using NonMotorizedVehicle interface ({len(non_motorized_vehicles)} vehicles):")
for vehicle in non_motorized_vehicles:
    print(f"  {vehicle.__class__.__name__}: {vehicle.pedal()}")

# What we accomplished in this step:
# - Added multiple vehicle types that all follow LSP
# - Created a fleet management system that works with any vehicle type
# - Demonstrated that the hierarchy scales well with new types
# - Showed how different interfaces can be used appropriately


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the advanced Liskov Substitution Principle solution!
#
# Key concepts learned:
# - Understanding LSP violations in vehicle hierarchies
# - Identifying inappropriate inheritance relationships
# - Redesigning hierarchies to follow LSP with proper abstractions
# - Creating appropriate interfaces that don't force invalid behaviors
# - Benefits of LSP-compliant design for system extensibility
# - How LSP enables robust polymorphic fleet management systems
#
# Advanced LSP Benefits demonstrated:
# - Subclasses can be substituted for their base classes without breaking code
# - No unexpected exceptions or behaviors when using polymorphism
# - Code that works with base classes automatically works with all subclasses
# - System can handle diverse vehicle types through common interfaces
# - Easy to add new vehicle types without breaking existing functionality
# - Fleet management systems work reliably with any vehicle type
#
# Real-world applications:
# - Transportation management systems with diverse vehicle fleets
# - Game systems with different character types and abilities
# - Device driver hierarchies with consistent operation interfaces
# - Payment processing systems with various payment method types
# - File system abstractions supporting different file types
# - Network protocol implementations with uniform interfaces
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY the original design violates LSP
# 4. Experiment with adding new vehicle types (Boat, Airplane, etc.)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
