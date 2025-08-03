# Python Polymorphism: Complete Tutorial 🔄

Welcome to the comprehensive guide to Python Polymorphism! This tutorial covers one of the most powerful and elegant features of Object-Oriented Programming, designed for learners from beginner to expert level.

## 📚 Table of Contents

1. [Introduction to Polymorphism](#introduction-to-polymorphism)
2. [What is Polymorphism?](#what-is-polymorphism)
3. [Types of Polymorphism](#types-of-polymorphism)
4. [Method Overriding](#method-overriding)
5. [Duck Typing](#duck-typing)
6. [Operator Overloading](#operator-overloading)
7. [Abstract Base Classes and Polymorphism](#abstract-base-classes-and-polymorphism)
8. [Protocol-Based Polymorphism](#protocol-based-polymorphism)
9. [Function and Method Overloading](#function-and-method-overloading)
10. [Advanced Polymorphic Patterns](#advanced-polymorphic-patterns)
11. [Best Practices](#best-practices)
12. [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)
13. [Real-World Examples](#real-world-examples)
14. [Performance Considerations](#performance-considerations)
15. [Exercises and Practice](#exercises-and-practice)

---

## Introduction to Polymorphism

### What is Polymorphism?

Polymorphism comes from Greek words "poly" (many) and "morph" (form), meaning "many forms." In programming, polymorphism allows objects of different types to be treated as instances of the same type through a common interface.

**Real-world analogy**: 
- A **remote control** can operate different devices (TV, stereo, DVD player) using the same buttons
- A **driver** can operate different vehicles (car, truck, motorcycle) using similar controls
- A **pen** can write on different surfaces (paper, whiteboard, tablet) but the writing action is the same

### Why Use Polymorphism?

1. **Code Flexibility**: Write code that works with multiple types
2. **Extensibility**: Add new types without changing existing code
3. **Maintainability**: Reduce code duplication and coupling
4. **Abstraction**: Focus on what objects do, not what they are
5. **Reusability**: Create generic algorithms that work with many types

### Key Benefits

- **Uniform Interface**: Treat different objects the same way
- **Runtime Flexibility**: Behavior determined at runtime, not compile time
- **Open/Closed Principle**: Open for extension, closed for modification
- **Loose Coupling**: Reduce dependencies between components

---

## What is Polymorphism?

### The Core Concept

Polymorphism allows a single interface to represent different underlying forms (data types). It enables you to write code that can work with objects of multiple types, as long as they support the required operations.

```python
# Basic polymorphism example
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Polymorphic function - works with any Animal
def animal_concert(animals):
    for animal in animals:
        print(animal.make_sound())  # Same method call, different behaviors

# Usage - all different types, same interface
animals = [Dog(), Cat(), Cow(), Dog(), Cat()]
animal_concert(animals)
# Output:
# Woof!
# Meow!
# Moo!
# Woof!
# Meow!
```

### Polymorphism vs Other Concepts

#### Polymorphism vs Inheritance
```python
# Inheritance creates relationships
class Vehicle:
    def start(self):
        return "Vehicle starting"

class Car(Vehicle):  # Car IS-A Vehicle
    def start(self):
        return "Car engine starting"

# Polymorphism enables uniform treatment
def start_vehicle(vehicle):  # Works with any Vehicle
    return vehicle.start()

car = Car()
print(start_vehicle(car))  # Polymorphic call
```

#### Polymorphism vs Encapsulation
```python
# Encapsulation hides implementation details
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Hidden implementation
    
    def withdraw(self, amount):  # Public interface
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

# Polymorphism allows different account types with same interface
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        # Different implementation, same interface
        if amount <= self._balance * 0.9:  # Keep 10% minimum
            self._balance -= amount
            return True
        return False

def process_withdrawal(account, amount):  # Polymorphic function
    return account.withdraw(amount)  # Same call, different behavior
```

### Interface-Based Thinking

```python
# Think in terms of capabilities, not types
class Drawable:
    def draw(self):
        raise NotImplementedError

class Circle(Drawable):
    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        return f"Drawing circle with radius {self.radius}"

class Rectangle(Drawable):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self):
        return f"Drawing rectangle {self.width}x{self.height}"

class Triangle(Drawable):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def draw(self):
        return f"Drawing triangle with base {self.base} and height {self.height}"

# Polymorphic drawing function
def render_shapes(shapes):
    for shape in shapes:
        print(shape.draw())  # Same method, different implementations

# Usage
shapes = [
    Circle(5),
    Rectangle(10, 8),
    Triangle(6, 4),
    Circle(3)
]

render_shapes(shapes)
```

---

## Types of Polymorphism

### 1. Runtime Polymorphism (Dynamic Polymorphism)

Runtime polymorphism occurs when the method to be called is determined at runtime based on the actual object type.

```python
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Bank Transfer"

# Runtime polymorphism in action
def handle_payment(processor, amount):
    # The actual method called depends on the runtime type of processor
    return processor.process_payment(amount)

# Different processors, same interface
processors = [
    CreditCardProcessor(),
    PayPalProcessor(),
    BankTransferProcessor()
]

for processor in processors:
    print(handle_payment(processor, 100))
```

### 2. Compile-time Polymorphism (Static Polymorphism)

In Python, this is achieved through method overloading and operator overloading.

```python
class Calculator:
    def add(self, a, b=None, c=None):
        """Method overloading simulation"""
        if c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

    def __add__(self, other):
        """Operator overloading"""
        return Calculator()  # Simplified example

calc = Calculator()
print(calc.add(5))        # Single argument
print(calc.add(5, 3))     # Two arguments  
print(calc.add(5, 3, 2))  # Three arguments
```

### 3. Parametric Polymorphism (Generics)

Python's dynamic typing provides natural parametric polymorphism.

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self) -> T:
        if not self._items:
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        return len(self._items) == 0

# Same Stack class works with different types
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 2

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # "world"
```

### 4. Subtype Polymorphism

This is the most common form in OOP, where subclasses can be used wherever their parent class is expected.

```python
class Media:
    def __init__(self, title):
        self.title = title
    
    def play(self):
        raise NotImplementedError

class Song(Media):
    def __init__(self, title, artist, duration):
        super().__init__(title)
        self.artist = artist
        self.duration = duration
    
    def play(self):
        return f"♪ Playing song: {self.title} by {self.artist}"

class Video(Media):
    def __init__(self, title, director, length):
        super().__init__(title)
        self.director = director
        self.length = length
    
    def play(self):
        return f"▶ Playing video: {self.title} directed by {self.director}"

class Podcast(Media):
    def __init__(self, title, host, episode):
        super().__init__(title)
        self.host = host
        self.episode = episode
    
    def play(self):
        return f"🎙 Playing podcast: {self.title} hosted by {self.host}"

# Polymorphic playlist
def create_playlist(media_items):
    for item in media_items:
        print(item.play())  # Subtype polymorphism

playlist = [
    Song("Bohemian Rhapsody", "Queen", 355),
    Video("Inception", "Christopher Nolan", 148),
    Podcast("Python Podcast", "Talk Python", 42),
    Song("Imagine", "John Lennon", 183)
]

create_playlist(playlist)
```

---

## Method Overriding

### Understanding Method Overriding

Method overriding is the foundation of runtime polymorphism. It allows subclasses to provide specific implementations of methods defined in their parent classes.

```python
class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")
    
    def describe(self):
        return f"A {self.color} shape"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):  # Override parent method
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):  # Override parent method
        return 2 * 3.14159 * self.radius
    
    def describe(self):  # Override and extend parent method
        base_description = super().describe()
        return f"{base_description} with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):  # Override parent method
        return self.width * self.height
    
    def perimeter(self):  # Override parent method
        return 2 * (self.width + self.height)
    
    def describe(self):  # Override and extend parent method
        base_description = super().describe()
        return f"{base_description} with dimensions {self.width}x{self.height}"

# Polymorphic usage
def analyze_shapes(shapes):
    for shape in shapes:
        print(f"{shape.describe()}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
        print()

shapes = [
    Circle("red", 5),
    Rectangle("blue", 4, 6),
    Circle("green", 3),
    Rectangle("yellow", 8, 3)
]

analyze_shapes(shapes)
```

### Method Overriding Best Practices

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False
    
    def start(self):
        """Base implementation for starting a vehicle"""
        if not self.is_running:
            self.is_running = True
            return f"{self.make} {self.model} is starting"
        return f"{self.make} {self.model} is already running"
    
    def stop(self):
        """Base implementation for stopping a vehicle"""
        if self.is_running:
            self.is_running = False
            return f"{self.make} {self.model} has stopped"
        return f"{self.make} {self.model} is already stopped"

class Car(Vehicle):
    def start(self):
        # ✅ Good: Call parent method and extend behavior
        result = super().start()
        if self.is_running:
            return f"{result} - Engine running smoothly"
        return result
    
    def stop(self):
        # ✅ Good: Extend parent behavior
        result = super().stop()
        if not self.is_running:
            return f"{result} - Engine off"
        return result

class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_level=100):
        super().__init__(make, model)
        self.battery_level = battery_level
    
    def start(self):
        # ✅ Good: Check preconditions before calling parent
        if self.battery_level <= 0:
            return f"Cannot start {self.make} {self.model} - battery empty"
        
        result = super().start()
        if self.is_running:
            return f"{result} - Electric motor activated"
        return result
    
    def charge(self):
        """Electric car specific method"""
        self.battery_level = 100
        return f"{self.make} {self.model} battery charged to 100%"

# Polymorphic vehicle operations
def test_vehicles(vehicles):
    for vehicle in vehicles:
        print(vehicle.start())
        print(vehicle.stop())
        
        # Check for electric car specific features
        if hasattr(vehicle, 'charge'):
            print(vehicle.charge())
        print()

vehicles = [
    Car("Toyota", "Camry"),
    ElectricCar("Tesla", "Model 3", 50),
    Car("Honda", "Civic"),
    ElectricCar("Nissan", "Leaf", 0)
]

test_vehicles(vehicles)
```

---

## Duck Typing

### What is Duck Typing?

Duck typing is a concept related to dynamic typing where the type or class of an object is less important than the methods it defines. "If it walks like a duck and quacks like a duck, then it must be a duck."

```python
# Duck typing example - no inheritance required!
class Duck:
    def quack(self):
        return "Quack quack!"
    
    def fly(self):
        return "Duck flying with wings"

class Airplane:
    def quack(self):
        return "Airplane horn: HONK!"
    
    def fly(self):
        return "Airplane flying with engines"

class Robot:
    def quack(self):
        return "Robot sound: BEEP BEEP!"
    
    def fly(self):
        return "Robot flying with propellers"

# Duck typing in action - no common base class needed!
def make_it_fly_and_quack(thing):
    print(thing.quack())
    print(thing.fly())

# All work despite being completely different types
things = [Duck(), Airplane(), Robot()]

for thing in things:
    make_it_fly_and_quack(thing)
    print()
```

### Practical Duck Typing Examples

#### File-like Objects
```python
import io

class StringBuffer:
    def __init__(self):
        self.buffer = ""
    
    def write(self, text):
        self.buffer += text
    
    def read(self):
        return self.buffer
    
    def close(self):
        pass  # Nothing to close for string buffer

class FileLogger:
    def __init__(self):
        self.logs = []
    
    def write(self, text):
        self.logs.append(text)
    
    def read(self):
        return "\n".join(self.logs)
    
    def close(self):
        print("Logger closed")

# Duck typing - any object with write() method works
def log_message(file_like_object, message):
    file_like_object.write(f"[LOG] {message}\n")

# All these work as "file-like" objects
outputs = [
    open("tmp_rovodev_test.txt", "w"),  # Real file
    io.StringIO(),                      # String IO
    StringBuffer(),                     # Custom string buffer
    FileLogger()                        # Custom logger
]

for output in outputs:
    log_message(output, "Hello, World!")
    output.close()

# Clean up
import os
if os.path.exists("tmp_rovodev_test.txt"):
    os.remove("tmp_rovodev_test.txt")
```

#### Iterator Protocol
```python
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

class FibonacciSequence:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

# Duck typing with iteration protocol
def process_sequence(iterable):
    for item in iterable:  # Works with any iterable
        print(f"Processing: {item}")

# All work as iterables
sequences = [
    CountDown(5),
    FibonacciSequence(8),
    [1, 2, 3, 4, 5],  # Built-in list
    "hello"           # Built-in string
]

for seq in sequences:
    print(f"Processing {type(seq).__name__}:")
    process_sequence(seq)
    print()
```

### Duck Typing vs Formal Interfaces

```python
# Traditional approach with formal interface
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawable):
    def draw(self):
        return "Drawing circle"

# Duck typing approach - no formal interface
class Square:  # No inheritance!
    def draw(self):
        return "Drawing square"

class Triangle:  # No inheritance!
    def draw(self):
        return "Drawing triangle"

# Both approaches work polymorphically
def render_all(shapes):
    for shape in shapes:
        print(shape.draw())  # Duck typing - just needs draw() method

shapes = [Circle(), Square(), Triangle()]
render_all(shapes)
```

---

## Operator Overloading

### Understanding Operator Overloading

Operator overloading allows you to define how operators work with your custom classes by implementing special methods (magic methods).

### Basic Arithmetic Operators

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Addition: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other):
        """Multiplication: v1 * scalar or v1 * v2 (dot product)"""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Dot product
        return NotImplemented
    
    def __rmul__(self, other):
        """Right multiplication: scalar * v1"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Division: v1 / scalar"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    def __neg__(self):
        """Negation: -v1"""
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        """Absolute value: abs(v1) - magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

# Usage examples
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"3 * v1 = {3 * v1}")
print(f"v1 * v2 = {v1 * v2}")  # Dot product
print(f"v1 / 2 = {v1 / 2}")
print(f"-v1 = {-v1}")
print(f"|v1| = {abs(v1)}")
```

### Comparison Operators

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        """Equality: student1 == student2"""
        if isinstance(other, Student):
            return self.grade == other.grade
        return NotImplemented
    
    def __lt__(self, other):
        """Less than: student1 < student2"""
        if isinstance(other, Student):
            return self.grade < other.grade
        return NotImplemented
    
    def __le__(self, other):
        """Less than or equal: student1 <= student2"""
        if isinstance(other, Student):
            return self.grade <= other.grade
        return NotImplemented
    
    def __gt__(self, other):
        """Greater than: student1 > student2"""
        if isinstance(other, Student):
            return self.grade > other.grade
        return NotImplemented
    
    def __ge__(self, other):
        """Greater than or equal: student1 >= student2"""
        if isinstance(other, Student):
            return self.grade >= other.grade
        return NotImplemented
    
    def __ne__(self, other):
        """Not equal: student1 != student2"""
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
    
    def __str__(self):
        return f"{self.name} (Grade: {self.grade})"

# Usage
students = [
    Student("Alice", 85),
    Student("Bob", 92),
    Student("Charlie", 78),
    Student("Diana", 92)
]

# Sorting uses comparison operators
students.sort()  # Uses __lt__ for sorting
print("Students sorted by grade:")
for student in students:
    print(student)

print(f"\nBob == Diana: {students[1] == students[3]}")  # Same grade
print(f"Alice < Bob: {students[0] < students[1]}")
```

### Container Operators

```python
class Matrix:
    def __init__(self, rows):
        self.rows = [list(row) for row in rows]
        self.height = len(rows)
        self.width = len(rows[0]) if rows else 0
    
    def __getitem__(self, key):
        """Indexing: matrix[i] or matrix[i, j]"""
        if isinstance(key, tuple):
            row, col = key
            return self.rows[row][col]
        else:
            return self.rows[key]
    
    def __setitem__(self, key, value):
        """Assignment: matrix[i] = value or matrix[i, j] = value"""
        if isinstance(key, tuple):
            row, col = key
            self.rows[row][col] = value
        else:
            self.rows[key] = list(value)
    
    def __len__(self):
        """Length: len(matrix)"""
        return self.height
    
    def __contains__(self, item):
        """Membership: item in matrix"""
        for row in self.rows:
            if item in row:
                return True
        return False
    
    def __iter__(self):
        """Iteration: for row in matrix"""
        return iter(self.rows)
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.rows])

# Usage
matrix = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original matrix:")
print(matrix)

print(f"\nMatrix length: {len(matrix)}")
print(f"Element at [1, 2]: {matrix[1, 2]}")
print(f"Row 0: {matrix[0]}")
print(f"Contains 5: {5 in matrix}")
print(f"Contains 10: {10 in matrix}")

# Modify matrix
matrix[1, 1] = 99
print(f"\nAfter modifying [1, 1] to 99:")
print(matrix)

# Iterate through rows
print("\nIterating through rows:")
for i, row in enumerate(matrix):
    print(f"Row {i}: {row}")
```

---

## Abstract Base Classes and Polymorphism

### Using ABCs for Polymorphic Interfaces

Abstract Base Classes provide a formal way to define interfaces that ensure polymorphic behavior.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Abstract base class for data processors"""
    
    @abstractmethod
    def load_data(self, source):
        """Load data from source"""
        pass
    
    @abstractmethod
    def process_data(self, data):
        """Process the loaded data"""
        pass
    
    @abstractmethod
    def save_data(self, data, destination):
        """Save processed data to destination"""
        pass
    
    # Template method - concrete implementation using abstract methods
    def execute_pipeline(self, source, destination):
        """Execute the complete data processing pipeline"""
        print(f"Starting data processing pipeline...")
        
        # Step 1: Load data
        data = self.load_data(source)
        print(f"Loaded data from {source}")
        
        # Step 2: Process data
        processed_data = self.process_data(data)
        print(f"Processed data")
        
        # Step 3: Save data
        self.save_data(processed_data, destination)
        print(f"Saved data to {destination}")
        
        print("Pipeline completed!")
        return processed_data

class CSVProcessor(DataProcessor):
    def load_data(self, source):
        # Simulate CSV loading
        return [["Name", "Age"], ["Alice", "25"], ["Bob", "30"]]
    
    def process_data(self, data):
        # Convert to uppercase
        return [[cell.upper() if isinstance(cell, str) else cell for cell in row] 
                for row in data]
    
    def save_data(self, data, destination):
        # Simulate CSV saving
        print(f"Saving CSV data: {data}")

class JSONProcessor(DataProcessor):
    def load_data(self, source):
        # Simulate JSON loading
        return {"users": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]}
    
    def process_data(self, data):
        # Add processed flag
        for user in data["users"]:
            user["processed"] = True
        return data
    
    def save_data(self, data, destination):
        # Simulate JSON saving
        print(f"Saving JSON data: {data}")

class XMLProcessor(DataProcessor):
    def load_data(self, source):
        # Simulate XML loading
        return "<users><user name='Alice' age='25'/><user name='Bob' age='30'/></users>"
    
    def process_data(self, data):
        # Add processing timestamp
        return data.replace("<users>", "<users processed='true'>")
    
    def save_data(self, data, destination):
        # Simulate XML saving
        print(f"Saving XML data: {data}")

# Polymorphic usage
def process_multiple_sources(processors, sources, destinations):
    for processor, source, dest in zip(processors, sources, destinations):
        print(f"\n--- Processing with {type(processor).__name__} ---")
        processor.execute_pipeline(source, dest)

processors = [
    CSVProcessor(),
    JSONProcessor(),
    XMLProcessor()
]

sources = ["data.csv", "data.json", "data.xml"]
destinations = ["output.csv", "output.json", "output.xml"]

process_multiple_sources(processors, sources, destinations)
```

### Multiple Inheritance with ABCs

```python
from abc import ABC, abstractmethod

class Readable(ABC):
    @abstractmethod
    def read(self):
        pass

class Writable(ABC):
    @abstractmethod
    def write(self, data):
        pass

class Seekable(ABC):
    @abstractmethod
    def seek(self, position):
        pass

# Multiple inheritance from multiple ABCs
class File(Readable, Writable, Seekable):
    def __init__(self, filename):
        self.filename = filename
        self.position = 0
        self.data = ""
    
    def read(self):
        return self.data[self.position:]
    
    def write(self, data):
        self.data += data
    
    def seek(self, position):
        self.position = max(0, min(position, len(self.data)))

class NetworkStream(Readable, Writable):
    def __init__(self, url):
        self.url = url
        self.buffer = ""
    
    def read(self):
        return f"Reading from {self.url}: {self.buffer}"
    
    def write(self, data):
        self.buffer += data

# Polymorphic functions for different capabilities
def read_from_source(readable):
    return readable.read()

def write_to_destination(writable, data):
    writable.write(data)

def seek_in_stream(seekable, position):
    seekable.seek(position)

# Usage
file_obj = File("test.txt")
network_obj = NetworkStream("http://example.com")

# Both support reading and writing
sources = [file_obj, network_obj]
for source in sources:
    write_to_destination(source, "Hello, World!")
    print(read_from_source(source))

# Only file supports seeking
if isinstance(file_obj, Seekable):
    seek_in_stream(file_obj, 5)
    print(f"After seeking: {read_from_source(file_obj)}")
```

---

## Protocol-Based Polymorphism

### Using typing.Protocol (Python 3.8+)

Protocols provide a way to define structural subtyping (duck typing) with type hints.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...
    
    def get_area(self) -> float:
        ...

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Drawing circle with radius {self.radius}"
    
    def get_area(self) -> float:
        return 3.14159 * self.radius ** 2

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        return f"Drawing rectangle {self.width}x{self.height}"
    
    def get_area(self) -> float:
        return self.width * self.height

# Function that accepts any object following the Drawable protocol
def render_shape(shape: Drawable) -> None:
    print(shape.draw())
    print(f"Area: {shape.get_area()}")

# Both classes satisfy the protocol without explicit inheritance
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    render_shape(shape)
```

### Runtime Checkable Protocols

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Serializable(Protocol):
    def serialize(self) -> str:
        ...
    
    def deserialize(self, data: str) -> None:
        ...

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def serialize(self) -> str:
        return f"{self.name},{self.email}"
    
    def deserialize(self, data: str) -> None:
        parts = data.split(',')
        self.name = parts[0]
        self.email = parts[1]

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def serialize(self) -> str:
        return f"{self.name}:{self.price}"
    
    def deserialize(self, data: str) -> None:
        parts = data.split(':')
        self.name = parts[0]
        self.price = float(parts[1])

def save_object(obj: Serializable) -> str:
    # Runtime check
    if not isinstance(obj, Serializable):
        raise TypeError(f"{type(obj)} does not implement Serializable protocol")
    
    return obj.serialize()

# Usage
user = User("Alice", "alice@example.com")
product = Product("Laptop", 999.99)

print(f"User data: {save_object(user)}")
print(f"Product data: {save_object(product)}")

# Runtime checking
print(f"User implements Serializable: {isinstance(user, Serializable)}")
print(f"Product implements Serializable: {isinstance(product, Serializable)}")
```

---

## Function and Method Overloading

### Simulating Method Overloading

Python doesn't have true method overloading, but we can simulate it using various techniques.

```python
from functools import singledispatch
from typing import Union

class Calculator:
    def add(self, *args):
        """Simulate method overloading with variable arguments"""
        if len(args) == 1:
            return args[0]
        elif len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return sum(args)
    
    def multiply(self, a, b=None, c=None):
        """Simulate overloading with default parameters"""
        if c is not None:
            return a * b * c
        elif b is not None:
            return a * b
        else:
            return a * a  # Square

calc = Calculator()
print(f"add(5): {calc.add(5)}")
print(f"add(5, 3): {calc.add(5, 3)}")
print(f"add(5, 3, 2): {calc.add(5, 3, 2)}")
print(f"add(1, 2, 3, 4, 5): {calc.add(1, 2, 3, 4, 5)}")

print(f"multiply(5): {calc.multiply(5)}")
print(f"multiply(5, 3): {calc.multiply(5, 3)}")
print(f"multiply(5, 3, 2): {calc.multiply(5, 3, 2)}")
```

### Using singledispatch for Function Overloading

```python
@singledispatch
def process_data(data):
    """Default implementation"""
    raise NotImplementedError(f"No implementation for type {type(data)}")

@process_data.register
def _(data: str):
    """Process string data"""
    return f"Processing string: {data.upper()}"

@process_data.register
def _(data: int):
    """Process integer data"""
    return f"Processing integer: {data * 2}"

@process_data.register
def _(data: list):
    """Process list data"""
    return f"Processing list of {len(data)} items: {sorted(data)}"

@process_data.register
def _(data: dict):
    """Process dictionary data"""
    return f"Processing dict with keys: {list(data.keys())}"

# Usage - same function name, different behavior based on type
test_data = [
    "hello world",
    42,
    [3, 1, 4, 1, 5],
    {"name": "Alice", "age": 30}
]

for data in test_data:
    print(process_data(data))
```

### Method Overloading with Type Checking

```python
class MathOperations:
    def power(self, base: Union[int, float], exponent: Union[int, float] = 2):
        """Calculate power with type-based behavior"""
        if isinstance(base, int) and isinstance(exponent, int):
            # Integer power - use built-in pow for efficiency
            return pow(base, exponent)
        else:
            # Float power - use ** operator
            return base ** exponent
    
    def combine(self, a, b):
        """Combine two values based on their types"""
        if isinstance(a, str) and isinstance(b, str):
            return a + " " + b  # Concatenate strings
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b  # Add numbers
        elif isinstance(a, list) and isinstance(b, list):
            return a + b  # Concatenate lists
        elif isinstance(a, dict) and isinstance(b, dict):
            result = a.copy()
            result.update(b)
            return result  # Merge dictionaries
        else:
            return str(a) + str(b)  # Convert to strings and concatenate

math_ops = MathOperations()

# Power operations
print(f"power(2, 3): {math_ops.power(2, 3)}")
print(f"power(2.5, 3.2): {math_ops.power(2.5, 3.2)}")

# Combine operations
print(f"combine('hello', 'world'): {math_ops.combine('hello', 'world')}")
print(f"combine(5, 3): {math_ops.combine(5, 3)}")
print(f"combine([1, 2], [3, 4]): {math_ops.combine([1, 2], [3, 4])}")
print(f"combine({{'a': 1}}, {{'b': 2}}): {math_ops.combine({'a': 1}, {'b': 2})}")
```

---

## Advanced Polymorphic Patterns

### Strategy Pattern with Polymorphism

```python
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, data):
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class QuickSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class MergeSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class DataSorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data)

# Usage
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original data: {data}")

strategies = [
    ("Bubble Sort", BubbleSort()),
    ("Quick Sort", QuickSort()),
    ("Merge Sort", MergeSort())
]

sorter = DataSorter(BubbleSort())

for name, strategy in strategies:
    sorter.set_strategy(strategy)
    sorted_data = sorter.sort_data(data)
    print(f"{name}: {sorted_data}")
```

### Observer Pattern with Polymorphism

```python
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, subject, event_data):
        pass

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self, event_data):
        for observer in self._observers:
            observer.update(self, event_data)

class EmailNotifier(Observer):
    def __init__(self, email):
        self.email = email
    
    def update(self, subject, event_data):
        print(f"📧 Email to {self.email}: {event_data}")

class SMSNotifier(Observer):
    def __init__(self, phone):
        self.phone = phone
    
    def update(self, subject, event_data):
        print(f"📱 SMS to {self.phone}: {event_data}")

class PushNotifier(Observer):
    def __init__(self, device_id):
        self.device_id = device_id
    
    def update(self, subject, event_data):
        print(f"🔔 Push to {self.device_id}: {event_data}")

class LoggerObserver(Observer):
    def update(self, subject, event_data):
        print(f"📝 LOG: {event_data}")

# Usage
news_service = Subject()

# Different types of observers
observers = [
    EmailNotifier("user@example.com"),
    SMSNotifier("+1234567890"),
    PushNotifier("device123"),
    LoggerObserver()
]

# Attach all observers
for observer in observers:
    news_service.attach(observer)

# Notify all observers polymorphically
news_service.notify("Breaking News: Python 4.0 Released!")
```

### Command Pattern with Polymorphism

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class Light:
    def __init__(self, location):
        self.location = location
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"Light in {self.location} is ON")
    
    def turn_off(self):
        self.is_on = False
        print(f"Light in {self.location} is OFF")

class Fan:
    def __init__(self, location):
        self.location = location
        self.speed = 0
    
    def set_speed(self, speed):
        self.speed = speed
        print(f"Fan in {self.location} set to speed {speed}")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
    
    def undo(self):
        self.light.turn_on()

class FanSpeedCommand(Command):
    def __init__(self, fan, speed):
        self.fan = fan
        self.speed = speed
        self.previous_speed = 0
    
    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.set_speed(self.speed)
    
    def undo(self):
        self.fan.set_speed(self.previous_speed)

class RemoteControl:
    def __init__(self):
        self.commands = []
        self.current_command = -1
    
    def execute_command(self, command: Command):
        # Remove any commands after current position
        self.commands = self.commands[:self.current_command + 1]
        
        # Add and execute new command
        self.commands.append(command)
        self.current_command += 1
        command.execute()
    
    def undo(self):
        if self.current_command >= 0:
            command = self.commands[self.current_command]
            command.undo()
            self.current_command -= 1

# Usage
living_room_light = Light("Living Room")
bedroom_fan = Fan("Bedroom")

remote = RemoteControl()

# Create different commands
commands = [
    LightOnCommand(living_room_light),
    FanSpeedCommand(bedroom_fan, 3),
    LightOffCommand(living_room_light),
    FanSpeedCommand(bedroom_fan, 1)
]

# Execute commands polymorphically
for command in commands:
    remote.execute_command(command)
    print()

# Undo operations
print("--- Undoing operations ---")
for _ in range(len(commands)):
    remote.undo()
    print()
```

---

## Best Practices

### 1. Design for Interfaces, Not Implementations

```python
# ❌ Bad - Depends on concrete implementations
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class NotificationManager:
    def __init__(self):
        self.email_service = EmailService()  # Tight coupling
    
    def notify(self, message):
        self.email_service.send_email(message)

# ✅ Good - Depends on abstractions
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"📧 Email: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"📱 SMS: {message}")

class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service  # Loose coupling
    
    def notify(self, message):
        self.service.send(message)

# Easy to extend and test
manager = NotificationManager(EmailService())
manager.notify("Hello World!")

manager = NotificationManager(SMSService())
manager.notify("Hello World!")
```

### 2. Use Composition Over Inheritance for Polymorphism

```python
# ❌ Inheritance-heavy approach
class Animal:
    def move(self):
        pass

class FlyingAnimal(Animal):
    def fly(self):
        print("Flying")

class SwimmingAnimal(Animal):
    def swim(self):
        print("Swimming")

class FlyingSwimmingAnimal(FlyingAnimal, SwimmingAnimal):
    pass  # Complex inheritance hierarchy

# ✅ Composition-based approach
class MovementCapability(ABC):
    @abstractmethod
    def move(self):
        pass

class Flying(MovementCapability):
    def move(self):
        print("Flying through the air")

class Swimming(MovementCapability):
    def move(self):
        print("Swimming in water")

class Walking(MovementCapability):
    def move(self):
        print("Walking on land")

class Animal:
    def __init__(self, name, capabilities):
        self.name = name
        self.capabilities = capabilities
    
    def move_all_ways(self):
        for capability in self.capabilities:
            capability.move()

# Flexible and extensible
duck = Animal("Duck", [Flying(), Swimming(), Walking()])
fish = Animal("Fish", [Swimming()])
bird = Animal("Bird", [Flying(), Walking()])

for animal in [duck, fish, bird]:
    print(f"{animal.name} can:")
    animal.move_all_ways()
    print()
```

### 3. Keep Polymorphic Interfaces Simple

```python
# ❌ Bad - Complex interface
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data, format, options, filters, transformations, validations):
        pass

# ✅ Good - Simple, focused interface
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass

class CSVProcessor(DataProcessor):
    def __init__(self, options=None):
        self.options = options or {}
    
    def process(self, data):
        # Use instance configuration instead of method parameters
        return self._apply_csv_processing(data)
    
    def _apply_csv_processing(self, data):
        # Implementation details
        return data
```

### 4. Use Type Hints for Better Polymorphism

```python
from typing import Protocol, List, Union

class Drawable(Protocol):
    def draw(self) -> str: ...
    def get_area(self) -> float: ...

class Shape:
    def __init__(self, color: str):
        self.color = color

class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
    
    def draw(self) -> str:
        return f"Drawing {self.color} circle"
    
    def get_area(self) -> float:
        return 3.14159 * self.radius ** 2

def render_shapes(shapes: List[Drawable]) -> None:
    for shape in shapes:
        print(shape.draw())
        print(f"Area: {shape.get_area()}")

# Type hints make polymorphic usage clear
shapes: List[Drawable] = [Circle("red", 5)]
render_shapes(shapes)
```

### 5. Handle Edge Cases in Polymorphic Code

```python
class SafeProcessor:
    def process_items(self, items):
        results = []
        for item in items:
            try:
                # Check if item supports the required interface
                if hasattr(item, 'process') and callable(getattr(item, 'process')):
                    result = item.process()
                    results.append(result)
                else:
                    print(f"Warning: {type(item)} doesn't support processing")
            except Exception as e:
                print(f"Error processing {type(item)}: {e}")
                # Continue with other items
        return results

class WorkingItem:
    def process(self):
        return "Processed successfully"

class BrokenItem:
    def process(self):
        raise ValueError("Something went wrong")

class InvalidItem:
    pass  # No process method

# Robust polymorphic processing
processor = SafeProcessor()
items = [WorkingItem(), BrokenItem(), InvalidItem(), WorkingItem()]
results = processor.process_items(items)
print(f"Successfully processed {len(results)} items")
```

---

## Common Pitfalls and Solutions

### 1. Violating the Liskov Substitution Principle

```python
# ❌ Bad - Violates LSP
class Bird:
    def fly(self):
        return "Flying high"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")  # Breaks contract

def make_bird_fly(bird: Bird):
    return bird.fly()  # Will fail with Penguin

# ✅ Good - Proper abstraction
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "Flying high"
    
    def fly(self):
        return self.move()

class SwimmingBird(Bird):
    def move(self):
        return "Swimming gracefully"
    
    def swim(self):
        return self.move()

class Eagle(FlyingBird):
    pass

class Penguin(SwimmingBird):
    pass

def make_bird_move(bird: Bird):
    return bird.move()  # Works with all birds

# Now both work correctly
eagle = Eagle()
penguin = Penguin()
print(make_bird_move(eagle))    # Flying high
print(make_bird_move(penguin))  # Swimming gracefully
```

### 2. Overusing isinstance() Checks

```python
# ❌ Bad - Too many type checks
def process_shape(shape):
    if isinstance(shape, Circle):
        return f"Circle area: {3.14159 * shape.radius ** 2}"
    elif isinstance(shape, Rectangle):
        return f"Rectangle area: {shape.width * shape.height}"
    elif isinstance(shape, Triangle):
        return f"Triangle area: {0.5 * shape.base * shape.height}"
    else:
        return "Unknown shape"

# ✅ Good - Use polymorphism
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def description(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def description(self):
        return "Circle"

def process_shape(shape: Shape):
    return f"{shape.description()} area: {shape.area()}"

# No type checking needed - polymorphism handles it
```

### 3. Inconsistent Method Signatures

```python
# ❌ Bad - Inconsistent signatures
class FileProcessor:
    def process(self, filename):
        pass

class DatabaseProcessor:
    def process(self, connection, query, params):  # Different signature!
        pass

# ✅ Good - Consistent interface
class DataProcessor(ABC):
    @abstractmethod
    def process(self, source):
        pass

class FileProcessor(DataProcessor):
    def process(self, source):
        # source is a filename
        with open(source, 'r') as file:
            return file.read()

class DatabaseProcessor(DataProcessor):
    def __init__(self, connection):
        self.connection = connection
    
    def process(self, source):
        # source is a query
        return self.connection.execute(source)
```

### 4. Not Handling NotImplemented Properly

```python
# ❌ Bad - Raises exceptions
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        raise TypeError(f"Cannot add Number and {type(other)}")

# ✅ Good - Returns NotImplemented
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return NotImplemented  # Let Python try other.__radd__
    
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Number(other + self.value)
        return NotImplemented

# Now works with built-in types
num = Number(5)
result1 = num + Number(3)  # Number(8)
result2 = 2 + num          # Number(7) - uses __radd__
```

---

## Real-World Examples

### Example 1: Plugin System

```python
from abc import ABC, abstractmethod
import importlib
from typing import Dict, List

class Plugin(ABC):
    """Base class for all plugins"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @property
    @abstractmethod
    def version(self) -> str:
        pass
    
    @abstractmethod
    def execute(self, data) -> any:
        pass

class DataValidationPlugin(Plugin):
    @property
    def name(self) -> str:
        return "Data Validator"
    
    @property
    def version(self) -> str:
        return "1.0.0"
    
    def execute(self, data) -> bool:
        # Validate data structure
        return isinstance(data, dict) and 'id' in data

class DataTransformPlugin(Plugin):
    @property
    def name(self) -> str:
        return "Data Transformer"
    
    @property
    def version(self) -> str:
        return "2.1.0"
    
    def execute(self, data) -> dict:
        # Transform data
        if isinstance(data, dict):
            return {k.upper(): v for k, v in data.items()}
        return {}

class DataLoggingPlugin(Plugin):
    @property
    def name(self) -> str:
        return "Data Logger"
    
    @property
    def version(self) -> str:
        return "1.5.0"
    
    def execute(self, data) -> None:
        print(f"Logging data: {data}")

class PluginManager:
    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}
    
    def register_plugin(self, plugin: Plugin):
        self.plugins[plugin.name] = plugin
        print(f"Registered plugin: {plugin.name} v{plugin.version}")
    
    def execute_plugins(self, data, plugin_names: List[str] = None):
        if plugin_names is None:
            plugin_names = list(self.plugins.keys())
        
        results = {}
        for name in plugin_names:
            if name in self.plugins:
                try:
                    result = self.plugins[name].execute(data)
                    results[name] = result
                except Exception as e:
                    print(f"Error in plugin {name}: {e}")
                    results[name] = None
        
        return results
    
    def list_plugins(self):
        for plugin in self.plugins.values():
            print(f"- {plugin.name} v{plugin.version}")

# Usage
manager = PluginManager()

# Register plugins polymorphically
plugins = [
    DataValidationPlugin(),
    DataTransformPlugin(),
    DataLoggingPlugin()
]

for plugin in plugins:
    manager.register_plugin(plugin)

# Execute plugins
test_data = {"id": 1, "name": "test", "value": 42}
results = manager.execute_plugins(test_data)

print("\nPlugin Results:")
for plugin_name, result in results.items():
    print(f"{plugin_name}: {result}")
```

### Example 2: Media Processing Pipeline

```python
from abc import ABC, abstractmethod
from typing import Any, List
import time

class MediaProcessor(ABC):
    @abstractmethod
    def can_process(self, media_type: str) -> bool:
        pass
    
    @abstractmethod
    def process(self, media_data: Any) -> Any:
        pass
    
    @property
    @abstractmethod
    def processor_type(self) -> str:
        pass

class ImageProcessor(MediaProcessor):
    def can_process(self, media_type: str) -> bool:
        return media_type.lower() in ['jpg', 'png', 'gif', 'bmp']
    
    def process(self, media_data: Any) -> Any:
        print(f"🖼️  Processing image: {media_data}")
        time.sleep(0.1)  # Simulate processing time
        return f"Processed image: {media_data}"
    
    @property
    def processor_type(self) -> str:
        return "Image"

class VideoProcessor(MediaProcessor):
    def can_process(self, media_type: str) -> bool:
        return media_type.lower() in ['mp4', 'avi', 'mov', 'mkv']
    
    def process(self, media_data: Any) -> Any:
        print(f"🎥 Processing video: {media_data}")
        time.sleep(0.3)  # Simulate longer processing time
        return f"Processed video: {media_data}"
    
    @property
    def processor_type(self) -> str:
        return "Video"

class AudioProcessor(MediaProcessor):
    def can_process(self, media_type: str) -> bool:
        return media_type.lower() in ['mp3', 'wav', 'flac', 'aac']
    
    def process(self, media_data: Any) -> Any:
        print(f"🎵 Processing audio: {media_data}")
        time.sleep(0.2)  # Simulate processing time
        return f"Processed audio: {media_data}"
    
    @property
    def processor_type(self) -> str:
        return "Audio"

class MediaFile:
    def __init__(self, filename: str, file_type: str, data: str):
        self.filename = filename
        self.file_type = file_type
        self.data = data

class MediaProcessingPipeline:
    def __init__(self):
        self.processors: List[MediaProcessor] = []
    
    def add_processor(self, processor: MediaProcessor):
        self.processors.append(processor)
        print(f"Added {processor.processor_type} processor")
    
    def process_file(self, media_file: MediaFile) -> Any:
        print(f"\n📁 Processing file: {media_file.filename}")
        
        # Find appropriate processor polymorphically
        for processor in self.processors:
            if processor.can_process(media_file.file_type):
                print(f"✅ Using {processor.processor_type} processor")
                return processor.process(media_file.data)
        
        print(f"❌ No processor found for {media_file.file_type}")
        return None
    
    def process_batch(self, media_files: List[MediaFile]) -> List[Any]:
        results = []
        print("🚀 Starting batch processing...")
        
        for media_file in media_files:
            result = self.process_file(media_file)
            results.append(result)
        
        print("✨ Batch processing completed!")
        return results

# Usage
pipeline = MediaProcessingPipeline()

# Add processors polymorphically
processors = [
    ImageProcessor(),
    VideoProcessor(),
    AudioProcessor()
]

for processor in processors:
    pipeline.add_processor(processor)

# Create test media files
media_files = [
    MediaFile("photo.jpg", "jpg", "image_data_123"),
    MediaFile("video.mp4", "mp4", "video_data_456"),
    MediaFile("song.mp3", "mp3", "audio_data_789"),
    MediaFile("document.pdf", "pdf", "pdf_data_000"),  # No processor
    MediaFile("animation.gif", "gif", "gif_data_111")
]

# Process all files
results = pipeline.process_batch(media_files)

print(f"\n📊 Processing Summary:")
print(f"Total files: {len(media_files)}")
print(f"Successfully processed: {len([r for r in results if r is not None])}")
print(f"Failed: {len([r for r in results if r is None])}")
```

---

## Performance Considerations

### 1. Method Resolution Overhead

```python
import time

class BaseClass:
    def method(self):
        return "base"

class DerivedClass(BaseClass):
    def method(self):
        return "derived"

# Direct method call vs polymorphic call
def test_performance():
    obj = DerivedClass()
    
    # Direct call
    start = time.time()
    for _ in range(1000000):
        obj.method()
    direct_time = time.time() - start
    
    # Polymorphic call through base reference
    base_obj: BaseClass = DerivedClass()
    start = time.time()
    for _ in range(1000000):
        base_obj.method()
    polymorphic_time = time.time() - start
    
    print(f"Direct call time: {direct_time:.4f}s")
    print(f"Polymorphic call time: {polymorphic_time:.4f}s")
    print(f"Overhead: {((polymorphic_time - direct_time) / direct_time * 100):.2f}%")

# test_performance()  # Uncomment to run performance test
```

### 2. Duck Typing vs isinstance() Checks

```python
# Duck typing - faster for valid objects
def process_duck_typing(obj):
    try:
        return obj.process()
    except AttributeError:
        return None

# Type checking - safer but slower
def process_with_check(obj):
    if hasattr(obj, 'process') and callable(getattr(obj, 'process')):
        return obj.process()
    return None

# Use duck typing when you control the input
# Use type checking when dealing with untrusted input
```

---

## Exercises and Practice

### Beginner Level 🟢

1. **Animal Sounds**: Create different animal classes that make different sounds polymorphically.

2. **Shape Calculator**: Implement various shapes with area and perimeter calculations.

3. **Vehicle Fleet**: Create different vehicle types with polymorphic start/stop methods.

4. **Payment Processing**: Implement different payment methods with a common interface.

5. **File Handlers**: Create handlers for different file types (text, image, video).

### Intermediate Level 🟡

6. **Strategy Pattern**: Implement different sorting algorithms using the strategy pattern.

7. **Observer Pattern**: Create a notification system with multiple observer types.

8. **Template Method**: Build a data processing pipeline with customizable steps.

9. **Duck Typing**: Create file-like objects that work with existing Python functions.

10. **Operator Overloading**: Implement a complex number class with full operator support.

### Advanced Level 🔴

11. **Plugin Architecture**: Design a extensible plugin system using polymorphism.

12. **Protocol Implementation**: Use typing.Protocol to define structural interfaces.

13. **Multiple Dispatch**: Implement function overloading based on argument types.

14. **Polymorphic Containers**: Create containers that work with any type of object.

15. **Performance Optimization**: Optimize polymorphic code for better performance.

---

## Summary

Congratulations! You've completed the comprehensive guide to Python Polymorphism. Here's what you've mastered:

### Key Concepts Learned:
- ✅ **Runtime Polymorphism**: Method overriding and dynamic dispatch
- ✅ **Duck Typing**: Structural subtyping and interface compatibility
- ✅ **Operator Overloading**: Custom behavior for built-in operators
- ✅ **Abstract Base Classes**: Formal interface definition
- ✅ **Protocol-Based Polymorphism**: Modern type-safe duck typing
- ✅ **Design Patterns**: Strategy, Observer, Command patterns
- ✅ **Best Practices**: Interface design and performance considerations

### Design Principles Mastered:
- **Open/Closed Principle**: Open for extension, closed for modification
- **Liskov Substitution Principle**: Subclasses must be substitutable
- **Interface Segregation**: Keep interfaces focused and minimal
- **Dependency Inversion**: Depend on abstractions, not concretions

### Next Steps:
1. **Practice**: Work through the exercises to reinforce your learning
2. **Study Design Patterns**: Learn more patterns that leverage polymorphism
3. **Explore Type Systems**: Dive deeper into Python's typing system
4. **Build Real Projects**: Apply polymorphism to solve real-world problems
5. **Performance Profiling**: Learn to optimize polymorphic code

### Remember:
- **Polymorphism enables flexibility** - write code that works with many types
- **Design for interfaces** - focus on what objects can do, not what they are
- **Use composition when appropriate** - not everything needs inheritance
- **Keep interfaces simple** - complex interfaces are hard to implement
- **Consider performance** - polymorphism has overhead, but benefits usually outweigh costs

Happy coding! 🐍✨

---

*This tutorial is part of the Python Practices repository. Continue your OOP journey with the Encapsulation and Design Patterns tutorials.*