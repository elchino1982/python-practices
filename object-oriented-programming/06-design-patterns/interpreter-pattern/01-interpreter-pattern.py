"""Question: Implement the Interpreter pattern to define grammar and interpret language expressions.

Create a simple calculator that can interpret and evaluate mathematical expressions
with variables, using the Interpreter pattern to parse and execute expressions.

Requirements:
1. Create Expression interface with interpret() method
2. Implement terminal expressions (Number, Variable)
3. Implement non-terminal expressions (Add, Subtract, Multiply, Divide)
4. Create Context class to store variable values
5. Build expression trees for complex expressions
6. Demonstrate parsing and evaluation of expressions

Example usage:
    context = Context()
    context.set_variable("x", 10)
    context.set_variable("y", 5)
    expression = AddExpression(Variable("x"), Variable("y"))
    result = expression.interpret(context)  # Returns 15
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!

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
# the complete thought process.
#
# ===============================================================================


# Step 1: Import modules and create the Expression interface and Context class
# ===============================================================================

# Explanation:
# The Interpreter pattern starts with an abstract expression interface that defines
# the interpret method. We also need a Context class to store variable values.

from abc import ABC, abstractmethod
from typing import Dict, Any

class Context:
    """Context class to store variable values and state."""
    
    def __init__(self):
        self._variables: Dict[str, float] = {}
    
    def set_variable(self, name: str, value: float):
        """Set a variable value in the context."""
        self._variables[name] = value
    
    def get_variable(self, name: str) -> float:
        """Get a variable value from the context."""
        if name not in self._variables:
            raise ValueError(f"Variable '{name}' is not defined")
        return self._variables[name]
    
    def has_variable(self, name: str) -> bool:
        """Check if a variable exists in the context."""
        return name in self._variables

class Expression(ABC):
    """Abstract expression interface."""
    
    @abstractmethod
    def interpret(self, context: Context) -> float:
        """Interpret the expression and return the result."""
        pass

# What we accomplished in this step:
# - Created the Context class to store variable values
# - Created the abstract Expression interface with interpret method


# Step 2: Create terminal expressions (Number and Variable)
# ===============================================================================

# Explanation:
# Terminal expressions are the leaf nodes in the expression tree. They don't
# contain other expressions. Number represents literal values, Variable represents named values.

from abc import ABC, abstractmethod
from typing import Dict, Any

class Context:
    """Context class to store variable values and state."""
    
    def __init__(self):
        self._variables: Dict[str, float] = {}
    
    def set_variable(self, name: str, value: float):
        """Set a variable value in the context."""
        self._variables[name] = value
    
    def get_variable(self, name: str) -> float:
        """Get a variable value from the context."""
        if name not in self._variables:
            raise ValueError(f"Variable '{name}' is not defined")
        return self._variables[name]
    
    def has_variable(self, name: str) -> bool:
        """Check if a variable exists in the context."""
        return name in self._variables

class Expression(ABC):
    """Abstract expression interface."""
    
    @abstractmethod
    def interpret(self, context: Context) -> float:
        """Interpret the expression and return the result."""
        pass

class Number(Expression):
    """Terminal expression for numeric literals."""
    
    def __init__(self, value: float):
        self.value = value
    
    def interpret(self, context: Context) -> float:
        """Return the numeric value."""
        return self.value
    
    def __str__(self):
        return str(self.value)

class Variable(Expression):
    """Terminal expression for variables."""
    
    def __init__(self, name: str):
        self.name = name
    
    def interpret(self, context: Context) -> float:
        """Return the variable value from context."""
        return context.get_variable(self.name)
    
    def __str__(self):
        return self.name

# What we accomplished in this step:
# - Created Number class for literal numeric values
# - Created Variable class for named variables that lookup values in context
# - Both implement the Expression interface


# Step 3: Create non-terminal expressions for arithmetic operations
# ===============================================================================

# Explanation:
# Non-terminal expressions contain other expressions and perform operations on them.
# These represent the internal nodes of the expression tree.

from abc import ABC, abstractmethod
from typing import Dict, Any

class Context:
    """Context class to store variable values and state."""
    
    def __init__(self):
        self._variables: Dict[str, float] = {}
    
    def set_variable(self, name: str, value: float):
        """Set a variable value in the context."""
        self._variables[name] = value
    
    def get_variable(self, name: str) -> float:
        """Get a variable value from the context."""
        if name not in self._variables:
            raise ValueError(f"Variable '{name}' is not defined")
        return self._variables[name]
    
    def has_variable(self, name: str) -> bool:
        """Check if a variable exists in the context."""
        return name in self._variables

class Expression(ABC):
    """Abstract expression interface."""
    
    @abstractmethod
    def interpret(self, context: Context) -> float:
        """Interpret the expression and return the result."""
        pass

class Number(Expression):
    """Terminal expression for numeric literals."""
    
    def __init__(self, value: float):
        self.value = value
    
    def interpret(self, context: Context) -> float:
        """Return the numeric value."""
        return self.value
    
    def __str__(self):
        return str(self.value)

class Variable(Expression):
    """Terminal expression for variables."""
    
    def __init__(self, name: str):
        self.name = name
    
    def interpret(self, context: Context) -> float:
        """Return the variable value from context."""
        return context.get_variable(self.name)
    
    def __str__(self):
        return self.name

class AddExpression(Expression):
    """Non-terminal expression for addition."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Add the results of left and right expressions."""
        return self.left.interpret(context) + self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} + {self.right})"

