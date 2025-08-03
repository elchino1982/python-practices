"""Question: Define a class Memento that uses the Memento pattern to capture
and restore an object's state.
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
# - What is the Memento pattern and when is it useful?
# - What are the three main components: Memento, Originator, and Caretaker?
# - How do you capture an object's state without violating encapsulation?
# - How do you restore a previous state from a memento?
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


# Step 1: Define the Memento class
# ===============================================================================

# Explanation:
# Let's start by creating the Memento class. This class stores a snapshot
# of an object's state at a particular point in time.

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

# What we accomplished in this step:
# - Created Memento class to store object state
# - Added constructor to initialize with state
# - Added getter method to retrieve stored state


# Step 2: Define the Originator class
# ===============================================================================

# Explanation:
# The Originator is the object whose state we want to save and restore.
# It can create mementos of its current state and restore from mementos.

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

# What we accomplished in this step:
# - Created Originator class that holds the state we want to save/restore
# - Added constructor to initialize with initial state


# Step 3: Add state management methods to Originator
# ===============================================================================

# Explanation:
# The Originator needs methods to save its current state to a memento
# and restore its state from a memento.

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

# What we accomplished in this step:
# - Added save_state method to create memento snapshots
# - Added restore_state method to restore from mementos
# - Added getter and setter for current state


# Step 4: Test our basic Memento implementation
# ===============================================================================

# Explanation:
# Let's test our Memento pattern by saving state, changing it, and then
# restoring the previous state.

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Test our basic Memento pattern:
print("=== Testing Basic Memento Pattern ===")

originator = Originator("Initial State")
print(f"Initial state: {originator.get_state()}")

# Save the current state
memento1 = originator.save_state()
print(f"Saved state to memento1")

# Change the state
originator.set_state("Modified State")
print(f"Changed state to: {originator.get_state()}")

# Save another state
memento2 = originator.save_state()
print(f"Saved state to memento2")

# Change state again
originator.set_state("Final State")
print(f"Changed state to: {originator.get_state()}")

# Restore from memento2
originator.restore_state(memento2)
print(f"Restored from memento2: {originator.get_state()}")

# Restore from memento1
originator.restore_state(memento1)
print(f"Restored from memento1: {originator.get_state()}")

# What we accomplished in this step:
# - Created originator with initial state
# - Saved multiple states as mementos
# - Demonstrated state restoration from different mementos
# - Verified that pattern works correctly


# Step 5: Enhanced Memento with complex state
# ===============================================================================

# Explanation:
# Let's create a more realistic example with a text editor that can
# save and restore its content, cursor position, and formatting.

class TextEditorMemento:
    def __init__(self, content, cursor_position, font_size):
        self._content = content
        self._cursor_position = cursor_position
        self._font_size = font_size

    def get_content(self):
        return self._content

    def get_cursor_position(self):
        return self._cursor_position

    def get_font_size(self):
        return self._font_size

class TextEditor:
    def __init__(self):
        self.content = ""
        self.cursor_position = 0
        self.font_size = 12

    def type_text(self, text):
        """Add text at cursor position"""
        self.content = (self.content[:self.cursor_position] + 
                       text + 
                       self.content[self.cursor_position:])
        self.cursor_position += len(text)

    def set_cursor_position(self, position):
        """Set cursor position"""
        self.cursor_position = max(0, min(position, len(self.content)))

    def set_font_size(self, size):
        """Set font size"""
        self.font_size = size

    def save_state(self):
        """Create memento of current state"""
        return TextEditorMemento(self.content, self.cursor_position, self.font_size)

    def restore_state(self, memento):
        """Restore state from memento"""
        self.content = memento.get_content()
        self.cursor_position = memento.get_cursor_position()
        self.font_size = memento.get_font_size()

    def get_state_info(self):
        """Get current state information"""
        return {
            'content': self.content,
            'cursor_position': self.cursor_position,
            'font_size': self.font_size,
            'content_length': len(self.content)
        }

# Test enhanced memento:
print("\n=== Enhanced Memento with Text Editor ===")

editor = TextEditor()

# Initial state
print("Initial state:")
print(f"  {editor.get_state_info()}")

# Type some text
editor.type_text("Hello World")
editor.set_font_size(14)
checkpoint1 = editor.save_state()
print("\nAfter typing 'Hello World' and setting font to 14:")
print(f"  {editor.get_state_info()}")

# Move cursor and add more text
editor.set_cursor_position(5)
editor.type_text(" Beautiful")
checkpoint2 = editor.save_state()
print("\nAfter inserting ' Beautiful' at position 5:")
print(f"  {editor.get_state_info()}")

# Change font and add more text
editor.set_font_size(16)
editor.set_cursor_position(len(editor.content))
editor.type_text("!")
checkpoint3 = editor.save_state()
print("\nAfter changing font to 16 and adding '!':")
print(f"  {editor.get_state_info()}")

# Restore to checkpoint2
editor.restore_state(checkpoint2)
print("\nRestored to checkpoint2:")
print(f"  {editor.get_state_info()}")

# Restore to checkpoint1
editor.restore_state(checkpoint1)
print("\nRestored to checkpoint1:")
print(f"  {editor.get_state_info()}")

# What we accomplished in this step:
# - Created realistic text editor with complex state
# - Demonstrated memento with multiple attributes
# - Showed practical use case for undo functionality
# - Verified state restoration with complex objects


# Step 6: Caretaker for managing multiple mementos
# ===============================================================================

# Explanation:
# Let's create a Caretaker class that manages multiple mementos and
# provides undo/redo functionality like a real application.

class MementoCaretaker:
    def __init__(self):
        self._mementos = []
        self._current_index = -1

    def save_memento(self, memento):
        """Save a new memento and update current position"""
        # Remove any mementos after current position (for new branch)
        self._mementos = self._mementos[:self._current_index + 1]
        # Add new memento
        self._mementos.append(memento)
        self._current_index += 1

    def undo(self):
        """Get previous memento"""
        if self._current_index > 0:
            self._current_index -= 1
            return self._mementos[self._current_index]
        return None

    def redo(self):
        """Get next memento"""
        if self._current_index < len(self._mementos) - 1:
            self._current_index += 1
            return self._mementos[self._current_index]
        return None

    def can_undo(self):
        """Check if undo is possible"""
        return self._current_index > 0

    def can_redo(self):
        """Check if redo is possible"""
        return self._current_index < len(self._mementos) - 1

    def get_history_info(self):
        """Get information about memento history"""
        return {
            'total_mementos': len(self._mementos),
            'current_index': self._current_index,
            'can_undo': self.can_undo(),
            'can_redo': self.can_redo()
        }

class Document:
    def __init__(self):
        self.title = "Untitled"
        self.content = ""
        self.word_count = 0

    def set_title(self, title):
        self.title = title

    def add_content(self, text):
        self.content += text
        self.word_count = len(self.content.split())

    def save_state(self):
        """Create memento of current document state"""
        return {
            'title': self.title,
            'content': self.content,
            'word_count': self.word_count
        }

    def restore_state(self, memento):
        """Restore document state from memento"""
        self.title = memento['title']
        self.content = memento['content']
        self.word_count = memento['word_count']

    def get_info(self):
        return f"Title: '{self.title}', Words: {self.word_count}, Content: '{self.content[:50]}...'"

# Test caretaker with undo/redo:
print("\n=== Caretaker with Undo/Redo Functionality ===")

document = Document()
caretaker = MementoCaretaker()

# Save initial state
caretaker.save_memento(document.save_state())
print(f"Initial: {document.get_info()}")

# Make changes and save states
document.set_title("My Document")
caretaker.save_memento(document.save_state())
print(f"After setting title: {document.get_info()}")

document.add_content("This is the first paragraph. ")
caretaker.save_memento(document.save_state())
print(f"After adding content: {document.get_info()}")

document.add_content("This is the second paragraph. ")
caretaker.save_memento(document.save_state())
print(f"After adding more content: {document.get_info()}")

# Test undo functionality
print(f"\nHistory info: {caretaker.get_history_info()}")

print("\nUndo operations:")
while caretaker.can_undo():
    memento = caretaker.undo()
    if memento:
        document.restore_state(memento)
        print(f"Undid to: {document.get_info()}")

# Test redo functionality
print("\nRedo operations:")
while caretaker.can_redo():
    memento = caretaker.redo()
    if memento:
        document.restore_state(memento)
        print(f"Redid to: {document.get_info()}")

# What we accomplished in this step:
# - Created Caretaker class to manage memento history
# - Implemented undo/redo functionality
# - Demonstrated practical document editing scenario
# - Showed how to manage multiple mementos efficiently


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Memento pattern and its three components
# - Implementing state capture and restoration without breaking encapsulation
# - Creating mementos for complex objects with multiple attributes
# - Building caretaker classes for undo/redo functionality
# - Managing memento history and navigation
# - Understanding practical applications like text editors and document systems
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a game state save system!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
