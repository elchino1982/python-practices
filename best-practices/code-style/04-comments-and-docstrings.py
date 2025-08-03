"""Question: Demonstrate best practices for comments and docstrings in Python.

Create examples showing proper commenting and documentation techniques
for different types of code structures.

Requirements:
1. Show different types of comments (inline, block, TODO)
2. Demonstrate proper docstring formats (Google, NumPy, Sphinx styles)
3. Show function, class, and module documentation
4. Demonstrate when to comment and when not to comment
5. Show examples of good vs bad comments

Example usage:
    calculator = Calculator()
    result = calculator.calculate_compound_interest(1000, 0.05, 10)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what makes a good comment vs bad comment
# - Start with simple examples
# - Practice different docstring styles
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
# - When should you write comments vs when should you avoid them?
# - What are the standard docstring formats?
# - How do you document functions, classes, and modules?
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


# Step 1: Basic comment types and when to use them
# ===============================================================================

# Explanation:
# Comments should explain WHY something is done, not WHAT is being done.
# The code itself should be clear enough to show what it does.

# This is a single-line comment explaining the purpose
def calculate_tax_rate(income: float) -> float:
    """Calculate tax rate based on income brackets."""
    
    # Tax brackets for 2025 (these change yearly, hence the comment)
    if income <= 10000:
        return 0.10  # 10% for low income
    elif income <= 50000:
        return 0.22  # 22% for middle income
    else:
        return 0.35  # 35% for high income


# Step 2: Block comments and TODO comments
# ===============================================================================

# Explanation:
# Block comments are used for longer explanations or complex algorithms.
# TODO comments help track future improvements or fixes needed.

# This is a single-line comment explaining the purpose
def calculate_tax_rate(income: float) -> float:
    """Calculate tax rate based on income brackets."""
    
    # Tax brackets for 2025 (these change yearly, hence the comment)
    if income <= 10000:
        return 0.10  # 10% for low income
    elif income <= 50000:
        return 0.22  # 22% for middle income
    else:
        return 0.35  # 35% for high income

"""
This is a multi-line block comment explaining a complex algorithm.

The compound interest calculation uses the formula:
A = P(1 + r/n)^(nt)

Where:
- A = final amount
- P = principal amount
- r = annual interest rate
- n = number of times interest is compounded per year
- t = time in years

This implementation assumes monthly compounding (n=12) for simplicity.
"""

def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest with monthly compounding."""
    
    # TODO: Add support for different compounding frequencies
    # TODO: Add input validation for negative values
    # FIXME: Handle edge case when rate is exactly 0
    
    n = 12  # Monthly compounding
    amount = principal * (1 + rate / n) ** (n * years)
    return round(amount, 2)


# Step 3: Google-style docstrings for functions
# ===============================================================================

# Explanation:
# Google-style docstrings are clean and readable. They use sections like
# Args, Returns, Raises, Example, etc.

# This is a single-line comment explaining the purpose
def calculate_tax_rate(income: float) -> float:
    """Calculate tax rate based on income brackets."""
    
    # Tax brackets for 2025 (these change yearly, hence the comment)
    if income <= 10000:
        return 0.10  # 10% for low income
    elif income <= 50000:
        return 0.22  # 22% for middle income
    else:
        return 0.35  # 35% for high income

"""
This is a multi-line block comment explaining a complex algorithm.

The compound interest calculation uses the formula:
A = P(1 + r/n)^(nt)

Where:
- A = final amount
- P = principal amount
- r = annual interest rate
- n = number of times interest is compounded per year
- t = time in years

This implementation assumes monthly compounding (n=12) for simplicity.
"""

