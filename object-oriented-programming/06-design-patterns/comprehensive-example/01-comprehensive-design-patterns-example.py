"""Question: Create a comprehensive example that combines multiple design patterns.

Build a complete e-commerce system that demonstrates the integration of multiple
design patterns working together in a realistic application.

Requirements:
1. Use Factory pattern for creating different product types
2. Implement Observer pattern for order status notifications
3. Use Strategy pattern for different payment methods
4. Apply Command pattern for order operations (place, cancel, modify)
5. Implement Decorator pattern for product pricing (discounts, taxes)
6. Use Facade pattern to simplify complex subsystem interactions
7. Apply Singleton pattern for system configuration
8. Demonstrate how patterns work together harmoniously

Example usage:
    # Factory creates products
    product_factory = ProductFactory()
    laptop = product_factory.create_product("laptop", "Gaming Laptop", 1500.0)
    
    # Decorator adds pricing features
    discounted_laptop = DiscountDecorator(laptop, 0.1)  # 10% discount
    final_laptop = TaxDecorator(discounted_laptop, 0.08)  # 8% tax
    
    # Observer notifies about order status
    order = Order()
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()
    order.attach(email_notifier)
    order.attach(sms_notifier)
    
    # Strategy handles payment
    payment_context = PaymentContext()
    payment_context.set_strategy(CreditCardStrategy())
    
    # Command encapsulates order operations
    place_order_cmd = PlaceOrderCommand(order, final_laptop)
    order_invoker = OrderInvoker()
    order_invoker.execute_command(place_order_cmd)
    
    # Facade simplifies the entire process
    ecommerce_facade = ECommerceFacade()
    ecommerce_facade.purchase_product("laptop", "credit_card", customer_info)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# This is an advanced exercise that combines multiple patterns. Try to:
# 1. Identify which patterns would be most useful for each requirement
# 2. Think about how the patterns can work together
# 3. Start with a simple implementation and gradually add complexity
# 4. Focus on clean interfaces and separation of concerns

# Try to implement your solution here:
# (Write your code below this line)


















































# ===============================================================================
#                           STEP-BY-STEP SOLUTION
# ===============================================================================
#
# CLASSROOM-STYLE WALKTHROUGH
#
# Let's solve this problem step by step, just like in a programming class!
# Each step builds upon the previous one, so you can follow along and understand
# the complete thought process of integrating multiple design patterns.
#
# ===============================================================================


# Step 1: Import modules and create basic product classes (Factory Pattern)
# ===============================================================================

# Explanation:
# We start with the Factory pattern to create different product types.
# This will be the foundation for our e-commerce system.

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from enum import Enum

class ProductType(Enum):
    """Enumeration of product types."""
    LAPTOP = "laptop"
    PHONE = "phone"
    TABLET = "tablet"
    ACCESSORY = "accessory"

class Product(ABC):
    """Abstract base class for all products."""
    
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.product_id = id(self)
    
    @abstractmethod
    def get_category(self) -> str:
        """Get product category."""
        pass
    
    def get_price(self) -> float:
        """Get current price (can be modified by decorators)."""
        return self.base_price
    
    def __str__(self):
        return f"{self.get_category()}: {self.name} - ${self.get_price():.2f}"

class Laptop(Product):
    """Concrete laptop product."""
    
    def __init__(self, name: str, base_price: float, specs: Dict[str, str] = None):
        super().__init__(name, base_price)
        self.specs = specs or {}
    
    def get_category(self) -> str:
        return "Laptop"

class Phone(Product):
    """Concrete phone product."""
    
    def __init__(self, name: str, base_price: float, carrier: str = "Unlocked"):
        super().__init__(name, base_price)
        self.carrier = carrier
    
    def get_category(self) -> str:
        return "Phone"

class Tablet(Product):
    """Concrete tablet product."""
    
    def __init__(self, name: str, base_price: float, screen_size: str = "10 inch"):
        super().__init__(name, base_price)
        self.screen_size = screen_size
    
    def get_category(self) -> str:
        return "Tablet"

class ProductFactory:
    """Factory for creating different product types."""
    
    @staticmethod
    def create_product(product_type: str, name: str, price: float, **kwargs) -> Product:
        """Create a product based on type."""
        product_type = product_type.lower()
        
        if product_type == ProductType.LAPTOP.value:
            return Laptop(name, price, kwargs.get('specs', {}))
        elif product_type == ProductType.PHONE.value:
            return Phone(name, price, kwargs.get('carrier', 'Unlocked'))
        elif product_type == ProductType.TABLET.value:
            return Tablet(name, price, kwargs.get('screen_size', '10 inch'))
        else:
            raise ValueError(f"Unknown product type: {product_type}")

# What we accomplished in this step:
# - Created abstract Product class and concrete implementations
# - Implemented Factory pattern for product creation
# - Added basic product hierarchy with different types

print("=== Step 1: Factory Pattern ===")
factory = ProductFactory()
laptop = factory.create_product("laptop", "Gaming Laptop", 1500.0)
phone = factory.create_product("phone", "Smartphone", 800.0)
print(laptop)
print(phone)
print()


# Step 2: Add Decorator Pattern for pricing features
# ===============================================================================

# Explanation:
# The Decorator pattern allows us to add pricing features (discounts, taxes)
# to products without modifying the original product classes.

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from enum import Enum

class ProductType(Enum):
    """Enumeration of product types."""
    LAPTOP = "laptop"
    PHONE = "phone"
    TABLET = "tablet"
    ACCESSORY = "accessory"

class Product(ABC):
    """Abstract base class for all products."""
    
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.product_id = id(self)
    
    @abstractmethod
    def get_category(self) -> str:
        """Get product category."""
        pass
    
    def get_price(self) -> float:
        """Get current price (can be modified by decorators)."""
        return self.base_price
    
    def __str__(self):
        return f"{self.get_category()}: {self.name} - ${self.get_price():.2f}"

class Laptop(Product):
    """Concrete laptop product."""
    
    def __init__(self, name: str, base_price: float, specs: Dict[str, str] = None):
        super().__init__(name, base_price)
        self.specs = specs or {}
    
    def get_category(self) -> str:
        return "Laptop"

class Phone(Product):
    """Concrete phone product."""
    
    def __init__(self, name: str, base_price: float, carrier: str = "Unlocked"):
        super().__init__(name, base_price)
        self.carrier = carrier
    
    def get_category(self) -> str:
        return "Phone"

class Tablet(Product):
    """Concrete tablet product."""
    
    def __init__(self, name: str, base_price: float, screen_size: str = "10 inch"):
        super().__init__(name, base_price)
        self.screen_size = screen_size
    
    def get_category(self) -> str:
        return "Tablet"

class ProductFactory:
    """Factory for creating different product types."""
    
    @staticmethod
    def create_product(product_type: str, name: str, price: float, **kwargs) -> Product:
        """Create a product based on type."""
        product_type = product_type.lower()
        
        if product_type == ProductType.LAPTOP.value:
            return Laptop(name, price, kwargs.get('specs', {}))
        elif product_type == ProductType.PHONE.value:
            return Phone(name, price, kwargs.get('carrier', 'Unlocked'))
        elif product_type == ProductType.TABLET.value:
            return Tablet(name, price, kwargs.get('screen_size', '10 inch'))
        else:
            raise ValueError(f"Unknown product type: {product_type}")

class ProductDecorator(Product):
    """Base decorator for products."""
    
    def __init__(self, product: Product):
        self.product = product
        super().__init__(product.name, product.base_price)
    
    def get_category(self) -> str:
        return self.product.get_category()
    
    def get_price(self) -> float:
        return self.product.get_price()

class DiscountDecorator(ProductDecorator):
    """Decorator that applies discount to product price."""
    
    def __init__(self, product: Product, discount_rate: float):
        super().__init__(product)
        self.discount_rate = discount_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 - self.discount_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Discount: {self.discount_rate*100:.0f}%)"

class TaxDecorator(ProductDecorator):
    """Decorator that applies tax to product price."""
    
    def __init__(self, product: Product, tax_rate: float):
        super().__init__(product)
        self.tax_rate = tax_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 + self.tax_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Tax: {self.tax_rate*100:.0f}%)"

class ShippingDecorator(ProductDecorator):
    """Decorator that adds shipping cost to product."""
    
    def __init__(self, product: Product, shipping_cost: float):
        super().__init__(product)
        self.shipping_cost = shipping_cost
    
    def get_price(self) -> float:
        return self.product.get_price() + self.shipping_cost
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Shipping: ${self.shipping_cost:.2f})"

# What we accomplished in this step:
# - Added Decorator pattern for pricing modifications
# - Created discount, tax, and shipping decorators
# - Decorators can be chained for multiple pricing features

print("=== Step 2: Decorator Pattern ===")
factory = ProductFactory()
laptop = factory.create_product("laptop", "Gaming Laptop", 1500.0)
print(f"Original: {laptop}")

# Apply decorators
discounted_laptop = DiscountDecorator(laptop, 0.1)  # 10% discount
print(f"With discount: {discounted_laptop}")

final_laptop = TaxDecorator(discounted_laptop, 0.08)  # 8% tax
print(f"With tax: {final_laptop}")

shipped_laptop = ShippingDecorator(final_laptop, 50.0)  # $50 shipping
print(f"With shipping: {shipped_laptop}")
print()


# Step 3: Add Observer Pattern for order status notifications
# ===============================================================================

# Explanation:
# The Observer pattern allows multiple notification systems to be notified
# when order status changes without tight coupling.

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from enum import Enum
from datetime import datetime

class ProductType(Enum):
    """Enumeration of product types."""
    LAPTOP = "laptop"
    PHONE = "phone"
    TABLET = "tablet"
    ACCESSORY = "accessory"

class OrderStatus(Enum):
    """Enumeration of order statuses."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Product(ABC):
    """Abstract base class for all products."""
    
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.product_id = id(self)
    
    @abstractmethod
    def get_category(self) -> str:
        """Get product category."""
        pass
    
    def get_price(self) -> float:
        """Get current price (can be modified by decorators)."""
        return self.base_price
    
    def __str__(self):
        return f"{self.get_category()}: {self.name} - ${self.get_price():.2f}"

