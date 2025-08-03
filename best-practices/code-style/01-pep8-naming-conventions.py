"""Question: Demonstrate PEP8 naming conventions for Python code.

Create examples that showcase proper naming conventions for:
1. Variables and functions (snake_case)
2. Classes (PascalCase)
3. Constants (UPPER_CASE)
4. Private attributes (leading underscore)
5. Protected attributes (single leading underscore)
6. Special methods (dunder methods)
7. Module and package names
8. Descriptive naming practices

Requirements:
1. Show correct vs incorrect naming examples
2. Demonstrate different naming contexts
3. Include comments explaining the conventions
4. Show real-world examples of good naming

Example usage:
    user_manager = UserManager()
    MAX_RETRY_COUNT = 3
    _private_method()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read PEP8 documentation
# - Think about readability and clarity
# - Consider the context of each name
# - Practice with real examples
# - Remember that names should be descriptive
#
# Remember: Good naming is one of the hardest parts of programming!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)




# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What makes a name readable?
# - When to use different naming conventions?
# - How to balance brevity with clarity?
# - What are the PEP8 rules for each type of identifier?
#
# Remember: Consistency is key!


# ===============================================================================
#                           STEP-BY-STEP SOLUTION
# ===============================================================================
#
# CLASSROOM-STYLE WALKTHROUGH
#
# Let's explore PEP8 naming conventions step by step, just like in a programming class!
# Each step builds upon the previous one, so you can follow along and understand
# the complete thought process.
#
# ===============================================================================


# Step 1: Basic variable and function naming (snake_case)
# ===============================================================================

# Explanation:
# Variables and functions should use snake_case - lowercase with underscores
# separating words. This makes names readable and follows Python conventions.

# ✅ GOOD: Variables with descriptive snake_case names
user_name = "john_doe"
total_price = 99.99
is_authenticated = True
shopping_cart_items = []
current_user_id = 12345

# ✅ GOOD: Functions with descriptive snake_case names
def calculate_total_price(items):
    """Calculate the total price of items in cart."""
    return sum(item.price for item in items)

def validate_user_credentials(username, password):
    """Validate user login credentials."""
    # Implementation here
    pass

def send_email_notification(recipient, subject, message):
    """Send email notification to user."""
    # Implementation here
    pass

# ❌ BAD: Avoid these naming patterns
userName = "bad"  # camelCase (use in JavaScript, not Python)
TotalPrice = 99.99  # PascalCase for variables
SHOPPING_CART = []  # ALL_CAPS for non-constants
x = 12345  # Non-descriptive single letter

def calculatePrice():  # camelCase function name
    pass

def ValidateUser():  # PascalCase function name
    pass

print("Step 1: Basic variable and function naming demonstrated")
print(f"User: {user_name}, Price: {total_price}, Authenticated: {is_authenticated}")

# ===============================================================================


# Step 2: Class naming (PascalCase) - Building on Step 1
# ===============================================================================

# Explanation:
# Classes should use PascalCase (also called CapWords) - each word starts
# with a capital letter, no underscores. This distinguishes classes from
# functions and variables.

# All code from Step 1:
user_name_step2 = "john_doe"
total_price_step2 = 99.99
is_authenticated_step2 = True
shopping_cart_items_step2 = []
current_user_id_step2 = 12345

def calculate_total_price_step2(items):
    """Calculate the total price of items in cart."""
    return sum(item.price for item in items)

def validate_user_credentials_step2(username, password):
    """Validate user login credentials."""
    pass

def send_email_notification_step2(recipient, subject, message):
    """Send email notification to user."""
    pass

# Step 2 additions: ✅ GOOD: Class names with PascalCase
class UserManager:
    """Manages user operations and authentication."""
    
    def __init__(self):
        self.active_users = []
    
    def create_user_account(self, username, email):
        """Create a new user account."""
        pass

class ShoppingCart:
    """Represents a shopping cart with items."""
    
    def __init__(self):
        self.cart_items = []
        self.total_amount = 0.0
    
    def add_item_to_cart(self, item):
        """Add an item to the shopping cart."""
        self.cart_items.append(item)

class EmailNotificationService:
    """Service for sending email notifications."""
    
    def __init__(self, smtp_server, port):
        self.smtp_server = smtp_server
        self.port_number = port
    
    def send_welcome_email(self, user_email):
        """Send welcome email to new user."""
        pass

class DatabaseConnectionManager:
    """Manages database connections and transactions."""
    
    def establish_connection(self):
        """Establish database connection."""
        pass

# ❌ BAD: Avoid these class naming patterns
class userManager:  # camelCase
    pass

class user_manager:  # snake_case
    pass

class USERMANAGER:  # ALL_CAPS
    pass

class shopping_Cart:  # Mixed case
    pass

# Step 2 demonstration
user_mgr = UserManager()
cart = ShoppingCart()
email_service = EmailNotificationService("smtp.gmail.com", 587)

print("Step 2: Class naming (PascalCase) demonstrated")
print(f"Created instances: {type(user_mgr).__name__}, {type(cart).__name__}")

# ===============================================================================


# Step 3: Constants naming (UPPER_CASE) - Building on Steps 1-2
# ===============================================================================

# Explanation:
# Constants should use UPPER_CASE with underscores separating words.
# Constants are values that don't change during program execution.

# All code from Steps 1-2:
user_name_step3 = "john_doe"
total_price_step3 = 99.99
is_authenticated_step3 = True
shopping_cart_items_step3 = []
current_user_id_step3 = 12345

def calculate_total_price_step3(items):
    """Calculate the total price of items in cart."""
    return sum(item.price for item in items)

def validate_user_credentials_step3(username, password):
    """Validate user login credentials."""
    pass

def send_email_notification_step3(recipient, subject, message):
    """Send email notification to user."""
    pass

class UserManagerStep3:
    """Manages user operations and authentication."""
    
    def __init__(self):
        self.active_users = []
    
    def create_user_account(self, username, email):
        """Create a new user account."""
        pass

class ShoppingCartStep3:
    """Represents a shopping cart with items."""
    
    def __init__(self):
        self.cart_items = []
        self.total_amount = 0.0
    
    def add_item_to_cart(self, item):
        """Add an item to the shopping cart."""
        self.cart_items.append(item)

# Step 3 additions: ✅ GOOD: Constants with UPPER_CASE names
MAX_LOGIN_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"
DATABASE_CONNECTION_STRING = "postgresql://localhost:5432/mydb"
SUPPORTED_FILE_EXTENSIONS = ['.jpg', '.png', '.gif', '.pdf']
TAX_RATE_PERCENTAGE = 8.25
CACHE_EXPIRY_HOURS = 24
ERROR_MESSAGES = {
    'INVALID_LOGIN': 'Invalid username or password',
    'SESSION_EXPIRED': 'Your session has expired',
    'INSUFFICIENT_PERMISSIONS': 'You do not have permission to perform this action'
}

# Configuration constants
DEBUG_MODE = False
LOG_LEVEL = 'INFO'
MAX_FILE_SIZE_MB = 10
PAGINATION_DEFAULT_SIZE = 25

# Mathematical constants
PI = 3.14159265359
GOLDEN_RATIO = 1.618033988749
EULER_NUMBER = 2.718281828459

# ❌ BAD: Avoid these constant naming patterns
maxLoginAttempts = 3  # camelCase
Max_Login_Attempts = 3  # Mixed case
max_login_attempts = 3  # snake_case (this looks like a variable)

class ConfigurationManager:
    """Example class using constants."""
    
    def __init__(self):
        self.max_retries = MAX_LOGIN_ATTEMPTS
        self.timeout = DEFAULT_TIMEOUT_SECONDS
        self.base_url = API_BASE_URL
    
    def validate_file_extension(self, filename):
        """Check if file extension is supported."""
        extension = filename.lower().split('.')[-1]
        return f'.{extension}' in SUPPORTED_FILE_EXTENSIONS
    
    def calculate_tax(self, amount):
        """Calculate tax amount."""
        return amount * (TAX_RATE_PERCENTAGE / 100)

# Step 3 demonstration
config_mgr = ConfigurationManager()
print("Step 3: Constants naming (UPPER_CASE) demonstrated")
print(f"Max attempts: {MAX_LOGIN_ATTEMPTS}, Timeout: {DEFAULT_TIMEOUT_SECONDS}s")
print(f"Tax on $100: ${config_mgr.calculate_tax(100):.2f}")

# ===============================================================================


# Step 4: Private and Protected attributes - Building on Steps 1-3
# ===============================================================================

# Explanation:
# - Private attributes: Use double underscore prefix (__attribute)
# - Protected attributes: Use single underscore prefix (_attribute)
# - Private methods: Use double underscore prefix (__method)
# - Protected methods: Use single underscore prefix (_method)

# All code from Steps 1-3:
user_name_step4 = "john_doe"
total_price_step4 = 99.99
is_authenticated_step4 = True

def calculate_total_price_step4(items):
    """Calculate the total price of items in cart."""
    return sum(item.price for item in items)

def validate_user_credentials_step4(username, password):
    """Validate user login credentials."""
    pass

MAX_LOGIN_ATTEMPTS_STEP4 = 3
DEFAULT_TIMEOUT_SECONDS_STEP4 = 30
API_BASE_URL_STEP4 = "https://api.example.com"
TAX_RATE_PERCENTAGE_STEP4 = 8.25

# Step 4 additions: ✅ GOOD: Private and protected attributes
class BankAccount:
    """Example class demonstrating private and protected attributes."""
    
    def __init__(self, account_number, initial_balance):
        # Public attributes (no underscore)
        self.account_number = account_number
        self.account_type = "checking"
        
        # Protected attributes (single underscore) - intended for internal use
        self._balance = initial_balance
        self._transaction_history = []
        self._account_status = "active"
        
        # Private attributes (double underscore) - name mangling applied
        self.__pin_code = None
        self.__security_key = "secret_key_12345"
        self.__internal_id = f"BANK_{account_number}_{hash(account_number)}"
    
    # Public methods
    def get_balance(self):
        """Get account balance (public method)."""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money to account."""
        if amount > 0:
            self._balance += amount
            self._add_transaction("deposit", amount)
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if self._validate_withdrawal(amount):
            self._balance -= amount
            self._add_transaction("withdrawal", amount)
            return True
        return False
    
    # Protected methods (single underscore) - intended for subclasses
    def _validate_withdrawal(self, amount):
        """Validate if withdrawal is allowed."""
        return amount > 0 and amount <= self._balance
    
    def _add_transaction(self, transaction_type, amount):
        """Add transaction to history."""
        import datetime
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'timestamp': datetime.datetime.now(),
            'balance_after': self._balance
        }
        self._transaction_history.append(transaction)
    
    def _get_transaction_history(self):
        """Get transaction history (protected method)."""
        return self._transaction_history.copy()
    
    # Private methods (double underscore) - name mangling applied
    def __validate_pin(self, pin):
        """Validate PIN code (private method)."""
        return pin == self.__pin_code
    
    def __generate_security_token(self):
        """Generate security token (private method)."""
        import hashlib
        return hashlib.md5(self.__security_key.encode()).hexdigest()
    
    def __reset_security_key(self):
        """Reset security key (private method)."""
        import secrets
        self.__security_key = secrets.token_hex(16)
    
    # Public method that uses private methods
    def authenticate(self, pin):
        """Authenticate user with PIN."""
        if self.__validate_pin(pin):
            return self.__generate_security_token()
        return None