def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest with monthly compounding."""
    
    # TODO: Add support for different compounding frequencies
    # TODO: Add input validation for negative values
    # FIXME: Handle edge case when rate is exactly 0
    
    n = 12  # Monthly compounding
    amount = principal * (1 + rate / n) ** (n * years)
    return round(amount, 2)

def calculate_loan_payment(principal: float, annual_rate: float, years: int) -> float:
    """Calculate monthly loan payment using the standard loan formula.
    
    Args:
        principal: The loan amount in dollars.
        annual_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years: Loan term in years.
    
    Returns:
        Monthly payment amount rounded to 2 decimal places.
    
    Raises:
        ValueError: If any parameter is negative or if rate/years is zero.
        
    Example:
        >>> calculate_loan_payment(100000, 0.05, 30)
        536.82
        
    Note:
        Uses the standard amortization formula:
        M = P * [r(1+r)^n] / [(1+r)^n - 1]
    """
    if principal < 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Principal and rate must be non-negative, years must be positive")
    
    if annual_rate == 0:
        return principal / (years * 12)  # Simple division for 0% interest
    
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    # Standard loan payment formula
    payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    
    return round(payment, 2)


# Step 4: Class docstrings and NumPy-style documentation
# ===============================================================================

# Explanation:
# Class docstrings should describe the purpose of the class and its main
# functionality. NumPy-style uses sections separated by dashes.

# This is a single-line comment explaining the purpose
def calculate_tax_rate(income: float) -> float:
    """Calculate tax rate based on income brackets."""
    
    # Tax brackets for 2025 (these change yearly, hence the comment)
    if income <= 10000:
        return 0.10  # 10% for low income
    elif income <= 50000:
        return 0.22  # 22% for middle income
    else:
        return 0.35  # 35% for high income

"""
This is a multi-line block comment explaining a complex algorithm.

The compound interest calculation uses the formula:
A = P(1 + r/n)^(nt)

Where:
- A = final amount
- P = principal amount
- r = annual interest rate
- n = number of times interest is compounded per year
- t = time in years

This implementation assumes monthly compounding (n=12) for simplicity.
"""

def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest with monthly compounding."""
    
    # TODO: Add support for different compounding frequencies
    # TODO: Add input validation for negative values
    # FIXME: Handle edge case when rate is exactly 0
    
    n = 12  # Monthly compounding
    amount = principal * (1 + rate / n) ** (n * years)
    return round(amount, 2)

def calculate_loan_payment(principal: float, annual_rate: float, years: int) -> float:
    """Calculate monthly loan payment using the standard loan formula.
    
    Args:
        principal: The loan amount in dollars.
        annual_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years: Loan term in years.
    
    Returns:
        Monthly payment amount rounded to 2 decimal places.
    
    Raises:
        ValueError: If any parameter is negative or if rate/years is zero.
        
    Example:
        >>> calculate_loan_payment(100000, 0.05, 30)
        536.82
        
    Note:
        Uses the standard amortization formula:
        M = P * [r(1+r)^n] / [(1+r)^n - 1]
    """
    if principal < 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Principal and rate must be non-negative, years must be positive")
    
    if annual_rate == 0:
        return principal / (years * 12)  # Simple division for 0% interest
    
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    # Standard loan payment formula
    payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    
    return round(payment, 2)

class Calculator:
    """A financial calculator for various monetary computations.
    
    This class provides methods for calculating taxes, compound interest,
    loan payments, and other financial metrics commonly used in
    personal finance applications.
    
    Attributes:
        precision (int): Number of decimal places for calculations.
        tax_year (int): Tax year for bracket calculations.
        
    Example:
        >>> calc = Calculator(precision=2, tax_year=2025)
        >>> calc.calculate_compound_interest(1000, 0.05, 10)
        1647.01
    """
    
    def __init__(self, precision: int = 2, tax_year: int = 2025):
        """Initialize the calculator with specified precision and tax year.
        
        Parameters
        ----------
        precision : int, optional
            Number of decimal places for rounding results (default is 2)
        tax_year : int, optional
            Tax year for bracket calculations (default is 2025)
        """
        self.precision = precision
        self.tax_year = tax_year
        
        # Initialize tax brackets based on year
        self._update_tax_brackets()
    
    def _update_tax_brackets(self):
        """Update tax brackets based on the current tax year.
        
        This is a private method that sets up the tax bracket thresholds
        and rates based on the specified tax year.
        """
        # Tax brackets change yearly - this is why we need comments
        if self.tax_year == 2025:
            self.tax_brackets = [
                (10000, 0.10),   # First bracket: 10%
                (50000, 0.22),   # Second bracket: 22%
                (float('inf'), 0.35)  # Top bracket: 35%
            ]
        else:
            # Default to 2025 brackets if year not supported
            # TODO: Add support for historical tax years
            self.tax_brackets = [
                (10000, 0.10),
                (50000, 0.22),
                (float('inf'), 0.35)
            ]