class Laptop(Product):
    """Concrete laptop product."""
    
    def __init__(self, name: str, base_price: float, specs: Dict[str, str] = None):
        super().__init__(name, base_price)
        self.specs = specs or {}
    
    def get_category(self) -> str:
        return "Laptop"

class Phone(Product):
    """Concrete phone product."""
    
    def __init__(self, name: str, base_price: float, carrier: str = "Unlocked"):
        super().__init__(name, base_price)
        self.carrier = carrier
    
    def get_category(self) -> str:
        return "Phone"

class Tablet(Product):
    """Concrete tablet product."""
    
    def __init__(self, name: str, base_price: float, screen_size: str = "10 inch"):
        super().__init__(name, base_price)
        self.screen_size = screen_size
    
    def get_category(self) -> str:
        return "Tablet"

class ProductFactory:
    """Factory for creating different product types."""
    
    @staticmethod
    def create_product(product_type: str, name: str, price: float, **kwargs) -> Product:
        """Create a product based on type."""
        product_type = product_type.lower()
        
        if product_type == ProductType.LAPTOP.value:
            return Laptop(name, price, kwargs.get('specs', {}))
        elif product_type == ProductType.PHONE.value:
            return Phone(name, price, kwargs.get('carrier', 'Unlocked'))
        elif product_type == ProductType.TABLET.value:
            return Tablet(name, price, kwargs.get('screen_size', '10 inch'))
        else:
            raise ValueError(f"Unknown product type: {product_type}")

class ProductDecorator(Product):
    """Base decorator for products."""
    
    def __init__(self, product: Product):
        self.product = product
        super().__init__(product.name, product.base_price)
    
    def get_category(self) -> str:
        return self.product.get_category()
    
    def get_price(self) -> float:
        return self.product.get_price()

class DiscountDecorator(ProductDecorator):
    """Decorator that applies discount to product price."""
    
    def __init__(self, product: Product, discount_rate: float):
        super().__init__(product)
        self.discount_rate = discount_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 - self.discount_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Discount: {self.discount_rate*100:.0f}%)"

class TaxDecorator(ProductDecorator):
    """Decorator that applies tax to product price."""
    
    def __init__(self, product: Product, tax_rate: float):
        super().__init__(product)
        self.tax_rate = tax_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 + self.tax_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Tax: {self.tax_rate*100:.0f}%)"

class ShippingDecorator(ProductDecorator):
    """Decorator that adds shipping cost to product."""
    
    def __init__(self, product: Product, shipping_cost: float):
        super().__init__(product)
        self.shipping_cost = shipping_cost
    
    def get_price(self) -> float:
        return self.product.get_price() + self.shipping_cost
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Shipping: ${self.shipping_cost:.2f})"

# Observer Pattern Implementation
class Observer(ABC):
    """Abstract observer interface."""
    
    @abstractmethod
    def update(self, order_id: str, status: OrderStatus, message: str):
        """Update observer with order status change."""
        pass