class SavingsAccount(BankAccount):
    """Subclass demonstrating access to protected members."""
    
    def __init__(self, account_number, initial_balance, interest_rate):
        super().__init__(account_number, initial_balance)
        self._interest_rate = interest_rate  # Protected attribute
        self.__minimum_balance = 100  # Private attribute
    
    def apply_interest(self):
        """Apply interest to account (uses protected attributes)."""
        if self._balance >= self.__minimum_balance:
            interest = self._balance * (self._interest_rate / 100)
            self._balance += interest
            self._add_transaction("interest", interest)  # Using protected method
            return interest
        return 0
    
    def get_account_summary(self):
        """Get account summary (uses protected methods)."""
        return {
            'balance': self._balance,
            'transactions': len(self._get_transaction_history()),
            'status': self._account_status,
            'interest_rate': self._interest_rate
        }

# ❌ BAD: Inconsistent naming patterns
class BadExample:
    def __init__(self):
        self.publicAttribute = "bad"  # camelCase
        self._protectedAttribute = "ok"  # This is fine
        self.__privateAttribute = "ok"  # This is fine
        self.Protected_Attribute = "bad"  # Mixed case
        self.__Public_Attribute = "bad"  # Private but mixed case

# Step 4 demonstration
account = BankAccount("12345", 1000.0)
savings = SavingsAccount("67890", 2000.0, 2.5)