# Step 5: Complete class with Sphinx-style docstrings
# ===============================================================================

# Explanation:
# Sphinx-style docstrings use :param:, :type:, :returns:, etc.
# They're great for generating documentation with Sphinx.

# This is a single-line comment explaining the purpose
def calculate_tax_rate(income: float) -> float:
    """Calculate tax rate based on income brackets."""
    
    # Tax brackets for 2025 (these change yearly, hence the comment)
    if income <= 10000:
        return 0.10  # 10% for low income
    elif income <= 50000:
        return 0.22  # 22% for middle income
    else:
        return 0.35  # 35% for high income

"""
This is a multi-line block comment explaining a complex algorithm.

The compound interest calculation uses the formula:
A = P(1 + r/n)^(nt)

Where:
- A = final amount
- P = principal amount
- r = annual interest rate
- n = number of times interest is compounded per year
- t = time in years

This implementation assumes monthly compounding (n=12) for simplicity.
"""

def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest with monthly compounding."""
    
    # TODO: Add support for different compounding frequencies
    # TODO: Add input validation for negative values
    # FIXME: Handle edge case when rate is exactly 0
    
    n = 12  # Monthly compounding
    amount = principal * (1 + rate / n) ** (n * years)
    return round(amount, 2)

def calculate_loan_payment(principal: float, annual_rate: float, years: int) -> float:
    """Calculate monthly loan payment using the standard loan formula.
    
    Args:
        principal: The loan amount in dollars.
        annual_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years: Loan term in years.
    
    Returns:
        Monthly payment amount rounded to 2 decimal places.
    
    Raises:
        ValueError: If any parameter is negative or if rate/years is zero.
        
    Example:
        >>> calculate_loan_payment(100000, 0.05, 30)
        536.82
        
    Note:
        Uses the standard amortization formula:
        M = P * [r(1+r)^n] / [(1+r)^n - 1]
    """
    if principal < 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Principal and rate must be non-negative, years must be positive")
    
    if annual_rate == 0:
        return principal / (years * 12)  # Simple division for 0% interest
    
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    # Standard loan payment formula
    payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    
    return round(payment, 2)

class Calculator:
    """A financial calculator for various monetary computations.
    
    This class provides methods for calculating taxes, compound interest,
    loan payments, and other financial metrics commonly used in
    personal finance applications.
    
    Attributes:
        precision (int): Number of decimal places for calculations.
        tax_year (int): Tax year for bracket calculations.
        
    Example:
        >>> calc = Calculator(precision=2, tax_year=2025)
        >>> calc.calculate_compound_interest(1000, 0.05, 10)
        1647.01
    """
    
    def __init__(self, precision: int = 2, tax_year: int = 2025):
        """Initialize the calculator with specified precision and tax year.
        
        Parameters
        ----------
        precision : int, optional
            Number of decimal places for rounding results (default is 2)
        tax_year : int, optional
            Tax year for bracket calculations (default is 2025)
        """
        self.precision = precision
        self.tax_year = tax_year
        
        # Initialize tax brackets based on year
        self._update_tax_brackets()
    
    def _update_tax_brackets(self):
        """Update tax brackets based on the current tax year.
        
        This is a private method that sets up the tax bracket thresholds
        and rates based on the specified tax year.
        """
        # Tax brackets change yearly - this is why we need comments
        if self.tax_year == 2025:
            self.tax_brackets = [
                (10000, 0.10),   # First bracket: 10%
                (50000, 0.22),   # Second bracket: 22%
                (float('inf'), 0.35)  # Top bracket: 35%
            ]
        else:
            # Default to 2025 brackets if year not supported
            # TODO: Add support for historical tax years
            self.tax_brackets = [
                (10000, 0.10),
                (50000, 0.22),
                (float('inf'), 0.35)
            ]
    
    def calculate_tax_rate(self, income: float) -> float:
        """Calculate tax rate based on income brackets.
        
        :param income: Annual income in dollars
        :type income: float
        :returns: Tax rate as a decimal (e.g., 0.22 for 22%)
        :rtype: float
        :raises ValueError: If income is negative
        
        .. note::
           Tax brackets are updated annually and may change.
           
        .. warning::
           This is a simplified calculation for demonstration purposes.
        """
        if income < 0:
            raise ValueError("Income cannot be negative")
        
        # Find the appropriate tax bracket
        for threshold, rate in self.tax_brackets:
            if income <= threshold:
                return rate
        
        # Fallback (should never reach here due to inf threshold)
        return self.tax_brackets[-1][1]
    
    def calculate_compound_interest(self, principal: float, rate: float, years: int) -> float:
        """Calculate compound interest with monthly compounding.
        
        :param principal: Initial investment amount
        :type principal: float
        :param rate: Annual interest rate as decimal
        :type rate: float
        :param years: Investment period in years
        :type years: int
        :returns: Final amount after compound interest
        :rtype: float
        """
        # Input validation with descriptive error messages
        if principal < 0:
            raise ValueError("Principal amount cannot be negative")
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if years < 0:
            raise ValueError("Investment period cannot be negative")
        
        # Handle edge case of zero interest rate
        if rate == 0:
            return round(principal, self.precision)
        
        n = 12  # Monthly compounding frequency
        amount = principal * (1 + rate / n) ** (n * years)
        return round(amount, self.precision)


# Step 6: Good vs Bad comments and complete implementation
# ===============================================================================

# Explanation:
# This step shows examples of good vs bad comments and completes our
# Calculator class with proper documentation throughout.

# This is a single-line comment explaining the purpose
def calculate_tax_rate(income: float) -> float:
    """Calculate tax rate based on income brackets."""
    
    # Tax brackets for 2025 (these change yearly, hence the comment)
    if income <= 10000:
        return 0.10  # 10% for low income
    elif income <= 50000:
        return 0.22  # 22% for middle income
    else:
        return 0.35  # 35% for high income

"""
This is a multi-line block comment explaining a complex algorithm.

