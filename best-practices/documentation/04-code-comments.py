"""Question: Demonstrate best practices for writing effective code comments.

Create a comprehensive example showing different types of comments and when to use them.

Requirements:
1. Show different comment types (single-line, multi-line, docstrings)
2. Demonstrate good vs bad commenting practices
3. Include examples of when NOT to comment
4. Show documentation comments for classes and functions
5. Demonstrate inline comments for complex logic

Example usage:
    calculator = AdvancedCalculator()
    result = calculator.calculate_compound_interest(1000, 0.05, 12, 5)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what makes a good comment vs a bad comment
# - Consider when comments are necessary vs when code should be self-explanatory
# - Practice writing clear, concise comments
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
# - What are the different types of comments in Python?
# - When should you write comments vs when should code be self-documenting?
# - What information should comments provide that code cannot?
# - How do you write effective docstrings?
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


# Step 1: Basic comment types and syntax
# ===============================================================================

# Explanation:
# Python supports several types of comments. Let's start with the basics
# and understand when and how to use each type effectively.

# This is a single-line comment using the hash symbol
# Single-line comments are perfect for brief explanations

"""
This is a multi-line comment using triple quotes.
Multi-line comments are useful for longer explanations,
documentation, or temporarily disabling code blocks.
"""

def basic_function():
    """This is a docstring - a special type of comment for documenting functions."""
    pass


# Step 2: Good vs Bad commenting practices
# ===============================================================================

# Explanation:
# Not all comments are created equal. Let's see examples of good and bad comments
# to understand what makes comments effective.

# BAD EXAMPLES - What NOT to do:

def bad_commenting_examples():
    """Examples of poor commenting practices."""
    
    # BAD: Stating the obvious
    x = 5  # Set x to 5
    
    # BAD: Redundant comments
    # Increment i by 1
    i = i + 1
    
    # BAD: Outdated comments (comment says one thing, code does another)
    # Calculate the square of the number
    result = x * x * x  # Actually calculates cube, not square!
    
    # BAD: Commenting bad code instead of fixing it
    # This is a hack to make it work
    if x == 5 and True and not False:  # Overly complex condition
        pass

# GOOD EXAMPLES - What TO do:

def good_commenting_examples():
    """Examples of effective commenting practices."""
    
    # GOOD: Explain WHY, not WHAT
    # Use binary search for O(log n) performance on large datasets
    result = binary_search(data, target)
    
    # GOOD: Explain complex business logic
    # Apply 15% discount for premium customers with orders over $100
    if customer.is_premium and order_total > 100:
        discount = order_total * 0.15
    
    # GOOD: Warn about potential issues
    # Note: This function modifies the original list
    original_list.sort()
    
    # GOOD: Explain non-obvious algorithms or formulas
    # Using Haversine formula to calculate distance between GPS coordinates
    distance = calculate_haversine_distance(lat1, lon1, lat2, lon2)


# Step 3: Comprehensive docstring examples
# ===============================================================================

# Explanation:
# Docstrings are the most important type of documentation in Python.
# They should describe what a function/class does, its parameters, return values,
# and any important behavior or exceptions.

# Previous code from Steps 1-2:
# This is a single-line comment using the hash symbol
# Single-line comments are perfect for brief explanations

"""
This is a multi-line comment using triple quotes.
Multi-line comments are useful for longer explanations,
documentation, or temporarily disabling code blocks.
"""

def basic_function():
    """This is a docstring - a special type of comment for documenting functions."""
    pass

def bad_commenting_examples():
    """Examples of poor commenting practices."""
    
    # BAD: Stating the obvious
    x = 5  # Set x to 5
    
    # BAD: Redundant comments
    # Increment i by 1
    i = i + 1
    
    # BAD: Outdated comments (comment says one thing, code does another)
    # Calculate the square of the number
    result = x * x * x  # Actually calculates cube, not square!
    
    # BAD: Commenting bad code instead of fixing it
    # This is a hack to make it work
    if x == 5 and True and not False:  # Overly complex condition
        pass

def good_commenting_examples():
    """Examples of effective commenting practices."""
    
    # GOOD: Explain WHY, not WHAT
    # Use binary search for O(log n) performance on large datasets
    result = binary_search(data, target)
    
    # GOOD: Explain complex business logic
    # Apply 15% discount for premium customers with orders over $100
    if customer.is_premium and order_total > 100:
        discount = order_total * 0.15
    
    # GOOD: Warn about potential issues
    # Note: This function modifies the original list
    original_list.sort()
    
    # GOOD: Explain non-obvious algorithms or formulas
    # Using Haversine formula to calculate distance between GPS coordinates
    distance = calculate_haversine_distance(lat1, lon1, lat2, lon2)

# NEW CONTENT for Step 3:

def calculate_compound_interest(principal, rate, compounds_per_year, years):
    """
    Calculate compound interest using the standard formula.
    
    This function implements the compound interest formula:
    A = P(1 + r/n)^(nt)
    
    Args:
        principal (float): The initial amount of money invested or borrowed.
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        compounds_per_year (int): Number of times interest is compounded per year.
        years (float): The number of years the money is invested or borrowed.
    
    Returns:
        float: The final amount after compound interest is applied.
    
    Raises:
        ValueError: If any parameter is negative or if compounds_per_year is zero.
        TypeError: If parameters are not numeric types.
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 12, 5)
        1283.36
        
    Note:
        This function assumes interest is compounded at regular intervals.
        For continuous compounding, use calculate_continuous_compound_interest().
    """
    # Input validation with descriptive error messages
    if not all(isinstance(x, (int, float)) for x in [principal, rate, years]):
        raise TypeError("Principal, rate, and years must be numeric")
    
    if not isinstance(compounds_per_year, int):
        raise TypeError("Compounds per year must be an integer")
    
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Principal, rate, and years must be non-negative")
    
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be positive")
    
    # Apply compound interest formula: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    
    return round(amount, 2)


# Step 4: Class documentation and inline comments for complex logic
# ===============================================================================

# Explanation:
# Classes need comprehensive documentation, and complex algorithms benefit
# from inline comments that explain the logic step by step.

# Previous code from Steps 1-3:
# This is a single-line comment using the hash symbol
# Single-line comments are perfect for brief explanations

"""
This is a multi-line comment using triple quotes.
Multi-line comments are useful for longer explanations,
documentation, or temporarily disabling code blocks.
"""

def basic_function():
    """This is a docstring - a special type of comment for documenting functions."""
    pass

def bad_commenting_examples():
    """Examples of poor commenting practices."""
    
    # BAD: Stating the obvious
    x = 5  # Set x to 5
    
    # BAD: Redundant comments
    # Increment i by 1
    i = i + 1
    
    # BAD: Outdated comments (comment says one thing, code does another)
    # Calculate the square of the number
    result = x * x * x  # Actually calculates cube, not square!
    
    # BAD: Commenting bad code instead of fixing it
    # This is a hack to make it work
    if x == 5 and True and not False:  # Overly complex condition
        pass

def good_commenting_examples():
    """Examples of effective commenting practices."""
    
    # GOOD: Explain WHY, not WHAT
    # Use binary search for O(log n) performance on large datasets
    result = binary_search(data, target)
    
    # GOOD: Explain complex business logic
    # Apply 15% discount for premium customers with orders over $100
    if customer.is_premium and order_total > 100:
        discount = order_total * 0.15
    
    # GOOD: Warn about potential issues
    # Note: This function modifies the original list
    original_list.sort()
    
    # GOOD: Explain non-obvious algorithms or formulas
    # Using Haversine formula to calculate distance between GPS coordinates
    distance = calculate_haversine_distance(lat1, lon1, lat2, lon2)

def calculate_compound_interest(principal, rate, compounds_per_year, years):
    """
    Calculate compound interest using the standard formula.
    
    This function implements the compound interest formula:
    A = P(1 + r/n)^(nt)
    
    Args:
        principal (float): The initial amount of money invested or borrowed.
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        compounds_per_year (int): Number of times interest is compounded per year.
        years (float): The number of years the money is invested or borrowed.
    
    Returns:
        float: The final amount after compound interest is applied.
    
    Raises:
        ValueError: If any parameter is negative or if compounds_per_year is zero.
        TypeError: If parameters are not numeric types.
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 12, 5)
        1283.36
        
    Note:
        This function assumes interest is compounded at regular intervals.
        For continuous compounding, use calculate_continuous_compound_interest().
    """
    # Input validation with descriptive error messages
    if not all(isinstance(x, (int, float)) for x in [principal, rate, years]):
        raise TypeError("Principal, rate, and years must be numeric")
    
    if not isinstance(compounds_per_year, int):
        raise TypeError("Compounds per year must be an integer")
    
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Principal, rate, and years must be non-negative")
    
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be positive")
    
    # Apply compound interest formula: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    
    return round(amount, 2)

# NEW CONTENT for Step 4:

class AdvancedCalculator:
    """
    A comprehensive calculator class for financial and mathematical operations.
    
    This class provides various calculation methods with proper error handling
    and input validation. It maintains a history of calculations for auditing
    purposes.
    
    Attributes:
        calculation_history (list): A list of tuples containing (operation, result, timestamp).
        precision (int): Number of decimal places for rounding results (default: 2).
    
    Example:
        >>> calc = AdvancedCalculator()
        >>> result = calc.calculate_compound_interest(1000, 0.05, 12, 5)
        >>> print(calc.get_calculation_history())
    """
    
    def __init__(self, precision=2):
        """
        Initialize the calculator with specified precision.
        
        Args:
            precision (int): Number of decimal places for results. Default is 2.
        """
        self.calculation_history = []  # Track all calculations for audit trail
        self.precision = precision     # Decimal precision for financial accuracy
    
    def calculate_compound_interest(self, principal, rate, compounds_per_year, years):
        """
        Calculate compound interest using the standard formula.
        
        This method is identical to the standalone function but adds
        the result to the calculation history.
        
        Args:
            principal (float): The initial amount of money.
            rate (float): Annual interest rate as decimal.
            compounds_per_year (int): Compounding frequency per year.
            years (float): Investment period in years.
        
        Returns:
            float: Final amount after compound interest.
        """
        # Reuse the validation and calculation logic from the standalone function
        result = calculate_compound_interest(principal, rate, compounds_per_year, years)
        
        # Record this calculation in history for audit purposes
        import datetime
        self.calculation_history.append((
            f"Compound Interest: P={principal}, r={rate}, n={compounds_per_year}, t={years}",
            result,
            datetime.datetime.now()
        ))
        
        return result
    
    def calculate_loan_payment(self, principal, annual_rate, years):
        """
        Calculate monthly loan payment using the standard loan formula.
        
        Uses the formula: M = P * [r(1+r)^n] / [(1+r)^n - 1]
        where M = monthly payment, P = principal, r = monthly rate, n = total payments
        
        Args:
            principal (float): Loan amount.
            annual_rate (float): Annual interest rate as decimal.
            years (int): Loan term in years.
        
        Returns:
            float: Monthly payment amount.
        """
        # Convert annual rate to monthly rate
        monthly_rate = annual_rate / 12
        
        # Calculate total number of payments
        total_payments = years * 12
        
        # Handle edge case: zero interest rate
        if monthly_rate == 0:
            # Simple division for zero-interest loans
            monthly_payment = principal / total_payments
        else:
            # Standard loan payment formula for interest-bearing loans
            # M = P * [r(1+r)^n] / [(1+r)^n - 1]
            
            # Calculate (1 + r)^n once to avoid repeated computation
            compound_factor = (1 + monthly_rate) ** total_payments
            
            # Apply the loan payment formula
            monthly_payment = principal * (monthly_rate * compound_factor) / (compound_factor - 1)
        
        # Round to specified precision and record in history
        result = round(monthly_payment, self.precision)
        
        import datetime
        self.calculation_history.append((
            f"Loan Payment: P={principal}, rate={annual_rate}, years={years}",
            result,
            datetime.datetime.now()
        ))
        
        return result


# Step 5: Complete example with when NOT to comment and best practices summary
# ===============================================================================

# Explanation:
# The final step shows when code should be self-documenting and provides
# a complete working example that demonstrates all commenting best practices.

# Previous code from Steps 1-4:
# This is a single-line comment using the hash symbol
# Single-line comments are perfect for brief explanations

"""
This is a multi-line comment using triple quotes.
Multi-line comments are useful for longer explanations,
documentation, or temporarily disabling code blocks.
"""

def basic_function():
    """This is a docstring - a special type of comment for documenting functions."""
    pass

def bad_commenting_examples():
    """Examples of poor commenting practices."""
    
    # BAD: Stating the obvious
    x = 5  # Set x to 5
    
    # BAD: Redundant comments
    # Increment i by 1
    i = i + 1
    
    # BAD: Outdated comments (comment says one thing, code does another)
    # Calculate the square of the number
    result = x * x * x  # Actually calculates cube, not square!
    
    # BAD: Commenting bad code instead of fixing it
    # This is a hack to make it work
    if x == 5 and True and not False:  # Overly complex condition
        pass

def good_commenting_examples():
    """Examples of effective commenting practices."""
    
    # GOOD: Explain WHY, not WHAT
    # Use binary search for O(log n) performance on large datasets
    result = binary_search(data, target)
    
    # GOOD: Explain complex business logic
    # Apply 15% discount for premium customers with orders over $100
    if customer.is_premium and order_total > 100:
        discount = order_total * 0.15
    
    # GOOD: Warn about potential issues
    # Note: This function modifies the original list
    original_list.sort()
    
    # GOOD: Explain non-obvious algorithms or formulas
    # Using Haversine formula to calculate distance between GPS coordinates
    distance = calculate_haversine_distance(lat1, lon1, lat2, lon2)

def calculate_compound_interest(principal, rate, compounds_per_year, years):
    """
    Calculate compound interest using the standard formula.
    
    This function implements the compound interest formula:
    A = P(1 + r/n)^(nt)
    
    Args:
        principal (float): The initial amount of money invested or borrowed.
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        compounds_per_year (int): Number of times interest is compounded per year.
        years (float): The number of years the money is invested or borrowed.
    
    Returns:
        float: The final amount after compound interest is applied.
    
    Raises:
        ValueError: If any parameter is negative or if compounds_per_year is zero.
        TypeError: If parameters are not numeric types.
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 12, 5)
        1283.36
        
    Note:
        This function assumes interest is compounded at regular intervals.
        For continuous compounding, use calculate_continuous_compound_interest().
    """
    # Input validation with descriptive error messages
    if not all(isinstance(x, (int, float)) for x in [principal, rate, years]):
        raise TypeError("Principal, rate, and years must be numeric")
    
    if not isinstance(compounds_per_year, int):
        raise TypeError("Compounds per year must be an integer")
    
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Principal, rate, and years must be non-negative")
    
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be positive")
    
    # Apply compound interest formula: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    
    return round(amount, 2)

class AdvancedCalculator:
    """
    A comprehensive calculator class for financial and mathematical operations.
    
    This class provides various calculation methods with proper error handling
    and input validation. It maintains a history of calculations for auditing
    purposes.
    
    Attributes:
        calculation_history (list): A list of tuples containing (operation, result, timestamp).
        precision (int): Number of decimal places for rounding results (default: 2).
    
    Example:
        >>> calc = AdvancedCalculator()
        >>> result = calc.calculate_compound_interest(1000, 0.05, 12, 5)
        >>> print(calc.get_calculation_history())
    """
    
    def __init__(self, precision=2):
        """
        Initialize the calculator with specified precision.
        
        Args:
            precision (int): Number of decimal places for results. Default is 2.
        """
        self.calculation_history = []  # Track all calculations for audit trail
        self.precision = precision     # Decimal precision for financial accuracy
    
    def calculate_compound_interest(self, principal, rate, compounds_per_year, years):
        """
        Calculate compound interest using the standard formula.
        
        This method is identical to the standalone function but adds
        the result to the calculation history.
        
        Args:
            principal (float): The initial amount of money.
            rate (float): Annual interest rate as decimal.
            compounds_per_year (int): Compounding frequency per year.
            years (float): Investment period in years.
        
        Returns:
            float: Final amount after compound interest.
        """
        # Reuse the validation and calculation logic from the standalone function
        result = calculate_compound_interest(principal, rate, compounds_per_year, years)
        
        # Record this calculation in history for audit purposes
        import datetime
        self.calculation_history.append((
            f"Compound Interest: P={principal}, r={rate}, n={compounds_per_year}, t={years}",
            result,
            datetime.datetime.now()
        ))
        
        return result
    
    def calculate_loan_payment(self, principal, annual_rate, years):
        """
        Calculate monthly loan payment using the standard loan formula.
        
        Uses the formula: M = P * [r(1+r)^n] / [(1+r)^n - 1]
        where M = monthly payment, P = principal, r = monthly rate, n = total payments
        
        Args:
            principal (float): Loan amount.
            annual_rate (float): Annual interest rate as decimal.
            years (int): Loan term in years.
        
        Returns:
            float: Monthly payment amount.
        """
        # Convert annual rate to monthly rate
        monthly_rate = annual_rate / 12
        
        # Calculate total number of payments
        total_payments = years * 12
        
        # Handle edge case: zero interest rate
        if monthly_rate == 0:
            # Simple division for zero-interest loans
            monthly_payment = principal / total_payments
        else:
            # Standard loan payment formula for interest-bearing loans
            # M = P * [r(1+r)^n] / [(1+r)^n - 1]
            
            # Calculate (1 + r)^n once to avoid repeated computation
            compound_factor = (1 + monthly_rate) ** total_payments
            
            # Apply the loan payment formula
            monthly_payment = principal * (monthly_rate * compound_factor) / (compound_factor - 1)
        
        # Round to specified precision and record in history
        result = round(monthly_payment, self.precision)
        
        import datetime
        self.calculation_history.append((
            f"Loan Payment: P={principal}, rate={annual_rate}, years={years}",
            result,
            datetime.datetime.now()
        ))
        
        return result

# NEW CONTENT for Step 5:

    def get_calculation_history(self):
        """Return the complete calculation history."""
        return self.calculation_history.copy()  # Return copy to prevent external modification
    
    def clear_history(self):
        """Clear all calculation history."""
        self.calculation_history.clear()


# Examples of when NOT to comment (self-documenting code):
def self_documenting_examples():
    """Examples of code that doesn't need comments because it's self-explanatory."""
    
    # These examples show good variable names and clear logic that don't need comments:
    
    customer_age = 25
    minimum_voting_age = 18
    
    # No comment needed - the code is clear
    if customer_age >= minimum_voting_age:
        can_vote = True
        print(f"Customer can vote: {can_vote}")
    
    # Clear list comprehension doesn't need explanation
    even_numbers = [num for num in range(10) if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")
    
    # Simple arithmetic with descriptive variable names
    subtotal = 100.0
    tax_rate = 0.08
    shipping_cost = 15.0
    total_price = subtotal + (subtotal * tax_rate) + shipping_cost
    print(f"Total price: ${total_price:.2f}")
    
    # Clear conditional logic with meaningful variable names
    email_address = "user@example.com"
    user_is_authenticated = True
    
    if "@" in email_address and user_is_authenticated:
        print("User is valid and authenticated")
    
    # Self-explanatory data processing
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [num ** 2 for num in numbers]
    print(f"Squared numbers: {squared_numbers}")


# Complete working example demonstrating all best practices:
def demonstrate_all_commenting_practices():
    """
    Comprehensive demonstration of all commenting best practices.
    
    This function showcases proper use of docstrings, inline comments,
    and self-documenting code in a realistic scenario.
    """
    print("=== Code Comments Best Practices Demo ===\n")
    
    # Create calculator instance with financial precision
    calculator = AdvancedCalculator(precision=2)
    
    # Test compound interest calculation
    print("1. Compound Interest Calculation:")
    principal = 1000.0
    annual_rate = 0.05  # 5% annual interest
    compounds_per_year = 12  # Monthly compounding
    investment_years = 5
    
    final_amount = calculator.calculate_compound_interest(
        principal, annual_rate, compounds_per_year, investment_years
    )
    
    print(f"   Initial investment: ${principal:,.2f}")
    print(f"   Annual rate: {annual_rate:.1%}")
    print(f"   Compounding: {compounds_per_year} times per year")
    print(f"   Investment period: {investment_years} years")
    print(f"   Final amount: ${final_amount:,.2f}")
    print(f"   Total interest earned: ${final_amount - principal:,.2f}\n")
    
    # Test loan payment calculation
    print("2. Loan Payment Calculation:")
    loan_amount = 250000.0  # $250,000 mortgage
    loan_rate = 0.035  # 3.5% annual rate
    loan_term = 30  # 30-year mortgage
    
    monthly_payment = calculator.calculate_loan_payment(loan_amount, loan_rate, loan_term)
    
    print(f"   Loan amount: ${loan_amount:,.2f}")
    print(f"   Annual rate: {loan_rate:.1%}")
    print(f"   Loan term: {loan_term} years")
    print(f"   Monthly payment: ${monthly_payment:,.2f}\n")
    
    # Display calculation history
    print("3. Calculation History:")
    history = calculator.get_calculation_history()
    for i, (operation, result, timestamp) in enumerate(history, 1):
        print(f"   {i}. {operation}")
        print(f"      Result: ${result:,.2f}")
        print(f"      Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")


# Summary of commenting best practices:
"""
COMMENTING BEST PRACTICES SUMMARY:

DO:
✓ Write docstrings for all public functions, classes, and modules
✓ Explain WHY something is done, not WHAT is done
✓ Document complex algorithms and business logic
✓ Warn about side effects or important behaviors
✓ Include examples in docstrings when helpful
✓ Keep comments up-to-date with code changes
✓ Use clear, concise language
✓ Document function parameters, return values, and exceptions

DON'T:
✗ State the obvious (e.g., "increment x by 1")
✗ Write redundant comments that repeat the code
✗ Leave outdated comments that contradict the code
✗ Comment bad code instead of fixing it
✗ Write comments for simple, self-explanatory code
✗ Use comments as a substitute for good variable/function names

REMEMBER:
- Good code is self-documenting through clear names and structure
- Comments should add value that the code itself cannot provide
- The best comment is often no comment when code is clear
- Maintain comments as carefully as you maintain code
"""


# Example usage and testing:
if __name__ == "__main__":
    # Run the comprehensive demonstration
    demonstrate_all_commenting_practices()
    
    # Show examples of self-documenting code
    print("=== Self-Documenting Code Examples ===")
    self_documenting_examples()
    print("Self-documenting code examples completed successfully!")