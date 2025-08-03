"""Question: Define a class Mediator that uses the Mediator pattern to coordinate
interactions between multiple objects.
Implement colleagues ColleagueA and ColleagueB that communicate through the mediator.
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
# - What is the Mediator pattern and when is it useful?
# - How does a mediator reduce coupling between objects?
# - How do colleagues communicate through the mediator?
# - What happens when the mediator receives notifications from colleagues?
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


# Step 1: Define the abstract Mediator class
# ===============================================================================

# Explanation:
# Let's start by creating the abstract Mediator class. This defines the interface
# for communication between colleagues.

class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created abstract Mediator class with notify method
# - Used NotImplementedError to enforce implementation in subclasses


# Step 2: Define the base Colleague class
# ===============================================================================

# Explanation:
# Now let's create the base Colleague class. Colleagues hold a reference
# to the mediator and use it to communicate with other colleagues.

class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclasses must implement this method")

class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

# What we accomplished in this step:
# - Created base Colleague class that holds mediator reference
# - All colleagues will communicate through this mediator


# Step 3: Create concrete colleague classes
# ===============================================================================

# Explanation:
# Let's create concrete colleague classes that perform actions and notify
# the mediator about their activities.

class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclasses must implement this method")

class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

class ColleagueA(Colleague):
    def do_a(self):
        print("ColleagueA does A")
        self._mediator.notify(self, "A")

class ColleagueB(Colleague):
    def do_b(self):
        print("ColleagueB does B")
        self._mediator.notify(self, "B")

# What we accomplished in this step:
# - Created ColleagueA and ColleagueB that inherit from Colleague
# - Each colleague notifies the mediator when performing actions


# Step 4: Create concrete mediator
# ===============================================================================

# Explanation:
# Now let's create a concrete mediator that coordinates interactions between
# colleagues based on the events they send.

class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleague_a = None
        self._colleague_b = None

    def set_colleague_a(self, colleague):
        self._colleague_a = colleague

    def set_colleague_b(self, colleague):
        self._colleague_b = colleague

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers B")
            self._colleague_b.do_b()
        elif event == "B":
            print("Mediator reacts on B and triggers A")
            self._colleague_a.do_a()

class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

class ColleagueA(Colleague):
    def do_a(self):
        print("ColleagueA does A")
        self._mediator.notify(self, "A")

class ColleagueB(Colleague):
    def do_b(self):
        print("ColleagueB does B")
        self._mediator.notify(self, "B")

# What we accomplished in this step:
# - Created ConcreteMediator that coordinates colleague interactions
# - Added methods to register colleagues with the mediator
# - Implemented logic to trigger actions based on events


# Step 5: Test our basic Mediator pattern
# ===============================================================================

# Explanation:
# Let's test our Mediator pattern by creating colleagues and observing
# how they interact through the mediator.

class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleague_a = None
        self._colleague_b = None

    def set_colleague_a(self, colleague):
        self._colleague_a = colleague

    def set_colleague_b(self, colleague):
        self._colleague_b = colleague

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers B")
            self._colleague_b.do_b()
        elif event == "B":
            print("Mediator reacts on B and triggers A")
            self._colleague_a.do_a()

class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

class ColleagueA(Colleague):
    def do_a(self):
        print("ColleagueA does A")
        self._mediator.notify(self, "A")

class ColleagueB(Colleague):
    def do_b(self):
        print("ColleagueB does B")
        self._mediator.notify(self, "B")

# Test our basic Mediator pattern:
print("=== Testing Basic Mediator Pattern ===")

mediator = ConcreteMediator()
colleague_a = ColleagueA(mediator)
colleague_b = ColleagueB(mediator)
mediator.set_colleague_a(colleague_a)
mediator.set_colleague_b(colleague_b)

print("Starting with ColleagueA action:")
colleague_a.do_a()

print("\nStarting with ColleagueB action:")
colleague_b.do_b()

# What we accomplished in this step:
# - Created mediator and colleagues
# - Registered colleagues with the mediator
# - Demonstrated how actions trigger chain reactions through the mediator


# Step 6: Enhanced Mediator with chat room example
# ===============================================================================

# Explanation:
# Let's create a more realistic example with a chat room where users
# communicate through a mediator that handles message routing.

class ChatMediator:
    def send_message(self, message, sender):
        raise NotImplementedError("Subclasses must implement this method")

class ChatRoom(ChatMediator):
    def __init__(self, name):
        self.name = name
        self.users = []
        self.message_history = []

    def add_user(self, user):
        self.users.append(user)
        user.set_chat_room(self)
        self.broadcast_system_message(f"{user.name} joined the chat room")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            self.broadcast_system_message(f"{user.name} left the chat room")

    def send_message(self, message, sender):
        timestamp = self._get_timestamp()
        formatted_message = f"[{timestamp}] {sender.name}: {message}"
        self.message_history.append(formatted_message)
        
        # Send to all users except sender
        for user in self.users:
            if user != sender:
                user.receive_message(formatted_message)

    def send_private_message(self, message, sender, recipient_name):
        recipient = self._find_user(recipient_name)
        if recipient:
            timestamp = self._get_timestamp()
            formatted_message = f"[{timestamp}] {sender.name} (private): {message}"
            recipient.receive_message(formatted_message)
            sender.receive_message(f"[{timestamp}] You (private to {recipient_name}): {message}")
        else:
            sender.receive_message(f"User '{recipient_name}' not found in chat room")

    def broadcast_system_message(self, message):
        timestamp = self._get_timestamp()
        formatted_message = f"[{timestamp}] SYSTEM: {message}"
        self.message_history.append(formatted_message)
        
        for user in self.users:
            user.receive_message(formatted_message)

    def _find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().strftime("%H:%M:%S")

    def get_message_history(self):
        return self.message_history

    def get_user_list(self):
        return [user.name for user in self.users]

class ChatUser:
    def __init__(self, name):
        self.name = name
        self.chat_room = None
        self.received_messages = []

    def set_chat_room(self, chat_room):
        self.chat_room = chat_room

    def send_message(self, message):
        if self.chat_room:
            self.chat_room.send_message(message, self)
        else:
            print(f"{self.name}: Not connected to any chat room")

    def send_private_message(self, message, recipient_name):
        if self.chat_room:
            self.chat_room.send_private_message(message, self, recipient_name)
        else:
            print(f"{self.name}: Not connected to any chat room")

    def receive_message(self, message):
        self.received_messages.append(message)
        print(f"{self.name} received: {message}")

    def leave_chat(self):
        if self.chat_room:
            self.chat_room.remove_user(self)
            self.chat_room = None

    def get_message_history(self):
        return self.received_messages

# Test enhanced Mediator pattern:
print("\n=== Enhanced Mediator Pattern with Chat Room ===")

# Create chat room and users
chat_room = ChatRoom("General Discussion")
alice = ChatUser("Alice")
bob = ChatUser("Bob")
charlie = ChatUser("Charlie")

# Users join the chat room
print("Users joining chat room:")
chat_room.add_user(alice)
chat_room.add_user(bob)
chat_room.add_user(charlie)

print(f"\nActive users: {chat_room.get_user_list()}")

# Users send messages
print("\nUsers chatting:")
alice.send_message("Hello everyone!")
bob.send_message("Hi Alice! How are you?")
charlie.send_message("Good morning!")

# Private message
print("\nPrivate messaging:")
alice.send_private_message("Can we discuss the project later?", "Bob")

# User leaves
print("\nUser leaving:")
charlie.leave_chat()

# More messages
print("\nContinued conversation:")
bob.send_message("Sure Alice, let's talk after lunch")
alice.send_message("Perfect!")

print(f"\nFinal active users: {chat_room.get_user_list()}")

# What we accomplished in this step:
# - Created realistic chat room application using Mediator pattern
# - Demonstrated how mediator handles complex interactions (public/private messages)
# - Showed user management and message history features
# - Illustrated how mediator reduces coupling between chat participants


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Mediator pattern and its benefits
# - Reducing coupling between objects through centralized communication
# - Creating mediators that coordinate complex interactions
# - Implementing realistic applications like chat rooms
# - Managing collections of objects through a mediator
# - Understanding when to use Mediator vs other patterns
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating an air traffic control mediator!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
