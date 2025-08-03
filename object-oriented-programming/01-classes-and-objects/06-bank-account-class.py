"""Question: Create a class named BankAccount with attributes account_number and balance.
Add methods to deposit and withdraw money, and to check the balance.
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


# Step 1: Define the BankAccount class
# ===============================================================================

# Explanation:
# Let's start by creating our BankAccount class. In Python, we use the 'class' keyword 
# followed by the class name. Class names should follow PascalCase convention.

class BankAccount:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic BankAccount class structure


# Step 2: Add the constructor (__init__ method)
# ===============================================================================

# Explanation:
# The __init__ method is called when we create a new instance of the class.
# It's where we initialize the object's attributes. The 'self' parameter refers to the instance being created.
# Note: balance=0 means balance has a default value of 0 if not provided.

class BankAccount:
    def __init__(self, account_number, balance=0):
        # We'll add attribute assignments next
        pass

# What we accomplished in this step:
# - Added the constructor method to initialize new instances


# Step 3: Initialize the attributes
# ===============================================================================

# Explanation:
# Now let's assign the parameters to instance attributes. Each attribute will store 
# the data for this specific instance of the class.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

# What we accomplished in this step:
# - Initialized all necessary attributes for the class


# Step 4: Add the deposit method
# ===============================================================================

# Explanation:
# Now let's add the deposit method that adds money to the account balance.
# This method will modify the balance attribute we defined earlier.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

# What we accomplished in this step:
# - Added the deposit method to increase the balance


# Step 5: Add the withdraw method
# ===============================================================================

# Explanation:
# Now let's add the withdraw method that removes money from the account balance.
# This method includes a check to ensure sufficient funds are available.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# What we accomplished in this step:
# - Added the withdraw method with balance checking


# Step 6: Add the check_balance method
# ===============================================================================

# Explanation:
# Now let's add the check_balance method that returns the current account balance.
# This method allows us to view the current balance without modifying it.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def check_balance(self):
        return self.balance

# What we accomplished in this step:
# - Added the check_balance method to view the current balance


# Step 7: Create an instance and test our class
# ===============================================================================

# Explanation:
# Finally, let's create an instance of our class and test it to make sure everything works correctly.
# This demonstrates how to use the class we just created.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def check_balance(self):
        return self.balance

# Test our class:
account = BankAccount("123456")
account.deposit(1000)
account.withdraw(500)
print(account.check_balance())  # Output: 500

# What we accomplished in this step:
# - Created and tested our complete BankAccount implementation


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