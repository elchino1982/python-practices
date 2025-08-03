"""Question: Define a class named Book with attributes title, author, and pages.
Add a method to check if the book is a novel (more than 100 pages).
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


# Step 1: Define the Book class
# ===============================================================================

# Explanation:
# Let's start by creating our Book class. In Python, we use the 'class' keyword 
# followed by the class name. Class names should follow PascalCase convention.

class Book:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Book class structure


# Step 2: Add the constructor (__init__ method)
# ===============================================================================

# Explanation:
# The __init__ method is called when we create a new instance of the class.
# It's where we initialize the object's attributes. The 'self' parameter refers to the instance being created.

class Book:
    def __init__(self, title, author, pages):
        # We'll add attribute assignments next
        pass

# What we accomplished in this step:
# - Added the constructor method to initialize new instances


# Step 3: Initialize the attributes
# ===============================================================================

# Explanation:
# Now let's assign the parameters to instance attributes. Each attribute will store 
# the data for this specific instance of the class.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# What we accomplished in this step:
# - Initialized all necessary attributes for the class


# Step 4: Add the is_novel method
# ===============================================================================

# Explanation:
# Now let's add the is_novel method that determines if a book is a novel based on page count.
# This method will use the pages attribute we defined earlier to make the determination.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def is_novel(self):
        return self.pages > 100

# What we accomplished in this step:
# - Added the is_novel method with page count logic


# Step 5: Create an instance and test our class
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our class and test it to make sure everything works correctly.
# This demonstrates how to use the class we just created.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def is_novel(self):
        return self.pages > 100

# Test our class:
book = Book("1984", "George Orwell", 328)
print(book.is_novel())  # Output: True

# What we accomplished in this step:
# - Created and tested our complete Book implementation


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
