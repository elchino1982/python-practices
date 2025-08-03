# Python Classes and Objects: Complete Tutorial 🏗️

Welcome to the comprehensive guide to Python Classes and Objects! This tutorial is designed for learners of all levels, from complete beginners to experienced developers looking to deepen their understanding.

## 📚 Table of Contents

1. [Introduction to Object-Oriented Programming](#introduction-to-object-oriented-programming)
2. [What Are Classes and Objects?](#what-are-classes-and-objects)
3. [Basic Class Definition](#basic-class-definition)
4. [The Constructor Method (__init__)](#the-constructor-method-__init__)
5. [Instance Attributes and Methods](#instance-attributes-and-methods)
6. [Class Attributes vs Instance Attributes](#class-attributes-vs-instance-attributes)
7. [Method Types](#method-types)
8. [Advanced Concepts](#advanced-concepts)
9. [Best Practices](#best-practices)
10. [Common Pitfalls and How to Avoid Them](#common-pitfalls-and-how-to-avoid-them)
11. [Practical Examples](#practical-examples)
12. [Exercises and Practice](#exercises-and-practice)

---

## Introduction to Object-Oriented Programming

### What is Object-Oriented Programming (OOP)?

Object-Oriented Programming is a programming paradigm that organizes code around **objects** rather than functions. Think of it as a way to model real-world entities in your code.

**Real-world analogy**: 
- A **car** is an object with properties (color, model, year) and behaviors (start, stop, accelerate)
- A **bank account** is an object with properties (balance, account number) and behaviors (deposit, withdraw, check balance)

### Why Use OOP?

1. **Organization**: Groups related data and functions together
2. **Reusability**: Write once, use many times
3. **Maintainability**: Easier to modify and extend
4. **Modeling**: Natural way to represent real-world concepts
5. **Encapsulation**: Hide internal details, expose only what's necessary

---

## What Are Classes and Objects?

### Understanding the Relationship

**Class**: A blueprint or template for creating objects
**Object**: An instance of a class (the actual "thing" created from the blueprint)

**Analogy**: 
- **Class** = Cookie cutter (the template)
- **Object** = Individual cookies (made from the template)

```python
# Class definition (the blueprint)
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Objects (instances of the class)
car1 = Car("Toyota", "Camry")    # First car object
car2 = Car("Honda", "Civic")     # Second car object
car3 = Car("Ford", "Mustang")    # Third car object
```

Each object has its own set of attributes but follows the same structure defined by the class.

---

## Basic Class Definition

### Simplest Class Possible

```python
class Person:
    pass  # Empty class - does nothing but is valid Python
```

### Adding Basic Structure

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
```

### Step-by-Step Breakdown

1. **`class Person:`** - Declares a new class named "Person"
2. **`def __init__(self, name, age):`** - Constructor method (runs when object is created)
3. **`self`** - Refers to the instance being created
4. **`self.name = name`** - Creates an instance attribute called "name"

### Creating and Using Objects

```python
# Create objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Each object has its own attributes
print(person1.name)  # Alice
print(person2.name)  # Bob (different!)
```

---

## The Constructor Method (__init__)

### What is __init__?

The `__init__` method is a special method (called a "dunder" method) that:
- Runs automatically when you create a new object
- Initializes the object's attributes
- Sets up the initial state of the object

### Anatomy of __init__

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        # Required parameter
        self.account_number = account_number
        
        # Optional parameter with default value
        self.balance = initial_balance
        
        # You can also set attributes not passed as parameters
        self.transaction_count = 0
        self.is_active = True
```

### Different Ways to Use __init__

#### 1. No Parameters (Default Constructor)
```python
class Counter:
    def __init__(self):
        self.count = 0

counter = Counter()  # No arguments needed
```

#### 2. Required Parameters
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(10, 5)  # Must provide width and height
```

#### 3. Optional Parameters with Defaults
```python
class Student:
    def __init__(self, name, grade="A", enrolled=True):
        self.name = name
        self.grade = grade
        self.enrolled = enrolled

# Different ways to create students
student1 = Student("Alice")                    # Uses defaults
student2 = Student("Bob", "B")                 # Custom grade
student3 = Student("Charlie", "C", False)      # All custom
```

#### 4. Using *args and **kwargs
```python
class FlexibleClass:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

obj = FlexibleClass(1, 2, 3, name="test", value=42)
print(obj.args)    # (1, 2, 3)
print(obj.kwargs)  # {'name': 'test', 'value': 42}
```

---

## Instance Attributes and Methods

### Instance Attributes

Instance attributes are variables that belong to a specific object instance.

```python
class Dog:
    def __init__(self, name, breed, age):
        # These are instance attributes
        self.name = name
        self.breed = breed
        self.age = age
        self.is_hungry = True  # Default value

# Each dog has its own attributes
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "German Shepherd", 5)

print(dog1.name)   # Buddy
print(dog2.name)   # Max
```

### Instance Methods

Instance methods are functions that belong to the class and can access/modify instance attributes.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_hungry = True

    # Instance methods
    def bark(self):
        return f"{self.name} says Woof!"
    
    def feed(self):
        if self.is_hungry:
            self.is_hungry = False
            return f"{self.name} has been fed!"
        else:
            return f"{self.name} is not hungry right now."
    
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"
    
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."

# Using the methods
dog = Dog("Buddy", "Golden Retriever", 3)
print(dog.bark())           # Buddy says Woof!
print(dog.feed())           # Buddy has been fed!
print(dog.get_info())       # Buddy is a 3-year-old Golden Retriever
print(dog.have_birthday())  # Happy birthday Buddy! Now 4 years old.
```

### The `self` Parameter

- **`self`** always refers to the current instance
- It must be the first parameter in instance methods
- You don't pass it when calling the method - Python does it automatically

```python
class Example:
    def __init__(self, value):
        self.value = value
    
    def show_self(self):
        print(f"self refers to: {self}")
        print(f"self.value is: {self.value}")

obj1 = Example("Hello")
obj2 = Example("World")

obj1.show_self()  # self refers to the obj1 instance
obj2.show_self()  # self refers to the obj2 instance
```

---

## Class Attributes vs Instance Attributes

Understanding the difference between class and instance attributes is crucial for effective OOP.

### Instance Attributes
- Belong to a specific instance
- Each object has its own copy
- Defined in `__init__` or other instance methods

### Class Attributes
- Belong to the class itself
- Shared by all instances
- Defined directly in the class body

```python
class Car:
    # Class attributes (shared by all instances)
    wheels = 4
    vehicle_type = "automobile"
    total_cars = 0  # Keep track of how many cars we've created
    
    def __init__(self, make, model, year):
        # Instance attributes (unique to each instance)
        self.make = make
        self.model = model
        self.year = year
        
        # Increment the class attribute when a new car is created
        Car.total_cars += 1

# Create some cars
car1 = Car("Toyota", "Camry", 2025)
car2 = Car("Honda", "Civic", 2025)
car3 = Car("Ford", "Mustang", 2025)

# Instance attributes are different for each car
print(car1.make)    # Toyota
print(car2.make)    # Honda
print(car3.make)    # Ford

# Class attributes are the same for all cars
print(car1.wheels)  # 4
print(car2.wheels)  # 4
print(car3.wheels)  # 4

# Access class attributes through the class name
print(Car.total_cars)  # 3
print(Car.vehicle_type)  # automobile

# You can also access class attributes through instances
print(car1.total_cars)  # 3 (but this is not recommended)
```

### Modifying Class Attributes

```python
class Student:
    school_name = "Python High School"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

# All students share the same school
student1 = Student("Alice")
student2 = Student("Bob")

print(student1.school_name)  # Python High School
print(student2.school_name)  # Python High School

# Change the class attribute
Student.school_name = "Advanced Python Academy"

# All instances see the change
print(student1.school_name)  # Advanced Python Academy
print(student2.school_name)  # Advanced Python Academy
```

### ⚠️ Common Pitfall: Mutable Class Attributes

```python
# DANGEROUS - Don't do this!
class BadExample:
    shared_list = []  # This list is shared by ALL instances!
    
    def __init__(self, name):
        self.name = name
    
    def add_item(self, item):
        self.shared_list.append(item)  # Modifies the shared list!

# This causes unexpected behavior
obj1 = BadExample("Object1")
obj2 = BadExample("Object2")

obj1.add_item("item1")
obj2.add_item("item2")

print(obj1.shared_list)  # ['item1', 'item2'] - Unexpected!
print(obj2.shared_list)  # ['item1', 'item2'] - Both have same list!

# CORRECT way - Use instance attributes for mutable objects
class GoodExample:
    def __init__(self, name):
        self.name = name
        self.my_list = []  # Each instance gets its own list
    
    def add_item(self, item):
        self.my_list.append(item)

obj3 = GoodExample("Object3")
obj4 = GoodExample("Object4")

obj3.add_item("item3")
obj4.add_item("item4")

print(obj3.my_list)  # ['item3'] - Correct!
print(obj4.my_list)  # ['item4'] - Each has its own list!
```

---

## Method Types

Python classes support three types of methods, each serving different purposes.

### 1. Instance Methods (Most Common)

```python
class Calculator:
    def __init__(self, name):
        self.name = name
        self.history = []
    
    # Instance method - works with instance data
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def get_history(self):
        return self.history

calc = Calculator("My Calculator")
result = calc.add(5, 3)  # 8
print(calc.get_history())  # ['5 + 3 = 8']
```

### 2. Class Methods (@classmethod)

Class methods receive the class as the first argument (conventionally named `cls`) instead of the instance.

```python
class Person:
    population = 0  # Class attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    
    @classmethod
    def get_population(cls):
        return cls.population
    
    @classmethod
    def from_string(cls, person_str):
        """Alternative constructor - creates Person from string"""
        name, age = person_str.split('-')
        return cls(name, int(age))  # cls() calls __init__
    
    @classmethod
    def create_baby(cls, name):
        """Another alternative constructor"""
        return cls(name, 0)

# Using regular constructor
person1 = Person("Alice", 25)

# Using class method as alternative constructor
person2 = Person.from_string("Bob-30")
person3 = Person.create_baby("Charlie")

print(Person.get_population())  # 3
print(person2.name, person2.age)  # Bob 30
print(person3.name, person3.age)  # Charlie 0
```

### 3. Static Methods (@staticmethod)

Static methods don't receive `self` or `cls` - they're like regular functions but belong to the class namespace.

```python
class MathUtils:
    @staticmethod
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """Calculate factorial"""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)
    
    @staticmethod
    def gcd(a, b):
        """Greatest common divisor"""
        while b:
            a, b = b, a % b
        return a

# Call static methods through the class
print(MathUtils.is_prime(17))    # True
print(MathUtils.factorial(5))    # 120
print(MathUtils.gcd(48, 18))     # 6

# You can also call through an instance (but it's not recommended)
utils = MathUtils()
print(utils.is_prime(13))        # True (works but not recommended)
```

### When to Use Each Method Type

| Method Type | When to Use | Example Use Cases |
|-------------|-------------|-------------------|
| **Instance Method** | When you need to access/modify instance data | `dog.bark()`, `account.withdraw()` |
| **Class Method** | Alternative constructors, working with class data | `Person.from_string()`, `Employee.get_count()` |
| **Static Method** | Utility functions related to the class | `MathUtils.is_prime()`, `DateUtils.is_weekend()` |

---

## Advanced Concepts

### Property Decorators

Properties allow you to use methods like attributes, enabling validation and computed values.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute (convention)
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter for radius with validation"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Computed property - calculated each time"""
        return 3.14159 * self._radius ** 2
    
    @property
    def diameter(self):
        """Another computed property"""
        return 2 * self._radius

# Usage
circle = Circle(5)
print(circle.radius)    # 5 (calls the getter)
print(circle.area)      # 78.53975 (computed)
print(circle.diameter)  # 10 (computed)

circle.radius = 10      # Calls the setter
print(circle.area)      # 314.159 (automatically updated)

# circle.radius = -5    # Would raise ValueError
```

### String Representation Methods

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """Human-readable string representation"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book = Book("1984", "George Orwell", 328)

print(str(book))    # '1984' by George Orwell
print(repr(book))   # Book('1984', 'George Orwell', 328)
print(book)         # '1984' by George Orwell (uses __str__)
```

---

## Best Practices

### 1. Naming Conventions

```python
# ✅ Good naming
class BankAccount:          # PascalCase for classes
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number      # snake_case for attributes
        self._balance = initial_balance           # Leading underscore for "private"
        self.__secret_key = "abc123"             # Double underscore for name mangling
    
    def get_balance(self):                       # snake_case for methods
        return self._balance
    
    def _validate_amount(self, amount):          # Leading underscore for "private" methods
        return amount > 0

# ❌ Bad naming
class bankaccount:          # Should be PascalCase
    def __init__(self, AccountNumber, InitialBalance):
        self.AccountNumber = AccountNumber       # Should be snake_case
        self.InitialBalance = InitialBalance
    
    def GetBalance(self):                        # Should be snake_case
        return self.InitialBalance
```

### 2. Use Docstrings

```python
class Rectangle:
    """
    A class representing a rectangle.
    
    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    """
    
    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
            
        Raises:
            ValueError: If width or height is negative
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle
        """
        return self.width * self.height
```

### 3. Input Validation

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Temperature must be a number")
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
```

### 4. Keep Methods Focused (Single Responsibility)

```python
# ✅ Good - Each method has one responsibility
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
    
    def activate(self):
        """Activate the user account"""
        self.is_active = True
    
    def deactivate(self):
        """Deactivate the user account"""
        self.is_active = False
    
    def update_email(self, new_email):
        """Update user's email address"""
        if self._is_valid_email(new_email):
            self.email = new_email
        else:
            raise ValueError("Invalid email format")
    
    def _is_valid_email(self, email):
        """Private method to validate email format"""
        return "@" in email and "." in email

# ❌ Bad - Method does too many things
class BadUser:
    def manage_account(self, action, email=None):
        """This method does too many different things"""
        if action == "activate":
            self.is_active = True
        elif action == "deactivate":
            self.is_active = False
        elif action == "update_email":
            if email and "@" in email:
                self.email = email
            else:
                raise ValueError("Invalid email")
        # ... more actions
```

---

## Common Pitfalls and How to Avoid Them

### 1. Forgetting `self` Parameter

```python
# ❌ Wrong - Missing self parameter
class BadExample:
    def __init__(name, age):  # Missing self!
        self.name = name      # This will cause an error
        self.age = age

# ✅ Correct
class GoodExample:
    def __init__(self, name, age):  # Include self
        self.name = name
        self.age = age
```

### 2. Mutable Default Arguments

```python
# ❌ Dangerous - Mutable default argument
class BadShoppingCart:
    def __init__(self, items=[]):  # Don't do this!
        self.items = items

# All instances share the same list!
cart1 = BadShoppingCart()
cart2 = BadShoppingCart()
cart1.items.append("apple")
print(cart2.items)  # ['apple'] - Unexpected!

# ✅ Correct approach
class GoodShoppingCart:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
```

### 3. Modifying Class Attributes Through Instances

```python
class Counter:
    count = 0  # Class attribute
    
    def __init__(self):
        Counter.count += 1  # ✅ Correct - modify through class name

# ❌ Problematic
counter1 = Counter()
counter1.count = 100  # Creates instance attribute, doesn't modify class attribute!

print(Counter.count)   # Still 1, not 100!
print(counter1.count)  # 100 (instance attribute)

# ✅ Correct
Counter.count = 100    # Modifies the class attribute
```

### 4. Not Understanding Attribute Lookup

```python
class Example:
    class_attr = "I'm a class attribute"
    
    def __init__(self):
        self.instance_attr = "I'm an instance attribute"

obj = Example()

# Python looks for attributes in this order:
# 1. Instance attributes
# 2. Class attributes
# 3. Parent class attributes (inheritance)

print(obj.instance_attr)  # Found in instance
print(obj.class_attr)     # Found in class

# If you create an instance attribute with the same name as a class attribute:
obj.class_attr = "I'm now an instance attribute"
print(obj.class_attr)     # "I'm now an instance attribute"
print(Example.class_attr) # "I'm a class attribute" (unchanged)
```

---

## Practical Examples

### Example 1: Bank Account System

```python
class BankAccount:
    """A simple bank account implementation"""
    
    # Class attributes
    bank_name = "Python Bank"
    interest_rate = 0.02
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self._add_transaction("Account opened", initial_balance)
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self._add_transaction("Deposit", amount)
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        self._add_transaction("Withdrawal", -amount)
        return self.balance
    
    def apply_interest(self):
        """Apply interest to the account"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._add_transaction("Interest", interest)
        return interest
    
    def _add_transaction(self, transaction_type, amount):
        """Private method to record transactions"""
        from datetime import datetime
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'timestamp': datetime.now(),
            'balance_after': self.balance
        }
        self.transaction_history.append(transaction)
    
    def get_statement(self):
        """Get account statement"""
        statement = f"\n=== {self.bank_name} Statement ===\n"
        statement += f"Account Holder: {self.account_holder}\n"
        statement += f"Current Balance: ${self.balance:.2f}\n"
        statement += f"Transaction History:\n"
        
        for transaction in self.transaction_history:
            statement += f"  {transaction['timestamp'].strftime('%Y-%m-%d %H:%M')} - "
            statement += f"{transaction['type']}: ${transaction['amount']:.2f} "
            statement += f"(Balance: ${transaction['balance_after']:.2f})\n"
        
        return statement
    
    def __str__(self):
        return f"BankAccount({self.account_holder}, ${self.balance:.2f})"

# Usage example
account = BankAccount("Alice Johnson", 1000)
account.deposit(500)
account.withdraw(200)
account.apply_interest()
print(account.get_statement())
```

### Example 2: Library Management System

```python
class Book:
    """Represents a book in the library"""
    
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = copies
        self.available_copies = copies
        self.borrowed_by = []
    
    def is_available(self):
        return self.available_copies > 0
    
    def borrow(self, borrower_name):
        if not self.is_available():
            return False
        
        self.available_copies -= 1
        self.borrowed_by.append(borrower_name)
        return True
    
    def return_book(self, borrower_name):
        if borrower_name in self.borrowed_by:
            self.available_copies += 1
            self.borrowed_by.remove(borrower_name)
            return True
        return False
    
    def __str__(self):
        return f"'{self.title}' by {self.author} (Available: {self.available_copies}/{self.total_copies})"

class Library:
    """Manages a collection of books"""
    
    def __init__(self, name):
        self.name = name
        self.books = {}  # ISBN -> Book object
        self.members = set()
    
    def add_book(self, book):
        """Add a book to the library"""
        if book.isbn in self.books:
            # If book already exists, increase copy count
            existing_book = self.books[book.isbn]
            existing_book.total_copies += book.total_copies
            existing_book.available_copies += book.available_copies
        else:
            self.books[book.isbn] = book
    
    def register_member(self, member_name):
        """Register a new library member"""
        self.members.add(member_name)
    
    def find_book(self, title=None, author=None, isbn=None):
        """Find books by title, author, or ISBN"""
        results = []
        for book in self.books.values():
            if isbn and book.isbn == isbn:
                return [book]
            if title and title.lower() in book.title.lower():
                results.append(book)
            elif author and author.lower() in book.author.lower():
                results.append(book)
        return results
    
    def borrow_book(self, isbn, borrower_name):
        """Borrow a book"""
        if borrower_name not in self.members:
            return False, "Borrower is not a registered member"
        
        if isbn not in self.books:
            return False, "Book not found"
        
        book = self.books[isbn]
        if book.borrow(borrower_name):
            return True, f"Successfully borrowed '{book.title}'"
        else:
            return False, "Book is not available"
    
    def return_book(self, isbn, borrower_name):
        """Return a book"""
        if isbn not in self.books:
            return False, "Book not found"
        
        book = self.books[isbn]
        if book.return_book(borrower_name):
            return True, f"Successfully returned '{book.title}'"
        else:
            return False, "This book was not borrowed by this person"
    
    def list_available_books(self):
        """List all available books"""
        available = [book for book in self.books.values() if book.is_available()]
        return available
    
    def __str__(self):
        return f"{self.name} Library ({len(self.books)} unique books, {len(self.members)} members)"

# Usage example
library = Library("City Central Library")

# Add books
book1 = Book("The Python Programming Language", "Guido van Rossum", "978-0134853987", 3)
book2 = Book("Clean Code", "Robert Martin", "978-0132350884", 2)
book3 = Book("Design Patterns", "Gang of Four", "978-0201633610", 1)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register members
library.register_member("Alice")
library.register_member("Bob")

# Borrow books
success, message = library.borrow_book("978-0134853987", "Alice")
print(message)

# List available books
print("\nAvailable books:")
for book in library.list_available_books():
    print(f"  {book}")
```

---

## Exercises and Practice

### Beginner Level 🟢

1. **Person Class**: Create a `Person` class with name and age attributes, and a `greet()` method.

2. **Rectangle Class**: Create a `Rectangle` class that calculates area and perimeter.

3. **Student Class**: Create a `Student` class that manages grades and calculates GPA.

4. **Car Class**: Create a `Car` class with make, model, year, and methods to start/stop.

5. **Bank Account**: Create a simple `BankAccount` class with deposit and withdraw methods.

### Intermediate Level 🟡

6. **Employee Management**: Create an `Employee` class with class methods for different employee types.

7. **Shopping Cart**: Create a `ShoppingCart` class that manages items and calculates totals.

8. **Temperature Converter**: Create a `Temperature` class with property decorators for different scales.

9. **Library System**: Extend the library example with due dates and late fees.

10. **Game Character**: Create a `Character` class for a simple RPG game.

### Advanced Level 🔴

11. **Cache System**: Implement a `Cache` class with size limits and LRU eviction.

12. **Database Connection**: Create a `DatabaseConnection` class with connection pooling.

13. **Event System**: Implement an event-driven system with observers.

14. **State Machine**: Create a `StateMachine` class for modeling workflows.

15. **Plugin System**: Design a plugin architecture using classes.

---

## Summary

Congratulations! You've completed the comprehensive guide to Python Classes and Objects. Here's what you've learned:

### Key Concepts Mastered:
- ✅ **Class Definition**: How to create and structure classes
- ✅ **Object Creation**: Instantiating objects from classes
- ✅ **Attributes**: Instance vs class attributes
- ✅ **Methods**: Instance, class, and static methods
- ✅ **Constructor**: The `__init__` method
- ✅ **Properties**: Using decorators for computed attributes
- ✅ **Best Practices**: Naming, documentation, and design principles

### Next Steps:
1. **Practice**: Work through the exercises to reinforce your learning
2. **Build Projects**: Apply these concepts to real-world problems
3. **Learn Inheritance**: Move on to the inheritance tutorial
4. **Explore Polymorphism**: Understand method overriding and duck typing
5. **Study Design Patterns**: Learn common OOP patterns

### Remember:
- **Practice makes perfect** - The more you code, the more natural OOP becomes
- **Start simple** - Begin with basic classes and gradually add complexity
- **Read others' code** - Study well-written Python libraries and frameworks
- **Refactor regularly** - Improve your class designs as you learn more

Happy coding! 🐍✨

---

*This tutorial is part of the Python Practices repository. For more advanced topics, check out the other tutorials in this series.*