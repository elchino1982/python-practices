# SOLID Principles Cheat Sheet

A comprehensive reference guide for the five SOLID design principles that make software designs more understandable, flexible, and maintainable.

## What are SOLID Principles?

SOLID is an acronym for five design principles introduced by Robert C. Martin (Uncle Bob) that help create better object-oriented code:

- **S** - Single Responsibility Principle
- **O** - Open/Closed Principle  
- **L** - Liskov Substitution Principle
- **I** - Interface Segregation Principle
- **D** - Dependency Inversion Principle

## 1. Single Responsibility Principle (SRP)

**"A class should have only one reason to change"**

### Definition:
A class should have only one job or responsibility. Each class should focus on a single functionality.

### ❌ Bad Example:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Database logic
        print(f"Saving {self.name} to database")
    
    def send_email(self):
        # Email logic
        print(f"Sending email to {self.email}")
    
    def validate_email(self):
        # Validation logic
        return "@" in self.email
```

**Problems:**
- User class has multiple responsibilities
- Changes to email logic affect the User class
- Hard to test individual functionalities

### ✅ Good Example:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database")

class EmailService:
    def send_email(self, user):
        print(f"Sending email to {user.email}")

class EmailValidator:
    def validate(self, email):
        return "@" in email
```

**Benefits:**
- Each class has a single responsibility
- Easy to modify and test
- Better code organization

### Real-World Applications:
- **User Management**: Separate user data, authentication, and authorization
- **E-commerce**: Separate product, inventory, and pricing logic
- **File Processing**: Separate reading, parsing, and validation

## 2. Open/Closed Principle (OCP)

**"Software entities should be open for extension, but closed for modification"**

### Definition:
You should be able to add new functionality without changing existing code. Use inheritance, interfaces, and composition.

### ❌ Bad Example:

```python
class DiscountCalculator:
    def calculate_discount(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.05
        elif customer_type == "premium":
            return amount * 0.10
        elif customer_type == "vip":
            return amount * 0.20
        # Adding new customer type requires modifying this method
```

**Problems:**
- Must modify existing code for new customer types
- Violates the principle of not changing tested code
- Risk of breaking existing functionality

### ✅ Good Example:

```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount):
        pass

class RegularCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount * 0.05

class PremiumCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount * 0.10

class VIPCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount * 0.20

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
    
    def calculate(self, amount):
        return self.strategy.calculate_discount(amount)

# Adding new customer type without modifying existing code
class GoldCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        return amount * 0.15
```

**Benefits:**
- Easy to add new discount types
- Existing code remains unchanged
- Each discount strategy is independently testable

### Real-World Applications:
- **Payment Processing**: Different payment methods (credit card, PayPal, crypto)
- **Notification Systems**: Email, SMS, push notifications
- **Data Export**: PDF, Excel, CSV formats

## 3. Liskov Substitution Principle (LSP)

**"Objects of a superclass should be replaceable with objects of its subclasses without breaking functionality"**

### Definition:
Subclasses should be substitutable for their base classes without altering the correctness of the program.

### ❌ Bad Example:

```python
class Bird:
    def fly(self):
        print("Flying...")

class Eagle(Bird):
    def fly(self):
        print("Eagle soaring high!")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Violates LSP

# This breaks when using Penguin
def make_bird_fly(bird: Bird):
    bird.fly()  # Will fail for Penguin

eagle = Eagle()
penguin = Penguin()

make_bird_fly(eagle)    # Works
make_bird_fly(penguin)  # Throws exception!
```

**Problems:**
- Penguin breaks the expected behavior of Bird
- Client code must know about specific implementations
- Substitution fails

### ✅ Good Example:

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        self.fly()
    
    def fly(self):
        print("Flying...")

class SwimmingBird(Bird):
    def move(self):
        self.swim()
    
    def swim(self):
        print("Swimming...")

class Eagle(FlyingBird):
    def fly(self):
        print("Eagle soaring high!")

class Penguin(SwimmingBird):
    def swim(self):
        print("Penguin swimming gracefully!")

# Now substitution works correctly
def make_bird_move(bird: Bird):
    bird.move()  # Works for all birds

eagle = Eagle()
penguin = Penguin()

