"""Question: Create a class BankAccount with protected attributes _account_number
and _balance. Add methods to deposit, withdraw, and check the balance.
Use encapsulation to ensure balance cannot be negative.
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
# - What are protected attributes? (attributes starting with _)
# - How do you prevent negative balances? (validation in withdraw method)
# - What should deposit method validate? (positive amounts)
# - How do you provide safe access to balance? (getter method)
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


# Step 1: Define the BankAccount class with protected attributes
# ===============================================================================

# Explanation:
# Let's start by creating our BankAccount class with protected attributes.
# Protected attributes start with _ and are meant for internal use.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

# What we accomplished in this step:
# - Created BankAccount class with protected attributes
# - Set default balance to 0 if not provided


# Step 2: Add deposit method with validation
# ===============================================================================

# Explanation:
# The deposit method should add money to the account, but only if the amount is positive.
# We use encapsulation to protect the balance from invalid operations.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

# What we accomplished in this step:
# - Added deposit method with positive amount validation


# Step 3: Add withdraw method with balance protection
# ===============================================================================

# Explanation:
# The withdraw method should remove money from the account, but only if there are sufficient funds.
# This prevents the balance from becoming negative.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds")

# What we accomplished in this step:
# - Added withdraw method with balance protection
# - Prevents negative balances through validation


# Step 4: Add method to check balance
# ===============================================================================

# Explanation:
# The get_balance method provides safe access to the protected balance attribute.
# This follows encapsulation principles by controlling access to internal data.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

# What we accomplished in this step:
# - Added get_balance method for safe balance access


# Step 5: Add method to get account number
# ===============================================================================

# Explanation:
# Let's also add a method to safely access the account number.
# This completes our encapsulation by providing controlled access to all attributes.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

# What we accomplished in this step:
# - Added get_account_number method for safe account number access


# Step 6: Create instances and test our bank account
# ===============================================================================

# Explanation:
# Finally, let's create instances of our BankAccount class and test all operations
# to make sure encapsulation and validation work correctly.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

# Test our class:
account = BankAccount("12345", 1000)

print(f"Account Number: {account.get_account_number()}")
print(f"Initial Balance: ${account.get_balance()}")

# Test deposit
account.deposit(500)

# Test withdrawal with sufficient funds
account.withdraw(200)

# Test withdrawal with insufficient funds
account.withdraw(2000)

# Test invalid operations
account.deposit(-100)
account.withdraw(-50)

print(f"Final Balance: ${account.get_balance()}")

# What we accomplished in this step:
# - Created and tested our complete BankAccount implementation
# - Demonstrated encapsulation and data protection


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Protected attributes (underscore convention)
# - Encapsulation principles
# - Data validation and protection
# - Safe access methods for internal data
# - Business logic implementation (banking rules)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding interest calculation or transaction history!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================