class EmailNotifier(Observer):
    """Email notification observer."""
    
    def __init__(self, email: str = "customer@example.com"):
        self.email = email
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"📧 EMAIL to {self.email}: Order {order_id} is now {status.value.upper()}")
        if message:
            print(f"   Message: {message}")

class SMSNotifier(Observer):
    """SMS notification observer."""
    
    def __init__(self, phone: str = "+1-555-0123"):
        self.phone = phone
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"📱 SMS to {self.phone}: Order {order_id} status: {status.value.upper()}")

class PushNotifier(Observer):
    """Push notification observer."""
    
    def __init__(self, device_id: str = "device123"):
        self.device_id = device_id
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"🔔 PUSH to {self.device_id}: Order {order_id} - {status.value.upper()}")

class Subject(ABC):
    """Abstract subject interface."""
    
    @abstractmethod
    def attach(self, observer: Observer):
        """Attach an observer."""
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        """Detach an observer."""
        pass
    
    @abstractmethod
    def notify(self, message: str = ""):
        """Notify all observers."""
        pass

class Order(Subject):
    """Order class that notifies observers of status changes."""
    
    def __init__(self, order_id: str = None):
        self.order_id = order_id or f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.status = OrderStatus.PENDING
        self.products: List[Product] = []
        self.observers: List[Observer] = []
        self.total_amount = 0.0
    
    def attach(self, observer: Observer):
        """Attach an observer."""
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer."""
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self, message: str = ""):
        """Notify all observers of status change."""
        for observer in self.observers:
            observer.update(self.order_id, self.status, message)
    
    def add_product(self, product: Product):
        """Add product to order."""
        self.products.append(product)
        self.total_amount += product.get_price()
    
    def set_status(self, status: OrderStatus, message: str = ""):
        """Set order status and notify observers."""
        self.status = status
        self.notify(message)
    
    def __str__(self):
        return f"Order {self.order_id}: {len(self.products)} items, Total: ${self.total_amount:.2f}, Status: {self.status.value}"

# What we accomplished in this step:
# - Added Observer pattern for order notifications
# - Created multiple notification types (Email, SMS, Push)
# - Order class acts as subject that notifies observers
# - Loose coupling between order and notification systems

print("=== Step 3: Observer Pattern ===")
# Create order and attach observers
order = Order()
email_notifier = EmailNotifier("john@example.com")
sms_notifier = SMSNotifier("+1-555-9876")
push_notifier = PushNotifier("john_device")

order.attach(email_notifier)
order.attach(sms_notifier)
order.attach(push_notifier)

# Add products and change status
factory = ProductFactory()
laptop = factory.create_product("laptop", "Gaming Laptop", 1500.0)
discounted_laptop = DiscountDecorator(laptop, 0.1)
order.add_product(discounted_laptop)

print(f"Created: {order}")
order.set_status(OrderStatus.CONFIRMED, "Payment received successfully")
order.set_status(OrderStatus.PROCESSING, "Order is being prepared")
order.set_status(OrderStatus.SHIPPED, "Package is on its way")
print()


# Step 4: Add Strategy Pattern for different payment methods
# ===============================================================================

# Explanation:
# The Strategy pattern allows us to define different payment algorithms
# and switch between them at runtime without changing the client code.

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from enum import Enum
from datetime import datetime

class ProductType(Enum):
    """Enumeration of product types."""
    LAPTOP = "laptop"
    PHONE = "phone"
    TABLET = "tablet"
    ACCESSORY = "accessory"

class OrderStatus(Enum):
    """Enumeration of order statuses."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class PaymentResult:
    """Result of a payment transaction."""
    
    def __init__(self, success: bool, transaction_id: str = "", message: str = ""):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message
        self.timestamp = datetime.now()

class Product(ABC):
    """Abstract base class for all products."""
    
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.product_id = id(self)
    
    @abstractmethod
    def get_category(self) -> str:
        """Get product category."""
        pass
    
    def get_price(self) -> float:
        """Get current price (can be modified by decorators)."""
        return self.base_price
    
    def __str__(self):
        return f"{self.get_category()}: {self.name} - ${self.get_price():.2f}"

class Laptop(Product):
    """Concrete laptop product."""
    
    def __init__(self, name: str, base_price: float, specs: Dict[str, str] = None):
        super().__init__(name, base_price)
        self.specs = specs or {}
    
    def get_category(self) -> str:
        return "Laptop"

class Phone(Product):
    """Concrete phone product."""
    
    def __init__(self, name: str, base_price: float, carrier: str = "Unlocked"):
        super().__init__(name, base_price)
        self.carrier = carrier
    
    def get_category(self) -> str:
        return "Phone"

class Tablet(Product):
    """Concrete tablet product."""
    
    def __init__(self, name: str, base_price: float, screen_size: str = "10 inch"):
        super().__init__(name, base_price)
        self.screen_size = screen_size
    
    def get_category(self) -> str:
        return "Tablet"

class ProductFactory:
    """Factory for creating different product types."""
    
    @staticmethod
    def create_product(product_type: str, name: str, price: float, **kwargs) -> Product:
        """Create a product based on type."""
        product_type = product_type.lower()
        
        if product_type == ProductType.LAPTOP.value:
            return Laptop(name, price, kwargs.get('specs', {}))
        elif product_type == ProductType.PHONE.value:
            return Phone(name, price, kwargs.get('carrier', 'Unlocked'))
        elif product_type == ProductType.TABLET.value:
            return Tablet(name, price, kwargs.get('screen_size', '10 inch'))
        else:
            raise ValueError(f"Unknown product type: {product_type}")

class ProductDecorator(Product):
    """Base decorator for products."""
    
    def __init__(self, product: Product):
        self.product = product
        super().__init__(product.name, product.base_price)
    
    def get_category(self) -> str:
        return self.product.get_category()
    
    def get_price(self) -> float:
        return self.product.get_price()

class DiscountDecorator(ProductDecorator):
    """Decorator that applies discount to product price."""
    
    def __init__(self, product: Product, discount_rate: float):
        super().__init__(product)
        self.discount_rate = discount_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 - self.discount_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Discount: {self.discount_rate*100:.0f}%)"

class TaxDecorator(ProductDecorator):
    """Decorator that applies tax to product price."""
    
    def __init__(self, product: Product, tax_rate: float):
        super().__init__(product)
        self.tax_rate = tax_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 + self.tax_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Tax: {self.tax_rate*100:.0f}%)"