make_bird_move(eagle)    # Eagle soaring high!
make_bird_move(penguin)  # Penguin swimming gracefully!
```

**Benefits:**
- All subclasses can be used interchangeably
- Client code doesn't need to know specific types
- Proper inheritance hierarchy

### Real-World Applications:
- **Shape Calculations**: All shapes can calculate area, but differently
- **Database Connections**: MySQL, PostgreSQL, SQLite all implement same interface
- **File Handlers**: Text, Binary, CSV files all implement file operations

## 4. Interface Segregation Principle (ISP)

**"Many client-specific interfaces are better than one general-purpose interface"**

### Definition:
Classes shouldn't be forced to depend on interfaces they don't use. Keep interfaces small and focused.

### ❌ Bad Example:

```python
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

class Human(Worker):
    def work(self):
        print("Human working...")
    
    def eat(self):
        print("Human eating...")
    
    def sleep(self):
        print("Human sleeping...")

class Robot(Worker):
    def work(self):
        print("Robot working...")
    
    def eat(self):
        # Robots don't eat!
        raise NotImplementedError("Robots don't eat")
    
    def sleep(self):
        # Robots don't sleep!
        raise NotImplementedError("Robots don't sleep")
```

**Problems:**
- Robot is forced to implement methods it doesn't need
- Interface is too broad
- Violates the principle of focused interfaces

### ✅ Good Example:

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working...")
    
    def eat(self):
        print("Human eating...")
    
    def sleep(self):
        print("Human sleeping...")

class Robot(Workable):
    def work(self):
        print("Robot working...")

# Usage
def make_work(worker: Workable):
    worker.work()

def feed_creature(creature: Eatable):
    creature.eat()

human = Human()
robot = Robot()

make_work(human)  # Works
make_work(robot)  # Works

feed_creature(human)  # Works
# feed_creature(robot)  # Won't compile - Robot doesn't implement Eatable
```

**Benefits:**
- Classes only implement what they need
- Smaller, focused interfaces
- Better flexibility and maintainability

### Real-World Applications:
- **Device Interfaces**: Printer (printable), Scanner (scannable), Fax (faxable)
- **User Roles**: Reader, Writer, Admin interfaces
- **API Design**: Separate read and write operations

## 5. Dependency Inversion Principle (DIP)

**"Depend on abstractions, not concretions"**

### Definition:
High-level modules shouldn't depend on low-level modules. Both should depend on abstractions (interfaces).

### ❌ Bad Example:

```python
class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class UserService:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency on concrete class
    
    def create_user(self, user_data):
        # Business logic
        processed_data = f"Processed: {user_data}"
        self.database.save(processed_data)

# Hard to test and change database
service = UserService()
service.create_user("John Doe")
```

