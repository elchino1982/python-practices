# Inheritance 🧬

Master the concept of inheritance in Python - one of the fundamental pillars of Object-Oriented Programming.

## 🎯 Learning Objectives

- Understand inheritance and the "is-a" relationship
- Learn to create parent and child classes
- Master method overriding and the super() function
- Implement abstract base classes and methods
- Work with polymorphism through inheritance
- Apply inheritance in real-world scenarios

## 📚 Exercises

### Intermediate Level (🟡)

1. **[Basic Employee Inheritance](./01-basic-inheritance-employee.py)** - Employee → Manager
   - Basic inheritance syntax with `class Child(Parent)`
   - Using `super().__init__()` to call parent constructor
   - Adding new attributes to child classes
   - Method overriding with `__str__` method
   - Step-by-step walkthrough of inheritance concepts

2. **[Abstract Shape Inheritance](./02-abstract-shape-inheritance.py)** - Shape → Circle, Square
   - Abstract base classes using `NotImplementedError`
   - Method overriding for abstract methods
   - Mathematical calculations in inherited methods
   - Polymorphism demonstration with shape collections
   - Testing different shape implementations

3. **[Animal Inheritance Hierarchy](./03-animal-inheritance-hierarchy.py)** - Animal → Dog
   - Simple inheritance with additional methods
   - Adding behavior-specific methods to child classes
   - Working with species and breed attributes
   - Practical example of "is-a" relationships

4. **[Vehicle Inheritance System](./04-vehicle-inheritance-system.py)** - Vehicle → ElectricVehicle
   - Extending base classes with specialized functionality
   - Adding domain-specific attributes (battery_capacity)
   - Implementing specialized methods (charge)
   - Real-world inheritance modeling

5. **[Abstract Methods Implementation](./05-abstract-methods-implementation.py)** - Shape → Circle, Rectangle
   - Advanced abstract class implementation
   - Multiple shape types with different constructors
   - Polymorphism with mixed object collections
   - Calculating areas and demonstrating method dispatch
   - String representation overriding

### Advanced Level (🟠)

6. **[Advanced Custom List Inheritance](./06-advanced-custom-list-inheritance.py)** - Built-in Extension
   - Inheriting from built-in Python classes (`list`)
   - Overriding magic methods (`__getitem__`, `__setitem__`)
   - Adding logging and custom behavior to existing functionality
   - Understanding method resolution order with built-ins

## 🔑 Key Concepts

### Basic Inheritance Syntax
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):  # Manager inherits from Employee
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent constructor
        self.department = department    # Add new attribute
```

### Abstract Base Classes
```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Must implement abstract method
        return 3.14159 * self.radius ** 2
```

### Method Overriding
```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return "Woof!"
```

### Polymorphism Through Inheritance
```python
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")  # Same method, different implementations
```

### Extending Built-in Classes
```python
class CustomList(list):
    def __getitem__(self, index):
        print(f"Accessing index {index}")
        return super().__getitem__(index)
```

## 🎓 Progressive Learning Path

### Start Here (Beginner)
1. **Basic Employee Inheritance** - Learn fundamental syntax and `super()`
2. **Animal Inheritance** - Practice simple "is-a" relationships

### Build Understanding (Intermediate)
3. **Abstract Shape Inheritance** - Understand abstract methods and polymorphism
4. **Vehicle Inheritance** - Apply concepts to real-world scenarios
5. **Advanced Abstract Methods** - Master complex inheritance patterns

### Advanced Concepts
6. **Custom List Inheritance** - Extend built-in classes and override magic methods

## 💡 Best Practices

### ✅ Do This
- **Use inheritance for "is-a" relationships** - Manager is-a Employee
- **Call `super().__init__()`** to properly initialize parent attributes
- **Override methods meaningfully** - add value, don't just call super()
- **Use abstract base classes** to define interfaces
- **Keep inheritance hierarchies shallow** - prefer 2-3 levels max

### ❌ Avoid This
- **Don't use inheritance for "has-a" relationships** - use composition instead
- **Don't create deep inheritance chains** - they become hard to maintain
- **Don't override methods without purpose** - only override when you need different behavior
- **Don't forget to call `super()`** when extending parent functionality

## 🔍 Common Patterns

### Template Method Pattern
```python
class DataProcessor:
    def process(self):
        self.load_data()
        self.transform_data()  # Abstract - subclasses implement
        self.save_data()
    
    def load_data(self):
        print("Loading data...")
    
    def save_data(self):
        print("Saving data...")
```

### Factory Method Pattern
```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
```

## 🚀 Getting Started

1. **Start with [Basic Employee Inheritance](./01-basic-inheritance-employee.py)** - Master the fundamentals
2. **Work through exercises in order** - Each builds on previous concepts
3. **Experiment with modifications** - Try adding new subclasses or methods
4. **Focus on understanding "why"** - Don't just copy code, understand the reasoning

## 🎯 Learning Tips

- **Code along with examples** - Don't just read, implement!
- **Test each concept** - Run the code and see how it behaves
- **Draw class diagrams** - Visualize the inheritance relationships
- **Think of real-world examples** - How would you model cars, animals, or employees?

---

Ready to master inheritance? Start with [Basic Employee Inheritance](./01-basic-inheritance-employee.py)! 🎯