The compound interest calculation uses the formula:
A = P(1 + r/n)^(nt)

Where:
- A = final amount
- P = principal amount
- r = annual interest rate
- n = number of times interest is compounded per year
- t = time in years

This implementation assumes monthly compounding (n=12) for simplicity.
"""

def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest with monthly compounding."""
    
    # TODO: Add support for different compounding frequencies
    # TODO: Add input validation for negative values
    # FIXME: Handle edge case when rate is exactly 0
    
    n = 12  # Monthly compounding
    amount = principal * (1 + rate / n) ** (n * years)
    return round(amount, 2)

def calculate_loan_payment(principal: float, annual_rate: float, years: int) -> float:
    """Calculate monthly loan payment using the standard loan formula.
    
    Args:
        principal: The loan amount in dollars.
        annual_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years: Loan term in years.
    
    Returns:
        Monthly payment amount rounded to 2 decimal places.
    
    Raises:
        ValueError: If any parameter is negative or if rate/years is zero.
        
    Example:
        >>> calculate_loan_payment(100000, 0.05, 30)
        536.82
        
    Note:
        Uses the standard amortization formula:
        M = P * [r(1+r)^n] / [(1+r)^n - 1]
    """
    if principal < 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Principal and rate must be non-negative, years must be positive")
    
    if annual_rate == 0:
        return principal / (years * 12)  # Simple division for 0% interest
    
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    # Standard loan payment formula
    payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    
    return round(payment, 2)

