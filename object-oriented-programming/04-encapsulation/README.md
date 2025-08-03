# Encapsulation 🔒

Master encapsulation in Python - the practice of hiding internal implementation details and controlling access to object data through well-defined interfaces.

## 🎯 Learning Objectives

- Understand private and protected attributes in Python
- Master property decorators for controlled access
- Implement data validation and business logic in setters
- Learn the descriptor protocol for advanced property management
- Create immutable objects and data structures
- Apply encapsulation patterns in real-world scenarios
- Work with observable properties and lazy evaluation

## 📚 Exercises

### Intermediate Level (🟡)

1. **[Private Account Attributes](./01-private-account-attributes.py)** - Banking System Basics
   - Basic encapsulation with account management
   - Deposit, withdraw, and transfer operations
   - Simple data protection and method design
   - Financial transaction validation

2. **[Private Person Data](./02-private-person-data.py)** - Personal Information Management
   - Private attributes with underscore convention
   - Getter and setter methods for controlled access
   - Data validation for personal information
   - Age and name validation patterns

3. **[Protected Bank Attributes](./03-protected-bank-attributes.py)** - Inheritance-Safe Design
   - Protected attributes with single underscore
   - Inheritance-friendly encapsulation
   - Bank account hierarchy design
   - Balance protection across subclasses

4. **[Property Decorators Product](./04-property-decorators-product.py)** - Modern Python Properties
   - `@property` decorator for getters
   - `@property.setter` for validation
   - Price and name validation logic
   - Discount application with business rules

5. **[Advanced Property Decorators](./05-advanced-property-decorators.py)** - Complex Validation
   - Advanced property patterns
   - Multi-level validation logic
   - Employee salary management
   - Complex business rule implementation

### Advanced Level (🟠)

6. **[Immutable Point Objects](./06-immutable-point-objects.py)** - Immutability Patterns
   - Creating truly immutable objects
   - `__slots__` for memory efficiency
   - Coordinate system implementation
   - Preventing object modification after creation

7. **[Observable Property Descriptors](./07-observable-property-descriptors.py)** - Descriptor Protocol
   - Custom descriptor implementation
   - Observer pattern with properties
   - Automatic change notification
   - Advanced property behavior customization

8. **[Immutable Dictionary Collections](./08-immutable-dictionary-collections.py)** - Collection Immutability
   - Extending built-in collections
   - Preventing modification of dictionary data
   - Immutable data structure patterns
   - Collection-level encapsulation

9. **[Lazy Property Descriptors](./09-lazy-property-descriptors.py)** - Performance Optimization
   - Lazy evaluation with descriptors
   - Caching expensive computations
   - On-demand property calculation
   - Memory and performance optimization

## 🔑 Key Concepts

### Private Attributes (Name Mangling)
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private (name mangled)
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

### Protected Attributes (Convention)
```python
class Vehicle:
    def __init__(self, make, model):
        self._make = make      # Protected (convention)
        self._model = model
        self._mileage = 0

class Car(Vehicle):
    def drive(self, miles):
        self._mileage += miles  # Accessible in subclass
```

### Property Decorators
```python
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
```

### Immutable Objects
```python
class ImmutablePoint:
    __slots__ = ('_x', '_y')
    
    def __init__(self, x, y):
        object.__setattr__(self, '_x', x)
        object.__setattr__(self, '_y', y)
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify immutable object")
```

### Descriptor Protocol
```python
class ValidatedProperty:
    def __init__(self, validator=None):
        self.validator = validator
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)
    
    def __set__(self, obj, value):
        if self.validator:
            self.validator(value)
        setattr(obj, self.name, value)

class Person:
    def validate_age(value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
    
    age = ValidatedProperty(validate_age)
```

### Lazy Properties
```python
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        # Check if value is already cached
        cache_name = f'_cached_{self.name}'
        if hasattr(obj, cache_name):
            return getattr(obj, cache_name)
        
        # Compute and cache the value
        value = self.func(obj)
        setattr(obj, cache_name, value)
        return value

class DataProcessor:
    @LazyProperty
    def expensive_calculation(self):
        print("Computing expensive result...")
        return sum(range(1000000))  # Expensive operation
```