class ShippingDecorator(ProductDecorator):
    """Decorator that adds shipping cost to product."""
    
    def __init__(self, product: Product, shipping_cost: float):
        super().__init__(product)
        self.shipping_cost = shipping_cost
    
    def get_price(self) -> float:
        return self.product.get_price() + self.shipping_cost
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Shipping: ${self.shipping_cost:.2f})"

# Observer Pattern Implementation
class Observer(ABC):
    """Abstract observer interface."""
    
    @abstractmethod
    def update(self, order_id: str, status: OrderStatus, message: str):
        """Update observer with order status change."""
        pass

class EmailNotifier(Observer):
    """Email notification observer."""
    
    def __init__(self, email: str = "customer@example.com"):
        self.email = email
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"📧 EMAIL to {self.email}: Order {order_id} is now {status.value.upper()}")
        if message:
            print(f"   Message: {message}")

class SMSNotifier(Observer):
    """SMS notification observer."""
    
    def __init__(self, phone: str = "+1-555-0123"):
        self.phone = phone
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"📱 SMS to {self.phone}: Order {order_id} status: {status.value.upper()}")

class PushNotifier(Observer):
    """Push notification observer."""
    
    def __init__(self, device_id: str = "device123"):
        self.device_id = device_id
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"🔔 PUSH to {self.device_id}: Order {order_id} - {status.value.upper()}")

class Subject(ABC):
    """Abstract subject interface."""
    
    @abstractmethod
    def attach(self, observer: Observer):
        """Attach an observer."""
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        """Detach an observer."""
        pass
    
    @abstractmethod
    def notify(self, message: str = ""):
        """Notify all observers."""
        pass

class Order(Subject):
    """Order class that notifies observers of status changes."""
    
    def __init__(self, order_id: str = None):
        self.order_id = order_id or f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.status = OrderStatus.PENDING
        self.products: List[Product] = []
        self.observers: List[Observer] = []
        self.total_amount = 0.0
    
    def attach(self, observer: Observer):
        """Attach an observer."""
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer."""
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self, message: str = ""):
        """Notify all observers of status change."""
        for observer in self.observers:
            observer.update(self.order_id, self.status, message)
    
    def add_product(self, product: Product):
        """Add product to order."""
        self.products.append(product)
        self.total_amount += product.get_price()
    
    def set_status(self, status: OrderStatus, message: str = ""):
        """Set order status and notify observers."""
        self.status = status
        self.notify(message)
    
    def __str__(self):
        return f"Order {self.order_id}: {len(self.products)} items, Total: ${self.total_amount:.2f}, Status: {self.status.value}"

# Strategy Pattern Implementation
class PaymentStrategy(ABC):
    """Abstract payment strategy interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process payment using this strategy."""
        pass
    
    @abstractmethod
    def get_payment_method_name(self) -> str:
        """Get the name of this payment method."""
        pass

class CreditCardStrategy(PaymentStrategy):
    """Credit card payment strategy."""
    
    def __init__(self, card_number: str = "**** **** **** 1234", cvv: str = "***"):
        self.card_number = card_number
        self.cvv = cvv
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process credit card payment."""
        print(f"💳 Processing credit card payment of ${amount:.2f}")
        print(f"   Card: {self.card_number}")
        
        # Simulate payment processing
        if amount > 0:
            transaction_id = f"CC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return PaymentResult(True, transaction_id, "Credit card payment successful")
        else:
            return PaymentResult(False, "", "Invalid amount")
    
    def get_payment_method_name(self) -> str:
        return "Credit Card"

class PayPalStrategy(PaymentStrategy):
    """PayPal payment strategy."""
    
    def __init__(self, email: str = "user@example.com"):
        self.email = email
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process PayPal payment."""
        print(f"🅿️ Processing PayPal payment of ${amount:.2f}")
        print(f"   Account: {self.email}")
        
        # Simulate payment processing
        if amount > 0:
            transaction_id = f"PP-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return PaymentResult(True, transaction_id, "PayPal payment successful")
        else:
            return PaymentResult(False, "", "Invalid amount")
    
    def get_payment_method_name(self) -> str:
        return "PayPal"

class BankTransferStrategy(PaymentStrategy):
    """Bank transfer payment strategy."""
    
    def __init__(self, account_number: str = "****1234"):
        self.account_number = account_number
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process bank transfer payment."""
        print(f"🏦 Processing bank transfer of ${amount:.2f}")
        print(f"   Account: {self.account_number}")
        
        # Simulate payment processing
        if amount > 0:
            transaction_id = f"BT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return PaymentResult(True, transaction_id, "Bank transfer initiated")
        else:
            return PaymentResult(False, "", "Invalid amount")
    
    def get_payment_method_name(self) -> str:
        return "Bank Transfer"

class PaymentContext:
    """Context class that uses payment strategies."""
    
    def __init__(self, strategy: PaymentStrategy = None):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        """Set the payment strategy."""
        self.strategy = strategy
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process payment using the current strategy."""
        if not self.strategy:
            return PaymentResult(False, "", "No payment method selected")
        
        print(f"Using {self.strategy.get_payment_method_name()} for payment")
        return self.strategy.process_payment(amount, order_id)

# What we accomplished in this step:
# - Added Strategy pattern for different payment methods
# - Created multiple payment strategies (Credit Card, PayPal, Bank Transfer)
# - PaymentContext allows switching between strategies at runtime
# - Each strategy encapsulates its own payment logic

print("=== Step 4: Strategy Pattern ===")
# Test different payment strategies
payment_context = PaymentContext()

# Test Credit Card payment
print("1. Credit Card Payment:")
payment_context.set_strategy(CreditCardStrategy("1234 5678 9012 3456"))
result = payment_context.process_payment(1350.0, "ORD-123")
print(f"Result: {result.success}, Transaction: {result.transaction_id}")
print()

# Test PayPal payment
print("2. PayPal Payment:")
payment_context.set_strategy(PayPalStrategy("john@example.com"))
result = payment_context.process_payment(1350.0, "ORD-123")
print(f"Result: {result.success}, Transaction: {result.transaction_id}")
print()

# Test Bank Transfer payment
print("3. Bank Transfer Payment:")
payment_context.set_strategy(BankTransferStrategy("ACC-9876"))
result = payment_context.process_payment(1350.0, "ORD-123")
print(f"Result: {result.success}, Transaction: {result.transaction_id}")
print()


# Step 5: Add Command Pattern for order operations
# ===============================================================================

# Explanation:
# The Command pattern encapsulates order operations (place, cancel, modify)
# as objects, allowing for undo/redo functionality and operation queuing.

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from enum import Enum
from datetime import datetime

class ProductType(Enum):
    """Enumeration of product types."""
    LAPTOP = "laptop"
    PHONE = "phone"
    TABLET = "tablet"
    ACCESSORY = "accessory"

class OrderStatus(Enum):
    """Enumeration of order statuses."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class PaymentResult:
    """Result of a payment transaction."""
    
    def __init__(self, success: bool, transaction_id: str = "", message: str = ""):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message
        self.timestamp = datetime.now()