class Calculator:
    """A financial calculator for various monetary computations.
    
    This class provides methods for calculating taxes, compound interest,
    loan payments, and other financial metrics commonly used in
    personal finance applications.
    
    Attributes:
        precision (int): Number of decimal places for calculations.
        tax_year (int): Tax year for bracket calculations.
        
    Example:
        >>> calc = Calculator(precision=2, tax_year=2025)
        >>> calc.calculate_compound_interest(1000, 0.05, 10)
        1647.01
    """
    
    def __init__(self, precision: int = 2, tax_year: int = 2025):
        """Initialize the calculator with specified precision and tax year.
        
        Parameters
        ----------
        precision : int, optional
            Number of decimal places for rounding results (default is 2)
        tax_year : int, optional
            Tax year for bracket calculations (default is 2025)
        """
        self.precision = precision
        self.tax_year = tax_year
        
        # Initialize tax brackets based on year
        self._update_tax_brackets()
    
    def _update_tax_brackets(self):
        """Update tax brackets based on the current tax year.
        
        This is a private method that sets up the tax bracket thresholds
        and rates based on the specified tax year.
        """
        # Tax brackets change yearly - this is why we need comments
        if self.tax_year == 2025:
            self.tax_brackets = [
                (10000, 0.10),   # First bracket: 10%
                (50000, 0.22),   # Second bracket: 22%
                (float('inf'), 0.35)  # Top bracket: 35%
            ]
        else:
            # Default to 2025 brackets if year not supported
            # TODO: Add support for historical tax years
            self.tax_brackets = [
                (10000, 0.10),
                (50000, 0.22),
                (float('inf'), 0.35)
            ]
    
    def calculate_tax_rate(self, income: float) -> float:
        """Calculate tax rate based on income brackets.
        
        :param income: Annual income in dollars
        :type income: float
        :returns: Tax rate as a decimal (e.g., 0.22 for 22%)
        :rtype: float
        :raises ValueError: If income is negative
        
        .. note::
           Tax brackets are updated annually and may change.
           
        .. warning::
           This is a simplified calculation for demonstration purposes.
        """
        if income < 0:
            raise ValueError("Income cannot be negative")
        
        # Find the appropriate tax bracket
        for threshold, rate in self.tax_brackets:
            if income <= threshold:
                return rate
        
        # Fallback (should never reach here due to inf threshold)
        return self.tax_brackets[-1][1]
    
    def calculate_compound_interest(self, principal: float, rate: float, years: int) -> float:
        """Calculate compound interest with monthly compounding.
        
        :param principal: Initial investment amount
        :type principal: float
        :param rate: Annual interest rate as decimal
        :type rate: float
        :param years: Investment period in years
        :type years: int
        :returns: Final amount after compound interest
        :rtype: float
        """
        # Input validation with descriptive error messages
        if principal < 0:
            raise ValueError("Principal amount cannot be negative")
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if years < 0:
            raise ValueError("Investment period cannot be negative")
        
        # Handle edge case of zero interest rate
        if rate == 0:
            return round(principal, self.precision)
        
        n = 12  # Monthly compounding frequency
        amount = principal * (1 + rate / n) ** (n * years)
        return round(amount, self.precision)
    
    def calculate_loan_payment(self, principal: float, annual_rate: float, years: int) -> float:
        """Calculate monthly loan payment using amortization formula.
        
        Args:
            principal: Loan amount in dollars.
            annual_rate: Annual interest rate as decimal.
            years: Loan term in years.
            
        Returns:
            Monthly payment amount.
            
        Raises:
            ValueError: If any parameter is invalid.
        """
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if annual_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if years <= 0:
            raise ValueError("Loan term must be positive")
        
        # Special case: zero interest rate
        if annual_rate == 0:
            return round(principal / (years * 12), self.precision)
        
        monthly_rate = annual_rate / 12
        num_payments = years * 12
        
        # Apply standard amortization formula
        payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                  ((1 + monthly_rate) ** num_payments - 1)
        
        return round(payment, self.precision)