**Problems:**
- UserService is tightly coupled to MySQLDatabase
- Hard to test (can't mock database)
- Difficult to switch to different database

### ✅ Good Example:

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL database")

class UserService:
    def __init__(self, database: Database):
        self.database = database  # Depends on abstraction
    
    def create_user(self, user_data):
        # Business logic
        processed_data = f"Processed: {user_data}"
        self.database.save(processed_data)

# Easy to switch databases and test
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()

service1 = UserService(mysql_db)
service2 = UserService(postgres_db)

service1.create_user("John Doe")    # Uses MySQL
service2.create_user("Jane Smith")  # Uses PostgreSQL
```

**Benefits:**
- Loose coupling between components
- Easy to test with mock objects
- Simple to switch implementations

### Dependency Injection Patterns:

```python
# Constructor Injection (recommended)
class OrderService:
    def __init__(self, payment_processor: PaymentProcessor, 
                 email_service: EmailService):
        self.payment_processor = payment_processor
        self.email_service = email_service

# Setter Injection
class OrderService:
    def set_payment_processor(self, processor: PaymentProcessor):
        self.payment_processor = processor

# Method Injection
class OrderService:
    def process_order(self, order, processor: PaymentProcessor):
        processor.process_payment(order.amount)
```

### Real-World Applications:
- **Logging Systems**: Abstract logger with file, database, cloud implementations
- **Caching**: Abstract cache with Redis, Memcached, in-memory implementations
- **Authentication**: Abstract auth with OAuth, JWT, session-based implementations

## SOLID Principles in Practice

### Example: E-commerce Order System

```python
from abc import ABC, abstractmethod
from typing import List

# SRP: Each class has single responsibility
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items: List[Product] = []
    
    def add_item(self, product: Product):
        self.items.append(product)
    
    def get_total(self) -> float:
        return sum(item.price for item in self.items)

# DIP: Depend on abstractions
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class EmailService(ABC):
    @abstractmethod
    def send_confirmation(self, order: Order):
        pass

# ISP: Focused interfaces
class Discountable(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass

# OCP: Open for extension
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via credit card")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via PayPal")
        return True

class SMTPEmailService(EmailService):
    def send_confirmation(self, order: Order):
        print(f"Sending email confirmation for order total: ${order.get_total()}")

# LSP: Substitutable implementations
class PremiumDiscountStrategy(Discountable):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.9  # 10% discount

class OrderProcessor:
    def __init__(self, payment_processor: PaymentProcessor, 
                 email_service: EmailService):
        self.payment_processor = payment_processor
        self.email_service = email_service
    
    def process_order(self, order: Order, discount_strategy: Discountable = None):
        total = order.get_total()
        
        if discount_strategy:
            total = discount_strategy.apply_discount(total)
        
        if self.payment_processor.process_payment(total):
            self.email_service.send_confirmation(order)
            return True
        return False

# Usage
order = Order()
order.add_item(Product("Laptop", 1000.0))
order.add_item(Product("Mouse", 25.0))

payment_processor = CreditCardProcessor()
email_service = SMTPEmailService()
discount = PremiumDiscountStrategy()

processor = OrderProcessor(payment_processor, email_service)
processor.process_order(order, discount)
```

## Benefits of Following SOLID Principles

### 1. **Maintainability**
- Code is easier to understand and modify
- Changes have minimal impact on other parts
- Clear separation of concerns

### 2. **Testability**
- Easy to write unit tests
- Dependencies can be mocked
- Isolated testing of components

### 3. **Flexibility**
- Easy to add new features
- Simple to change implementations
- Supports different configurations

### 4. **Reusability**
- Components can be reused in different contexts
- Modular design promotes code sharing
- Reduces duplication

### 5. **Scalability**
- Architecture supports growth
- Easy to add new team members
- Parallel development possible

## Common Violations and How to Fix Them

### 1. **God Classes** (SRP Violation)
```python
# ❌ Bad: God class doing everything
class UserManager:
    def create_user(self): pass
    def validate_email(self): pass
    def send_email(self): pass
    def save_to_database(self): pass
    def generate_report(self): pass
    def log_activity(self): pass

# ✅ Good: Separate responsibilities
class User: pass
class UserValidator: pass
class EmailService: pass
class UserRepository: pass
class ReportGenerator: pass
class Logger: pass
```

### 2. **Rigid Code** (OCP Violation)
```python
# ❌ Bad: Must modify for new types
def calculate_area(shape_type, dimensions):
    if shape_type == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape_type == "circle":
        return 3.14 * dimensions[0] ** 2
    # Must modify for new shapes

# ✅ Good: Extensible design
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Rectangle(Shape):
    def area(self): return self.width * self.height

class Circle(Shape):
    def area(self): return 3.14 * self.radius ** 2
```

### 3. **Broken Inheritance** (LSP Violation)
```python
# ❌ Bad: Subclass changes behavior
class Rectangle:
    def set_width(self, width): self.width = width
    def set_height(self, height): self.height = height

class Square(Rectangle):
    def set_width(self, width): 
        self.width = self.height = width  # Changes behavior!

# ✅ Good: Proper inheritance
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Rectangle(Shape):
    def area(self): return self.width * self.height

class Square(Shape):
    def area(self): return self.side ** 2
```

## Quick Reference

### SOLID Checklist:
- [ ] **SRP**: Does each class have only one reason to change?
- [ ] **OCP**: Can I add new features without modifying existing code?
- [ ] **LSP**: Can I substitute subclasses without breaking functionality?
- [ ] **ISP**: Are my interfaces focused and not forcing unused methods?
- [ ] **DIP**: Do I depend on abstractions rather than concrete classes?

### When to Apply SOLID:
- ✅ **Do**: When building maintainable systems
- ✅ **Do**: When code will be extended or modified
- ✅ **Do**: When working in teams
- ⚠️ **Consider**: For simple scripts or prototypes
- ❌ **Don't**: Over-engineer simple solutions

### Code Smells Indicating SOLID Violations:
- Large classes with many responsibilities
- Frequent modifications to existing code for new features
- Difficulty testing components in isolation
- Classes implementing unused interface methods
- Direct instantiation of concrete classes everywhere

---

*Master these SOLID principles to write better, more maintainable object-oriented code. Remember: good design is about managing dependencies and responsibilities!*