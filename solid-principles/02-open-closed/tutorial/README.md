# Open/Closed Principle (OCP) Tutorial 🚀

## Table of Contents
1. [Introduction](#introduction)
2. [What is the Open/Closed Principle?](#what-is-the-openclosed-principle)
3. [Understanding "Open for Extension, Closed for Modification"](#understanding-open-for-extension-closed-for-modification)
4. [Why OCP Matters](#why-ocp-matters)
5. [Common Violations and Code Smells](#common-violations-and-code-smells)
6. [Basic Examples](#basic-examples)
7. [Intermediate Examples](#intermediate-examples)
8. [Advanced Examples](#advanced-examples)
9. [Design Patterns Supporting OCP](#design-patterns-supporting-ocp)
10. [Real-World Applications](#real-world-applications)
11. [Best Practices](#best-practices)
12. [Common Pitfalls](#common-pitfalls)
13. [Exercises](#exercises)
14. [Summary](#summary)

---

## Introduction

Welcome to the comprehensive tutorial on the **Open/Closed Principle (OCP)** - the second principle in the SOLID design principles. This principle is fundamental to creating flexible, maintainable, and extensible software systems. Whether you're building simple applications or complex enterprise systems, understanding OCP will dramatically improve your code's adaptability to changing requirements.

### What You'll Learn
- 🎯 **Core Concept**: What "open for extension, closed for modification" really means
- 🔍 **Identification**: How to spot OCP violations and opportunities
- 🛠️ **Implementation**: Multiple techniques to achieve OCP compliance
- 💡 **Design Patterns**: Strategy, Template Method, Factory, and more
- 🚀 **Real Examples**: From simple shapes to complex business systems

### Prerequisites
- Understanding of classes, inheritance, and polymorphism
- Familiarity with the Single Responsibility Principle (SRP)
- Basic knowledge of interfaces/abstract classes
- Python syntax and object-oriented concepts

---

## What is the Open/Closed Principle?

> **"Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification."** - Bertrand Meyer

The Open/Closed Principle states that you should be able to **add new functionality** to your code without **changing existing code**. This means:

- **Open for Extension**: You can add new features and behaviors
- **Closed for Modification**: You don't modify existing, working code

### Simple Analogy 🔌
Think of OCP like a **power outlet system**:
- **The outlet (interface)** stays the same - it's "closed for modification"
- **Different devices (implementations)** can plug in - it's "open for extension"
- You can add new devices without rewiring your house
- Each device works differently but uses the same interface

### Technical Definition
A system follows OCP when:
1. **New features** can be added through new classes/modules
2. **Existing code** remains unchanged when adding functionality
3. **Abstractions** (interfaces/base classes) define contracts
4. **Concrete implementations** extend these abstractions

---

## Understanding "Open for Extension, Closed for Modification"

### What Does "Open for Extension" Mean?

**Open for Extension** means you can add new functionality by:
- Creating new classes that implement existing interfaces
- Inheriting from base classes and overriding methods
- Adding new modules that follow established contracts
- Extending behavior without touching existing code

```python
# Base abstraction - defines the contract
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError

# Extension 1 - adds credit card functionality
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

# Extension 2 - adds PayPal functionality (no existing code changed!)
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"
```

### What Does "Closed for Modification" Mean?

**Closed for Modification** means:
- You don't change existing, tested, working code
- Existing classes and methods remain untouched
- No risk of breaking existing functionality
- Stable interfaces that other code depends on

```python
# ❌ Violating OCP - modifying existing code for new features
class PaymentProcessor:
    def process_payment(self, amount, payment_type):
        if payment_type == "credit_card":
            return f"Processing ${amount} via Credit Card"
        elif payment_type == "paypal":
            return f"Processing ${amount} via PayPal"
        elif payment_type == "bitcoin":  # ← Modification required!
            return f"Processing ${amount} via Bitcoin"
        # Every new payment method requires modifying this class!
```

### The Balance: Extension vs Modification

The key insight is achieving the right balance:

| Aspect | Open for Extension | Closed for Modification |
|--------|-------------------|------------------------|
| **Purpose** | Add new features | Protect existing code |
| **Mechanism** | Inheritance, Composition | Abstraction, Interfaces |
| **Benefits** | Flexibility, Growth | Stability, Reliability |
| **Risk** | Complexity | Rigidity |

---

## Why OCP Matters

### Benefits of Following OCP

#### 1. **Reduced Risk** 🛡️
```python
# ❌ High Risk - Modifying existing code
class ReportGenerator:
    def generate_report(self, data, format_type):
        if format_type == "pdf":
            # PDF generation logic
            pass
        elif format_type == "excel":
            # Excel generation logic
            pass
        # Adding CSV requires modifying this tested code!

# ✅ Low Risk - Extending through new classes
class ReportGenerator:
    def __init__(self, formatter):
        self.formatter = formatter
    
    def generate_report(self, data):
        return self.formatter.format(data)

class PDFFormatter:
    def format(self, data): pass

class ExcelFormatter:
    def format(self, data): pass

# New CSV formatter - no existing code touched!
class CSVFormatter:
    def format(self, data): pass
```

#### 2. **Easier Testing** 🧪
- **Isolated Testing**: New features don't affect existing tests
- **Focused Tests**: Each extension has its own test suite
- **Regression Prevention**: Existing functionality remains stable

#### 3. **Faster Development** ⚡
- **Parallel Development**: Teams can work on different extensions
- **No Integration Conflicts**: New features don't interfere with existing code
- **Reduced Debugging**: Less chance of breaking working functionality

#### 4. **Better Maintainability** 🔧
- **Clear Separation**: Each feature has its own implementation
- **Easier Updates**: Modify specific behaviors without affecting others
- **Simplified Debugging**: Issues are isolated to specific implementations

#### 5. **Enhanced Flexibility** 🤸
- **Runtime Configuration**: Switch implementations dynamically
- **Plugin Architecture**: Add features without recompiling
- **A/B Testing**: Easy to test different implementations

### Real-World Impact

#### Before OCP (Problems)
```python
class NotificationService:
    def send_notification(self, message, type):
        if type == "email":
            # Email sending logic
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            # ... complex email setup
            print(f"Email sent: {message}")
        elif type == "sms":
            # SMS sending logic
            # ... SMS API integration
            print(f"SMS sent: {message}")
        elif type == "push":
            # Push notification logic
            # ... push notification setup
            print(f"Push notification sent: {message}")
        # Adding Slack notifications requires modifying this class!
```

**Problems:**
- 🚫 **Every new notification type** requires modifying existing code
- 🚫 **Risk of breaking** existing notification methods
- 🚫 **Testing complexity** increases with each addition
- 🚫 **Team conflicts** when multiple developers modify the same file
- 🚫 **Deployment risk** - changes affect all notification types

#### After OCP (Solutions)
```python
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(NotificationSender):
    def send(self, message):
        # Email-specific implementation
        print(f"Email sent: {message}")

class SMSSender(NotificationSender):
    def send(self, message):
        # SMS-specific implementation
        print(f"SMS sent: {message}")

class PushSender(NotificationSender):
    def send(self, message):
        # Push notification implementation
        print(f"Push notification sent: {message}")

class NotificationService:
    def __init__(self):
        self.senders = []
    
    def add_sender(self, sender: NotificationSender):
        self.senders.append(sender)
    
    def send_notification(self, message):
        for sender in self.senders:
            sender.send(message)

# Adding Slack notifications - no existing code modified!
class SlackSender(NotificationSender):
    def send(self, message):
        print(f"Slack message sent: {message}")
```

**Benefits:**
- ✅ **New notification types** added without touching existing code
- ✅ **Zero risk** to existing notification methods
- ✅ **Independent testing** for each notification type
- ✅ **Parallel development** - teams work on separate classes
- ✅ **Safe deployment** - new features don't affect existing ones

---

## Common Violations and Code Smells

### How to Identify OCP Violations

#### 🚨 Warning Signs

1. **Conditional Statements** for type checking
2. **Switch/Case Statements** that grow over time
3. **Frequent Modifications** to the same class for new features
4. **Large Classes** with multiple responsibilities
5. **Hard-coded Dependencies** on specific implementations

#### 🔍 Code Smell Examples

##### 1. **The Growing If-Else Chain**
```python
# ❌ Violates OCP - grows with every new shape
class AreaCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14159 * shape.radius ** 2
        elif shape.type == "triangle":
            return 0.5 * shape.base * shape.height
        elif shape.type == "pentagon":  # ← Another modification!
            # Pentagon area calculation
            pass
        # Every new shape requires modifying this method!
```

##### 2. **Type-Based Processing**
```python
# ❌ Violates OCP - processing logic mixed with type checking
class DocumentProcessor:
    def process_document(self, document):
        if isinstance(document, PDFDocument):
            # PDF-specific processing
            self.extract_pdf_text(document)
            self.validate_pdf_structure(document)
        elif isinstance(document, WordDocument):
            # Word-specific processing
            self.extract_word_text(document)
            self.check_word_formatting(document)
        elif isinstance(document, ExcelDocument):  # ← Modification needed!
            # Excel-specific processing
            pass
        # Adding new document types requires changing this method!
```

##### 3. **Factory with Hard-coded Types**
```python
# ❌ Violates OCP - factory needs modification for new types
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "truck":
            return Truck()
        elif vehicle_type == "bicycle":  # ← Factory modification required!
            return Bicycle()
        # Every new vehicle type requires modifying this factory!
```

### Refactoring Strategies

#### Strategy 1: **Extract Polymorphic Hierarchy**
```python
# ✅ OCP Compliant - polymorphic shape hierarchy
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()

# Adding new shapes - no existing code modified!
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
```

#### Strategy 2: **Use Strategy Pattern**
```python
# ✅ OCP Compliant - strategy pattern for document processing
class DocumentProcessor(ABC):
    @abstractmethod
    def process(self, document):
        pass

class PDFProcessor(DocumentProcessor):
    def process(self, document):
        # PDF-specific processing
        pass

class WordProcessor(DocumentProcessor):
    def process(self, document):
        # Word-specific processing
        pass

class DocumentService:
    def __init__(self, processor: DocumentProcessor):
        self.processor = processor
    
    def process_document(self, document):
        return self.processor.process(document)

# Adding Excel processing - no existing code modified!
class ExcelProcessor(DocumentProcessor):
    def process(self, document):
        # Excel-specific processing
        pass
```

#### Strategy 3: **Plugin-Based Architecture**
```python
# ✅ OCP Compliant - registry-based factory
class VehicleRegistry:
    _vehicles = {}
    
    @classmethod
    def register(cls, vehicle_type, vehicle_class):
        cls._vehicles[vehicle_type] = vehicle_class
    
    @classmethod
    def create_vehicle(cls, vehicle_type):
        vehicle_class = cls._vehicles.get(vehicle_type)
        if vehicle_class:
            return vehicle_class()
        raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# Register existing vehicles
VehicleRegistry.register("car", Car)
VehicleRegistry.register("motorcycle", Motorcycle)

# Adding new vehicles - no factory modification needed!
VehicleRegistry.register("bicycle", Bicycle)
VehicleRegistry.register("scooter", Scooter)
```

---

## Basic Examples

### Example 1: Shape Area Calculator

#### ❌ **Before: OCP Violation**
```python
class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        self.properties = kwargs

class AreaCalculator:
    def calculate_area(self, shape):
        if shape.shape_type == "rectangle":
            return shape.properties["width"] * shape.properties["height"]
        elif shape.shape_type == "circle":
            return 3.14159 * shape.properties["radius"] ** 2
        elif shape.shape_type == "triangle":
            return 0.5 * shape.properties["base"] * shape.properties["height"]
        else:
            raise ValueError(f"Unknown shape type: {shape.shape_type}")

# Usage
rectangle = Shape("rectangle", width=5, height=3)
circle = Shape("circle", radius=4)
calculator = AreaCalculator()
print(calculator.calculate_area(rectangle))  # 15
print(calculator.calculate_area(circle))     # 50.26544
```

**Problems:**
- Adding new shapes requires modifying `AreaCalculator`
- Risk of breaking existing functionality
- Violates Single Responsibility Principle too
- Hard to test individual shape calculations

#### ✅ **After: Following OCP**
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class defining the shape contract"""
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    """Rectangle implementation - closed for modification"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    """Circle implementation - closed for modification"""
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    """Triangle implementation - closed for modification"""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:
    """Calculator that works with any shape - closed for modification"""
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()
    
    def calculate_total_area(self, shapes):
        return sum(shape.calculate_area() for shape in shapes)

# Adding new shapes - open for extension!
class Pentagon(Shape):
    """New shape added without modifying existing code"""
    def __init__(self, side_length):
        self.side_length = side_length
    
    def calculate_area(self):
        # Pentagon area formula
        return (1/4) * math.sqrt(25 + 10*math.sqrt(5)) * self.side_length ** 2

class Ellipse(Shape):
    """Another new shape - no existing code touched"""
    def __init__(self, semi_major, semi_minor):
        self.semi_major = semi_major
        self.semi_minor = semi_minor
    
    def calculate_area(self):
        return math.pi * self.semi_major * self.semi_minor

# Usage - works with all shapes without modification
calculator = AreaCalculator()
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 8),
    Pentagon(5),
    Ellipse(3, 2)
]

for shape in shapes:
    area = calculator.calculate_area(shape)
    print(f"{shape.__class__.__name__}: {area:.2f}")

total_area = calculator.calculate_total_area(shapes)
print(f"Total area: {total_area:.2f}")
```

**Benefits:**
- ✅ New shapes added without modifying existing code
- ✅ Each shape is responsible for its own area calculation
- ✅ Easy to test each shape independently
- ✅ Calculator works with any shape that follows the contract
- ✅ No risk of breaking existing shapes when adding new ones

### Example 2: Discount System

#### ❌ **Before: OCP Violation**
```python
class DiscountCalculator:
    def apply_discount(self, price, customer_type, **kwargs):
        if customer_type == "regular":
            return price  # No discount
        elif customer_type == "premium":
            return price * 0.9  # 10% discount
        elif customer_type == "vip":
            return price * 0.8  # 20% discount
        elif customer_type == "student":
            # Student discount with ID verification
            if kwargs.get("student_id"):
                return price * 0.85  # 15% discount
            return price
        elif customer_type == "senior":
            # Senior discount with age verification
            if kwargs.get("age", 0) >= 65:
                return price * 0.75  # 25% discount
            return price
        else:
            return price

# Usage
calculator = DiscountCalculator()
print(calculator.apply_discount(100, "premium"))  # 90.0
print(calculator.apply_discount(100, "student", student_id="12345"))  # 85.0
```

**Problems:**
- Every new customer type requires modifying the main method
- Complex conditional logic becomes hard to maintain
- Different discount rules mixed in one place
- Hard to test individual discount types

#### ✅ **After: Following OCP**
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """Abstract discount strategy - defines the contract"""
    @abstractmethod
    def apply_discount(self, price):
        pass
    
    @abstractmethod
    def is_applicable(self, customer):
        pass

class RegularCustomerDiscount(DiscountStrategy):
    """No discount for regular customers"""
    def apply_discount(self, price):
        return price
    
    def is_applicable(self, customer):
        return customer.type == "regular"

class PremiumCustomerDiscount(DiscountStrategy):
    """10% discount for premium customers"""
    def apply_discount(self, price):
        return price * 0.9
    
    def is_applicable(self, customer):
        return customer.type == "premium"

class VIPCustomerDiscount(DiscountStrategy):
    """20% discount for VIP customers"""
    def apply_discount(self, price):
        return price * 0.8
    
    def is_applicable(self, customer):
        return customer.type == "vip"

class StudentDiscount(DiscountStrategy):
    """15% discount for students with valid ID"""
    def apply_discount(self, price):
        return price * 0.85
    
    def is_applicable(self, customer):
        return (customer.type == "student" and 
                hasattr(customer, "student_id") and 
                customer.student_id)

class SeniorDiscount(DiscountStrategy):
    """25% discount for seniors (65+)"""
    def apply_discount(self, price):
        return price * 0.75
    
    def is_applicable(self, customer):
        return (customer.type == "senior" and 
                hasattr(customer, "age") and 
                customer.age >= 65)

class Customer:
    """Customer data model"""
    def __init__(self, customer_type, **kwargs):
        self.type = customer_type
        for key, value in kwargs.items():
            setattr(self, key, value)

class DiscountCalculator:
    """Calculator that uses strategy pattern - closed for modification"""
    def __init__(self):
        self.strategies = [
            RegularCustomerDiscount(),
            PremiumCustomerDiscount(),
            VIPCustomerDiscount(),
            StudentDiscount(),
            SeniorDiscount()
        ]
    
    def add_strategy(self, strategy: DiscountStrategy):
        """Allow adding new discount strategies"""
        self.strategies.append(strategy)
    
    def apply_discount(self, price, customer):
        for strategy in self.strategies:
            if strategy.is_applicable(customer):
                return strategy.apply_discount(price)
        return price  # No applicable discount

# Adding new discount types - open for extension!
class EmployeeDiscount(DiscountStrategy):
    """30% discount for employees"""
    def apply_discount(self, price):
        return price * 0.7
    
    def is_applicable(self, customer):
        return (customer.type == "employee" and 
                hasattr(customer, "employee_id") and 
                customer.employee_id)

class BulkOrderDiscount(DiscountStrategy):
    """5% discount for orders over $500"""
    def apply_discount(self, price):
        return price * 0.95
    
    def is_applicable(self, customer):
        return hasattr(customer, "order_total") and customer.order_total > 500

# Usage
calculator = DiscountCalculator()

# Add new discount strategies without modifying existing code
calculator.add_strategy(EmployeeDiscount())
calculator.add_strategy(BulkOrderDiscount())

# Test different customers
customers = [
    Customer("regular"),
    Customer("premium"),
    Customer("student", student_id="12345"),
    Customer("senior", age=70),
    Customer("employee", employee_id="EMP001"),
    Customer("regular", order_total=600)  # Bulk order
]

price = 100
for customer in customers:
    discounted_price = calculator.apply_discount(price, customer)
    print(f"{customer.type}: ${price} → ${discounted_price}")
```

**Benefits:**
- ✅ New discount types added without modifying existing code
- ✅ Each discount strategy is isolated and testable
- ✅ Complex discount rules are encapsulated in their own classes
- ✅ Easy to combine multiple discounts or change discount logic
- ✅ Calculator remains stable while being extensible

---

## Intermediate Examples

### Example 3: Data Export System

#### ❌ **Before: OCP Violation**
```python
import json
import csv
import xml.etree.ElementTree as ET

class DataExporter:
    def export_data(self, data, format_type, filename):
        if format_type == "json":
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        elif format_type == "csv":
            if isinstance(data, list) and data:
                with open(filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
        elif format_type == "xml":
            root = ET.Element("data")
            for item in data:
                item_elem = ET.SubElement(root, "item")
                for key, value in item.items():
                    child = ET.SubElement(item_elem, key)
                    child.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(filename)
        elif format_type == "yaml":  # ← Requires modification!
            import yaml
            with open(filename, 'w') as f:
                yaml.dump(data, f)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
```

**Problems:**
- Every new format requires modifying the main class
- Mixed responsibilities (JSON, CSV, XML logic in one place)
- Hard to test individual export formats
- Risk of breaking existing formats when adding new ones

#### ✅ **After: Following OCP**
```python
from abc import ABC, abstractmethod
import json
import csv
import xml.etree.ElementTree as ET

class DataExporter(ABC):
    """Abstract base class for data exporters"""
    @abstractmethod
    def export(self, data, filename):
        pass
    
    @abstractmethod
    def get_file_extension(self):
        pass

class JSONExporter(DataExporter):
    """JSON export implementation"""
    def export(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_file_extension(self):
        return ".json"

class CSVExporter(DataExporter):
    """CSV export implementation"""
    def export(self, data, filename):
        if not isinstance(data, list) or not data:
            raise ValueError("CSV export requires a list of dictionaries")
        
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    def get_file_extension(self):
        return ".csv"

class XMLExporter(DataExporter):
    """XML export implementation"""
    def export(self, data, filename):
        root = ET.Element("data")
        for item in data:
            item_elem = ET.SubElement(root, "item")
            for key, value in item.items():
                child = ET.SubElement(item_elem, key)
                child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
    
    def get_file_extension(self):
        return ".xml"

class ExportManager:
    """Manager that coordinates exports - closed for modification"""
    def __init__(self):
        self.exporters = {}
    
    def register_exporter(self, format_name, exporter: DataExporter):
        """Register a new exporter"""
        self.exporters[format_name] = exporter
    
    def export_data(self, data, format_name, base_filename):
        if format_name not in self.exporters:
            raise ValueError(f"Unsupported format: {format_name}")
        
        exporter = self.exporters[format_name]
        filename = base_filename + exporter.get_file_extension()
        exporter.export(data, filename)
        return filename

# Adding new formats - open for extension!
class YAMLExporter(DataExporter):
    """YAML export implementation - no existing code modified"""
    def export(self, data, filename):
        import yaml
        with open(filename, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
    
    def get_file_extension(self):
        return ".yaml"

class ExcelExporter(DataExporter):
    """Excel export implementation - no existing code modified"""
    def export(self, data, filename):
        try:
            import pandas as pd
            df = pd.DataFrame(data)
            df.to_excel(filename, index=False)
        except ImportError:
            raise ImportError("pandas and openpyxl required for Excel export")
    
    def get_file_extension(self):
        return ".xlsx"

class HTMLExporter(DataExporter):
    """HTML table export implementation"""
    def export(self, data, filename):
        html_content = "<html><body><table border='1'>\n"
        
        if data:
            # Header
            html_content += "<tr>"
            for key in data[0].keys():
                html_content += f"<th>{key}</th>"
            html_content += "</tr>\n"
            
            # Data rows
            for item in data:
                html_content += "<tr>"
                for value in item.values():
                    html_content += f"<td>{value}</td>"
                html_content += "</tr>\n"
        
        html_content += "</table></body></html>"
        
        with open(filename, 'w') as f:
            f.write(html_content)
    
    def get_file_extension(self):
        return ".html"

# Usage
manager = ExportManager()

# Register built-in exporters
manager.register_exporter("json", JSONExporter())
manager.register_exporter("csv", CSVExporter())
manager.register_exporter("xml", XMLExporter())

# Register new exporters without modifying existing code
manager.register_exporter("yaml", YAMLExporter())
manager.register_exporter("excel", ExcelExporter())
manager.register_exporter("html", HTMLExporter())

# Sample data
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Export to different formats
formats = ["json", "csv", "xml", "yaml", "html"]
for format_name in formats:
    try:
        filename = manager.export_data(data, format_name, "users")
        print(f"Exported to {filename}")
    except Exception as e:
        print(f"Failed to export {format_name}: {e}")
```

### Example 4: Payment Processing System

#### ❌ **Before: OCP Violation**
```python
class PaymentProcessor:
    def process_payment(self, amount, payment_method, **kwargs):
        if payment_method == "credit_card":
            card_number = kwargs.get("card_number")
            cvv = kwargs.get("cvv")
            expiry = kwargs.get("expiry")
            
            # Credit card validation
            if not self._validate_credit_card(card_number, cvv, expiry):
                return {"status": "failed", "message": "Invalid card details"}
            
            # Process credit card payment
            return {"status": "success", "transaction_id": f"cc_{card_number[-4:]}"}
        
        elif payment_method == "paypal":
            email = kwargs.get("email")
            password = kwargs.get("password")
            
            # PayPal authentication
            if not self._authenticate_paypal(email, password):
                return {"status": "failed", "message": "PayPal authentication failed"}
            
            # Process PayPal payment
            return {"status": "success", "transaction_id": f"pp_{email}"}
        
        elif payment_method == "bank_transfer":
            account_number = kwargs.get("account_number")
            routing_number = kwargs.get("routing_number")
            
            # Bank transfer validation
            if not self._validate_bank_details(account_number, routing_number):
                return {"status": "failed", "message": "Invalid bank details"}
            
            # Process bank transfer
            return {"status": "success", "transaction_id": f"bt_{account_number[-4:]}"}
        
        else:
            return {"status": "failed", "message": f"Unsupported payment method: {payment_method}"}
    
    def _validate_credit_card(self, card_number, cvv, expiry):
        # Credit card validation logic
        return len(card_number) == 16 and len(cvv) == 3
    
    def _authenticate_paypal(self, email, password):
        # PayPal authentication logic
        return "@" in email and len(password) > 6
    
    def _validate_bank_details(self, account_number, routing_number):
        # Bank validation logic
        return len(account_number) >= 8 and len(routing_number) == 9
```

#### ✅ **After: Following OCP**
```python
from abc import ABC, abstractmethod
from typing import Dict, Any

class PaymentMethod(ABC):
    """Abstract payment method"""
    @abstractmethod
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def get_method_name(self) -> str:
        pass

class CreditCardPayment(PaymentMethod):
    """Credit card payment implementation"""
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        required_fields = ["card_number", "cvv", "expiry"]
        if not all(field in payment_data for field in required_fields):
            return False
        
        card_number = payment_data["card_number"]
        cvv = payment_data["cvv"]
        
        return len(card_number) == 16 and len(cvv) == 3
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate_payment_data(payment_data):
            return {"status": "failed", "message": "Invalid card details"}
        
        card_number = payment_data["card_number"]
        # Simulate credit card processing
        return {
            "status": "success",
            "transaction_id": f"cc_{card_number[-4:]}_{amount}",
            "method": self.get_method_name()
        }
    
    def get_method_name(self) -> str:
        return "Credit Card"

class PayPalPayment(PaymentMethod):
    """PayPal payment implementation"""
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        required_fields = ["email", "password"]
        if not all(field in payment_data for field in required_fields):
            return False
        
        email = payment_data["email"]
        password = payment_data["password"]
        
        return "@" in email and len(password) > 6
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate_payment_data(payment_data):
            return {"status": "failed", "message": "PayPal authentication failed"}
        
        email = payment_data["email"]
        # Simulate PayPal processing
        return {
            "status": "success",
            "transaction_id": f"pp_{email}_{amount}",
            "method": self.get_method_name()
        }
    
    def get_method_name(self) -> str:
        return "PayPal"

class BankTransferPayment(PaymentMethod):
    """Bank transfer payment implementation"""
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        required_fields = ["account_number", "routing_number"]
        if not all(field in payment_data for field in required_fields):
            return False
        
        account_number = payment_data["account_number"]
        routing_number = payment_data["routing_number"]
        
        return len(account_number) >= 8 and len(routing_number) == 9
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate_payment_data(payment_data):
            return {"status": "failed", "message": "Invalid bank details"}
        
        account_number = payment_data["account_number"]
        # Simulate bank transfer processing
        return {
            "status": "success",
            "transaction_id": f"bt_{account_number[-4:]}_{amount}",
            "method": self.get_method_name()
        }
    
    def get_method_name(self) -> str:
        return "Bank Transfer"

class PaymentProcessor:
    """Payment processor that coordinates different payment methods"""
    def __init__(self):
        self.payment_methods = {}
    
    def register_payment_method(self, method_key: str, payment_method: PaymentMethod):
        """Register a new payment method"""
        self.payment_methods[method_key] = payment_method
    
    def process_payment(self, amount: float, method_key: str, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        if method_key not in self.payment_methods:
            return {"status": "failed", "message": f"Unsupported payment method: {method_key}"}
        
        payment_method = self.payment_methods[method_key]
        return payment_method.process_payment(amount, payment_data)
    
    def get_supported_methods(self) -> list:
        """Get list of supported payment methods"""
        return [method.get_method_name() for method in self.payment_methods.values()]

# Adding new payment methods - open for extension!
class CryptocurrencyPayment(PaymentMethod):
    """Cryptocurrency payment implementation"""
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        required_fields = ["wallet_address", "private_key"]
        if not all(field in payment_data for field in required_fields):
            return False
        
        wallet_address = payment_data["wallet_address"]
        return len(wallet_address) >= 26  # Basic Bitcoin address validation
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate_payment_data(payment_data):
            return {"status": "failed", "message": "Invalid cryptocurrency details"}
        
        wallet_address = payment_data["wallet_address"]
        # Simulate cryptocurrency processing
        return {
            "status": "success",
            "transaction_id": f"crypto_{wallet_address[-6:]}_{amount}",
            "method": self.get_method_name()
        }
    
    def get_method_name(self) -> str:
        return "Cryptocurrency"

class ApplePayPayment(PaymentMethod):
    """Apple Pay payment implementation"""
    def validate_payment_data(self, payment_data: Dict[str, Any]) -> bool:
        required_fields = ["device_id", "touch_id"]
        return all(field in payment_data for field in required_fields)
    
    def process_payment(self, amount: float, payment_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate_payment_data(payment_data):
            return {"status": "failed", "message": "Apple Pay authentication failed"}
        
        device_id = payment_data["device_id"]
        return {
            "status": "success",
            "transaction_id": f"apple_{device_id}_{amount}",
            "method": self.get_method_name()
        }
    
    def get_method_name(self) -> str:
        return "Apple Pay"

# Usage
processor = PaymentProcessor()

# Register existing payment methods
processor.register_payment_method("credit_card", CreditCardPayment())
processor.register_payment_method("paypal", PayPalPayment())
processor.register_payment_method("bank_transfer", BankTransferPayment())

# Register new payment methods without modifying existing code
processor.register_payment_method("crypto", CryptocurrencyPayment())
processor.register_payment_method("apple_pay", ApplePayPayment())

print("Supported payment methods:", processor.get_supported_methods())

# Test different payment methods
test_payments = [
    ("credit_card", {"card_number": "1234567890123456", "cvv": "123", "expiry": "12/25"}),
    ("paypal", {"email": "user@example.com", "password": "password123"}),
    ("crypto", {"wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "private_key": "secret"}),
    ("apple_pay", {"device_id": "iPhone12", "touch_id": "verified"})
]

amount = 100.0
for method_key, payment_data in test_payments:
    result = processor.process_payment(amount, method_key, payment_data)
    print(f"{method_key}: {result}")
```

**Benefits:**
- ✅ New payment methods added without modifying existing code
- ✅ Each payment method handles its own validation and processing
- ✅ Easy to test individual payment methods
- ✅ Processor remains stable while supporting new payment types
- ✅ Clear separation of concerns for each payment method

---

## Advanced Examples

### Example 5: Plugin-Based Architecture

#### Real-World Scenario: Content Management System with Plugins

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List
import importlib
import os

class Plugin(ABC):
    """Base plugin interface"""
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def get_version(self) -> str:
        pass
    
    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        pass

class ContentProcessor(Plugin):
    """Abstract content processor plugin"""
    @abstractmethod
    def process_content(self, content: str, metadata: Dict[str, Any]) -> str:
        pass
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        content = context.get("content", "")
        metadata = context.get("metadata", {})
        processed_content = self.process_content(content, metadata)
        return {"content": processed_content, "metadata": metadata}

class SecurityPlugin(Plugin):
    """Abstract security plugin"""
    @abstractmethod
    def scan_content(self, content: str) -> Dict[str, Any]:
        pass
    
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        content = context.get("content", "")
        scan_result = self.scan_content(content)
        context["security_scan"] = scan_result
        return context

# Built-in plugins
class MarkdownProcessor(ContentProcessor):
    """Markdown to HTML processor"""
    def get_name(self) -> str:
        return "Markdown Processor"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.enable_tables = config.get("enable_tables", True)
        self.enable_code_highlighting = config.get("enable_code_highlighting", True)
        return True
    
    def process_content(self, content: str, metadata: Dict[str, Any]) -> str:
        # Simplified markdown processing
        processed = content.replace("**", "<strong>").replace("**", "</strong>")
        processed = processed.replace("*", "<em>").replace("*", "</em>")
        
        if self.enable_tables:
            # Table processing logic
            pass
        
        if self.enable_code_highlighting:
            # Code highlighting logic
            pass
        
        return processed

class BasicSecurityScanner(SecurityPlugin):
    """Basic security scanner"""
    def get_name(self) -> str:
        return "Basic Security Scanner"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.blocked_words = config.get("blocked_words", ["script", "iframe", "object"])
        self.max_length = config.get("max_content_length", 10000)
        return True
    
    def scan_content(self, content: str) -> Dict[str, Any]:
        issues = []
        
        # Check content length
        if len(content) > self.max_length:
            issues.append(f"Content exceeds maximum length of {self.max_length}")
        
        # Check for blocked words
        for word in self.blocked_words:
            if word.lower() in content.lower():
                issues.append(f"Blocked word detected: {word}")
        
        return {
            "passed": len(issues) == 0,
            "issues": issues,
            "scanned_at": "2025-01-01T00:00:00Z"
        }

class PluginManager:
    """Plugin manager - closed for modification, open for extension"""
    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}
        self.plugin_configs: Dict[str, Dict[str, Any]] = {}
        self.execution_order: List[str] = []
    
    def register_plugin(self, plugin_id: str, plugin: Plugin, config: Dict[str, Any] = None):
        """Register a new plugin"""
        if config is None:
            config = {}
        
        if plugin.initialize(config):
            self.plugins[plugin_id] = plugin
            self.plugin_configs[plugin_id] = config
            self.execution_order.append(plugin_id)
            print(f"Plugin registered: {plugin.get_name()} v{plugin.get_version()}")
        else:
            print(f"Failed to initialize plugin: {plugin.get_name()}")
    
    def unregister_plugin(self, plugin_id: str):
        """Unregister a plugin"""
        if plugin_id in self.plugins:
            plugin = self.plugins[plugin_id]
            del self.plugins[plugin_id]
            del self.plugin_configs[plugin_id]
            self.execution_order.remove(plugin_id)
            print(f"Plugin unregistered: {plugin.get_name()}")
    
    def execute_plugins(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute all plugins in order"""
        result = context.copy()
        
        for plugin_id in self.execution_order:
            if plugin_id in self.plugins:
                plugin = self.plugins[plugin_id]
                try:
                    result = plugin.execute(result)
                    print(f"Executed plugin: {plugin.get_name()}")
                except Exception as e:
                    print(f"Plugin execution failed: {plugin.get_name()} - {e}")
        
        return result
    
    def get_plugin_info(self) -> List[Dict[str, str]]:
        """Get information about all registered plugins"""
        return [
            {
                "id": plugin_id,
                "name": plugin.get_name(),
                "version": plugin.get_version()
            }
            for plugin_id, plugin in self.plugins.items()
        ]

# Adding new plugins - open for extension!
class HTMLSanitizer(ContentProcessor):
    """HTML sanitization plugin"""
    def get_name(self) -> str:
        return "HTML Sanitizer"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.allowed_tags = config.get("allowed_tags", ["p", "br", "strong", "em"])
        return True
    
    def process_content(self, content: str, metadata: Dict[str, Any]) -> str:
        # Simplified HTML sanitization
        import re
        
        # Remove all tags except allowed ones
        allowed_pattern = "|".join(self.allowed_tags)
        pattern = f"<(?!/?({allowed_pattern})\\b)[^>]*>"
        sanitized = re.sub(pattern, "", content)
        
        return sanitized

class AdvancedSecurityScanner(SecurityPlugin):
    """Advanced security scanner with ML capabilities"""
    def get_name(self) -> str:
        return "Advanced Security Scanner"
    
    def get_version(self) -> str:
        return "2.0.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.ml_model_path = config.get("ml_model_path", "security_model.pkl")
        self.confidence_threshold = config.get("confidence_threshold", 0.8)
        # Initialize ML model here
        return True
    
    def scan_content(self, content: str) -> Dict[str, Any]:
        # Simulate ML-based security scanning
        issues = []
        confidence_scores = {}
        
        # Simulate various security checks
        if "javascript:" in content.lower():
            issues.append("Potential XSS attack detected")
            confidence_scores["xss"] = 0.95
        
        if "union select" in content.lower():
            issues.append("Potential SQL injection detected")
            confidence_scores["sql_injection"] = 0.87
        
        return {
            "passed": len(issues) == 0,
            "issues": issues,
            "confidence_scores": confidence_scores,
            "scanned_at": "2025-01-01T00:00:00Z",
            "scanner_version": self.get_version()
        }

class SEOOptimizer(ContentProcessor):
    """SEO optimization plugin"""
    def get_name(self) -> str:
        return "SEO Optimizer"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.target_keywords = config.get("target_keywords", [])
        self.min_word_count = config.get("min_word_count", 300)
        return True
    
    def process_content(self, content: str, metadata: Dict[str, Any]) -> str:
        # Add SEO metadata
        word_count = len(content.split())
        
        # Add meta description if missing
        if "description" not in metadata:
            # Generate description from first 160 characters
            description = content[:160].strip()
            if len(content) > 160:
                description += "..."
            metadata["description"] = description
        
        # Add keyword density information
        if self.target_keywords:
            keyword_density = {}
            content_lower = content.lower()
            for keyword in self.target_keywords:
                count = content_lower.count(keyword.lower())
                density = (count / word_count) * 100 if word_count > 0 else 0
                keyword_density[keyword] = density
            
            metadata["keyword_density"] = keyword_density
        
        # Add word count
        metadata["word_count"] = word_count
        
        return content

# Usage example
def main():
    # Create plugin manager
    manager = PluginManager()
    
    # Register built-in plugins
    manager.register_plugin("markdown", MarkdownProcessor(), {
        "enable_tables": True,
        "enable_code_highlighting": True
    })
    
    manager.register_plugin("basic_security", BasicSecurityScanner(), {
        "blocked_words": ["script", "iframe", "eval"],
        "max_content_length": 5000
    })
    
    # Register new plugins without modifying existing code
    manager.register_plugin("html_sanitizer", HTMLSanitizer(), {
        "allowed_tags": ["p", "br", "strong", "em", "ul", "li"]
    })
    
    manager.register_plugin("advanced_security", AdvancedSecurityScanner(), {
        "confidence_threshold": 0.85
    })
    
    manager.register_plugin("seo_optimizer", SEOOptimizer(), {
        "target_keywords": ["python", "programming", "tutorial"],
        "min_word_count": 500
    })
    
    # Display registered plugins
    print("Registered plugins:")
    for plugin_info in manager.get_plugin_info():
        print(f"- {plugin_info['name']} v{plugin_info['version']} (ID: {plugin_info['id']})")
    
    # Process content through all plugins
    content = """
    # Python Programming Tutorial
    
    This is a **comprehensive** tutorial on *Python programming*.
    Learn about variables, functions, and classes.
    
    ```python
    def hello_world():
        print("Hello, World!")
    ```
    """
    
    context = {
        "content": content,
        "metadata": {
            "title": "Python Programming Tutorial",
            "author": "John Doe"
        }
    }
    
    # Execute all plugins
    result = manager.execute_plugins(context)
    
    print("\nProcessing complete!")
    print(f"Final content length: {len(result['content'])}")
    print(f"Metadata keys: {list(result['metadata'].keys())}")
    
    if "security_scan" in result:
        security_result = result["security_scan"]
        print(f"Security scan passed: {security_result['passed']}")
        if security_result['issues']:
            print(f"Security issues: {security_result['issues']}")

if __name__ == "__main__":
    main()
```

**Advanced Benefits:**
- ✅ **Plugin Architecture**: New functionality added without core system changes
- ✅ **Runtime Configuration**: Plugins can be loaded/unloaded dynamically
- ✅ **Extensible Framework**: Third-party developers can create plugins
- ✅ **Isolated Functionality**: Each plugin is independent and testable
- ✅ **Flexible Execution**: Plugin execution order can be configured

---

## Design Patterns Supporting OCP

### 1. Strategy Pattern

The Strategy pattern encapsulates algorithms and makes them interchangeable, perfectly supporting OCP.

```python
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

class BubbleSort(SortingStrategy):
    def sort(self, data: list) -> list:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class QuickSort(SortingStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class MergeSort(SortingStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: list, right: list) -> list:
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

class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy
    
    def sort_data(self, data: list) -> list:
        return self.strategy.sort(data)

# Adding new sorting algorithms - open for extension!
class HeapSort(SortingStrategy):
    def sort(self, data: list) -> list:
        import heapq
        return sorted(data)  # Simplified implementation

# Usage
data = [64, 34, 25, 12, 22, 11, 90]

sorter = Sorter(BubbleSort())
print("Bubble Sort:", sorter.sort_data(data))

sorter.set_strategy(QuickSort())
print("Quick Sort:", sorter.sort_data(data))

sorter.set_strategy(HeapSort())
print("Heap Sort:", sorter.sort_data(data))
```

### 2. Template Method Pattern

The Template Method pattern defines the skeleton of an algorithm, allowing subclasses to override specific steps.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Template method pattern for data processing"""
    
    def process_data(self, data):
        """Template method - defines the algorithm structure"""
        validated_data = self.validate_data(data)
        transformed_data = self.transform_data(validated_data)
        processed_data = self.apply_business_logic(transformed_data)
        result = self.format_output(processed_data)
        self.log_processing(result)
        return result
    
    @abstractmethod
    def validate_data(self, data):
        pass
    
    @abstractmethod
    def transform_data(self, data):
        pass
    
    @abstractmethod
    def apply_business_logic(self, data):
        pass
    
    def format_output(self, data):
        """Default implementation - can be overridden"""
        return {"result": data, "status": "success"}
    
    def log_processing(self, result):
        """Default implementation - can be overridden"""
        print(f"Processing completed: {result['status']}")

class UserDataProcessor(DataProcessor):
    def validate_data(self, data):
        if not isinstance(data, dict) or "email" not in data:
            raise ValueError("Invalid user data")
        return data
    
    def transform_data(self, data):
        # Normalize email to lowercase
        data["email"] = data["email"].lower()
        return data
    
    def apply_business_logic(self, data):
        # Add user ID and creation timestamp
        import uuid
        from datetime import datetime
        data["user_id"] = str(uuid.uuid4())
        data["created_at"] = datetime.now().isoformat()
        return data

class OrderDataProcessor(DataProcessor):
    def validate_data(self, data):
        required_fields = ["customer_id", "items", "total"]
        if not all(field in data for field in required_fields):
            raise ValueError("Invalid order data")
        return data
    
    def transform_data(self, data):
        # Calculate tax
        data["tax"] = data["total"] * 0.1
        data["total_with_tax"] = data["total"] + data["tax"]
        return data
    
    def apply_business_logic(self, data):
        # Generate order number and set status
        import random
        data["order_number"] = f"ORD-{random.randint(10000, 99999)}"
        data["status"] = "pending"
        return data
    
    def format_output(self, data):
        # Custom formatting for orders
        return {
            "order_id": data["order_number"],
            "status": "created",
            "total": data["total_with_tax"],
            "details": data
        }

# Adding new processors - open for extension!
class ProductDataProcessor(DataProcessor):
    def validate_data(self, data):
        if "name" not in data or "price" not in data:
            raise ValueError("Invalid product data")
        return data
    
    def transform_data(self, data):
        # Generate SKU
        import re
        name_part = re.sub(r'[^a-zA-Z0-9]', '', data["name"])[:8].upper()
        data["sku"] = f"PROD-{name_part}"
        return data
    
    def apply_business_logic(self, data):
        # Set default values
        data["in_stock"] = True
        data["category"] = data.get("category", "general")
        return data

# Usage
user_data = {"email": "USER@EXAMPLE.COM", "name": "John Doe"}
order_data = {"customer_id": "123", "items": ["item1"], "total": 100}
product_data = {"name": "Python Book", "price": 29.99}

processors = [
    UserDataProcessor(),
    OrderDataProcessor(),
    ProductDataProcessor()
]

test_data = [user_data, order_data, product_data]

for processor, data in zip(processors, test_data):
    try:
        result = processor.process_data(data)
        print(f"{processor.__class__.__name__}: {result}")
    except Exception as e:
        print(f"Error processing {processor.__class__.__name__}: {e}")
```

### 3. Factory Method Pattern

The Factory Method pattern creates objects without specifying their exact classes, supporting OCP by allowing new types to be added.

```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def create_content(self) -> str:
        pass
    
    @abstractmethod
    def get_file_extension(self) -> str:
        pass

class PDFDocument(Document):
    def create_content(self) -> str:
        return "PDF content with formatting and images"
    
    def get_file_extension(self) -> str:
        return ".pdf"

class WordDocument(Document):
    def create_content(self) -> str:
        return "Word document with rich text formatting"
    
    def get_file_extension(self) -> str:
        return ".docx"

class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass
    
    def process_document(self, title: str) -> str:
        """Template method using factory method"""
        document = self.create_document()
        content = document.create_content()
        extension = document.get_file_extension()
        filename = f"{title}{extension}"
        
        # Simulate document processing
        print(f"Creating {filename}")
        print(f"Content: {content}")
        return filename

class PDFFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()

class WordFactory(DocumentFactory):
    def create_document(self) -> Document:
        return WordDocument()

# Adding new document types - open for extension!
class PowerPointDocument(Document):
    def create_content(self) -> str:
        return "PowerPoint presentation with slides and animations"
    
    def get_file_extension(self) -> str:
        return ".pptx"

class PowerPointFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PowerPointDocument()

class ExcelDocument(Document):
    def create_content(self) -> str:
        return "Excel spreadsheet with formulas and charts"
    
    def get_file_extension(self) -> str:
        return ".xlsx"

class ExcelFactory(DocumentFactory):
    def create_document(self) -> Document:
        return ExcelDocument()

# Usage
factories = [
    PDFFactory(),
    WordFactory(),
    PowerPointFactory(),
    ExcelFactory()
]

for factory in factories:
    filename = factory.process_document("MyDocument")
    print(f"Generated: {filename}\n")
```

**Design Pattern Benefits:**
- ✅ **Strategy**: Algorithms can be swapped at runtime
- ✅ **Template Method**: Algorithm structure is stable, steps are extensible
- ✅ **Factory Method**: New product types can be added without changing factories
- ✅ **All Patterns**: Support OCP by enabling extension without modification

---

## Real-World Applications

### Industry Examples

#### 1. **Web Framework Middleware**
```python
# Django/Flask-style middleware system
class Middleware(ABC):
    @abstractmethod
    def process_request(self, request):
        pass
    
    @abstractmethod
    def process_response(self, request, response):
        pass

class AuthenticationMiddleware(Middleware):
    def process_request(self, request):
        # Check authentication
        pass
    
    def process_response(self, request, response):
        return response

class CorsMiddleware(Middleware):
    def process_request(self, request):
        # Handle CORS preflight
        pass
    
    def process_response(self, request, response):
        # Add CORS headers
        return response

# New middleware can be added without modifying the framework
class RateLimitingMiddleware(Middleware):
    def process_request(self, request):
        # Check rate limits
        pass
    
    def process_response(self, request, response):
        return response
```

#### 2. **Database Drivers**
```python
class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self, connection_string):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLDriver(DatabaseDriver):
    def connect(self, connection_string):
        # MySQL connection logic
        pass
    
    def execute_query(self, query):
        # MySQL query execution
        pass

class PostgreSQLDriver(DatabaseDriver):
    def connect(self, connection_string):
        # PostgreSQL connection logic
        pass
    
    def execute_query(self, query):
        # PostgreSQL query execution
        pass

# Adding new database support without modifying existing code
class MongoDBDriver(DatabaseDriver):
    def connect(self, connection_string):
        # MongoDB connection logic
        pass
    
    def execute_query(self, query):
        # MongoDB query execution
        pass
```

#### 3. **Cloud Service Providers**
```python
class CloudProvider(ABC):
    @abstractmethod
    def deploy_application(self, app_config):
        pass
    
    @abstractmethod
    def scale_resources(self, resource_config):
        pass

class AWSProvider(CloudProvider):
    def deploy_application(self, app_config):
        # AWS deployment logic
        pass
    
    def scale_resources(self, resource_config):
        # AWS scaling logic
        pass

class AzureProvider(CloudProvider):
    def deploy_application(self, app_config):
        # Azure deployment logic
        pass
    
    def scale_resources(self, resource_config):
        # Azure scaling logic
        pass

# Adding new cloud providers
class GoogleCloudProvider(CloudProvider):
    def deploy_application(self, app_config):
        # GCP deployment logic
        pass
    
    def scale_resources(self, resource_config):
        # GCP scaling logic
        pass
```

### Framework Integration

#### **Plugin Systems**
```python
# Modern plugin architecture
class PluginRegistry:
    def __init__(self):
        self.plugins = {}
    
    def register(self, plugin_type, plugin_class):
        if plugin_type not in self.plugins:
            self.plugins[plugin_type] = []
        self.plugins[plugin_type].append(plugin_class)
    
    def get_plugins(self, plugin_type):
        return self.plugins.get(plugin_type, [])

# Usage in frameworks like Django, Flask, FastAPI
registry = PluginRegistry()
registry.register("authentication", OAuth2Plugin)
registry.register("authentication", JWTPlugin)
registry.register("caching", RedisPlugin)
registry.register("caching", MemcachedPlugin)
```

---

## Best Practices

### 1. **Design Guidelines**

#### **Start with Abstractions**
```python
# ✅ Define interfaces first
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, payment_data):
        pass

# ✅ Then implement concrete classes
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount, payment_data):
        # Implementation
        pass

# ❌ Don't start with concrete implementations
class CreditCardProcessor:
    def process_payment(self, amount, card_number, cvv):
        # Hard to extend later
        pass
```

#### **Use Composition Over Inheritance**
```python
# ✅ Composition - more flexible
class EmailService:
    def __init__(self, sender: EmailSender, formatter: EmailFormatter):
        self.sender = sender
        self.formatter = formatter
    
    def send_email(self, recipient, subject, content):
        formatted_content = self.formatter.format(content)
        self.sender.send(recipient, subject, formatted_content)

# ❌ Deep inheritance - rigid
class SMTPEmailService(EmailService):
    class HTMLEmailService(SMTPEmailService):
        class TemplatedHTMLEmailService(HTMLEmailService):
            # Too many inheritance levels
            pass
```

### 2. **Implementation Strategies**

#### **Dependency Injection**
```python
class OrderService:
    def __init__(self, 
                 payment_processor: PaymentProcessor,
                 inventory_manager: InventoryManager,
                 notification_service: NotificationService):
        self.payment_processor = payment_processor
        self.inventory_manager = inventory_manager
        self.notification_service = notification_service
    
    def process_order(self, order):
        # Use injected dependencies
        self.inventory_manager.reserve_items(order.items)
        result = self.payment_processor.process_payment(order.total, order.payment_data)
        if result.success:
            self.notification_service.send_confirmation(order)
```

#### **Configuration-Based Extension**
```python
class ProcessorFactory:
    def __init__(self, config):
        self.config = config
        self.processors = {}
        self._register_processors()
    
    def _register_processors(self):
        for processor_config in self.config.get("processors", []):
            processor_class = self._load_class(processor_config["class"])
            self.processors[processor_config["name"]] = processor_class
    
    def create_processor(self, processor_name):
        if processor_name in self.processors:
            return self.processors[processor_name]()
        raise ValueError(f"Unknown processor: {processor_name}")
```

### 3. **Testing Strategies**

#### **Test Each Extension Independently**
```python
import unittest
from unittest.mock import Mock

class TestPaymentProcessors(unittest.TestCase):
    def test_credit_card_processor(self):
        processor = CreditCardProcessor()
        payment_data = {"card_number": "1234567890123456", "cvv": "123"}
        result = processor.process_payment(100.0, payment_data)
        self.assertTrue(result.success)
    
    def test_paypal_processor(self):
        processor = PayPalProcessor()
        payment_data = {"email": "test@example.com", "password": "password"}
        result = processor.process_payment(100.0, payment_data)
        self.assertTrue(result.success)

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.mock_payment_processor = Mock()
        self.mock_inventory_manager = Mock()
        self.mock_notification_service = Mock()
        
        self.order_service = OrderService(
            self.mock_payment_processor,
            self.mock_inventory_manager,
            self.mock_notification_service
        )
    
    def test_successful_order_processing(self):
        order = Mock()
        self.mock_payment_processor.process_payment.return_value = Mock(success=True)
        
        self.order_service.process_order(order)
        
        self.mock_inventory_manager.reserve_items.assert_called_once()
        self.mock_payment_processor.process_payment.assert_called_once()
        self.mock_notification_service.send_confirmation.assert_called_once()
```

### 4. **Documentation and Communication**

#### **Document Extension Points**
```python
class DataProcessor(ABC):
    """
    Abstract base class for data processors.
    
    To add a new data processor:
    1. Inherit from DataProcessor
    2. Implement process_data method
    3. Register with ProcessorRegistry
    
    Example:
        class CustomProcessor(DataProcessor):
            def process_data(self, data):
                # Your processing logic here
                return processed_data
        
        registry.register("custom", CustomProcessor)
    """
    @abstractmethod
    def process_data(self, data):
        """
        Process the input data.
        
        Args:
            data: Input data to process
            
        Returns:
            Processed data
            
        Raises:
            ProcessingError: If processing fails
        """
        pass
```

---

## Common Pitfalls

### 1. **Over-Engineering**

#### ❌ **Creating Abstractions Too Early**
```python
# Don't create abstractions until you have at least 2-3 implementations
class UserService:
    def get_user(self, user_id):
        # Simple implementation
        return database.get_user(user_id)

# ❌ Premature abstraction
class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

class DatabaseUserRepository(UserRepository):
    def get_user(self, user_id):
        return database.get_user(user_id)

# ✅ Add abstraction when you need multiple implementations
class UserService:
    def get_user(self, user_id):
        return database.get_user(user_id)

# Later, when you need caching:
class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

class DatabaseUserRepository(UserRepository):
    def get_user(self, user_id):
        return database.get_user(user_id)

class CachedUserRepository(UserRepository):
    def get_user(self, user_id):
        # Check cache first, then database
        pass
```

### 2. **Leaky Abstractions**

#### ❌ **Exposing Implementation Details**
```python
# ❌ Abstraction leaks implementation details
class FileStorage(ABC):
    @abstractmethod
    def save_file(self, filename, content):
        pass
    
    @abstractmethod
    def get_file_path(self):  # ← Leaky! Not all storage has file paths
        pass

class S3Storage(FileStorage):
    def save_file(self, filename, content):
        # S3 implementation
        pass
    
    def get_file_path(self):
        # S3 doesn't have traditional file paths!
        return f"s3://bucket/{filename}"

# ✅ Clean abstraction
class FileStorage(ABC):
    @abstractmethod
    def save_file(self, filename, content):
        pass
    
    @abstractmethod
    def get_file_url(self):  # ← Better abstraction
        pass
```

### 3. **Violation Through Dependencies**

#### ❌ **Hard-coded Dependencies**
```python
# ❌ Violates OCP through hard-coded dependencies
class OrderProcessor:
    def __init__(self):
        self.email_service = SMTPEmailService()  # ← Hard-coded!
        self.payment_processor = CreditCardProcessor()  # ← Hard-coded!
    
    def process_order(self, order):
        # Processing logic
        pass

# ✅ Dependency injection preserves OCP
class OrderProcessor:
    def __init__(self, email_service: EmailService, payment_processor: PaymentProcessor):
        self.email_service = email_service
        self.payment_processor = payment_processor
    
    def process_order(self, order):
        # Processing logic
        pass
```

### 4. **Ignoring Performance**

#### ⚠️ **Balance Flexibility with Performance**
```python
# Sometimes direct implementation is better for performance-critical code
class HighPerformanceCalculator:
    def calculate(self, data):
        # Direct implementation for performance
        if self.calculation_type == "simple":
            return sum(data)
        elif self.calculation_type == "complex":
            return sum(x * x for x in data)
        # Limited but fast

# Use OCP for non-performance-critical parts
class ReportGenerator:
    def __init__(self, formatter: ReportFormatter):
        self.formatter = formatter  # Flexible formatting
    
    def generate_report(self, data):
        # Use flexible formatter
        return self.formatter.format(data)
```

---

## Exercises

### 🎯 Practice Problems

Now it's time to apply what you've learned! Work through these exercises to master the Open/Closed Principle.

#### **Exercise 1: Basic Level**
**File**: `01-basic-open-closed.py`

**Problem**: You have a `Shape` class with area calculation logic that uses if-else statements. Refactor it to follow OCP.

**Your Task**:
1. Identify the OCP violation in the current code
2. Create an abstract base class for shapes
3. Implement concrete shape classes
4. Ensure new shapes can be added without modifying existing code

**Learning Goals**:
- Recognize OCP violations
- Practice polymorphism and inheritance
- Understand the benefits of extensible design

#### **Exercise 2: Advanced Level**
**File**: `02-advanced-open-closed.py`

**Problem**: You have a `Discount` system that uses conditional logic to apply different discount types. This is a complex business scenario.

**Your Task**:
1. Analyze the multiple discount strategies
2. Design a strategy pattern implementation
3. Create a flexible discount system
4. Add new discount types without modifying existing code

**Learning Goals**:
- Apply strategy pattern for OCP
- Handle complex business rules
- Design extensible systems
- Manage multiple strategies

### 💡 **Self-Assessment Questions**

Before looking at the solutions, ask yourself:

1. **Identification**: Can you spot the conditional logic that violates OCP?
2. **Abstraction**: What interface/abstract class would you create?
3. **Implementation**: How would you structure the concrete classes?
4. **Extension**: How easy is it to add new functionality?
5. **Benefits**: What specific advantages does your refactoring provide?

### 🔍 **Code Review Checklist**

When reviewing your solution:

- [ ] **No Conditional Logic**: Removed if-else chains for type checking
- [ ] **Clear Abstractions**: Well-defined interfaces or abstract classes
- [ ] **Polymorphic Behavior**: Uses inheritance and method overriding
- [ ] **Easy Extension**: New types can be added without modification
- [ ] **Stable Core**: Existing code remains unchanged when extending
- [ ] **Single Responsibility**: Each class has one reason to change

### 🚀 **Challenge Exercises**

Ready for more? Try these additional challenges:

#### **Challenge 1: Plugin-Based Calculator**
Create a calculator system that supports plugins:
- Basic operations (add, subtract, multiply, divide)
- Advanced operations (power, square root, logarithm)
- Statistical operations (mean, median, standard deviation)
- Custom operations can be added as plugins

**Focus**: Design a plugin architecture that follows OCP.

#### **Challenge 2: Multi-Format Logger**
Design a logging system that supports multiple output formats:
- Console logging with different levels
- File logging with rotation
- Database logging with structured data
- Remote logging to external services
- Custom formatters and destinations

**Focus**: Use strategy pattern and factory pattern to achieve OCP.

#### **Challenge 3: E-commerce Pricing Engine**
Build a flexible pricing engine for an e-commerce platform:
- Base product pricing
- Quantity-based discounts
- Customer tier discounts
- Seasonal promotions
- Bundle pricing
- Dynamic pricing based on demand

**Focus**: Handle complex business rules while maintaining OCP.

---

## Summary

### 🎯 **Key Takeaways**

#### **What is OCP?**
- **Definition**: Software entities should be open for extension, closed for modification
- **Purpose**: Enable adding new functionality without changing existing code
- **Goal**: Create flexible, maintainable, and extensible systems

#### **How to Apply OCP**
1. **Identify Extension Points**: Look for areas that might need new functionality
2. **Create Abstractions**: Define interfaces or abstract classes
3. **Use Polymorphism**: Implement concrete classes that extend abstractions
4. **Inject Dependencies**: Avoid hard-coded dependencies on concrete classes

#### **Benefits of OCP**
- ✅ **Reduced Risk**: No modification of tested, working code
- ✅ **Easier Testing**: New features can be tested independently
- ✅ **Faster Development**: Parallel development of different extensions
- ✅ **Better Maintainability**: Clear separation of concerns
- ✅ **Enhanced Flexibility**: Runtime configuration and plugin architectures

#### **Common Patterns**
- **Strategy Pattern**: Encapsulate algorithms and make them interchangeable
- **Template Method**: Define algorithm skeleton, allow step customization
- **Factory Method**: Create objects without specifying exact classes
- **Plugin Architecture**: Load and execute extensions dynamically

### 🔍 **Recognition Patterns**

#### **OCP Violations (Red Flags)**
- Long if-else or switch statements for type checking
- Frequent modifications to the same class for new features
- Hard-coded dependencies on specific implementations
- Type checking with isinstance() for behavior selection
- Growing conditional complexity over time

#### **Good OCP Implementation (Green Flags)**
- Clear abstractions with well-defined interfaces
- Polymorphic behavior through inheritance
- New functionality added through new classes
- Stable core classes that rarely change
- Plugin or strategy-based architectures

### 📈 **Progression Path**

#### **Beginner Level**
- Recognize basic OCP violations (if-else chains)
- Create simple polymorphic hierarchies
- Practice with basic strategy pattern
- Focus on single extension points

#### **Intermediate Level**
- Design complex strategy systems
- Handle multiple extension points
- Apply factory patterns for object creation
- Manage dependencies effectively

#### **Advanced Level**
- Design plugin architectures
- Create framework-level extension points
- Balance flexibility with performance
- Mentor others in OCP application

### 🛠️ **Practical Application**

#### **In Your Daily Work**
1. **Code Reviews**: Look for conditional logic that could be polymorphic
2. **New Features**: Design extension points before implementing
3. **Refactoring**: Replace conditional logic with strategy patterns
4. **Architecture**: Plan for future extensions in system design

#### **Team Practices**
- **Design Sessions**: Discuss extension points during planning
- **Coding Standards**: Include OCP guidelines in team standards
- **Code Templates**: Create templates for common OCP patterns
- **Knowledge Sharing**: Share OCP success stories and lessons learned

### 🎓 **Next Steps**

#### **Continue Learning**
1. **Practice**: Work through exercises multiple times with different scenarios
2. **Apply**: Use OCP in your current projects
3. **Study**: Analyze well-designed frameworks and libraries
4. **Experiment**: Try different design patterns that support OCP

#### **Related Topics**
- **Liskov Substitution Principle**: Ensure proper inheritance relationships
- **Dependency Inversion Principle**: Depend on abstractions, not concretions
- **Design Patterns**: Study patterns that naturally support OCP
- **Software Architecture**: Apply OCP at the system level

### 💭 **Final Thoughts**

The Open/Closed Principle is about **future-proofing your code**. When you consistently apply OCP:

- **Your systems become more adaptable** to changing requirements
- **Your code becomes more professional** and easier to extend
- **Your team becomes more productive** with parallel development
- **Your applications become more robust** with stable core functionality

Remember: **Don't over-engineer**, but do plan for reasonable extensions. The key is finding the right balance between flexibility and simplicity.

### 🔗 **Resources for Continued Learning**

#### **Books**
- "Design Patterns" by Gang of Four
- "Clean Code" by Robert C. Martin
- "Refactoring" by Martin Fowler

#### **Online Resources**
- [SOLID Principles Documentation](../README.md)
- [Single Responsibility Principle](../01-single-responsibility/)
- [Design Patterns Examples](../../object-oriented-programming/06-design-patterns/)

#### **Practice Platforms**
- Work through the provided exercises
- Contribute to open-source projects
- Design pattern practice problems
- Code review sessions focusing on OCP

---

**🎉 Congratulations!** You've completed the comprehensive Open/Closed Principle tutorial. You're now equipped with the knowledge and skills to create flexible, extensible, and maintainable software systems.

**Ready for the next challenge?** Continue with the [Liskov Substitution Principle](../03-liskov-substitution/) to further enhance your SOLID design skills!

---

*Happy coding! 🚀*