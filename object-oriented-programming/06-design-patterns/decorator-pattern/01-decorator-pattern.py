"""Question: Implement the Decorator pattern to add behavior to objects dynamically.

Create a coffee ordering system where basic coffee can be decorated with
various add-ons (milk, sugar, whipped cream) to modify behavior and cost.

Requirements:
1. Create Coffee interface with cost() and description() methods
2. Implement basic coffee types (Espresso, HouseBlend)
3. Create abstract CondimentDecorator
4. Implement concrete decorators (Milk, Sugar, WhippedCream)
5. Allow multiple decorators to be stacked
6. Demonstrate dynamic behavior modification

Example usage:
    coffee = Espresso()
    coffee = Milk(coffee)
    coffee = Sugar(coffee)
    print(f"{coffee.description()} costs ${coffee.cost()}")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!

# Try to implement your solution here:
# (Write your code below this line)


















































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What is the component interface you need?
# - How do decorators wrap other components?
# - How do you maintain the same interface while adding behavior?
# - How can decorators be stacked on top of each other?
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


# Step 1: Create the component interface and basic coffee classes
# ===============================================================================

# Explanation:
# The Decorator pattern starts with a component interface that defines the
# operations that can be altered by decorators. We'll create a Coffee interface
# with cost() and description() methods.

from abc import ABC, abstractmethod

class Coffee(ABC):
    """Abstract coffee component interface."""
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost of the coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description of the coffee."""
        pass

class Espresso(Coffee):
    """Concrete coffee implementation - Espresso."""
    
    def cost(self) -> float:
        return 1.99
    
    def description(self) -> str:
        return "Espresso"

class HouseBlend(Coffee):
    """Concrete coffee implementation - House Blend."""
    
    def cost(self) -> float:
        return 0.89
    
    def description(self) -> str:
        return "House Blend Coffee"

# What we accomplished in this step:
# - Created abstract Coffee interface with cost() and description() methods
# - Implemented two basic coffee types: Espresso and HouseBlend


# Step 2: Create the abstract decorator class
# ===============================================================================

# Explanation:
# The abstract decorator implements the component interface and has a reference
# to a component object. This allows decorators to wrap other components.

from abc import ABC, abstractmethod

class Coffee(ABC):
    """Abstract coffee component interface."""
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost of the coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description of the coffee."""
        pass

class Espresso(Coffee):
    """Concrete coffee implementation - Espresso."""
    
    def cost(self) -> float:
        return 1.99
    
    def description(self) -> str:
        return "Espresso"

class HouseBlend(Coffee):
    """Concrete coffee implementation - House Blend."""
    
    def cost(self) -> float:
        return 0.89
    
    def description(self) -> str:
        return "House Blend Coffee"

class CondimentDecorator(Coffee):
    """Abstract decorator for coffee condiments."""
    
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost including the wrapped coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description including the wrapped coffee."""
        pass

# What we accomplished in this step:
# - Created abstract CondimentDecorator that implements Coffee interface
# - Added composition relationship to wrap another Coffee object
# - Set up the foundation for concrete decorators


# Step 3: Create the first concrete decorator - Milk
# ===============================================================================

# Explanation:
# Concrete decorators extend the abstract decorator and add specific behavior.
# They delegate to the wrapped component and add their own functionality.

from abc import ABC, abstractmethod

class Coffee(ABC):
    """Abstract coffee component interface."""
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost of the coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description of the coffee."""
        pass

class Espresso(Coffee):
    """Concrete coffee implementation - Espresso."""
    
    def cost(self) -> float:
        return 1.99
    
    def description(self) -> str:
        return "Espresso"

class HouseBlend(Coffee):
    """Concrete coffee implementation - House Blend."""
    
    def cost(self) -> float:
        return 0.89
    
    def description(self) -> str:
        return "House Blend Coffee"

class CondimentDecorator(Coffee):
    """Abstract decorator for coffee condiments."""
    
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost including the wrapped coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description including the wrapped coffee."""
        pass

class Milk(CondimentDecorator):
    """Concrete decorator for adding milk to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.10
    
    def description(self) -> str:
        return self.coffee.description() + ", Milk"

# What we accomplished in this step:
# - Created first concrete decorator (Milk) that adds $0.10 to cost
# - Implemented delegation pattern: calls wrapped coffee's methods first
# - Added milk-specific behavior to description


# Step 4: Create additional concrete decorators
# ===============================================================================

# Explanation:
# Let's add more concrete decorators to show how multiple condiments can be
# implemented with different costs and descriptions.

from abc import ABC, abstractmethod

class Coffee(ABC):
    """Abstract coffee component interface."""
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost of the coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description of the coffee."""
        pass

