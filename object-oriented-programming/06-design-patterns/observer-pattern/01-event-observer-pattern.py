"""Question: Define a class Event that uses the observer pattern to notify
multiple listeners when an event occurs. Implement methods to add and remove listeners.
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
# - How do you store multiple listeners/observers?
# - What data structure is best for adding and removing listeners?
# - How do you notify all listeners when an event occurs?
# - What parameters should the notify method accept?
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


# Step 1: Define the Event class
# ===============================================================================

# Explanation:
# Let's start by creating our Event class. This class will implement the observer
# pattern, allowing multiple listeners to be notified when events occur.

class Event:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Event class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The constructor should initialize a list to store all the listeners that
# want to be notified when events occur.

class Event:
    def __init__(self):
        self._listeners = []

# What we accomplished in this step:
# - Added constructor that initializes an empty listeners list
# - Used underscore prefix to indicate internal/private attribute


# Step 3: Add the add_listener method
# ===============================================================================

# Explanation:
# This method allows new listeners (functions or callable objects) to subscribe
# to the event. They will be called when the event is triggered.

class Event:
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

# What we accomplished in this step:
# - Added method to register new listeners
# - Listeners are stored in the internal list


# Step 4: Add the remove_listener method
# ===============================================================================

# Explanation:
# This method allows listeners to unsubscribe from the event.
# They will no longer be notified when the event occurs.

class Event:
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

# What we accomplished in this step:
# - Added method to unregister listeners
# - Uses list.remove() to find and remove the listener


# Step 5: Add the notify method
# ===============================================================================

# Explanation:
# This method triggers the event by calling all registered listeners.
# It accepts any arguments and passes them to each listener.

class Event:
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def notify(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)

# What we accomplished in this step:
# - Added notify method that calls all listeners
# - Uses *args and **kwargs to pass any arguments to listeners
# - Iterates through all listeners and calls each one


# Step 6: Test our Event class
# ===============================================================================

# Explanation:
# Now let's test our Event class by creating listeners and demonstrating
# how the observer pattern works in practice.

class Event:
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def notify(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)

# Test our Event class:
def listener1(event_data):
    print(f"Listener 1 received: {event_data}")

def listener2(event_data):
    print(f"Listener 2 received: {event_data}")

def listener3(event_data):
    print(f"Listener 3 received: {event_data}")

print("=== Testing Event with Multiple Listeners ===")
event = Event()

# Add listeners
event.add_listener(listener1)
event.add_listener(listener2)
event.add_listener(listener3)

# Trigger event
print("Triggering event with 'Hello World':")
event.notify("Hello World")

print("\nRemoving listener2 and triggering again:")
event.remove_listener(listener2)
event.notify("Second event")

# What we accomplished in this step:
# - Created multiple listener functions
# - Tested adding and removing listeners
# - Verified that all listeners receive notifications
# - Demonstrated listener removal functionality


# Step 7: Enhanced version with error handling and features
# ===============================================================================

# Explanation:
# Let's create an enhanced version that handles edge cases and provides
# additional features like listener counting and safe removal.

class Event:
    def __init__(self, name="Unnamed Event"):
        self._listeners = []
        self.name = name

    def add_listener(self, listener):
        if not callable(listener):
            raise TypeError("Listener must be callable")
        if listener not in self._listeners:
            self._listeners.append(listener)
            print(f"Added listener to {self.name}")
        else:
            print(f"Listener already registered for {self.name}")

    def remove_listener(self, listener):
        try:
            self._listeners.remove(listener)
            print(f"Removed listener from {self.name}")
        except ValueError:
            print(f"Listener not found in {self.name}")

    def notify(self, *args, **kwargs):
        print(f"Notifying {len(self._listeners)} listeners for {self.name}")
        for listener in self._listeners:
            try:
                listener(*args, **kwargs)
            except Exception as e:
                print(f"Error in listener: {e}")

    def get_listener_count(self):
        return len(self._listeners)

    def clear_listeners(self):
        count = len(self._listeners)
        self._listeners.clear()
        print(f"Cleared {count} listeners from {self.name}")

# Test enhanced version:
print("\n=== Enhanced Event with Error Handling ===")

def good_listener(data):
    print(f"Good listener: {data}")

def bad_listener(data):
    raise Exception("Something went wrong!")

enhanced_event = Event("User Login Event")

# Test enhanced features
enhanced_event.add_listener(good_listener)
enhanced_event.add_listener(bad_listener)
enhanced_event.add_listener(good_listener)  # Try to add duplicate

print(f"Listener count: {enhanced_event.get_listener_count()}")

# Test notification with error handling
enhanced_event.notify("User logged in")

# Test safe removal
enhanced_event.remove_listener(bad_listener)
enhanced_event.remove_listener(bad_listener)  # Try to remove again

# Test clearing all listeners
enhanced_event.clear_listeners()

# What we accomplished in this step:
# - Added error handling for invalid listeners
# - Prevented duplicate listener registration
# - Added safe removal with error handling
# - Provided listener counting and clearing functionality
# - Added event naming for better debugging


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Implementing the observer pattern
# - Managing collections of callback functions
# - Using *args and **kwargs for flexible function calls
# - Error handling in event systems
# - Preventing duplicate registrations
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding priority levels for listeners!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