class Product(ABC):
    """Abstract base class for all products."""
    
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.product_id = id(self)
    
    @abstractmethod
    def get_category(self) -> str:
        """Get product category."""
        pass
    
    def get_price(self) -> float:
        """Get current price (can be modified by decorators)."""
        return self.base_price
    
    def __str__(self):
        return f"{self.get_category()}: {self.name} - ${self.get_price():.2f}"

class Laptop(Product):
    """Concrete laptop product."""
    
    def __init__(self, name: str, base_price: float, specs: Dict[str, str] = None):
        super().__init__(name, base_price)
        self.specs = specs or {}
    
    def get_category(self) -> str:
        return "Laptop"

class Phone(Product):
    """Concrete phone product."""
    
    def __init__(self, name: str, base_price: float, carrier: str = "Unlocked"):
        super().__init__(name, base_price)
        self.carrier = carrier
    
    def get_category(self) -> str:
        return "Phone"

class Tablet(Product):
    """Concrete tablet product."""
    
    def __init__(self, name: str, base_price: float, screen_size: str = "10 inch"):
        super().__init__(name, base_price)
        self.screen_size = screen_size
    
    def get_category(self) -> str:
        return "Tablet"

class ProductFactory:
    """Factory for creating different product types."""
    
    @staticmethod
    def create_product(product_type: str, name: str, price: float, **kwargs) -> Product:
        """Create a product based on type."""
        product_type = product_type.lower()
        
        if product_type == ProductType.LAPTOP.value:
            return Laptop(name, price, kwargs.get('specs', {}))
        elif product_type == ProductType.PHONE.value:
            return Phone(name, price, kwargs.get('carrier', 'Unlocked'))
        elif product_type == ProductType.TABLET.value:
            return Tablet(name, price, kwargs.get('screen_size', '10 inch'))
        else:
            raise ValueError(f"Unknown product type: {product_type}")

class ProductDecorator(Product):
    """Base decorator for products."""
    
    def __init__(self, product: Product):
        self.product = product
        super().__init__(product.name, product.base_price)
    
    def get_category(self) -> str:
        return self.product.get_category()
    
    def get_price(self) -> float:
        return self.product.get_price()

class DiscountDecorator(ProductDecorator):
    """Decorator that applies discount to product price."""
    
    def __init__(self, product: Product, discount_rate: float):
        super().__init__(product)
        self.discount_rate = discount_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 - self.discount_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Discount: {self.discount_rate*100:.0f}%)"

class TaxDecorator(ProductDecorator):
    """Decorator that applies tax to product price."""
    
    def __init__(self, product: Product, tax_rate: float):
        super().__init__(product)
        self.tax_rate = tax_rate
    
    def get_price(self) -> float:
        original_price = self.product.get_price()
        return original_price * (1 + self.tax_rate)
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Tax: {self.tax_rate*100:.0f}%)"

class ShippingDecorator(ProductDecorator):
    """Decorator that adds shipping cost to product."""
    
    def __init__(self, product: Product, shipping_cost: float):
        super().__init__(product)
        self.shipping_cost = shipping_cost
    
    def get_price(self) -> float:
        return self.product.get_price() + self.shipping_cost
    
    def __str__(self):
        return f"{self.product.get_category()}: {self.name} - ${self.get_price():.2f} (Shipping: ${self.shipping_cost:.2f})"

# Observer Pattern Implementation
class Observer(ABC):
    """Abstract observer interface."""
    
    @abstractmethod
    def update(self, order_id: str, status: OrderStatus, message: str):
        """Update observer with order status change."""
        pass

class EmailNotifier(Observer):
    """Email notification observer."""
    
    def __init__(self, email: str = "customer@example.com"):
        self.email = email
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"📧 EMAIL to {self.email}: Order {order_id} is now {status.value.upper()}")
        if message:
            print(f"   Message: {message}")

class SMSNotifier(Observer):
    """SMS notification observer."""
    
    def __init__(self, phone: str = "+1-555-0123"):
        self.phone = phone
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"📱 SMS to {self.phone}: Order {order_id} status: {status.value.upper()}")

class PushNotifier(Observer):
    """Push notification observer."""
    
    def __init__(self, device_id: str = "device123"):
        self.device_id = device_id
    
    def update(self, order_id: str, status: OrderStatus, message: str):
        print(f"🔔 PUSH to {self.device_id}: Order {order_id} - {status.value.upper()}")

class Subject(ABC):
    """Abstract subject interface."""
    
    @abstractmethod
    def attach(self, observer: Observer):
        """Attach an observer."""
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        """Detach an observer."""
        pass
    
    @abstractmethod
    def notify(self, message: str = ""):
        """Notify all observers."""
        pass

class Order(Subject):
    """Order class that notifies observers of status changes."""
    
    def __init__(self, order_id: str = None):
        self.order_id = order_id or f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.status = OrderStatus.PENDING
        self.products: List[Product] = []
        self.observers: List[Observer] = []
        self.total_amount = 0.0
        self.previous_status = None
        self.previous_products = []
        self.previous_total = 0.0
    
    def attach(self, observer: Observer):
        """Attach an observer."""
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer."""
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self, message: str = ""):
        """Notify all observers of status change."""
        for observer in self.observers:
            observer.update(self.order_id, self.status, message)
    
    def add_product(self, product: Product):
        """Add product to order."""
        self.products.append(product)
        self.total_amount += product.get_price()
    
    def remove_product(self, product: Product):
        """Remove product from order."""
        if product in self.products:
            self.products.remove(product)
            self.total_amount -= product.get_price()
    
    def save_state(self):
        """Save current state for undo operations."""
        self.previous_status = self.status
        self.previous_products = self.products.copy()
        self.previous_total = self.total_amount
    
    def restore_state(self):
        """Restore previous state for undo operations."""
        if self.previous_status is not None:
            self.status = self.previous_status
            self.products = self.previous_products.copy()
            self.total_amount = self.previous_total
    
    def set_status(self, status: OrderStatus, message: str = ""):
        """Set order status and notify observers."""
        self.status = status
        self.notify(message)
    
    def __str__(self):
        return f"Order {self.order_id}: {len(self.products)} items, Total: ${self.total_amount:.2f}, Status: {self.status.value}"

# Strategy Pattern Implementation
class PaymentStrategy(ABC):
    """Abstract payment strategy interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process payment using this strategy."""
        pass
    
    @abstractmethod
    def get_payment_method_name(self) -> str:
        """Get the name of this payment method."""
        pass

class CreditCardStrategy(PaymentStrategy):
    """Credit card payment strategy."""
    
    def __init__(self, card_number: str = "**** **** **** 1234", cvv: str = "***"):
        self.card_number = card_number
        self.cvv = cvv
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process credit card payment."""
        print(f"💳 Processing credit card payment of ${amount:.2f}")
        print(f"   Card: {self.card_number}")
        
        # Simulate payment processing
        if amount > 0:
            transaction_id = f"CC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return PaymentResult(True, transaction_id, "Credit card payment successful")
        else:
            return PaymentResult(False, "", "Invalid amount")
    
    def get_payment_method_name(self) -> str:
        return "Credit Card"