class Espresso(Coffee):
    """Concrete coffee implementation - Espresso."""
    
    def cost(self) -> float:
        return 1.99
    
    def description(self) -> str:
        return "Espresso"

class HouseBlend(Coffee):
    """Concrete coffee implementation - House Blend."""
    
    def cost(self) -> float:
        return 0.89
    
    def description(self) -> str:
        return "House Blend Coffee"

class CondimentDecorator(Coffee):
    """Abstract decorator for coffee condiments."""
    
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost including the wrapped coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description including the wrapped coffee."""
        pass

class Milk(CondimentDecorator):
    """Concrete decorator for adding milk to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.10
    
    def description(self) -> str:
        return self.coffee.description() + ", Milk"

class Sugar(CondimentDecorator):
    """Concrete decorator for adding sugar to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.05
    
    def description(self) -> str:
        return self.coffee.description() + ", Sugar"

class WhippedCream(CondimentDecorator):
    """Concrete decorator for adding whipped cream to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.15
    
    def description(self) -> str:
        return self.coffee.description() + ", Whipped Cream"

# What we accomplished in this step:
# - Added Sugar decorator ($0.05) and WhippedCream decorator ($0.15)
# - Each decorator follows the same pattern: delegate + add behavior
# - All decorators can be stacked on any Coffee object


# Step 5: Demonstrate basic usage and decorator stacking
# ===============================================================================

# Explanation:
# Let's test our decorator pattern implementation to show how decorators
# can be stacked and how behavior is dynamically modified.

from abc import ABC, abstractmethod

class Coffee(ABC):
    """Abstract coffee component interface."""
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost of the coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description of the coffee."""
        pass

class Espresso(Coffee):
    """Concrete coffee implementation - Espresso."""
    
    def cost(self) -> float:
        return 1.99
    
    def description(self) -> str:
        return "Espresso"

class HouseBlend(Coffee):
    """Concrete coffee implementation - House Blend."""
    
    def cost(self) -> float:
        return 0.89
    
    def description(self) -> str:
        return "House Blend Coffee"

class CondimentDecorator(Coffee):
    """Abstract decorator for coffee condiments."""
    
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost including the wrapped coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description including the wrapped coffee."""
        pass

class Milk(CondimentDecorator):
    """Concrete decorator for adding milk to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.10
    
    def description(self) -> str:
        return self.coffee.description() + ", Milk"

class Sugar(CondimentDecorator):
    """Concrete decorator for adding sugar to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.05
    
    def description(self) -> str:
        return self.coffee.description() + ", Sugar"

class WhippedCream(CondimentDecorator):
    """Concrete decorator for adding whipped cream to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.15
    
    def description(self) -> str:
        return self.coffee.description() + ", Whipped Cream"

print("=== Testing Decorator Pattern ===\n")

# Test 1: Basic coffee without decorators
print("1. Basic Coffee Orders:")
espresso = Espresso()
print(f"{espresso.description()} costs ${espresso.cost():.2f}")

house_blend = HouseBlend()
print(f"{house_blend.description()} costs ${house_blend.cost():.2f}")
print()

# Test 2: Single decorator
print("2. Coffee with Single Condiment:")
espresso_with_milk = Milk(Espresso())
print(f"{espresso_with_milk.description()} costs ${espresso_with_milk.cost():.2f}")
print()

# Test 3: Multiple decorators stacked
print("3. Coffee with Multiple Condiments:")
coffee = Espresso()
coffee = Milk(coffee)
coffee = Sugar(coffee)
print(f"{coffee.description()} costs ${coffee.cost():.2f}")
print()

# What we accomplished in this step:
# - Demonstrated basic coffee orders without decorators
# - Showed single decorator usage
# - Illustrated decorator stacking with multiple condiments


# Step 6: Demonstrate advanced decorator combinations and dynamic behavior
# ===============================================================================

# Explanation:
# Let's show more complex examples including multiple decorators, different
# combinations, and how the pattern enables dynamic behavior modification.

from abc import ABC, abstractmethod

class Coffee(ABC):
    """Abstract coffee component interface."""
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost of the coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description of the coffee."""
        pass

class Espresso(Coffee):
    """Concrete coffee implementation - Espresso."""
    
    def cost(self) -> float:
        return 1.99
    
    def description(self) -> str:
        return "Espresso"

class HouseBlend(Coffee):
    """Concrete coffee implementation - House Blend."""
    
    def cost(self) -> float:
        return 0.89
    
    def description(self) -> str:
        return "House Blend Coffee"

class CondimentDecorator(Coffee):
    """Abstract decorator for coffee condiments."""
    
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    
    @abstractmethod
    def cost(self) -> float:
        """Get the cost including the wrapped coffee."""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """Get the description including the wrapped coffee."""
        pass

