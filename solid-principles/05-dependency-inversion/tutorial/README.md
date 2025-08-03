# Dependency Inversion Principle (DIP) - Complete Tutorial

## Table of Contents
1. [Introduction](#introduction)
2. [What is the Dependency Inversion Principle?](#what-is-the-dependency-inversion-principle)
3. [Why DIP Matters](#why-dip-matters)
4. [Beginner Level: Understanding the Basics](#beginner-level-understanding-the-basics)
5. [Intermediate Level: Practical Applications](#intermediate-level-practical-applications)
6. [Advanced Level: Complex Systems](#advanced-level-complex-systems)
7. [Expert Level: Architecture and Design Patterns](#expert-level-architecture-and-design-patterns)
8. [Practical Exercises and Challenges](#practical-exercises-and-challenges)
9. [Common Pitfalls and Troubleshooting](#common-pitfalls-and-troubleshooting)
10. [Performance Considerations](#performance-considerations)
11. [Integration with Testing Frameworks](#integration-with-testing-frameworks)
12. [Migration Strategies](#migration-strategies)
13. [Conclusion and Next Steps](#conclusion-and-next-steps)

---

## Introduction

Welcome to the comprehensive tutorial on the Dependency Inversion Principle (DIP), the fifth and final principle of SOLID design principles. This tutorial will take you from a complete beginner to an expert level understanding of DIP, with practical examples and real-world applications.

### Who This Tutorial Is For
- **Beginners**: New to programming or SOLID principles
- **Intermediate**: Familiar with basic OOP concepts and interfaces
- **Advanced**: Experienced developers looking to master dependency management
- **Experts**: Architects and senior developers seeking advanced patterns

### Prerequisites
- Basic understanding of Python
- Familiarity with classes, objects, and inheritance
- Understanding of interfaces/abstract classes (helpful but not required)
- Basic knowledge of other SOLID principles (recommended)

---

## What is the Dependency Inversion Principle?

> **"High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions."**
> 
> *- Robert C. Martin*

The Dependency Inversion Principle consists of two key parts:

### 1. **High-level modules should not depend on low-level modules**
- High-level modules contain the business logic and policies
- Low-level modules handle implementation details (databases, file systems, etc.)
- Both should depend on abstractions (interfaces)

### 2. **Abstractions should not depend on details**
- Interfaces should not be influenced by concrete implementations
- Concrete implementations should conform to interfaces
- This creates stable, flexible architectures

### Key Concepts

- **Dependency**: When one class uses another class
- **Inversion**: Reversing the direction of dependency
- **Abstraction**: Interface or abstract class that defines a contract
- **Concrete Implementation**: Actual implementation of an abstraction
- **Dependency Injection**: Providing dependencies from the outside

---

## Why DIP Matters

### Problems DIP Solves

1. **Tight Coupling**: Classes directly depending on concrete implementations
2. **Difficult Testing**: Hard to mock or substitute dependencies
3. **Inflexible Design**: Changes in low-level modules break high-level modules
4. **Violation of Open/Closed Principle**: Modifications required for new implementations

### Benefits of Following DIP

1. **Loose Coupling**: Classes depend on abstractions, not concrete implementations
2. **Testability**: Easy to inject mock objects for testing
3. **Flexibility**: Easy to swap implementations without changing client code
4. **Maintainability**: Changes in implementation don't affect business logic
5. **Extensibility**: New implementations can be added without modifying existing code
6. **Reusability**: High-level modules can work with different implementations

---

## Beginner Level: Understanding the Basics

### 🎯 Learning Objectives
By the end of this section, you will:
- Understand what dependency inversion means
- Recognize DIP violations in simple code
- Know how to apply DIP using interfaces
- Write your first DIP-compliant code

### Example 1: The Classic Email Notification Problem

Let's start with a simple example that demonstrates the core concept of DIP.

#### ❌ Bad Example (DIP Violation)

```python
# Low-level module - concrete implementation
class EmailService:
    def send_email(self, recipient, subject, message):
        print(f"Sending email to {recipient}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        return True

# High-level module - depends directly on concrete implementation
class UserRegistration:
    def __init__(self):
        # Direct dependency on concrete class - BAD!
        self.email_service = EmailService()
    
    def register_user(self, username, email):
        # Business logic
        print(f"Registering user: {username}")
        
        # Send welcome email
        success = self.email_service.send_email(
            email, 
            "Welcome!", 
            f"Welcome {username}! Your account has been created."
        )
        
        if success:
            print(f"User {username} registered successfully")
        return success

# Usage
registration = UserRegistration()
registration.register_user("alice", "alice@example.com")
```

**What's wrong here?**
- `UserRegistration` (high-level) directly depends on `EmailService` (low-level)
- Hard to test - can't easily mock the email service
- Inflexible - can't switch to SMS or other notification methods
- Violates DIP - high-level module depends on low-level module

#### ✅ Good Example (DIP Compliant)

```python
from abc import ABC, abstractmethod

# Abstraction - interface that both modules depend on
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient, subject, message):
        pass

# Low-level module - implements the abstraction
class EmailService(NotificationService):
    def send_notification(self, recipient, subject, message):
        print(f"Sending email to {recipient}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        return True

class SMSService(NotificationService):
    def send_notification(self, recipient, subject, message):
        print(f"Sending SMS to {recipient}")
        print(f"Message: {subject} - {message}")
        return True

# High-level module - depends on abstraction
class UserRegistration:
    def __init__(self, notification_service: NotificationService):
        # Dependency injection - depends on abstraction
        self.notification_service = notification_service
    
    def register_user(self, username, contact):
        # Business logic
        print(f"Registering user: {username}")
        
        # Send welcome notification
        success = self.notification_service.send_notification(
            contact, 
            "Welcome!", 
            f"Welcome {username}! Your account has been created."
        )
        
        if success:
            print(f"User {username} registered successfully")
        return success

# Usage - dependency is injected from outside
email_service = EmailService()
registration_with_email = UserRegistration(email_service)
registration_with_email.register_user("alice", "alice@example.com")

print("\n" + "="*50 + "\n")

# Easy to switch implementations
sms_service = SMSService()
registration_with_sms = UserRegistration(sms_service)
registration_with_sms.register_user("bob", "+1234567890")
```

**What's better now?**
- `UserRegistration` depends on `NotificationService` abstraction
- Easy to test - can inject mock notification service
- Flexible - can use email, SMS, or any other notification method
- Follows DIP - both modules depend on abstraction

### Example 2: Data Storage Problem

Let's look at another common scenario - data persistence.

#### ❌ Bad Example (DIP Violation)

```python
import json

# Low-level module
class FileStorage:
    def __init__(self, filename):
        self.filename = filename
    
    def save_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)
        print(f"Data saved to {self.filename}")
    
    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
            print(f"Data loaded from {self.filename}")
            return data
        except FileNotFoundError:
            return {}

# High-level module - directly depends on FileStorage
class UserManager:
    def __init__(self):
        # Direct dependency - BAD!
        self.storage = FileStorage("users.json")
        self.users = self.storage.load_data()
    
    def add_user(self, user_id, user_data):
        self.users[user_id] = user_data
        self.storage.save_data(self.users)
        print(f"User {user_id} added")
    
    def get_user(self, user_id):
        return self.users.get(user_id)

# Usage
user_manager = UserManager()
user_manager.add_user("001", {"name": "Alice", "email": "alice@example.com"})
```

#### ✅ Good Example (DIP Compliant)

```python
from abc import ABC, abstractmethod
import json

# Abstraction
class DataStorage(ABC):
    @abstractmethod
    def save_data(self, data):
        pass
    
    @abstractmethod
    def load_data(self):
        pass

# Low-level modules - implement the abstraction
class FileStorage(DataStorage):
    def __init__(self, filename):
        self.filename = filename
    
    def save_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)
        print(f"Data saved to {self.filename}")
    
    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
            print(f"Data loaded from {self.filename}")
            return data
        except FileNotFoundError:
            return {}

class MemoryStorage(DataStorage):
    def __init__(self):
        self.data = {}
    
    def save_data(self, data):
        self.data = data.copy()
        print("Data saved to memory")
    
    def load_data(self):
        print("Data loaded from memory")
        return self.data.copy()

class DatabaseStorage(DataStorage):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.data = {}  # Simulated database
    
    def save_data(self, data):
        self.data = data.copy()
        print(f"Data saved to database: {self.connection_string}")
    
    def load_data(self):
        print(f"Data loaded from database: {self.connection_string}")
        return self.data.copy()

# High-level module - depends on abstraction
class UserManager:
    def __init__(self, storage: DataStorage):
        # Dependency injection
        self.storage = storage
        self.users = self.storage.load_data()
    
    def add_user(self, user_id, user_data):
        self.users[user_id] = user_data
        self.storage.save_data(self.users)
        print(f"User {user_id} added")
    
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def list_users(self):
        return list(self.users.keys())

# Usage - easy to switch storage implementations
print("=== Using File Storage ===")
file_storage = FileStorage("users.json")
user_manager_file = UserManager(file_storage)
user_manager_file.add_user("001", {"name": "Alice", "email": "alice@example.com"})

print("\n=== Using Memory Storage ===")
memory_storage = MemoryStorage()
user_manager_memory = UserManager(memory_storage)
user_manager_memory.add_user("002", {"name": "Bob", "email": "bob@example.com"})

print("\n=== Using Database Storage ===")
db_storage = DatabaseStorage("postgresql://localhost:5432/mydb")
user_manager_db = UserManager(db_storage)
user_manager_db.add_user("003", {"name": "Charlie", "email": "charlie@example.com"})

# All user managers work the same way, regardless of storage
print(f"\nFile storage users: {user_manager_file.list_users()}")
print(f"Memory storage users: {user_manager_memory.list_users()}")
print(f"Database storage users: {user_manager_db.list_users()}")
```

### 🧪 Try It Yourself: Simple Exercise

Create a DIP-compliant logging system:

```python
# Your task: Create a logging system that follows DIP
# Requirements:
# 1. Create a Logger abstraction
# 2. Implement ConsoleLogger and FileLogger
# 3. Create an Application class that uses the logger
# 4. Show how easy it is to switch between loggers

# Hint: Think about what methods a logger should have
# - log_info(message)
# - log_error(message)
# - log_warning(message)

# Start your implementation here:
from abc import ABC, abstractmethod

class Logger(ABC):
    # Define your abstract methods here
    pass

# Your implementations here...
```

### Key Takeaways for Beginners

1. **Depend on Abstractions**: Always depend on interfaces, not concrete classes
2. **Inject Dependencies**: Don't create dependencies inside classes - inject them
3. **Think About Contracts**: Define what you need, not how it's implemented
4. **Flexibility First**: Design for change - you'll need different implementations later
5. **Test-Friendly Design**: DIP makes your code much easier to test

### Understanding the "Inversion"

The "inversion" in Dependency Inversion refers to inverting the direction of dependency:

**Before DIP (Traditional):**
```
High-level module → Low-level module
```

**After DIP (Inverted):**
```
High-level module → Abstraction ← Low-level module
```

Both high-level and low-level modules now depend on the abstraction, not on each other!

---

## Intermediate Level: Practical Applications

### 🎯 Learning Objectives
By the end of this section, you will:
- Apply DIP to more complex scenarios
- Understand different dependency injection patterns
- Learn about inversion of control containers
- Handle multiple dependencies effectively

### Example 3: E-commerce Order Processing System

Let's build a more sophisticated system that demonstrates DIP in a business context.

#### The Challenge
We need to build an order processing system that can:
- Calculate prices with different pricing strategies
- Process payments through various providers
- Send notifications via multiple channels
- Handle inventory from different sources

#### ✅ DIP Solution

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

# Domain models
@dataclass
class Product:
    id: str
    name: str
    base_price: float
    category: str

@dataclass
class OrderItem:
    product: Product
    quantity: int
    unit_price: float

@dataclass
class Order:
    id: str
    customer_id: str
    items: List[OrderItem]
    total_amount: float
    status: str

# Abstractions for different concerns
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, product: Product, quantity: int, customer_id: str) -> float:
        pass

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, payment_method: str, customer_id: str) -> bool:
        pass

class InventoryService(ABC):
    @abstractmethod
    def check_availability(self, product_id: str, quantity: int) -> bool:
        pass
    
    @abstractmethod
    def reserve_items(self, product_id: str, quantity: int) -> bool:
        pass

class NotificationService(ABC):
    @abstractmethod
    def send_order_confirmation(self, customer_id: str, order: Order) -> bool:
        pass

class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order: Order) -> bool:
        pass
    
    @abstractmethod
    def get_order(self, order_id: str) -> Order:
        pass

# Concrete implementations
class RegularPricingStrategy(PricingStrategy):
    def calculate_price(self, product: Product, quantity: int, customer_id: str) -> float:
        return product.base_price * quantity

class VIPPricingStrategy(PricingStrategy):
    def __init__(self, discount_rate: float = 0.1):
        self.discount_rate = discount_rate
    
    def calculate_price(self, product: Product, quantity: int, customer_id: str) -> float:
        base_total = product.base_price * quantity
        return base_total * (1 - self.discount_rate)

class BulkPricingStrategy(PricingStrategy):
    def __init__(self, bulk_threshold: int = 10, bulk_discount: float = 0.15):
        self.bulk_threshold = bulk_threshold
        self.bulk_discount = bulk_discount
    
    def calculate_price(self, product: Product, quantity: int, customer_id: str) -> float:
        base_total = product.base_price * quantity
        if quantity >= self.bulk_threshold:
            return base_total * (1 - self.bulk_discount)
        return base_total

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float, payment_method: str, customer_id: str) -> bool:
        print(f"Processing credit card payment of ${amount:.2f} for customer {customer_id}")
        # Simulate payment processing
        return amount > 0

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float, payment_method: str, customer_id: str) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f} for customer {customer_id}")
        # Simulate PayPal processing
        return amount > 0

class LocalInventoryService(InventoryService):
    def __init__(self):
        self.inventory = {
            "PROD-001": 100,
            "PROD-002": 50,
            "PROD-003": 25
        }
    
    def check_availability(self, product_id: str, quantity: int) -> bool:
        available = self.inventory.get(product_id, 0)
        return available >= quantity
    
    def reserve_items(self, product_id: str, quantity: int) -> bool:
        if self.check_availability(product_id, quantity):
            self.inventory[product_id] -= quantity
            print(f"Reserved {quantity} units of {product_id}")
            return True
        return False

class EmailNotificationService(NotificationService):
    def send_order_confirmation(self, customer_id: str, order: Order) -> bool:
        print(f"Sending email confirmation to customer {customer_id}")
        print(f"Order {order.id} confirmed - Total: ${order.total_amount:.2f}")
        return True

class SMSNotificationService(NotificationService):
    def send_order_confirmation(self, customer_id: str, order: Order) -> bool:
        print(f"Sending SMS confirmation to customer {customer_id}")
        print(f"Order {order.id} confirmed - Total: ${order.total_amount:.2f}")
        return True

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}
    
    def save_order(self, order: Order) -> bool:
        self.orders[order.id] = order
        print(f"Order {order.id} saved to repository")
        return True
    
    def get_order(self, order_id: str) -> Order:
        return self.orders.get(order_id)

# High-level module that orchestrates the order processing
class OrderProcessor:
    def __init__(self, 
                 pricing_strategy: PricingStrategy,
                 payment_processor: PaymentProcessor,
                 inventory_service: InventoryService,
                 notification_service: NotificationService,
                 order_repository: OrderRepository):
        # All dependencies injected - follows DIP
        self.pricing_strategy = pricing_strategy
        self.payment_processor = payment_processor
        self.inventory_service = inventory_service
        self.notification_service = notification_service
        self.order_repository = order_repository
        self.order_counter = 0
    
    def process_order(self, customer_id: str, cart_items: List[Dict], payment_method: str) -> Order:
        """Process a complete order using injected dependencies"""
        
        # Step 1: Check inventory and calculate prices
        order_items = []
        total_amount = 0
        
        for item in cart_items:
            product = item['product']
            quantity = item['quantity']
            
            # Check inventory
            if not self.inventory_service.check_availability(product.id, quantity):
                raise ValueError(f"Insufficient inventory for {product.name}")
            
            # Calculate price using injected strategy
            unit_price = self.pricing_strategy.calculate_price(product, quantity, customer_id)
            
            order_item = OrderItem(product, quantity, unit_price)
            order_items.append(order_item)
            total_amount += unit_price
        
        # Step 2: Reserve inventory
        for item in order_items:
            if not self.inventory_service.reserve_items(item.product.id, item.quantity):
                raise ValueError(f"Failed to reserve {item.product.name}")
        
        # Step 3: Process payment
        payment_success = self.payment_processor.process_payment(
            total_amount, payment_method, customer_id
        )
        
        if not payment_success:
            raise ValueError("Payment processing failed")
        
        # Step 4: Create and save order
        self.order_counter += 1
        order = Order(
            id=f"ORD-{self.order_counter:06d}",
            customer_id=customer_id,
            items=order_items,
            total_amount=total_amount,
            status="confirmed"
        )
        
        self.order_repository.save_order(order)
        
        # Step 5: Send confirmation
        self.notification_service.send_order_confirmation(customer_id, order)
        
        return order

# Factory pattern to create different configurations
class OrderProcessorFactory:
    @staticmethod
    def create_regular_processor() -> OrderProcessor:
        return OrderProcessor(
            pricing_strategy=RegularPricingStrategy(),
            payment_processor=CreditCardProcessor(),
            inventory_service=LocalInventoryService(),
            notification_service=EmailNotificationService(),
            order_repository=InMemoryOrderRepository()
        )
    
    @staticmethod
    def create_vip_processor() -> OrderProcessor:
        return OrderProcessor(
            pricing_strategy=VIPPricingStrategy(discount_rate=0.15),
            payment_processor=PayPalProcessor(),
            inventory_service=LocalInventoryService(),
            notification_service=SMSNotificationService(),
            order_repository=InMemoryOrderRepository()
        )
    
    @staticmethod
    def create_bulk_processor() -> OrderProcessor:
        return OrderProcessor(
            pricing_strategy=BulkPricingStrategy(bulk_threshold=5, bulk_discount=0.2),
            payment_processor=CreditCardProcessor(),
            inventory_service=LocalInventoryService(),
            notification_service=EmailNotificationService(),
            order_repository=InMemoryOrderRepository()
        )

# Example usage
print("=== DIP in E-commerce Order Processing ===")

# Sample products
products = [
    Product("PROD-001", "Laptop", 999.99, "Electronics"),
    Product("PROD-002", "Mouse", 29.99, "Electronics"),
    Product("PROD-003", "Keyboard", 79.99, "Electronics")
]

# Sample cart
cart_items = [
    {"product": products[0], "quantity": 1},
    {"product": products[1], "quantity": 2}
]

# Process order with regular pricing
print("\n--- Regular Customer Order ---")
regular_processor = OrderProcessorFactory.create_regular_processor()
regular_order = regular_processor.process_order("CUST-001", cart_items, "credit_card")

# Process order with VIP pricing
print("\n--- VIP Customer Order ---")
vip_processor = OrderProcessorFactory.create_vip_processor()
vip_order = vip_processor.process_order("VIP-001", cart_items, "paypal")

# Process bulk order
print("\n--- Bulk Order ---")
bulk_cart = [{"product": products[2], "quantity": 10}]
bulk_processor = OrderProcessorFactory.create_bulk_processor()
bulk_order = bulk_processor.process_order("BULK-001", bulk_cart, "credit_card")

print(f"\nRegular order total: ${regular_order.total_amount:.2f}")
print(f"VIP order total: ${vip_order.total_amount:.2f}")
print(f"Bulk order total: ${bulk_order.total_amount:.2f}")
```

### Example 4: Configuration-Based Dependency Injection

Let's explore how to use configuration to wire dependencies.

```python
from abc import ABC, abstractmethod
import json
from typing import Dict, Any

# Configuration-driven dependency injection
class ServiceRegistry:
    def __init__(self):
        self._services = {}
        self._factories = {}
    
    def register_service(self, interface_name: str, implementation):
        """Register a service implementation"""
        self._services[interface_name] = implementation
    
    def register_factory(self, interface_name: str, factory_func):
        """Register a factory function for creating services"""
        self._factories[interface_name] = factory_func
    
    def get_service(self, interface_name: str):
        """Get a service by interface name"""
        if interface_name in self._services:
            return self._services[interface_name]
        elif interface_name in self._factories:
            service = self._factories[interface_name]()
            self._services[interface_name] = service  # Cache it
            return service
        else:
            raise ValueError(f"No service registered for {interface_name}")

class ConfigurationManager:
    def __init__(self, config_file: str = None):
        self.config = {}
        if config_file:
            self.load_config(config_file)
    
    def load_config(self, config_file: str):
        """Load configuration from file"""
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"Config file {config_file} not found, using defaults")
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

# Application that uses configuration-driven DI
class Application:
    def __init__(self, config_manager: ConfigurationManager, service_registry: ServiceRegistry):
        self.config = config_manager
        self.registry = service_registry
        self._setup_services()
    
    def _setup_services(self):
        """Setup services based on configuration"""
        # Get logger configuration
        logger_type = self.config.get('logging.type', 'console')
        
        if logger_type == 'console':
            self.registry.register_factory('logger', lambda: ConsoleLogger())
        elif logger_type == 'file':
            log_file = self.config.get('logging.file', 'app.log')
            self.registry.register_factory('logger', lambda: FileLogger(log_file))
        
        # Get database configuration
        db_type = self.config.get('database.type', 'memory')
        
        if db_type == 'memory':
            self.registry.register_factory('database', lambda: InMemoryDatabase())
        elif db_type == 'file':
            db_file = self.config.get('database.file', 'data.json')
            self.registry.register_factory('database', lambda: FileDatabase(db_file))
    
    def run(self):
        """Run the application using configured services"""
        logger = self.registry.get_service('logger')
        database = self.registry.get_service('database')
        
        logger.log_info("Application starting...")
        
        # Use the services
        database.save("user:1", {"name": "Alice", "email": "alice@example.com"})
        user_data = database.load("user:1")
        
        logger.log_info(f"Loaded user data: {user_data}")
        logger.log_info("Application finished")

# Service implementations
class Logger(ABC):
    @abstractmethod
    def log_info(self, message: str):
        pass
    
    @abstractmethod
    def log_error(self, message: str):
        pass

class ConsoleLogger(Logger):
    def log_info(self, message: str):
        print(f"INFO: {message}")
    
    def log_error(self, message: str):
        print(f"ERROR: {message}")

class FileLogger(Logger):
    def __init__(self, filename: str):
        self.filename = filename
    
    def log_info(self, message: str):
        with open(self.filename, 'a') as f:
            f.write(f"INFO: {message}\n")
        print(f"Logged to {self.filename}: INFO: {message}")
    
    def log_error(self, message: str):
        with open(self.filename, 'a') as f:
            f.write(f"ERROR: {message}\n")
        print(f"Logged to {self.filename}: ERROR: {message}")

class Database(ABC):
    @abstractmethod
    def save(self, key: str, data: Any):
        pass
    
    @abstractmethod
    def load(self, key: str) -> Any:
        pass

class InMemoryDatabase(Database):
    def __init__(self):
        self.data = {}
    
    def save(self, key: str, data: Any):
        self.data[key] = data
        print(f"Saved {key} to memory database")
    
    def load(self, key: str) -> Any:
        return self.data.get(key)

class FileDatabase(Database):
    def __init__(self, filename: str):
        self.filename = filename
        self.data = {}
        self._load_from_file()
    
    def _load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
    
    def _save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
    
    def save(self, key: str, data: Any):
        self.data[key] = data
        self._save_to_file()
        print(f"Saved {key} to file database: {self.filename}")
    
    def load(self, key: str) -> Any:
        return self.data.get(key)

# Example usage
print("\n=== Configuration-Based Dependency Injection ===")

# Create configuration
config = ConfigurationManager()
config.config = {
    "logging": {
        "type": "console"
    },
    "database": {
        "type": "memory"
    }
}

# Create service registry
registry = ServiceRegistry()

# Create and run application
app = Application(config, registry)
app.run()

print("\n--- Switching to File-based Services ---")

# Change configuration
config.config = {
    "logging": {
        "type": "file",
        "file": "app.log"
    },
    "database": {
        "type": "file",
        "file": "data.json"
    }
}

# Create new application with different configuration
app2 = Application(config, ServiceRegistry())
app2.run()
```

### 🧪 Intermediate Exercise

Create a DIP-compliant reporting system:

```python
# Your task: Create a reporting system that follows DIP
# Requirements:
# 1. Create abstractions for DataSource, ReportFormatter, and ReportDelivery
# 2. Implement multiple data sources (Database, API, File)
# 3. Implement multiple formatters (PDF, Excel, HTML)
# 4. Implement multiple delivery methods (Email, FTP, Local file)
# 5. Create a ReportGenerator that uses all three abstractions
# 6. Show how easy it is to create different report configurations

# Start your implementation here:
```

### Key Takeaways for Intermediate Level

1. **Multiple Dependencies**: Real applications often have many dependencies - inject them all
2. **Factory Pattern**: Use factories to create different configurations of dependencies
3. **Configuration-Driven**: Use configuration files to control which implementations to use
4. **Service Registry**: Centralize service creation and management
5. **Composition Root**: Have one place where all dependencies are wired together

---

## Advanced Level: Complex Systems

### 🎯 Learning Objectives
By the end of this section, you will:
- Design DIP-compliant architectures for enterprise systems
- Understand advanced dependency injection patterns
- Learn about IoC containers and their benefits
- Handle complex dependency graphs and lifecycles

### Example 5: Enterprise Application with IoC Container

Let's build a sophisticated IoC (Inversion of Control) container and use it in an enterprise application.

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, Callable, TypeVar, Type, Optional, List
from enum import Enum
import inspect
from dataclasses import dataclass
import threading

T = TypeVar('T')

class ServiceLifetime(Enum):
    SINGLETON = "singleton"
    TRANSIENT = "transient"
    SCOPED = "scoped"

@dataclass
class ServiceDescriptor:
    service_type: Type
    implementation_type: Optional[Type] = None
    factory: Optional[Callable] = None
    instance: Optional[Any] = None
    lifetime: ServiceLifetime = ServiceLifetime.TRANSIENT

class ServiceScope:
    def __init__(self):
        self._scoped_services = {}
        self._lock = threading.Lock()
    
    def get_scoped_service(self, service_type: Type):
        with self._lock:
            return self._scoped_services.get(service_type)
    
    def set_scoped_service(self, service_type: Type, instance: Any):
        with self._lock:
            self._scoped_services[service_type] = instance
    
    def dispose(self):
        with self._lock:
            for instance in self._scoped_services.values():
                if hasattr(instance, 'dispose'):
                    instance.dispose()
            self._scoped_services.clear()

class DependencyInjectionContainer:
    def __init__(self):
        self._services: Dict[Type, ServiceDescriptor] = {}
        self._singletons: Dict[Type, Any] = {}
        self._lock = threading.Lock()
        self._current_scope: Optional[ServiceScope] = None
    
    def register_singleton(self, service_type: Type, implementation_type: Type = None, factory: Callable = None):
        """Register a service as singleton"""
        self._register_service(service_type, implementation_type, factory, ServiceLifetime.SINGLETON)
        return self
    
    def register_transient(self, service_type: Type, implementation_type: Type = None, factory: Callable = None):
        """Register a service as transient (new instance each time)"""
        self._register_service(service_type, implementation_type, factory, ServiceLifetime.TRANSIENT)
        return self
    
    def register_scoped(self, service_type: Type, implementation_type: Type = None, factory: Callable = None):
        """Register a service as scoped (one instance per scope)"""
        self._register_service(service_type, implementation_type, factory, ServiceLifetime.SCOPED)
        return self
    
    def register_instance(self, service_type: Type, instance: Any):
        """Register a specific instance"""
        descriptor = ServiceDescriptor(
            service_type=service_type,
            instance=instance,
            lifetime=ServiceLifetime.SINGLETON
        )
        self._services[service_type] = descriptor
        return self
    
    def _register_service(self, service_type: Type, implementation_type: Type, factory: Callable, lifetime: ServiceLifetime):
        if implementation_type is None and factory is None:
            implementation_type = service_type
        
        descriptor = ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation_type,
            factory=factory,
            lifetime=lifetime
        )
        self._services[service_type] = descriptor
    
    def resolve(self, service_type: Type[T]) -> T:
        """Resolve a service instance"""
        if service_type not in self._services:
            raise ValueError(f"Service {service_type.__name__} is not registered")
        
        descriptor = self._services[service_type]
        
        # Handle singleton
        if descriptor.lifetime == ServiceLifetime.SINGLETON:
            if descriptor.instance is not None:
                return descriptor.instance
            
            with self._lock:
                if service_type in self._singletons:
                    return self._singletons[service_type]
                
                instance = self._create_instance(descriptor)
                self._singletons[service_type] = instance
                return instance
        
        # Handle scoped
        elif descriptor.lifetime == ServiceLifetime.SCOPED:
            if self._current_scope is None:
                raise ValueError("No active scope for scoped service")
            
            instance = self._current_scope.get_scoped_service(service_type)
            if instance is None:
                instance = self._create_instance(descriptor)
                self._current_scope.set_scoped_service(service_type, instance)
            return instance
        
        # Handle transient
        else:
            return self._create_instance(descriptor)
    
    def _create_instance(self, descriptor: ServiceDescriptor):
        """Create an instance using factory or constructor injection"""
        if descriptor.factory is not None:
            return descriptor.factory()
        
        if descriptor.implementation_type is None:
            raise ValueError("No implementation type or factory provided")
        
        # Get constructor and its parameters
        constructor = descriptor.implementation_type.__init__
        sig = inspect.signature(constructor)
        
        # Resolve constructor dependencies
        args = {}
        for param_name, param in sig.parameters.items():
            if param_name == 'self':
                continue
            
            if param.annotation == inspect.Parameter.empty:
                raise ValueError(f"Parameter {param_name} in {descriptor.implementation_type.__name__} has no type annotation")
            
            # Resolve dependency
            dependency = self.resolve(param.annotation)
            args[param_name] = dependency
        
        return descriptor.implementation_type(**args)
    
    def create_scope(self) -> ServiceScope:
        """Create a new service scope"""
        return ServiceScope()
    
    def __enter__(self):
        self._current_scope = self.create_scope()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._current_scope:
            self._current_scope.dispose()
            self._current_scope = None

# Enterprise application example
class ILogger(ABC):
    @abstractmethod
    def log_info(self, message: str):
        pass
    
    @abstractmethod
    def log_error(self, message: str):
        pass

class IUserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def save_user(self, user: Dict[str, Any]) -> bool:
        pass

class IEmailService(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        pass

class ICacheService(ABC):
    @abstractmethod
    def get(self, key: str) -> Any:
        pass
    
    @abstractmethod
    def set(self, key: str, value: Any, ttl: int = 3600):
        pass

class IMetricsService(ABC):
    @abstractmethod
    def increment_counter(self, metric: str):
        pass
    
    @abstractmethod
    def record_timing(self, metric: str, duration: float):
        pass

# Concrete implementations
class ConsoleLogger(ILogger):
    def log_info(self, message: str):
        print(f"INFO: {message}")
    
    def log_error(self, message: str):
        print(f"ERROR: {message}")

class DatabaseUserRepository(IUserRepository):
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.users = {}  # Simulated database
    
    def get_user(self, user_id: str) -> Dict[str, Any]:
        self.logger.log_info(f"Fetching user {user_id} from database")
        return self.users.get(user_id, {})
    
    def save_user(self, user: Dict[str, Any]) -> bool:
        user_id = user.get('id')
        self.users[user_id] = user
        self.logger.log_info(f"Saved user {user_id} to database")
        return True

class SMTPEmailService(IEmailService):
    def __init__(self, logger: ILogger):
        self.logger = logger
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        self.logger.log_info(f"Sending email to {to}: {subject}")
        # Simulate email sending
        return True

class RedisCache(ICacheService):
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.cache = {}  # Simulated Redis
    
    def get(self, key: str) -> Any:
        value = self.cache.get(key)
        self.logger.log_info(f"Cache GET {key}: {'HIT' if value else 'MISS'}")
        return value
    
    def set(self, key: str, value: Any, ttl: int = 3600):
        self.cache[key] = value
        self.logger.log_info(f"Cache SET {key} (TTL: {ttl})")

class PrometheusMetrics(IMetricsService):
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.counters = {}
        self.timings = {}
    
    def increment_counter(self, metric: str):
        self.counters[metric] = self.counters.get(metric, 0) + 1
        self.logger.log_info(f"Metric {metric} incremented to {self.counters[metric]}")
    
    def record_timing(self, metric: str, duration: float):
        if metric not in self.timings:
            self.timings[metric] = []
        self.timings[metric].append(duration)
        self.logger.log_info(f"Recorded timing for {metric}: {duration}ms")

# Business services
class UserService:
    def __init__(self, 
                 user_repository: IUserRepository, 
                 email_service: IEmailService,
                 cache_service: ICacheService,
                 metrics_service: IMetricsService,
                 logger: ILogger):
        self.user_repository = user_repository
        self.email_service = email_service
        self.cache_service = cache_service
        self.metrics_service = metrics_service
        self.logger = logger
    
    def get_user(self, user_id: str) -> Dict[str, Any]:
        import time
        start_time = time.time()
        
        self.metrics_service.increment_counter("user.get_requests")
        
        # Try cache first
        cache_key = f"user:{user_id}"
        cached_user = self.cache_service.get(cache_key)
        
        if cached_user:
            self.metrics_service.increment_counter("user.cache_hits")
            duration = (time.time() - start_time) * 1000
            self.metrics_service.record_timing("user.get_duration", duration)
            return cached_user
        
        # Fetch from repository
        user = self.user_repository.get_user(user_id)
        
        if user:
            # Cache the result
            self.cache_service.set(cache_key, user, ttl=1800)
            self.metrics_service.increment_counter("user.cache_misses")
        
        duration = (time.time() - start_time) * 1000
        self.metrics_service.record_timing("user.get_duration", duration)
        
        return user
    
    def create_user(self, user_data: Dict[str, Any]) -> bool:
        self.metrics_service.increment_counter("user.create_requests")
        
        # Save user
        success = self.user_repository.save_user(user_data)
        
        if success:
            # Send welcome email
            self.email_service.send_email(
                user_data.get('email', ''),
                "Welcome!",
                f"Welcome {user_data.get('name', 'User')}!"
            )
            
            # Invalidate cache
            cache_key = f"user:{user_data.get('id')}"
            self.cache_service.set(cache_key, user_data)
            
            self.logger.log_info(f"User {user_data.get('id')} created successfully")
            self.metrics_service.increment_counter("user.create_success")
        else:
            self.logger.log_error(f"Failed to create user {user_data.get('id')}")
            self.metrics_service.increment_counter("user.create_failures")
        
        return success

class OrderService:
    def __init__(self, 
                 user_service: UserService,
                 email_service: IEmailService,
                 metrics_service: IMetricsService,
                 logger: ILogger):
        self.user_service = user_service
        self.email_service = email_service
        self.metrics_service = metrics_service
        self.logger = logger
    
    def create_order(self, user_id: str, order_data: Dict[str, Any]) -> bool:
        self.metrics_service.increment_counter("order.create_requests")
        
        # Get user information
        user = self.user_service.get_user(user_id)
        if not user:
            self.logger.log_error(f"User {user_id} not found for order creation")
            return False
        
        # Process order (simplified)
        order_id = f"ORD-{hash(str(order_data)) % 1000000:06d}"
        self.logger.log_info(f"Processing order {order_id} for user {user_id}")
        
        # Send order confirmation
        self.email_service.send_email(
            user.get('email', ''),
            "Order Confirmation",
            f"Your order {order_id} has been confirmed!"
        )
        
        self.metrics_service.increment_counter("order.create_success")
        return True

# Application composition root
class ApplicationComposer:
    @staticmethod
    def compose_services() -> DependencyInjectionContainer:
        container = DependencyInjectionContainer()
        
        # Register infrastructure services as singletons
        container.register_singleton(ILogger, ConsoleLogger)
        container.register_singleton(ICacheService, RedisCache)
        container.register_singleton(IMetricsService, PrometheusMetrics)
        
        # Register data access as scoped
        container.register_scoped(IUserRepository, DatabaseUserRepository)
        container.register_scoped(IEmailService, SMTPEmailService)
        
        # Register business services as scoped
        container.register_scoped(UserService)
        container.register_scoped(OrderService)
        
        return container

# Example usage
print("=== Advanced DIP with IoC Container ===")

# Compose the application
container = ApplicationComposer.compose_services()

# Use scoped services
with container:
    # Resolve services - all dependencies are automatically injected
    user_service = container.resolve(UserService)
    order_service = container.resolve(OrderService)
    
    # Use the services
    print("\n--- Creating User ---")
    user_data = {
        "id": "USER-001",
        "name": "Alice Johnson",
        "email": "alice@example.com"
    }
    user_service.create_user(user_data)
    
    print("\n--- Getting User ---")
    retrieved_user = user_service.get_user("USER-001")
    print(f"Retrieved user: {retrieved_user}")
    
    print("\n--- Creating Order ---")
    order_data = {
        "items": [{"product": "Laptop", "quantity": 1, "price": 999.99}],
        "total": 999.99
    }
    order_service.create_order("USER-001", order_data)

print("\n--- Second Scope ---")
# Create another scope to demonstrate scoped lifetime
with container:
    user_service2 = container.resolve(UserService)
    
    # This will hit the cache from the previous scope
    print("\n--- Getting User Again (Different Scope) ---")
    retrieved_user2 = user_service2.get_user("USER-001")
    print(f"Retrieved user in new scope: {retrieved_user2}")
```

### Example 6: Aspect-Oriented Programming with DIP

Let's implement cross-cutting concerns using DIP and decorators.

```python
from abc import ABC, abstractmethod
from typing import Any, Callable
import time
import functools
from datetime import datetime

# Cross-cutting concern interfaces
class IAuditService(ABC):
    @abstractmethod
    def log_method_call(self, class_name: str, method_name: str, args: tuple, kwargs: dict):
        pass

class IPerformanceMonitor(ABC):
    @abstractmethod
    def start_timing(self, operation: str) -> str:
        pass
    
    @abstractmethod
    def end_timing(self, timing_id: str):
        pass

class ISecurityService(ABC):
    @abstractmethod
    def check_authorization(self, user_id: str, resource: str, action: str) -> bool:
        pass

# Implementations
class DatabaseAuditService(IAuditService):
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.audit_log = []
    
    def log_method_call(self, class_name: str, method_name: str, args: tuple, kwargs: dict):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "class": class_name,
            "method": method_name,
            "args": str(args),
            "kwargs": str(kwargs)
        }
        self.audit_log.append(entry)
        self.logger.log_info(f"AUDIT: {class_name}.{method_name} called")

class PerformanceMonitor(IPerformanceMonitor):
    def __init__(self, logger: ILogger, metrics_service: IMetricsService):
        self.logger = logger
        self.metrics_service = metrics_service
        self.active_timings = {}
    
    def start_timing(self, operation: str) -> str:
        timing_id = f"{operation}_{time.time()}"
        self.active_timings[timing_id] = {
            "operation": operation,
            "start_time": time.time()
        }
        return timing_id
    
    def end_timing(self, timing_id: str):
        if timing_id in self.active_timings:
            timing_info = self.active_timings[timing_id]
            duration = (time.time() - timing_info["start_time"]) * 1000
            
            self.logger.log_info(f"PERFORMANCE: {timing_info['operation']} took {duration:.2f}ms")
            self.metrics_service.record_timing(timing_info['operation'], duration)
            
            del self.active_timings[timing_id]

class RoleBasedSecurityService(ISecurityService):
    def __init__(self, logger: ILogger):
        self.logger = logger
        self.user_roles = {
            "admin": ["read", "write", "delete"],
            "user": ["read", "write"],
            "guest": ["read"]
        }
    
    def check_authorization(self, user_id: str, resource: str, action: str) -> bool:
        # Simplified role checking
        user_role = "user"  # Would normally look this up
        allowed_actions = self.user_roles.get(user_role, [])
        
        authorized = action in allowed_actions
        self.logger.log_info(f"SECURITY: User {user_id} {action} on {resource}: {'ALLOWED' if authorized else 'DENIED'}")
        
        return authorized

# Aspect decorators
def audited(audit_service: IAuditService):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            audit_service.log_method_call(
                self.__class__.__name__,
                func.__name__,
                args,
                kwargs
            )
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def timed(performance_monitor: IPerformanceMonitor):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            operation = f"{self.__class__.__name__}.{func.__name__}"
            timing_id = performance_monitor.start_timing(operation)
            try:
                result = func(self, *args, **kwargs)
                return result
            finally:
                performance_monitor.end_timing(timing_id)
        return wrapper
    return decorator

def secured(security_service: ISecurityService, resource: str, action: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # Assume first argument is user_id for simplicity
            user_id = args[0] if args else "anonymous"
            
            if not security_service.check_authorization(user_id, resource, action):
                raise PermissionError(f"Access denied for {action} on {resource}")
            
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

# Business service with aspects
class SecureUserService:
    def __init__(self, 
                 user_repository: IUserRepository,
                 audit_service: IAuditService,
                 performance_monitor: IPerformanceMonitor,
                 security_service: ISecurityService,
                 logger: ILogger):
        self.user_repository = user_repository
        self.audit_service = audit_service
        self.performance_monitor = performance_monitor
        self.security_service = security_service
        self.logger = logger
    
    @audited(lambda self: self.audit_service)
    @timed(lambda self: self.performance_monitor)
    @secured(lambda self: self.security_service, "user", "read")
    def get_user(self, user_id: str) -> Dict[str, Any]:
        return self.user_repository.get_user(user_id)
    
    @audited(lambda self: self.audit_service)
    @timed(lambda self: self.performance_monitor)
    @secured(lambda self: self.security_service, "user", "write")
    def create_user(self, user_id: str, user_data: Dict[str, Any]) -> bool:
        user_data['id'] = user_id
        return self.user_repository.save_user(user_data)
    
    @audited(lambda self: self.audit_service)
    @timed(lambda self: self.performance_monitor)
    @secured(lambda self: self.security_service, "user", "delete")
    def delete_user(self, user_id: str) -> bool:
        self.logger.log_info(f"Deleting user {user_id}")
        # Simulate deletion
        return True

# Enhanced composition root
class EnhancedApplicationComposer:
    @staticmethod
    def compose_services() -> DependencyInjectionContainer:
        container = DependencyInjectionContainer()
        
        # Register infrastructure services
        container.register_singleton(ILogger, ConsoleLogger)
        container.register_singleton(IMetricsService, PrometheusMetrics)
        container.register_singleton(IAuditService, DatabaseAuditService)
        container.register_singleton(IPerformanceMonitor, PerformanceMonitor)
        container.register_singleton(ISecurityService, RoleBasedSecurityService)
        
        # Register data access
        container.register_scoped(IUserRepository, DatabaseUserRepository)
        
        # Register enhanced business services
        container.register_scoped(SecureUserService)
        
        return container

# Example usage
print("\n=== Aspect-Oriented Programming with DIP ===")

enhanced_container = EnhancedApplicationComposer.compose_services()

with enhanced_container:
    secure_user_service = enhanced_container.resolve(SecureUserService)
    
    print("\n--- Secure Operations ---")
    
    try:
        # This should work (read permission)
        user = secure_user_service.get_user("USER-001")
        print("Get user operation completed")
        
        # This should work (write permission)
        secure_user_service.create_user("USER-002", {"name": "Bob", "email": "bob@example.com"})
        print("Create user operation completed")
        
        # This might fail depending on user role (delete permission)
        secure_user_service.delete_user("USER-002")
        print("Delete user operation completed")
        
    except PermissionError as e:
        print(f"Security error: {e}")
```

### Key Takeaways for Advanced Level

1. **IoC Containers**: Automate dependency resolution and lifecycle management
2. **Service Lifetimes**: Understand singleton, transient, and scoped lifetimes
3. **Constructor Injection**: Use reflection/inspection for automatic dependency injection
4. **Aspect-Oriented Programming**: Implement cross-cutting concerns using DIP
5. **Composition Root**: Centralize all dependency wiring in one place
6. **Enterprise Patterns**: Apply DIP to complex enterprise scenarios

---

## Expert Level: Architecture and Design Patterns

### 🎯 Learning Objectives
By the end of this section, you will:
- Master advanced architectural patterns using DIP
- Understand how DIP enables microservices architecture
- Implement sophisticated dependency injection frameworks
- Design plugin-based architectures
- Apply DIP in distributed systems

### Example 7: Microservices Architecture with DIP

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List
import asyncio

# Service discovery abstraction
class ServiceDiscovery(ABC):
    @abstractmethod
    async def register_service(self, service_name: str, endpoint: str) -> bool:
        pass
    
    @abstractmethod
    async def discover_service(self, service_name: str) -> str:
        pass

# Message broker abstraction
class MessageBroker(ABC):
    @abstractmethod
    async def publish(self, topic: str, message: Dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    async def subscribe(self, topic: str, callback) -> None:
        pass

# Configuration service abstraction
class ConfigurationService(ABC):
    @abstractmethod
    def get_config(self, key: str) -> Any:
        pass

# Microservice base class
class MicroService:
    def __init__(self, 
                 service_discovery: ServiceDiscovery,
                 message_broker: MessageBroker,
                 config_service: ConfigurationService):
        self.service_discovery = service_discovery
        self.message_broker = message_broker
        self.config_service = config_service
        self.service_name = self.__class__.__name__
    
    async def start(self):
        endpoint = self.config_service.get_config(f"{self.service_name}.endpoint")
        await self.service_discovery.register_service(self.service_name, endpoint)
        await self.setup_message_handlers()
    
    async def setup_message_handlers(self):
        # Override in subclasses
        pass

# Concrete implementations
class ConsulServiceDiscovery(ServiceDiscovery):
    async def register_service(self, service_name: str, endpoint: str) -> bool:
        print(f"Registering {service_name} at {endpoint} with Consul")
        return True
    
    async def discover_service(self, service_name: str) -> str:
        print(f"Discovering {service_name} from Consul")
        return f"http://localhost:8080/{service_name}"

class RabbitMQBroker(MessageBroker):
    async def publish(self, topic: str, message: Dict[str, Any]) -> bool:
        print(f"Publishing to {topic}: {message}")
        return True
    
    async def subscribe(self, topic: str, callback) -> None:
        print(f"Subscribing to {topic}")

class EtcdConfigService(ConfigurationService):
    def __init__(self):
        self.config = {
            "UserService.endpoint": "http://localhost:8001",
            "OrderService.endpoint": "http://localhost:8002"
        }
    
    def get_config(self, key: str) -> Any:
        return self.config.get(key)

# Business services
class UserService(MicroService):
    async def setup_message_handlers(self):
        await self.message_broker.subscribe("user.created", self.handle_user_created)
    
    async def handle_user_created(self, message: Dict[str, Any]):
        print(f"UserService handling: {message}")

class OrderService(MicroService):
    async def setup_message_handlers(self):
        await self.message_broker.subscribe("order.placed", self.handle_order_placed)
    
    async def handle_order_placed(self, message: Dict[str, Any]):
        print(f"OrderService handling: {message}")
        # Discover user service
        user_service_url = await self.service_discovery.discover_service("UserService")
        print(f"Calling user service at: {user_service_url}")

# Service composition
async def main():
    # Infrastructure dependencies
    service_discovery = ConsulServiceDiscovery()
    message_broker = RabbitMQBroker()
    config_service = EtcdConfigService()
    
    # Create services
    user_service = UserService(service_discovery, message_broker, config_service)
    order_service = OrderService(service_discovery, message_broker, config_service)
    
    # Start services
    await user_service.start()
    await order_service.start()
    
    # Simulate some activity
    await message_broker.publish("user.created", {"user_id": 123, "name": "Alice"})
    await message_broker.publish("order.placed", {"order_id": 456, "user_id": 123})

# asyncio.run(main())
```

### Example 8: Event-Driven Architecture with DIP

```python
from abc import ABC, abstractmethod
from typing import Dict, List, Callable, Any
from dataclasses import dataclass
from datetime import datetime
import uuid

# Event abstraction
@dataclass
class Event:
    id: str
    type: str
    data: Dict[str, Any]
    timestamp: datetime
    source: str

# Event store abstraction
class EventStore(ABC):
    @abstractmethod
    def append_event(self, stream_id: str, event: Event) -> bool:
        pass
    
    @abstractmethod
    def get_events(self, stream_id: str) -> List[Event]:
        pass

# Event bus abstraction
class EventBus(ABC):
    @abstractmethod
    def publish(self, event: Event) -> None:
        pass
    
    @abstractmethod
    def subscribe(self, event_type: str, handler: Callable[[Event], None]) -> None:
        pass

# Aggregate root base class
class AggregateRoot:
    def __init__(self, aggregate_id: str, event_store: EventStore, event_bus: EventBus):
        self.aggregate_id = aggregate_id
        self.event_store = event_store
        self.event_bus = event_bus
        self.uncommitted_events: List[Event] = []
        self.version = 0
    
    def apply_event(self, event: Event):
        self.uncommitted_events.append(event)
        self._when(event)
    
    def commit(self):
        for event in self.uncommitted_events:
            self.event_store.append_event(self.aggregate_id, event)
            self.event_bus.publish(event)
        self.uncommitted_events.clear()
    
    def _when(self, event: Event):
        # Override in subclasses to handle state changes
        pass

# Concrete implementations
class InMemoryEventStore(EventStore):
    def __init__(self):
        self.streams: Dict[str, List[Event]] = {}
    
    def append_event(self, stream_id: str, event: Event) -> bool:
        if stream_id not in self.streams:
            self.streams[stream_id] = []
        self.streams[stream_id].append(event)
        return True
    
    def get_events(self, stream_id: str) -> List[Event]:
        return self.streams.get(stream_id, [])

class InMemoryEventBus(EventBus):
    def __init__(self):
        self.handlers: Dict[str, List[Callable[[Event], None]]] = {}
    
    def publish(self, event: Event) -> None:
        handlers = self.handlers.get(event.type, [])
        for handler in handlers:
            handler(event)
    
    def subscribe(self, event_type: str, handler: Callable[[Event], None]) -> None:
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)

# Business domain example
class BankAccount(AggregateRoot):
    def __init__(self, account_id: str, event_store: EventStore, event_bus: EventBus):
        super().__init__(account_id, event_store, event_bus)
        self.balance = 0.0
        self.is_active = False
    
    def open_account(self, initial_deposit: float):
        event = Event(
            id=str(uuid.uuid4()),
            type="AccountOpened",
            data={"account_id": self.aggregate_id, "initial_deposit": initial_deposit},
            timestamp=datetime.now(),
            source="BankAccount"
        )
        self.apply_event(event)
    
    def deposit(self, amount: float):
        if not self.is_active:
            raise ValueError("Account is not active")
        
        event = Event(
            id=str(uuid.uuid4()),
            type="MoneyDeposited",
            data={"account_id": self.aggregate_id, "amount": amount},
            timestamp=datetime.now(),
            source="BankAccount"
        )
        self.apply_event(event)
    
    def _when(self, event: Event):
        if event.type == "AccountOpened":
            self.balance = event.data["initial_deposit"]
            self.is_active = True
        elif event.type == "MoneyDeposited":
            self.balance += event.data["amount"]

# Usage example
event_store = InMemoryEventStore()
event_bus = InMemoryEventBus()

# Create and use account
account = BankAccount("acc-123", event_store, event_bus)
account.open_account(1000.0)
account.deposit(500.0)
account.commit()

print(f"Account balance: {account.balance}")
print(f"Events stored: {len(event_store.get_events('acc-123'))}")
```

### Key Takeaways for Expert Level

1. **Architectural Patterns**: DIP enables sophisticated patterns like microservices, event sourcing, and CQRS
2. **Distributed Systems**: DIP facilitates loose coupling in distributed architectures
3. **Event-Driven Design**: Abstractions enable flexible event processing and domain modeling
4. **Framework Design**: Understanding DIP is crucial for creating reusable frameworks
5. **System Composition**: Expert-level DIP involves composing complex systems from simple abstractions

---

## Practical Exercises and Challenges

### 🏋️ Exercise 1: Basic DIP Implementation (Beginner)

**Challenge**: Refactor a tightly coupled logging system to follow DIP.

```python
# Starting code (DIP violation)
class FileLogger:
    def log(self, message):
        with open("app.log", "a") as f:
            f.write(f"{message}\n")

class Application:
    def __init__(self):
        self.logger = FileLogger()  # Tight coupling!
    
    def process_data(self, data):
        self.logger.log(f"Processing: {data}")
        # Process data...
        self.logger.log("Processing complete")

# Your task: Refactor this to follow DIP
# 1. Create an abstract Logger interface
# 2. Make FileLogger implement the interface
# 3. Add a ConsoleLogger implementation
# 4. Modify Application to depend on the abstraction
```

**Solution**:
```python
from abc import ABC, abstractmethod

# Step 1: Create abstraction
class ILogger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

# Step 2: Implement concrete loggers
class FileLogger(ILogger):
    def __init__(self, filename: str = "app.log"):
        self.filename = filename
    
    def log(self, message: str) -> None:
        with open(self.filename, "a") as f:
            f.write(f"{message}\n")

class ConsoleLogger(ILogger):
    def log(self, message: str) -> None:
        print(f"LOG: {message}")

# Step 3: Refactor Application
class Application:
    def __init__(self, logger: ILogger):
        self.logger = logger  # Depends on abstraction
    
    def process_data(self, data):
        self.logger.log(f"Processing: {data}")
        # Process data...
        self.logger.log("Processing complete")

# Usage
file_logger = FileLogger()
console_logger = ConsoleLogger()

app1 = Application(file_logger)
app2 = Application(console_logger)

app1.process_data("user_data.csv")
app2.process_data("sales_data.json")
```

### 🏋️ Exercise 2: Payment Processing System (Intermediate)

**Challenge**: Design a payment processing system that can handle multiple payment methods.

```python
# Requirements:
# 1. Support Credit Card, PayPal, and Bank Transfer payments
# 2. Each payment method has different validation rules
# 3. The payment processor should work with any payment method
# 4. Add logging and error handling
# 5. Make it easy to add new payment methods

# Your implementation here...
```

**Solution**:
```python
from abc import ABC, abstractmethod
from typing import Dict, Any
from enum import Enum

class PaymentStatus(Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"

class PaymentResult:
    def __init__(self, status: PaymentStatus, transaction_id: str = None, error_message: str = None):
        self.status = status
        self.transaction_id = transaction_id
        self.error_message = error_message

# Abstraction for payment methods
class IPaymentMethod(ABC):
    @abstractmethod
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> PaymentResult:
        pass

# Abstraction for logging
class IPaymentLogger(ABC):
    @abstractmethod
    def log_payment_attempt(self, method: str, amount: float) -> None:
        pass
    
    @abstractmethod
    def log_payment_result(self, result: PaymentResult) -> None:
        pass

# Concrete implementations
class CreditCardPayment(IPaymentMethod):
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        required_fields = ['card_number', 'expiry_date', 'cvv', 'cardholder_name']
        return all(field in payment_data for field in required_fields)
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> PaymentResult:
        if not self.validate_payment_data(payment_data):
            return PaymentResult(PaymentStatus.FAILED, error_message="Invalid card data")
        
        # Simulate payment processing
        transaction_id = f"CC_{hash(payment_data['card_number']) % 10000}"
        return PaymentResult(PaymentStatus.SUCCESS, transaction_id)

class PayPalPayment(IPaymentMethod):
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        return 'email' in payment_data and 'password' in payment_data
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> PaymentResult:
        if not self.validate_payment_data(payment_data):
            return PaymentResult(PaymentStatus.FAILED, error_message="Invalid PayPal credentials")
        
        transaction_id = f"PP_{hash(payment_data['email']) % 10000}"
        return PaymentResult(PaymentStatus.SUCCESS, transaction_id)

class BankTransferPayment(IPaymentMethod):
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        required_fields = ['account_number', 'routing_number', 'account_holder']
        return all(field in payment_data for field in required_fields)
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> PaymentResult:
        if not self.validate_payment_data(payment_data):
            return PaymentResult(PaymentStatus.FAILED, error_message="Invalid bank account data")
        
        transaction_id = f"BT_{hash(payment_data['account_number']) % 10000}"
        return PaymentResult(PaymentStatus.PENDING, transaction_id)

class ConsolePaymentLogger(IPaymentLogger):
    def log_payment_attempt(self, method: str, amount: float) -> None:
        print(f"Payment attempt: {method} for ${amount:.2f}")
    
    def log_payment_result(self, result: PaymentResult) -> None:
        print(f"Payment result: {result.status.value}")
        if result.transaction_id:
            print(f"Transaction ID: {result.transaction_id}")
        if result.error_message:
            print(f"Error: {result.error_message}")

# High-level payment processor
class PaymentProcessor:
    def __init__(self, logger: IPaymentLogger):
        self.logger = logger
    
    def process_payment(self, payment_method: IPaymentMethod, amount: float, payment_data: Dict[str, Any]) -> PaymentResult:
        method_name = payment_method.__class__.__name__
        self.logger.log_payment_attempt(method_name, amount)
        
        result = payment_method.process_payment(amount, payment_data)
        self.logger.log_payment_result(result)
        
        return result

# Usage example
logger = ConsolePaymentLogger()
processor = PaymentProcessor(logger)

# Credit card payment
cc_payment = CreditCardPayment()
cc_data = {
    'card_number': '1234567890123456',
    'expiry_date': '12/25',
    'cvv': '123',
    'cardholder_name': 'John Doe'
}
result1 = processor.process_payment(cc_payment, 100.00, cc_data)

# PayPal payment
paypal_payment = PayPalPayment()
paypal_data = {
    'email': 'user@example.com',
    'password': 'secret123'
}
result2 = processor.process_payment(paypal_payment, 75.50, paypal_data)

# Bank transfer
bank_payment = BankTransferPayment()
bank_data = {
    'account_number': '1234567890',
    'routing_number': '987654321',
    'account_holder': 'Jane Smith'
}
result3 = processor.process_payment(bank_payment, 200.00, bank_data)
```

### 🏋️ Exercise 3: Plugin Architecture (Advanced)

**Challenge**: Create a plugin system for a text editor that can load different file format handlers.

```python
# Requirements:
# 1. Support multiple file formats (JSON, XML, CSV, etc.)
# 2. Plugins should be loadable at runtime
# 3. Each plugin handles reading and writing its format
# 4. The editor should work with any plugin
# 5. Add plugin discovery and registration

# Your implementation here...
```

**Solution**:
```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Type
import json
import csv
import xml.etree.ElementTree as ET
from io import StringIO

# Plugin interface
class IFileFormatPlugin(ABC):
    @property
    @abstractmethod
    def file_extensions(self) -> List[str]:
        pass
    
    @property
    @abstractmethod
    def format_name(self) -> str:
        pass
    
    @abstractmethod
    def can_handle(self, filename: str) -> bool:
        pass
    
    @abstractmethod
    def read_file(self, content: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def write_file(self, data: Dict[str, Any]) -> str:
        pass

# Plugin registry
class PluginRegistry:
    def __init__(self):
        self._plugins: Dict[str, IFileFormatPlugin] = {}
    
    def register_plugin(self, plugin: IFileFormatPlugin) -> None:
        for ext in plugin.file_extensions:
            self._plugins[ext.lower()] = plugin
        print(f"Registered plugin: {plugin.format_name}")
    
    def get_plugin_for_file(self, filename: str) -> IFileFormatPlugin:
        ext = filename.split('.')[-1].lower()
        if ext in self._plugins:
            return self._plugins[ext]
        raise ValueError(f"No plugin found for file extension: {ext}")
    
    def list_supported_formats(self) -> List[str]:
        return list(set(plugin.format_name for plugin in self._plugins.values()))

# Concrete plugins
class JSONPlugin(IFileFormatPlugin):
    @property
    def file_extensions(self) -> List[str]:
        return ['json']
    
    @property
    def format_name(self) -> str:
        return "JSON"
    
    def can_handle(self, filename: str) -> bool:
        return filename.lower().endswith('.json')
    
    def read_file(self, content: str) -> Dict[str, Any]:
        return json.loads(content)
    
    def write_file(self, data: Dict[str, Any]) -> str:
        return json.dumps(data, indent=2)

class CSVPlugin(IFileFormatPlugin):
    @property
    def file_extensions(self) -> List[str]:
        return ['csv']
    
    @property
    def format_name(self) -> str:
        return "CSV"
    
    def can_handle(self, filename: str) -> bool:
        return filename.lower().endswith('.csv')
    
    def read_file(self, content: str) -> Dict[str, Any]:
        reader = csv.DictReader(StringIO(content))
        return {"rows": list(reader)}
    
    def write_file(self, data: Dict[str, Any]) -> str:
        if "rows" not in data or not data["rows"]:
            return ""
        
        output = StringIO()
        fieldnames = data["rows"][0].keys()
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data["rows"])
        return output.getvalue()

class XMLPlugin(IFileFormatPlugin):
    @property
    def file_extensions(self) -> List[str]:
        return ['xml']
    
    @property
    def format_name(self) -> str:
        return "XML"
    
    def can_handle(self, filename: str) -> bool:
        return filename.lower().endswith('.xml')
    
    def read_file(self, content: str) -> Dict[str, Any]:
        root = ET.fromstring(content)
        return self._element_to_dict(root)
    
    def write_file(self, data: Dict[str, Any]) -> str:
        root = self._dict_to_element("root", data)
        return ET.tostring(root, encoding='unicode')
    
    def _element_to_dict(self, element):
        result = {}
        if element.text and element.text.strip():
            result['text'] = element.text.strip()
        
        for child in element:
            child_data = self._element_to_dict(child)
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_data)
            else:
                result[child.tag] = child_data
        
        return result
    
    def _dict_to_element(self, tag, data):
        element = ET.Element(tag)
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'text':
                    element.text = str(value)
                else:
                    if isinstance(value, list):
                        for item in value:
                            element.append(self._dict_to_element(key, item))
                    else:
                        element.append(self._dict_to_element(key, value))
        else:
            element.text = str(data)
        return element

# Text editor that uses plugins
class TextEditor:
    def __init__(self, plugin_registry: PluginRegistry):
        self.plugin_registry = plugin_registry
        self.current_file = None
        self.current_data = None
    
    def open_file(self, filename: str, content: str) -> None:
        try:
            plugin = self.plugin_registry.get_plugin_for_file(filename)
            self.current_data = plugin.read_file(content)
            self.current_file = filename
            print(f"Opened {filename} using {plugin.format_name} plugin")
        except Exception as e:
            print(f"Error opening file: {e}")
    
    def save_file(self, filename: str = None) -> str:
        if self.current_data is None:
            raise ValueError("No data to save")
        
        target_file = filename or self.current_file
        if not target_file:
            raise ValueError("No filename specified")
        
        try:
            plugin = self.plugin_registry.get_plugin_for_file(target_file)
            content = plugin.write_file(self.current_data)
            print(f"Saved {target_file} using {plugin.format_name} plugin")
            return content
        except Exception as e:
            print(f"Error saving file: {e}")
            return ""
    
    def get_data(self) -> Dict[str, Any]:
        return self.current_data
    
    def set_data(self, data: Dict[str, Any]) -> None:
        self.current_data = data
    
    def list_supported_formats(self) -> List[str]:
        return self.plugin_registry.list_supported_formats()

# Usage example
print("=== Plugin Architecture Demo ===")

# Create registry and register plugins
registry = PluginRegistry()
registry.register_plugin(JSONPlugin())
registry.register_plugin(CSVPlugin())
registry.register_plugin(XMLPlugin())

# Create editor
editor = TextEditor(registry)

print(f"\nSupported formats: {editor.list_supported_formats()}")

# Test JSON
json_content = '{"name": "John", "age": 30, "city": "New York"}'
editor.open_file("data.json", json_content)
print(f"JSON data: {editor.get_data()}")

# Test CSV
csv_content = "name,age,city\nJohn,30,New York\nJane,25,Boston"
editor.open_file("data.csv", csv_content)
print(f"CSV data: {editor.get_data()}")

# Test XML
xml_content = "<person><name>John</name><age>30</age><city>New York</city></person>"
editor.open_file("data.xml", xml_content)
print(f"XML data: {editor.get_data()}")

# Modify data and save
editor.set_data({"person": {"name": "Alice", "age": 28, "city": "Seattle"}})
saved_content = editor.save_file("modified.xml")
print(f"\nSaved XML content:\n{saved_content}")
```

---

## Common Pitfalls and Troubleshooting

### 🚨 Common Mistakes and How to Fix Them

#### 1. **Creating Abstractions That Are Too Specific**

**❌ Problem**:
```python
# Too specific - tied to email implementation
class IEmailNotificationService(ABC):
    @abstractmethod
    def send_email(self, to_email: str, subject: str, body: str) -> bool:
        pass
```

**✅ Solution**:
```python
# Generic - works for any notification type
class INotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, subject: str, message: str) -> bool:
        pass
```

#### 2. **Leaky Abstractions**

**❌ Problem**:
```python
class IDataStorage(ABC):
    @abstractmethod
    def save_to_database(self, data: dict) -> bool:  # Leaks database implementation
        pass
```

**✅ Solution**:
```python
class IDataStorage(ABC):
    @abstractmethod
    def save(self, data: dict) -> bool:  # Generic operation
        pass
```

#### 3. **Dependency Injection in Wrong Places**

**❌ Problem**:
```python
class UserService:
    def create_user(self, user_data: dict, logger: ILogger):  # DI in method
        logger.log("Creating user")
        # ...
```

**✅ Solution**:
```python
class UserService:
    def __init__(self, logger: ILogger):  # DI in constructor
        self.logger = logger
    
    def create_user(self, user_data: dict):
        self.logger.log("Creating user")
        # ...
```

#### 4. **Not Using Dependency Injection Containers Properly**

**❌ Problem**:
```python
# Manual dependency creation everywhere
def create_user_service():
    logger = FileLogger()
    db = DatabaseConnection()
    repo = UserRepository(db)
    return UserService(repo, logger)
```

**✅ Solution**:
```python
# Use DI container
container = DIContainer()
container.register(ILogger, FileLogger)
container.register(IDatabase, DatabaseConnection)
container.register(IUserRepository, UserRepository)
container.register(UserService)

user_service = container.resolve(UserService)
```

### 🔧 Debugging DIP Issues

#### Checklist for DIP Compliance

1. **Dependency Direction Check**:
   - [ ] High-level modules don't import low-level modules directly
   - [ ] Both depend on abstractions (interfaces/abstract classes)
   - [ ] Concrete implementations implement abstractions

2. **Abstraction Quality Check**:
   - [ ] Abstractions are stable (don't change often)
   - [ ] Abstractions don't leak implementation details
   - [ ] Abstractions are focused on behavior, not implementation

3. **Dependency Injection Check**:
   - [ ] Dependencies are injected from outside
   - [ ] No direct instantiation of dependencies inside classes
   - [ ] Constructor injection is preferred over setter injection

4. **Testing Check**:
   - [ ] Easy to create mock implementations
   - [ ] Tests don't require real implementations
   - [ ] Dependencies can be easily substituted

#### Common Error Messages and Solutions

**Error**: `TypeError: Can't instantiate abstract class`
```python
# Problem: Trying to instantiate abstract class
service = INotificationService()  # ❌

# Solution: Use concrete implementation
service = EmailNotificationService()  # ✅
```

**Error**: `AttributeError: 'NoneType' object has no attribute`
```python
# Problem: Dependency not injected
class UserService:
    def __init__(self, logger: ILogger = None):  # ❌ Default None
        self.logger = logger

# Solution: Make dependency required
class UserService:
    def __init__(self, logger: ILogger):  # ✅ Required dependency
        self.logger = logger
```

---

## Performance Considerations

### 🚀 Optimizing DIP-Based Systems

#### 1. **Lazy Loading of Dependencies**

```python
from typing import Optional

class LazyUserService:
    def __init__(self, repository_factory: Callable[[], IUserRepository]):
        self._repository_factory = repository_factory
        self._repository: Optional[IUserRepository] = None
    
    @property
    def repository(self) -> IUserRepository:
        if self._repository is None:
            self._repository = self._repository_factory()
        return self._repository
    
    def get_user(self, user_id: str):
        return self.repository.get_by_id(user_id)
```

#### 2. **Singleton Pattern for Expensive Dependencies**

```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Expensive initialization
            cls._instance.connect()
        return cls._instance
    
    def connect(self):
        print("Establishing expensive database connection...")
        # Actual connection logic
```

#### 3. **Dependency Caching**

```python
class CachedDIContainer:
    def __init__(self):
        self._singletons = {}
        self._factories = {}
    
    def register_singleton(self, interface: Type, implementation: Type):
        self._factories[interface] = implementation
    
    def resolve(self, interface: Type):
        if interface in self._singletons:
            return self._singletons[interface]
        
        if interface in self._factories:
            instance = self._factories[interface]()
            self._singletons[interface] = instance
            return instance
        
        raise ValueError(f"No registration found for {interface}")
```

---

## Integration with Testing Frameworks

### 🧪 Testing DIP-Compliant Code

#### Unit Testing with Mocks

```python
import unittest
from unittest.mock import Mock, patch

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock(spec=IUserRepository)
        self.mock_logger = Mock(spec=ILogger)
        self.user_service = UserService(self.mock_repository, self.mock_logger)
    
    def test_create_user_success(self):
        # Arrange
        user_data = {"name": "John", "email": "john@example.com"}
        self.mock_repository.save.return_value = True
        
        # Act
        result = self.user_service.create_user(user_data)
        
        # Assert
        self.assertTrue(result)
        self.mock_repository.save.assert_called_once_with(user_data)
        self.mock_logger.log.assert_called()
    
    def test_create_user_failure(self):
        # Arrange
        user_data = {"name": "John", "email": "john@example.com"}
        self.mock_repository.save.return_value = False
        
        # Act
        result = self.user_service.create_user(user_data)
        
        # Assert
        self.assertFalse(result)
        self.mock_logger.log.assert_called()

if __name__ == '__main__':
    unittest.main()
```

#### Integration Testing with Test Doubles

```python
class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self.users = {}
    
    def save(self, user_data: dict) -> bool:
        user_id = user_data.get('id', len(self.users) + 1)
        self.users[user_id] = user_data
        return True
    
    def get_by_id(self, user_id: str) -> dict:
        return self.users.get(user_id)

class TestLogger(ILogger):
    def __init__(self):
        self.logs = []
    
    def log(self, message: str) -> None:
        self.logs.append(message)

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryUserRepository()
        self.logger = TestLogger()
        self.user_service = UserService(self.repository, self.logger)
    
    def test_full_user_workflow(self):
        # Create user
        user_data = {"id": "1", "name": "John", "email": "john@example.com"}
        created = self.user_service.create_user(user_data)
        self.assertTrue(created)
        
        # Retrieve user
        retrieved_user = self.user_service.get_user("1")
        self.assertEqual(retrieved_user["name"], "John")
        
        # Check logs
        self.assertGreater(len(self.logger.logs), 0)
```

---

## Migration Strategies

### 🔄 Refactoring Legacy Code to Follow DIP

#### Step-by-Step Migration Process

**Step 1: Identify Dependencies**
```python
# Legacy code analysis
class OrderProcessor:
    def __init__(self):
        self.email_service = SMTPEmailService()  # Direct dependency
        self.payment_gateway = StripePaymentGateway()  # Direct dependency
        self.inventory = DatabaseInventory()  # Direct dependency
```

**Step 2: Extract Interfaces**
```python
# Create abstractions
class IEmailService(ABC):
    @abstractmethod
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        pass

class IPaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        pass

class IInventory(ABC):
    @abstractmethod
    def check_availability(self, product_id: str, quantity: int) -> bool:
        pass
    
    @abstractmethod
    def reserve_items(self, product_id: str, quantity: int) -> bool:
        pass
```

**Step 3: Implement Interfaces**
```python
# Make existing classes implement interfaces
class SMTPEmailService(IEmailService):
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        # Existing implementation
        pass

class StripePaymentGateway(IPaymentGateway):
    def process_payment(self, amount: float, payment_info: dict) -> bool:
        # Existing implementation
        pass

class DatabaseInventory(IInventory):
    def check_availability(self, product_id: str, quantity: int) -> bool:
        # Existing implementation
        pass
    
    def reserve_items(self, product_id: str, quantity: int) -> bool:
        # Existing implementation
        pass
```

**Step 4: Refactor Client Code**
```python
# Refactored OrderProcessor
class OrderProcessor:
    def __init__(self, 
                 email_service: IEmailService,
                 payment_gateway: IPaymentGateway,
                 inventory: IInventory):
        self.email_service = email_service
        self.payment_gateway = payment_gateway
        self.inventory = inventory
    
    # Rest of the implementation remains the same
```

**Step 5: Update Composition Root**
```python
# Create composition root
def create_order_processor():
    email_service = SMTPEmailService()
    payment_gateway = StripePaymentGateway()
    inventory = DatabaseInventory()
    
    return OrderProcessor(email_service, payment_gateway, inventory)
```

#### Gradual Migration Techniques

**Technique 1: Adapter Pattern for Legacy Integration**
```python
class LegacyEmailServiceAdapter(IEmailService):
    def __init__(self, legacy_service):
        self.legacy_service = legacy_service
    
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        # Adapt legacy interface to new interface
        return self.legacy_service.send_message(recipient, f"{subject}: {body}")
```

**Technique 2: Feature Toggles**
```python
class ConfigurableOrderProcessor:
    def __init__(self, config: dict):
        if config.get('use_new_email_service', False):
            self.email_service = NewEmailService()
        else:
            self.email_service = LegacyEmailServiceAdapter(LegacyEmailService())
```

---

## Conclusion and Next Steps

### 🎯 Key Takeaways

1. **DIP is about direction**: Dependencies should flow toward abstractions, not implementations
2. **Abstractions are contracts**: They define what can be done, not how it's done
3. **Dependency injection is the mechanism**: It's how we achieve dependency inversion
4. **Testing becomes easier**: Mock objects and test doubles are natural with DIP
5. **Flexibility is the goal**: Easy to swap implementations and extend functionality

### 🚀 Next Steps for Mastery

1. **Practice with Real Projects**: Apply DIP to your current codebase
2. **Learn DI Frameworks**: Explore frameworks like `dependency-injector` for Python
3. **Study Architecture Patterns**: Learn about Clean Architecture, Hexagonal Architecture
4. **Read More**: Study "Clean Architecture" by Robert C. Martin
5. **Join Communities**: Participate in discussions about software architecture

### 📚 Recommended Reading

- **Books**:
  - "Clean Architecture" by Robert C. Martin
  - "Dependency Injection in .NET" by Mark Seemann (concepts apply to Python)
  - "Patterns of Enterprise Application Architecture" by Martin Fowler

- **Articles**:
  - "The Dependency Inversion Principle" by Robert C. Martin
  - "Inversion of Control Containers and the Dependency Injection pattern" by Martin Fowler

### 🛠️ Tools and Libraries

- **Python DI Frameworks**:
  - `dependency-injector`: Comprehensive DI framework
  - `punq`: Lightweight DI container
  - `pinject`: Google's dependency injection library

- **Testing Tools**:
  - `unittest.mock`: Built-in mocking framework
  - `pytest-mock`: Pytest plugin for mocking
  - `factory_boy`: Test data generation

### 💡 Final Thoughts

The Dependency Inversion Principle is more than just a coding technique—it's a mindset that leads to better software architecture. By consistently applying DIP, you'll create systems that are:

- **More testable**: Easy to unit test with mocks
- **More flexible**: Easy to change implementations
- **More maintainable**: Changes are isolated and controlled
- **More reusable**: Components can be used in different contexts

Remember: **"Depend on abstractions, not concretions"** is not just a rule—it's a pathway to better software design.

---

*Happy coding! 🚀*