class PayPalStrategy(PaymentStrategy):
    """PayPal payment strategy."""
    
    def __init__(self, email: str = "user@example.com"):
        self.email = email
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process PayPal payment."""
        print(f"🅿️ Processing PayPal payment of ${amount:.2f}")
        print(f"   Account: {self.email}")
        
        # Simulate payment processing
        if amount > 0:
            transaction_id = f"PP-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return PaymentResult(True, transaction_id, "PayPal payment successful")
        else:
            return PaymentResult(False, "", "Invalid amount")
    
    def get_payment_method_name(self) -> str:
        return "PayPal"

class BankTransferStrategy(PaymentStrategy):
    """Bank transfer payment strategy."""
    
    def __init__(self, account_number: str = "****1234"):
        self.account_number = account_number
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process bank transfer payment."""
        print(f"🏦 Processing bank transfer of ${amount:.2f}")
        print(f"   Account: {self.account_number}")
        
        # Simulate payment processing
        if amount > 0:
            transaction_id = f"BT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            return PaymentResult(True, transaction_id, "Bank transfer initiated")
        else:
            return PaymentResult(False, "", "Invalid amount")
    
    def get_payment_method_name(self) -> str:
        return "Bank Transfer"

class PaymentContext:
    """Context class that uses payment strategies."""
    
    def __init__(self, strategy: PaymentStrategy = None):
        self.strategy = strategy
    
    def set_strategy(self, strategy: PaymentStrategy):
        """Set the payment strategy."""
        self.strategy = strategy
    
    def process_payment(self, amount: float, order_id: str) -> PaymentResult:
        """Process payment using the current strategy."""
        if not self.strategy:
            return PaymentResult(False, "", "No payment method selected")
        
        print(f"Using {self.strategy.get_payment_method_name()} for payment")
        return self.strategy.process_payment(amount, order_id)

