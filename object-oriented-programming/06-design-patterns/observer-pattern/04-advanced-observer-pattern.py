"""Question: Create a class Observable that allows observers to subscribe
and get notified when the state changes.
Implement the observer pattern using private and protected attributes.
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
# - What are private vs protected attributes? (_ vs __)
# - How is this different from previous Observer implementations?
# - What methods does Observable need? (subscribe, unsubscribe, notify)
# - What interface should Observer have? (update method)
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
# Let's start with the Observer base class that defines the interface.
# This establishes the contract that all observers must follow.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created Observer base class with abstract update method


# Step 2: Define Observable class with private attributes
# ===============================================================================

# Explanation:
# The Observable class will use private attributes to encapsulate its internal state.
# We'll use _ for protected and __ for private attributes to demonstrate encapsulation levels.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class Observable:
    def __init__(self):
        self._observers = []        # Protected: accessible by subclasses
        self.__state = None         # Private: only accessible within this class

# What we accomplished in this step:
# - Created Observable class with protected and private attributes
# - Demonstrated different levels of encapsulation


# Step 3: Add subscription management methods
# ===============================================================================

# Explanation:
# Let's add methods to manage observer subscriptions. We'll include both
# subscribe and unsubscribe for complete functionality.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class Observable:
    def __init__(self):
        self._observers = []
        self.__state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer subscribed. Total observers: {len(self._observers)}")

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer unsubscribed. Total observers: {len(self._observers)}")

# What we accomplished in this step:
# - Added subscribe and unsubscribe methods
# - Included duplicate prevention and feedback


# Step 4: Add state management with private access
# ===============================================================================

# Explanation:
# Let's add methods to manage the private state. We'll provide controlled access
# to the private __state attribute through public methods.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class Observable:
    def __init__(self):
        self._observers = []
        self.__state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer subscribed. Total observers: {len(self._observers)}")

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer unsubscribed. Total observers: {len(self._observers)}")

    def set_state(self, new_state):
        old_state = self.__state
        self.__state = new_state
        self._notify_observers(f"State changed from {old_state} to {new_state}")

    def get_state(self):
        return self.__state

# What we accomplished in this step:
# - Added state management methods
# - Demonstrated controlled access to private attributes


# Step 5: Add notification mechanism
# ===============================================================================

# Explanation:
# Let's add the notification methods. We'll have both a private method for internal use
# and a public method for external notifications.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class Observable:
    def __init__(self):
        self._observers = []
        self.__state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer subscribed. Total observers: {len(self._observers)}")

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer unsubscribed. Total observers: {len(self._observers)}")

    def set_state(self, new_state):
        old_state = self.__state
        self.__state = new_state
        self._notify_observers(f"State changed from {old_state} to {new_state}")

    def get_state(self):
        return self.__state

    def _notify_observers(self, message):
        """Protected method for internal notification"""
        for observer in self._observers:
            observer.update(message)

    def notify(self, message):
        """Public method for external notifications"""
        self._notify_observers(message)

# What we accomplished in this step:
# - Added protected _notify_observers method
# - Added public notify method for external use


# Step 6: Create concrete observer implementations
# ===============================================================================

# Explanation:
# Let's create different types of concrete observers to demonstrate
# the flexibility of the Observer pattern.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class Observable:
    def __init__(self):
        self._observers = []
        self.__state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer subscribed. Total observers: {len(self._observers)}")

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer unsubscribed. Total observers: {len(self._observers)}")

    def set_state(self, new_state):
        old_state = self.__state
        self.__state = new_state
        self._notify_observers(f"State changed from {old_state} to {new_state}")

    def get_state(self):
        return self.__state

    def _notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def notify(self, message):
        self._notify_observers(message)

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"[{self.name}] Received: {message}")

class LoggingObserver(Observer):
    def __init__(self):
        self.log = []

    def update(self, message):
        self.log.append(message)
        print(f"[LOGGER] Logged: {message}")

# What we accomplished in this step:
# - Created ConcreteObserver with custom name
# - Created LoggingObserver that maintains a log


# Step 7: Test the observer pattern with encapsulation
# ===============================================================================

# Explanation:
# Finally, let's test our complete implementation to demonstrate how private
# and protected attributes work with the Observer pattern.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class Observable:
    def __init__(self):
        self._observers = []
        self.__state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer subscribed. Total observers: {len(self._observers)}")

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer unsubscribed. Total observers: {len(self._observers)}")

    def set_state(self, new_state):
        old_state = self.__state
        self.__state = new_state
        self._notify_observers(f"State changed from {old_state} to {new_state}")

    def get_state(self):
        return self.__state

    def _notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def notify(self, message):
        self._notify_observers(message)

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"[{self.name}] Received: {message}")

class LoggingObserver(Observer):
    def __init__(self):
        self.log = []

    def update(self, message):
        self.log.append(message)
        print(f"[LOGGER] Logged: {message}")

# Test our implementation:
print("Testing Observer Pattern with Encapsulation:")

# Create observable and observers
observable = Observable()
observer1 = ConcreteObserver("Alice")
observer2 = ConcreteObserver("Bob")
logger = LoggingObserver()

# Subscribe observers
observable.subscribe(observer1)
observable.subscribe(observer2)
observable.subscribe(logger)

print(f"\nInitial state: {observable.get_state()}")

# Test state changes
print("\nChanging state to 'active':")
observable.set_state("active")

print("\nChanging state to 'inactive':")
observable.set_state("inactive")

# Test direct notification
print("\nSending direct notification:")
observable.notify("System maintenance scheduled")

# Test unsubscription
print("\nUnsubscribing Alice:")
observable.unsubscribe(observer1)

print("\nSending final notification:")
observable.notify("Maintenance completed")

print(f"\nLogger history: {logger.log}")

# What we accomplished in this step:
# - Created and tested our complete Observer implementation
# - Demonstrated encapsulation with private and protected attributes


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Observer pattern with proper encapsulation
# - Private (__) vs protected (_) attributes
# - Controlled access to internal state
# - Multiple observer types and behaviors
# - Subscription management and notification systems
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding priority-based notifications!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================