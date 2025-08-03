"""Question: Create a class Observable that allows observers to subscribe
 and get notified when the state changes. Implement the observer pattern.
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
# - What is the Observer pattern? (one-to-many dependency between objects)
# - What does Observable need? (list of observers, state, notify method)
# - What does Observer need? (update method to receive notifications)
# - How do you subscribe/unsubscribe observers?
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


# Step 1: Define the Observer base class
# ===============================================================================

# Explanation:
# The Observer pattern involves two main components: Observable (subject) and Observer.
# Let's start with the Observer base class that defines the interface.

class Observer:
    def update(self, state):
        pass  # Subclasses will implement this

# What we accomplished in this step:
# - Created the Observer base class with update method interface


# Step 2: Define the Observable class structure
# ===============================================================================

# Explanation:
# The Observable class maintains a list of observers and notifies them when state changes.
# Let's start with the basic structure and constructor.

class Observer:
    def update(self, state):
        pass

class Observable:
    def __init__(self):
        self._observers = []  # List to store observers
        self._state = None    # Current state

# What we accomplished in this step:
# - Created Observable class with observers list and state


# Step 3: Add subscribe and unsubscribe methods
# ===============================================================================

# Explanation:
# We need methods to add and remove observers from our list.
# We should check for duplicates when subscribing.

class Observer:
    def update(self, state):
        pass

class Observable:
    def __init__(self):
        self._observers = []
        self._state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

# What we accomplished in this step:
# - Added subscribe method to add observers
# - Added unsubscribe method to remove observers


# Step 4: Add notify_observers method
# ===============================================================================

# Explanation:
# This method iterates through all observers and calls their update method
# with the current state.

class Observer:
    def update(self, state):
        pass

class Observable:
    def __init__(self):
        self._observers = []
        self._state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

# What we accomplished in this step:
# - Added notify_observers method to update all observers


# Step 5: Add state management methods
# ===============================================================================

# Explanation:
# We need methods to set and get the state. When state is set,
# we automatically notify all observers.

class Observer:
    def update(self, state):
        pass

class Observable:
    def __init__(self):
        self._observers = []
        self._state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify_observers()

    def get_state(self):
        return self._state

# What we accomplished in this step:
# - Added set_state method that triggers notifications
# - Added get_state method to access current state


# Step 6: Create a concrete observer implementation
# ===============================================================================

# Explanation:
# Now let's create a concrete observer that actually does something
# when it receives updates.

class Observer:
    def update(self, state):
        pass

class Observable:
    def __init__(self):
        self._observers = []
        self._state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify_observers()

    def get_state(self):
        return self._state

class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, state):
        print(f"{self._name} received state change: {state}")

# What we accomplished in this step:
# - Created ConcreteObserver that prints notifications


# Step 7: Test the observer pattern
# ===============================================================================

# Explanation:
# Finally, let's create instances and test the complete observer pattern
# to make sure everything works correctly.

class Observer:
    def update(self, state):
        pass

class Observable:
    def __init__(self):
        self._observers = []
        self._state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify_observers()

    def get_state(self):
        return self._state

class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, state):
        print(f"{self._name} received state change: {state}")

# Test our observer pattern:
observable = Observable()

# Create observers
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

# Subscribe observers
observable.subscribe(observer1)
observable.subscribe(observer2)

print("Setting state to 'State 1':")
observable.set_state("State 1")

print("\nSetting state to 'State 2':")
observable.set_state("State 2")

print("\nUnsubscribing Observer 1...")
observable.unsubscribe(observer1)

print("\nSetting state to 'State 3':")
observable.set_state("State 3")

# What we accomplished in this step:
# - Created and tested our complete Observer pattern implementation
# - Demonstrated subscription, notification, and unsubscription


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Observer design pattern implementation
# - One-to-many object relationships
# - Automatic notification systems
# - Interface-based programming with base classes
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding different types of observers!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================