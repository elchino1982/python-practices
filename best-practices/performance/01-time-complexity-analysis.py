"""Question: Analyze and implement functions with different time complexities.

Create functions that demonstrate various time complexities and learn how to analyze
the performance characteristics of algorithms.

Requirements:
1. Implement functions with O(1), O(log n), O(n), O(n log n), O(n²), and O(2^n) complexities
2. Create a time complexity analyzer class
3. Demonstrate performance measurement and comparison
4. Provide clear explanations of each complexity class
5. Show practical examples and use cases

Example usage:
    analyzer = TimeComplexityAnalyzer()
    analyzer.measure_function(linear_search, [1, 2, 3, 4, 5], 3)
    analyzer.compare_algorithms([linear_search, binary_search], data, target)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what different time complexities mean
# - Start with simple O(1) and O(n) examples
# - Consider how input size affects execution time
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
# - What does O(1) mean? (constant time)
# - How does O(n) relate to input size? (linear time)
# - What makes an algorithm O(n²)? (nested loops)
# - How can you measure execution time?
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


# Step 1: Import modules and create basic O(1) constant time functions
# ===============================================================================

# Explanation:
# O(1) means constant time - the execution time doesn't change regardless of input size.
# These operations take the same amount of time whether we have 10 or 10,000 elements.

import time
import math
import random
from typing import List, Callable, Any, Tuple
from functools import wraps

def constant_time_access(data: List[int], index: int) -> int:
    """O(1) - Constant time: Array/list access by index."""
    return data[index]

def constant_time_append(data: List[int], value: int) -> None:
    """O(1) - Constant time: Append to end of list (amortized)."""
    data.append(value)

def constant_time_hash_lookup(data: dict, key: str) -> Any:
    """O(1) - Constant time: Hash table/dictionary lookup."""
    return data.get(key)

# Test the O(1) functions
print("=== Step 1: O(1) Constant Time Functions ===")
test_list = [1, 2, 3, 4, 5]
test_dict = {"a": 1, "b": 2, "c": 3}

print(f"Accessing index 2: {constant_time_access(test_list, 2)}")
constant_time_append(test_list, 6)
print(f"After append: {test_list}")
print(f"Hash lookup 'b': {constant_time_hash_lookup(test_dict, 'b')}")
print()


# Step 2: O(log n) logarithmic time functions
# ===============================================================================

# Explanation:
# O(log n) means logarithmic time - the execution time grows logarithmically with input size.
# These algorithms typically divide the problem in half at each step (like binary search).

def binary_search(data: List[int], target: int) -> int:
    """O(log n) - Logarithmic time: Binary search in sorted array."""
    left, right = 0, len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

def logarithmic_height_calculation(n: int) -> int:
    """O(log n) - Calculate height of balanced binary tree."""
    if n <= 0:
        return 0
    return math.floor(math.log2(n)) + 1

def power_efficient(base: int, exponent: int) -> int:
    """O(log n) - Fast exponentiation using divide and conquer."""
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    if exponent % 2 == 0:
        half_power = power_efficient(base, exponent // 2)
        return half_power * half_power
    else:
        return base * power_efficient(base, exponent - 1)

# Test the O(log n) functions
print("=== Step 2: O(log n) Logarithmic Time Functions ===")
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(f"Binary search for 7: index {binary_search(sorted_list, 7)}")
print(f"Binary search for 8: index {binary_search(sorted_list, 8)}")
print(f"Tree height for 15 nodes: {logarithmic_height_calculation(15)}")
print(f"2^10 using fast exponentiation: {power_efficient(2, 10)}")
print()


# Step 3: O(n) linear time functions
# ===============================================================================

# Explanation:
# O(n) means linear time - the execution time grows linearly with input size.
# These algorithms typically need to examine each element once.

def linear_search(data: List[int], target: int) -> int:
    """O(n) - Linear time: Search through unsorted array."""
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1  # Not found

def find_maximum(data: List[int]) -> int:
    """O(n) - Linear time: Find maximum element in array."""
    if not data:
        raise ValueError("Empty list")
    
    max_val = data[0]
    for value in data[1:]:
        if value > max_val:
            max_val = value
    return max_val

def sum_array(data: List[int]) -> int:
    """O(n) - Linear time: Calculate sum of all elements."""
    total = 0
    for value in data:
        total += value
    return total

def count_occurrences(data: List[int], target: int) -> int:
    """O(n) - Linear time: Count how many times target appears."""
    count = 0
    for value in data:
        if value == target:
            count += 1
    return count

def reverse_array(data: List[int]) -> List[int]:
    """O(n) - Linear time: Create reversed copy of array."""
    reversed_data = []
    for i in range(len(data) - 1, -1, -1):
        reversed_data.append(data[i])
    return reversed_data

# Test the O(n) functions
print("=== Step 3: O(n) Linear Time Functions ===")
test_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(f"Linear search for 5: index {linear_search(test_array, 5)}")
print(f"Maximum element: {find_maximum(test_array)}")
print(f"Sum of array: {sum_array(test_array)}")
print(f"Count of 1s: {count_occurrences(test_array, 1)}")
print(f"Original: {test_array}")
print(f"Reversed: {reverse_array(test_array)}")
print()


# Step 4: O(n log n) linearithmic time functions
# ===============================================================================

# Explanation:
# O(n log n) means linearithmic time - common in efficient sorting algorithms.
# These algorithms typically use divide-and-conquer strategies.

def merge_sort(data: List[int]) -> List[int]:
    """O(n log n) - Linearithmic time: Merge sort algorithm."""
    if len(data) <= 1:
        return data.copy()
    
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function for merge sort."""
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