class Milk(CondimentDecorator):
    """Concrete decorator for adding milk to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.10
    
    def description(self) -> str:
        return self.coffee.description() + ", Milk"

class Sugar(CondimentDecorator):
    """Concrete decorator for adding sugar to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.05
    
    def description(self) -> str:
        return self.coffee.description() + ", Sugar"

class WhippedCream(CondimentDecorator):
    """Concrete decorator for adding whipped cream to coffee."""
    
    def cost(self) -> float:
        return self.coffee.cost() + 0.15
    
    def description(self) -> str:
        return self.coffee.description() + ", Whipped Cream"

print("=== Testing Decorator Pattern ===\n")

# Test 1: Basic coffee without decorators
print("1. Basic Coffee Orders:")
espresso = Espresso()
print(f"{espresso.description()} costs ${espresso.cost():.2f}")

house_blend = HouseBlend()
print(f"{house_blend.description()} costs ${house_blend.cost():.2f}")
print()

# Test 2: Single decorator
print("2. Coffee with Single Condiment:")
espresso_with_milk = Milk(Espresso())
print(f"{espresso_with_milk.description()} costs ${espresso_with_milk.cost():.2f}")
print()

# Test 3: Multiple decorators stacked
print("3. Coffee with Multiple Condiments:")
coffee = Espresso()
coffee = Milk(coffee)
coffee = Sugar(coffee)
print(f"{coffee.description()} costs ${coffee.cost():.2f}")
print()

# Test 4: Complex decorator combinations
print("4. Complex Decorator Combinations:")
# Deluxe espresso with all condiments
deluxe_espresso = WhippedCream(Sugar(Milk(Espresso())))
print(f"{deluxe_espresso.description()} costs ${deluxe_espresso.cost():.2f}")

# House blend with double milk and sugar
double_milk_coffee = Milk(Milk(Sugar(HouseBlend())))
print(f"{double_milk_coffee.description()} costs ${double_milk_coffee.cost():.2f}")
print()

# Test 5: Dynamic behavior modification
print("5. Dynamic Behavior Modification:")
def customize_coffee(base_coffee: Coffee, condiments: list) -> Coffee:
    """Dynamically add condiments to coffee based on customer preferences."""
    result = base_coffee
    for condiment in condiments:
        if condiment == "milk":
            result = Milk(result)
        elif condiment == "sugar":
            result = Sugar(result)
        elif condiment == "whipped_cream":
            result = WhippedCream(result)
    return result

# Customer 1: Espresso with milk and sugar
customer1_order = customize_coffee(Espresso(), ["milk", "sugar"])
print(f"Customer 1: {customer1_order.description()} costs ${customer1_order.cost():.2f}")

# Customer 2: House blend with whipped cream only
customer2_order = customize_coffee(HouseBlend(), ["whipped_cream"])
print(f"Customer 2: {customer2_order.description()} costs ${customer2_order.cost():.2f}")

# Customer 3: Espresso with everything
customer3_order = customize_coffee(Espresso(), ["milk", "sugar", "whipped_cream"])
print(f"Customer 3: {customer3_order.description()} costs ${customer3_order.cost():.2f}")
print()

# What we accomplished in this step:
# - Showed complex decorator combinations and stacking
# - Demonstrated double decorators (double milk)
# - Created dynamic behavior modification with runtime customization
# - Illustrated how decorators enable flexible object composition


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Decorator pattern structure and purpose
# - Component interface for consistent behavior
# - Abstract decorator as base for concrete decorators
# - Concrete decorators that add specific functionality
# - Decorator stacking for multiple behaviors
# - Dynamic behavior modification at runtime
# - Composition over inheritance principle
#
# Benefits of the Decorator Pattern:
# - Add behavior to objects dynamically without altering their structure
# - More flexible than static inheritance
# - Supports the Open/Closed Principle (open for extension, closed for modification)
# - Allows for unlimited combinations of behaviors
# - Each decorator has a single responsibility
#
# Real-world applications:
# - GUI component styling (borders, scrollbars, etc.)
# - Stream processing (compression, encryption, buffering)
# - Web request/response middleware
# - Coffee shop ordering systems (as demonstrated)
# - Text formatting (bold, italic, underline combinations)
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding new condiments!)
# 5. Create your own decorator pattern implementation
#
# Challenge exercises:
# - Add new coffee types (Cappuccino, Latte)
# - Create size decorators (Small, Medium, Large) that affect cost
# - Implement discount decorators for loyalty customers
# - Add temperature decorators (Hot, Iced) with different costs
#
# Remember: The best way to learn is by doing!
# ===============================================================================