# Command Pattern Implementation
class Command(ABC):
    """Abstract command interface."""
    
    @abstractmethod
    def execute(self) -> bool:
        """Execute the command."""
        pass
    
    @abstractmethod
    def undo(self) -> bool:
        """Undo the command."""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Get command description."""
        pass

class PlaceOrderCommand(Command):
    """Command to place an order."""
    
    def __init__(self, order: Order, product: Product, payment_context: PaymentContext):
        self.order = order
        self.product = product
        self.payment_context = payment_context
        self.executed = False
        self.payment_result = None
    
    def execute(self) -> bool:
        """Execute place order command."""
        if self.executed:
            return False
        
        print(f"🛒 Placing order for {self.product}")
        self.order.save_state()
        self.order.add_product(self.product)
        
        # Process payment
        self.payment_result = self.payment_context.process_payment(
            self.product.get_price(), self.order.order_id
        )
        
        if self.payment_result.success:
            self.order.set_status(OrderStatus.CONFIRMED, "Order placed successfully")
            self.executed = True
            return True
        else:
            self.order.restore_state()
            print(f"❌ Order placement failed: {self.payment_result.message}")
            return False
    
    def undo(self) -> bool:
        """Undo place order command."""
        if not self.executed:
            return False
        
        print(f"↩️ Undoing order placement for {self.product}")
        self.order.remove_product(self.product)
        self.order.set_status(OrderStatus.CANCELLED, "Order cancelled")
        self.executed = False
        return True
    
    def get_description(self) -> str:
        return f"Place order for {self.product.name}"

class CancelOrderCommand(Command):
    """Command to cancel an order."""
    
    def __init__(self, order: Order):
        self.order = order
        self.executed = False
        self.previous_status = None
    
    def execute(self) -> bool:
        """Execute cancel order command."""
        if self.executed or self.order.status == OrderStatus.CANCELLED:
            return False
        
        print(f"❌ Cancelling order {self.order.order_id}")
        self.previous_status = self.order.status
        self.order.set_status(OrderStatus.CANCELLED, "Order cancelled by customer")
        self.executed = True
        return True
    
    def undo(self) -> bool:
        """Undo cancel order command."""
        if not self.executed:
            return False
        
        print(f"↩️ Restoring order {self.order.order_id}")
        self.order.set_status(self.previous_status, "Order restored")
        self.executed = False
        return True
    
    def get_description(self) -> str:
        return f"Cancel order {self.order.order_id}"

class ModifyOrderCommand(Command):
    """Command to modify an order by adding/removing products."""
    
    def __init__(self, order: Order, product: Product, action: str = "add"):
        self.order = order
        self.product = product
        self.action = action  # "add" or "remove"
        self.executed = False
    
    def execute(self) -> bool:
        """Execute modify order command."""
        if self.executed:
            return False
        
        self.order.save_state()
        
        if self.action == "add":
            print(f"➕ Adding {self.product} to order")
            self.order.add_product(self.product)
        elif self.action == "remove":
            print(f"➖ Removing {self.product} from order")
            self.order.remove_product(self.product)
        else:
            return False
        
        self.order.set_status(OrderStatus.PENDING, "Order modified")
        self.executed = True
        return True
    
    def undo(self) -> bool:
        """Undo modify order command."""
        if not self.executed:
            return False
        
        print(f"↩️ Undoing order modification")
        self.order.restore_state()
        self.executed = False
        return True
    
    def get_description(self) -> str:
        return f"{self.action.title()} {self.product.name} to/from order"

class OrderInvoker:
    """Invoker that executes and manages commands."""
    
    def __init__(self):
        self.command_history: List[Command] = []
        self.current_position = -1
    
    def execute_command(self, command: Command) -> bool:
        """Execute a command and add it to history."""
        if command.execute():
            # Remove any commands after current position (for redo functionality)
            self.command_history = self.command_history[:self.current_position + 1]
            self.command_history.append(command)
            self.current_position += 1
            print(f"✅ Executed: {command.get_description()}")
            return True
        else:
            print(f"❌ Failed to execute: {command.get_description()}")
            return False
    
    def undo(self) -> bool:
        """Undo the last command."""
        if self.current_position >= 0:
            command = self.command_history[self.current_position]
            if command.undo():
                self.current_position -= 1
                print(f"↩️ Undone: {command.get_description()}")
                return True
        print("❌ Nothing to undo")
        return False
    
    def redo(self) -> bool:
        """Redo the next command."""
        if self.current_position < len(self.command_history) - 1:
            self.current_position += 1
            command = self.command_history[self.current_position]
            if command.execute():
                print(f"↪️ Redone: {command.get_description()}")
                return True
        print("❌ Nothing to redo")
        return False
    
    def get_command_history(self) -> List[str]:
        """Get the command history."""
        return [cmd.get_description() for cmd in self.command_history]

# What we accomplished in this step:
# - Added Command pattern for order operations
# - Created commands for place, cancel, and modify operations
# - Added undo/redo functionality through OrderInvoker
# - Commands encapsulate operations and their reversal logic

print("=== Step 5: Command Pattern ===")
# Create order system with command pattern
order = Order()
email_notifier = EmailNotifier("customer@example.com")
order.attach(email_notifier)

# Create payment context
payment_context = PaymentContext()
payment_context.set_strategy(CreditCardStrategy())

# Create products
factory = ProductFactory()
laptop = factory.create_product("laptop", "Gaming Laptop", 1500.0)
discounted_laptop = DiscountDecorator(laptop, 0.1)
phone = factory.create_product("phone", "Smartphone", 800.0)

# Create command invoker
invoker = OrderInvoker()

# Execute commands
place_laptop_cmd = PlaceOrderCommand(order, discounted_laptop, payment_context)
invoker.execute_command(place_laptop_cmd)

modify_add_phone_cmd = ModifyOrderCommand(order, phone, "add")
invoker.execute_command(modify_add_phone_cmd)

print(f"\nCurrent order: {order}")

# Test undo functionality
print("\n--- Testing Undo/Redo ---")
invoker.undo()  # Undo adding phone
print(f"After undo: {order}")

invoker.redo()  # Redo adding phone
print(f"After redo: {order}")

cancel_cmd = CancelOrderCommand(order)
invoker.execute_command(cancel_cmd)

print(f"Command history: {invoker.get_command_history()}")
print()


# Step 6: Add Singleton Pattern for system configuration
# ===============================================================================

# Explanation:
# The Singleton pattern ensures only one instance of system configuration
# exists throughout the application, providing global access to settings.

import threading

class SystemConfig:
    """Singleton class for system configuration."""
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(SystemConfig, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.settings = {
                'tax_rate': 0.08,
                'shipping_cost': 50.0,
                'currency': 'USD',
                'max_order_items': 10,
                'notification_enabled': True,
                'payment_timeout': 300,  # seconds
                'discount_threshold': 1000.0,  # minimum amount for discount eligibility
                'system_name': 'E-Commerce System',
                'version': '1.0.0'
            }
            self._initialized = True
    
    def get_setting(self, key: str, default=None):
        """Get a configuration setting."""
        return self.settings.get(key, default)
    
    def set_setting(self, key: str, value):
        """Set a configuration setting."""
        self.settings[key] = value
    
    def get_all_settings(self) -> Dict[str, Any]:
        """Get all configuration settings."""
        return self.settings.copy()
    
    def __str__(self):
        return f"SystemConfig({self.settings['system_name']} v{self.settings['version']})"


# Step 7: Add Facade Pattern to simplify complex subsystem interactions
# ===============================================================================

# Explanation:
# The Facade pattern provides a simplified interface to the complex e-commerce
# subsystem, hiding the complexity of multiple patterns working together.

class ECommerceFacade:
    """Facade that simplifies the e-commerce system interactions."""
    
    def __init__(self):
        self.config = SystemConfig()
        self.product_factory = ProductFactory()
        self.order_invoker = OrderInvoker()
        self.payment_context = PaymentContext()
        
        # Default observers for all orders
        self.default_observers = [
            EmailNotifier(),
            SMSNotifier(),
            PushNotifier()
        ]
    
    def create_customer_order(self, customer_email: str = "customer@example.com") -> Order:
        """Create a new order for a customer."""
        order = Order()
        
        # Attach default observers
        email_notifier = EmailNotifier(customer_email)
        order.attach(email_notifier)
        
        if self.config.get_setting('notification_enabled'):
            for observer in self.default_observers[1:]:  # Skip default email, use customer's
                order.attach(observer)
        
        return order
    
    def purchase_product(self, product_type: str, product_name: str, base_price: float,
                        payment_method: str = "credit_card", customer_email: str = "customer@example.com",
                        apply_discount: bool = False, **product_kwargs) -> Dict[str, Any]:
        """
        Complete product purchase workflow using facade pattern.
        
        This method demonstrates how all patterns work together:
        - Factory creates the product
        - Decorator applies pricing modifications
        - Observer notifies about order status
        - Strategy handles payment processing
        - Command encapsulates the order operation
        - Singleton provides configuration
        """
        
        try:
            print(f"🏪 {self.config.get_setting('system_name')} - Processing Purchase")
            print("=" * 60)
            
            # Step 1: Create product using Factory pattern
            print("1️⃣ Creating product...")
            product = self.product_factory.create_product(product_type, product_name, base_price, **product_kwargs)
            print(f"   Created: {product}")
            
            # Step 2: Apply pricing decorators
            print("\n2️⃣ Applying pricing...")
            final_product = product
            
            # Apply discount if eligible
            if apply_discount and base_price >= self.config.get_setting('discount_threshold'):
                final_product = DiscountDecorator(final_product, 0.1)  # 10% discount
                print(f"   Discount applied: {final_product}")
            
            # Apply tax from configuration
            tax_rate = self.config.get_setting('tax_rate')
            final_product = TaxDecorator(final_product, tax_rate)
            print(f"   Tax applied: {final_product}")
            
            # Apply shipping
            shipping_cost = self.config.get_setting('shipping_cost')
            final_product = ShippingDecorator(final_product, shipping_cost)
            print(f"   Shipping added: {final_product}")
            
            # Step 3: Create order with Observer pattern
            print("\n3️⃣ Creating order with notifications...")
            order = self.create_customer_order(customer_email)
            print(f"   Order created: {order}")
            
            # Step 4: Set up payment strategy
            print("\n4️⃣ Setting up payment...")
            if payment_method.lower() == "credit_card":
                self.payment_context.set_strategy(CreditCardStrategy())
            elif payment_method.lower() == "paypal":
                self.payment_context.set_strategy(PayPalStrategy(customer_email))
            elif payment_method.lower() == "bank_transfer":
                self.payment_context.set_strategy(BankTransferStrategy())
            else:
                raise ValueError(f"Unsupported payment method: {payment_method}")
            
            # Step 5: Execute order using Command pattern
            print("\n5️⃣ Processing order...")
            place_order_cmd = PlaceOrderCommand(order, final_product, self.payment_context)
            success = self.order_invoker.execute_command(place_order_cmd)
            
            if success:
                print("\n✅ Purchase completed successfully!")
                return {
                    'success': True,
                    'order_id': order.order_id,
                    'total_amount': final_product.get_price(),
                    'status': order.status.value,
                    'message': 'Purchase completed successfully'
                }
            else:
                print("\n❌ Purchase failed!")
                return {
                    'success': False,
                    'order_id': order.order_id,
                    'total_amount': 0.0,
                    'status': 'failed',
                    'message': 'Payment processing failed'
                }
                
        except Exception as e:
            print(f"\n💥 Error during purchase: {str(e)}")
            return {
                'success': False,
                'order_id': None,
                'total_amount': 0.0,
                'status': 'error',
                'message': f'Error: {str(e)}'
            }
    
    def cancel_order(self, order: Order) -> bool:
        """Cancel an existing order."""
        print(f"🚫 Cancelling order {order.order_id}")
        cancel_cmd = CancelOrderCommand(order)
        return self.order_invoker.execute_command(cancel_cmd)
    
    def modify_order(self, order: Order, product: Product, action: str = "add") -> bool:
        """Modify an existing order."""
        print(f"✏️ Modifying order {order.order_id}")
        modify_cmd = ModifyOrderCommand(order, product, action)
        return self.order_invoker.execute_command(modify_cmd)
    
    def undo_last_operation(self) -> bool:
        """Undo the last operation."""
        return self.order_invoker.undo()
    
    def redo_last_operation(self) -> bool:
        """Redo the last operation."""
        return self.order_invoker.redo()
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get system information."""
        return {
            'config': self.config.get_all_settings(),
            'command_history': self.order_invoker.get_command_history()
        }

