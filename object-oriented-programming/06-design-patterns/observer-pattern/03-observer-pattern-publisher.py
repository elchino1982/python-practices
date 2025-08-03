"""Question: Create a class Publisher that allows subscribers to subscribe
and get notified when a new article is published. Implement the observer pattern.
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
# - What is the Observer pattern? (Publisher notifies multiple subscribers)
# - What does Publisher need? (list of subscribers, subscribe method, publish method)
# - What does Subscriber need? (notify method to receive articles)
# - How is this similar to q18 but with different terminology?
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


# Step 1: Define the Subscriber base class
# ===============================================================================

# Explanation:
# The Observer pattern (here called Publisher-Subscriber) involves two main components.
# Let's start with the Subscriber base class that defines the interface.

class Subscriber:
    def notify(self, article):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created the Subscriber base class with notify method interface


# Step 2: Define the Publisher class structure
# ===============================================================================

# Explanation:
# The Publisher class maintains a list of subscribers and notifies them when articles are published.
# Let's start with the basic structure and constructor.

class Subscriber:
    def notify(self, article):
        raise NotImplementedError("Subclasses must implement this method")

class Publisher:
    def __init__(self):
        self._subscribers = []  # List to store subscribers

# What we accomplished in this step:
# - Created Publisher class with subscribers list


# Step 3: Add subscribe method
# ===============================================================================

# Explanation:
# We need a method to add subscribers to our list.
# This allows new subscribers to start receiving notifications.

class Subscriber:
    def notify(self, article):
        raise NotImplementedError("Subclasses must implement this method")

class Publisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

# What we accomplished in this step:
# - Added subscribe method to add subscribers


# Step 4: Add publish method
# ===============================================================================

# Explanation:
# The publish method takes an article and notifies all subscribers about it.
# This is the core of the Observer pattern.

class Subscriber:
    def notify(self, article):
        raise NotImplementedError("Subclasses must implement this method")

class Publisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def publish(self, article):
        for subscriber in self._subscribers:
            subscriber.notify(article)

# What we accomplished in this step:
# - Added publish method to notify all subscribers


# Step 5: Create a concrete subscriber implementation
# ===============================================================================

# Explanation:
# Now let's create a concrete subscriber that actually does something
# when it receives article notifications.

class Subscriber:
    def notify(self, article):
        raise NotImplementedError("Subclasses must implement this method")

class Publisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def publish(self, article):
        for subscriber in self._subscribers:
            subscriber.notify(article)

class ConcreteSubscriber(Subscriber):
    def __init__(self, name="Subscriber"):
        self.name = name

    def notify(self, article):
        print(f"{self.name} received new article: {article}")

# What we accomplished in this step:
# - Created ConcreteSubscriber that prints article notifications


# Step 6: Test the publisher-subscriber pattern
# ===============================================================================

# Explanation:
# Finally, let's create instances and test the complete publisher-subscriber pattern
# to make sure everything works correctly.

class Subscriber:
    def notify(self, article):
        raise NotImplementedError("Subclasses must implement this method")

class Publisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def publish(self, article):
        for subscriber in self._subscribers:
            subscriber.notify(article)

class ConcreteSubscriber(Subscriber):
    def __init__(self, name="Subscriber"):
        self.name = name

    def notify(self, article):
        print(f"{self.name} received new article: {article}")

# Test our publisher-subscriber pattern:
publisher = Publisher()

# Create subscribers
subscriber1 = ConcreteSubscriber("Alice")
subscriber2 = ConcreteSubscriber("Bob")
subscriber3 = ConcreteSubscriber("Charlie")

# Subscribe to publisher
publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)
publisher.subscribe(subscriber3)

# Publish articles
print("Publishing first article:")
publisher.publish("Understanding the Observer Pattern")

print("\nPublishing second article:")
publisher.publish("Advanced Python OOP Techniques")

# What we accomplished in this step:
# - Created and tested our complete Publisher-Subscriber implementation
# - Demonstrated multiple subscribers receiving notifications


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Publisher-Subscriber pattern (variant of Observer pattern)
# - One-to-many communication between objects
# - Interface-based programming with abstract methods
# - Real-world application of design patterns
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding unsubscribe functionality!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================