def quick_sort(data: List[int]) -> List[int]:
    """O(n log n) average case - Quick sort algorithm."""
    if len(data) <= 1:
        return data.copy()
    
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(data: List[int]) -> List[int]:
    """O(n log n) - Heap sort algorithm."""
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    arr = data.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

# Test the O(n log n) functions
print("=== Step 4: O(n log n) Linearithmic Time Functions ===")
unsorted_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]

print(f"Original array: {unsorted_array}")
print(f"Merge sort: {merge_sort(unsorted_array)}")
print(f"Quick sort: {quick_sort(unsorted_array)}")
print(f"Heap sort: {heap_sort(unsorted_array)}")
print()


# Step 5: O(n²) quadratic time functions
# ===============================================================================

# Explanation:
# O(n²) means quadratic time - execution time grows quadratically with input size.
# These algorithms typically have nested loops that both depend on input size.

def bubble_sort(data: List[int]) -> List[int]:
    """O(n²) - Quadratic time: Bubble sort algorithm."""
    arr = data.copy()
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def selection_sort(data: List[int]) -> List[int]:
    """O(n²) - Quadratic time: Selection sort algorithm."""
    arr = data.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def insertion_sort(data: List[int]) -> List[int]:
    """O(n²) - Quadratic time: Insertion sort algorithm."""
    arr = data.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def find_all_pairs_sum(data: List[int], target: int) -> List[Tuple[int, int]]:
    """O(n²) - Find all pairs that sum to target."""
    pairs = []
    n = len(data)
    
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] + data[j] == target:
                pairs.append((data[i], data[j]))
    
    return pairs

def matrix_multiplication(matrix_a: List[List[int]], matrix_b: List[List[int]]) -> List[List[int]]:
    """O(n³) - Cubic time: Basic matrix multiplication (even worse than quadratic!)."""
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])
    
    if cols_a != rows_b:
        raise ValueError("Cannot multiply matrices: incompatible dimensions")
    
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result

def count_inversions(data: List[int]) -> int:
    """O(n²) - Count number of inversions in array."""
    count = 0
    n = len(data)
    
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                count += 1
    
    return count

# Test the O(n²) functions
print("=== Step 5: O(n²) Quadratic Time Functions ===")
test_array_small = [64, 34, 25, 12, 22]

print(f"Original: {test_array_small}")
print(f"Bubble sort: {bubble_sort(test_array_small)}")
print(f"Selection sort: {selection_sort(test_array_small)}")
print(f"Insertion sort: {insertion_sort(test_array_small)}")