class SubtractExpression(Expression):
    """Non-terminal expression for subtraction."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Subtract right expression from left expression."""
        return self.left.interpret(context) - self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} - {self.right})"

class MultiplyExpression(Expression):
    """Non-terminal expression for multiplication."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Multiply the results of left and right expressions."""
        return self.left.interpret(context) * self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} * {self.right})"

class DivideExpression(Expression):
    """Non-terminal expression for division."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Divide left expression by right expression."""
        right_value = self.right.interpret(context)
        if right_value == 0:
            raise ValueError("Division by zero")
        return self.left.interpret(context) / right_value
    
    def __str__(self):
        return f"({self.left} / {self.right})"

# What we accomplished in this step:
# - Created AddExpression for addition operations
# - Created SubtractExpression for subtraction operations
# - Created MultiplyExpression for multiplication operations
# - Created DivideExpression for division operations with zero-division protection
# - All non-terminal expressions contain two child expressions


# Step 4: Create a simple expression parser
# ===============================================================================

# Explanation:
# A parser helps build expression trees from string representations.
# This is a simple parser for basic arithmetic expressions.

from abc import ABC, abstractmethod
from typing import Dict, Any, List
import re

class Context:
    """Context class to store variable values and state."""
    
    def __init__(self):
        self._variables: Dict[str, float] = {}
    
    def set_variable(self, name: str, value: float):
        """Set a variable value in the context."""
        self._variables[name] = value
    
    def get_variable(self, name: str) -> float:
        """Get a variable value from the context."""
        if name not in self._variables:
            raise ValueError(f"Variable '{name}' is not defined")
        return self._variables[name]
    
    def has_variable(self, name: str) -> bool:
        """Check if a variable exists in the context."""
        return name in self._variables

class Expression(ABC):
    """Abstract expression interface."""
    
    @abstractmethod
    def interpret(self, context: Context) -> float:
        """Interpret the expression and return the result."""
        pass

class Number(Expression):
    """Terminal expression for numeric literals."""
    
    def __init__(self, value: float):
        self.value = value
    
    def interpret(self, context: Context) -> float:
        """Return the numeric value."""
        return self.value
    
    def __str__(self):
        return str(self.value)

class Variable(Expression):
    """Terminal expression for variables."""
    
    def __init__(self, name: str):
        self.name = name
    
    def interpret(self, context: Context) -> float:
        """Return the variable value from context."""
        return context.get_variable(self.name)
    
    def __str__(self):
        return self.name

class AddExpression(Expression):
    """Non-terminal expression for addition."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Add the results of left and right expressions."""
        return self.left.interpret(context) + self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} + {self.right})"

class SubtractExpression(Expression):
    """Non-terminal expression for subtraction."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Subtract right expression from left expression."""
        return self.left.interpret(context) - self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} - {self.right})"

class MultiplyExpression(Expression):
    """Non-terminal expression for multiplication."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Multiply the results of left and right expressions."""
        return self.left.interpret(context) * self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} * {self.right})"

class DivideExpression(Expression):
    """Non-terminal expression for division."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Divide left expression by right expression."""
        right_value = self.right.interpret(context)
        if right_value == 0:
            raise ValueError("Division by zero")
        return self.left.interpret(context) / right_value
    
    def __str__(self):
        return f"({self.left} / {self.right})"