# Examples of GOOD vs BAD comments
# ===============================================================================

# BAD COMMENT EXAMPLES (Don't do this!):
def bad_example():
    """Examples of what NOT to do with comments."""
    
    # BAD: Stating the obvious
    x = 5  # Set x to 5
    
    # BAD: Redundant with code
    if x > 0:  # Check if x is greater than 0
        print("Positive")  # Print "Positive"
    
    # BAD: Outdated comment
    y = x * 2  # Multiply by 3 (comment is wrong!)
    
    # BAD: Commented out code without explanation
    # z = x + y
    # print(z)
    
    return x + y

# GOOD COMMENT EXAMPLES (Do this!):
def good_example():
    """Examples of effective commenting practices."""
    
    # GOOD: Explain WHY, not WHAT
    timeout = 30  # API calls timeout after 30 seconds per company policy
    
    # GOOD: Explain business logic
    if timeout > 25:  # Anything over 25s is considered slow for user experience
        print("Warning: Slow response")
    
    # GOOD: Explain complex calculations
    # Using Wilson score interval for 95% confidence
    # This provides better ranking than simple average for small sample sizes
    score = (positive_votes + 1.9208) / (total_votes + 3.8416)
    
    # GOOD: Explain workarounds or hacks
    # Workaround for Python 3.8 compatibility issue with asyncio
    import sys
    if sys.version_info >= (3, 9):
        # Use new syntax available in 3.9+
        pass
    
    return score


# Step 7: Demonstration and best practices summary
# ===============================================================================

# Explanation:
# This final step demonstrates the complete implementation and summarizes
# all the best practices for comments and docstrings.

# This is a single-line comment explaining the purpose
def calculate_tax_rate(income: float) -> float:
    """Calculate tax rate based on income brackets."""
    
    # Tax brackets for 2025 (these change yearly, hence the comment)
    if income <= 10000:
        return 0.10  # 10% for low income
    elif income <= 50000:
        return 0.22  # 22% for middle income
    else:
        return 0.35  # 35% for high income

"""
This is a multi-line block comment explaining a complex algorithm.

The compound interest calculation uses the formula:
A = P(1 + r/n)^(nt)

Where:
- A = final amount
- P = principal amount
- r = annual interest rate
- n = number of times interest is compounded per year
- t = time in years

This implementation assumes monthly compounding (n=12) for simplicity.
"""

