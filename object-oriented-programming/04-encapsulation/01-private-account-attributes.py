"""Question: Create a class named Account with attributes account_number
and balance. Add methods to deposit, withdraw, and transfer money to another account.
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
# - What attributes does the Account class need?
# - How do you handle insufficient funds when withdrawing?
# - How does transfer work? (hint: it's like withdraw from one and deposit to another)
# - Should you allow negative balances?
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


# Step 1: Define the Account class
# ===============================================================================

# Explanation:
# Let's start by creating our Account class. This class will represent
# a bank account with basic banking operations.

class Account:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Account class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The __init__ method initializes the Account with account_number and balance.
# We'll set a default balance of 0 if none is provided.

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

# What we accomplished in this step:
# - Added constructor to initialize account_number and balance
# - Used default parameter for balance


# Step 3: Add the deposit method
# ===============================================================================

# Explanation:
# The deposit method adds money to the account. This is straightforward -
# we just add the amount to the current balance.

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# What we accomplished in this step:
# - Added deposit method to add money to the account


# Step 4: Add the withdraw method
# ===============================================================================

# Explanation:
# The withdraw method removes money from the account, but we need to check
# if there are sufficient funds first to prevent negative balances.

class Account:
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
# - Added withdraw method with insufficient funds checking


# Step 5: Add the transfer method
# ===============================================================================

# Explanation:
# The transfer method moves money from this account to another account.
# It's essentially a withdraw from this account and a deposit to the other.

class Account:
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

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
        else:
            print("Insufficient funds")

# What we accomplished in this step:
# - Added transfer method that uses existing withdraw and deposit methods


# Step 6: Create instances and test our class
# ===============================================================================

# Explanation:
# Finally, let's create instances of our Account class and test all the banking operations
# to make sure everything works correctly.

class Account:
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

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
        else:
            print("Insufficient funds")

# Test our class:
# Create two accounts
acc1 = Account("12345", 1000)
acc2 = Account("67890", 500)

print(f"Account 1 initial balance: ${acc1.balance}")
print(f"Account 2 initial balance: ${acc2.balance}")

# Test deposit
acc1.deposit(200)
print(f"Account 1 after $200 deposit: ${acc1.balance}")

# Test withdraw
acc1.withdraw(150)
print(f"Account 1 after $150 withdrawal: ${acc1.balance}")

# Test transfer
acc1.transfer(300, acc2)
print(f"Account 1 after $300 transfer: ${acc1.balance}")
print(f"Account 2 after receiving $300: ${acc2.balance}")

# Test insufficient funds
acc1.withdraw(2000)  # Should print "Insufficient funds"

# What we accomplished in this step:
# - Created and tested our complete Account implementation
# - Demonstrated all banking operations working together


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Class design for real-world objects (bank accounts)
# - Method interaction (transfer uses withdraw and deposit)
# - Input validation and error handling
# - Object interaction (accounts working with other accounts)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding interest calculation or account history!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================