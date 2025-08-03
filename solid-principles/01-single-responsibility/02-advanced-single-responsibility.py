"""Question: Create a class Order that handles order processing and payment.
Refactor the class to adhere to the Single Responsibility Principle
by separating order processing from payment processing.
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what classes and methods you need
# - Start with a simple implementation
# - Test your code step by step
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What are the different responsibilities in the Order class?
# - How can you separate order processing from payment processing?
# - What are the benefits of having separate classes for orders and payments?
# - How might different payment methods or order types affect the design?
#
# Remember: Start simple and build up complexity gradually!


# ===============================================================================
#                           STEP-BY-STEP SOLUTION
# ===============================================================================
#
# CLASSROOM-STYLE WALKTHROUGH
#
# Let's solve this problem step by step, just like in a programming class!
# Each step builds upon the previous one, so you can follow along and understand
# the complete thought process.
#
# ===============================================================================


# Step 1: Identify the SRP violation in the original Order class
# ===============================================================================

# Explanation:
# Let's examine the original Order class that violates SRP by handling
# both order processing AND payment processing responsibilities.

class Order:
    def __init__(self, items, payment_method):
        self.items = items
        self.payment_method = payment_method

    def process_order(self):
        # Process order items
        total = sum(item['price'] for item in self.items)
        print(f"Processing order with {len(self.items)} items, total: ${total}")
        return total

    def process_payment(self):
        # Process payment
        print(f"Processing payment via {self.payment_method}")
        return "Payment successful"

# What we can observe:
# - The Order class has TWO responsibilities:
#   1. Managing order items and processing (process_order)
#   2. Handling payment processing (process_payment)
# - This violates SRP because the class has multiple reasons to change

print("=== Original Order Class (SRP Violation) ===")
items = [{"name": "Laptop", "price": 999}, {"name": "Mouse", "price": 25}]
order = Order(items, "credit_card")
total = order.process_order()
payment_result = order.process_payment()
print(f"Total: ${total}, Payment: {payment_result}")


# Step 2: Create OrderProcessor class for order management
# ===============================================================================

# Explanation:
# Let's create an OrderProcessor class that only handles order-related logic,
# separating it from payment concerns.

class OrderProcessor:
    def __init__(self, items):
        self.items = items
        self.order_id = self._generate_order_id()

    def process_order(self):
        total = self._calculate_total()
        self._validate_items()
        print(f"Order {self.order_id}: Processing {len(self.items)} items, total: ${total}")
        return {"order_id": self.order_id, "total": total, "status": "processed"}

    def _calculate_total(self):
        return sum(item['price'] for item in self.items)

    def _validate_items(self):
        for item in self.items:
            if item['price'] <= 0:
                raise ValueError(f"Invalid price for item: {item['name']}")

    def _generate_order_id(self):
        import random
        return f"ORD-{random.randint(1000, 9999)}"

    def get_order_summary(self):
        return {
            "order_id": self.order_id,
            "items": self.items,
            "total": self._calculate_total()
        }

# What we accomplished in this step:
# - OrderProcessor class focuses only on order management
# - Added order validation and ID generation
# - Removed any payment-related logic


# Step 3: Create PaymentProcessor class for payment handling
# ===============================================================================

# Explanation:
# Now let's create a PaymentProcessor class that only handles payment processing,
# following the SRP by giving it a single responsibility.

class OrderProcessor:
    def __init__(self, items):
        self.items = items
        self.order_id = self._generate_order_id()

    def process_order(self):
        total = self._calculate_total()
        self._validate_items()
        print(f"Order {self.order_id}: Processing {len(self.items)} items, total: ${total}")
        return {"order_id": self.order_id, "total": total, "status": "processed"}

    def _calculate_total(self):
        return sum(item['price'] for item in self.items)

    def _validate_items(self):
        for item in self.items:
            if item['price'] <= 0:
                raise ValueError(f"Invalid price for item: {item['name']}")

    def _generate_order_id(self):
        import random
        return f"ORD-{random.randint(1000, 9999)}"

    def get_order_summary(self):
        return {
            "order_id": self.order_id,
            "items": self.items,
            "total": self._calculate_total()
        }

class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        self.transaction_id = None

    def process_payment(self, amount):
        self._validate_payment_method()
        self.transaction_id = self._generate_transaction_id()
        
        if self._simulate_payment(amount):
            print(f"Payment of ${amount} processed via {self.payment_method}")
            return {"transaction_id": self.transaction_id, "status": "success", "amount": amount}
        else:
            return {"transaction_id": self.transaction_id, "status": "failed", "amount": amount}

    def _validate_payment_method(self):
        valid_methods = ["credit_card", "debit_card", "paypal", "bank_transfer"]
        if self.payment_method not in valid_methods:
            raise ValueError(f"Invalid payment method: {self.payment_method}")

    def _simulate_payment(self, amount):
        # Simulate payment processing (always succeeds for demo)
        return amount > 0

    def _generate_transaction_id(self):
        import random
        return f"TXN-{random.randint(10000, 99999)}"

# What we accomplished in this step:
# - Created PaymentProcessor class with single responsibility: payment handling
# - Separated concerns: OrderProcessor handles orders, PaymentProcessor handles payments
# - Each class now has only one reason to change


# Step 4: Test our SRP-compliant design
# ===============================================================================

# Explanation:
# Let's test our refactored design to ensure it works correctly and
# demonstrates the benefits of following SRP.

class OrderProcessor:
    def __init__(self, items):
        self.items = items
        self.order_id = self._generate_order_id()

    def process_order(self):
        total = self._calculate_total()
        self._validate_items()
        print(f"Order {self.order_id}: Processing {len(self.items)} items, total: ${total}")
        return {"order_id": self.order_id, "total": total, "status": "processed"}

    def _calculate_total(self):
        return sum(item['price'] for item in self.items)

    def _validate_items(self):
        for item in self.items:
            if item['price'] <= 0:
                raise ValueError(f"Invalid price for item: {item['name']}")

    def _generate_order_id(self):
        import random
        return f"ORD-{random.randint(1000, 9999)}"

    def get_order_summary(self):
        return {
            "order_id": self.order_id,
            "items": self.items,
            "total": self._calculate_total()
        }

class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        self.transaction_id = None

    def process_payment(self, amount):
        self._validate_payment_method()
        self.transaction_id = self._generate_transaction_id()
        
        if self._simulate_payment(amount):
            print(f"Payment of ${amount} processed via {self.payment_method}")
            return {"transaction_id": self.transaction_id, "status": "success", "amount": amount}
        else:
            return {"transaction_id": self.transaction_id, "status": "failed", "amount": amount}

    def _validate_payment_method(self):
        valid_methods = ["credit_card", "debit_card", "paypal", "bank_transfer"]
        if self.payment_method not in valid_methods:
            raise ValueError(f"Invalid payment method: {self.payment_method}")

    def _simulate_payment(self, amount):
        # Simulate payment processing (always succeeds for demo)
        return amount > 0

    def _generate_transaction_id(self):
        import random
        return f"TXN-{random.randint(10000, 99999)}"

# Test our SRP-compliant design:
print("\n=== SRP-Compliant Design ===")

items = [{"name": "Laptop", "price": 999}, {"name": "Mouse", "price": 25}]

# Process order
order_processor = OrderProcessor(items)
order_result = order_processor.process_order()
print(f"Order result: {order_result}")

# Process payment
payment_processor = PaymentProcessor("credit_card")
payment_result = payment_processor.process_payment(order_result["total"])
print(f"Payment result: {payment_result}")

# Test with different payment method
paypal_processor = PaymentProcessor("paypal")
paypal_result = paypal_processor.process_payment(order_result["total"])
print(f"PayPal result: {paypal_result}")

# What we accomplished in this step:
# - Demonstrated that our refactored design works correctly
# - Showed how OrderProcessor and PaymentProcessor can be used independently
# - Verified that we can easily use different payment methods


# Step 5: Enhanced example with order management system
# ===============================================================================

# Explanation:
# Let's create a comprehensive example that shows the benefits of SRP
# by building a complete order management system.

class OrderProcessor:
    def __init__(self, items, customer_id):
        self.items = items
        self.customer_id = customer_id
        self.order_id = self._generate_order_id()
        self.status = "pending"
        self.created_at = self._get_timestamp()

    def process_order(self):
        self._validate_items()
        total = self._calculate_total()
        tax = self._calculate_tax(total)
        final_total = total + tax
        
        self.status = "processed"
        print(f"Order {self.order_id}: Processed for customer {self.customer_id}")
        
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "subtotal": total,
            "tax": tax,
            "total": final_total,
            "status": self.status,
            "created_at": self.created_at
        }

    def cancel_order(self):
        if self.status == "pending":
            self.status = "cancelled"
            return True
        return False

    def _calculate_total(self):
        return sum(item['price'] * item.get('quantity', 1) for item in self.items)

    def _calculate_tax(self, subtotal):
        return round(subtotal * 0.08, 2)  # 8% tax

    def _validate_items(self):
        for item in self.items:
            if item['price'] <= 0:
                raise ValueError(f"Invalid price for item: {item['name']}")
            if item.get('quantity', 1) <= 0:
                raise ValueError(f"Invalid quantity for item: {item['name']}")

    def _generate_order_id(self):
        import random
        return f"ORD-{random.randint(1000, 9999)}"

    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().isoformat()

class PaymentProcessor:
    def __init__(self, payment_method, gateway="default"):
        self.payment_method = payment_method
        self.gateway = gateway
        self.transaction_history = []

    def process_payment(self, amount, order_id=None):
        self._validate_payment_method()
        transaction_id = self._generate_transaction_id()
        
        # Simulate different payment processing based on method
        success = self._simulate_payment_gateway(amount)
        
        transaction = {
            "transaction_id": transaction_id,
            "order_id": order_id,
            "amount": amount,
            "payment_method": self.payment_method,
            "gateway": self.gateway,
            "status": "success" if success else "failed",
            "timestamp": self._get_timestamp()
        }
        
        self.transaction_history.append(transaction)
        
        if success:
            print(f"Payment ${amount} successful via {self.payment_method} (TXN: {transaction_id})")
        else:
            print(f"Payment ${amount} failed via {self.payment_method} (TXN: {transaction_id})")
        
        return transaction

    def refund_payment(self, transaction_id, amount):
        # Find original transaction
        original = next((t for t in self.transaction_history if t["transaction_id"] == transaction_id), None)
        if not original or original["status"] != "success":
            return {"status": "failed", "message": "Original transaction not found or not successful"}
        
        refund_id = self._generate_transaction_id()
        refund = {
            "transaction_id": refund_id,
            "original_transaction_id": transaction_id,
            "amount": -amount,  # Negative amount for refund
            "payment_method": self.payment_method,
            "gateway": self.gateway,
            "status": "refunded",
            "timestamp": self._get_timestamp()
        }
        
        self.transaction_history.append(refund)
        print(f"Refund ${amount} processed for transaction {transaction_id}")
        return refund

    def _validate_payment_method(self):
        valid_methods = ["credit_card", "debit_card", "paypal", "bank_transfer", "apple_pay"]
        if self.payment_method not in valid_methods:
            raise ValueError(f"Invalid payment method: {self.payment_method}")

    def _simulate_payment_gateway(self, amount):
        # Simulate different success rates for different methods
        import random
        if self.payment_method == "credit_card":
            return random.random() > 0.05  # 95% success rate
        elif self.payment_method == "paypal":
            return random.random() > 0.02  # 98% success rate
        else:
            return random.random() > 0.1   # 90% success rate

    def _generate_transaction_id(self):
        import random
        return f"TXN-{random.randint(10000, 99999)}"

    def _get_timestamp(self):
        import datetime
        return datetime.datetime.now().isoformat()

    def get_transaction_history(self):
        return self.transaction_history

class OrderManagementSystem:
    def __init__(self):
        self.orders = {}
        self.payments = {}

    def create_order(self, items, customer_id, payment_method):
        # Create order
        order_processor = OrderProcessor(items, customer_id)
        order_result = order_processor.process_order()
        
        # Process payment
        payment_processor = PaymentProcessor(payment_method)
        payment_result = payment_processor.process_payment(
            order_result["total"], 
            order_result["order_id"]
        )
        
        # Store order and payment info
        self.orders[order_result["order_id"]] = {
            "processor": order_processor,
            "details": order_result
        }
        
        self.payments[payment_result["transaction_id"]] = {
            "processor": payment_processor,
            "details": payment_result
        }
        
        return {
            "order": order_result,
            "payment": payment_result
        }

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def cancel_order(self, order_id):
        if order_id in self.orders:
            order_info = self.orders[order_id]
            if order_info["processor"].cancel_order():
                # Find and refund payment
                for payment_id, payment_info in self.payments.items():
                    if payment_info["details"]["order_id"] == order_id:
                        payment_info["processor"].refund_payment(
                            payment_id, 
                            payment_info["details"]["amount"]
                        )
                        break
                return True
        return False

# Test enhanced SRP design:
print("\n=== Enhanced Order Management System ===")

oms = OrderManagementSystem()

# Create orders
items1 = [
    {"name": "Laptop", "price": 999, "quantity": 1},
    {"name": "Mouse", "price": 25, "quantity": 2}
]

items2 = [
    {"name": "Keyboard", "price": 75, "quantity": 1},
    {"name": "Monitor", "price": 299, "quantity": 1}
]

print("Creating orders:")
result1 = oms.create_order(items1, "CUST-001", "credit_card")
print(f"Order 1: {result1['order']['order_id']}, Payment: {result1['payment']['status']}")

result2 = oms.create_order(items2, "CUST-002", "paypal")
print(f"Order 2: {result2['order']['order_id']}, Payment: {result2['payment']['status']}")

# Test order cancellation
print(f"\nCancelling order: {result1['order']['order_id']}")
cancelled = oms.cancel_order(result1['order']['order_id'])
print(f"Cancellation successful: {cancelled}")

# What we accomplished in this step:
# - Created a comprehensive order management system using SRP
# - OrderProcessor handles all order-related logic independently
# - PaymentProcessor handles all payment-related logic independently
# - Easy to extend with new features without affecting other components
# - System is highly maintainable and testable


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the advanced Single Responsibility Principle solution!
#
# Key concepts learned:
# - Advanced application of SRP in e-commerce systems
# - Separating order processing from payment processing
# - Creating flexible systems that support multiple payment methods
# - Transaction history and refund handling
# - Building comprehensive business systems with proper separation of concerns
# - Benefits of SRP in complex, real-world scenarios
#
# Advanced SRP Benefits demonstrated:
# - OrderProcessor can evolve independently (tax calculation, inventory, etc.)
# - PaymentProcessor can support new payment methods without affecting orders
# - Easy to add new features like refunds, payment history, etc.
# - Different payment gateways can be integrated easily
# - Testing becomes easier with separated concerns
# - Business logic changes don't cascade across unrelated components
#
# Real-world applications:
# - E-commerce platforms with separate order and payment services
# - Microservices architecture (order service vs payment service)
# - Integration with multiple payment providers
# - Compliance and audit requirements (separate payment logs)
# - A/B testing different payment flows
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY separation enables business flexibility
# 4. Experiment with adding new payment methods or order features
#
# Remember: The best way to learn is by doing!
# ===============================================================================