class ExpressionParser:
    """Simple parser for arithmetic expressions."""
    
    def __init__(self):
        self.operators = {
            '+': AddExpression,
            '-': SubtractExpression,
            '*': MultiplyExpression,
            '/': DivideExpression
        }
    
    def parse(self, expression_str: str) -> Expression:
        """Parse a string expression into an Expression tree."""
        # Remove spaces
        expression_str = expression_str.replace(' ', '')
        
        # Simple tokenization
        tokens = self._tokenize(expression_str)
        
        # Build expression tree (simple left-to-right evaluation)
        return self._build_expression(tokens)
    
    def _tokenize(self, expression_str: str) -> List[str]:
        """Tokenize the expression string."""
        # Simple regex to split on operators while keeping them
        pattern = r'([+\-*/()])'
        tokens = re.split(pattern, expression_str)
        return [token for token in tokens if token]
    
    def _build_expression(self, tokens: List[str]) -> Expression:
        """Build expression tree from tokens (simplified)."""
        if len(tokens) == 1:
            # Single token - either number or variable
            token = tokens[0]
            if token.replace('.', '').replace('-', '').isdigit():
                return Number(float(token))
            else:
                return Variable(token)
        
        # Find the main operator (rightmost + or -, then * or /)
        main_op_index = -1
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in ['+', '-']:
                main_op_index = i
                break
        
        if main_op_index == -1:
            for i in range(len(tokens) - 1, -1, -1):
                if tokens[i] in ['*', '/']:
                    main_op_index = i
                    break
        
        if main_op_index == -1:
            raise ValueError("Invalid expression")
        
        operator = tokens[main_op_index]
        left_tokens = tokens[:main_op_index]
        right_tokens = tokens[main_op_index + 1:]
        
        left_expr = self._build_expression(left_tokens)
        right_expr = self._build_expression(right_tokens)
        
        return self.operators[operator](left_expr, right_expr)

# What we accomplished in this step:
# - Created ExpressionParser class to build expression trees from strings
# - Added tokenization to split expressions into components
# - Implemented simple expression tree building with operator precedence
# - Parser can handle numbers, variables, and basic arithmetic operations


# Step 5: Test the complete Interpreter pattern implementation
# ===============================================================================

# Explanation:
# Let's test our Interpreter pattern implementation with various expressions
# to demonstrate how it works with variables and complex expressions.

from abc import ABC, abstractmethod
from typing import Dict, Any, List
import re

class Context:
    """Context class to store variable values and state."""
    
    def __init__(self):
        self._variables: Dict[str, float] = {}
    
    def set_variable(self, name: str, value: float):
        """Set a variable value in the context."""
        self._variables[name] = value
    
    def get_variable(self, name: str) -> float:
        """Get a variable value from the context."""
        if name not in self._variables:
            raise ValueError(f"Variable '{name}' is not defined")
        return self._variables[name]
    
    def has_variable(self, name: str) -> bool:
        """Check if a variable exists in the context."""
        return name in self._variables

class Expression(ABC):
    """Abstract expression interface."""
    
    @abstractmethod
    def interpret(self, context: Context) -> float:
        """Interpret the expression and return the result."""
        pass

class Number(Expression):
    """Terminal expression for numeric literals."""
    
    def __init__(self, value: float):
        self.value = value
    
    def interpret(self, context: Context) -> float:
        """Return the numeric value."""
        return self.value
    
    def __str__(self):
        return str(self.value)

class Variable(Expression):
    """Terminal expression for variables."""
    
    def __init__(self, name: str):
        self.name = name
    
    def interpret(self, context: Context) -> float:
        """Return the variable value from context."""
        return context.get_variable(self.name)
    
    def __str__(self):
        return self.name

class AddExpression(Expression):
    """Non-terminal expression for addition."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Add the results of left and right expressions."""
        return self.left.interpret(context) + self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} + {self.right})"

class SubtractExpression(Expression):
    """Non-terminal expression for subtraction."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Subtract right expression from left expression."""
        return self.left.interpret(context) - self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} - {self.right})"

class MultiplyExpression(Expression):
    """Non-terminal expression for multiplication."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Multiply the results of left and right expressions."""
        return self.left.interpret(context) * self.right.interpret(context)
    
    def __str__(self):
        return f"({self.left} * {self.right})"

class DivideExpression(Expression):
    """Non-terminal expression for division."""
    
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def interpret(self, context: Context) -> float:
        """Divide left expression by right expression."""
        right_value = self.right.interpret(context)
        if right_value == 0:
            raise ValueError("Division by zero")
        return self.left.interpret(context) / right_value
    
    def __str__(self):
        return f"({self.left} / {self.right})"

