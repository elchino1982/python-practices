# Object-Oriented Programming (OOP) in Python Cheat Sheet

## 1. Classes and Objects

### Class Definition:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)
```

### Creating an Object:

```python
obj = MyClass(10)
obj.display_value()  # Output: 10
```

## 2. Attributes and Methods

### Instance Attributes:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")
```

### Class Attributes:

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Properties in Python

Properties in Python provide a way to manage the access to instance attributes. They allow you to define methods that get and set the value of an attribute, while still using attribute access syntax.

#### Basic Property Example:

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

#### Using Properties:

```python
person = Person("Alice", 30)
print(person.name)  # Output: Alice
person.age = 31     # Uses the setter
print(person.age)   # Output: 31
```

#### Read-Only Properties:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius
```

#### Deleting a Property:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print("Deleting name")
        del self._name
```

## 3. Inheritance

### Basic Inheritance:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

### Method Overriding:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle starting...")

class Car(Vehicle):
    def start(self):
        print(f"{self.brand} car engine starting...")
```

### Using super():

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed
```

### Multiple Inheritance:

```python
class Flyable:
    def fly(self):
        print("Flying...")

class Swimmable:
    def swim(self):
        print("Swimming...")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")
```

## 4. Polymorphism

### Method Overriding (Runtime Polymorphism):

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphic usage
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(shape.area())
```

### Operator Overloading:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

## 5. Encapsulation

### Private Attributes (Name Mangling):

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

### Protected Attributes (Convention):

```python
class Vehicle:
    def __init__(self):
        self._engine_status = "off"  # Protected attribute

    def _start_engine(self):  # Protected method
        self._engine_status = "on"
```

## 6. Abstraction

### Abstract Base Classes:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

## 7. Special Methods (Magic Methods)

### Common Magic Methods:

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.pages < other.pages
```

## 8. Class Methods and Static Methods

### Class Methods:

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def from_string(cls, name_str):
        return cls(name_str)
```

### Static Methods:

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def is_even(number):
        return number % 2 == 0
```

## 9. Design Patterns

### Singleton Pattern:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory Pattern:

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")
```

### Observer Pattern:

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass
```

## 10. Best Practices

### 1. Use Descriptive Names
```python
# Good
class BankAccount:
    def calculate_interest(self):
        pass

# Avoid
class BA:
    def calc_int(self):
        pass
```

### 2. Keep Classes Focused
```python
# Good - Single Responsibility
class EmailSender:
    def send_email(self, message):
        pass

class EmailValidator:
    def validate_email(self, email):
        pass
```

### 3. Use Composition Over Inheritance
```python
# Good - Composition
class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = [Wheel() for _ in range(4)]

# Sometimes better than deep inheritance
```

### 4. Document Your Classes
```python
class Rectangle:
    """
    A rectangle shape with width and height.
    
    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    """
    
    def __init__(self, width: float, height: float):
        """
        Initialize a rectangle.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height
```

## Quick Reference

### Class Structure Template:
```python
class ClassName:
    # Class attributes
    class_attribute = "value"
    
    def __init__(self, parameters):
        # Instance attributes
        self.instance_attribute = parameters
    
    def instance_method(self):
        # Instance method
        return self.instance_attribute
    
    @classmethod
    def class_method(cls):
        # Class method
        return cls.class_attribute
    
    @staticmethod
    def static_method():
        # Static method
        return "static result"
    
    @property
    def property_name(self):
        # Property getter
        return self._private_attribute
    
    @property_name.setter
    def property_name(self, value):
        # Property setter
        self._private_attribute = value
```

---

*This cheat sheet covers the essential concepts of Object-Oriented Programming in Python. Practice these concepts with real examples to master OOP!*