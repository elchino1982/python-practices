"""Question: Define a class named Library with attributes name and books
(a list of book titles). Add methods to add a book, remove a book, and list all books.
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
# - What attributes does the class need?
# - What methods should you implement?
# - How do the methods interact with the attributes?
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


# Step 1: Define the Library class
# ===============================================================================

# Explanation:
# Let's start by creating our Library class. In Python, we use the 'class' keyword 
# followed by the class name. Class names should follow PascalCase convention.

class Library:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Library class structure


# Step 2: Add the constructor (__init__ method)
# ===============================================================================

# Explanation:
# The __init__ method is called when we create a new instance of the class.
# It's where we initialize the object's attributes. The 'self' parameter refers to the instance being created.

class Library:
    def __init__(self, name):
        # We'll add attribute assignments next
        pass

# What we accomplished in this step:
# - Added the constructor method to initialize new instances


# Step 3: Initialize the attributes
# ===============================================================================

# Explanation:
# Now let's assign the parameters to instance attributes. Each attribute will store 
# the data for this specific instance of the class.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

# What we accomplished in this step:
# - Initialized the name and empty books list attributes


# Step 4: Add the add_book method
# ===============================================================================

# Explanation:
# Now let's add the add_book method that adds a new book to the library's collection.
# This method will modify the books list attribute we defined earlier.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book_title):
        self.books.append(book_title)

# What we accomplished in this step:
# - Added the add_book method to add books to the collection


# Step 5: Add the remove_book method
# ===============================================================================

# Explanation:
# Now let's add the remove_book method that removes a book from the library's collection.
# This method includes a check to ensure the book exists before trying to remove it.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book_title):
        self.books.append(book_title)
    
    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)

# What we accomplished in this step:
# - Added the remove_book method with existence checking


# Step 6: Add the list_books method
# ===============================================================================

# Explanation:
# Now let's add the list_books method that returns all books in the library's collection.
# This method allows us to view the current collection without modifying it.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book_title):
        self.books.append(book_title)
    
    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
    
    def list_books(self):
        return self.books

# What we accomplished in this step:
# - Added the list_books method to view the collection


# Step 7: Create an instance and test our class
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our class and test it to make sure everything works correctly.
# This demonstrates how to use the class we just created.

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book_title):
        self.books.append(book_title)
    
    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
    
    def list_books(self):
        return self.books

# Test our class:
library = Library("City Library")
library.add_book("1984")
library.add_book("To Kill a Mockingbird")
library.remove_book("1984")
print(library.list_books())  # Output: ['To Kill a Mockingbird']

# What we accomplished in this step:
# - Created and tested our complete Library implementation


# ===============================================================================
# CONGRATULATIONS! 
# 
# You've successfully completed the step-by-step solution!
# 
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications
# 
# Remember: The best way to learn is by doing!
# ===============================================================================