# What we accomplished in Steps 6-7:
# - Added Singleton pattern for centralized system configuration
# - Created Facade pattern that unifies all other patterns
# - Demonstrated how all patterns work together harmoniously
# - Provided simple interface for complex e-commerce operations

print("=== Step 6: Singleton Pattern ===")
# Test Singleton pattern
config1 = SystemConfig()
config2 = SystemConfig()
print(f"Same instance: {config1 is config2}")
print(f"Config: {config1}")
print(f"Tax rate: {config1.get_setting('tax_rate')}")
print()

print("=== Step 7: Facade Pattern - Complete Integration ===")
# Test the complete system using Facade
ecommerce = ECommerceFacade()

# Purchase 1: Laptop with discount
print("🛍️ Purchase 1: High-end laptop")
result1 = ecommerce.purchase_product(
    product_type="laptop",
    product_name="Gaming Laptop Pro",
    base_price=1500.0,
    payment_method="credit_card",
    customer_email="gamer@example.com",
    apply_discount=True,
    specs={"CPU": "Intel i9", "RAM": "32GB", "GPU": "RTX 4080"}
)
print(f"Result: {result1}")
print()

# Purchase 2: Phone with PayPal
print("🛍️ Purchase 2: Smartphone")
result2 = ecommerce.purchase_product(
    product_type="phone",
    product_name="iPhone 15 Pro",
    base_price=999.0,
    payment_method="paypal",
    customer_email="user@example.com",
    carrier="Verizon"
)
print(f"Result: {result2}")
print()

# Show system information
print("📊 System Information:")
system_info = ecommerce.get_system_info()
print(f"Configuration: {system_info['config']['system_name']} v{system_info['config']['version']}")
print(f"Command History: {system_info['command_history']}")
print()


# Final Step: Complete demonstration showing all patterns working together
# ===============================================================================

print("=== 🎯 FINAL DEMONSTRATION: All Patterns Working Together ===")
print()

# Create a comprehensive example
facade = ECommerceFacade()

# Scenario: Customer wants to buy multiple items
print("📱 Customer John wants to buy a laptop and phone...")

# Create products using Factory
laptop = facade.product_factory.create_product("laptop", "MacBook Pro", 2500.0)
phone = facade.product_factory.create_product("phone", "iPhone 15", 1200.0)

# Apply decorators for pricing
discounted_laptop = DiscountDecorator(laptop, 0.15)  # 15% discount
final_laptop = TaxDecorator(discounted_laptop, 0.08)  # 8% tax

# Create order with observers
order = facade.create_customer_order("john@example.com")

# Set payment strategy
facade.payment_context.set_strategy(CreditCardStrategy("1234-5678-9012-3456"))

# Use commands to build the order
print("\n1. Adding laptop to order...")
place_laptop_cmd = PlaceOrderCommand(order, final_laptop, facade.payment_context)
facade.order_invoker.execute_command(place_laptop_cmd)

print("\n2. Adding phone to order...")
modify_add_phone_cmd = ModifyOrderCommand(order, phone, "add")
facade.order_invoker.execute_command(modify_add_phone_cmd)

print(f"\n📦 Final Order: {order}")

print("\n3. Customer changes mind about phone...")
facade.order_invoker.undo()  # Remove phone

print("\n4. Customer decides to add phone back...")
facade.order_invoker.redo()  # Add phone back

print(f"\n🎉 Order Complete: {order}")
print(f"💰 Total Amount: ${order.total_amount:.2f}")

# Show how Singleton maintains consistent configuration
config = SystemConfig()
print(f"\n⚙️ System Config: {config.get_setting('system_name')} v{config.get_setting('version')}")
print(f"💸 Tax Rate: {config.get_setting('tax_rate')*100}%")
print(f"🚚 Shipping: ${config.get_setting('shipping_cost')}")

print("\n" + "="*80)
print("🏆 CONGRATULATIONS! You've successfully implemented and integrated:")
print("   ✅ Factory Pattern - Product creation")
print("   ✅ Decorator Pattern - Pricing features")
print("   ✅ Observer Pattern - Order notifications")
print("   ✅ Strategy Pattern - Payment methods")
print("   ✅ Command Pattern - Order operations with undo/redo")
print("   ✅ Singleton Pattern - System configuration")
print("   ✅ Facade Pattern - Simplified interface")
print("="*80)
print()