account.deposit(500)
account.withdraw(200)
savings.apply_interest()

print("Step 4: Private and protected attributes demonstrated")
print(f"Account balance: ${account.get_balance()}")
print(f"Savings balance: ${savings.get_balance()}")
print(f"Can access protected _balance: ${savings._balance}")
# print(f"Cannot easily access private: {account.__pin_code}")  # This would cause AttributeError

# ===============================================================================


# Step 5: Special methods (dunder methods) - Building on Steps 1-4
# ===============================================================================

# Explanation:
# Special methods use double underscores before and after the name (__method__).
# These are predefined by Python and provide special functionality like
# operator overloading, string representation, iteration, etc.

# All code from Steps 1-4:
user_name_step5 = "john_doe"
total_price_step5 = 99.99

def calculate_total_price_step5(items):
    """Calculate the total price of items in cart."""
    return sum(item.price for item in items)

MAX_LOGIN_ATTEMPTS_STEP5 = 3
API_BASE_URL_STEP5 = "https://api.example.com"

class BankAccountStep5:
    """Bank account with basic functionality."""
    
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance
        self._transaction_history = []
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

# Step 5 additions: ✅ GOOD: Special methods (dunder methods)
class Product:
    """Product class demonstrating special methods."""
    
    def __init__(self, name, price, quantity=1):
        """Initialize product (constructor)."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self._created_at = __import__('datetime').datetime.now()
    
    def __str__(self):
        """String representation for end users."""
        return f"{self.name} (${self.price:.2f} x {self.quantity})"
    
    def __repr__(self):
        """String representation for developers/debugging."""
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
    
    def __eq__(self, other):
        """Equality comparison."""
        if not isinstance(other, Product):
            return False
        return (self.name == other.name and 
                self.price == other.price)
    
    def __lt__(self, other):
        """Less than comparison (for sorting)."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price
    
    def __le__(self, other):
        """Less than or equal comparison."""
        return self < other or self == other
    
    def __gt__(self, other):
        """Greater than comparison."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price
    
    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self > other or self == other
    
    def __add__(self, other):
        """Addition operator (combine quantities)."""
        if isinstance(other, Product) and self.name == other.name and self.price == other.price:
            return Product(self.name, self.price, self.quantity + other.quantity)
        return NotImplemented
    
    def __mul__(self, factor):
        """Multiplication operator (multiply quantity)."""
        if isinstance(factor, (int, float)) and factor >= 0:
            return Product(self.name, self.price, int(self.quantity * factor))
        return NotImplemented
    
    def __hash__(self):
        """Hash method (for use in sets and as dict keys)."""
        return hash((self.name, self.price))
    
    def __len__(self):
        """Length method (return quantity)."""
        return self.quantity
    
    def __bool__(self):
        """Boolean conversion (True if quantity > 0)."""
        return self.quantity > 0
    
    def __getitem__(self, key):
        """Index access (for demonstration)."""
        if key == 'name':
            return self.name
        elif key == 'price':
            return self.price
        elif key == 'quantity':
            return self.quantity
        else:
            raise KeyError(f"Invalid key: {key}")
    
    def __setitem__(self, key, value):
        """Index assignment."""
        if key == 'name':
            self.name = value
        elif key == 'price':
            self.price = value
        elif key == 'quantity':
            self.quantity = value
        else:
            raise KeyError(f"Invalid key: {key}")
    
    def __contains__(self, item):
        """Membership test (in operator)."""
        return item.lower() in self.name.lower()
    
    def __call__(self, discount_percent=0):
        """Make object callable (calculate discounted price)."""
        discounted_price = self.price * (1 - discount_percent / 100)
        return discounted_price * self.quantity

class ShoppingCartStep5:
    """Shopping cart demonstrating container special methods."""
    
    def __init__(self):
        self._items = []
    
    def __len__(self):
        """Return number of items in cart."""
        return len(self._items)
    
    def __iter__(self):
        """Make cart iterable."""
        return iter(self._items)
    
    def __getitem__(self, index):
        """Get item by index."""
        return self._items[index]
    
    def __setitem__(self, index, value):
        """Set item by index."""
        if isinstance(value, Product):
            self._items[index] = value
        else:
            raise TypeError("Only Product objects can be added to cart")
    
    def __delitem__(self, index):
        """Delete item by index."""
        del self._items[index]
    
    def __contains__(self, item):
        """Check if product is in cart."""
        return item in self._items
    
    def __str__(self):
        """String representation of cart."""
        if not self._items:
            return "Empty shopping cart"
        items_str = "\n".join(f"  - {item}" for item in self._items)
        total = sum(item.price * item.quantity for item in self._items)
        return f"Shopping Cart:\n{items_str}\nTotal: ${total:.2f}"
    
    def __repr__(self):
        """Developer representation of cart."""
        return f"ShoppingCartStep5(items={len(self._items)})"
    
    def add_item(self, product):
        """Add product to cart."""
        self._items.append(product)
    
    def __iadd__(self, product):
        """In-place addition (+= operator)."""
        self.add_item(product)
        return self

# ❌ BAD: Don't create your own dunder methods
class BadSpecialMethods:
    def __my_custom_method__(self):  # Don't do this!
        pass
    
    def __another_bad_idea__(self):  # Don't do this!
        pass

# Step 5 demonstration
laptop = Product("Gaming Laptop", 1299.99, 1)
mouse = Product("Wireless Mouse", 29.99, 2)
keyboard = Product("Mechanical Keyboard", 149.99, 1)

cart = ShoppingCartStep5()
cart += laptop  # Using __iadd__
cart.add_item(mouse)
cart.add_item(keyboard)

print("Step 5: Special methods (dunder methods) demonstrated")
print(f"Product: {laptop}")  # Uses __str__
print(f"Product repr: {repr(mouse)}")  # Uses __repr__
print(f"Laptop == mouse: {laptop == mouse}")  # Uses __eq__
print(f"Laptop > mouse: {laptop > mouse}")  # Uses __gt__
print(f"Cart length: {len(cart)}")  # Uses __len__
print(f"'Gaming' in laptop: {'Gaming' in laptop}")  # Uses __contains__
print(f"Laptop with 10% discount: ${laptop(10):.2f}")  # Uses __call__
print(f"Cart contents:\n{cart}")  # Uses __str__

# ===============================================================================


# Step 6: Module and package naming - Building on Steps 1-5
# ===============================================================================

# Explanation:
# - Modules: Use short, lowercase names with underscores if needed
# - Packages: Use short, lowercase names, avoid underscores when possible
# - Import aliases: Use meaningful, short names

# All code from Steps 1-5:
user_name_step6 = "john_doe"
MAX_LOGIN_ATTEMPTS_STEP6 = 3

def calculate_total_price_step6(items):
    """Calculate the total price of items in cart."""
    return sum(item.price for item in items)

class ProductStep6:
    """Product class for step 6."""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

# Step 6 additions: ✅ GOOD: Module and import naming examples

# Good module names (examples of what files should be named):
# user_management.py
# email_service.py
# database_utils.py
# api_client.py
# config.py
# models.py
# views.py
# utils.py

# Good package names (examples of directory names):
# myproject/
# userauth/
# ecommerce/
# dataprocessing/
# webapi/

# ✅ GOOD: Import statements with proper aliases
import os
import sys
import json
import datetime as dt
import collections as col
from typing import List, Dict, Optional
from pathlib import Path

# For demonstration, let's simulate some imports
# import user_management as user_mgmt
# import email_service as email
# import database_utils as db_utils
# from myproject.auth import authentication_service as auth
# from myproject.utils import string_helpers as str_utils

# ✅ GOOD: Descriptive import aliases
def demonstrate_good_imports():
    """Show examples of good import practices."""
    
    # Standard library imports
    current_time = dt.datetime.now()
    user_data = col.defaultdict(list)
    
    # File operations
    config_path = Path("config.json")
    
    return {
        'timestamp': current_time,
        'data': user_data,
        'config_path': config_path
    }

# ❌ BAD: Poor module and import naming
# Bad module names (avoid these):
# UserManagement.py (PascalCase)
# user-management.py (hyphens)
# userManagement.py (camelCase)
# USER_MANAGEMENT.py (ALL_CAPS)

# Bad import aliases:
# import datetime as d  # Too short, not descriptive
# import collections as c  # Too short
# import user_management as um  # Unclear abbreviation
# from myproject import authentication_service as authentication_service  # Redundant

print("Step 6: Module and package naming demonstrated")
print(f"Good imports result: {demonstrate_good_imports()}")

# ===============================================================================


# Step 7: Descriptive naming practices - Building on Steps 1-6
# ===============================================================================

# Explanation:
# Names should be descriptive, unambiguous, and reveal intent.
# Avoid abbreviations, single letters (except for loops), and misleading names.

# All code from Steps 1-6:
user_name_step7 = "john_doe"
MAX_LOGIN_ATTEMPTS_STEP7 = 3

def calculate_total_price_step7(items):
    """Calculate the total price of items in cart."""
    return sum(item.price for item in items)

class ProductStep7:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Step 7 additions: ✅ GOOD: Descriptive naming practices

# ✅ GOOD: Descriptive variable names
customer_email_address = "customer@example.com"
total_order_amount = 299.99
is_payment_successful = True
user_authentication_token = "abc123xyz789"
shopping_cart_item_count = 5
maximum_retry_attempts = 3
database_connection_timeout_seconds = 30
email_notification_recipients = ["admin@example.com", "user@example.com"]

# ✅ GOOD: Descriptive function names
def validate_email_address_format(email):
    """Validate if email address has correct format."""
    return "@" in email and "." in email.split("@")[-1]

def calculate_shipping_cost_by_weight(weight_kg, destination_country):
    """Calculate shipping cost based on weight and destination."""
    base_rate = 5.0
    per_kg_rate = 2.0
    international_multiplier = 1.5 if destination_country != "US" else 1.0
    return (base_rate + weight_kg * per_kg_rate) * international_multiplier

def send_order_confirmation_email(customer_email, order_details):
    """Send order confirmation email to customer."""
    subject = f"Order Confirmation #{order_details['order_id']}"
    # Email sending logic here
    pass

def process_credit_card_payment(card_number, expiry_date, cvv, amount):
    """Process credit card payment through payment gateway."""
    # Payment processing logic here
    return {"status": "success", "transaction_id": "txn_123456"}

# ✅ GOOD: Descriptive class names
class CustomerOrderManager:
    """Manages customer orders and order processing."""
    
    def __init__(self):
        self.pending_orders = []
        self.completed_orders = []
        self.failed_orders = []
    
    def create_new_customer_order(self, customer_id, order_items):
        """Create a new order for customer."""
        order_id = self._generate_unique_order_id()
        order_total = self._calculate_order_total_amount(order_items)
        
        new_order = {
            'order_id': order_id,
            'customer_id': customer_id,
            'items': order_items,
            'total_amount': order_total,
            'status': 'pending',
            'created_timestamp': dt.datetime.now()
        }
        
        self.pending_orders.append(new_order)
        return new_order
    
    def _generate_unique_order_id(self):
        """Generate unique order ID."""
        import uuid
        return f"ORD_{uuid.uuid4().hex[:8].upper()}"
    
    def _calculate_order_total_amount(self, order_items):
        """Calculate total amount for order items."""
        return sum(item['price'] * item['quantity'] for item in order_items)

class EmailNotificationManager:
    """Manages email notifications for various events."""
    
    def __init__(self, smtp_server_host, smtp_server_port):
        self.smtp_server_host = smtp_server_host
        self.smtp_server_port = smtp_server_port
        self.email_templates = {}
    
    def send_welcome_email_to_new_user(self, user_email, user_name):
        """Send welcome email to newly registered user."""
        template = self.email_templates.get('welcome', 'Welcome {name}!')
        message_body = template.format(name=user_name)
        # Send email logic here
        pass

# ❌ BAD: Poor descriptive naming practices
# Avoid these patterns:

# Non-descriptive variable names
x = "customer@example.com"  # What is x?
data = 299.99  # What kind of data?
flag = True  # What does this flag represent?
temp = "abc123"  # Temporary what?
num = 5  # Number of what?
max = 3  # Maximum what?
timeout = 30  # Timeout for what?
list1 = ["admin@example.com"]  # List of what?

# Non-descriptive function names
def validate(email):  # Validate what?
    pass

def calc(weight, country):  # Calculate what?
    pass

def send(email, details):  # Send what?
    pass

def process(card, date, cvv, amt):  # Process what? Unclear abbreviations
    pass

# Non-descriptive class names
class Manager:  # Manager of what?
    pass

class Handler:  # Handler for what?
    pass

class Processor:  # Processor for what?
    pass

# Step 7 demonstration
order_manager = CustomerOrderManager()
email_manager = EmailNotificationManager("smtp.gmail.com", 587)

sample_order_items = [
    {'name': 'Laptop', 'price': 999.99, 'quantity': 1},
    {'name': 'Mouse', 'price': 29.99, 'quantity': 2}
]

new_customer_order = order_manager.create_new_customer_order("CUST_001", sample_order_items)
shipping_cost = calculate_shipping_cost_by_weight(2.5, "Canada")

print("Step 7: Descriptive naming practices demonstrated")
print(f"New order ID: {new_customer_order['order_id']}")
print(f"Order total: ${new_customer_order['total_amount']:.2f}")
print(f"Shipping cost: ${shipping_cost:.2f}")
print(f"Email valid: {validate_email_address_format(customer_email_address)}")

# ===============================================================================


# FINAL SUMMARY: Complete PEP8 Naming Conventions Guide
# ===============================================================================

print("\n" + "="*80)
print("COMPLETE PEP8 NAMING CONVENTIONS SUMMARY")
print("="*80)
print("✅ Variables & Functions: snake_case (user_name, calculate_total)")
print("✅ Classes: PascalCase (UserManager, ShoppingCart)")
print("✅ Constants: UPPER_CASE (MAX_ATTEMPTS, API_URL)")
print("✅ Protected: _single_underscore (_balance, _validate)")
print("✅ Private: __double_underscore (__pin_code, __security_key)")
print("✅ Special methods: __dunder__ (__init__, __str__, __eq__)")
print("✅ Modules: lowercase_with_underscores (user_management.py)")
print("✅ Packages: lowercase (myproject, userauth)")
print("✅ Descriptive: Clear, unambiguous names that reveal intent")
print("="*80)
print("Remember: Good naming makes code self-documenting and maintainable!")
print("="*80)

# ===============================================================================