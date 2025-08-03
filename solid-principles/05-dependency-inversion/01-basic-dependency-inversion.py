"""Question: Define a class Light with a method turn_on.
Create a class Switch that depends on Light.
Refactor the classes to adhere to
the Dependency Inversion Principle by introducing an interface Switchable.
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
# - What is the Dependency Inversion Principle (DIP)?
# - How does the original Switch class violate DIP?
# - What is the difference between depending on abstractions vs. concrete classes?
# - How can you create an interface that both Switch and Light can depend on?
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


# Step 1: Identify the DIP violation in the original design
# ===============================================================================

# Explanation:
# Let's examine the original Switch and Light classes that violate DIP by
# having Switch directly depend on the concrete Light class.

class Light:
    def turn_on(self):
        return "Light is on"

class Switch:
    def __init__(self, light):
        self.light = light  # Direct dependency on concrete Light class

    def operate(self):
        return self.light.turn_on()

# What we can observe:
# - Switch directly depends on Light (concrete class)
# - This violates DIP: high-level module (Switch) depends on low-level module (Light)
# - Switch is tightly coupled to Light
# - Hard to test Switch with different devices
# - Difficult to add new switchable devices

print("=== Original Design (DIP Violation) ===")
light = Light()
switch = Switch(light)
result = switch.operate()
print(f"Result: {result}")
print("DIP Violation: Switch directly depends on concrete Light class!")


# Step 2: Create an abstraction for switchable devices
# ===============================================================================

# Explanation:
# Let's create an abstract interface that defines the contract for switchable
# devices, following DIP by depending on abstractions.

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

# What we accomplished in this step:
# - Created Switchable abstraction that defines the interface
# - This abstraction will be the dependency for high-level modules
# - Concrete implementations will depend on this abstraction


# Step 3: Implement Light as a concrete switchable device
# ===============================================================================

# Explanation:
# Now let's implement Light as a concrete implementation of the
# Switchable abstraction.

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Switchable):
    def turn_on(self):
        return "Light is on"

# What we accomplished in this step:
# - Light now implements Switchable abstraction
# - Low-level module (Light) depends on abstraction (Switchable)
# - Follows DIP: concrete implementation depends on abstraction


# Step 4: Refactor Switch to depend on abstraction
# ===============================================================================

# Explanation:
# Let's refactor Switch to depend on the Switchable abstraction
# instead of the concrete Light implementation.

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Switchable):
    def turn_on(self):
        return "Light is on"

class Switch:
    def __init__(self, device: Switchable):
        self.device = device  # Depends on abstraction

    def operate(self):
        return self.device.turn_on()

# What we accomplished in this step:
# - Switch now depends on Switchable abstraction
# - Uses dependency injection to receive the switchable device
# - High-level module (Switch) depends on abstraction (Switchable)
# - Follows DIP: both modules depend on abstraction


# Step 5: Test our DIP-compliant design
# ===============================================================================

# Explanation:
# Let's test our refactored design to verify that it follows DIP
# and provides the same functionality with better flexibility.

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Switchable):
    def turn_on(self):
        return "Light is on"

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        return self.device.turn_on()

# Test our DIP-compliant design:
print("\n=== DIP-Compliant Design ===")

light = Light()
switch = Switch(light)
result = switch.operate()
print(f"Result: {result}")
print("DIP Success: Switch depends on Switchable abstraction!")

# What we accomplished in this step:
# - Verified that our refactored design works correctly
# - Switch now depends on abstraction instead of concrete implementation
# - System is more flexible and follows DIP


# Step 6: Demonstrate DIP benefits by adding new switchable devices
# ===============================================================================

# Explanation:
# Let's prove that our DIP-compliant design is flexible by adding new
# switchable devices without modifying existing code.

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Switchable):
    def turn_on(self):
        return "Light is on"

# Adding new switchable devices without modifying existing code (DIP benefit!)
class Fan(Switchable):
    def turn_on(self):
        return "Fan is spinning"

class Radio(Switchable):
    def turn_on(self):
        return "Radio is playing music"

class AirConditioner(Switchable):
    def turn_on(self):
        return "Air conditioner is cooling"

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        return self.device.turn_on()

print("\n=== Demonstrating DIP Benefits (Multiple Devices) ===")

# Test with different switchable devices
devices = [
    Light(),
    Fan(),
    Radio(),
    AirConditioner()
]

for device in devices:
    switch = Switch(device)
    result = switch.operate()
    device_name = device.__class__.__name__
    print(f"{device_name}: {result}")

print("\nDIP Benefits: Easy to add new devices without modifying Switch!")

# What we accomplished in this step:
# - Added multiple switchable devices without modifying Switch
# - Demonstrated flexibility and extensibility of DIP-compliant design
# - Showed how abstraction enables easy device switching


# Step 7: Enhanced example with smart home automation system
# ===============================================================================

# Explanation:
# Let's create a more comprehensive example that shows advanced DIP
# applications with a smart home automation system.

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass

class Dimmable(ABC):
    @abstractmethod
    def set_brightness(self, level):
        pass

class Controllable(ABC):
    @abstractmethod
    def set_setting(self, setting, value):
        pass

# Enhanced device implementations
class SmartLight(Switchable, Dimmable):
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True
        self.brightness = 100
        return f"Smart light in {self.location} is on at {self.brightness}% brightness"

    def turn_off(self):
        self.is_on = False
        self.brightness = 0
        return f"Smart light in {self.location} is off"

    def get_status(self):
        status = "on" if self.is_on else "off"
        return f"Smart light in {self.location}: {status}, brightness: {self.brightness}%"

    def set_brightness(self, level):
        if self.is_on:
            self.brightness = max(0, min(100, level))
            return f"Smart light brightness set to {self.brightness}%"
        return "Cannot set brightness - light is off"

class SmartFan(Switchable, Controllable):
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.speed = 0

    def turn_on(self):
        self.is_on = True
        self.speed = 1
        return f"Smart fan in {self.location} is on at speed {self.speed}"

    def turn_off(self):
        self.is_on = False
        self.speed = 0
        return f"Smart fan in {self.location} is off"

    def get_status(self):
        status = "on" if self.is_on else "off"
        return f"Smart fan in {self.location}: {status}, speed: {self.speed}"

    def set_setting(self, setting, value):
        if setting == "speed" and self.is_on:
            self.speed = max(0, min(5, value))
            return f"Fan speed set to {self.speed}"
        return f"Cannot set {setting} - fan is off or invalid setting"

class SmartThermostat(Switchable, Controllable):
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.temperature = 72

    def turn_on(self):
        self.is_on = True
        return f"Thermostat in {self.location} is on, set to {self.temperature}°F"

    def turn_off(self):
        self.is_on = False
        return f"Thermostat in {self.location} is off"

    def get_status(self):
        status = "on" if self.is_on else "off"
        return f"Thermostat in {self.location}: {status}, temperature: {self.temperature}°F"

    def set_setting(self, setting, value):
        if setting == "temperature":
            self.temperature = max(50, min(90, value))
            return f"Temperature set to {self.temperature}°F"
        return f"Invalid setting: {setting}"

# Smart home controllers that depend on abstractions
class SmartSwitch:
    def __init__(self, device: Switchable):
        self.device = device

    def turn_on(self):
        return self.device.turn_on()

    def turn_off(self):
        return self.device.turn_off()

    def get_device_status(self):
        return self.device.get_status()

class DimmerSwitch:
    def __init__(self, device: Dimmable):
        if not isinstance(device, Dimmable):
            raise TypeError("Device must be dimmable")
        self.device = device

    def set_brightness(self, level):
        return self.device.set_brightness(level)

class SmartController:
    def __init__(self, device: Controllable):
        if not isinstance(device, Controllable):
            raise TypeError("Device must be controllable")
        self.device = device

    def adjust_setting(self, setting, value):
        return self.device.set_setting(setting, value)

class HomeAutomationSystem:
    def __init__(self):
        self.devices = []
        self.switches = []

    def add_device(self, device: Switchable):
        self.devices.append(device)
        switch = SmartSwitch(device)
        self.switches.append(switch)

    def turn_all_on(self):
        results = []
        for switch in self.switches:
            result = switch.turn_on()
            results.append(result)
        return results

    def turn_all_off(self):
        results = []
        for switch in self.switches:
            result = switch.turn_off()
            results.append(result)
        return results

    def get_system_status(self):
        status = []
        for switch in self.switches:
            device_status = switch.get_device_status()
            status.append(device_status)
        return status

    def control_dimmable_devices(self, brightness_level):
        results = []
        for device in self.devices:
            if isinstance(device, Dimmable):
                dimmer = DimmerSwitch(device)
                result = dimmer.set_brightness(brightness_level)
                results.append(f"{device.__class__.__name__}: {result}")
        return results

    def control_adjustable_devices(self, setting, value):
        results = []
        for device in self.devices:
            if isinstance(device, Controllable):
                controller = SmartController(device)
                result = controller.adjust_setting(setting, value)
                results.append(f"{device.__class__.__name__}: {result}")
        return results

# Test enhanced DIP design:
print("\n=== Enhanced DIP Design with Smart Home System ===")

# Create smart home system
home = HomeAutomationSystem()

# Add various smart devices
devices = [
    SmartLight("Living Room"),
    SmartLight("Bedroom"),
    SmartFan("Living Room"),
    SmartThermostat("Main Floor")
]

for device in devices:
    home.add_device(device)

print("Initial system status:")
for status in home.get_system_status():
    print(f"  {status}")

print("\nTurning all devices on:")
for result in home.turn_all_on():
    print(f"  {result}")

print("\nAdjusting dimmable devices to 75% brightness:")
for result in home.control_dimmable_devices(75):
    print(f"  {result}")

print("\nSetting fan speed to 3:")
for result in home.control_adjustable_devices("speed", 3):
    print(f"  {result}")

print("\nSetting temperature to 68°F:")
for result in home.control_adjustable_devices("temperature", 68):
    print(f"  {result}")

print("\nFinal system status:")
for status in home.get_system_status():
    print(f"  {status}")

# What we accomplished in this step:
# - Created comprehensive smart home system using DIP
# - Demonstrated multiple abstractions (Switchable, Dimmable, Controllable)
# - Showed how DIP enables flexible device management
# - Illustrated real-world application of dependency injection


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the Dependency Inversion Principle solution!
#
# Key concepts learned:
# - Understanding the Dependency Inversion Principle (DIP)
# - Identifying tight coupling between high-level and low-level modules
# - Creating abstractions that both modules can depend on
# - Using dependency injection to provide implementations
# - Benefits of DIP: flexibility, testability, and maintainability
# - How DIP enables easy switching between implementations
#
# DIP Benefits demonstrated:
# - High-level modules don't depend on low-level modules (both depend on abstractions)
# - Easy to add new implementations without modifying existing code
# - Improved testability through dependency injection
# - Flexible device management in smart home systems
# - Loose coupling between components
# - Better separation of concerns
#
# Real-world applications:
# - Smart home automation systems with various device types
# - IoT device management platforms
# - Plugin architectures with interchangeable components
# - Database access layers with different database providers
# - Payment processing systems with multiple payment gateways
# - Notification systems with various delivery channels
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY depending on abstractions is better than concrete classes
# 4. Experiment with adding new devices (SmartTV, SmartSpeaker, etc.)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
