# Python Performance Optimization: Complete Tutorial

## 🚀 Welcome to Python Performance Mastery

This comprehensive tutorial covers everything you need to know about optimizing Python code performance, from basic concepts for beginners to advanced techniques for experts. Whether you're just starting out or looking to fine-tune enterprise applications, this guide has you covered.

## 📚 Table of Contents

### Part 1: Fundamentals (Beginner Level)
1. [Introduction to Performance](#1-introduction-to-performance)
2. [Understanding Time Complexity](#2-understanding-time-complexity)
3. [Basic Memory Management](#3-basic-memory-management)
4. [Choosing the Right Data Structures](#4-choosing-the-right-data-structures)

### Part 2: Intermediate Techniques
5. [Algorithm Optimization](#5-algorithm-optimization)
6. [Profiling and Benchmarking](#6-profiling-and-benchmarking)
7. [Caching Strategies](#7-caching-strategies)
8. [String Operations Optimization](#8-string-operations-optimization)

### Part 3: Advanced Optimization (Expert Level)
9. [Lazy Evaluation Techniques](#9-lazy-evaluation-techniques)
10. [I/O Optimization](#10-io-optimization)
11. [Concurrent Programming](#11-concurrent-programming)
12. [Advanced Memory Optimization](#12-advanced-memory-optimization)

### Part 4: Real-World Applications
13. [Performance Testing Strategies](#13-performance-testing-strategies)
14. [Production Optimization](#14-production-optimization)
15. [Common Performance Pitfalls](#15-common-performance-pitfalls)

---

## 1. Introduction to Performance

### What is Performance Optimization?

Performance optimization is the process of making your Python code run faster, use less memory, and handle more data efficiently. It's about finding the balance between code readability, maintainability, and execution speed.

### Why Performance Matters

- **User Experience**: Faster applications provide better user experience
- **Cost Efficiency**: Optimized code requires fewer server resources
- **Scalability**: Well-optimized code can handle more users and data
- **Competitive Advantage**: Performance can be a key differentiator

### Performance Metrics to Consider

1. **Execution Time**: How long does your code take to run?
2. **Memory Usage**: How much RAM does your application consume?
3. **CPU Utilization**: How efficiently does your code use processor resources?
4. **I/O Operations**: How efficiently does your code handle file and network operations?
5. **Throughput**: How many operations can your code handle per second?

### The Performance Optimization Process

```python
# Step 1: Measure (Profile your code)
# Step 2: Analyze (Identify bottlenecks)
# Step 3: Optimize (Apply appropriate techniques)
# Step 4: Verify (Measure again to confirm improvements)
# Step 5: Repeat (Continue the cycle)
```

### Golden Rules of Optimization

1. **"Premature optimization is the root of all evil"** - Donald Knuth
   - Always profile first, optimize second
   - Focus on actual bottlenecks, not perceived ones

2. **Measure Everything**
   - Use profiling tools to identify real performance issues
   - Don't guess where the problems are

3. **Optimize for the Common Case**
   - Focus on code paths that run most frequently
   - 80/20 rule: 80% of execution time is spent in 20% of code

4. **Readability vs Performance**
   - Maintain code readability when possible
   - Document complex optimizations thoroughly

---

## 2. Understanding Time Complexity

### What is Time Complexity?

Time complexity describes how the runtime of an algorithm grows as the input size increases. It's expressed using Big O notation and helps us understand the efficiency of our algorithms.

### Big O Notation Explained

#### O(1) - Constant Time
```python
def get_first_element(lst):
    """Always takes the same time regardless of list size"""
    return lst[0] if lst else None

# Example: Dictionary lookup
my_dict = {"key": "value"}
result = my_dict["key"]  # O(1)
```

#### O(log n) - Logarithmic Time
```python
def binary_search(arr, target):
    """Divides search space in half each iteration"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
index = binary_search(sorted_list, 7)  # O(log n)
```

#### O(n) - Linear Time
```python
def find_maximum(lst):
    """Must check every element once"""
    if not lst:
        return None
    
    max_val = lst[0]
    for item in lst[1:]:  # O(n)
        if item > max_val:
            max_val = item
    return max_val

# Better approach using built-in
def find_maximum_optimized(lst):
    return max(lst) if lst else None  # Still O(n) but optimized in C
```

#### O(n²) - Quadratic Time
```python
def bubble_sort(arr):
    """Nested loops over the same data"""
    n = len(arr)
    for i in range(n):          # O(n)
        for j in range(0, n-i-1):  # O(n)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Better alternative
def optimized_sort(arr):
    return sorted(arr)  # O(n log n) - much better!
```

### Practical Time Complexity Analysis

#### Example 1: List vs Set Membership Testing
```python
import time

def test_membership_performance():
    # Create test data
    data_list = list(range(10000))
    data_set = set(range(10000))
    target = 9999
    
    # Test list membership (O(n))
    start = time.time()
    for _ in range(1000):
        result = target in data_list
    list_time = time.time() - start
    
    # Test set membership (O(1))
    start = time.time()
    for _ in range(1000):
        result = target in data_set
    set_time = time.time() - start
    
    print(f"List membership: {list_time:.4f}s")
    print(f"Set membership: {set_time:.4f}s")
    print(f"Set is {list_time/set_time:.1f}x faster")

# test_membership_performance()
```

#### Example 2: String Concatenation Complexity
```python
def inefficient_string_building(words):
    """O(n²) - creates new string each time"""
    result = ""
    for word in words:
        result += word + " "  # Creates new string each iteration
    return result.strip()

def efficient_string_building(words):
    """O(n) - builds list then joins once"""
    return " ".join(words)

# Performance comparison
def compare_string_methods():
    words = ["hello"] * 1000
    
    import time
    
    # Inefficient method
    start = time.time()
    result1 = inefficient_string_building(words)
    time1 = time.time() - start
    
    # Efficient method
    start = time.time()
    result2 = efficient_string_building(words)
    time2 = time.time() - start
    
    print(f"Inefficient: {time1:.4f}s")
    print(f"Efficient: {time2:.4f}s")
    print(f"Improvement: {time1/time2:.1f}x faster")
```

### Time Complexity Best Practices

1. **Know Your Data Structures**
   ```python
   # Dictionary/Set operations: O(1) average
   # List indexing: O(1)
   # List searching: O(n)
   # List insertion at end: O(1) amortized
   # List insertion at beginning: O(n)
   ```

2. **Avoid Nested Loops When Possible**
   ```python
   # Bad: O(n²)
   def find_duplicates_slow(lst):
       duplicates = []
       for i in range(len(lst)):
           for j in range(i+1, len(lst)):
               if lst[i] == lst[j] and lst[i] not in duplicates:
                   duplicates.append(lst[i])
       return duplicates
   
   # Good: O(n)
   def find_duplicates_fast(lst):
       seen = set()
       duplicates = set()
       for item in lst:
           if item in seen:
               duplicates.add(item)
           else:
               seen.add(item)
       return list(duplicates)
   ```

3. **Use Built-in Functions**
   ```python
   # Built-in functions are usually optimized in C
   # and have better time complexity
   
   # Instead of manual loops, use:
   numbers = [1, 2, 3, 4, 5]
   
   # sum() instead of manual addition
   total = sum(numbers)  # O(n) but optimized
   
   # max()/min() instead of manual comparison
   maximum = max(numbers)  # O(n) but optimized
   
   # sorted() instead of manual sorting
   sorted_nums = sorted(numbers)  # O(n log n) but highly optimized
   ```

---

## 3. Basic Memory Management

### Understanding Python Memory Model

Python manages memory automatically through reference counting and garbage collection, but understanding how it works helps you write more efficient code.

### Memory Allocation Basics

#### Object Creation and References
```python
# Each assignment creates a reference, not a copy
a = [1, 2, 3]
b = a  # b points to the same list object
b.append(4)
print(a)  # [1, 2, 3, 4] - a is modified too!

# To create a copy:
c = a.copy()  # Shallow copy
d = a[:]      # Another way to shallow copy
e = list(a)   # Yet another way
```

#### Memory-Efficient Data Types
```python
# Use appropriate data types for memory efficiency

# For large sequences of numbers, use array instead of list
import array
numbers_list = [1, 2, 3, 4, 5] * 1000  # More memory
numbers_array = array.array('i', [1, 2, 3, 4, 5] * 1000)  # Less memory

# For boolean flags, consider using bitwise operations
# Instead of: flags = [True, False, True, False] * 1000
# Use: flags = 0b1010... (for simple cases)

# Use tuples for immutable sequences (less memory overhead)
coordinates_list = [1, 2]    # Mutable, more memory
coordinates_tuple = (1, 2)   # Immutable, less memory
```

### Memory Optimization Techniques

#### 1. Use Generators Instead of Lists
```python
# Memory-heavy approach
def get_squares_list(n):
    """Creates entire list in memory"""
    return [i**2 for i in range(n)]

# Memory-efficient approach
def get_squares_generator(n):
    """Generates values on-demand"""
    return (i**2 for i in range(n))

# Example usage
def compare_memory_usage():
    import sys
    
    # List approach - stores all values
    squares_list = get_squares_list(10000)
    list_size = sys.getsizeof(squares_list)
    
    # Generator approach - stores only the generator object
    squares_gen = get_squares_generator(10000)
    gen_size = sys.getsizeof(squares_gen)
    
    print(f"List size: {list_size} bytes")
    print(f"Generator size: {gen_size} bytes")
    print(f"Memory savings: {list_size/gen_size:.1f}x")

# compare_memory_usage()
```

#### 2. Use `__slots__` for Classes
```python
# Regular class - uses dictionary for attributes
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Optimized class - uses slots
class OptimizedPoint:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison
def compare_class_memory():
    import sys
    
    regular = RegularPoint(1, 2)
    optimized = OptimizedPoint(1, 2)
    
    print(f"Regular class: {sys.getsizeof(regular.__dict__)} bytes")
    print(f"Optimized class: {sys.getsizeof(optimized)} bytes")
```

#### 3. Efficient String Handling
```python
# Inefficient string concatenation
def build_string_inefficient(words):
    result = ""
    for word in words:
        result += word + " "  # Creates new string each time
    return result

# Efficient string concatenation
def build_string_efficient(words):
    return " ".join(words)  # Single allocation

# For complex string building, use StringIO
from io import StringIO

def build_complex_string(data):
    buffer = StringIO()
    for item in data:
        buffer.write(str(item))
        buffer.write("\n")
    return buffer.getvalue()
```

### Memory Profiling Tools

#### Using `tracemalloc` (Built-in)
```python
import tracemalloc

def memory_intensive_function():
    # Start tracing
    tracemalloc.start()
    
    # Your code here
    data = [i**2 for i in range(100000)]
    
    # Get memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.1f} MB")
    
    tracemalloc.stop()

# memory_intensive_function()
```

#### Using `sys.getsizeof()` for Object Size
```python
import sys

def analyze_object_sizes():
    # Different data structures
    empty_list = []
    small_list = [1, 2, 3]
    large_list = list(range(1000))
    
    empty_dict = {}
    small_dict = {"a": 1, "b": 2}
    
    empty_set = set()
    small_set = {1, 2, 3}
    
    # Print sizes
    print("Object sizes:")
    print(f"Empty list: {sys.getsizeof(empty_list)} bytes")
    print(f"Small list (3 items): {sys.getsizeof(small_list)} bytes")
    print(f"Large list (1000 items): {sys.getsizeof(large_list)} bytes")
    print(f"Empty dict: {sys.getsizeof(empty_dict)} bytes")
    print(f"Small dict: {sys.getsizeof(small_dict)} bytes")
    print(f"Empty set: {sys.getsizeof(empty_set)} bytes")
    print(f"Small set: {sys.getsizeof(small_set)} bytes")

# analyze_object_sizes()
```

### Memory Best Practices

#### 1. Delete Unused References
```python
def process_large_data():
    large_data = load_massive_dataset()  # Hypothetical function
    
    # Process the data
    result = analyze_data(large_data)
    
    # Explicitly delete reference to free memory
    del large_data
    
    return result
```

#### 2. Use Context Managers for Resources
```python
# Good: Automatic resource cleanup
def read_file_efficiently(filename):
    with open(filename, 'r') as file:
        return file.read()
    # File automatically closed, memory freed

# Bad: Manual resource management
def read_file_inefficiently(filename):
    file = open(filename, 'r')
    content = file.read()
    # Forgot to close file - memory leak!
    return content
```

#### 3. Avoid Circular References
```python
# Bad: Circular reference
class Parent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        child.parent = self  # Circular reference
        self.children.append(child)

class Child:
    def __init__(self):
        self.parent = None

# Better: Use weak references
import weakref

class BetterParent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        child.parent = weakref.ref(self)  # Weak reference
        self.children.append(child)

class BetterChild:
    def __init__(self):
        self.parent = None
    
    def get_parent(self):
        return self.parent() if self.parent else None
```

#### 4. Use Appropriate Collection Types
```python
# For unique items, use set instead of list
def remove_duplicates_inefficient(items):
    unique = []
    for item in items:
        if item not in unique:  # O(n) operation
            unique.append(item)
    return unique

def remove_duplicates_efficient(items):
    return list(set(items))  # O(1) average for set operations

# For counting, use Counter
from collections import Counter

def count_items_inefficient(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def count_items_efficient(items):
    return Counter(items)  # Optimized C implementation
```

---

## 4. Choosing the Right Data Structures

### Data Structure Performance Characteristics

Understanding the performance characteristics of different data structures is crucial for writing efficient Python code.

#### Lists vs Tuples vs Arrays

```python
import array
import time

def compare_sequence_types():
    """Compare performance of different sequence types"""
    size = 100000
    
    # List creation and access
    start = time.time()
    my_list = [i for i in range(size)]
    list_creation = time.time() - start
    
    start = time.time()
    for i in range(1000):
        _ = my_list[size//2]  # Access middle element
    list_access = time.time() - start
    
    # Tuple creation and access
    start = time.time()
    my_tuple = tuple(range(size))
    tuple_creation = time.time() - start
    
    start = time.time()
    for i in range(1000):
        _ = my_tuple[size//2]
    tuple_access = time.time() - start
    
    # Array creation and access
    start = time.time()
    my_array = array.array('i', range(size))
    array_creation = time.time() - start
    
    start = time.time()
    for i in range(1000):
        _ = my_array[size//2]
    array_access = time.time() - start
    
    print("Sequence Type Comparison:")
    print(f"List creation: {list_creation:.4f}s")
    print(f"Tuple creation: {tuple_creation:.4f}s")
    print(f"Array creation: {array_creation:.4f}s")
    print(f"List access: {list_access:.4f}s")
    print(f"Tuple access: {tuple_access:.4f}s")
    print(f"Array access: {array_access:.4f}s")

# compare_sequence_types()
```

#### Dictionary vs List for Lookups

```python
def compare_lookup_performance():
    """Compare lookup performance between dict and list"""
    size = 10000
    
    # Create test data
    data_list = list(range(size))
    data_dict = {i: i for i in range(size)}
    data_set = set(range(size))
    
    target = size - 1  # Worst case for list
    
    # List lookup (O(n))
    start = time.time()
    for _ in range(1000):
        result = target in data_list
    list_time = time.time() - start
    
    # Dictionary lookup (O(1))
    start = time.time()
    for _ in range(1000):
        result = target in data_dict
    dict_time = time.time() - start
    
    # Set lookup (O(1))
    start = time.time()
    for _ in range(1000):
        result = target in data_set
    set_time = time.time() - start
    
    print("Lookup Performance Comparison:")
    print(f"List lookup: {list_time:.4f}s")
    print(f"Dict lookup: {dict_time:.4f}s")
    print(f"Set lookup: {set_time:.4f}s")
    print(f"Dict is {list_time/dict_time:.1f}x faster than list")
    print(f"Set is {list_time/set_time:.1f}x faster than list")

# compare_lookup_performance()
```

### Specialized Data Structures

#### Using Collections Module

```python
from collections import deque, defaultdict, Counter, OrderedDict
import time

# 1. deque for efficient append/pop operations
def compare_list_vs_deque():
    """Compare list vs deque for queue operations"""
    size = 10000
    
    # List as queue (inefficient)
    my_list = []
    start = time.time()
    for i in range(size):
        my_list.append(i)
    for i in range(size):
        my_list.pop(0)  # O(n) operation!
    list_time = time.time() - start
    
    # Deque as queue (efficient)
    my_deque = deque()
    start = time.time()
    for i in range(size):
        my_deque.append(i)
    for i in range(size):
        my_deque.popleft()  # O(1) operation!
    deque_time = time.time() - start
    
    print(f"List as queue: {list_time:.4f}s")
    print(f"Deque as queue: {deque_time:.4f}s")
    print(f"Deque is {list_time/deque_time:.1f}x faster")

# 2. defaultdict for automatic initialization
def demonstrate_defaultdict():
    """Show defaultdict vs regular dict"""
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    
    # Regular dict approach
    def count_with_dict(words):
        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    
    # defaultdict approach
    def count_with_defaultdict(words):
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1  # No need to check if key exists
        return dict(counts)
    
    # Both produce the same result, but defaultdict is cleaner
    result1 = count_with_dict(words)
    result2 = count_with_defaultdict(words)
    print(f"Regular dict: {result1}")
    print(f"defaultdict: {result2}")

# 3. Counter for counting operations
def demonstrate_counter():
    """Show Counter vs manual counting"""
    data = [1, 2, 3, 1, 2, 1, 4, 5, 4, 1]
    
    # Manual counting
    def manual_count(data):
        counts = {}
        for item in data:
            counts[item] = counts.get(item, 0) + 1
        return counts
    
    # Using Counter
    def counter_count(data):
        return Counter(data)
    
    # Performance comparison
    large_data = [i % 100 for i in range(100000)]
    
    start = time.time()
    manual_result = manual_count(large_data)
    manual_time = time.time() - start
    
    start = time.time()
    counter_result = counter_count(large_data)
    counter_time = time.time() - start
    
    print(f"Manual counting: {manual_time:.4f}s")
    print(f"Counter: {counter_time:.4f}s")
    print(f"Counter is {manual_time/counter_time:.1f}x faster")

# compare_list_vs_deque()
# demonstrate_defaultdict()
# demonstrate_counter()
```

### Data Structure Selection Guide

#### When to Use Each Data Structure

```python
# 1. Lists - Use when you need:
# - Ordered collection
# - Random access by index
# - Frequent append operations
# - Slicing operations

def when_to_use_lists():
    # Good use cases for lists
    numbers = [1, 2, 3, 4, 5]
    
    # Random access
    middle_element = numbers[len(numbers)//2]
    
    # Slicing
    first_three = numbers[:3]
    
    # Appending
    numbers.append(6)
    
    return numbers

# 2. Sets - Use when you need:
# - Unique elements
# - Fast membership testing
# - Set operations (union, intersection, etc.)

def when_to_use_sets():
    # Remove duplicates
    numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
    unique_numbers = list(set(numbers_with_duplicates))
    
    # Fast membership testing
    valid_ids = {1, 5, 10, 15, 20}
    user_id = 10
    is_valid = user_id in valid_ids  # O(1) operation
    
    # Set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    intersection = set1 & set2  # {3, 4}
    union = set1 | set2  # {1, 2, 3, 4, 5, 6}
    
    return unique_numbers, is_valid, intersection, union

# 3. Dictionaries - Use when you need:
# - Key-value mapping
# - Fast lookups by key
# - Counting or grouping

def when_to_use_dicts():
    # Fast lookups
    user_data = {
        "john": {"age": 30, "city": "New York"},
        "jane": {"age": 25, "city": "San Francisco"}
    }
    john_info = user_data["john"]  # O(1) lookup
    
    # Counting
    text = "hello world"
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Grouping
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "A"}
    ]
    
    by_grade = {}
    for student in students:
        grade = student["grade"]
        if grade not in by_grade:
            by_grade[grade] = []
        by_grade[grade].append(student["name"])
    
    return john_info, char_counts, by_grade

# 4. Tuples - Use when you need:
# - Immutable sequences
# - Dictionary keys
# - Multiple return values

def when_to_use_tuples():
    # Coordinates (immutable)
    point = (10, 20)
    
    # Multiple return values
    def get_name_age():
        return "John", 30
    
    name, age = get_name_age()
    
    # Dictionary keys
    locations = {
        (0, 0): "origin",
        (10, 20): "point A",
        (30, 40): "point B"
    }
    
    return point, name, age, locations
```

### Advanced Data Structure Optimizations

#### Memory-Efficient Alternatives

```python
# 1. Use array for numeric data
import array

def optimize_numeric_storage():
    # Regular list (more memory)
    numbers_list = [i for i in range(10000)]
    
    # Array (less memory for numbers)
    numbers_array = array.array('i', range(10000))
    
    import sys
    print(f"List size: {sys.getsizeof(numbers_list)} bytes")
    print(f"Array size: {sys.getsizeof(numbers_array)} bytes")
    print(f"Memory savings: {sys.getsizeof(numbers_list)/sys.getsizeof(numbers_array):.1f}x")

# 2. Use slots for classes
class OptimizedClass:
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# 3. Use generators for large sequences
def large_sequence_generator(n):
    """Memory-efficient sequence generation"""
    for i in range(n):
        yield i ** 2

# Usage
def use_optimized_structures():
    # Use generator instead of list for large data
    squares = large_sequence_generator(1000000)
    
    # Process data one item at a time
    total = 0
    count = 0
    for square in squares:
        total += square
        count += 1
        if count >= 100:  # Process only first 100
            break
    
    average = total / count
    return average

# optimize_numeric_storage()
# result = use_optimized_structures()
# print(f"Average of first 100 squares: {result}")
```

### Data Structure Performance Summary

```python
def performance_summary():
    """Summary of data structure performance characteristics"""
    
    performance_table = {
        "Operation": ["Access", "Search", "Insertion", "Deletion"],
        "List": ["O(1)", "O(n)", "O(1)*", "O(n)"],
        "Tuple": ["O(1)", "O(n)", "N/A", "N/A"],
        "Set": ["N/A", "O(1)", "O(1)", "O(1)"],
        "Dict": ["O(1)", "O(1)", "O(1)", "O(1)"],
        "Deque": ["O(n)", "O(n)", "O(1)", "O(1)"]
    }
    
    print("Data Structure Performance Summary:")
    print("=" * 50)
    for i, operation in enumerate(performance_table["Operation"]):
        print(f"{operation:10} | List: {performance_table['List'][i]:4} | "
              f"Tuple: {performance_table['Tuple'][i]:4} | "
              f"Set: {performance_table['Set'][i]:4} | "
              f"Dict: {performance_table['Dict'][i]:4} | "
              f"Deque: {performance_table['Deque'][i]:4}")
    
    print("\n* O(1) for append, O(n) for insert at arbitrary position")
    print("N/A = Not Applicable (operation not supported)")

# performance_summary()
```

---

## 5. Algorithm Optimization

### Understanding Algorithm Efficiency

Algorithm optimization focuses on improving the fundamental approach to solving problems, often yielding dramatic performance improvements.

### Common Algorithm Optimization Techniques

#### 1. Divide and Conquer

```python
def merge_sort(arr):
    """Efficient O(n log n) sorting algorithm"""
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Compare with bubble sort
def bubble_sort(arr):
    """Inefficient O(n²) sorting algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def compare_sorting_algorithms():
    import random
    import time
    
    # Generate test data
    data = [random.randint(1, 1000) for _ in range(1000)]
    
    # Test bubble sort
    start = time.time()
    bubble_sorted = bubble_sort(data.copy())
    bubble_time = time.time() - start
    
    # Test merge sort
    start = time.time()
    merge_sorted = merge_sort(data.copy())
    merge_time = time.time() - start
    
    # Test built-in sort
    start = time.time()
    builtin_sorted = sorted(data)
    builtin_time = time.time() - start
    
    print(f"Bubble sort: {bubble_time:.4f}s")
    print(f"Merge sort: {merge_time:.4f}s")
    print(f"Built-in sort: {builtin_time:.4f}s")
    print(f"Merge sort is {bubble_time/merge_time:.1f}x faster than bubble sort")

# compare_sorting_algorithms()
```

#### 2. Dynamic Programming

```python
# Fibonacci: Naive vs Optimized approaches

def fibonacci_naive(n):
    """Naive recursive approach - O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_memoized(n, memo={}):
    """Memoized approach - O(n)"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

def fibonacci_iterative(n):
    """Iterative approach - O(n) time, O(1) space"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def compare_fibonacci_approaches():
    import time
    
    n = 35
    
    # Naive approach (warning: slow!)
    start = time.time()
    result_naive = fibonacci_naive(n)
    naive_time = time.time() - start
    
    # Memoized approach
    start = time.time()
    result_memo = fibonacci_memoized(n)
    memo_time = time.time() - start
    
    # Iterative approach
    start = time.time()
    result_iter = fibonacci_iterative(n)
    iter_time = time.time() - start
    
    print(f"Fibonacci({n}) = {result_naive}")
    print(f"Naive: {naive_time:.4f}s")
    print(f"Memoized: {memo_time:.4f}s")
    print(f"Iterative: {iter_time:.4f}s")
    print(f"Memoized is {naive_time/memo_time:.0f}x faster than naive")
    print(f"Iterative is {naive_time/iter_time:.0f}x faster than naive")

# compare_fibonacci_approaches()
```

#### 3. Greedy Algorithms

```python
def coin_change_greedy(amount, coins):
    """Greedy approach for coin change (works for standard coin systems)"""
    coins = sorted(coins, reverse=True)  # Start with largest coins
    result = []
    
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    
    return result if amount == 0 else None

def coin_change_dynamic(amount, coins):
    """Dynamic programming approach (works for all coin systems)"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return None
    
    # Reconstruct solution
    result = []
    current = amount
    while current > 0:
        coin = parent[current]
        result.append(coin)
        current -= coin
    
    return result

def compare_coin_change():
    amount = 67
    coins = [1, 5, 10, 25]  # Standard US coins
    
    greedy_result = coin_change_greedy(amount, coins)
    dp_result = coin_change_dynamic(amount, coins)
    
    print(f"Amount: {amount}")
    print(f"Greedy result: {greedy_result} (total: {len(greedy_result)} coins)")
    print(f"DP result: {dp_result} (total: {len(dp_result)} coins)")

# compare_coin_change()
```

### Search Algorithm Optimizations

#### Binary Search vs Linear Search

```python
def linear_search(arr, target):
    """O(n) search algorithm"""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    """O(log n) search algorithm (requires sorted array)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def compare_search_algorithms():
    import random
    import time
    
    # Create sorted test data
    size = 100000
    arr = sorted(random.randint(1, 1000000) for _ in range(size))
    target = arr[size // 2]  # Target in middle
    
    # Linear search
    start = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start
    
    # Binary search
    start = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start
    
    print(f"Array size: {size}")
    print(f"Linear search: {linear_time:.6f}s")
    print(f"Binary search: {binary_time:.6f}s")
    print(f"Binary search is {linear_time/binary_time:.0f}x faster")

# compare_search_algorithms()
```

### String Algorithm Optimizations

#### Efficient String Matching

```python
def naive_string_search(text, pattern):
    """Naive string matching - O(n*m)"""
    matches = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            matches.append(i)
    
    return matches

def kmp_string_search(text, pattern):
    """KMP algorithm - O(n+m)"""
    def compute_lps(pattern):
        """Compute Longest Prefix Suffix array"""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    matches = []
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

def compare_string_search():
    import time
    
    # Create test data
    text = "abcabcabcabc" * 1000
    pattern = "abcabc"
    
    # Naive search
    start = time.time()
    naive_matches = naive_string_search(text, pattern)
    naive_time = time.time() - start
    
    # KMP search
    start = time.time()
    kmp_matches = kmp_string_search(text, pattern)
    kmp_time = time.time() - start
    
    print(f"Text length: {len(text)}")
    print(f"Pattern: '{pattern}'")
    print(f"Matches found: {len(naive_matches)}")
    print(f"Naive search: {naive_time:.6f}s")
    print(f"KMP search: {kmp_time:.6f}s")
    print(f"KMP is {naive_time/kmp_time:.1f}x faster")

# compare_string_search()
```

### Graph Algorithm Optimizations

#### Shortest Path Algorithms

```python
from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
    
    def bfs_shortest_path(self, start, end):
        """BFS for unweighted graphs - O(V + E)"""
        if start == end:
            return [start]
        
        visited = set()
        queue = deque([(start, [start])])
        
        while queue:
            node, path = queue.popleft()
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, _ in self.graph[node]:
                if neighbor == end:
                    return path + [neighbor]
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def dijkstra_shortest_path(self, start, end):
        """Dijkstra's algorithm for weighted graphs - O((V + E) log V)"""
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0
        previous = {}
        pq = [(0, start)]
        
        while pq:
            current_distance, current = heapq.heappop(pq)
            
            if current == end:
                # Reconstruct path
                path = []
                while current in previous:
                    path.append(current)
                    current = previous[current]
                path.append(start)
                return path[::-1]
            
            if current_distance > distances[current]:
                continue
            
            for neighbor, weight in self.graph[current]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        
        return None

def demonstrate_graph_algorithms():
    # Create a sample graph
    g = Graph()
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', 1), ('B', 'D', 5),
        ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
        g.add_edge(v, u, w)  # Undirected graph
    
    # Find shortest paths
    start, end = 'A', 'E'
    
    bfs_path = g.bfs_shortest_path(start, end)
    dijkstra_path = g.dijkstra_shortest_path(start, end)
    
    print(f"BFS path (unweighted): {' -> '.join(bfs_path) if bfs_path else 'No path'}")
    print(f"Dijkstra path (weighted): {' -> '.join(dijkstra_path) if dijkstra_path else 'No path'}")

# demonstrate_graph_algorithms()
```

### Algorithm Optimization Best Practices

#### 1. Choose the Right Algorithm

```python
def algorithm_selection_guide():
    """Guide for selecting appropriate algorithms"""
    
    sorting_guide = {
        "Small arrays (< 50)": "Insertion sort",
        "General purpose": "Timsort (Python's built-in)",
        "Memory constrained": "Heap sort",
        "Stable sort needed": "Merge sort",
        "Nearly sorted data": "Insertion sort or Timsort"
    }
    
    search_guide = {
        "Unsorted data": "Linear search",
        "Sorted data": "Binary search",
        "Frequent searches": "Hash table (dict/set)",
        "Range queries": "Binary search tree or segment tree"
    }
    
    print("Algorithm Selection Guide:")
    print("\nSorting:")
    for case, algorithm in sorting_guide.items():
        print(f"  {case}: {algorithm}")
    
    print("\nSearching:")
    for case, algorithm in search_guide.items():
        print(f"  {case}: {algorithm}")

# algorithm_selection_guide()
```

#### 2. Optimize for Your Data

```python
def data_specific_optimizations():
    """Examples of optimizations based on data characteristics"""
    
    # For mostly sorted data
    def optimized_sort_for_nearly_sorted(arr):
        """Use insertion sort for nearly sorted data"""
        if len(arr) < 50:  # Small arrays
            return insertion_sort(arr)
        else:
            return sorted(arr)  # Timsort handles this well
    
    # For data with many duplicates
    def optimized_sort_for_duplicates(arr):
        """Use counting sort for data with limited range"""
        if len(set(arr)) < len(arr) // 2:  # Many duplicates
            return counting_sort(arr)
        else:
            return sorted(arr)
    
    # For searching in static data
    def optimized_search_for_static_data(data, queries):
        """Preprocess data for multiple queries"""
        # Convert to set for O(1) lookups
        data_set = set(data)
        results = []
        
        for query in queries:
            results.append(query in data_set)
        
        return results

def insertion_sort(arr):
    """Simple insertion sort for small arrays"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def counting_sort(arr):
    """Counting sort for arrays with limited range"""
    if not arr:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Calculate cumulative count
    for i in range(1, range_size):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output
```

---

## 6. Profiling and Benchmarking

### Understanding Performance Profiling

Profiling is the process of measuring where your program spends its time and resources. It's essential for identifying bottlenecks and optimizing effectively.

### Built-in Profiling Tools

#### 1. Using `cProfile`

```python
import cProfile
import pstats
import io
from functools import wraps

def profile_function(func):
    """Decorator to profile a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        
        # Create a string buffer to capture the output
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        
        print(f"Profile for {func.__name__}:")
        print(s.getvalue())
        return result
    return wrapper

# Example usage
@profile_function
def slow_function():
    """A deliberately slow function for demonstration"""
    import time
    
    # Simulate some work
    total = 0
    for i in range(1000000):
        total += i ** 2
    
    # Simulate I/O operation
    time.sleep(0.1)
    
    return total

# slow_function()
```

#### 2. Using `timeit` for Micro-benchmarks

```python
import timeit
from functools import partial

def benchmark_functions(*functions, number=10000, setup=""):
    """Benchmark multiple functions"""
    results = {}
    
    for func in functions:
        if callable(func):
            # Time the function
            time_taken = timeit.timeit(func, number=number, setup=setup)
            results[func.__name__] = time_taken
        else:
            # Time a code string
            time_taken = timeit.timeit(func, number=number, setup=setup)
            results[func] = time_taken
    
    # Sort by performance
    sorted_results = sorted(results.items(), key=lambda x: x[1])
    
    print(f"Benchmark Results ({number} iterations):")
    print("-" * 50)
    fastest_time = sorted_results[0][1]
    
    for name, time_taken in sorted_results:
        speedup = time_taken / fastest_time
        print(f"{name:30} {time_taken:.6f}s ({speedup:.2f}x)")

# Example: Compare different ways to create lists
def list_comprehension():
    return [i**2 for i in range(1000)]

def map_function():
    return list(map(lambda x: x**2, range(1000)))

def for_loop():
    result = []
    for i in range(1000):
        result.append(i**2)
    return result

# benchmark_functions(list_comprehension, map_function, for_loop, number=1000)
```

#### 3. Using `line_profiler` for Line-by-Line Analysis

```python
# Note: Requires installation: pip install line_profiler
# Usage: kernprof -l -v script.py

def demonstrate_line_profiling():
    """Example function for line profiling"""
    
    # @profile  # Uncomment when using line_profiler
    def process_data(data):
        """Function to be profiled line by line"""
        # Step 1: Filter data
        filtered = [x for x in data if x > 0]
        
        # Step 2: Transform data
        transformed = [x**2 for x in filtered]
        
        # Step 3: Aggregate data
        total = sum(transformed)
        average = total / len(transformed) if transformed else 0
        
        return average
    
    # Generate test data
    import random
    test_data = [random.randint(-100, 100) for _ in range(10000)]
    
    # Process the data
    result = process_data(test_data)
    return result

# result = demonstrate_line_profiling()
```

### Memory Profiling

#### 1. Using `tracemalloc`

```python
import tracemalloc
import linecache

def memory_profile_function(func):
    """Decorator to profile memory usage"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start tracing
        tracemalloc.start()
        
        # Execute function
        result = func(*args, **kwargs)
        
        # Get memory statistics
        current, peak = tracemalloc.get_traced_memory()
        
        print(f"Memory Profile for {func.__name__}:")
        print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
        print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
        
        # Get top memory allocations
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        
        print("\nTop 3 memory allocations:")
        for index, stat in enumerate(top_stats[:3], 1):
            frame = stat.traceback.format()[-1]
            print(f"{index}. {frame}")
            print(f"   Size: {stat.size / 1024:.1f} KB")
        
        tracemalloc.stop()
        return result
    return wrapper

@memory_profile_function
def memory_intensive_function():
    """Function that uses significant memory"""
    # Create large data structures
    large_list = [i for i in range(1000000)]
    large_dict = {i: i**2 for i in range(100000)}
    
    # Process data
    result = sum(large_list) + sum(large_dict.values())
    
    return result

# memory_intensive_function()
```

#### 2. Using `memory_profiler`

```python
# Note: Requires installation: pip install memory-profiler
# Usage: python -m memory_profiler script.py

def demonstrate_memory_profiler():
    """Example for memory_profiler usage"""
    
    # @profile  # Uncomment when using memory_profiler
    def memory_heavy_function():
        """Function to be memory profiled"""
        import numpy as np
        
        # Create large arrays
        a = np.random.random((1000, 1000))
        b = np.random.random((1000, 1000))
        
        # Perform operations
        c = np.dot(a, b)
        d = c + a
        
        return d.sum()
    
    return memory_heavy_function()

# result = demonstrate_memory_profiler()
```

### Custom Benchmarking Framework

#### Creating a Comprehensive Benchmark Suite

```python
import time
import statistics
import gc
from contextlib import contextmanager

class PerformanceBenchmark:
    """Comprehensive benchmarking framework"""
    
    def __init__(self):
        self.results = {}
    
    @contextmanager
    def timer(self, name):
        """Context manager for timing code blocks"""
        start_time = time.perf_counter()
        try:
            yield
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            
            if name not in self.results:
                self.results[name] = []
            self.results[name].append(execution_time)
    
    def benchmark_function(self, func, *args, iterations=10, warmup=2, **kwargs):
        """Benchmark a function with multiple iterations"""
        name = func.__name__
        
        # Warmup runs
        for _ in range(warmup):
            func(*args, **kwargs)
        
        # Actual benchmark runs
        times = []
        for _ in range(iterations):
            gc.collect()  # Force garbage collection
            start = time.perf_counter()
            func(*args, **kwargs)
            end = time.perf_counter()
            times.append(end - start)
        
        self.results[name] = times
        return times
    
    def compare_functions(self, functions, *args, iterations=10, **kwargs):
        """Compare multiple functions"""
        for func in functions:
            self.benchmark_function(func, *args, iterations=iterations, **kwargs)
    
    def print_results(self):
        """Print benchmark results with statistics"""
        if not self.results:
            print("No benchmark results available")
            return
        
        print("Benchmark Results:")
        print("=" * 80)
        print(f"{'Function':<25} {'Mean':<12} {'Std Dev':<12} {'Min':<12} {'Max':<12}")
        print("-" * 80)
        
        # Sort by mean time
        sorted_results = sorted(
            self.results.items(), 
            key=lambda x: statistics.mean(x[1])
        )
        
        fastest_mean = statistics.mean(sorted_results[0][1])
        
        for name, times in sorted_results:
            mean_time = statistics.mean(times)
            std_dev = statistics.stdev(times) if len(times) > 1 else 0
            min_time = min(times)
            max_time = max(times)
            speedup = mean_time / fastest_mean
            
            print(f"{name:<25} {mean_time:<12.6f} {std_dev:<12.6f} "
                  f"{min_time:<12.6f} {max_time:<12.6f} ({speedup:.2f}x)")
    
    def clear_results(self):
        """Clear all benchmark results"""
        self.results.clear()

# Example usage
def demonstrate_benchmark_framework():
    """Demonstrate the benchmarking framework"""
    benchmark = PerformanceBenchmark()
    
    # Define test functions
    def string_concat_plus(words):
        result = ""
        for word in words:
            result += word
        return result
    
    def string_concat_join(words):
        return "".join(words)
    
    def string_concat_format(words):
        return "{}".format("".join(words))
    
    # Test data
    test_words = ["hello"] * 1000
    
    # Benchmark functions
    functions = [string_concat_plus, string_concat_join, string_concat_format]
    benchmark.compare_functions(functions, test_words, iterations=10)
    
    # Print results
    benchmark.print_results()

# demonstrate_benchmark_framework()
```

### Performance Testing Best Practices

#### 1. Statistical Significance

```python
import statistics
import math

def is_statistically_significant(times1, times2, confidence=0.95):
    """Check if performance difference is statistically significant"""
    n1, n2 = len(times1), len(times2)
    mean1, mean2 = statistics.mean(times1), statistics.mean(times2)
    var1, var2 = statistics.variance(times1), statistics.variance(times2)
    
    # Welch's t-test for unequal variances
    pooled_se = math.sqrt(var1/n1 + var2/n2)
    t_stat = (mean1 - mean2) / pooled_se
    
    # Degrees of freedom (Welch-Satterthwaite equation)
    df = (var1/n1 + var2/n2)**2 / ((var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1))
    
    # Critical value for 95% confidence (approximation)
    critical_value = 2.0  # Simplified for demonstration
    
    is_significant = abs(t_stat) > critical_value
    
    return {
        'significant': is_significant,
        't_statistic': t_stat,
        'degrees_of_freedom': df,
        'mean_difference': mean2 - mean1,
        'percent_change': ((mean2 - mean1) / mean1) * 100
    }

def robust_benchmark_comparison(func1, func2, *args, iterations=20, **kwargs):
    """Perform robust comparison of two functions"""
    benchmark = PerformanceBenchmark()
    
    # Benchmark both functions
    times1 = benchmark.benchmark_function(func1, *args, iterations=iterations, **kwargs)
    times2 = benchmark.benchmark_function(func2, *args, iterations=iterations, **kwargs)
    
    # Statistical analysis
    stats = is_statistically_significant(times1, times2)
    
    print(f"Comparison: {func1.__name__} vs {func2.__name__}")
    print(f"Function 1 mean: {statistics.mean(times1):.6f}s")
    print(f"Function 2 mean: {statistics.mean(times2):.6f}s")
    print(f"Difference: {stats['percent_change']:.2f}%")
    print(f"Statistically significant: {stats['significant']}")
    
    return stats
```

#### 2. Environment Control

```python
import os
import psutil
import platform

def get_system_info():
    """Get system information for benchmark context"""
    info = {
        'platform': platform.platform(),
        'processor': platform.processor(),
        'python_version': platform.python_version(),
        'cpu_count': os.cpu_count(),
        'memory_total': psutil.virtual_memory().total / (1024**3),  # GB
        'memory_available': psutil.virtual_memory().available / (1024**3),  # GB
    }
    return info

def controlled_benchmark(func, *args, **kwargs):
    """Run benchmark with environment monitoring"""
    # Check system load
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    
    if cpu_percent > 50:
        print(f"Warning: High CPU usage ({cpu_percent}%)")
    if memory_percent > 80:
        print(f"Warning: High memory usage ({memory_percent}%)")
    
    # Get system info
    sys_info = get_system_info()
    print("System Information:")
    for key, value in sys_info.items():
        print(f"  {key}: {value}")
    
    # Run benchmark
    benchmark = PerformanceBenchmark()
    times = benchmark.benchmark_function(func, *args, **kwargs)
    
    return times, sys_info

# Example usage
def example_controlled_benchmark():
    def test_function():
        return sum(i**2 for i in range(10000))
    
    times, sys_info = controlled_benchmark(test_function, iterations=10)
    print(f"\nBenchmark completed: {statistics.mean(times):.6f}s average")

# example_controlled_benchmark()
```

### Profiling Real-World Applications

#### Web Application Profiling

```python
import functools
import time
from collections import defaultdict

class WebAppProfiler:
    """Profiler for web applications"""
    
    def __init__(self):
        self.request_times = defaultdict(list)
        self.function_times = defaultdict(list)
    
    def profile_request(self, endpoint):
        """Decorator for profiling web requests"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    end_time = time.perf_counter()
                    execution_time = end_time - start_time
                    self.request_times[endpoint].append(execution_time)
            return wrapper
        return decorator
    
    def profile_function(self, func):
        """Decorator for profiling individual functions"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                self.function_times[func.__name__].append(execution_time)
        return wrapper
    
    def get_report(self):
        """Generate performance report"""
        report = {
            'requests': {},
            'functions': {}
        }
        
        # Request statistics
        for endpoint, times in self.request_times.items():
            report['requests'][endpoint] = {
                'count': len(times),
                'mean': statistics.mean(times),
                'median': statistics.median(times),
                'p95': sorted(times)[int(0.95 * len(times))] if times else 0,
                'total': sum(times)
            }
        
        # Function statistics
        for func_name, times in self.function_times.items():
            report['functions'][func_name] = {
                'count': len(times),
                'mean': statistics.mean(times),
                'total': sum(times)
            }
        
        return report

# Example usage
profiler = WebAppProfiler()

@profiler.profile_request('/api/users')
def get_users():
    """Simulated API endpoint"""
    time.sleep(0.01)  # Simulate database query
    return {"users": ["user1", "user2"]}

@profiler.profile_function
def database_query():
    """Simulated database operation"""
    time.sleep(0.005)
    return "query result"

# Simulate some requests
# for _ in range(10):
#     get_users()
#     database_query()

# print(profiler.get_report())
```

---