"""Question: Create a class Strategy that uses the Strategy pattern to define
a family of algorithms. Implement strategies for Addition and Subtraction.
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
# - What is the Strategy pattern and when is it useful?
# - How do you create an abstract strategy interface?
# - How do concrete strategies implement different algorithms?
# - How does the context use strategies interchangeably?
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


# Step 1: Define the abstract Strategy class
# ===============================================================================

# Explanation:
# Let's start by creating the abstract Strategy class. This defines the interface
# that all concrete strategies must implement.

class Strategy:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement this method")

# What we accomplished in this step:
# - Created abstract Strategy class with execute method
# - Used NotImplementedError to enforce implementation in subclasses


# Step 2: Create concrete strategy classes
# ===============================================================================

# Explanation:
# Now let's create concrete strategy classes that implement different algorithms.
# Each strategy will perform a different mathematical operation.

class Strategy:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement this method")

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

# What we accomplished in this step:
# - Created Addition and Subtraction strategy classes
# - Each implements the execute method with different algorithms


# Step 3: Create the Context class
# ===============================================================================

# Explanation:
# The Context class uses a strategy to perform operations. It can switch
# between different strategies at runtime.

class Strategy:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement this method")

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# What we accomplished in this step:
# - Created Context class that holds current strategy
# - Added methods to change strategy and execute operations


# Step 4: Test our basic Strategy pattern
# ===============================================================================

# Explanation:
# Let's test our Strategy pattern by creating a context with different strategies
# and observing how the algorithm changes.

class Strategy:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement this method")

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# Test our basic Strategy pattern:
print("=== Testing Basic Strategy Pattern ===")

context = Context(Addition())
result1 = context.execute_strategy(5, 3)
print(f"Addition strategy: 5 + 3 = {result1}")

context.set_strategy(Subtraction())
result2 = context.execute_strategy(5, 3)
print(f"Subtraction strategy: 5 - 3 = {result2}")

context.set_strategy(Addition())
result3 = context.execute_strategy(10, 7)
print(f"Back to addition: 10 + 7 = {result3}")

# What we accomplished in this step:
# - Created context with initial strategy
# - Demonstrated strategy changes and different algorithms
# - Verified that pattern works correctly


# Step 5: Enhanced Strategy pattern with more operations
# ===============================================================================

# Explanation:
# Let's create a more comprehensive calculator with multiple mathematical
# operations and error handling.

class MathStrategy:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_name(self):
        raise NotImplementedError("Subclasses must implement this method")

class AdditionStrategy(MathStrategy):
    def execute(self, a, b):
        return a + b
    
    def get_name(self):
        return "Addition"

class SubtractionStrategy(MathStrategy):
    def execute(self, a, b):
        return a - b
    
    def get_name(self):
        return "Subtraction"

class MultiplicationStrategy(MathStrategy):
    def execute(self, a, b):
        return a * b
    
    def get_name(self):
        return "Multiplication"

class DivisionStrategy(MathStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def get_name(self):
        return "Division"

class PowerStrategy(MathStrategy):
    def execute(self, a, b):
        return a ** b
    
    def get_name(self):
        return "Power"

class Calculator:
    def __init__(self, strategy=None):
        self._strategy = strategy
        self.history = []

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if self._strategy is None:
            raise ValueError("No strategy set")
        
        try:
            result = self._strategy.execute(a, b)
            operation = f"{a} {self._get_symbol()} {b} = {result}"
            self.history.append(operation)
            return result
        except Exception as e:
            error_msg = f"Error in {self._strategy.get_name()}: {str(e)}"
            self.history.append(error_msg)
            raise

    def _get_symbol(self):
        strategy_symbols = {
            'Addition': '+',
            'Subtraction': '-',
            'Multiplication': '*',
            'Division': '/',
            'Power': '^'
        }
        return strategy_symbols.get(self._strategy.get_name(), '?')

    def get_current_strategy(self):
        return self._strategy.get_name() if self._strategy else "None"

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()

# Test enhanced Strategy pattern:
print("\n=== Enhanced Strategy Pattern with Calculator ===")

calculator = Calculator()

# Test different strategies
strategies = [
    AdditionStrategy(),
    SubtractionStrategy(),
    MultiplicationStrategy(),
    DivisionStrategy(),
    PowerStrategy()
]

test_cases = [(10, 3), (15, 5), (8, 2), (7, 0), (2, 4)]

for strategy in strategies:
    calculator.set_strategy(strategy)
    print(f"\nTesting {strategy.get_name()} strategy:")
    
    for a, b in test_cases:
        try:
            result = calculator.calculate(a, b)
            print(f"  {a} {calculator._get_symbol()} {b} = {result}")
        except Exception as e:
            print(f"  {a} {calculator._get_symbol()} {b} -> Error: {e}")
        
        # Only test a few cases for each strategy
        if strategy.get_name() == "Division" and b == 0:
            break

print(f"\nCalculation history:")
for entry in calculator.get_history():
    print(f"  {entry}")

# What we accomplished in this step:
# - Created comprehensive calculator with multiple strategies
# - Added error handling for division by zero
# - Implemented operation history tracking
# - Added strategy identification and symbols


# Step 6: Strategy pattern with sorting algorithms
# ===============================================================================

# Explanation:
# Let's create a more complex example with different sorting algorithms
# to demonstrate the Strategy pattern with more sophisticated algorithms.

class SortingStrategy:
    def sort(self, data):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_name(self):
        raise NotImplementedError("Subclasses must implement this method")

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        arr = data.copy()  # Don't modify original
        n = len(arr)
        comparisons = 0
        
        for i in range(n):
            for j in range(0, n - i - 1):
                comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr, comparisons
    
    def get_name(self):
        return "Bubble Sort"

class QuickSortStrategy(SortingStrategy):
    def __init__(self):
        self.comparisons = 0
    
    def sort(self, data):
        arr = data.copy()
        self.comparisons = 0
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr, self.comparisons
    
    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)
    
    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def get_name(self):
        return "Quick Sort"

class MergeSortStrategy(SortingStrategy):
    def __init__(self):
        self.comparisons = 0
    
    def sort(self, data):
        arr = data.copy()
        self.comparisons = 0
        self._merge_sort(arr, 0, len(arr) - 1)
        return arr, self.comparisons
    
    def _merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(arr, left, mid)
            self._merge_sort(arr, mid + 1, right)
            self._merge(arr, left, mid, right)
    
    def _merge(self, arr, left, mid, right):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            self.comparisons += 1
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    def get_name(self):
        return "Merge Sort"

class SortingContext:
    def __init__(self, strategy=None):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort_data(self, data):
        if self._strategy is None:
            raise ValueError("No sorting strategy set")
        
        import time
        start_time = time.time()
        sorted_data, comparisons = self._strategy.sort(data)
        end_time = time.time()
        
        return {
            'sorted_data': sorted_data,
            'comparisons': comparisons,
            'time_taken': end_time - start_time,
            'algorithm': self._strategy.get_name()
        }

# Test sorting strategies:
print("\n=== Strategy Pattern with Sorting Algorithms ===")

import random

# Generate test data
test_data = [random.randint(1, 100) for _ in range(20)]
print(f"Original data: {test_data}")

sorter = SortingContext()
strategies = [BubbleSortStrategy(), QuickSortStrategy(), MergeSortStrategy()]

print(f"\nSorting results:")
for strategy in strategies:
    sorter.set_strategy(strategy)
    result = sorter.sort_data(test_data)
    
    print(f"\n{result['algorithm']}:")
    print(f"  Sorted: {result['sorted_data']}")
    print(f"  Comparisons: {result['comparisons']}")
    print(f"  Time: {result['time_taken']:.6f} seconds")

# What we accomplished in this step:
# - Implemented multiple sorting algorithms as strategies
# - Added performance measurement (comparisons and time)
# - Demonstrated strategy pattern with complex algorithms
# - Showed how strategies can be compared and analyzed


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Strategy pattern and its benefits
# - Creating abstract strategy interfaces
# - Implementing concrete strategies with different algorithms
# - Building context classes that use strategies interchangeably
# - Adding error handling and performance measurement
# - Comparing different algorithms using the same interface
# - Understanding when to use Strategy vs other patterns
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating payment processing strategies!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