## 🎓 Progressive Learning Path

### Start Here (Foundation)
1. **Private Account Attributes** - Learn basic encapsulation concepts
2. **Private Person Data** - Practice with getter/setter methods
3. **Protected Bank Attributes** - Understand inheritance-safe design

### Build Property Skills
4. **Property Decorators Product** - Master `@property` decorator
5. **Advanced Property Decorators** - Complex validation patterns

### Advanced Patterns
6. **Immutable Point Objects** - Create unchangeable objects
7. **Observable Property Descriptors** - Custom descriptor implementation
8. **Immutable Dictionary Collections** - Collection-level immutability
9. **Lazy Property Descriptors** - Performance optimization techniques

## 🔐 Encapsulation Levels

### Public Attributes
```python
class Person:
    def __init__(self, name):
        self.name = name  # Public - accessible everywhere
```

### Protected Attributes (Single Underscore)
```python
class Person:
    def __init__(self, name):
        self._name = name  # Protected - internal use, accessible in subclasses
```

### Private Attributes (Double Underscore)
```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private - name mangled, harder to access
    
    def get_name(self):
        return self.__name  # Controlled access through methods
```

## 💡 Best Practices

### ✅ Do This
- **Use properties for validation** - Control how data is set and retrieved
- **Follow naming conventions** - Single underscore for protected, double for private
- **Validate in setters** - Ensure data integrity at the point of entry
- **Provide controlled access** - Use methods and properties instead of direct access
- **Design for inheritance** - Use protected attributes when subclasses need access
- **Create immutable objects** - When data shouldn't change after creation

### ❌ Avoid This
- **Don't expose internal state** - Keep implementation details hidden
- **Don't skip validation** - Always validate data in setters
- **Don't use private attributes unnecessarily** - Use them only when truly needed
- **Don't break encapsulation in tests** - Test through public interfaces
- **Don't make everything private** - Use appropriate access levels

## 🔍 Common Patterns

### Validation Pattern
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
        if '@' not in value:
            raise ValueError("Invalid email address")
        self._address = value
```

### Builder Pattern with Encapsulation
```python
class ConfigBuilder:
    def __init__(self):
        self._config = {}
    
    def set_database_url(self, url):
        self._config['db_url'] = url
        return self
    
    def set_debug_mode(self, debug):
        self._config['debug'] = bool(debug)
        return self
    
    def build(self):
        return ImmutableConfig(self._config)

class ImmutableConfig:
    def __init__(self, config):
        self._config = config.copy()
    
    def get(self, key, default=None):
        return self._config.get(key, default)
```

### Observer Pattern with Properties
```python
class Observable:
    def __init__(self):
        self._observers = []
        self._value = None
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        self._notify_observers(old_value, new_value)
    
    def _notify_observers(self, old_value, new_value):
        for observer in self._observers:
            observer(old_value, new_value)
```

## 🚀 Getting Started

1. **Start with [Private Account Attributes](./01-private-account-attributes.py)** - Learn fundamental encapsulation
2. **Progress through property examples** - Master controlled access patterns
3. **Experiment with validation** - Try different validation rules
4. **Explore advanced patterns** - Descriptors, immutability, and lazy evaluation

## 🎯 Learning Tips

- **Think about data integrity** - What validation rules make sense?
- **Consider the interface** - How should users interact with your objects?
- **Practice with real scenarios** - Banking, user management, configuration
- **Test edge cases** - What happens with invalid data?
- **Understand the trade-offs** - Performance vs. safety vs. flexibility

## 🧪 Practice Challenges

After completing the exercises, try these extensions:

1. **Create a validated user registration system** - Email, password, age validation
2. **Build a configuration manager** - Immutable settings with validation
3. **Implement a shopping cart** - Price calculations with business rules
4. **Design a file system abstraction** - Controlled access to file operations
5. **Create a caching decorator** - Lazy evaluation with expiration

---

Ready to master encapsulation? Start with [Private Account Attributes](./01-private-account-attributes.py)! 🎯