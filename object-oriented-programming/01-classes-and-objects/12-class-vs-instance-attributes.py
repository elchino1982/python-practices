"""Question: Create a class Document with a class attribute document_count 
to keep track of the number of documents created.
Add methods to read and write content to the document.
Use class methods to get the document count.
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
# - What are class attributes? (shared by all instances)
# - When should you increment the counter? (in __init__)
# - How do you access class attributes? (ClassName.attribute or cls.attribute)
# - What's the difference between instance and class methods?
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


# Step 1: Define the Document class with class attribute
# ===============================================================================

# Explanation:
# Let's start by creating our Document class with a class attribute to track
# the total number of documents created. Class attributes are shared by all instances.

class Document:
    document_count = 0

# What we accomplished in this step:
# - Created Document class with class attribute document_count


# Step 2: Add constructor that increments the counter
# ===============================================================================

# Explanation:
# The __init__ method should increment the document count each time a new
# document is created. We'll also initialize the document with title and content.

class Document:
    document_count = 0

    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        Document.document_count += 1

# What we accomplished in this step:
# - Added constructor that increments document_count
# - Initialized title and content attributes


# Step 3: Add read method
# ===============================================================================

# Explanation:
# The read method should return the current content of the document.
# This provides a clean interface for accessing document content.

class Document:
    document_count = 0

    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        Document.document_count += 1

    def read(self):
        return self.content

# What we accomplished in this step:
# - Added read method to access document content


# Step 4: Add write method
# ===============================================================================

# Explanation:
# The write method should update the document's content.
# We can also add some additional functionality like tracking modifications.

class Document:
    document_count = 0

    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        self.modified = False
        Document.document_count += 1

    def read(self):
        return self.content

    def write(self, content):
        self.content = content
        self.modified = True

# What we accomplished in this step:
# - Added write method to update document content
# - Added modified flag to track changes


# Step 5: Add class method to get document count
# ===============================================================================

# Explanation:
# Class methods take 'cls' as the first parameter and can access class attributes.
# This provides a clean interface for accessing the document count.

class Document:
    document_count = 0

    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        self.modified = False
        Document.document_count += 1

    def read(self):
        return self.content

    def write(self, content):
        self.content = content
        self.modified = True

    @classmethod
    def get_document_count(cls):
        return cls.document_count

# What we accomplished in this step:
# - Added class method to access document count


# Step 6: Add additional useful methods
# ===============================================================================

# Explanation:
# Let's add some additional methods to make our Document class more useful,
# including methods to append content and clear the document.

class Document:
    document_count = 0

    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        self.modified = False
        Document.document_count += 1

    def read(self):
        return self.content

    def write(self, content):
        self.content = content
        self.modified = True

    def append(self, content):
        self.content += content
        self.modified = True

    def clear(self):
        self.content = ""
        self.modified = True

    def get_length(self):
        return len(self.content)

    @classmethod
    def get_document_count(cls):
        return cls.document_count

    @classmethod
    def reset_count(cls):
        cls.document_count = 0

# What we accomplished in this step:
# - Added append method to add content
# - Added clear method to empty document
# - Added get_length method for content length
# - Added reset_count class method for testing


# Step 7: Add string representation and test the class
# ===============================================================================

# Explanation:
# Let's add a __str__ method and test our complete Document implementation
# to make sure the class attribute tracking works correctly.

class Document:
    document_count = 0

    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        self.modified = False
        Document.document_count += 1

    def read(self):
        return self.content

    def write(self, content):
        self.content = content
        self.modified = True

    def append(self, content):
        self.content += content
        self.modified = True

    def clear(self):
        self.content = ""
        self.modified = True

    def get_length(self):
        return len(self.content)

    @classmethod
    def get_document_count(cls):
        return cls.document_count

    @classmethod
    def reset_count(cls):
        cls.document_count = 0

    def __str__(self):
        status = "Modified" if self.modified else "Unmodified"
        return f"Document(title='{self.title}', length={self.get_length()}, {status})"

# Test our class:
print("Testing Document class with class attribute tracking:")

print(f"Initial document count: {Document.get_document_count()}")

# Create first document
doc1 = Document("Report 1", "Initial content for report 1")
print(f"After creating doc1: {Document.get_document_count()}")
print(f"Doc1: {doc1}")

# Create second document
doc2 = Document("Report 2")
print(f"After creating doc2: {Document.get_document_count()}")
print(f"Doc2: {doc2}")

# Test read and write operations
print(f"\nReading doc1: '{doc1.read()}'")

doc2.write("This is the content for report 2")
print(f"After writing to doc2: {doc2}")

# Create third document
doc3 = Document("Report 3", "Some initial content")
print(f"After creating doc3: {Document.get_document_count()}")

# Test append functionality
doc3.append(" - Additional content added")
print(f"After appending to doc3: {doc3}")
print(f"Doc3 content: '{doc3.read()}'")

# Test that count is shared across all instances
print(f"\nFinal document count: {Document.get_document_count()}")
print(f"Count accessed via doc1: {doc1.get_document_count()}")
print(f"Count accessed via doc2: {doc2.get_document_count()}")
print(f"Count accessed via doc3: {doc3.get_document_count()}")

# What we accomplished in this step:
# - Created and tested our complete Document implementation
# - Demonstrated class attribute sharing across instances


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Class attributes vs instance attributes
# - Automatic counting with class attributes
# - Class methods for accessing shared data
# - Document management operations (read, write, append, clear)
# - Shared state across all instances of a class
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding document categories or creation timestamps!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================