def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest with monthly compounding."""
    
    # TODO: Add support for different compounding frequencies
    # TODO: Add input validation for negative values
    # FIXME: Handle edge case when rate is exactly 0
    
    n = 12  # Monthly compounding
    amount = principal * (1 + rate / n) ** (n * years)
    return round(amount, 2)

def calculate_loan_payment(principal: float, annual_rate: float, years: int) -> float:
    """Calculate monthly loan payment using the standard loan formula.
    
    Args:
        principal: The loan amount in dollars.
        annual_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years: Loan term in years.
    
    Returns:
        Monthly payment amount rounded to 2 decimal places.
    
    Raises:
        ValueError: If any parameter is negative or if rate/years is zero.
        
    Example:
        >>> calculate_loan_payment(100000, 0.05, 30)
        536.82
        
    Note:
        Uses the standard amortization formula:
        M = P * [r(1+r)^n] / [(1+r)^n - 1]
    """
    if principal < 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Principal and rate must be non-negative, years must be positive")
    
    if annual_rate == 0:
        return principal / (years * 12)  # Simple division for 0% interest
    
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    # Standard loan payment formula
    payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    
    return round(payment, 2)

class Calculator:
    """A financial calculator for various monetary computations.
    
    This class provides methods for calculating taxes, compound interest,
    loan payments, and other financial metrics commonly used in
    personal finance applications.
    
    Attributes:
        precision (int): Number of decimal places for calculations.
        tax_year (int): Tax year for bracket calculations.
        
    Example:
        >>> calc = Calculator(precision=2, tax_year=2025)
        >>> calc.calculate_compound_interest(1000, 0.05, 10)
        1647.01
    """
    
    def __init__(self, precision: int = 2, tax_year: int = 2025):
        """Initialize the calculator with specified precision and tax year.
        
        Parameters
        ----------
        precision : int, optional
            Number of decimal places for rounding results (default is 2)
        tax_year : int, optional
            Tax year for bracket calculations (default is 2025)
        """
        self.precision = precision
        self.tax_year = tax_year
        
        # Initialize tax brackets based on year
        self._update_tax_brackets()
    
    def _update_tax_brackets(self):
        """Update tax brackets based on the current tax year.
        
        This is a private method that sets up the tax bracket thresholds
        and rates based on the specified tax year.
        """
        # Tax brackets change yearly - this is why we need comments
        if self.tax_year == 2025:
            self.tax_brackets = [
                (10000, 0.10),   # First bracket: 10%
                (50000, 0.22),   # Second bracket: 22%
                (float('inf'), 0.35)  # Top bracket: 35%
            ]
        else:
            # Default to 2025 brackets if year not supported
            # TODO: Add support for historical tax years
            self.tax_brackets = [
                (10000, 0.10),
                (50000, 0.22),
                (float('inf'), 0.35)
            ]
    
    def calculate_tax_rate(self, income: float) -> float:
        """Calculate tax rate based on income brackets.
        
        :param income: Annual income in dollars
        :type income: float
        :returns: Tax rate as a decimal (e.g., 0.22 for 22%)
        :rtype: float
        :raises ValueError: If income is negative
        
        .. note::
           Tax brackets are updated annually and may change.
           
        .. warning::
           This is a simplified calculation for demonstration purposes.
        """
        if income < 0:
            raise ValueError("Income cannot be negative")
        
        # Find the appropriate tax bracket
        for threshold, rate in self.tax_brackets:
            if income <= threshold:
                return rate
        
        # Fallback (should never reach here due to inf threshold)
        return self.tax_brackets[-1][1]
    
    def calculate_compound_interest(self, principal: float, rate: float, years: int) -> float:
        """Calculate compound interest with monthly compounding.
        
        :param principal: Initial investment amount
        :type principal: float
        :param rate: Annual interest rate as decimal
        :type rate: float
        :param years: Investment period in years
        :type years: int
        :returns: Final amount after compound interest
        :rtype: float
        """
        # Input validation with descriptive error messages
        if principal < 0:
            raise ValueError("Principal amount cannot be negative")
        if rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if years < 0:
            raise ValueError("Investment period cannot be negative")
        
        # Handle edge case of zero interest rate
        if rate == 0:
            return round(principal, self.precision)
        
        n = 12  # Monthly compounding frequency
        amount = principal * (1 + rate / n) ** (n * years)
        return round(amount, self.precision)
    
    def calculate_loan_payment(self, principal: float, annual_rate: float, years: int) -> float:
        """Calculate monthly loan payment using amortization formula.
        
        Args:
            principal: Loan amount in dollars.
            annual_rate: Annual interest rate as decimal.
            years: Loan term in years.
            
        Returns:
            Monthly payment amount.
            
        Raises:
            ValueError: If any parameter is invalid.
        """
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be positive")
        if annual_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if years <= 0:
            raise ValueError("Loan term must be positive")
        
        # Special case: zero interest rate
        if annual_rate == 0:
            return round(principal / (years * 12), self.precision)
        
        monthly_rate = annual_rate / 12
        num_payments = years * 12
        
        # Apply standard amortization formula
        payment = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                  ((1 + monthly_rate) ** num_payments - 1)
        
        return round(payment, self.precision)


# Examples of GOOD vs BAD comments
# ===============================================================================

# BAD COMMENT EXAMPLES (Don't do this!):
def bad_example():
    """Examples of what NOT to do with comments."""
    
    # BAD: Stating the obvious
    x = 5  # Set x to 5
    
    # BAD: Redundant with code
    if x > 0:  # Check if x is greater than 0
        print("Positive")  # Print "Positive"
    
    # BAD: Outdated comment
    y = x * 2  # Multiply by 3 (comment is wrong!)
    
    # BAD: Commented out code without explanation
    # z = x + y
    # print(z)
    
    return x + y

# GOOD COMMENT EXAMPLES (Do this!):
def good_example():
    """Examples of effective commenting practices."""
    
    # GOOD: Explain WHY, not WHAT
    timeout = 30  # API calls timeout after 30 seconds per company policy
    
    # GOOD: Explain business logic
    if timeout > 25:  # Anything over 25s is considered slow for user experience
        print("Warning: Slow response")
    
    # GOOD: Explain complex calculations
    # Using Wilson score interval for 95% confidence
    # This provides better ranking than simple average for small sample sizes
    score = (positive_votes + 1.9208) / (total_votes + 3.8416)
    
    # GOOD: Explain workarounds or hacks
    # Workaround for Python 3.8 compatibility issue with asyncio
    import sys
    if sys.version_info >= (3, 9):
        # Use new syntax available in 3.9+
        pass
    
    return score

# Demonstration of the complete implementation
if __name__ == "__main__":
    """Demonstrate the Calculator class and various commenting styles."""
    
    print("=== Financial Calculator Demo ===")
    
    # Create calculator instance with default settings
    calc = Calculator()
    
    # Test compound interest calculation
    principal = 1000
    rate = 0.05  # 5% annual interest
    years = 10
    
    result = calc.calculate_compound_interest(principal, rate, years)
    print(f"Compound Interest: ${principal} at {rate*100}% for {years} years = ${result}")
    
    # Test tax rate calculation
    income = 75000
    tax_rate = calc.calculate_tax_rate(income)
    print(f"Tax Rate: Income of ${income} has tax rate of {tax_rate*100}%")
    
    # Test loan payment calculation
    loan_amount = 200000
    loan_rate = 0.04  # 4% annual interest
    loan_years = 30
    
    payment = calc.calculate_loan_payment(loan_amount, loan_rate, loan_years)
    print(f"Loan Payment: ${loan_amount} at {loan_rate*100}% for {loan_years} years = ${payment}/month")


# ===============================================================================
#                           BEST PRACTICES SUMMARY
# ===============================================================================

"""
COMMENTS AND DOCSTRINGS BEST PRACTICES:

