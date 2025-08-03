# Encapsulation in Python - Comprehensive Tutorial

## Table of Contents
1. [Introduction to Encapsulation](#introduction)
2. [Understanding Access Levels](#access-levels)
3. [Basic Encapsulation Concepts](#basic-concepts)
4. [Property Decorators](#property-decorators)
5. [Advanced Encapsulation Techniques](#advanced-techniques)
6. [Real-World Applications](#real-world-applications)
7. [Best Practices](#best-practices)
8. [Common Pitfalls](#common-pitfalls)
9. [Exercises and Practice](#exercises)

---

## Introduction to Encapsulation {#introduction}

**Encapsulation** is one of the four fundamental principles of Object-Oriented Programming (OOP), alongside inheritance, polymorphism, and abstraction. It's the practice of bundling data (attributes) and methods that operate on that data within a single unit (class), while restricting direct access to some of the object's components.

### Why Encapsulation Matters

🎯 **Key Benefits:**
- **Data Protection**: Prevents unauthorized access and modification
- **Code Maintainability**: Changes to internal implementation don't affect external code
- **Validation**: Ensures data integrity through controlled access
- **Abstraction**: Hides complex implementation details from users
- **Security**: Protects sensitive information from direct manipulation

### Real-World Analogy

Think of encapsulation like a **car's dashboard**:
- You can see the speedometer, fuel gauge, and controls (public interface)
- You can't directly access the engine internals (private implementation)
- You interact through standardized controls (methods)
- The car protects you from dangerous components while giving you what you need

---

## Understanding Access Levels {#access-levels}

Python uses naming conventions to indicate different levels of access:

### 1. Public Attributes (No Prefix)
```python
class Car:
    def __init__(self):
        self.brand = "Toyota"  # Public - accessible everywhere
```

### 2. Protected Attributes (Single Underscore `_`)
```python
class Car:
    def __init__(self):
        self._engine_type = "V6"  # Protected - intended for internal use
```

### 3. Private Attributes (Double Underscore `__`)
```python
class Car:
    def __init__(self):
        self.__serial_number = "ABC123"  # Private - name mangled
```

### Access Level Comparison

| Access Level | Syntax | Visibility | Use Case |
|-------------|--------|------------|----------|
| Public | `attribute` | Everywhere | External interface |
| Protected | `_attribute` | Class & subclasses | Internal implementation |
| Private | `__attribute` | Current class only | Sensitive data |

---

## Basic Encapsulation Concepts {#basic-concepts}

### 1. Simple Private Attributes

Let's start with a basic example of encapsulation:

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number  # Protected
        self.__balance = initial_balance       # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        return self.__balance
```

**Key Points:**
- `_account_number` is protected (internal use)
- `__balance` is private (name mangled to `_BankAccount__balance`)
- Methods provide controlled access to private data

### 2. Understanding Name Mangling

```python
class Example:
    def __init__(self):
        self.public = "Everyone can see this"
        self._protected = "Internal use (convention)"
        self.__private = "Name mangled"

# Demonstration
obj = Example()
print(obj.public)           # ✅ Works
print(obj._protected)       # ✅ Works (but shouldn't be used externally)
# print(obj.__private)      # ❌ AttributeError
print(obj._Example__private) # ✅ Works (name mangling revealed)
```

### 3. Validation Through Encapsulation

```python
class Person:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.set_name(name)  # Use setter for validation
        self.set_age(age)
    
    def set_name(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name.strip()
        else:
            raise ValueError("Name must be a non-empty string")
    
    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 150:
            self._age = age
        else:
            raise ValueError("Age must be between 0 and 150")
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
```

---

## Property Decorators {#property-decorators}

Properties provide a Pythonic way to implement getters and setters while maintaining the simplicity of attribute access.

### 1. Basic Property Usage

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property for Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature via Fahrenheit"""
        self.celsius = (value - 32) * 5/9

# Usage
temp = Temperature(25)
print(f"Celsius: {temp.celsius}")      # 25
print(f"Fahrenheit: {temp.fahrenheit}") # 77.0

temp.fahrenheit = 100
print(f"Celsius: {temp.celsius}")      # 37.77777777777778
```

### 2. Read-Only Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Read-only computed property"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """Read-only computed property"""
        import math
        return 2 * math.pi * self._radius

# Usage
circle = Circle(5)
print(f"Area: {circle.area:.2f}")           # Area: 78.54
print(f"Circumference: {circle.circumference:.2f}") # Circumference: 31.42

# circle.area = 100  # ❌ AttributeError: can't set attribute
```

### 3. Property with Deleter

```python
class CacheManager:
    def __init__(self):
        self._cache = {}
        self._data = None
    
    @property
    def data(self):
        if self._data is None:
            print("Loading data...")
            self._data = "Expensive computation result"
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self._cache.clear()  # Clear cache when data changes
    
    @data.deleter
    def data(self):
        print("Clearing data and cache...")
        self._data = None
        self._cache.clear()

# Usage
cache = CacheManager()
print(cache.data)  # Loading data... Expensive computation result
cache.data = "New data"
del cache.data     # Clearing data and cache...
```

---

## Advanced Encapsulation Techniques {#advanced-techniques}

### 1. Descriptors

Descriptors provide the most powerful way to customize attribute access:

```python
class ValidatedAttribute:
    def __init__(self, validator=None, default=None):
        self.validator = validator
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, self.default)
    
    def __set__(self, instance, value):
        if self.validator and not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        setattr(instance, self.name, value)

# Validators
def positive_number(value):
    return isinstance(value, (int, float)) and value > 0

def non_empty_string(value):
    return isinstance(value, str) and len(value.strip()) > 0

class Product:
    name = ValidatedAttribute(non_empty_string)
    price = ValidatedAttribute(positive_number)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Usage
product = Product("Laptop", 999.99)
print(f"{product.name}: ${product.price}")

# product.price = -100  # ❌ ValueError: Invalid value for _price: -100
```

### 2. Lazy Properties

```python
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        # Check if value is already computed
        attr_name = f'_lazy_{self.name}'
        if not hasattr(instance, attr_name):
            # Compute and cache the value
            value = self.func(instance)
            setattr(instance, attr_name, value)
        
        return getattr(instance, attr_name)

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @LazyProperty
    def processed_data(self):
        print("Processing data... (expensive operation)")
        # Simulate expensive computation
        import time
        time.sleep(1)
        return [x * 2 for x in self.data]
    
    @LazyProperty
    def statistics(self):
        print("Computing statistics...")
        processed = self.processed_data  # Uses cached value if available
        return {
            'sum': sum(processed),
            'avg': sum(processed) / len(processed),
            'max': max(processed),
            'min': min(processed)
        }

# Usage
processor = DataProcessor([1, 2, 3, 4, 5])
print("First access:")
print(processor.processed_data)  # Processing data... [2, 4, 6, 8, 10]
print("Second access:")
print(processor.processed_data)  # [2, 4, 6, 8, 10] (cached)
```

---

## Real-World Applications {#real-world-applications}

### 1. Database Connection Manager

```python
class DatabaseConnection:
    def __init__(self, host, port, database):
        self._host = host
        self._port = port
        self._database = database
        self.__connection = None
        self.__is_connected = False
    
    @property
    def is_connected(self):
        return self.__is_connected
    
    def connect(self):
        if not self.__is_connected:
            print(f"Connecting to {self._database} at {self._host}:{self._port}")
            # Simulate connection
            self.__connection = f"connection_to_{self._database}"
            self.__is_connected = True
        return self.__connection
    
    def disconnect(self):
        if self.__is_connected:
            print("Disconnecting from database")
            self.__connection = None
            self.__is_connected = False
    
    def execute_query(self, query):
        if not self.__is_connected:
            raise RuntimeError("Must connect to database first")
        print(f"Executing: {query}")
        return f"Result of {query}"
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

# Usage
with DatabaseConnection("localhost", 5432, "myapp") as db:
    result = db.execute_query("SELECT * FROM users")
    print(result)
```

### 2. Configuration Manager

```python
class ConfigManager:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.__config = {}
            self.__readonly_keys = set()
            self._initialized = True
    
    def set(self, key, value, readonly=False):
        if key in self.__readonly_keys:
            raise ValueError(f"Configuration key '{key}' is read-only")
        self.__config[key] = value
        if readonly:
            self.__readonly_keys.add(key)
    
    def get(self, key, default=None):
        return self.__config.get(key, default)
    
    def get_all(self):
        return self.__config.copy()
    
    @property
    def readonly_keys(self):
        return self.__readonly_keys.copy()

# Usage
config = ConfigManager()
config.set("database_url", "postgresql://localhost/mydb", readonly=True)
config.set("debug", True)

print(config.get("database_url"))  # postgresql://localhost/mydb
# config.set("database_url", "new_url")  # ❌ ValueError: read-only
```

### 3. Event System

```python
class Event:
    def __init__(self, name):
        self._name = name
        self._handlers = []
    
    @property
    def name(self):
        return self._name
    
    def subscribe(self, handler):
        if callable(handler):
            self._handlers.append(handler)
        else:
            raise ValueError("Handler must be callable")
    
    def unsubscribe(self, handler):
        if handler in self._handlers:
            self._handlers.remove(handler)
    
    def emit(self, *args, **kwargs):
        for handler in self._handlers:
            try:
                handler(*args, **kwargs)
            except Exception as e:
                print(f"Error in event handler: {e}")

class EventManager:
    def __init__(self):
        self.__events = {}
    
    def create_event(self, event_name):
        if event_name not in self.__events:
            self.__events[event_name] = Event(event_name)
        return self.__events[event_name]
    
    def get_event(self, event_name):
        return self.__events.get(event_name)
    
    @property
    def event_names(self):
        return list(self.__events.keys())

# Usage
event_manager = EventManager()
user_login = event_manager.create_event("user_login")

def log_login(username):
    print(f"User {username} logged in")

def send_welcome_email(username):
    print(f"Sending welcome email to {username}")

user_login.subscribe(log_login)
user_login.subscribe(send_welcome_email)

user_login.emit("alice")  # Triggers both handlers
```

---

## Best Practices {#best-practices}

### 1. Choose the Right Access Level

```python
class BestPracticeExample:
    def __init__(self, public_data, internal_data, sensitive_data):
        # Public: Part of the API, safe to access
        self.public_data = public_data
        
        # Protected: Internal implementation, may change
        self._internal_data = internal_data
        
        # Private: Sensitive or implementation-specific
        self.__sensitive_data = sensitive_data
    
    # Public method: Part of the API
    def get_summary(self):
        return f"Data: {self.public_data}"
    
    # Protected method: For subclasses
    def _process_internal_data(self):
        return self._internal_data.upper()
    
    # Private method: Implementation detail
    def __validate_sensitive_data(self):
        return len(self.__sensitive_data) > 0
```

### 2. Use Properties for Computed Values

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        """Computed property - always up to date"""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Computed property - always up to date"""
        return 2 * (self._width + self._height)
```

### 3. Validate Data in Setters

```python
class Email:
    def __init__(self, address):
        self._address = None
        self.address = address  # Use setter for validation
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        if not self._is_valid_email(value):
            raise ValueError(f"Invalid email address: {value}")
        self._address = value
    
    @staticmethod
    def _is_valid_email(email):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @property
    def domain(self):
        return self._address.split('@')[1] if self._address else None
    
    @property
    def username(self):
        return self._address.split('@')[0] if self._address else None
```

---

## Common Pitfalls {#common-pitfalls}

### 1. Overusing Private Attributes

❌ **Bad:**
```python
class OverEncapsulated:
    def __init__(self, x, y):
        self.__x = x  # Unnecessary private
        self.__y = y  # Unnecessary private
    
    def __get_x(self):  # Unnecessary private method
        return self.__x
```

✅ **Good:**
```python
class WellEncapsulated:
    def __init__(self, x, y):
        self._x = x  # Protected is often sufficient
        self._y = y
    
    @property
    def x(self):
        return self._x
```

### 2. Not Using Properties for Validation

❌ **Bad:**
```python
class BadValidation:
    def __init__(self, age):
        self.age = age  # No validation
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age  # Still allows direct access
```

✅ **Good:**
```python
class GoodValidation:
    def __init__(self, age):
        self._age = None
        self.age = age  # Uses property setter
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

### 3. Inconsistent Access Patterns

❌ **Bad:**
```python
class InconsistentAccess:
    def __init__(self, name, email):
        self.name = name      # Public
        self._email = email   # Protected
    
    def get_name(self):       # Unnecessary getter for public attribute
        return self.name
    
    # No getter for email, but it's protected
```

✅ **Good:**
```python
class ConsistentAccess:
    def __init__(self, name, email):
        self._name = name
        self._email = email
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
```

---

## Exercises and Practice {#exercises}

### Beginner Level

1. **Basic Encapsulation**
   - Create a `Student` class with private attributes for name, age, and grades
   - Add methods to safely access and modify these attributes
   - Include validation for age (0-100) and grades (0-100)

2. **Property Practice**
   - Create a `Rectangle` class using properties for width and height
   - Add computed properties for area and perimeter
   - Ensure width and height are always positive

### Intermediate Level

3. **Bank Account System**
   - Create a `BankAccount` class with encapsulated balance
   - Add methods for deposit, withdraw, and transfer
   - Include transaction history and account validation

4. **Temperature Converter**
   - Create a `Temperature` class that stores Celsius internally
   - Add properties for Fahrenheit and Kelvin conversion
   - Include validation for absolute zero

### Advanced Level

5. **Custom Descriptor**
   - Create a `TypedAttribute` descriptor that enforces type checking
   - Use it in a `Person` class for name (str) and age (int)
   - Add optional default values and custom error messages

6. **Observable Pattern**
   - Create an `ObservableList` class that notifies observers of changes
   - Implement add, remove, and clear methods
   - Allow multiple observers with different notification preferences

### Expert Level

7. **Lazy Loading System**
   - Create a `LazyLoader` descriptor for expensive computations
   - Add cache invalidation based on dependent attributes
   - Implement thread-safe lazy loading

8. **Configuration Manager**
   - Create a singleton `Config` class with encapsulated settings
   - Support nested configuration with dot notation access
   - Add validation, type checking, and change notifications

---

## Summary

Encapsulation is a powerful principle that helps you:

- **Protect data** from unauthorized access and modification
- **Maintain code quality** through controlled interfaces
- **Enable validation** and business rule enforcement
- **Improve maintainability** by hiding implementation details
- **Provide clear APIs** for other developers

### Key Takeaways

1. **Use appropriate access levels**: Public for APIs, protected for internal use, private for sensitive data
2. **Leverage properties**: They provide clean syntax with powerful functionality
3. **Validate data**: Always validate inputs in setters and methods
4. **Be consistent**: Follow the same patterns throughout your codebase
5. **Don't over-encapsulate**: Balance protection with usability

### Next Steps

- Practice with the provided exercises
- Explore the example files in this directory
- Study real-world codebases to see encapsulation in action
- Experiment with advanced techniques like descriptors and metaclasses

Remember: Encapsulation is not about hiding everything—it's about providing the right level of access for each piece of data and functionality in your system.

---