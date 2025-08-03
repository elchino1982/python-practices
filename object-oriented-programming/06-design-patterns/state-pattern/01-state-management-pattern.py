"""Question: Create a class StatefulObject that maintains an internal
state and allows state transitions.
Implement methods to get the current state, set a new state, and define valid transitions.
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
# - What is a state machine? (object that can be in different states)
# - How do you store valid transitions? (dictionary mapping states to allowed next states)
# - How do you validate state transitions? (check if transition is allowed)
# - What should happen for invalid transitions? (reject and show error)
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


# Step 1: Define the StatefulObject class
# ===============================================================================

# Explanation:
# Let's start by creating our StatefulObject class. This class will implement
# a simple state machine that tracks current state and valid transitions.

class StatefulObject:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic StatefulObject class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The __init__ method initializes the object with an initial state and
# an empty dictionary to store valid transitions.

class StatefulObject:
    def __init__(self, initial_state):
        self.state = initial_state
        self.valid_transitions = {}

# What we accomplished in this step:
# - Added constructor to set initial state and transitions dictionary


# Step 3: Add method to define valid transitions
# ===============================================================================

# Explanation:
# The add_transition method allows us to define which state transitions are valid.
# We store this as a dictionary where keys are current states and values are lists of allowed next states.

class StatefulObject:
    def __init__(self, initial_state):
        self.state = initial_state
        self.valid_transitions = {}

    def add_transition(self, from_state, to_state):
        if from_state not in self.valid_transitions:
            self.valid_transitions[from_state] = []
        self.valid_transitions[from_state].append(to_state)

# What we accomplished in this step:
# - Added add_transition method to define valid state transitions


# Step 4: Add method to get current state
# ===============================================================================

# Explanation:
# The get_state method simply returns the current state of the object.
# This provides a clean interface to access the state.

class StatefulObject:
    def __init__(self, initial_state):
        self.state = initial_state
        self.valid_transitions = {}

    def add_transition(self, from_state, to_state):
        if from_state not in self.valid_transitions:
            self.valid_transitions[from_state] = []
        self.valid_transitions[from_state].append(to_state)

    def get_state(self):
        return self.state

# What we accomplished in this step:
# - Added get_state method to access current state


# Step 5: Add method to set new state with validation
# ===============================================================================

# Explanation:
# The set_state method attempts to change to a new state, but only if the transition is valid.
# If invalid, it prints an error message and keeps the current state.

class StatefulObject:
    def __init__(self, initial_state):
        self.state = initial_state
        self.valid_transitions = {}

    def add_transition(self, from_state, to_state):
        if from_state not in self.valid_transitions:
            self.valid_transitions[from_state] = []
        self.valid_transitions[from_state].append(to_state)

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        if new_state in self.valid_transitions.get(self.state, []):
            self.state = new_state
            print(f"State changed to: {new_state}")
        else:
            print(f"Invalid transition from {self.state} to {new_state}")

# What we accomplished in this step:
# - Added set_state method with transition validation


# Step 6: Create an instance and test our state machine
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our StatefulObject and test various state transitions
# to make sure everything works correctly.

class StatefulObject:
    def __init__(self, initial_state):
        self.state = initial_state
        self.valid_transitions = {}

    def add_transition(self, from_state, to_state):
        if from_state not in self.valid_transitions:
            self.valid_transitions[from_state] = []
        self.valid_transitions[from_state].append(to_state)

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        if new_state in self.valid_transitions.get(self.state, []):
            self.state = new_state
            print(f"State changed to: {new_state}")
        else:
            print(f"Invalid transition from {self.state} to {new_state}")

# Test our state machine:
# Create a simple traffic light state machine
traffic_light = StatefulObject("red")

# Define valid transitions
traffic_light.add_transition("red", "green")
traffic_light.add_transition("green", "yellow")
traffic_light.add_transition("yellow", "red")

print(f"Initial state: {traffic_light.get_state()}")

# Test valid transitions
print("\nTesting valid transitions:")
traffic_light.set_state("green")    # red -> green (valid)
traffic_light.set_state("yellow")   # green -> yellow (valid)
traffic_light.set_state("red")      # yellow -> red (valid)

# Test invalid transitions
print("\nTesting invalid transitions:")
traffic_light.set_state("yellow")   # red -> yellow (invalid)
traffic_light.set_state("green")    # red -> green (valid)
traffic_light.set_state("red")      # green -> red (invalid)

print(f"\nFinal state: {traffic_light.get_state()}")

# What we accomplished in this step:
# - Created and tested our complete StatefulObject implementation
# - Demonstrated both valid and invalid state transitions


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - State machine implementation
# - State transition validation
# - Dictionary-based data structure for transitions
# - Error handling for invalid operations
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a door lock or game state machine!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================