1. COMMENT TYPES:
   - Single-line comments (#): For brief explanations
   - Multi-line comments ('''): For complex algorithm explanations
   - TODO/FIXME: For tracking future improvements
   - Inline comments: Sparingly, for clarification

2. DOCSTRING STYLES:
   - Google Style: Clean, readable, good for teams
   - NumPy Style: Great for scientific computing
   - Sphinx Style: Excellent for auto-documentation

3. WHEN TO COMMENT:
   ✅ DO:
   - Explain WHY something is done
   - Document business logic and rules
   - Explain complex algorithms
   - Note workarounds or hacks
   - Document edge cases
   - Explain non-obvious code

   ❌ DON'T:
   - State the obvious
   - Repeat what code clearly shows
   - Leave outdated comments
   - Comment out code without explanation
   - Write comments that don't add value

4. DOCSTRING REQUIREMENTS:
   - Every public function, class, and module should have docstrings
   - Include parameters, return values, and exceptions
   - Provide examples when helpful
   - Keep docstrings up-to-date with code changes

5. MAINTENANCE:
   - Update comments when code changes
   - Remove outdated or incorrect comments
   - Use consistent style throughout project
   - Review comments during code reviews

Remember: Good code is self-documenting, but great code has strategic
comments that explain the reasoning behind the implementation!
"""


