"""Question: Create a class Discount with a method apply_discount.
Implement subclasses PercentageDiscount and FixedAmountDiscount
that apply different types of discounts.
Ensure the classes are open for extension but closed for modification.
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
# - How do you create a base class that can be extended but not modified?
# - What are the different ways to calculate discounts?
# - How does inheritance support the Open/Closed Principle?
# - What are the benefits of having separate discount types?
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


# Step 1: Create the abstract base Discount class
# ===============================================================================

# Explanation:
# Let's start by creating the Discount base class that defines the interface
# for all discount types. This class is "closed for modification" but provides
# a foundation for extension.

class Discount:
    def apply_discount(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created abstract base class that defines the discount interface
# - Used NotImplementedError to enforce implementation in subclasses
# - This class is now "closed for modification" - we won't change it


# Step 2: Create PercentageDiscount class
# ===============================================================================

# Explanation:
# Now let's create a PercentageDiscount class that applies percentage-based
# discounts. This demonstrates "open for extension".

class Discount:
    def apply_discount(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

# What we accomplished in this step:
# - Extended Discount without modifying it (open for extension)
# - Implemented percentage-based discount calculation
# - Followed the contract defined by the base class


# Step 3: Create FixedAmountDiscount class
# ===============================================================================

# Explanation:
# Let's add a FixedAmountDiscount class that applies fixed amount discounts.
# Notice how we can add new functionality without modifying existing code.

class Discount:
    def apply_discount(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

class FixedAmountDiscount(Discount):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, amount):
        return amount - self.discount_amount

# What we accomplished in this step:
# - Added FixedAmountDiscount without modifying Discount or PercentageDiscount
# - Demonstrated how OCP enables easy extension
# - Each discount type has its own specific implementation


# Step 4: Test our OCP-compliant design
# ===============================================================================

# Explanation:
# Let's test our design to see how polymorphism works with our
# OCP-compliant discount hierarchy.

class Discount:
    def apply_discount(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

class FixedAmountDiscount(Discount):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, amount):
        return amount - self.discount_amount

# Test our OCP-compliant design:
print("=== Testing OCP-Compliant Discount Design ===")

discounts = [PercentageDiscount(10), FixedAmountDiscount(20)]
amount = 100

print(f"Original amount: ${amount}")
print("Applying different discounts:")

for i, discount in enumerate(discounts, 1):
    discount_name = discount.__class__.__name__
    discounted_amount = discount.apply_discount(amount)
    savings = amount - discounted_amount
    print(f"Discount {i} ({discount_name}): ${discounted_amount:.2f} (saved ${savings:.2f})")

# What we accomplished in this step:
# - Demonstrated polymorphism with different discount types
# - Showed how the same interface works for all discounts
# - Verified that our OCP design works correctly


# Step 5: Demonstrate extension by adding new discount types
# ===============================================================================

# Explanation:
# Let's prove that our design follows OCP by adding new discount types
# without modifying any existing code.

class Discount:
    def apply_discount(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

class FixedAmountDiscount(Discount):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, amount):
        return amount - self.discount_amount

# Adding new discount types without modifying existing code (OCP in action!)
class TieredDiscount(Discount):
    def __init__(self, tiers):
        # tiers is a list of (threshold, discount_percentage) tuples
        self.tiers = sorted(tiers, key=lambda x: x[0], reverse=True)

    def apply_discount(self, amount):
        for threshold, discount_percentage in self.tiers:
            if amount >= threshold:
                return amount - (amount * discount_percentage / 100)
        return amount  # No discount if below all thresholds

class BuyOneGetOneDiscount(Discount):
    def __init__(self, item_price):
        self.item_price = item_price

    def apply_discount(self, amount):
        # Assumes amount is total for multiple items of same price
        num_items = int(amount / self.item_price)
        free_items = num_items // 2  # Every second item is free
        return amount - (free_items * self.item_price)

print("\n=== Demonstrating Extension (Adding New Discount Types) ===")

# Test with new discount types
tiered_discount = TieredDiscount([(100, 15), (50, 10), (25, 5)])
bogo_discount = BuyOneGetOneDiscount(25)  # Item costs $25

test_amounts = [30, 75, 150]

print("Testing TieredDiscount:")
for amount in test_amounts:
    discounted = tiered_discount.apply_discount(amount)
    savings = amount - discounted
    print(f"  ${amount} -> ${discounted:.2f} (saved ${savings:.2f})")

print("\nTesting BuyOneGetOneDiscount (item price $25):")
for amount in [25, 50, 75, 100]:
    discounted = bogo_discount.apply_discount(amount)
    savings = amount - discounted
    items = int(amount / 25)
    print(f"  ${amount} ({items} items) -> ${discounted:.2f} (saved ${savings:.2f})")

# What we accomplished in this step:
# - Added complex discount types without modifying existing code
# - Demonstrated "open for extension, closed for modification"
# - Showed how new business rules can be easily integrated


# Step 6: Enhanced example with discount management system
# ===============================================================================

# Explanation:
# Let's create a comprehensive example that shows how OCP enables
# building complex discount management systems.

class Discount:
    def apply_discount(self, amount):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_description(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def is_applicable(self, amount, context=None):
        """Check if discount can be applied to the given amount/context"""
        return True  # Default: always applicable

class PercentageDiscount(Discount):
    def __init__(self, percentage, min_amount=0):
        self.percentage = percentage
        self.min_amount = min_amount

    def apply_discount(self, amount):
        if amount >= self.min_amount:
            return amount - (amount * self.percentage / 100)
        return amount

    def get_description(self):
        if self.min_amount > 0:
            return f"{self.percentage}% off orders over ${self.min_amount}"
        return f"{self.percentage}% off"

    def is_applicable(self, amount, context=None):
        return amount >= self.min_amount

class FixedAmountDiscount(Discount):
    def __init__(self, discount_amount, min_amount=0):
        self.discount_amount = discount_amount
        self.min_amount = min_amount

    def apply_discount(self, amount):
        if amount >= self.min_amount:
            return max(0, amount - self.discount_amount)
        return amount

    def get_description(self):
        if self.min_amount > 0:
            return f"${self.discount_amount} off orders over ${self.min_amount}"
        return f"${self.discount_amount} off"

    def is_applicable(self, amount, context=None):
        return amount >= self.min_amount

class SeasonalDiscount(Discount):
    def __init__(self, percentage, valid_months):
        self.percentage = percentage
        self.valid_months = valid_months

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

    def get_description(self):
        months = ", ".join(self.valid_months)
        return f"{self.percentage}% seasonal discount (valid: {months})"

    def is_applicable(self, amount, context=None):
        if context and 'current_month' in context:
            return context['current_month'] in self.valid_months
        return True  # Assume applicable if no context

class LoyaltyDiscount(Discount):
    def __init__(self, percentage, required_tier):
        self.percentage = percentage
        self.required_tier = required_tier

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

    def get_description(self):
        return f"{self.percentage}% loyalty discount ({self.required_tier} tier)"

    def is_applicable(self, amount, context=None):
        if context and 'customer_tier' in context:
            tier_levels = {'bronze': 1, 'silver': 2, 'gold': 3, 'platinum': 4}
            customer_level = tier_levels.get(context['customer_tier'], 0)
            required_level = tier_levels.get(self.required_tier, 0)
            return customer_level >= required_level
        return False

class DiscountManager:
    def __init__(self):
        self.available_discounts = []

    def add_discount(self, discount):
        self.available_discounts.append(discount)

    def find_best_discount(self, amount, context=None):
        applicable_discounts = [
            d for d in self.available_discounts 
            if d.is_applicable(amount, context)
        ]
        
        if not applicable_discounts:
            return None, amount
        
        best_discount = None
        best_final_amount = amount
        
        for discount in applicable_discounts:
            final_amount = discount.apply_discount(amount)
            if final_amount < best_final_amount:
                best_discount = discount
                best_final_amount = final_amount
        
        return best_discount, best_final_amount

    def apply_all_applicable_discounts(self, amount, context=None):
        applicable_discounts = [
            d for d in self.available_discounts 
            if d.is_applicable(amount, context)
        ]
        
        results = []
        for discount in applicable_discounts:
            final_amount = discount.apply_discount(amount)
            savings = amount - final_amount
            results.append({
                'discount': discount,
                'description': discount.get_description(),
                'original_amount': amount,
                'final_amount': final_amount,
                'savings': savings
            })
        
        return results

    def get_available_discounts(self, amount, context=None):
        return [
            d for d in self.available_discounts 
            if d.is_applicable(amount, context)
        ]

# Test enhanced discount management system:
print("\n=== Enhanced Discount Management System ===")

manager = DiscountManager()

# Add various discounts
manager.add_discount(PercentageDiscount(10, min_amount=50))
manager.add_discount(FixedAmountDiscount(15, min_amount=100))
manager.add_discount(SeasonalDiscount(20, ['December', 'January']))
manager.add_discount(LoyaltyDiscount(25, 'gold'))

# Test scenarios
test_scenarios = [
    {
        'amount': 75,
        'context': {'current_month': 'December', 'customer_tier': 'silver'},
        'description': 'Regular customer, December, $75 order'
    },
    {
        'amount': 120,
        'context': {'current_month': 'June', 'customer_tier': 'gold'},
        'description': 'Gold customer, June, $120 order'
    },
    {
        'amount': 200,
        'context': {'current_month': 'December', 'customer_tier': 'platinum'},
        'description': 'Platinum customer, December, $200 order'
    }
]

for scenario in test_scenarios:
    print(f"\nScenario: {scenario['description']}")
    
    # Find best discount
    best_discount, best_amount = manager.find_best_discount(
        scenario['amount'], scenario['context']
    )
    
    if best_discount:
        savings = scenario['amount'] - best_amount
        print(f"Best discount: {best_discount.get_description()}")
        print(f"Final amount: ${best_amount:.2f} (saved ${savings:.2f})")
    else:
        print("No applicable discounts")
    
    # Show all applicable discounts
    all_results = manager.apply_all_applicable_discounts(
        scenario['amount'], scenario['context']
    )
    
    if len(all_results) > 1:
        print("All applicable discounts:")
        for result in all_results:
            print(f"  - {result['description']}: ${result['final_amount']:.2f} "
                  f"(save ${result['savings']:.2f})")

# What we accomplished in this step:
# - Created a sophisticated discount management system
# - Added context-aware discount applicability
# - Demonstrated how OCP enables complex business rule systems
# - Showed discount comparison and optimization
# - Built a system that can easily accommodate new discount types


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the advanced Open/Closed Principle solution!
#
# Key concepts learned:
# - Advanced application of OCP with discount systems
# - Creating extensible business rule engines
# - Context-aware discount applicability
# - Discount comparison and optimization strategies
# - Building management systems that work with any discount type
# - How OCP enables sophisticated e-commerce functionality
#
# Advanced OCP Benefits demonstrated:
# - New discount types can be added without modifying existing code
# - Complex business rules can be implemented as separate classes
# - Discount management systems work with any discount type
# - Easy to test individual discount strategies in isolation
# - System supports unlimited discount combinations and rules
# - Context-aware discounts enable personalized pricing
#
# Real-world applications:
# - E-commerce platforms with dynamic pricing
# - Loyalty program management systems
# - Promotional campaign engines
# - Insurance premium calculation with various discounts
# - Subscription service pricing with multiple discount tiers
# - Restaurant/retail point-of-sale systems with flexible pricing
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY inheritance enables extension without modification
# 4. Experiment with creating new discount types (student discounts, bulk discounts, etc.)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
