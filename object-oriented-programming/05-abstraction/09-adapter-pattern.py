"""Question: Implement the Adapter pattern to make incompatible interfaces work together.

Create an adapter that allows old legacy payment systems to work with a new
payment processing interface.

Requirements:
1. Create a modern payment processor interface
2. Create legacy payment systems with different interfaces
3. Create adapters to make legacy systems compatible
4. Demonstrate the adapter pattern usage

Example usage:
    legacy_system = OldPayPalSystem()
    adapter = PayPalAdapter(legacy_system)
    processor = PaymentProcessor(adapter)
    processor.process_payment(100.0)
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
# - What is the target interface you want to use?
# - What legacy systems have incompatible interfaces?
# - How do adapters convert between interfaces?
# - How does the client code work with adapters?
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


# Step 1: Create the target interface (what we want to use)
# ===============================================================================

# Explanation:
# The target interface defines the modern, standardized way we want to
# process payments. This is what our new code expects to work with.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Modern payment processor interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Process a payment and return transaction details."""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process a refund and return refund details."""
        pass

# What we accomplished in this step:
# - Created the target interface that defines our desired API
# - Standardized payment processing methods


# Step 2: Create legacy systems with incompatible interfaces
# ===============================================================================

# Explanation:
# These are existing payment systems that we need to integrate, but they
# have different method names, parameters, and return formats.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Modern payment processor interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Process a payment and return transaction details."""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process a refund and return refund details."""
        pass

class OldPayPalSystem:
    """Legacy PayPal system with different interface."""
    
    def make_payment(self, sum_in_cents: int, curr: str):
        """Legacy method with different parameter format."""
        return {
            'status': 'completed',
            'transaction_ref': f'PP_{sum_in_cents}_{curr}',
            'amount_cents': sum_in_cents,
            'currency': curr
        }
    
    def make_refund(self, ref: str, sum_in_cents: int):
        """Legacy refund method."""
        return {
            'status': 'refunded',
            'refund_ref': f'RF_{ref}',
            'amount_cents': sum_in_cents
        }

class OldStripeSystem:
    """Legacy Stripe system with different interface."""
    
    def charge(self, amount_dollars: float, currency_code: str = "USD"):
        """Legacy charge method."""
        return {
            'success': True,
            'charge_id': f'ch_{int(amount_dollars * 100)}',
            'amount': amount_dollars,
            'currency': currency_code
        }
    
    def create_refund(self, charge_id: str, refund_amount: float):
        """Legacy refund method."""
        return {
            'success': True,
            'refund_id': f're_{charge_id}',
            'amount': refund_amount
        }

# What we accomplished in this step:
# - Created legacy systems with incompatible interfaces
# - Demonstrated different method names and parameter formats


# Step 3: Create adapter for PayPal legacy system
# ===============================================================================

# Explanation:
# The adapter implements the target interface but internally uses the
# legacy system. It converts between the two interfaces.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Modern payment processor interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Process a payment and return transaction details."""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process a refund and return refund details."""
        pass

class OldPayPalSystem:
    """Legacy PayPal system with different interface."""
    
    def make_payment(self, sum_in_cents: int, curr: str):
        """Legacy method with different parameter format."""
        return {
            'status': 'completed',
            'transaction_ref': f'PP_{sum_in_cents}_{curr}',
            'amount_cents': sum_in_cents,
            'currency': curr
        }
    
    def make_refund(self, ref: str, sum_in_cents: int):
        """Legacy refund method."""
        return {
            'status': 'refunded',
            'refund_ref': f'RF_{ref}',
            'amount_cents': sum_in_cents
        }

class OldStripeSystem:
    """Legacy Stripe system with different interface."""
    
    def charge(self, amount_dollars: float, currency_code: str = "USD"):
        """Legacy charge method."""
        return {
            'success': True,
            'charge_id': f'ch_{int(amount_dollars * 100)}',
            'amount': amount_dollars,
            'currency': currency_code
        }
    
    def create_refund(self, charge_id: str, refund_amount: float):
        """Legacy refund method."""
        return {
            'success': True,
            'refund_id': f're_{charge_id}',
            'amount': refund_amount
        }

class PayPalAdapter(PaymentProcessor):
    """Adapter for PayPal legacy system."""
    
    def __init__(self, paypal_system: OldPayPalSystem):
        self.paypal_system = paypal_system
    
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Adapt the interface to work with PayPal legacy system."""
        # Convert dollars to cents
        amount_cents = int(amount * 100)
        
        # Call legacy method
        result = self.paypal_system.make_payment(amount_cents, currency)
        
        # Convert response to modern format
        return {
            'success': result['status'] == 'completed',
            'transaction_id': result['transaction_ref'],
            'amount': amount,
            'currency': currency,
            'processor': 'PayPal'
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Adapt refund interface."""
        amount_cents = int(amount * 100)
        result = self.paypal_system.make_refund(transaction_id, amount_cents)
        
        return {
            'success': result['status'] == 'refunded',
            'refund_id': result['refund_ref'],
            'amount': amount,
            'original_transaction': transaction_id
        }

# What we accomplished in this step:
# - Created adapter that implements target interface
# - Converted between different parameter formats and return types


# Step 4: Create adapter for Stripe legacy system
# ===============================================================================

# Explanation:
# Similar to PayPal adapter, but handles Stripe's specific interface.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Modern payment processor interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Process a payment and return transaction details."""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process a refund and return refund details."""
        pass

class OldPayPalSystem:
    """Legacy PayPal system with different interface."""
    
    def make_payment(self, sum_in_cents: int, curr: str):
        """Legacy method with different parameter format."""
        return {
            'status': 'completed',
            'transaction_ref': f'PP_{sum_in_cents}_{curr}',
            'amount_cents': sum_in_cents,
            'currency': curr
        }
    
    def make_refund(self, ref: str, sum_in_cents: int):
        """Legacy refund method."""
        return {
            'status': 'refunded',
            'refund_ref': f'RF_{ref}',
            'amount_cents': sum_in_cents
        }

class OldStripeSystem:
    """Legacy Stripe system with different interface."""
    
    def charge(self, amount_dollars: float, currency_code: str = "USD"):
        """Legacy charge method."""
        return {
            'success': True,
            'charge_id': f'ch_{int(amount_dollars * 100)}',
            'amount': amount_dollars,
            'currency': currency_code
        }
    
    def create_refund(self, charge_id: str, refund_amount: float):
        """Legacy refund method."""
        return {
            'success': True,
            'refund_id': f're_{charge_id}',
            'amount': refund_amount
        }

class PayPalAdapter(PaymentProcessor):
    """Adapter for PayPal legacy system."""
    
    def __init__(self, paypal_system: OldPayPalSystem):
        self.paypal_system = paypal_system
    
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Adapt the interface to work with PayPal legacy system."""
        # Convert dollars to cents
        amount_cents = int(amount * 100)
        
        # Call legacy method
        result = self.paypal_system.make_payment(amount_cents, currency)
        
        # Convert response to modern format
        return {
            'success': result['status'] == 'completed',
            'transaction_id': result['transaction_ref'],
            'amount': amount,
            'currency': currency,
            'processor': 'PayPal'
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Adapt refund interface."""
        amount_cents = int(amount * 100)
        result = self.paypal_system.make_refund(transaction_id, amount_cents)
        
        return {
            'success': result['status'] == 'refunded',
            'refund_id': result['refund_ref'],
            'amount': amount,
            'original_transaction': transaction_id
        }

class StripeAdapter(PaymentProcessor):
    """Adapter for Stripe legacy system."""
    
    def __init__(self, stripe_system: OldStripeSystem):
        self.stripe_system = stripe_system
    
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Adapt the interface to work with Stripe legacy system."""
        result = self.stripe_system.charge(amount, currency)
        
        return {
            'success': result['success'],
            'transaction_id': result['charge_id'],
            'amount': amount,
            'currency': currency,
            'processor': 'Stripe'
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Adapt refund interface."""
        result = self.stripe_system.create_refund(transaction_id, amount)
        
        return {
            'success': result['success'],
            'refund_id': result['refund_id'],
            'amount': amount,
            'original_transaction': transaction_id
        }

# What we accomplished in this step:
# - Created another adapter for different legacy system
# - Showed how adapters handle different legacy interfaces


# Step 5: Create client code that uses the unified interface
# ===============================================================================

# Explanation:
# The client code works with the target interface and doesn't need to know
# about the legacy systems or adapters.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Modern payment processor interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Process a payment and return transaction details."""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process a refund and return refund details."""
        pass

class OldPayPalSystem:
    """Legacy PayPal system with different interface."""
    
    def make_payment(self, sum_in_cents: int, curr: str):
        """Legacy method with different parameter format."""
        return {
            'status': 'completed',
            'transaction_ref': f'PP_{sum_in_cents}_{curr}',
            'amount_cents': sum_in_cents,
            'currency': curr
        }
    
    def make_refund(self, ref: str, sum_in_cents: int):
        """Legacy refund method."""
        return {
            'status': 'refunded',
            'refund_ref': f'RF_{ref}',
            'amount_cents': sum_in_cents
        }

class OldStripeSystem:
    """Legacy Stripe system with different interface."""
    
    def charge(self, amount_dollars: float, currency_code: str = "USD"):
        """Legacy charge method."""
        return {
            'success': True,
            'charge_id': f'ch_{int(amount_dollars * 100)}',
            'amount': amount_dollars,
            'currency': currency_code
        }
    
    def create_refund(self, charge_id: str, refund_amount: float):
        """Legacy refund method."""
        return {
            'success': True,
            'refund_id': f're_{charge_id}',
            'amount': refund_amount
        }

class PayPalAdapter(PaymentProcessor):
    """Adapter for PayPal legacy system."""
    
    def __init__(self, paypal_system: OldPayPalSystem):
        self.paypal_system = paypal_system
    
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Adapt the interface to work with PayPal legacy system."""
        # Convert dollars to cents
        amount_cents = int(amount * 100)
        
        # Call legacy method
        result = self.paypal_system.make_payment(amount_cents, currency)
        
        # Convert response to modern format
        return {
            'success': result['status'] == 'completed',
            'transaction_id': result['transaction_ref'],
            'amount': amount,
            'currency': currency,
            'processor': 'PayPal'
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Adapt refund interface."""
        amount_cents = int(amount * 100)
        result = self.paypal_system.make_refund(transaction_id, amount_cents)
        
        return {
            'success': result['status'] == 'refunded',
            'refund_id': result['refund_ref'],
            'amount': amount,
            'original_transaction': transaction_id
        }

class StripeAdapter(PaymentProcessor):
    """Adapter for Stripe legacy system."""
    
    def __init__(self, stripe_system: OldStripeSystem):
        self.stripe_system = stripe_system
    
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Adapt the interface to work with Stripe legacy system."""
        result = self.stripe_system.charge(amount, currency)
        
        return {
            'success': result['success'],
            'transaction_id': result['charge_id'],
            'amount': amount,
            'currency': currency,
            'processor': 'Stripe'
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Adapt refund interface."""
        result = self.stripe_system.create_refund(transaction_id, amount)
        
        return {
            'success': result['success'],
            'refund_id': result['refund_id'],
            'amount': amount,
            'original_transaction': transaction_id
        }

class PaymentService:
    """Service that processes payments using unified interface."""
    
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor
    
    def make_payment(self, amount: float, currency: str = "USD"):
        """Make a payment using the processor."""
        print(f"Processing payment of {amount} {currency}...")
        result = self.processor.process_payment(amount, currency)
        
        if result['success']:
            print(f"✓ Payment successful! Transaction ID: {result['transaction_id']}")
            print(f"  Processor: {result.get('processor', 'Unknown')}")
            return result
        else:
            print("✗ Payment failed!")
            return None
    
    def make_refund(self, transaction_id: str, amount: float):
        """Make a refund using the processor."""
        print(f"Processing refund of {amount} for transaction {transaction_id}...")
        result = self.processor.refund_payment(transaction_id, amount)
        
        if result['success']:
            print(f"✓ Refund successful! Refund ID: {result['refund_id']}")
            return result
        else:
            print("✗ Refund failed!")
            return None

# What we accomplished in this step:
# - Created client code that works with any payment processor
# - Demonstrated polymorphism through the common interface


# Step 6: Test the complete implementation
# ===============================================================================

# Explanation:
# Let's test our Adapter pattern implementation with different legacy systems.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Modern payment processor interface."""
    
    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Process a payment and return transaction details."""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Process a refund and return refund details."""
        pass

class OldPayPalSystem:
    """Legacy PayPal system with different interface."""
    
    def make_payment(self, sum_in_cents: int, curr: str):
        """Legacy method with different parameter format."""
        return {
            'status': 'completed',
            'transaction_ref': f'PP_{sum_in_cents}_{curr}',
            'amount_cents': sum_in_cents,
            'currency': curr
        }
    
    def make_refund(self, ref: str, sum_in_cents: int):
        """Legacy refund method."""
        return {
            'status': 'refunded',
            'refund_ref': f'RF_{ref}',
            'amount_cents': sum_in_cents
        }

class OldStripeSystem:
    """Legacy Stripe system with different interface."""
    
    def charge(self, amount_dollars: float, currency_code: str = "USD"):
        """Legacy charge method."""
        return {
            'success': True,
            'charge_id': f'ch_{int(amount_dollars * 100)}',
            'amount': amount_dollars,
            'currency': currency_code
        }
    
    def create_refund(self, charge_id: str, refund_amount: float):
        """Legacy refund method."""
        return {
            'success': True,
            'refund_id': f're_{charge_id}',
            'amount': refund_amount
        }

class PayPalAdapter(PaymentProcessor):
    """Adapter for PayPal legacy system."""
    
    def __init__(self, paypal_system: OldPayPalSystem):
        self.paypal_system = paypal_system
    
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Adapt the interface to work with PayPal legacy system."""
        # Convert dollars to cents
        amount_cents = int(amount * 100)
        
        # Call legacy method
        result = self.paypal_system.make_payment(amount_cents, currency)
        
        # Convert response to modern format
        return {
            'success': result['status'] == 'completed',
            'transaction_id': result['transaction_ref'],
            'amount': amount,
            'currency': currency,
            'processor': 'PayPal'
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Adapt refund interface."""
        amount_cents = int(amount * 100)
        result = self.paypal_system.make_refund(transaction_id, amount_cents)
        
        return {
            'success': result['status'] == 'refunded',
            'refund_id': result['refund_ref'],
            'amount': amount,
            'original_transaction': transaction_id
        }

class StripeAdapter(PaymentProcessor):
    """Adapter for Stripe legacy system."""
    
    def __init__(self, stripe_system: OldStripeSystem):
        self.stripe_system = stripe_system
    
    def process_payment(self, amount: float, currency: str = "USD") -> dict:
        """Adapt the interface to work with Stripe legacy system."""
        result = self.stripe_system.charge(amount, currency)
        
        return {
            'success': result['success'],
            'transaction_id': result['charge_id'],
            'amount': amount,
            'currency': currency,
            'processor': 'Stripe'
        }
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        """Adapt refund interface."""
        result = self.stripe_system.create_refund(transaction_id, amount)
        
        return {
            'success': result['success'],
            'refund_id': result['refund_id'],
            'amount': amount,
            'original_transaction': transaction_id
        }

class PaymentService:
    """Service that processes payments using unified interface."""
    
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor
    
    def make_payment(self, amount: float, currency: str = "USD"):
        """Make a payment using the processor."""
        print(f"Processing payment of {amount} {currency}...")
        result = self.processor.process_payment(amount, currency)
        
        if result['success']:
            print(f"✓ Payment successful! Transaction ID: {result['transaction_id']}")
            print(f"  Processor: {result.get('processor', 'Unknown')}")
            return result
        else:
            print("✗ Payment failed!")
            return None
    
    def make_refund(self, transaction_id: str, amount: float):
        """Make a refund using the processor."""
        print(f"Processing refund of {amount} for transaction {transaction_id}...")
        result = self.processor.refund_payment(transaction_id, amount)
        
        if result['success']:
            print(f"✓ Refund successful! Refund ID: {result['refund_id']}")
            return result
        else:
            print("✗ Refund failed!")
            return None

print("=== Testing Adapter Pattern ===\n")

# Test with different legacy systems through adapters
legacy_systems = [
    ("PayPal", PayPalAdapter(OldPayPalSystem())),
    ("Stripe", StripeAdapter(OldStripeSystem()))
]

for system_name, adapter in legacy_systems:
    print(f"--- Testing {system_name} Adapter ---")
    
    # Create payment service with adapter
    payment_service = PaymentService(adapter)
    
    # Process payment
    payment_result = payment_service.make_payment(99.99, "USD")
    
    if payment_result:
        # Process refund
        payment_service.make_refund(
            payment_result['transaction_id'], 
            50.00
        )
    
    print()

# Demonstrate polymorphism - same interface, different implementations
print("--- Demonstrating Polymorphism ---")
adapters = [
    PayPalAdapter(OldPayPalSystem()),
    StripeAdapter(OldStripeSystem())
]

for adapter in adapters:
    result = adapter.process_payment(25.00)
    print(f"{result['processor']}: {result['transaction_id']}")

# What we accomplished in this step:
# - Tested adapters with different legacy systems
# - Demonstrated how client code works the same way with all adapters
# - Showed polymorphism in action


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Adapter pattern structure and purpose
# - Target interface definition
# - Legacy system integration without modification
# - Interface conversion and data transformation
# - Client code isolation from legacy systems
# - Polymorphism through common interfaces
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding more legacy systems!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================