"""Question: Define a class Bird with a method fly.
Create subclasses Sparrow and Penguin.
Ensure that substituting a Penguin for a Bird does not violate
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
# - How does the original Bird hierarchy violate LSP?
# - What happens when you substitute a Penguin for a Bird?
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
# Let's examine the original Bird hierarchy that violates LSP by having
# a Penguin that cannot fly, breaking the expected behavior of Bird.

class Bird:
    def fly(self):
        raise NotImplementedError("Subclasses must implement this method")

class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")

# What we can observe:
# - The Bird class defines a fly() method that all birds should implement
# - Sparrow implements fly() correctly
# - Penguin violates LSP by throwing an exception instead of flying
# - Code that expects any Bird to fly will break with Penguin

print("=== Original Design (LSP Violation) ===")
birds = [Sparrow(), Penguin()]

print("Testing bird flying:")
for i, bird in enumerate(birds, 1):
    bird_type = bird.__class__.__name__
    try:
        result = bird.fly()
        print(f"Bird {i} ({bird_type}): {result}")
    except Exception as e:
        print(f"Bird {i} ({bird_type}): ERROR - {e}")

print("LSP Violation: Penguin cannot be substituted for Bird without breaking functionality!")


# Step 2: Redesign with proper abstraction
# ===============================================================================

# Explanation:
# Let's redesign the hierarchy to follow LSP by creating more specific
# abstractions that don't force all birds to fly.

class Bird:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class FlyingBird(Bird):
    def fly(self):
        raise NotImplementedError("Flying birds must implement this method")
    
    def move(self):
        return self.fly()

class FlightlessBird(Bird):
    def walk(self):
        raise NotImplementedError("Flightless birds must implement this method")
    
    def move(self):
        return self.walk()

# What we accomplished in this step:
# - Created Bird base class with common behaviors (move, make_sound)
# - Separated flying and flightless birds into different hierarchies
# - Each hierarchy only defines methods that make sense for that type


# Step 3: Implement Sparrow as a FlyingBird
# ===============================================================================

# Explanation:
# Now let's implement Sparrow as a FlyingBird, which naturally supports flying.

class Bird:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class FlyingBird(Bird):
    def fly(self):
        raise NotImplementedError("Flying birds must implement this method")
    
    def move(self):
        return self.fly()

class FlightlessBird(Bird):
    def walk(self):
        raise NotImplementedError("Flightless birds must implement this method")
    
    def move(self):
        return self.walk()

class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow is flying quickly between trees"
    
    def make_sound(self):
        return "Sparrow chirps melodiously"

# What we accomplished in this step:
# - Implemented Sparrow as a FlyingBird
# - Sparrow naturally supports flying behavior
# - Follows LSP: Sparrow can be substituted for FlyingBird or Bird


# Step 4: Implement Penguin as a FlightlessBird
# ===============================================================================

# Explanation:
# Let's implement Penguin as a FlightlessBird, which naturally supports
# walking instead of flying.

class Bird:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class FlyingBird(Bird):
    def fly(self):
        raise NotImplementedError("Flying birds must implement this method")
    
    def move(self):
        return self.fly()

class FlightlessBird(Bird):
    def walk(self):
        raise NotImplementedError("Flightless birds must implement this method")
    
    def move(self):
        return self.walk()

class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow is flying quickly between trees"
    
    def make_sound(self):
        return "Sparrow chirps melodiously"

class Penguin(FlightlessBird):
    def walk(self):
        return "Penguin is waddling on ice"
    
    def make_sound(self):
        return "Penguin makes a honking sound"

# What we accomplished in this step:
# - Implemented Penguin as a FlightlessBird
# - Penguin naturally supports walking behavior
# - Follows LSP: Penguin can be substituted for FlightlessBird or Bird


# Step 5: Test our LSP-compliant design
# ===============================================================================

# Explanation:
# Let's test our redesigned hierarchy to verify that it follows LSP
# and all substitutions work correctly.

class Bird:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class FlyingBird(Bird):
    def fly(self):
        raise NotImplementedError("Flying birds must implement this method")
    
    def move(self):
        return self.fly()

class FlightlessBird(Bird):
    def walk(self):
        raise NotImplementedError("Flightless birds must implement this method")
    
    def move(self):
        return self.walk()

class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow is flying quickly between trees"
    
    def make_sound(self):
        return "Sparrow chirps melodiously"

class Penguin(FlightlessBird):
    def walk(self):
        return "Penguin is waddling on ice"
    
    def make_sound(self):
        return "Penguin makes a honking sound"

# Test our LSP-compliant design:
print("\n=== LSP-Compliant Design ===")

# Test with all birds using common Bird interface
all_birds = [Sparrow(), Penguin()]

print("Testing common Bird behaviors:")
for i, bird in enumerate(all_birds, 1):
    bird_type = bird.__class__.__name__
    print(f"Bird {i} ({bird_type}):")
    print(f"  Movement: {bird.move()}")
    print(f"  Sound: {bird.make_sound()}")

# Test flying birds specifically
flying_birds = [Sparrow()]
print("\nTesting FlyingBird behaviors:")
for bird in flying_birds:
    bird_type = bird.__class__.__name__
    print(f"{bird_type}:")
    print(f"  Flying: {bird.fly()}")
    print(f"  Movement: {bird.move()}")

# Test flightless birds specifically
flightless_birds = [Penguin()]
print("\nTesting FlightlessBird behaviors:")
for bird in flightless_birds:
    bird_type = bird.__class__.__name__
    print(f"{bird_type}:")
    print(f"  Walking: {bird.walk()}")
    print(f"  Movement: {bird.move()}")

print("\nLSP Success: All substitutions work correctly without breaking functionality!")

# What we accomplished in this step:
# - Verified that all birds can be used through the Bird interface
# - Demonstrated that specific bird types work with their appropriate interfaces
# - Confirmed that no exceptions are thrown during substitution


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the Liskov Substitution Principle solution!
#
# Key concepts learned:
# - Understanding the Liskov Substitution Principle (LSP)
# - Identifying LSP violations in inheritance hierarchies
# - Redesigning hierarchies to follow LSP
# - Creating appropriate abstractions that don't force invalid behaviors
# - Benefits of LSP-compliant design for maintainability and extensibility
# - How LSP enables polymorphism without breaking functionality
#
# LSP Benefits demonstrated:
# - Subclasses can be substituted for their base classes without breaking code
# - No unexpected exceptions or behaviors when using polymorphism
# - Code that works with base classes automatically works with all subclasses
# - System is more robust and predictable
# - Easy to add new types without breaking existing functionality
#
# Real-world applications:
# - GUI component hierarchies (all buttons should behave like buttons)
# - Database connection classes (all connections should support basic operations)
# - File system abstractions (all file types should support common operations)
# - Payment processing systems (all payment methods should process payments)
# - Game entity hierarchies (all entities should support common behaviors)
# - API client libraries (all clients should support the same interface)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY the original design violates LSP
# 4. Experiment with adding new bird types (Robin, Owl, etc.)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
