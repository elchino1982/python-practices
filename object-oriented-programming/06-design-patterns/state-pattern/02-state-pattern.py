"""Question: Implement a class State that uses the State pattern to
change its behavior when its internal state changes.
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
# - What is the State pattern and when is it useful?
# - How do you create an abstract base state class?
# - How do concrete states implement different behaviors?
# - How does the context delegate behavior to the current state?
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


# Step 1: Define the abstract State class
# ===============================================================================

# Explanation:
# Let's start by creating the abstract State class. This defines the interface
# that all concrete states must implement.

class State:
    def handle(self):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created abstract State class with handle method
# - Used NotImplementedError to enforce implementation in subclasses


# Step 2: Create concrete state classes
# ===============================================================================

# Explanation:
# Now let's create concrete state classes that implement different behaviors.
# Each state will handle requests differently.

class State:
    def handle(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteStateA(State):
    def handle(self):
        return "State A handling request"

class ConcreteStateB(State):
    def handle(self):
        return "State B handling request"

# What we accomplished in this step:
# - Created ConcreteStateA and ConcreteStateB classes
# - Each implements the handle method with different behavior


# Step 3: Create the Context class
# ===============================================================================

# Explanation:
# The Context class holds a reference to the current state and delegates
# behavior to that state. It can also change states.

class State:
    def handle(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteStateA(State):
    def handle(self):
        return "State A handling request"

class ConcreteStateB(State):
    def handle(self):
        return "State B handling request"

class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        return self._state.handle()

# What we accomplished in this step:
# - Created Context class that holds current state
# - Added methods to change state and delegate requests


# Step 4: Test our basic State pattern
# ===============================================================================

# Explanation:
# Let's test our State pattern by creating a context with different states
# and observing how behavior changes.

class State:
    def handle(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteStateA(State):
    def handle(self):
        return "State A handling request"

class ConcreteStateB(State):
    def handle(self):
        return "State B handling request"

class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        return self._state.handle()

# Test our basic State pattern:
print("=== Testing Basic State Pattern ===")

context = Context(ConcreteStateA())
print(f"Initial state: {context.request()}")

context.set_state(ConcreteStateB())
print(f"After changing to State B: {context.request()}")

context.set_state(ConcreteStateA())
print(f"After changing back to State A: {context.request()}")

# What we accomplished in this step:
# - Created context with initial state
# - Demonstrated state changes and different behaviors
# - Verified that pattern works correctly


# Step 5: Enhanced State pattern with state transitions
# ===============================================================================

# Explanation:
# Let's create a more realistic example with a traffic light that automatically
# transitions between states and has different behaviors for each state.

class TrafficLightState:
    def handle_request(self, context):
        raise NotImplementedError("Subclasses must implement this method")
    
    def next_state(self, context):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_color(self):
        raise NotImplementedError("Subclasses must implement this method")

class RedState(TrafficLightState):
    def handle_request(self, context):
        return "RED: Stop! Do not proceed."
    
    def next_state(self, context):
        print("RED -> GREEN: Light changing to green")
        context.set_state(GreenState())
    
    def get_color(self):
        return "RED"

class YellowState(TrafficLightState):
    def handle_request(self, context):
        return "YELLOW: Caution! Prepare to stop."
    
    def next_state(self, context):
        print("YELLOW -> RED: Light changing to red")
        context.set_state(RedState())
    
    def get_color(self):
        return "YELLOW"

class GreenState(TrafficLightState):
    def handle_request(self, context):
        return "GREEN: Go! Proceed with caution."
    
    def next_state(self, context):
        print("GREEN -> YELLOW: Light changing to yellow")
        context.set_state(YellowState())
    
    def get_color(self):
        return "GREEN"

class TrafficLight:
    def __init__(self):
        self._state = RedState()  # Start with red
        self.cycle_count = 0

    def set_state(self, state):
        self._state = state

    def get_instruction(self):
        return self._state.handle_request(self)

    def get_current_color(self):
        return self._state.get_color()

    def change_light(self):
        self._state.next_state(self)
        self.cycle_count += 1

    def get_status(self):
        return {
            'color': self.get_current_color(),
            'instruction': self.get_instruction(),
            'cycle_count': self.cycle_count
        }

# Test enhanced State pattern:
print("\n=== Enhanced State Pattern with Traffic Light ===")

traffic_light = TrafficLight()

print("Traffic light simulation:")
for i in range(8):  # Go through multiple cycles
    status = traffic_light.get_status()
    print(f"Cycle {i+1}: {status['color']} - {status['instruction']}")
    traffic_light.change_light()

print(f"\nTotal cycles completed: {traffic_light.cycle_count}")

# What we accomplished in this step:
# - Created realistic traffic light with automatic state transitions
# - Each state knows how to transition to the next state
# - Demonstrated state-specific behavior and transitions
# - Added cycle counting and status reporting


# Step 6: State pattern with conditional transitions
# ===============================================================================

# Explanation:
# Let's create a more complex example with a document workflow that has
# conditional state transitions based on user roles and document content.

class DocumentState:
    def edit(self, context, user_role):
        raise NotImplementedError()
    
    def submit(self, context, user_role):
        raise NotImplementedError()
    
    def approve(self, context, user_role):
        raise NotImplementedError()
    
    def reject(self, context, user_role):
        raise NotImplementedError()
    
    def get_status(self):
        raise NotImplementedError()

class DraftState(DocumentState):
    def edit(self, context, user_role):
        if user_role in ["author", "editor"]:
            return "Document edited successfully"
        return "Access denied: Cannot edit document"
    
    def submit(self, context, user_role):
        if user_role in ["author", "editor"]:
            context.set_state(UnderReviewState())
            return "Document submitted for review"
        return "Access denied: Cannot submit document"
    
    def approve(self, context, user_role):
        return "Cannot approve: Document is still in draft"
    
    def reject(self, context, user_role):
        return "Cannot reject: Document is still in draft"
    
    def get_status(self):
        return "DRAFT"

class UnderReviewState(DocumentState):
    def edit(self, context, user_role):
        return "Cannot edit: Document is under review"
    
    def submit(self, context, user_role):
        return "Document is already submitted"
    
    def approve(self, context, user_role):
        if user_role == "reviewer":
            context.set_state(ApprovedState())
            return "Document approved"
        return "Access denied: Only reviewers can approve"
    
    def reject(self, context, user_role):
        if user_role == "reviewer":
            context.set_state(DraftState())
            return "Document rejected, returned to draft"
        return "Access denied: Only reviewers can reject"
    
    def get_status(self):
        return "UNDER_REVIEW"

class ApprovedState(DocumentState):
    def edit(self, context, user_role):
        return "Cannot edit: Document is approved"
    
    def submit(self, context, user_role):
        return "Document is already approved"
    
    def approve(self, context, user_role):
        return "Document is already approved"
    
    def reject(self, context, user_role):
        if user_role == "admin":
            context.set_state(DraftState())
            return "Document rejected by admin, returned to draft"
        return "Access denied: Only admins can reject approved documents"
    
    def get_status(self):
        return "APPROVED"

class Document:
    def __init__(self, title):
        self.title = title
        self._state = DraftState()
        self.history = []

    def set_state(self, state):
        old_status = self._state.get_status()
        self._state = state
        new_status = self._state.get_status()
        self.history.append(f"{old_status} -> {new_status}")

    def edit(self, user_role):
        result = self._state.edit(self, user_role)
        self.history.append(f"Edit attempt by {user_role}: {result}")
        return result

    def submit(self, user_role):
        result = self._state.submit(self, user_role)
        self.history.append(f"Submit attempt by {user_role}: {result}")
        return result

    def approve(self, user_role):
        result = self._state.approve(self, user_role)
        self.history.append(f"Approve attempt by {user_role}: {result}")
        return result

    def reject(self, user_role):
        result = self._state.reject(self, user_role)
        self.history.append(f"Reject attempt by {user_role}: {result}")
        return result

    def get_status(self):
        return self._state.get_status()

    def get_history(self):
        return self.history

# Test document workflow:
print("\n=== Document Workflow with Conditional State Transitions ===")

doc = Document("Project Proposal")

print(f"Document: {doc.title}")
print(f"Initial status: {doc.get_status()}")

# Author edits and submits
print(f"\n1. {doc.edit('author')}")
print(f"2. {doc.submit('author')}")
print(f"   Status: {doc.get_status()}")

# Editor tries to edit (should fail)
print(f"\n3. {doc.edit('editor')}")

# Reviewer approves
print(f"4. {doc.approve('reviewer')}")
print(f"   Status: {doc.get_status()}")

# Author tries to edit approved doc (should fail)
print(f"\n5. {doc.edit('author')}")

# Admin rejects approved doc
print(f"6. {doc.reject('admin')}")
print(f"   Status: {doc.get_status()}")

print(f"\nDocument history:")
for entry in doc.get_history():
    print(f"  {entry}")

# What we accomplished in this step:
# - Created complex document workflow with role-based permissions
# - Implemented conditional state transitions
# - Added history tracking for audit trails
# - Demonstrated real-world state pattern usage


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the State pattern and its benefits
# - Creating abstract state classes with common interfaces
# - Implementing concrete states with different behaviors
# - Building context classes that delegate to current state
# - Creating automatic state transitions
# - Implementing conditional transitions based on business rules
# - Adding history tracking and audit capabilities
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a game character with different states!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
