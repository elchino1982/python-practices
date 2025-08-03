"""Question: Implement the Facade pattern to provide a simplified interface to a complex subsystem.

Create a home theater system facade that simplifies controlling multiple
components (DVD player, projector, sound system, lights) with simple methods.

Requirements:
1. Create complex subsystem classes (DVDPlayer, Projector, SoundSystem, Lights)
2. Implement HomeTheaterFacade with simple methods
3. Hide complexity of subsystem interactions
4. Provide high-level operations (watchMovie, endMovie)
5. Demonstrate how facade simplifies client code
6. Show both facade usage and direct subsystem access

Example usage:
    theater = HomeTheaterFacade()
    theater.watch_movie("The Matrix")
    theater.end_movie()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!

# Try to implement your solution here:
# (Write your code below this line)


















































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


# Step 1: Create the complex subsystem classes
# ===============================================================================

# Explanation:
# The Facade pattern starts with complex subsystem classes that have their own
# interfaces and methods. These represent the components we want to simplify.

class DVDPlayer:
    """Complex subsystem component - DVD Player."""
    
    def __init__(self):
        self.movie = None
        self.is_on = False
    
    def on(self):
        """Turn on the DVD player."""
        self.is_on = True
        print("DVD Player: Turning on")
    
    def off(self):
        """Turn off the DVD player."""
        self.is_on = False
        self.movie = None
        print("DVD Player: Turning off")
    
    def play(self, movie: str):
        """Play a movie."""
        if self.is_on:
            self.movie = movie
            print(f"DVD Player: Playing '{movie}'")
        else:
            print("DVD Player: Cannot play - player is off")
    
    def stop(self):
        """Stop playing."""
        if self.movie:
            print(f"DVD Player: Stopping '{self.movie}'")
            self.movie = None
        else:
            print("DVD Player: No movie to stop")
    
    def eject(self):
        """Eject the DVD."""
        if self.is_on:
            if self.movie:
                print(f"DVD Player: Ejecting '{self.movie}'")
                self.movie = None
            else:
                print("DVD Player: No DVD to eject")
        else:
            print("DVD Player: Cannot eject - player is off")

class Projector:
    """Complex subsystem component - Projector."""
    
    def __init__(self):
        self.is_on = False
        self.input_source = None
    
    def on(self):
        """Turn on the projector."""
        self.is_on = True
        print("Projector: Turning on")
    
    def off(self):
        """Turn off the projector."""
        self.is_on = False
        self.input_source = None
        print("Projector: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Projector: Setting input to {source}")
        else:
            print("Projector: Cannot set input - projector is off")
    
    def wide_screen_mode(self):
        """Set to wide screen mode."""
        if self.is_on:
            print("Projector: Setting to wide screen mode")
        else:
            print("Projector: Cannot set mode - projector is off")

# What we accomplished in this step:
# - Created DVDPlayer with complex interface (on, off, play, stop, eject)
# - Created Projector with its own methods (on, off, set_input, wide_screen_mode)
# - Each class has its own state management and error handling


# Step 2: Add more complex subsystem classes
# ===============================================================================

# Explanation:
# Let's add the remaining subsystem components - SoundSystem and Lights.
# Each has its own complex interface that clients would need to learn.

class DVDPlayer:
    """Complex subsystem component - DVD Player."""
    
    def __init__(self):
        self.movie = None
        self.is_on = False
    
    def on(self):
        """Turn on the DVD player."""
        self.is_on = True
        print("DVD Player: Turning on")
    
    def off(self):
        """Turn off the DVD player."""
        self.is_on = False
        self.movie = None
        print("DVD Player: Turning off")
    
    def play(self, movie: str):
        """Play a movie."""
        if self.is_on:
            self.movie = movie
            print(f"DVD Player: Playing '{movie}'")
        else:
            print("DVD Player: Cannot play - player is off")
    
    def stop(self):
        """Stop playing."""
        if self.movie:
            print(f"DVD Player: Stopping '{self.movie}'")
            self.movie = None
        else:
            print("DVD Player: No movie to stop")
    
    def eject(self):
        """Eject the DVD."""
        if self.is_on:
            if self.movie:
                print(f"DVD Player: Ejecting '{self.movie}'")
                self.movie = None
            else:
                print("DVD Player: No DVD to eject")
        else:
            print("DVD Player: Cannot eject - player is off")

class Projector:
    """Complex subsystem component - Projector."""
    
    def __init__(self):
        self.is_on = False
        self.input_source = None
    
    def on(self):
        """Turn on the projector."""
        self.is_on = True
        print("Projector: Turning on")
    
    def off(self):
        """Turn off the projector."""
        self.is_on = False
        self.input_source = None
        print("Projector: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Projector: Setting input to {source}")
        else:
            print("Projector: Cannot set input - projector is off")
    
    def wide_screen_mode(self):
        """Set to wide screen mode."""
        if self.is_on:
            print("Projector: Setting to wide screen mode")
        else:
            print("Projector: Cannot set mode - projector is off")

class SoundSystem:
    """Complex subsystem component - Sound System."""
    
    def __init__(self):
        self.is_on = False
        self.volume = 0
        self.input_source = None
    
    def on(self):
        """Turn on the sound system."""
        self.is_on = True
        print("Sound System: Turning on")
    
    def off(self):
        """Turn off the sound system."""
        self.is_on = False
        self.volume = 0
        self.input_source = None
        print("Sound System: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Sound System: Setting input to {source}")
        else:
            print("Sound System: Cannot set input - system is off")
    
    def set_volume(self, volume: int):
        """Set volume level."""
        if self.is_on:
            self.volume = max(0, min(100, volume))  # Clamp between 0-100
            print(f"Sound System: Setting volume to {self.volume}")
        else:
            print("Sound System: Cannot set volume - system is off")
    
    def set_surround_sound(self):
        """Enable surround sound mode."""
        if self.is_on:
            print("Sound System: Setting to surround sound mode")
        else:
            print("Sound System: Cannot set mode - system is off")

class Lights:
    """Complex subsystem component - Lights."""
    
    def __init__(self):
        self.brightness = 100  # 0-100
        self.is_on = True
    
    def on(self):
        """Turn on the lights."""
        self.is_on = True
        print("Lights: Turning on")
    
    def off(self):
        """Turn off the lights."""
        self.is_on = False
        print("Lights: Turning off")
    
    def dim(self, brightness: int):
        """Dim lights to specified brightness."""
        if self.is_on:
            self.brightness = max(0, min(100, brightness))
            print(f"Lights: Dimming to {self.brightness}%")
        else:
            print("Lights: Cannot dim - lights are off")
    
    def set_movie_mode(self):
        """Set lights to movie mode (very dim)."""
        if self.is_on:
            self.brightness = 10
            print("Lights: Setting to movie mode (10% brightness)")
        else:
            self.on()
            self.brightness = 10
            print("Lights: Turning on and setting to movie mode (10% brightness)")

# What we accomplished in this step:
# - Added SoundSystem with volume, input, and surround sound controls
# - Added Lights with brightness and movie mode functionality
# - Each subsystem has multiple methods and state to manage
# - Clients would need to learn all these interfaces without a facade


# Step 3: Create the basic facade class
# ===============================================================================

# Explanation:
# The facade provides a simplified interface to the complex subsystem.
# It encapsulates the complexity and provides high-level operations.

class DVDPlayer:
    """Complex subsystem component - DVD Player."""
    
    def __init__(self):
        self.movie = None
        self.is_on = False
    
    def on(self):
        """Turn on the DVD player."""
        self.is_on = True
        print("DVD Player: Turning on")
    
    def off(self):
        """Turn off the DVD player."""
        self.is_on = False
        self.movie = None
        print("DVD Player: Turning off")
    
    def play(self, movie: str):
        """Play a movie."""
        if self.is_on:
            self.movie = movie
            print(f"DVD Player: Playing '{movie}'")
        else:
            print("DVD Player: Cannot play - player is off")
    
    def stop(self):
        """Stop playing."""
        if self.movie:
            print(f"DVD Player: Stopping '{self.movie}'")
            self.movie = None
        else:
            print("DVD Player: No movie to stop")
    
    def eject(self):
        """Eject the DVD."""
        if self.is_on:
            if self.movie:
                print(f"DVD Player: Ejecting '{self.movie}'")
                self.movie = None
            else:
                print("DVD Player: No DVD to eject")
        else:
            print("DVD Player: Cannot eject - player is off")

class Projector:
    """Complex subsystem component - Projector."""
    
    def __init__(self):
        self.is_on = False
        self.input_source = None
    
    def on(self):
        """Turn on the projector."""
        self.is_on = True
        print("Projector: Turning on")
    
    def off(self):
        """Turn off the projector."""
        self.is_on = False
        self.input_source = None
        print("Projector: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Projector: Setting input to {source}")
        else:
            print("Projector: Cannot set input - projector is off")
    
    def wide_screen_mode(self):
        """Set to wide screen mode."""
        if self.is_on:
            print("Projector: Setting to wide screen mode")
        else:
            print("Projector: Cannot set mode - projector is off")

class SoundSystem:
    """Complex subsystem component - Sound System."""
    
    def __init__(self):
        self.is_on = False
        self.volume = 0
        self.input_source = None
    
    def on(self):
        """Turn on the sound system."""
        self.is_on = True
        print("Sound System: Turning on")
    
    def off(self):
        """Turn off the sound system."""
        self.is_on = False
        self.volume = 0
        self.input_source = None
        print("Sound System: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Sound System: Setting input to {source}")
        else:
            print("Sound System: Cannot set input - system is off")
    
    def set_volume(self, volume: int):
        """Set volume level."""
        if self.is_on:
            self.volume = max(0, min(100, volume))  # Clamp between 0-100
            print(f"Sound System: Setting volume to {self.volume}")
        else:
            print("Sound System: Cannot set volume - system is off")
    
    def set_surround_sound(self):
        """Enable surround sound mode."""
        if self.is_on:
            print("Sound System: Setting to surround sound mode")
        else:
            print("Sound System: Cannot set mode - system is off")

class Lights:
    """Complex subsystem component - Lights."""
    
    def __init__(self):
        self.brightness = 100  # 0-100
        self.is_on = True
    
    def on(self):
        """Turn on the lights."""
        self.is_on = True
        print("Lights: Turning on")
    
    def off(self):
        """Turn off the lights."""
        self.is_on = False
        print("Lights: Turning off")
    
    def dim(self, brightness: int):
        """Dim lights to specified brightness."""
        if self.is_on:
            self.brightness = max(0, min(100, brightness))
            print(f"Lights: Dimming to {self.brightness}%")
        else:
            print("Lights: Cannot dim - lights are off")
    
    def set_movie_mode(self):
        """Set lights to movie mode (very dim)."""
        if self.is_on:
            self.brightness = 10
            print("Lights: Setting to movie mode (10% brightness)")
        else:
            self.on()
            self.brightness = 10
            print("Lights: Turning on and setting to movie mode (10% brightness)")

class HomeTheaterFacade:
    """Facade that provides simplified interface to the home theater system."""
    
    def __init__(self):
        # Initialize all subsystem components
        self.dvd_player = DVDPlayer()
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.lights = Lights()
    
    def watch_movie(self, movie: str):
        """Simplified method to start watching a movie."""
        print("=== Starting Movie Experience ===")
        
        # Turn on all components in the right order
        self.lights.set_movie_mode()
        self.projector.on()
        self.projector.set_input("DVD")
        self.projector.wide_screen_mode()
        
        self.sound_system.on()
        self.sound_system.set_input("DVD")
        self.sound_system.set_volume(75)
        self.sound_system.set_surround_sound()
        
        self.dvd_player.on()
        self.dvd_player.play(movie)
        
        print("=== Movie Started - Enjoy! ===")
    
    def end_movie(self):
        """Simplified method to end the movie experience."""
        print("=== Ending Movie Experience ===")
        
        # Turn off all components in reverse order
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd_player.off()
        
        self.sound_system.off()
        self.projector.off()
        self.lights.on()  # Turn lights back to normal
        
        print("=== Movie Experience Ended ===")

# What we accomplished in this step:
# - Created HomeTheaterFacade that encapsulates all subsystem components
# - Implemented watch_movie() method that coordinates multiple subsystems
# - Implemented end_movie() method that properly shuts down the system
# - Hid the complexity of managing multiple components from the client


# Step 4: Add more facade methods and functionality
# ===============================================================================

# Explanation:
# Let's expand the facade with more convenient methods and options.
# This shows how facades can provide multiple levels of abstraction.

class DVDPlayer:
    """Complex subsystem component - DVD Player."""
    
    def __init__(self):
        self.movie = None
        self.is_on = False
    
    def on(self):
        """Turn on the DVD player."""
        self.is_on = True
        print("DVD Player: Turning on")
    
    def off(self):
        """Turn off the DVD player."""
        self.is_on = False
        self.movie = None
        print("DVD Player: Turning off")
    
    def play(self, movie: str):
        """Play a movie."""
        if self.is_on:
            self.movie = movie
            print(f"DVD Player: Playing '{movie}'")
        else:
            print("DVD Player: Cannot play - player is off")
    
    def stop(self):
        """Stop playing."""
        if self.movie:
            print(f"DVD Player: Stopping '{self.movie}'")
            self.movie = None
        else:
            print("DVD Player: No movie to stop")
    
    def eject(self):
        """Eject the DVD."""
        if self.is_on:
            if self.movie:
                print(f"DVD Player: Ejecting '{self.movie}'")
                self.movie = None
            else:
                print("DVD Player: No DVD to eject")
        else:
            print("DVD Player: Cannot eject - player is off")

class Projector:
    """Complex subsystem component - Projector."""
    
    def __init__(self):
        self.is_on = False
        self.input_source = None
    
    def on(self):
        """Turn on the projector."""
        self.is_on = True
        print("Projector: Turning on")
    
    def off(self):
        """Turn off the projector."""
        self.is_on = False
        self.input_source = None
        print("Projector: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Projector: Setting input to {source}")
        else:
            print("Projector: Cannot set input - projector is off")
    
    def wide_screen_mode(self):
        """Set to wide screen mode."""
        if self.is_on:
            print("Projector: Setting to wide screen mode")
        else:
            print("Projector: Cannot set mode - projector is off")

class SoundSystem:
    """Complex subsystem component - Sound System."""
    
    def __init__(self):
        self.is_on = False
        self.volume = 0
        self.input_source = None
    
    def on(self):
        """Turn on the sound system."""
        self.is_on = True
        print("Sound System: Turning on")
    
    def off(self):
        """Turn off the sound system."""
        self.is_on = False
        self.volume = 0
        self.input_source = None
        print("Sound System: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Sound System: Setting input to {source}")
        else:
            print("Sound System: Cannot set input - system is off")
    
    def set_volume(self, volume: int):
        """Set volume level."""
        if self.is_on:
            self.volume = max(0, min(100, volume))  # Clamp between 0-100
            print(f"Sound System: Setting volume to {self.volume}")
        else:
            print("Sound System: Cannot set volume - system is off")
    
    def set_surround_sound(self):
        """Enable surround sound mode."""
        if self.is_on:
            print("Sound System: Setting to surround sound mode")
        else:
            print("Sound System: Cannot set mode - system is off")

class Lights:
    """Complex subsystem component - Lights."""
    
    def __init__(self):
        self.brightness = 100  # 0-100
        self.is_on = True
    
    def on(self):
        """Turn on the lights."""
        self.is_on = True
        print("Lights: Turning on")
    
    def off(self):
        """Turn off the lights."""
        self.is_on = False
        print("Lights: Turning off")
    
    def dim(self, brightness: int):
        """Dim lights to specified brightness."""
        if self.is_on:
            self.brightness = max(0, min(100, brightness))
            print(f"Lights: Dimming to {self.brightness}%")
        else:
            print("Lights: Cannot dim - lights are off")
    
    def set_movie_mode(self):
        """Set lights to movie mode (very dim)."""
        if self.is_on:
            self.brightness = 10
            print("Lights: Setting to movie mode (10% brightness)")
        else:
            self.on()
            self.brightness = 10
            print("Lights: Turning on and setting to movie mode (10% brightness)")

class HomeTheaterFacade:
    """Facade that provides simplified interface to the home theater system."""
    
    def __init__(self):
        # Initialize all subsystem components
        self.dvd_player = DVDPlayer()
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.lights = Lights()
    
    def watch_movie(self, movie: str):
        """Simplified method to start watching a movie."""
        print("=== Starting Movie Experience ===")
        
        # Turn on all components in the right order
        self.lights.set_movie_mode()
        self.projector.on()
        self.projector.set_input("DVD")
        self.projector.wide_screen_mode()
        
        self.sound_system.on()
        self.sound_system.set_input("DVD")
        self.sound_system.set_volume(75)
        self.sound_system.set_surround_sound()
        
        self.dvd_player.on()
        self.dvd_player.play(movie)
        
        print("=== Movie Started - Enjoy! ===")
    
    def end_movie(self):
        """Simplified method to end the movie experience."""
        print("=== Ending Movie Experience ===")
        
        # Turn off all components in reverse order
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd_player.off()
        
        self.sound_system.off()
        self.projector.off()
        self.lights.on()  # Turn lights back to normal
        
        print("=== Movie Experience Ended ===")
    
    def pause_movie(self):
        """Pause the current movie and brighten lights slightly."""
        print("=== Pausing Movie ===")
        self.dvd_player.stop()
        self.lights.dim(30)  # Brighten lights for intermission
        print("=== Movie Paused ===")
    
    def resume_movie(self):
        """Resume the movie and dim lights back."""
        print("=== Resuming Movie ===")
        self.lights.set_movie_mode()
        if self.dvd_player.movie:
            print(f"DVD Player: Resuming '{self.dvd_player.movie}'")
        print("=== Movie Resumed ===")
    
    def adjust_volume(self, volume: int):
        """Convenient method to adjust volume."""
        self.sound_system.set_volume(volume)
    
    def set_ambient_mode(self):
        """Set up ambient lighting and background music."""
        print("=== Setting Ambient Mode ===")
        self.lights.dim(50)
        self.sound_system.on()
        self.sound_system.set_input("Streaming")
        self.sound_system.set_volume(30)
        print("=== Ambient Mode Set ===")
    
    def shutdown_all(self):
        """Emergency shutdown of all systems."""
        print("=== Emergency Shutdown ===")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        self.lights.on()
        print("=== All Systems Shutdown ===")

# What we accomplished in this step:
# - Added pause_movie() and resume_movie() for better control
# - Added adjust_volume() for convenient volume control
# - Added set_ambient_mode() for different use cases
# - Added shutdown_all() for emergency situations
# - Demonstrated how facades can provide multiple abstraction levels


# Step 5: Test the facade pattern and demonstrate direct access
# ===============================================================================

# Explanation:
# Let's test our facade implementation and show the difference between
# using the facade vs. accessing subsystems directly.

class DVDPlayer:
    """Complex subsystem component - DVD Player."""
    
    def __init__(self):
        self.movie = None
        self.is_on = False
    
    def on(self):
        """Turn on the DVD player."""
        self.is_on = True
        print("DVD Player: Turning on")
    
    def off(self):
        """Turn off the DVD player."""
        self.is_on = False
        self.movie = None
        print("DVD Player: Turning off")
    
    def play(self, movie: str):
        """Play a movie."""
        if self.is_on:
            self.movie = movie
            print(f"DVD Player: Playing '{movie}'")
        else:
            print("DVD Player: Cannot play - player is off")
    
    def stop(self):
        """Stop playing."""
        if self.movie:
            print(f"DVD Player: Stopping '{self.movie}'")
            self.movie = None
        else:
            print("DVD Player: No movie to stop")
    
    def eject(self):
        """Eject the DVD."""
        if self.is_on:
            if self.movie:
                print(f"DVD Player: Ejecting '{self.movie}'")
                self.movie = None
            else:
                print("DVD Player: No DVD to eject")
        else:
            print("DVD Player: Cannot eject - player is off")

class Projector:
    """Complex subsystem component - Projector."""
    
    def __init__(self):
        self.is_on = False
        self.input_source = None
    
    def on(self):
        """Turn on the projector."""
        self.is_on = True
        print("Projector: Turning on")
    
    def off(self):
        """Turn off the projector."""
        self.is_on = False
        self.input_source = None
        print("Projector: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Projector: Setting input to {source}")
        else:
            print("Projector: Cannot set input - projector is off")
    
    def wide_screen_mode(self):
        """Set to wide screen mode."""
        if self.is_on:
            print("Projector: Setting to wide screen mode")
        else:
            print("Projector: Cannot set mode - projector is off")

class SoundSystem:
    """Complex subsystem component - Sound System."""
    
    def __init__(self):
        self.is_on = False
        self.volume = 0
        self.input_source = None
    
    def on(self):
        """Turn on the sound system."""
        self.is_on = True
        print("Sound System: Turning on")
    
    def off(self):
        """Turn off the sound system."""
        self.is_on = False
        self.volume = 0
        self.input_source = None
        print("Sound System: Turning off")
    
    def set_input(self, source: str):
        """Set input source."""
        if self.is_on:
            self.input_source = source
            print(f"Sound System: Setting input to {source}")
        else:
            print("Sound System: Cannot set input - system is off")
    
    def set_volume(self, volume: int):
        """Set volume level."""
        if self.is_on:
            self.volume = max(0, min(100, volume))  # Clamp between 0-100
            print(f"Sound System: Setting volume to {self.volume}")
        else:
            print("Sound System: Cannot set volume - system is off")
    
    def set_surround_sound(self):
        """Enable surround sound mode."""
        if self.is_on:
            print("Sound System: Setting to surround sound mode")
        else:
            print("Sound System: Cannot set mode - system is off")

class Lights:
    """Complex subsystem component - Lights."""
    
    def __init__(self):
        self.brightness = 100  # 0-100
        self.is_on = True
    
    def on(self):
        """Turn on the lights."""
        self.is_on = True
        print("Lights: Turning on")
    
    def off(self):
        """Turn off the lights."""
        self.is_on = False
        print("Lights: Turning off")
    
    def dim(self, brightness: int):
        """Dim lights to specified brightness."""
        if self.is_on:
            self.brightness = max(0, min(100, brightness))
            print(f"Lights: Dimming to {self.brightness}%")
        else:
            print("Lights: Cannot dim - lights are off")
    
    def set_movie_mode(self):
        """Set lights to movie mode (very dim)."""
        if self.is_on:
            self.brightness = 10
            print("Lights: Setting to movie mode (10% brightness)")
        else:
            self.on()
            self.brightness = 10
            print("Lights: Turning on and setting to movie mode (10% brightness)")

class HomeTheaterFacade:
    """Facade that provides simplified interface to the home theater system."""
    
    def __init__(self):
        # Initialize all subsystem components
        self.dvd_player = DVDPlayer()
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.lights = Lights()
    
    def watch_movie(self, movie: str):
        """Simplified method to start watching a movie."""
        print("=== Starting Movie Experience ===")
        
        # Turn on all components in the right order
        self.lights.set_movie_mode()
        self.projector.on()
        self.projector.set_input("DVD")
        self.projector.wide_screen_mode()
        
        self.sound_system.on()
        self.sound_system.set_input("DVD")
        self.sound_system.set_volume(75)
        self.sound_system.set_surround_sound()
        
        self.dvd_player.on()
        self.dvd_player.play(movie)
        
        print("=== Movie Started - Enjoy! ===")
    
    def end_movie(self):
        """Simplified method to end the movie experience."""
        print("=== Ending Movie Experience ===")
        
        # Turn off all components in reverse order
        self.dvd_player.stop()
        self.dvd_player.eject()
        self.dvd_player.off()
        
        self.sound_system.off()
        self.projector.off()
        self.lights.on()  # Turn lights back to normal
        
        print("=== Movie Experience Ended ===")
    
    def pause_movie(self):
        """Pause the current movie and brighten lights slightly."""
        print("=== Pausing Movie ===")
        self.dvd_player.stop()
        self.lights.dim(30)  # Brighten lights for intermission
        print("=== Movie Paused ===")
    
    def resume_movie(self):
        """Resume the movie and dim lights back."""
        print("=== Resuming Movie ===")
        self.lights.set_movie_mode()
        if self.dvd_player.movie:
            print(f"DVD Player: Resuming '{self.dvd_player.movie}'")
        print("=== Movie Resumed ===")
    
    def adjust_volume(self, volume: int):
        """Convenient method to adjust volume."""
        self.sound_system.set_volume(volume)
    
    def set_ambient_mode(self):
        """Set up ambient lighting and background music."""
        print("=== Setting Ambient Mode ===")
        self.lights.dim(50)
        self.sound_system.on()
        self.sound_system.set_input("Streaming")
        self.sound_system.set_volume(30)
        print("=== Ambient Mode Set ===")
    
    def shutdown_all(self):
        """Emergency shutdown of all systems."""
        print("=== Emergency Shutdown ===")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        self.lights.on()
        print("=== All Systems Shutdown ===")

print("=== Testing Facade Pattern ===\\n")

# Test 1: Using the facade (simple and convenient)
print("1. Using the Facade (Simple Interface):")
print("-" * 50)
theater = HomeTheaterFacade()
theater.watch_movie("The Matrix")
print()

theater.pause_movie()
print()

theater.adjust_volume(85)
print()

theater.resume_movie()
print()

theater.end_movie()
print("\\n" + "="*60 + "\\n")

# Test 2: Direct subsystem access (complex but flexible)
print("2. Direct Subsystem Access (Complex but Flexible):")
print("-" * 50)
print("Without facade, client needs to manage all components manually:")

# Create components manually
dvd = DVDPlayer()
projector = Projector()
sound = SoundSystem()
lights = Lights()

# Client must know the correct sequence and all the methods
print("Client manually setting up movie experience...")
lights.set_movie_mode()
projector.on()
projector.set_input("DVD")
projector.wide_screen_mode()
sound.on()
sound.set_input("DVD")
sound.set_volume(75)
sound.set_surround_sound()
dvd.on()
dvd.play("Inception")

print("\\nClient manually adjusting volume...")
sound.set_volume(90)

print("\\nClient manually shutting down...")
dvd.stop()
dvd.eject()
dvd.off()
sound.off()
projector.off()
lights.on()

print("\\n" + "="*60 + "\\n")

# Test 3: Demonstrate facade flexibility
print("3. Facade Flexibility:")
print("-" * 50)
theater2 = HomeTheaterFacade()
theater2.set_ambient_mode()
print()

theater2.watch_movie("Interstellar")
print()

theater2.shutdown_all()

# What we accomplished in this step:
# - Tested the facade with multiple scenarios
# - Demonstrated the simplicity of facade usage vs direct access
# - Showed how facade hides complexity from clients
# - Illustrated the flexibility of having both options available


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step Facade pattern solution!
#
# Key concepts learned:
# - Facade pattern structure and purpose
# - Simplifying complex subsystem interfaces
# - Providing high-level operations for common tasks
# - Hiding subsystem complexity from clients
# - Maintaining flexibility for direct subsystem access
# - Coordinating multiple subsystem components
#
# Benefits of the Facade pattern:
# 1. Simplicity: Clients use simple methods instead of complex subsystem APIs
# 2. Decoupling: Clients don't depend directly on subsystem classes
# 3. Convenience: Common operations are wrapped in easy-to-use methods
# 4. Flexibility: Direct subsystem access is still available when needed
# 5. Maintainability: Changes to subsystems can be isolated in the facade
#
# When to use the Facade pattern:
# - When you have a complex subsystem with many classes
# - When you want to provide a simple interface to complex functionality
# - When you need to decouple clients from subsystem implementation details
# - When you want to layer your subsystems
# - When most clients need only a subset of subsystem functionality
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a streaming service!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
