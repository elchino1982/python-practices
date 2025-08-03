"""Question: Create a class Command that uses the Command pattern to
encapsulate a request as an object. Implement commands for TurnOn and TurnOff.
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
# - What is the Command pattern and why is it useful?
# - How do you create a base class that defines an interface?
# - What method should all commands implement?
# - How do you create concrete command classes that inherit from the base?
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


# Step 1: Define the base Command class
# ===============================================================================

# Explanation:
# Let's start by creating our base Command class. This class defines the interface
# that all concrete commands must implement. It uses the Command pattern to
# encapsulate requests as objects.

class Command:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Command class structure


# Step 2: Add the execute method to the base class
# ===============================================================================

# Explanation:
# The execute method is the core of the Command pattern. All concrete commands
# must implement this method. We'll make it abstract by raising NotImplementedError.

class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Added abstract execute method that must be overridden
# - Provides clear error message for unimplemented methods


# Step 3: Create the TurnOn command
# ===============================================================================

# Explanation:
# Now let's create our first concrete command. The TurnOn command will inherit
# from Command and implement the execute method with specific behavior.

class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

class TurnOn(Command):
    def execute(self):
        return "Turning on"

# What we accomplished in this step:
# - Created TurnOn class that inherits from Command
# - Implemented execute method with specific "turn on" behavior


# Step 4: Create the TurnOff command
# ===============================================================================

# Explanation:
# Let's create our second concrete command. The TurnOff command will also inherit
# from Command but implement different behavior.

class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

class TurnOn(Command):
    def execute(self):
        return "Turning on"

class TurnOff(Command):
    def execute(self):
        return "Turning off"

# What we accomplished in this step:
# - Created TurnOff class that inherits from Command
# - Implemented execute method with specific "turn off" behavior


# Step 5: Test our Command pattern implementation
# ===============================================================================

# Explanation:
# Now let's test our Command pattern by creating instances of our commands
# and executing them. This demonstrates how commands can be treated uniformly.

class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

class TurnOn(Command):
    def execute(self):
        return "Turning on"

class TurnOff(Command):
    def execute(self):
        return "Turning off"

# Test our Command pattern:
print("=== Basic Command Pattern Test ===")
commands = [TurnOn(), TurnOff()]
for command in commands:
    result = command.execute()
    print(f"{command.__class__.__name__}: {result}")

# What we accomplished in this step:
# - Created instances of both command types
# - Executed commands in a loop, treating them uniformly
# - Demonstrated polymorphism with the Command pattern


# Step 6: Enhanced version with device context
# ===============================================================================

# Explanation:
# Let's create an enhanced version that includes a device to operate on.
# This makes the commands more realistic and demonstrates how commands
# can encapsulate both the action and the target.

class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

    def undo(self):
        raise NotImplementedError("Subclasses must implement this method")

class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.name} is now ON"
        return f"{self.name} is already ON"

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.name} is now OFF"
        return f"{self.name} is already OFF"

    def get_status(self):
        status = "ON" if self.is_on else "OFF"
        return f"{self.name} is {status}"

class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_on()

    def undo(self):
        return self.device.turn_off()

class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        return self.device.turn_off()

    def undo(self):
        return self.device.turn_on()

# Test enhanced version:
print("\n=== Enhanced Command Pattern with Device ===")

# Create devices
tv = Device("Smart TV")
lights = Device("Living Room Lights")

print("Initial status:")
print(tv.get_status())
print(lights.get_status())

# Create commands
tv_on = TurnOnCommand(tv)
tv_off = TurnOffCommand(tv)
lights_on = TurnOnCommand(lights)
lights_off = TurnOffCommand(lights)

# Execute commands
print("\nExecuting commands:")
print(tv_on.execute())
print(lights_on.execute())
print(tv.get_status())
print(lights.get_status())

print("\nExecuting more commands:")
print(tv_off.execute())
print(lights_off.execute())

print("\nTesting undo functionality:")
print(tv_off.undo())  # Should turn TV back on
print(lights_off.undo())  # Should turn lights back on

# What we accomplished in this step:
# - Created a Device class to represent controllable devices
# - Enhanced commands to work with specific devices
# - Added undo functionality to commands
# - Demonstrated more realistic command usage


# Step 7: Command invoker with history
# ===============================================================================

# Explanation:
# Let's create a command invoker that can execute commands and maintain
# a history for undo operations. This completes the Command pattern implementation.

class RemoteControl:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        result = command.execute()
        self.history.append(command)
        print(f"Executed: {result}")
        return result

    def undo_last_command(self):
        if self.history:
            last_command = self.history.pop()
            result = last_command.undo()
            print(f"Undid: {result}")
            return result
        else:
            print("No commands to undo")

    def get_history_size(self):
        return len(self.history)

# Test complete Command pattern with invoker:
print("\n=== Complete Command Pattern with Remote Control ===")

# Create devices and remote
stereo = Device("Stereo System")
fan = Device("Ceiling Fan")
remote = RemoteControl()

# Create commands
stereo_on = TurnOnCommand(stereo)
stereo_off = TurnOffCommand(stereo)
fan_on = TurnOnCommand(fan)
fan_off = TurnOffCommand(fan)

# Use remote to execute commands
print("Using remote control:")
remote.execute_command(stereo_on)
remote.execute_command(fan_on)
remote.execute_command(stereo_off)

print(f"\nHistory size: {remote.get_history_size()}")

print("\nUndoing commands:")
remote.undo_last_command()  # Undo stereo off (turn it back on)
remote.undo_last_command()  # Undo fan on (turn it back off)
remote.undo_last_command()  # Undo stereo on (turn it back off)
remote.undo_last_command()  # No more commands to undo

# What we accomplished in this step:
# - Created RemoteControl class as a command invoker
# - Added command history tracking
# - Implemented undo functionality with history
# - Demonstrated complete Command pattern usage


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Command pattern and its benefits
# - Creating abstract base classes with NotImplementedError
# - Implementing concrete command classes
# - Encapsulating requests as objects
# - Adding undo functionality to commands
# - Creating command invokers with history
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding macro commands that execute multiple commands!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