pairs_array = [1, 2, 3, 4, 5, 6]
print(f"Pairs that sum to 7 in {pairs_array}: {find_all_pairs_sum(pairs_array, 7)}")

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
print(f"Matrix A: {matrix_a}")
print(f"Matrix B: {matrix_b}")
print(f"A × B: {matrix_multiplication(matrix_a, matrix_b)}")

inversion_array = [5, 2, 6, 1]
print(f"Inversions in {inversion_array}: {count_inversions(inversion_array)}")
print()


# Step 6: O(2^n) exponential time functions
# ===============================================================================

# Explanation:
# O(2^n) means exponential time - execution time doubles with each additional input.
# These algorithms are typically recursive with multiple recursive calls per level.

def fibonacci_naive(n: int) -> int:
    """O(2^n) - Exponential time: Naive recursive Fibonacci."""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

def fibonacci_optimized(n: int, memo: dict = None) -> int:
    """O(n) - Linear time: Memoized Fibonacci (much better!)."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_optimized(n - 1, memo) + fibonacci_optimized(n - 2, memo)
    return memo[n]

def power_set(data: List[int]) -> List[List[int]]:
    """O(2^n) - Generate all possible subsets."""
    if not data:
        return [[]]
    
    first = data[0]
    rest_subsets = power_set(data[1:])
    
    new_subsets = []
    for subset in rest_subsets:
        new_subsets.append([first] + subset)
    
    return rest_subsets + new_subsets

def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """O(2^n) - Tower of Hanoi solution."""
    moves = []
    
    def hanoi_recursive(n, src, dest, aux):
        if n == 1:
            moves.append(f"Move disk 1 from {src} to {dest}")
        else:
            hanoi_recursive(n - 1, src, aux, dest)
            moves.append(f"Move disk {n} from {src} to {dest}")
            hanoi_recursive(n - 1, aux, dest, src)
    
    hanoi_recursive(n, source, destination, auxiliary)
    return moves

def subset_sum_exists(data: List[int], target: int) -> bool:
    """O(2^n) - Check if any subset sums to target (brute force)."""
    def check_subset(index, current_sum):
        if current_sum == target:
            return True
        if index >= len(data):
            return False
        
        # Include current element or exclude it
        return (check_subset(index + 1, current_sum + data[index]) or 
                check_subset(index + 1, current_sum))
    
    return check_subset(0, 0)

def traveling_salesman_brute_force(distances: List[List[int]]) -> Tuple[int, List[int]]:
    """O(n!) - Even worse than exponential: TSP brute force."""
    n = len(distances)
    cities = list(range(1, n))  # Exclude starting city (0)
    min_cost = float('inf')
    best_path = []
    
    def permutations(arr):
        if len(arr) <= 1:
            return [arr]
        result = []
        for i in range(len(arr)):
            rest = arr[:i] + arr[i+1:]
            for p in permutations(rest):
                result.append([arr[i]] + p)
        return result
    
    for perm in permutations(cities):
        current_cost = 0
        path = [0] + perm + [0]  # Start and end at city 0
        
        for i in range(len(path) - 1):
            current_cost += distances[path[i]][path[i + 1]]
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = path
    
    return min_cost, best_path

# Test the O(2^n) functions (with small inputs!)
print("=== Step 6: O(2^n) Exponential Time Functions ===")

# Fibonacci comparison
print("Fibonacci comparison (n=10):")
print(f"Naive recursive: {fibonacci_naive(10)}")
print(f"Optimized memoized: {fibonacci_optimized(10)}")

# Power set
small_set = [1, 2, 3]
print(f"Power set of {small_set}: {power_set(small_set)}")

# Tower of Hanoi
hanoi_moves = tower_of_hanoi(3, "A", "C", "B")
print(f"Tower of Hanoi (3 disks) moves: {len(hanoi_moves)}")
for move in hanoi_moves[:5]:  # Show first 5 moves
    print(f"  {move}")

# Subset sum
test_set = [3, 34, 4, 12, 5, 2]
print(f"Does subset of {test_set} sum to 9? {subset_sum_exists(test_set, 9)}")

# TSP (very small example)
distances_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_cost, best_route = traveling_salesman_brute_force(distances_matrix)
print(f"TSP minimum cost: {min_cost}, best route: {best_route}")
print()


# Step 7: Time Complexity Analyzer Class
# ===============================================================================

# Explanation:
# Now we'll create a class to measure and analyze the actual performance of our functions.
# This helps us verify our theoretical complexity analysis with real measurements.

class TimeComplexityAnalyzer:
    """A class to measure and analyze time complexity of functions."""
    
    def __init__(self):
        self.measurements = {}
    
    def measure_function(self, func: Callable, *args, **kwargs) -> float:
        """Measure execution time of a function."""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        func_name = func.__name__
        if func_name not in self.measurements:
            self.measurements[func_name] = []
        
        self.measurements[func_name].append({
            'input_size': self._estimate_input_size(args),
            'time': execution_time,
            'result': result
        })
        
        return execution_time
    
    def _estimate_input_size(self, args) -> int:
        """Estimate input size from function arguments."""
        for arg in args:
            if isinstance(arg, (list, tuple, str)):
                return len(arg)
            elif isinstance(arg, int):
                return arg
        return 1
    
    def compare_algorithms(self, functions: List[Callable], data, *extra_args) -> dict:
        """Compare multiple algorithms on the same data."""
        results = {}
        
        for func in functions:
            try:
                execution_time = self.measure_function(func, data, *extra_args)
                results[func.__name__] = execution_time
            except Exception as e:
                results[func.__name__] = f"Error: {e}"
        
        return results
    
    def benchmark_scaling(self, func: Callable, input_generator: Callable, 
                         sizes: List[int], *extra_args) -> List[dict]:
        """Benchmark how function performance scales with input size."""
        results = []
        
        for size in sizes:
            test_data = input_generator(size)
            execution_time = self.measure_function(func, test_data, *extra_args)
            
            results.append({
                'size': size,
                'time': execution_time,
                'time_per_element': execution_time / size if size > 0 else 0
            })
        
        return results
    
    def analyze_complexity(self, func_name: str) -> str:
        """Analyze the complexity based on measurements."""
        if func_name not in self.measurements:
            return "No measurements available"
        
        measurements = self.measurements[func_name]
        if len(measurements) < 2:
            return "Need more measurements for analysis"
        
        # Sort by input size
        measurements.sort(key=lambda x: x['input_size'])
        
        # Calculate ratios
        analysis = []
        for i in range(1, len(measurements)):
            prev = measurements[i-1]
            curr = measurements[i]
            
            size_ratio = curr['input_size'] / prev['input_size']
            time_ratio = curr['time'] / prev['time'] if prev['time'] > 0 else float('inf')
            
            analysis.append(f"Size {prev['input_size']} → {curr['input_size']} "
                          f"(×{size_ratio:.1f}): Time ×{time_ratio:.2f}")
        
        return "\n".join(analysis)
    
    def get_summary(self) -> str:
        """Get a summary of all measurements."""
        summary = "=== Performance Analysis Summary ===\n"
        
        for func_name, measurements in self.measurements.items():
            summary += f"\n{func_name}:\n"
            for measurement in measurements:
                summary += (f"  Input size: {measurement['input_size']}, "
                          f"Time: {measurement['time']:.6f}s\n")
        
        return summary

# Test the TimeComplexityAnalyzer
print("=== Step 7: Time Complexity Analyzer ===")
analyzer = TimeComplexityAnalyzer()

# Generate test data of different sizes
def generate_random_list(size: int) -> List[int]:
    return [random.randint(1, 1000) for _ in range(size)]

def generate_sorted_list(size: int) -> List[int]:
    return list(range(1, size + 1))

# Benchmark different algorithms
sizes = [100, 200, 500, 1000]
print("Benchmarking linear search scaling:")
linear_results = analyzer.benchmark_scaling(linear_search, generate_random_list, sizes, 500)
for result in linear_results:
    print(f"  Size {result['size']}: {result['time']:.6f}s")

print("\nBenchmarking binary search scaling:")
binary_results = analyzer.benchmark_scaling(binary_search, generate_sorted_list, sizes, 500)
for result in binary_results:
    print(f"  Size {result['size']}: {result['time']:.6f}s")

# Compare sorting algorithms
test_data = generate_random_list(1000)
print(f"\nComparing sorting algorithms on {len(test_data)} elements:")
sorting_comparison = analyzer.compare_algorithms(
    [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort], 
    test_data
)
for algo, time_taken in sorting_comparison.items():
    if isinstance(time_taken, float):
        print(f"  {algo}: {time_taken:.6f}s")
    else:
        print(f"  {algo}: {time_taken}")

print(f"\nAnalyzer summary:")
print(analyzer.get_summary())
print()


# Step 8: Practical Examples and Best Practices
# ===============================================================================

# Explanation:
# Let's demonstrate practical applications and best practices for choosing
# the right algorithm based on time complexity considerations.

class ComplexityBestPractices:
    """Demonstrates best practices for algorithm selection and optimization."""
    
    @staticmethod
    def choose_search_algorithm(data: List[int], is_sorted: bool = False) -> Callable:
        """Choose the best search algorithm based on data characteristics."""
        if is_sorted:
            return binary_search  # O(log n)
        else:
            return linear_search  # O(n)
    
    @staticmethod
    def choose_sorting_algorithm(data_size: int, memory_constraint: bool = False) -> Callable:
        """Choose the best sorting algorithm based on constraints."""
        if data_size < 50:
            return insertion_sort  # O(n²) but fast for small arrays
        elif memory_constraint:
            return heap_sort  # O(n log n) with O(1) extra space
        else:
            return merge_sort  # O(n log n) guaranteed, stable
    
    @staticmethod
    def optimize_fibonacci(n: int) -> int:
        """Demonstrate optimization from O(2^n) to O(n)."""
        # Instead of naive recursion, use iterative approach
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def efficient_duplicate_detection(data: List[int]) -> bool:
        """O(n) duplicate detection using hash set instead of O(n²) nested loops."""
        seen = set()
        for item in data:
            if item in seen:
                return True
            seen.add(item)
        return False
    
    @staticmethod
    def efficient_two_sum(data: List[int], target: int) -> List[Tuple[int, int]]:
        """O(n) two sum using hash map instead of O(n²) nested loops."""
        seen = {}
        pairs = []
        
        for i, num in enumerate(data):
            complement = target - num
            if complement in seen:
                pairs.append((complement, num))
            seen[num] = i
        
        return pairs

def demonstrate_complexity_impact():
    """Demonstrate the real-world impact of different complexities."""
    print("=== Step 8: Practical Examples and Best Practices ===")
    
    # Show how complexity affects performance with different input sizes
    sizes = [10, 100, 1000, 10000]
    
    print("Time complexity impact demonstration:")
    print("Input Size | O(1) | O(log n) | O(n) | O(n log n) | O(n²)")
    print("-" * 60)
    
    for n in sizes:
        o_1 = 1
        o_log_n = math.log2(n) if n > 0 else 0
        o_n = n
        o_n_log_n = n * math.log2(n) if n > 0 else 0
        o_n_squared = n * n
        
        print(f"{n:10} | {o_1:4.0f} | {o_log_n:8.1f} | {o_n:4.0f} | {o_n_log_n:10.0f} | {o_n_squared:8.0f}")
    
    print("\nPractical algorithm selection examples:")
    
    # Example 1: Search algorithm selection
    practices = ComplexityBestPractices()
    
    sorted_data = list(range(1, 1001))
    unsorted_data = [random.randint(1, 1000) for _ in range(1000)]
    
    # Demonstrate search algorithm choice
    analyzer = TimeComplexityAnalyzer()
    
    print("\nSearch algorithm comparison:")
    search_target = 500
    
    # Binary search on sorted data
    binary_time = analyzer.measure_function(binary_search, sorted_data, search_target)
    print(f"Binary search (sorted data): {binary_time:.6f}s")
    
    # Linear search on unsorted data
    linear_time = analyzer.measure_function(linear_search, unsorted_data, search_target)
    print(f"Linear search (unsorted data): {linear_time:.6f}s")
    
    # Example 2: Fibonacci optimization
    print("\nFibonacci optimization comparison:")
    n = 30
    
    # Optimized iterative version
    start_time = time.perf_counter()
    result_optimized = practices.optimize_fibonacci(n)
    optimized_time = time.perf_counter() - start_time
    print(f"Optimized Fibonacci({n}): {result_optimized} in {optimized_time:.6f}s")
    
    # Note: We don't run naive version for n=30 as it would take too long!
    print(f"Naive recursive would take exponentially longer!")
    
    # Example 3: Duplicate detection
    print("\nDuplicate detection comparison:")
    test_data_with_dups = list(range(1000)) + [500]  # Add one duplicate
    
    dup_time = analyzer.measure_function(practices.efficient_duplicate_detection, test_data_with_dups)
    print(f"Efficient duplicate detection: {dup_time:.6f}s")
    
    # Example 4: Two sum optimization
    print("\nTwo sum optimization:")
    two_sum_data = [2, 7, 11, 15, 3, 6, 8, 1]
    target_sum = 9
    
    efficient_pairs = practices.efficient_two_sum(two_sum_data, target_sum)
    print(f"Efficient two sum pairs for target {target_sum}: {efficient_pairs}")

def complexity_guidelines():
    """Provide guidelines for complexity analysis."""
    print("\n=== Complexity Analysis Guidelines ===")
    
    guidelines = {
        "O(1) - Constant": [
            "Array/list access by index",
            "Hash table lookup",
            "Stack push/pop operations",
            "Mathematical calculations"
        ],
        "O(log n) - Logarithmic": [
            "Binary search in sorted array",
            "Balanced tree operations",
            "Divide and conquer algorithms",
            "Finding height of balanced tree"
        ],
        "O(n) - Linear": [
            "Single loop through data",
            "Linear search",
            "Finding min/max in unsorted array",
            "Counting occurrences"
        ],
        "O(n log n) - Linearithmic": [
            "Efficient sorting (merge, heap, quick sort average)",
            "Building balanced trees",
            "Divide and conquer with linear merge",
            "Fast Fourier Transform"
        ],
        "O(n²) - Quadratic": [
            "Nested loops over same data",
            "Simple sorting (bubble, selection, insertion)",
            "Comparing all pairs",
            "Basic matrix operations"
        ],
        "O(2^n) - Exponential": [
            "Recursive algorithms with multiple calls",
            "Generating all subsets",
            "Solving NP-complete problems brute force",
            "Tower of Hanoi"
        ]
    }
    
    for complexity, examples in guidelines.items():
        print(f"\n{complexity}:")
        for example in examples:
            print(f"  • {example}")
    
    print("\n=== Optimization Tips ===")
    tips = [
        "Use appropriate data structures (hash tables for O(1) lookup)",
        "Consider sorting data if you'll search it multiple times",
        "Use memoization to optimize recursive algorithms",
        "Choose algorithms based on input size and constraints",
        "Profile your code to identify actual bottlenecks",
        "Remember: premature optimization is the root of all evil",
        "Focus on algorithmic improvements before micro-optimizations"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"{i}. {tip}")

# Run the demonstrations
demonstrate_complexity_impact()
complexity_guidelines()

print("\n" + "="*80)
print("CONGRATULATIONS! You've completed the Time Complexity Analysis tutorial!")
print("="*80)
print("\nKey takeaways:")
print("• Understanding time complexity helps you choose the right algorithm")
print("• O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n)")
print("• Always consider your input size and constraints")
print("• Measure performance to verify theoretical analysis")
print("• Sometimes a 'worse' algorithm is better for small inputs")
print("• Optimization should be based on actual bottlenecks")

# ===============================================================================

