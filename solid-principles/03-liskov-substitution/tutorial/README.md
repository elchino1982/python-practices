# Liskov Substitution Principle (LSP) - Comprehensive Tutorial

## Table of Contents
1. [Introduction](#introduction)
2. [What is the Liskov Substitution Principle?](#what-is-the-liskov-substitution-principle)
3. [Why LSP Matters](#why-lsp-matters)
4. [Basic Concepts](#basic-concepts)
5. [Common Violations](#common-violations)
6. [Beginner Level Examples](#beginner-level-examples)
7. [Intermediate Level Examples](#intermediate-level-examples)
8. [Advanced Level Examples](#advanced-level-examples)
9. [Expert Level Concepts](#expert-level-concepts)
10. [Best Practices](#best-practices)
11. [Common Pitfalls](#common-pitfalls)
12. [Real-World Applications](#real-world-applications)
13. [Testing LSP Compliance](#testing-lsp-compliance)
14. [Summary](#summary)

---

## Introduction

The Liskov Substitution Principle (LSP) is the third principle in the SOLID design principles, named after Barbara Liskov who introduced it in 1987. It's one of the most important principles for creating robust, maintainable object-oriented code.

**Barbara Liskov's Original Definition (1987):**
> "What is wanted here is something like the following substitution property: If for each object o1 of type S there is an object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2 then S is a subtype of T."

**Simplified Definition:**
> Objects of a superclass should be replaceable with objects of a subclass without breaking the application.

---

## What is the Liskov Substitution Principle?

The LSP states that **derived classes must be substitutable for their base classes**. This means:

1. **Behavioral Compatibility**: Subclasses should behave in a way that doesn't break the expectations set by the parent class
2. **Contract Preservation**: The "contract" defined by the base class (preconditions, postconditions, invariants) must be honored
3. **Semantic Consistency**: The meaning and purpose of methods should remain consistent across the inheritance hierarchy

### Key Components:

- **Preconditions**: What must be true before a method is called
- **Postconditions**: What must be true after a method completes
- **Invariants**: What must always be true about the object's state
- **History Constraint**: Properties that must be preserved over time

---

## Why LSP Matters

### 🎯 Benefits of Following LSP:

1. **Reliability**: Code behaves predictably when using inheritance
2. **Maintainability**: Changes to subclasses don't break existing code
3. **Extensibility**: New subclasses can be added without modifying existing code
4. **Polymorphism**: True polymorphic behavior without surprises
5. **Testing**: Base class tests can validate subclass behavior

### 💥 Problems When LSP is Violated:

1. **Runtime Errors**: Unexpected exceptions or crashes
2. **Broken Polymorphism**: Need to check types before using objects
3. **Fragile Code**: Changes in one place break code elsewhere
4. **Maintenance Nightmare**: Difficult to extend or modify
5. **Testing Issues**: Need separate tests for each subclass

---

## Basic Concepts

### The "IS-A" Relationship vs "BEHAVES-LIKE-A"

Many developers confuse the "IS-A" relationship with proper substitutability:

```python
# ❌ WRONG: Just because a square IS-A rectangle doesn't mean it BEHAVES-LIKE-A rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):  # Square IS-A Rectangle, but...
    def set_width(self, width):
        self.width = width
        self.height = width  # This breaks LSP!
    
    def set_height(self, height):
        self.width = height
        self.height = height  # This breaks LSP!

# This code will fail with Square but work with Rectangle
def test_rectangle(rect):
    rect.set_width(5)
    rect.set_height(4)
    assert rect.area() == 20  # Fails for Square!
```

### Contract Rules for LSP Compliance:

1. **Preconditions cannot be strengthened** in subclasses
2. **Postconditions cannot be weakened** in subclasses
3. **Invariants must be preserved** in subclasses
4. **History constraint** (immutable properties must remain immutable)

---

## Common Violations

### 1. Strengthening Preconditions

```python
# ❌ BAD: Subclass requires more restrictive input
class Bird:
    def fly(self, altitude):
        if altitude < 0:
            raise ValueError("Altitude cannot be negative")
        return f"Flying at {altitude} feet"

class Eagle(Bird):
    def fly(self, altitude):
        if altitude < 1000:  # Stronger precondition!
            raise ValueError("Eagles must fly above 1000 feet")
        return f"Eagle soaring at {altitude} feet"
```

### 2. Weakening Postconditions

```python
# ❌ BAD: Subclass doesn't guarantee what parent promises
class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b  # Always returns a number

class WeirdCalculator(Calculator):
    def divide(self, a, b):
        if b == 0:
            return "undefined"  # Weaker postcondition!
        return a / b
```

### 3. Changing Method Signatures

```python
# ❌ BAD: Subclass changes expected interface
class FileProcessor:
    def process(self, filename):
        with open(filename, 'r') as f:
            return f.read()

class DatabaseProcessor(FileProcessor):
    def process(self, filename, connection):  # Changed signature!
        # Process with database connection
        pass
```

---

## Beginner Level Examples

### Example 1: Basic Bird Hierarchy (From our exercises)

Let's look at a proper implementation that follows LSP:

```python
from abc import ABC, abstractmethod

# ✅ GOOD: Proper abstraction
class Bird(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def move(self):
        """All birds can move, but in different ways"""
        pass
    
    def eat(self):
        return f"{self.name} is eating"

class FlyingBird(Bird):
    def move(self):
        return f"{self.name} is flying"
    
    def fly(self):
        return f"{self.name} is soaring through the sky"

class FlightlessBird(Bird):
    def move(self):
        return f"{self.name} is walking/running"

class Eagle(FlyingBird):
    def move(self):
        return f"{self.name} is flying majestically"

class Penguin(FlightlessBird):
    def move(self):
        return f"{self.name} is waddling"
    
    def swim(self):
        return f"{self.name} is swimming"

# ✅ This works perfectly - all birds can be substituted
def make_bird_move(bird: Bird):
    return bird.move()

# Usage
birds = [Eagle("Golden Eagle"), Penguin("Emperor Penguin")]
for bird in birds:
    print(make_bird_move(bird))  # Works for all!
```

### Example 2: Shape Hierarchy

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# ✅ Perfect substitutability
def calculate_total_area(shapes):
    return sum(shape.area() for shape in shapes)

shapes = [Circle(5), Rectangle(4, 6)]
print(f"Total area: {calculate_total_area(shapes)}")
```

---

## Intermediate Level Examples

### Example 3: Vehicle Hierarchy with Engine Management

```python
from abc import ABC, abstractmethod
from enum import Enum

class EngineState(Enum):
    STOPPED = "stopped"
    RUNNING = "running"
    MAINTENANCE = "maintenance"

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._engine_state = EngineState.STOPPED
    
    @abstractmethod
    def start_engine(self):
        """Start the vehicle's engine"""
        pass
    
    def stop_engine(self):
        """Stop the vehicle's engine"""
        if self._engine_state == EngineState.RUNNING:
            self._engine_state = EngineState.STOPPED
            return f"{self.make} {self.model} engine stopped"
        return f"{self.make} {self.model} engine is already stopped"
    
    @property
    def engine_state(self):
        return self._engine_state
    
    def get_info(self):
        return f"{self.make} {self.model} - Engine: {self._engine_state.value}"

class Car(Vehicle):
    def start_engine(self):
        if self._engine_state == EngineState.STOPPED:
            self._engine_state = EngineState.RUNNING
            return f"{self.make} {self.model} car engine started with ignition"
        return f"{self.make} {self.model} car engine is already running"

class Motorcycle(Vehicle):
    def start_engine(self):
        if self._engine_state == EngineState.STOPPED:
            self._engine_state = EngineState.RUNNING
            return f"{self.make} {self.model} motorcycle engine started with kick/button"
        return f"{self.make} {self.model} motorcycle engine is already running"

class ElectricCar(Vehicle):
    def start_engine(self):
        # Electric cars don't have traditional engines, but we maintain the contract
        if self._engine_state == EngineState.STOPPED:
            self._engine_state = EngineState.RUNNING
            return f"{self.make} {self.model} electric motor activated"
        return f"{self.make} {self.model} electric motor is already active"

# ✅ Perfect LSP compliance - all vehicles can be used interchangeably
def start_vehicle_fleet(vehicles):
    results = []
    for vehicle in vehicles:
        result = vehicle.start_engine()
        results.append(result)
    return results

# Usage
fleet = [
    Car("Toyota", "Camry"),
    Motorcycle("Harley", "Davidson"),
    ElectricCar("Tesla", "Model 3")
]

for result in start_vehicle_fleet(fleet):
    print(result)
```

### Example 4: Payment Processing System

```python
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict, Any

class PaymentResult:
    def __init__(self, success: bool, transaction_id: str = None, error_message: str = None):
        self.success = success
        self.transaction_id = transaction_id
        self.error_message = error_message

class PaymentProcessor(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def process_payment(self, amount: Decimal, payment_details: Dict[str, Any]) -> PaymentResult:
        """Process a payment and return the result"""
        pass
    
    def validate_amount(self, amount: Decimal) -> bool:
        """Common validation for all payment processors"""
        return amount > 0

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: Decimal, payment_details: Dict[str, Any]) -> PaymentResult:
        if not self.validate_amount(amount):
            return PaymentResult(False, error_message="Invalid amount")
        
        # Simulate credit card processing
        card_number = payment_details.get('card_number')
        if not card_number or len(card_number) != 16:
            return PaymentResult(False, error_message="Invalid card number")
        
        transaction_id = f"CC_{card_number[-4:]}_{amount}"
        return PaymentResult(True, transaction_id=transaction_id)

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: Decimal, payment_details: Dict[str, Any]) -> PaymentResult:
        if not self.validate_amount(amount):
            return PaymentResult(False, error_message="Invalid amount")
        
        # Simulate PayPal processing
        email = payment_details.get('email')
        if not email or '@' not in email:
            return PaymentResult(False, error_message="Invalid email")
        
        transaction_id = f"PP_{email.split('@')[0]}_{amount}"
        return PaymentResult(True, transaction_id=transaction_id)

class CryptoProcessor(PaymentProcessor):
    def process_payment(self, amount: Decimal, payment_details: Dict[str, Any]) -> PaymentResult:
        if not self.validate_amount(amount):
            return PaymentResult(False, error_message="Invalid amount")
        
        # Simulate crypto processing
        wallet_address = payment_details.get('wallet_address')
        if not wallet_address or len(wallet_address) < 26:
            return PaymentResult(False, error_message="Invalid wallet address")
        
        transaction_id = f"CRYPTO_{wallet_address[:8]}_{amount}"
        return PaymentResult(True, transaction_id=transaction_id)

# ✅ All processors follow the same contract
def process_order_payment(processor: PaymentProcessor, amount: Decimal, details: Dict[str, Any]):
    print(f"Processing ${amount} with {processor.name}")
    result = processor.process_payment(amount, details)
    
    if result.success:
        print(f"✅ Payment successful! Transaction ID: {result.transaction_id}")
    else:
        print(f"❌ Payment failed: {result.error_message}")
    
    return result

# Usage
processors = [
    CreditCardProcessor("Credit Card"),
    PayPalProcessor("PayPal"),
    CryptoProcessor("Cryptocurrency")
]

payment_details = [
    {'card_number': '1234567890123456'},
    {'email': 'user@example.com'},
    {'wallet_address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'}
]

for processor, details in zip(processors, payment_details):
    process_order_payment(processor, Decimal('99.99'), details)
    print()
```

---

## Advanced Level Examples

### Example 5: Database Connection Pool with Different Backends

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import threading
import time
from contextlib import contextmanager

class DatabaseConnection(ABC):
    def __init__(self, connection_id: str):
        self.connection_id = connection_id
        self.is_active = False
        self.last_used = time.time()
    
    @abstractmethod
    def connect(self) -> bool:
        """Establish connection to database"""
        pass
    
    @abstractmethod
    def disconnect(self) -> bool:
        """Close connection to database"""
        pass
    
    @abstractmethod
    def execute_query(self, query: str, params: Optional[Dict] = None) -> Any:
        """Execute a query and return results"""
        pass
    
    def is_healthy(self) -> bool:
        """Check if connection is healthy"""
        return self.is_active and (time.time() - self.last_used) < 300  # 5 minutes

class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, connection_id: str, host: str, database: str):
        super().__init__(connection_id)
        self.host = host
        self.database = database
    
    def connect(self) -> bool:
        # Simulate PostgreSQL connection
        print(f"Connecting to PostgreSQL at {self.host}/{self.database}")
        self.is_active = True
        return True
    
    def disconnect(self) -> bool:
        print(f"Disconnecting from PostgreSQL {self.connection_id}")
        self.is_active = False
        return True
    
    def execute_query(self, query: str, params: Optional[Dict] = None) -> Any:
        if not self.is_active:
            raise RuntimeError("Connection not active")
        
        self.last_used = time.time()
        # Simulate PostgreSQL-specific query execution
        return f"PostgreSQL result for: {query}"

class MySQLConnection(DatabaseConnection):
    def __init__(self, connection_id: str, host: str, database: str):
        super().__init__(connection_id)
        self.host = host
        self.database = database
    
    def connect(self) -> bool:
        # Simulate MySQL connection
        print(f"Connecting to MySQL at {self.host}/{self.database}")
        self.is_active = True
        return True
    
    def disconnect(self) -> bool:
        print(f"Disconnecting from MySQL {self.connection_id}")
        self.is_active = False
        return True
    
    def execute_query(self, query: str, params: Optional[Dict] = None) -> Any:
        if not self.is_active:
            raise RuntimeError("Connection not active")
        
        self.last_used = time.time()
        # Simulate MySQL-specific query execution
        return f"MySQL result for: {query}"

class MongoDBConnection(DatabaseConnection):
    def __init__(self, connection_id: str, host: str, database: str):
        super().__init__(connection_id)
        self.host = host
        self.database = database
    
    def connect(self) -> bool:
        # Simulate MongoDB connection
        print(f"Connecting to MongoDB at {self.host}/{self.database}")
        self.is_active = True
        return True
    
    def disconnect(self) -> bool:
        print(f"Disconnecting from MongoDB {self.connection_id}")
        self.is_active = False
        return True
    
    def execute_query(self, query: str, params: Optional[Dict] = None) -> Any:
        if not self.is_active:
            raise RuntimeError("Connection not active")
        
        self.last_used = time.time()
        # Simulate MongoDB-specific query execution (could be different format)
        return f"MongoDB result for: {query}"

class ConnectionPool:
    def __init__(self, max_connections: int = 10):
        self.max_connections = max_connections
        self.available_connections: List[DatabaseConnection] = []
        self.used_connections: List[DatabaseConnection] = []
        self._lock = threading.Lock()
    
    def add_connection(self, connection: DatabaseConnection):
        """Add a connection to the pool"""
        with self._lock:
            if len(self.available_connections) + len(self.used_connections) < self.max_connections:
                connection.connect()
                self.available_connections.append(connection)
                return True
            return False
    
    @contextmanager
    def get_connection(self):
        """Get a connection from the pool (context manager)"""
        connection = None
        try:
            with self._lock:
                if not self.available_connections:
                    raise RuntimeError("No available connections")
                
                connection = self.available_connections.pop()
                self.used_connections.append(connection)
            
            yield connection
        
        finally:
            if connection:
                with self._lock:
                    self.used_connections.remove(connection)
                    if connection.is_healthy():
                        self.available_connections.append(connection)
                    else:
                        connection.disconnect()
    
    def cleanup_stale_connections(self):
        """Remove unhealthy connections"""
        with self._lock:
            healthy_connections = []
            for conn in self.available_connections:
                if conn.is_healthy():
                    healthy_connections.append(conn)
                else:
                    conn.disconnect()
            self.available_connections = healthy_connections

# ✅ Perfect LSP compliance - all database types work identically
def execute_queries_on_different_databases():
    pool = ConnectionPool()
    
    # Add different types of database connections
    connections = [
        PostgreSQLConnection("pg_1", "localhost", "app_db"),
        MySQLConnection("mysql_1", "localhost", "app_db"),
        MongoDBConnection("mongo_1", "localhost", "app_db")
    ]
    
    for conn in connections:
        pool.add_connection(conn)
    
    # Execute queries - same code works for all database types!
    queries = [
        "SELECT * FROM users",
        "SELECT COUNT(*) FROM orders",
        "SELECT * FROM products WHERE price > 100"
    ]
    
    for query in queries:
        try:
            with pool.get_connection() as conn:
                result = conn.execute_query(query)
                print(f"Query: {query}")
                print(f"Result: {result}")
                print(f"Connection type: {type(conn).__name__}")
                print("-" * 50)
        except RuntimeError as e:
            print(f"Error: {e}")

# Usage
execute_queries_on_different_databases()
```

### Example 6: Event Processing System with Different Handlers

```python
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from datetime import datetime
import json

class Event:
    def __init__(self, event_type: str, data: Dict[str, Any], timestamp: datetime = None):
        self.event_type = event_type
        self.data = data
        self.timestamp = timestamp or datetime.now()
        self.processed = False
    
    def to_dict(self):
        return {
            'event_type': self.event_type,
            'data': self.data,
            'timestamp': self.timestamp.isoformat(),
            'processed': self.processed
        }

class EventHandler(ABC):
    def __init__(self, name: str):
        self.name = name
        self.processed_count = 0
    
    @abstractmethod
    def can_handle(self, event: Event) -> bool:
        """Check if this handler can process the event"""
        pass
    
    @abstractmethod
    def handle(self, event: Event) -> bool:
        """Process the event and return success status"""
        pass
    
    def get_stats(self) -> Dict[str, Any]:
        """Get handler statistics"""
        return {
            'name': self.name,
            'processed_count': self.processed_count
        }

class EmailEventHandler(EventHandler):
    def can_handle(self, event: Event) -> bool:
        return event.event_type in ['user_registered', 'password_reset', 'order_confirmed']
    
    def handle(self, event: Event) -> bool:
        if not self.can_handle(event):
            return False
        
        # Simulate email processing
        email_templates = {
            'user_registered': 'Welcome email',
            'password_reset': 'Password reset email',
            'order_confirmed': 'Order confirmation email'
        }
        
        template = email_templates.get(event.event_type)
        recipient = event.data.get('email', 'unknown@example.com')
        
        print(f"📧 Sending {template} to {recipient}")
        self.processed_count += 1
        event.processed = True
        return True

class NotificationEventHandler(EventHandler):
    def can_handle(self, event: Event) -> bool:
        return event.event_type in ['order_shipped', 'payment_failed', 'system_alert']
    
    def handle(self, event: Event) -> bool:
        if not self.can_handle(event):
            return False
        
        # Simulate push notification
        notification_types = {
            'order_shipped': 'Your order has been shipped!',
            'payment_failed': 'Payment failed - please update payment method',
            'system_alert': 'System maintenance scheduled'
        }
        
        message = notification_types.get(event.event_type)
        user_id = event.data.get('user_id', 'unknown')
        
        print(f"🔔 Push notification to user {user_id}: {message}")
        self.processed_count += 1
        event.processed = True
        return True

class AnalyticsEventHandler(EventHandler):
    def can_handle(self, event: Event) -> bool:
        # Analytics handler can process any event
        return True
    
    def handle(self, event: Event) -> bool:
        # Simulate analytics processing
        print(f"📊 Analytics: Recording {event.event_type} event")
        
        # Log event data for analytics
        analytics_data = {
            'event': event.event_type,
            'timestamp': event.timestamp.isoformat(),
            'data_keys': list(event.data.keys())
        }
        
        print(f"📊 Analytics data: {json.dumps(analytics_data, indent=2)}")
        self.processed_count += 1
        return True  # Analytics doesn't mark event as processed

class EventProcessor:
    def __init__(self):
        self.handlers: List[EventHandler] = []
    
    def register_handler(self, handler: EventHandler):
        """Register an event handler"""
        self.handlers.append(handler)
    
    def process_event(self, event: Event) -> bool:
        """Process an event with all applicable handlers"""
        processed_by_any = False
        
        for handler in self.handlers:
            if handler.can_handle(event):
                try:
                    success = handler.handle(event)
                    if success:
                        processed_by_any = True
                        print(f"✅ Event processed by {handler.name}")
                    else:
                        print(f"❌ Event processing failed by {handler.name}")
                except Exception as e:
                    print(f"💥 Error in {handler.name}: {e}")
        
        return processed_by_any
    
    def get_all_stats(self) -> List[Dict[str, Any]]:
        """Get statistics for all handlers"""
        return [handler.get_stats() for handler in self.handlers]

# ✅ Perfect LSP compliance - all handlers work identically
def demonstrate_event_processing():
    processor = EventProcessor()
    
    # Register different types of handlers
    handlers = [
        EmailEventHandler("Email Service"),
        NotificationEventHandler("Push Notification Service"),
        AnalyticsEventHandler("Analytics Service")
    ]
    
    for handler in handlers:
        processor.register_handler(handler)
    
    # Create various events
    events = [
        Event("user_registered", {"email": "user@example.com", "user_id": "123"}),
        Event("order_shipped", {"user_id": "123", "order_id": "ORD-456"}),
        Event("payment_failed", {"user_id": "123", "amount": 99.99}),
        Event("password_reset", {"email": "user@example.com"}),
        Event("system_alert", {"severity": "high", "message": "Database maintenance"})
    ]
    
    # Process all events
    for event in events:
        print(f"\n🎯 Processing event: {event.event_type}")
        print("-" * 60)
        processor.process_event(event)
    
    # Show statistics
    print("\n📈 Handler Statistics:")
    print("=" * 60)
    for stats in processor.get_all_stats():
        print(f"{stats['name']}: {stats['processed_count']} events processed")

# Usage
demonstrate_event_processing()
```

---

## Expert Level Concepts

### Covariance and Contravariance in LSP

Understanding how LSP relates to type variance is crucial for expert-level design:

```python
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

# Covariance: Return types can be more specific (subtypes)
class Animal:
    def __init__(self, name: str):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} barks!"

class Cat(Animal):
    def meow(self):
        return f"{self.name} meows!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self, name: str) -> Animal:
        """Base factory returns Animal"""
        pass

class DogFactory(AnimalFactory):
    def create_animal(self, name: str) -> Dog:  # ✅ Covariant return type
        """Can return more specific type (Dog)"""
        return Dog(name)

class CatFactory(AnimalFactory):
    def create_animal(self, name: str) -> Cat:  # ✅ Covariant return type
        """Can return more specific type (Cat)"""
        return Cat(name)

# Contravariance: Parameter types can be more general (supertypes)
class AnimalHandler(ABC):
    @abstractmethod
    def handle(self, animal: Dog) -> str:
        """Base handler expects Dog"""
        pass

class GeneralAnimalHandler(AnimalHandler):
    def handle(self, animal: Animal) -> str:  # ✅ Contravariant parameter type
        """Can accept more general type (Animal)"""
        return f"Handling {animal.name}"
```

### Advanced Contract Design

```python
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from dataclasses import dataclass
from enum import Enum

class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

@dataclass
class TransactionResult:
    status: TransactionStatus
    transaction_id: str
    amount: float
    fee: float = 0.0
    error_message: str = None

@runtime_checkable
class Auditable(Protocol):
    """Protocol for auditable operations"""
    def get_audit_trail(self) -> List[str]:
        ...

class FinancialTransaction(ABC):
    """
    Advanced contract with comprehensive pre/post conditions
    
    Invariants:
    - Transaction amount must always be positive
    - Transaction ID must be unique and immutable
    - Status transitions must follow valid state machine
    
    Preconditions:
    - Amount > 0
    - Valid account information
    
    Postconditions:
    - Transaction recorded in audit trail
    - Status properly set
    - Fees calculated correctly
    """
    
    def __init__(self, transaction_id: str, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not transaction_id:
            raise ValueError("Transaction ID required")
        
        self._transaction_id = transaction_id
        self._amount = amount
        self._status = TransactionStatus.PENDING
        self._audit_trail = [f"Transaction {transaction_id} created"]
    
    @property
    def transaction_id(self) -> str:
        """Immutable transaction ID"""
        return self._transaction_id
    
    @property
    def amount(self) -> float:
        """Immutable transaction amount"""
        return self._amount
    
    @property
    def status(self) -> TransactionStatus:
        return self._status
    
    @abstractmethod
    def execute(self) -> TransactionResult:
        """
        Execute the transaction
        
        Preconditions:
        - Status must be PENDING
        
        Postconditions:
        - Status changed to COMPLETED or FAILED
        - Audit trail updated
        - Result contains all required information
        """
        pass
    
    def _update_status(self, new_status: TransactionStatus, message: str = None):
        """Protected method to update status with audit trail"""
        valid_transitions = {
            TransactionStatus.PENDING: [TransactionStatus.COMPLETED, TransactionStatus.FAILED, TransactionStatus.CANCELLED],
            TransactionStatus.COMPLETED: [],  # Terminal state
            TransactionStatus.FAILED: [TransactionStatus.PENDING],  # Can retry
            TransactionStatus.CANCELLED: []  # Terminal state
        }
        
        if new_status not in valid_transitions[self._status]:
            raise ValueError(f"Invalid status transition from {self._status} to {new_status}")
        
        old_status = self._status
        self._status = new_status
        audit_message = f"Status changed from {old_status.value} to {new_status.value}"
        if message:
            audit_message += f": {message}"
        self._audit_trail.append(audit_message)
    
    def get_audit_trail(self) -> List[str]:
        """Get complete audit trail"""
        return self._audit_trail.copy()

class BankTransfer(FinancialTransaction):
    def __init__(self, transaction_id: str, amount: float, from_account: str, to_account: str):
        super().__init__(transaction_id, amount)
        self.from_account = from_account
        self.to_account = to_account
        self._audit_trail.append(f"Bank transfer from {from_account} to {to_account}")
    
    def execute(self) -> TransactionResult:
        # Precondition check
        if self._status != TransactionStatus.PENDING:
            raise RuntimeError("Transaction must be in PENDING status")
        
        try:
            # Simulate bank transfer logic
            fee = self._amount * 0.01  # 1% fee
            
            # Simulate processing
            if self._amount > 10000:  # Large amount validation
                self._audit_trail.append("Large amount transfer - additional verification required")
            
            # Update status
            self._update_status(TransactionStatus.COMPLETED, "Bank transfer successful")
            
            # Postcondition: Return complete result
            return TransactionResult(
                status=self._status,
                transaction_id=self._transaction_id,
                amount=self._amount,
                fee=fee
            )
        
        except Exception as e:
            self._update_status(TransactionStatus.FAILED, str(e))
            return TransactionResult(
                status=self._status,
                transaction_id=self._transaction_id,
                amount=self._amount,
                error_message=str(e)
            )

class CryptocurrencyTransfer(FinancialTransaction):
    def __init__(self, transaction_id: str, amount: float, wallet_address: str, network: str):
        super().__init__(transaction_id, amount)
        self.wallet_address = wallet_address
        self.network = network
        self._audit_trail.append(f"Crypto transfer to {wallet_address} on {network}")
    
    def execute(self) -> TransactionResult:
        # Precondition check (same as parent)
        if self._status != TransactionStatus.PENDING:
            raise RuntimeError("Transaction must be in PENDING status")
        
        try:
            # Simulate crypto transfer logic
            network_fees = {
                'bitcoin': self._amount * 0.001,
                'ethereum': self._amount * 0.002,
                'litecoin': self._amount * 0.0005
            }
            fee = network_fees.get(self.network.lower(), self._amount * 0.001)
            
            # Simulate blockchain confirmation
            self._audit_trail.append(f"Broadcasting to {self.network} network")
            
            # Update status
            self._update_status(TransactionStatus.COMPLETED, "Crypto transfer confirmed")
            
            # Postcondition: Return complete result (same contract as parent)
            return TransactionResult(
                status=self._status,
                transaction_id=self._transaction_id,
                amount=self._amount,
                fee=fee
            )
        
        except Exception as e:
            self._update_status(TransactionStatus.FAILED, str(e))
            return TransactionResult(
                status=self._status,
                transaction_id=self._transaction_id,
                amount=self._amount,
                error_message=str(e)
            )

# ✅ Perfect LSP compliance with comprehensive contracts
def process_financial_transactions(transactions: List[FinancialTransaction]):
    """Process any type of financial transaction uniformly"""
    results = []
    
    for transaction in transactions:
        print(f"\n💰 Processing {type(transaction).__name__}")
        print(f"Transaction ID: {transaction.transaction_id}")
        print(f"Amount: ${transaction.amount}")
        
        # Execute transaction - same interface for all types
        result = transaction.execute()
        results.append(result)
        
        print(f"Status: {result.status.value}")
        if result.fee:
            print(f"Fee: ${result.fee}")
        if result.error_message:
            print(f"Error: {result.error_message}")
        
        # Show audit trail
        print("Audit Trail:")
        for entry in transaction.get_audit_trail():
            print(f"  - {entry}")
    
    return results

# Usage
transactions = [
    BankTransfer("BT001", 1000.0, "ACC123", "ACC456"),
    CryptocurrencyTransfer("CT001", 500.0, "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "bitcoin"),
    BankTransfer("BT002", 15000.0, "ACC789", "ACC012")  # Large amount
]

results = process_financial_transactions(transactions)
```

---

## Best Practices

### 1. Design by Contract

```python
def validate_lsp_compliance(base_class, derived_class):
    """
    Checklist for LSP compliance validation
    """
    checklist = {
        "preconditions": "Subclass doesn't strengthen preconditions",
        "postconditions": "Subclass doesn't weaken postconditions", 
        "invariants": "Subclass preserves class invariants",
        "exceptions": "Subclass doesn't throw unexpected exceptions",
        "side_effects": "Subclass doesn't introduce harmful side effects",
        "performance": "Subclass performance is reasonable",
        "semantics": "Subclass behavior matches semantic expectations"
    }
    return checklist
```

### 2. Use Abstract Base Classes Effectively

```python
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Repository(ABC, Generic[T]):
    """Generic repository pattern with LSP compliance"""
    
    @abstractmethod
    def save(self, entity: T) -> T:
        """Save entity and return saved version"""
        pass
    
    @abstractmethod
    def find_by_id(self, entity_id: str) -> T:
        """Find entity by ID, raise NotFound if not exists"""
        pass
    
    @abstractmethod
    def delete(self, entity_id: str) -> bool:
        """Delete entity, return True if deleted"""
        pass
    
    def exists(self, entity_id: str) -> bool:
        """Check if entity exists (default implementation)"""
        try:
            self.find_by_id(entity_id)
            return True
        except NotFoundError:
            return False

class NotFoundError(Exception):
    pass

class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name

class DatabaseUserRepository(Repository[User]):
    def __init__(self):
        self._users = {}
    
    def save(self, user: User) -> User:
        self._users[user.user_id] = user
        return user
    
    def find_by_id(self, user_id: str) -> User:
        if user_id not in self._users:
            raise NotFoundError(f"User {user_id} not found")
        return self._users[user_id]
    
    def delete(self, user_id: str) -> bool:
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

class CacheUserRepository(Repository[User]):
    def __init__(self, cache_ttl: int = 300):
        self._cache = {}
        self._cache_ttl = cache_ttl
    
    def save(self, user: User) -> User:
        # Same contract as parent
        self._cache[user.user_id] = user
        return user
    
    def find_by_id(self, user_id: str) -> User:
        # Same contract as parent
        if user_id not in self._cache:
            raise NotFoundError(f"User {user_id} not found in cache")
        return self._cache[user_id]
    
    def delete(self, user_id: str) -> bool:
        # Same contract as parent
        if user_id in self._cache:
            del self._cache[user_id]
            return True
        return False
```

### 3. Favor Composition Over Inheritance When LSP is Hard

```python
# When LSP is difficult to maintain, use composition
class FileStorage:
    def store(self, filename: str, content: bytes) -> str:
        # Store file and return path
        pass

class CloudStorage:
    def upload(self, key: str, data: bytes) -> str:
        # Upload to cloud and return URL
        pass

# Instead of forcing inheritance, use composition
class StorageAdapter:
    def __init__(self, storage_impl):
        self._storage = storage_impl
    
    def store(self, name: str, content: bytes) -> str:
        if hasattr(self._storage, 'store'):
            return self._storage.store(name, content)
        elif hasattr(self._storage, 'upload'):
            return self._storage.upload(name, content)
        else:
            raise NotImplementedError("Storage implementation not supported")
```

---

## Common Pitfalls

### 1. The Rectangle-Square Problem

```python
# ❌ Classic LSP violation
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def area(self):
        return self._width * self._height

class Square(Rectangle):  # Violates LSP!
    def set_width(self, width):
        self._width = width
        self._height = width  # Breaks client expectations
    
    def set_height(self, height):
        self._width = height
        self._height = height  # Breaks client expectations

# ✅ Better approach using immutable objects
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        return self._width
    
    @property
    def height(self) -> float:
        return self._height
    
    def area(self) -> float:
        return self._width * self._height
    
    def resize(self, width: float, height: float) -> 'Rectangle':
        return Rectangle(width, height)

class Square(Shape):
    def __init__(self, side: float):
        self._side = side
    
    @property
    def side(self) -> float:
        return self._side
    
    def area(self) -> float:
        return self._side ** 2
    
    def resize(self, side: float) -> 'Square':
        return Square(side)
```

### 2. Throwing Unexpected Exceptions

```python
# ❌ BAD: Subclass throws exceptions parent doesn't
class FileReader:
    def read_file(self, filename: str) -> str:
        try:
            with open(filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ""  # Returns empty string on error

class StrictFileReader(FileReader):
    def read_file(self, filename: str) -> str:
        # This violates LSP by throwing unexpected exceptions
        if not filename.endswith('.txt'):
            raise ValueError("Only .txt files allowed")  # ❌ Unexpected exception
        return super().read_file(filename)

# ✅ GOOD: Consistent exception handling
class FileReader:
    def read_file(self, filename: str) -> str:
        """Read file content. May raise FileNotFoundError or PermissionError."""
        with open(filename, 'r') as f:
            return f.read()

class CachedFileReader(FileReader):
    def __init__(self):
        self._cache = {}
    
    def read_file(self, filename: str) -> str:
        # Same exceptions as parent, just adds caching
        if filename in self._cache:
            return self._cache[filename]
        
        content = super().read_file(filename)  # May raise same exceptions
        self._cache[filename] = content
        return content
```

### 3. Performance Degradation

```python
# ❌ BAD: Subclass has significantly worse performance
class DataProcessor:
    def process(self, data: List[int]) -> List[int]:
        # O(n) operation
        return [x * 2 for x in data]

class SlowDataProcessor(DataProcessor):
    def process(self, data: List[int]) -> List[int]:
        # O(n²) operation - violates performance expectations
        result = []
        for i, x in enumerate(data):
            # Unnecessary nested loop
            for j in range(len(data)):
                if i == j:
                    result.append(x * 2)
        return result

# ✅ GOOD: Maintain reasonable performance characteristics
class OptimizedDataProcessor(DataProcessor):
    def process(self, data: List[int]) -> List[int]:
        # Still O(n), just optimized implementation
        import numpy as np
        return (np.array(data) * 2).tolist()
```

---

## Real-World Applications

### 1. Web Framework Request Handlers

```python
from abc import ABC, abstractmethod
from typing import Dict, Any

class HttpRequest:
    def __init__(self, method: str, path: str, headers: Dict[str, str], body: str = ""):
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body

class HttpResponse:
    def __init__(self, status_code: int, body: str, headers: Dict[str, str] = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers or {}

class RequestHandler(ABC):
    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse:
        """Handle HTTP request and return response"""
        pass

class JsonApiHandler(RequestHandler):
    def handle(self, request: HttpRequest) -> HttpResponse:
        # Always returns JSON response
        return HttpResponse(
            status_code=200,
            body='{"message": "JSON API response"}',
            headers={"Content-Type": "application/json"}
        )

class HtmlHandler(RequestHandler):
    def handle(self, request: HttpRequest) -> HttpResponse:
        # Always returns HTML response
        return HttpResponse(
            status_code=200,
            body='<html><body>HTML response</body></html>',
            headers={"Content-Type": "text/html"}
        )

class FileDownloadHandler(RequestHandler):
    def handle(self, request: HttpRequest) -> HttpResponse:
        # Returns file download response
        return HttpResponse(
            status_code=200,
            body="file content here",
            headers={
                "Content-Type": "application/octet-stream",
                "Content-Disposition": "attachment; filename=file.txt"
            }
        )

# ✅ All handlers are perfectly substitutable
def process_request(handler: RequestHandler, request: HttpRequest) -> HttpResponse:
    return handler.handle(request)
```

### 2. Database ORM with Different Backends

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class Model:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class QuerySet(ABC):
    @abstractmethod
    def filter(self, **kwargs) -> 'QuerySet':
        pass
    
    @abstractmethod
    def all(self) -> List[Model]:
        pass
    
    @abstractmethod
    def first(self) -> Optional[Model]:
        pass
    
    @abstractmethod
    def count(self) -> int:
        pass

class SQLQuerySet(QuerySet):
    def __init__(self, model_class, connection):
        self.model_class = model_class
        self.connection = connection
        self._filters = {}
    
    def filter(self, **kwargs) -> 'SQLQuerySet':
        new_qs = SQLQuerySet(self.model_class, self.connection)
        new_qs._filters = {**self._filters, **kwargs}
        return new_qs
    
    def all(self) -> List[Model]:
        # Generate SQL query from filters
        sql = f"SELECT * FROM {self.model_class.__name__.lower()}"
        if self._filters:
            conditions = [f"{k} = '{v}'" for k, v in self._filters.items()]
            sql += f" WHERE {' AND '.join(conditions)}"
        
        # Simulate database query
        return [Model(id=1, name="Test")]
    
    def first(self) -> Optional[Model]:
        results = self.all()
        return results[0] if results else None
    
    def count(self) -> int:
        return len(self.all())

class MongoQuerySet(QuerySet):
    def __init__(self, model_class, collection):
        self.model_class = model_class
        self.collection = collection
        self._filters = {}
    
    def filter(self, **kwargs) -> 'MongoQuerySet':
        new_qs = MongoQuerySet(self.model_class, self.collection)
        new_qs._filters = {**self._filters, **kwargs}
        return new_qs
    
    def all(self) -> List[Model]:
        # Generate MongoDB query from filters
        query = self._filters
        
        # Simulate MongoDB query
        return [Model(id=1, name="Test")]
    
    def first(self) -> Optional[Model]:
        results = self.all()
        return results[0] if results else None
    
    def count(self) -> int:
        return len(self.all())

# ✅ Perfect LSP compliance - same interface for different databases
def search_users(queryset: QuerySet, name: str) -> List[Model]:
    return queryset.filter(name=name).all()
```

---

## Testing LSP Compliance

### 1. Automated LSP Testing

```python
import unittest
from abc import ABC, abstractmethod
from typing import Type, Any, List

class LSPTestCase(unittest.TestCase):
    """Base class for testing LSP compliance"""
    
    def setUp(self):
        self.base_class = None
        self.derived_classes = []
    
    def test_interface_compatibility(self):
        """Test that all derived classes implement the same interface"""
        if not self.base_class or not self.derived_classes:
            self.skipTest("Base class and derived classes not set")
        
        base_methods = set(dir(self.base_class))
        
        for derived_class in self.derived_classes:
            derived_methods = set(dir(derived_class))
            missing_methods = base_methods - derived_methods
            
            # Filter out private methods and properties
            missing_public_methods = [
                method for method in missing_methods 
                if not method.startswith('_') and callable(getattr(self.base_class, method, None))
            ]
            
            self.assertEqual(
                len(missing_public_methods), 0,
                f"{derived_class.__name__} missing methods: {missing_public_methods}"
            )
    
    def test_method_signatures(self):
        """Test that method signatures are compatible"""
        import inspect
        
        if not self.base_class or not self.derived_classes:
            self.skipTest("Base class and derived classes not set")
        
        base_methods = inspect.getmembers(self.base_class, predicate=inspect.isfunction)
        
        for derived_class in self.derived_classes:
            for method_name, base_method in base_methods:
                if hasattr(derived_class, method_name):
                    derived_method = getattr(derived_class, method_name)
                    
                    base_sig = inspect.signature(base_method)
                    derived_sig = inspect.signature(derived_method)
                    
                    # Check parameter compatibility (simplified check)
                    self.assertEqual(
                        len(base_sig.parameters), len(derived_sig.parameters),
                        f"Parameter count mismatch in {derived_class.__name__}.{method_name}"
                    )

class ShapeTestCase(LSPTestCase):
    def setUp(self):
        super().setUp()
        
        class Shape(ABC):
            @abstractmethod
            def area(self) -> float:
                pass
            
            @abstractmethod
            def perimeter(self) -> float:
                pass
        
        class Rectangle(Shape):
            def __init__(self, width: float, height: float):
                self.width = width
                self.height = height
            
            def area(self) -> float:
                return self.width * self.height
            
            def perimeter(self) -> float:
                return 2 * (self.width + self.height)
        
        class Circle(Shape):
            def __init__(self, radius: float):
                self.radius = radius
            
            def area(self) -> float:
                import math
                return math.pi * self.radius ** 2
            
            def perimeter(self) -> float:
                import math
                return 2 * math.pi * self.radius
        
        self.base_class = Shape
        self.derived_classes = [Rectangle, Circle]
    
    def test_behavioral_compatibility(self):
        """Test that all shapes behave consistently"""
        rectangle = self.derived_classes[0](5, 4)  # Rectangle
        circle = self.derived_classes[1](3)        # Circle
        
        # All shapes should return positive area and perimeter
        self.assertGreater(rectangle.area(), 0)
        self.assertGreater(rectangle.perimeter(), 0)
        self.assertGreater(circle.area(), 0)
        self.assertGreater(circle.perimeter(), 0)
        
        # Area and perimeter should be numbers
        self.assertIsInstance(rectangle.area(), (int, float))
        self.assertIsInstance(rectangle.perimeter(), (int, float))
        self.assertIsInstance(circle.area(), (int, float))
        self.assertIsInstance(circle.perimeter(), (int, float))

# Run the tests
if __name__ == '__main__':
    unittest.main()
```

### 2. Property-Based Testing for LSP

```python
from hypothesis import given, strategies as st
import unittest

class PropertyBasedLSPTest(unittest.TestCase):
    """Property-based testing for LSP compliance"""
    
    @given(st.floats(min_value=0.1, max_value=1000))
    def test_shape_area_properties(self, size):
        """Test that all shapes satisfy area properties"""
        from math import pi
        
        # Rectangle with equal sides
        rectangle = Rectangle(size, size)
        
        # Circle with radius that gives same area as square
        circle_radius = (size ** 2 / pi) ** 0.5
        circle = Circle(circle_radius)
        
        # Both should have positive area
        self.assertGreater(rectangle.area(), 0)
        self.assertGreater(circle.area(), 0)
        
        # Area should scale with size
        larger_rectangle = Rectangle(size * 2, size * 2)
        self.assertGreater(larger_rectangle.area(), rectangle.area())
    
    @given(st.lists(st.integers(min_value=1, max_value=100), min_size=1, max_size=1000))
    def test_data_processor_properties(self, data):
        """Test that all data processors maintain properties"""
        processors = [DataProcessor(), OptimizedDataProcessor()]
        
        for processor in processors:
            result = processor.process(data)
            
            # Output should have same length as input
            self.assertEqual(len(result), len(data))
            
            # Each element should be doubled
            for original, processed in zip(data, result):
                self.assertEqual(processed, original * 2)
```

---

## Summary

### Key Takeaways

1. **LSP is about behavioral compatibility**, not just interface compatibility
2. **Subclasses must honor the contract** established by their parent class
3. **Preconditions cannot be strengthened** in subclasses
4. **Postconditions cannot be weakened** in subclasses
5. **Invariants must be preserved** across the inheritance hierarchy
6. **Use composition when inheritance violates LSP**

### Quick Checklist for LSP Compliance

- [ ] Can I substitute any subclass for the parent class without breaking functionality?
- [ ] Do all subclasses honor the same preconditions?
- [ ] Do all subclasses guarantee the same postconditions?
- [ ] Are class invariants preserved in all subclasses?
- [ ] Do subclasses throw only expected exceptions?
- [ ] Is performance reasonably consistent across subclasses?
- [ ] Do subclasses maintain semantic consistency?

### When to Use LSP

✅ **Use inheritance with LSP when:**
- You have a clear "is-a" relationship
- Subclasses truly behave like their parent
- You need polymorphic behavior
- The contract is well-defined and stable

❌ **Avoid inheritance when:**
- LSP would be violated
- You only need code reuse (use composition)
- The relationship is "has-a" rather than "is-a"
- The contract is unclear or frequently changing

### Final Thoughts

The Liskov Substitution Principle is fundamental to creating robust, maintainable object-oriented systems. It ensures that inheritance hierarchies are logically sound and that polymorphism works as expected. By following LSP, you create code that is:

- **Predictable**: Clients can rely on consistent behavior
- **Extensible**: New subclasses can be added safely
- **Testable**: Base class tests validate all subclasses
- **Maintainable**: Changes don't break existing functionality

Remember: **Inheritance should model behavior, not just structure**. If a subclass can't fully substitute for its parent, consider using composition or redesigning your hierarchy.

---

*This tutorial covered the Liskov Substitution Principle from basic concepts to expert-level applications. Practice with the examples and apply these principles in your own code to build better object-oriented systems.*