class ExpressionParser:
    """Simple parser for arithmetic expressions."""
    
    def __init__(self):
        self.operators = {
            '+': AddExpression,
            '-': SubtractExpression,
            '*': MultiplyExpression,
            '/': DivideExpression
        }
    
    def parse(self, expression_str: str) -> Expression:
        """Parse a string expression into an Expression tree."""
        # Remove spaces
        expression_str = expression_str.replace(' ', '')
        
        # Simple tokenization
        tokens = self._tokenize(expression_str)
        
        # Build expression tree (simple left-to-right evaluation)
        return self._build_expression(tokens)
    
    def _tokenize(self, expression_str: str) -> List[str]:
        """Tokenize the expression string."""
        # Simple regex to split on operators while keeping them
        pattern = r'([+\-*/()])'
        tokens = re.split(pattern, expression_str)
        return [token for token in tokens if token]
    
    def _build_expression(self, tokens: List[str]) -> Expression:
        """Build expression tree from tokens (simplified)."""
        if len(tokens) == 1:
            # Single token - either number or variable
            token = tokens[0]
            if token.replace('.', '').replace('-', '').isdigit():
                return Number(float(token))
            else:
                return Variable(token)
        
        # Find the main operator (rightmost + or -, then * or /)
        main_op_index = -1
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in ['+', '-']:
                main_op_index = i
                break
        
        if main_op_index == -1:
            for i in range(len(tokens) - 1, -1, -1):
                if tokens[i] in ['*', '/']:
                    main_op_index = i
                    break
        
        if main_op_index == -1:
            raise ValueError("Invalid expression")
        
        operator = tokens[main_op_index]
        left_tokens = tokens[:main_op_index]
        right_tokens = tokens[main_op_index + 1:]
        
        left_expr = self._build_expression(left_tokens)
        right_expr = self._build_expression(right_tokens)
        
        return self.operators[operator](left_expr, right_expr)

print("=== Testing Interpreter Pattern ===\n")

# Create context and set variables
context = Context()
context.set_variable("x", 10)
context.set_variable("y", 5)
context.set_variable("z", 2)

print("Variables in context:")
print(f"x = {context.get_variable('x')}")
print(f"y = {context.get_variable('y')}")
print(f"z = {context.get_variable('z')}")
print()

# Test 1: Manual expression building
print("1. Manual Expression Building:")
expression1 = AddExpression(Variable("x"), Variable("y"))
print(f"Expression: {expression1}")
print(f"Result: {expression1.interpret(context)}")
print()

# Test 2: Complex manual expression
print("2. Complex Manual Expression:")
expression2 = MultiplyExpression(
    AddExpression(Variable("x"), Variable("y")),
    SubtractExpression(Variable("x"), Variable("z"))
)
print(f"Expression: {expression2}")
print(f"Result: {expression2.interpret(context)}")
print()

# Test 3: Using parser for simple expressions
print("3. Using Parser for Simple Expressions:")
parser = ExpressionParser()

simple_expressions = ["x+y", "x-z", "x*y", "x/z"]
for expr_str in simple_expressions:
    try:
        expression = parser.parse(expr_str)
        result = expression.interpret(context)
        print(f"'{expr_str}' = {result}")
    except Exception as e:
        print(f"Error parsing '{expr_str}': {e}")
print()

# Test 4: Numeric expressions
print("4. Numeric Expressions:")
numeric_expressions = ["5+3", "10-4", "6*7", "20/4"]
for expr_str in numeric_expressions:
    try:
        expression = parser.parse(expr_str)
        result = expression.interpret(context)
        print(f"'{expr_str}' = {result}")
    except Exception as e:
        print(f"Error parsing '{expr_str}': {e}")
print()

# Test 5: Mixed expressions
print("5. Mixed Expressions (numbers and variables):")
mixed_expressions = ["x+5", "10-y", "z*3", "20/y"]
for expr_str in mixed_expressions:
    try:
        expression = parser.parse(expr_str)
        result = expression.interpret(context)
        print(f"'{expr_str}' = {result}")
    except Exception as e:
        print(f"Error parsing '{expr_str}': {e}")
print()

# Test 6: Error handling
print("6. Error Handling:")
try:
    undefined_var = Variable("undefined")
    undefined_var.interpret(context)
except ValueError as e:
    print(f"Expected error for undefined variable: {e}")

try:
    division_by_zero = DivideExpression(Number(10), Number(0))
    division_by_zero.interpret(context)
except ValueError as e:
    print(f"Expected error for division by zero: {e}")

# What we accomplished in this step:
# - Tested manual expression building with variables
# - Tested complex nested expressions
# - Demonstrated parser usage with simple expressions
# - Tested numeric-only expressions
# - Tested mixed expressions with numbers and variables
# - Demonstrated proper error handling for undefined variables and division by zero


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step Interpreter pattern solution!
#
# Key concepts learned:
# - Interpreter pattern structure and purpose
# - Abstract expression interface for grammar rules
# - Terminal expressions (Number, Variable) for leaf nodes
# - Non-terminal expressions (Add, Subtract, etc.) for operations
# - Context class for storing variable state
# - Expression tree building and evaluation
# - Simple parsing for string-to-expression conversion
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each component is necessary
# 4. Experiment with modifications (try adding power operator!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================