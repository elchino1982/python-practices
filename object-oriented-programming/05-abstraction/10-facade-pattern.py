"""Question: Implement the Facade pattern to provide a simplified interface to a complex subsystem.

Create a home automation facade that simplifies controlling multiple smart home
devices and systems.

Requirements:
1. Create complex subsystem classes for different home systems
2. Create a facade that provides simple methods to control everything
3. Demonstrate how the facade hides complexity from clients
4. Show both direct subsystem access and facade usage

Example usage:
    home = SmartHomeFacade()
    home.leave_home()  # Turns off lights, locks doors, sets security, etc.
    home.arrive_home()  # Unlocks door, turns on lights, adjusts temperature
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
# - What complex subsystems do you need?
# - How does the facade simplify interactions?
# - What high-level operations should the facade provide?
# - How does the facade coordinate multiple subsystems?
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


# Step 1: Create the lighting subsystem
# ===============================================================================

# Explanation:
# We start with complex subsystems that have many detailed operations.
# The lighting system manages multiple rooms and brightness levels.

class LightingSystem:
    """Complex lighting control system."""
    
    def __init__(self):
        self.lights = {
            'living_room': False,
            'bedroom': False,
            'kitchen': False,
            'bathroom': False,
            'outdoor': False
        }
        self.brightness = {room: 50 for room in self.lights}
    
    def turn_on_light(self, room: str, brightness: int = 100):
        """Turn on light in specific room."""
        if room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
            return f"Light in {room} turned on at {brightness}% brightness"
        return f"Room {room} not found"
    
    def turn_off_light(self, room: str):
        """Turn off light in specific room."""
        if room in self.lights:
            self.lights[room] = False
            return f"Light in {room} turned off"
        return f"Room {room} not found"
    
    def turn_on_all_lights(self, brightness: int = 100):
        """Turn on all lights."""
        for room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
        return f"All lights turned on at {brightness}% brightness"
    
    def turn_off_all_lights(self):
        """Turn off all lights."""
        for room in self.lights:
            self.lights[room] = False
        return "All lights turned off"
    
    def dim_lights(self, brightness: int):
        """Dim all lights to specified brightness."""
        for room in self.lights:
            if self.lights[room]:
                self.brightness[room] = brightness
        return f"All lights dimmed to {brightness}%"

# What we accomplished in this step:
# - Created complex lighting subsystem with many operations
# - Demonstrated detailed control over individual rooms and brightness


# Step 2: Add the security subsystem
# ===============================================================================

# Explanation:
# Security systems are complex with multiple sensors and states.
# We build upon the lighting system from Step 1.

class LightingSystem:
    """Complex lighting control system."""
    
    def __init__(self):
        self.lights = {
            'living_room': False,
            'bedroom': False,
            'kitchen': False,
            'bathroom': False,
            'outdoor': False
        }
        self.brightness = {room: 50 for room in self.lights}
    
    def turn_on_light(self, room: str, brightness: int = 100):
        """Turn on light in specific room."""
        if room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
            return f"Light in {room} turned on at {brightness}% brightness"
        return f"Room {room} not found"
    
    def turn_off_light(self, room: str):
        """Turn off light in specific room."""
        if room in self.lights:
            self.lights[room] = False
            return f"Light in {room} turned off"
        return f"Room {room} not found"
    
    def turn_on_all_lights(self, brightness: int = 100):
        """Turn on all lights."""
        for room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
        return f"All lights turned on at {brightness}% brightness"
    
    def turn_off_all_lights(self):
        """Turn off all lights."""
        for room in self.lights:
            self.lights[room] = False
        return "All lights turned off"
    
    def dim_lights(self, brightness: int):
        """Dim all lights to specified brightness."""
        for room in self.lights:
            if self.lights[room]:
                self.brightness[room] = brightness
        return f"All lights dimmed to {brightness}%"

class SecuritySystem:
    """Complex security system."""
    
    def __init__(self):
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
    
    def arm_system(self, mode: str = "away"):
        """Arm the security system."""
        self.armed = True
        self.cameras_recording = True
        self.motion_sensors_active = True
        self.door_sensors_active = True
        return f"Security system armed in {mode} mode"
    
    def disarm_system(self):
        """Disarm the security system."""
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
        return "Security system disarmed"
    
    def get_status(self):
        """Get security system status."""
        return {
            'armed': self.armed,
            'cameras': self.cameras_recording,
            'motion_sensors': self.motion_sensors_active,
            'door_sensors': self.door_sensors_active,
            'alarm': self.alarm_triggered
        }

# What we accomplished in this step:
# - Added complex security subsystem with multiple components
# - Added state management for various security features
# - Now have two complex subsystems to coordinate


# Step 3: Add climate control and door lock subsystems
# ===============================================================================

# Explanation:
# More complex subsystems that the facade will coordinate.
# We build upon the lighting and security systems from previous steps.

class LightingSystem:
    """Complex lighting control system."""
    
    def __init__(self):
        self.lights = {
            'living_room': False,
            'bedroom': False,
            'kitchen': False,
            'bathroom': False,
            'outdoor': False
        }
        self.brightness = {room: 50 for room in self.lights}
    
    def turn_on_light(self, room: str, brightness: int = 100):
        """Turn on light in specific room."""
        if room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
            return f"Light in {room} turned on at {brightness}% brightness"
        return f"Room {room} not found"
    
    def turn_off_light(self, room: str):
        """Turn off light in specific room."""
        if room in self.lights:
            self.lights[room] = False
            return f"Light in {room} turned off"
        return f"Room {room} not found"
    
    def turn_on_all_lights(self, brightness: int = 100):
        """Turn on all lights."""
        for room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
        return f"All lights turned on at {brightness}% brightness"
    
    def turn_off_all_lights(self):
        """Turn off all lights."""
        for room in self.lights:
            self.lights[room] = False
        return "All lights turned off"
    
    def dim_lights(self, brightness: int):
        """Dim all lights to specified brightness."""
        for room in self.lights:
            if self.lights[room]:
                self.brightness[room] = brightness
        return f"All lights dimmed to {brightness}%"

class SecuritySystem:
    """Complex security system."""
    
    def __init__(self):
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
    
    def arm_system(self, mode: str = "away"):
        """Arm the security system."""
        self.armed = True
        self.cameras_recording = True
        self.motion_sensors_active = True
        self.door_sensors_active = True
        return f"Security system armed in {mode} mode"
    
    def disarm_system(self):
        """Disarm the security system."""
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
        return "Security system disarmed"
    
    def get_status(self):
        """Get security system status."""
        return {
            'armed': self.armed,
            'cameras': self.cameras_recording,
            'motion_sensors': self.motion_sensors_active,
            'door_sensors': self.door_sensors_active,
            'alarm': self.alarm_triggered
        }

class ClimateControl:
    """Complex climate control system."""
    
    def __init__(self):
        self.temperature = 72
        self.target_temperature = 72
        self.heating_on = False
        self.cooling_on = False
        self.fan_speed = 0
    
    def set_temperature(self, temp: int):
        """Set target temperature."""
        self.target_temperature = temp
        self._adjust_system()
        return f"Target temperature set to {temp}°F"
    
    def _adjust_system(self):
        """Internal method to adjust heating/cooling."""
        if self.target_temperature > self.temperature:
            self.heating_on = True
            self.cooling_on = False
            self.fan_speed = 3
        elif self.target_temperature < self.temperature:
            self.heating_on = False
            self.cooling_on = True
            self.fan_speed = 3
        else:
            self.heating_on = False
            self.cooling_on = False
            self.fan_speed = 1
    
    def set_eco_mode(self):
        """Set energy-saving mode."""
        if self.heating_on:
            self.target_temperature = max(65, self.target_temperature - 3)
        elif self.cooling_on:
            self.target_temperature = min(78, self.target_temperature + 3)
        self._adjust_system()
        return f"Eco mode activated. Temperature set to {self.target_temperature}°F"

class DoorLockSystem:
    """Complex door lock system."""
    
    def __init__(self):
        self.doors = {
            'front_door': False,
            'back_door': False,
            'garage_door': False
        }
    
    def lock_door(self, door: str):
        """Lock specific door."""
        if door in self.doors:
            self.doors[door] = True
            return f"{door} locked"
        return f"Door {door} not found"
    
    def unlock_door(self, door: str):
        """Unlock specific door."""
        if door in self.doors:
            self.doors[door] = False
            return f"{door} unlocked"
        return f"Door {door} not found"
    
    def lock_all_doors(self):
        """Lock all doors."""
        for door in self.doors:
            self.doors[door] = True
        return "All doors locked"

# What we accomplished in this step:
# - Added more complex subsystems with internal logic
# - Created systems that need coordination
# - Now have four complex subsystems ready for facade coordination


# Step 4: Create the facade class
# ===============================================================================

# Explanation:
# The facade provides simple, high-level operations that coordinate
# multiple subsystems behind the scenes.
# We build upon all subsystems from previous steps.

class LightingSystem:
    """Complex lighting control system."""
    
    def __init__(self):
        self.lights = {
            'living_room': False,
            'bedroom': False,
            'kitchen': False,
            'bathroom': False,
            'outdoor': False
        }
        self.brightness = {room: 50 for room in self.lights}
    
    def turn_on_light(self, room: str, brightness: int = 100):
        """Turn on light in specific room."""
        if room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
            return f"Light in {room} turned on at {brightness}% brightness"
        return f"Room {room} not found"
    
    def turn_off_light(self, room: str):
        """Turn off light in specific room."""
        if room in self.lights:
            self.lights[room] = False
            return f"Light in {room} turned off"
        return f"Room {room} not found"
    
    def turn_on_all_lights(self, brightness: int = 100):
        """Turn on all lights."""
        for room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
        return f"All lights turned on at {brightness}% brightness"
    
    def turn_off_all_lights(self):
        """Turn off all lights."""
        for room in self.lights:
            self.lights[room] = False
        return "All lights turned off"
    
    def dim_lights(self, brightness: int):
        """Dim all lights to specified brightness."""
        for room in self.lights:
            if self.lights[room]:
                self.brightness[room] = brightness
        return f"All lights dimmed to {brightness}%"

class SecuritySystem:
    """Complex security system."""
    
    def __init__(self):
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
    
    def arm_system(self, mode: str = "away"):
        """Arm the security system."""
        self.armed = True
        self.cameras_recording = True
        self.motion_sensors_active = True
        self.door_sensors_active = True
        return f"Security system armed in {mode} mode"
    
    def disarm_system(self):
        """Disarm the security system."""
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
        return "Security system disarmed"
    
    def get_status(self):
        """Get security system status."""
        return {
            'armed': self.armed,
            'cameras': self.cameras_recording,
            'motion_sensors': self.motion_sensors_active,
            'door_sensors': self.door_sensors_active,
            'alarm': self.alarm_triggered
        }

class ClimateControl:
    """Complex climate control system."""
    
    def __init__(self):
        self.temperature = 72
        self.target_temperature = 72
        self.heating_on = False
        self.cooling_on = False
        self.fan_speed = 0
    
    def set_temperature(self, temp: int):
        """Set target temperature."""
        self.target_temperature = temp
        self._adjust_system()
        return f"Target temperature set to {temp}°F"
    
    def _adjust_system(self):
        """Internal method to adjust heating/cooling."""
        if self.target_temperature > self.temperature:
            self.heating_on = True
            self.cooling_on = False
            self.fan_speed = 3
        elif self.target_temperature < self.temperature:
            self.heating_on = False
            self.cooling_on = True
            self.fan_speed = 3
        else:
            self.heating_on = False
            self.cooling_on = False
            self.fan_speed = 1
    
    def set_eco_mode(self):
        """Set energy-saving mode."""
        if self.heating_on:
            self.target_temperature = max(65, self.target_temperature - 3)
        elif self.cooling_on:
            self.target_temperature = min(78, self.target_temperature + 3)
        self._adjust_system()
        return f"Eco mode activated. Temperature set to {self.target_temperature}°F"

class DoorLockSystem:
    """Complex door lock system."""
    
    def __init__(self):
        self.doors = {
            'front_door': False,
            'back_door': False,
            'garage_door': False
        }
    
    def lock_door(self, door: str):
        """Lock specific door."""
        if door in self.doors:
            self.doors[door] = True
            return f"{door} locked"
        return f"Door {door} not found"
    
    def unlock_door(self, door: str):
        """Unlock specific door."""
        if door in self.doors:
            self.doors[door] = False
            return f"{door} unlocked"
        return f"Door {door} not found"
    
    def lock_all_doors(self):
        """Lock all doors."""
        for door in self.doors:
            self.doors[door] = True
        return "All doors locked"

class SmartHomeFacade:
    """Simplified interface for complex smart home systems."""
    
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControl()
        self.doors = DoorLockSystem()
    
    def leave_home(self):
        """Execute leaving home routine."""
        print("🏠 Executing 'Leave Home' routine...")
        
        actions = []
        actions.append(self.lighting.turn_off_all_lights())
        actions.append(self.doors.lock_all_doors())
        actions.append(self.security.arm_system("away"))
        actions.append(self.climate.set_eco_mode())
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🔒 Home secured for departure!")
        return actions
    
    def arrive_home(self):
        """Execute arriving home routine."""
        print("🏠 Executing 'Arrive Home' routine...")
        
        actions = []
        actions.append(self.doors.unlock_door("front_door"))
        actions.append(self.security.disarm_system())
        actions.append(self.lighting.turn_on_light("living_room", 75))
        actions.append(self.lighting.turn_on_light("kitchen", 50))
        actions.append(self.climate.set_temperature(72))
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🏡 Welcome home!")
        return actions
    
    def bedtime_routine(self):
        """Execute bedtime routine."""
        print("🌙 Executing 'Bedtime' routine...")
        
        actions = []
        actions.append(self.lighting.turn_off_light("living_room"))
        actions.append(self.lighting.turn_off_light("kitchen"))
        actions.append(self.lighting.turn_on_light("bedroom", 25))
        actions.append(self.doors.lock_all_doors())
        actions.append(self.security.arm_system("home"))
        actions.append(self.climate.set_temperature(68))
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("😴 Good night!")
        return actions

# What we accomplished in this step:
# - Created facade that coordinates multiple subsystems
# - Provided simple, high-level operations
# - Hid complexity from the client
# - Demonstrated the core facade pattern


# Step 5: Add more facade operations
# ===============================================================================

# Explanation:
# Let's add more high-level operations to show the facade's versatility.
# We build upon all previous steps including the basic facade.

class LightingSystem:
    """Complex lighting control system."""
    
    def __init__(self):
        self.lights = {
            'living_room': False,
            'bedroom': False,
            'kitchen': False,
            'bathroom': False,
            'outdoor': False
        }
        self.brightness = {room: 50 for room in self.lights}
    
    def turn_on_light(self, room: str, brightness: int = 100):
        """Turn on light in specific room."""
        if room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
            return f"Light in {room} turned on at {brightness}% brightness"
        return f"Room {room} not found"
    
    def turn_off_light(self, room: str):
        """Turn off light in specific room."""
        if room in self.lights:
            self.lights[room] = False
            return f"Light in {room} turned off"
        return f"Room {room} not found"
    
    def turn_on_all_lights(self, brightness: int = 100):
        """Turn on all lights."""
        for room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
        return f"All lights turned on at {brightness}% brightness"
    
    def turn_off_all_lights(self):
        """Turn off all lights."""
        for room in self.lights:
            self.lights[room] = False
        return "All lights turned off"
    
    def dim_lights(self, brightness: int):
        """Dim all lights to specified brightness."""
        for room in self.lights:
            if self.lights[room]:
                self.brightness[room] = brightness
        return f"All lights dimmed to {brightness}%"

class SecuritySystem:
    """Complex security system."""
    
    def __init__(self):
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
    
    def arm_system(self, mode: str = "away"):
        """Arm the security system."""
        self.armed = True
        self.cameras_recording = True
        self.motion_sensors_active = True
        self.door_sensors_active = True
        return f"Security system armed in {mode} mode"
    
    def disarm_system(self):
        """Disarm the security system."""
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
        return "Security system disarmed"
    
    def get_status(self):
        """Get security system status."""
        return {
            'armed': self.armed,
            'cameras': self.cameras_recording,
            'motion_sensors': self.motion_sensors_active,
            'door_sensors': self.door_sensors_active,
            'alarm': self.alarm_triggered
        }

class ClimateControl:
    """Complex climate control system."""
    
    def __init__(self):
        self.temperature = 72
        self.target_temperature = 72
        self.heating_on = False
        self.cooling_on = False
        self.fan_speed = 0
    
    def set_temperature(self, temp: int):
        """Set target temperature."""
        self.target_temperature = temp
        self._adjust_system()
        return f"Target temperature set to {temp}°F"
    
    def _adjust_system(self):
        """Internal method to adjust heating/cooling."""
        if self.target_temperature > self.temperature:
            self.heating_on = True
            self.cooling_on = False
            self.fan_speed = 3
        elif self.target_temperature < self.temperature:
            self.heating_on = False
            self.cooling_on = True
            self.fan_speed = 3
        else:
            self.heating_on = False
            self.cooling_on = False
            self.fan_speed = 1
    
    def set_eco_mode(self):
        """Set energy-saving mode."""
        if self.heating_on:
            self.target_temperature = max(65, self.target_temperature - 3)
        elif self.cooling_on:
            self.target_temperature = min(78, self.target_temperature + 3)
        self._adjust_system()
        return f"Eco mode activated. Temperature set to {self.target_temperature}°F"

class DoorLockSystem:
    """Complex door lock system."""
    
    def __init__(self):
        self.doors = {
            'front_door': False,
            'back_door': False,
            'garage_door': False
        }
    
    def lock_door(self, door: str):
        """Lock specific door."""
        if door in self.doors:
            self.doors[door] = True
            return f"{door} locked"
        return f"Door {door} not found"
    
    def unlock_door(self, door: str):
        """Unlock specific door."""
        if door in self.doors:
            self.doors[door] = False
            return f"{door} unlocked"
        return f"Door {door} not found"
    
    def lock_all_doors(self):
        """Lock all doors."""
        for door in self.doors:
            self.doors[door] = True
        return "All doors locked"

class SmartHomeFacade:
    """Simplified interface for complex smart home systems."""
    
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControl()
        self.doors = DoorLockSystem()
    
    def leave_home(self):
        """Execute leaving home routine."""
        print("🏠 Executing 'Leave Home' routine...")
        
        actions = []
        actions.append(self.lighting.turn_off_all_lights())
        actions.append(self.doors.lock_all_doors())
        actions.append(self.security.arm_system("away"))
        actions.append(self.climate.set_eco_mode())
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🔒 Home secured for departure!")
        return actions
    
    def arrive_home(self):
        """Execute arriving home routine."""
        print("🏠 Executing 'Arrive Home' routine...")
        
        actions = []
        actions.append(self.doors.unlock_door("front_door"))
        actions.append(self.security.disarm_system())
        actions.append(self.lighting.turn_on_light("living_room", 75))
        actions.append(self.lighting.turn_on_light("kitchen", 50))
        actions.append(self.climate.set_temperature(72))
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🏡 Welcome home!")
        return actions
    
    def bedtime_routine(self):
        """Execute bedtime routine."""
        print("🌙 Executing 'Bedtime' routine...")
        
        actions = []
        actions.append(self.lighting.turn_off_light("living_room"))
        actions.append(self.lighting.turn_off_light("kitchen"))
        actions.append(self.lighting.turn_on_light("bedroom", 25))
        actions.append(self.doors.lock_all_doors())
        actions.append(self.security.arm_system("home"))
        actions.append(self.climate.set_temperature(68))
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("😴 Good night!")
        return actions

# Enhanced SmartHomeFacade with additional methods
class EnhancedSmartHomeFacade(SmartHomeFacade):
    """Enhanced facade with more operations."""
    
    def movie_night(self):
        """Execute movie night routine."""
        print("🎬 Executing 'Movie Night' routine...")
        
        actions = []
        actions.append(self.lighting.dim_lights(20))
        actions.append(self.climate.set_temperature(70))
        actions.append(self.doors.lock_all_doors())
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🍿 Enjoy your movie!")
        return actions

    def emergency_mode(self):
        """Execute emergency routine."""
        print("🚨 Executing 'Emergency Mode' routine...")
        
        actions = []
        actions.append(self.lighting.turn_on_all_lights(100))
        actions.append(self.doors.unlock_door("front_door"))
        actions.append(self.doors.unlock_door("back_door"))
        actions.append(self.security.disarm_system())
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🚨 Emergency mode activated!")
        return actions

# What we accomplished in this step:
# - Added more high-level operations
# - Showed how facade can provide different scenarios
# - Enhanced the facade with additional convenience methods


# Step 6: Test the complete implementation
# ===============================================================================

# Explanation:
# Let's test our Facade pattern and compare it with direct subsystem access.
# We build upon all previous steps.

class LightingSystem:
    """Complex lighting control system."""
    
    def __init__(self):
        self.lights = {
            'living_room': False,
            'bedroom': False,
            'kitchen': False,
            'bathroom': False,
            'outdoor': False
        }
        self.brightness = {room: 50 for room in self.lights}
    
    def turn_on_light(self, room: str, brightness: int = 100):
        """Turn on light in specific room."""
        if room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
            return f"Light in {room} turned on at {brightness}% brightness"
        return f"Room {room} not found"
    
    def turn_off_light(self, room: str):
        """Turn off light in specific room."""
        if room in self.lights:
            self.lights[room] = False
            return f"Light in {room} turned off"
        return f"Room {room} not found"
    
    def turn_on_all_lights(self, brightness: int = 100):
        """Turn on all lights."""
        for room in self.lights:
            self.lights[room] = True
            self.brightness[room] = brightness
        return f"All lights turned on at {brightness}% brightness"
    
    def turn_off_all_lights(self):
        """Turn off all lights."""
        for room in self.lights:
            self.lights[room] = False
        return "All lights turned off"
    
    def dim_lights(self, brightness: int):
        """Dim all lights to specified brightness."""
        for room in self.lights:
            if self.lights[room]:
                self.brightness[room] = brightness
        return f"All lights dimmed to {brightness}%"

class SecuritySystem:
    """Complex security system."""
    
    def __init__(self):
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
    
    def arm_system(self, mode: str = "away"):
        """Arm the security system."""
        self.armed = True
        self.cameras_recording = True
        self.motion_sensors_active = True
        self.door_sensors_active = True
        return f"Security system armed in {mode} mode"
    
    def disarm_system(self):
        """Disarm the security system."""
        self.armed = False
        self.cameras_recording = False
        self.motion_sensors_active = False
        self.door_sensors_active = False
        self.alarm_triggered = False
        return "Security system disarmed"
    
    def get_status(self):
        """Get security system status."""
        return {
            'armed': self.armed,
            'cameras': self.cameras_recording,
            'motion_sensors': self.motion_sensors_active,
            'door_sensors': self.door_sensors_active,
            'alarm': self.alarm_triggered
        }

class ClimateControl:
    """Complex climate control system."""
    
    def __init__(self):
        self.temperature = 72
        self.target_temperature = 72
        self.heating_on = False
        self.cooling_on = False
        self.fan_speed = 0
    
    def set_temperature(self, temp: int):
        """Set target temperature."""
        self.target_temperature = temp
        self._adjust_system()
        return f"Target temperature set to {temp}°F"
    
    def _adjust_system(self):
        """Internal method to adjust heating/cooling."""
        if self.target_temperature > self.temperature:
            self.heating_on = True
            self.cooling_on = False
            self.fan_speed = 3
        elif self.target_temperature < self.temperature:
            self.heating_on = False
            self.cooling_on = True
            self.fan_speed = 3
        else:
            self.heating_on = False
            self.cooling_on = False
            self.fan_speed = 1
    
    def set_eco_mode(self):
        """Set energy-saving mode."""
        if self.heating_on:
            self.target_temperature = max(65, self.target_temperature - 3)
        elif self.cooling_on:
            self.target_temperature = min(78, self.target_temperature + 3)
        self._adjust_system()
        return f"Eco mode activated. Temperature set to {self.target_temperature}°F"

class DoorLockSystem:
    """Complex door lock system."""
    
    def __init__(self):
        self.doors = {
            'front_door': False,
            'back_door': False,
            'garage_door': False
        }
    
    def lock_door(self, door: str):
        """Lock specific door."""
        if door in self.doors:
            self.doors[door] = True
            return f"{door} locked"
        return f"Door {door} not found"
    
    def unlock_door(self, door: str):
        """Unlock specific door."""
        if door in self.doors:
            self.doors[door] = False
            return f"{door} unlocked"
        return f"Door {door} not found"
    
    def lock_all_doors(self):
        """Lock all doors."""
        for door in self.doors:
            self.doors[door] = True
        return "All doors locked"

class SmartHomeFacade:
    """Simplified interface for complex smart home systems."""
    
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControl()
        self.doors = DoorLockSystem()
    
    def leave_home(self):
        """Execute leaving home routine."""
        print("🏠 Executing 'Leave Home' routine...")
        
        actions = []
        actions.append(self.lighting.turn_off_all_lights())
        actions.append(self.doors.lock_all_doors())
        actions.append(self.security.arm_system("away"))
        actions.append(self.climate.set_eco_mode())
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🔒 Home secured for departure!")
        return actions
    
    def arrive_home(self):
        """Execute arriving home routine."""
        print("🏠 Executing 'Arrive Home' routine...")
        
        actions = []
        actions.append(self.doors.unlock_door("front_door"))
        actions.append(self.security.disarm_system())
        actions.append(self.lighting.turn_on_light("living_room", 75))
        actions.append(self.lighting.turn_on_light("kitchen", 50))
        actions.append(self.climate.set_temperature(72))
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🏡 Welcome home!")
        return actions
    
    def bedtime_routine(self):
        """Execute bedtime routine."""
        print("🌙 Executing 'Bedtime' routine...")
        
        actions = []
        actions.append(self.lighting.turn_off_light("living_room"))
        actions.append(self.lighting.turn_off_light("kitchen"))
        actions.append(self.lighting.turn_on_light("bedroom", 25))
        actions.append(self.doors.lock_all_doors())
        actions.append(self.security.arm_system("home"))
        actions.append(self.climate.set_temperature(68))
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("😴 Good night!")
        return actions

# Enhanced SmartHomeFacade with additional methods
class EnhancedSmartHomeFacade(SmartHomeFacade):
    """Enhanced facade with more operations."""
    
    def movie_night(self):
        """Execute movie night routine."""
        print("🎬 Executing 'Movie Night' routine...")
        
        actions = []
        actions.append(self.lighting.dim_lights(20))
        actions.append(self.climate.set_temperature(70))
        actions.append(self.doors.lock_all_doors())
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🍿 Enjoy your movie!")
        return actions

    def emergency_mode(self):
        """Execute emergency routine."""
        print("🚨 Executing 'Emergency Mode' routine...")
        
        actions = []
        actions.append(self.lighting.turn_on_all_lights(100))
        actions.append(self.doors.unlock_door("front_door"))
        actions.append(self.doors.unlock_door("back_door"))
        actions.append(self.security.disarm_system())
        
        for action in actions:
            print(f"  ✓ {action}")
        
        print("🚨 Emergency mode activated!")
        return actions

print("=== Testing Facade Pattern ===\n")

# Create enhanced smart home facade
home = EnhancedSmartHomeFacade()

# Test different routines
print("--- Testing Facade Operations ---")
home.arrive_home()
print()

home.movie_night()
print()

home.bedtime_routine()
print()

home.leave_home()
print()

home.emergency_mode()
print()

# Compare with direct subsystem access
print("--- Direct Subsystem Access (Complex) ---")
print("Manual bedtime setup without facade:")

lighting = LightingSystem()
security = SecuritySystem()
climate = ClimateControl()
doors = DoorLockSystem()

print(f"  {lighting.turn_off_light('living_room')}")
print(f"  {lighting.turn_off_light('kitchen')}")
print(f"  {lighting.turn_on_light('bedroom', 25)}")
print(f"  {doors.lock_all_doors()}")
print(f"  {security.arm_system('home')}")
print(f"  {climate.set_temperature(68)}")
print("  (Much more complex without facade!)")

# What we accomplished in this step:
# - Tested all facade operations
# - Compared facade simplicity with direct subsystem access
# - Demonstrated the value of the facade pattern
# - Showed complete working implementation


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Facade pattern structure and purpose
# - Simplifying complex subsystem interactions
# - High-level operation coordination
# - Hiding implementation complexity from clients
# - Providing convenient interfaces for common tasks
# - Reducing coupling between client and subsystems
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding more subsystems!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================