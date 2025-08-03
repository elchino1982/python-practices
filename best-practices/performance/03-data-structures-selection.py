"""Question: Demonstrate optimal data structure selection for different performance scenarios.

Create examples showing when to use different data structures (list, set, dict, deque, etc.)
based on performance characteristics and use cases.

Requirements:
1. Compare performance of different data structures for common operations
2. Show time complexity analysis for each operation
3. Demonstrate real-world scenarios where each structure excels
4. Include benchmarking examples
5. Provide guidelines for data structure selection

Example usage:
    analyzer = DataStructureAnalyzer()
    analyzer.compare_search_performance()
    analyzer.compare_insertion_performance()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what data structures you need to compare
# - Start with simple performance tests
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
# - What operations do you want to benchmark? (search, insert, delete, access)
# - Which data structures should you compare? (list, set, dict, deque, tuple)
# - How will you measure performance? (time.time(), timeit module)
# - What scenarios represent real-world use cases?
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


# Step 1: Import required modules and create basic performance testing utilities
# ===============================================================================

# Explanation:
# We need timing utilities to measure performance and various data structures
# to compare. We'll start with basic imports and a simple timing decorator.

import time
import timeit
from collections import deque, defaultdict
from typing import List, Set, Dict, Any, Callable
import random
import sys

def time_operation(func: Callable) -> Callable:
    """Decorator to measure execution time of operations."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper


# Step 2: Create the main DataStructureAnalyzer class
# ===============================================================================

# Explanation:
# This class will contain all our performance comparison methods.
# We'll start with basic setup and data generation methods.

class DataStructureAnalyzer:
    """Analyzes and compares performance of different data structures."""
    
    def __init__(self, data_size: int = 10000):
        """Initialize with configurable data size for testing."""
        self.data_size = data_size
        self.test_data = self._generate_test_data()
        self.search_targets = random.sample(self.test_data, min(100, len(self.test_data)))
    
    def _generate_test_data(self) -> List[int]:
        """Generate random test data for benchmarking."""
        return [random.randint(1, self.data_size * 2) for _ in range(self.data_size)]
    
    def print_complexity_info(self):
        """Print time complexity information for common operations."""
        print("=" * 60)
        print("TIME COMPLEXITY REFERENCE")
        print("=" * 60)
        print("Data Structure | Access | Search | Insertion | Deletion")
        print("-" * 60)
        print("List           | O(1)   | O(n)   | O(1)*     | O(n)")
        print("Set            | N/A    | O(1)   | O(1)      | O(1)")
        print("Dict           | O(1)   | O(1)   | O(1)      | O(1)")
        print("Deque          | O(n)   | O(n)   | O(1)      | O(1)")
        print("Tuple          | O(1)   | O(n)   | N/A       | N/A")
        print("-" * 60)
        print("* O(1) for append, O(n) for insert at arbitrary position")
        print("=" * 60)


# Step 3: Add search performance comparison methods
# ===============================================================================

# Explanation:
# Search operations are fundamental and show clear differences between
# data structures. Lists use linear search, while sets and dicts use hashing.

    def compare_search_performance(self):
        """Compare search performance across different data structures."""
        print("\n" + "=" * 60)
        print("SEARCH PERFORMANCE COMPARISON")
        print("=" * 60)
        
        # Prepare data structures
        test_list = list(self.test_data)
        test_set = set(self.test_data)
        test_dict = {item: f"value_{item}" for item in self.test_data}
        test_tuple = tuple(self.test_data)
        
        print(f"Searching for {len(self.search_targets)} items in {self.data_size} elements...")
        print()
        
        # List search (O(n))
        start_time = time.perf_counter()
        list_found = sum(1 for target in self.search_targets if target in test_list)
        list_time = time.perf_counter() - start_time
        print(f"List search:   {list_time:.6f} seconds (found {list_found} items)")
        
        # Set search (O(1))
        start_time = time.perf_counter()
        set_found = sum(1 for target in self.search_targets if target in test_set)
        set_time = time.perf_counter() - start_time
        print(f"Set search:    {set_time:.6f} seconds (found {set_found} items)")
        
        # Dict search (O(1))
        start_time = time.perf_counter()
        dict_found = sum(1 for target in self.search_targets if target in test_dict)
        dict_time = time.perf_counter() - start_time
        print(f"Dict search:   {dict_time:.6f} seconds (found {dict_found} items)")
        
        # Tuple search (O(n))
        start_time = time.perf_counter()
        tuple_found = sum(1 for target in self.search_targets if target in test_tuple)
        tuple_time = time.perf_counter() - start_time
        print(f"Tuple search:  {tuple_time:.6f} seconds (found {tuple_found} items)")
        
        print()
        print("Performance ratio (compared to set):")
        print(f"List is {list_time/set_time:.1f}x slower than set")
        print(f"Dict is {dict_time/set_time:.1f}x compared to set")
        print(f"Tuple is {tuple_time/set_time:.1f}x slower than set")


# Step 4: Add insertion performance comparison methods
# ===============================================================================

# Explanation:
# Insertion performance varies greatly depending on where you insert.
# We'll compare append, prepend, and middle insertion operations.

    def compare_insertion_performance(self):
        """Compare insertion performance across different data structures."""
        print("\n" + "=" * 60)
        print("INSERTION PERFORMANCE COMPARISON")
        print("=" * 60)
        
        insertion_count = 1000
        new_items = [random.randint(1, 100000) for _ in range(insertion_count)]
        
        print(f"Inserting {insertion_count} items...")
        print()
        
        # List append (O(1) amortized)
        test_list = []
        start_time = time.perf_counter()
        for item in new_items:
            test_list.append(item)
        list_append_time = time.perf_counter() - start_time
        print(f"List append:        {list_append_time:.6f} seconds")
        
        # List prepend (O(n))
        test_list = []
        start_time = time.perf_counter()
        for item in new_items:
            test_list.insert(0, item)
        list_prepend_time = time.perf_counter() - start_time
        print(f"List prepend:       {list_prepend_time:.6f} seconds")
        
        # Set add (O(1) amortized)
        test_set = set()
        start_time = time.perf_counter()
        for item in new_items:
            test_set.add(item)
        set_add_time = time.perf_counter() - start_time
        print(f"Set add:            {set_add_time:.6f} seconds")
        
        # Dict insert (O(1) amortized)
        test_dict = {}
        start_time = time.perf_counter()
        for item in new_items:
            test_dict[item] = f"value_{item}"
        dict_insert_time = time.perf_counter() - start_time
        print(f"Dict insert:        {dict_insert_time:.6f} seconds")
        
        # Deque append (O(1))
        test_deque = deque()
        start_time = time.perf_counter()
        for item in new_items:
            test_deque.append(item)
        deque_append_time = time.perf_counter() - start_time
        print(f"Deque append:       {deque_append_time:.6f} seconds")
        
        # Deque prepend (O(1))
        test_deque = deque()
        start_time = time.perf_counter()
        for item in new_items:
            test_deque.appendleft(item)
        deque_prepend_time = time.perf_counter() - start_time
        print(f"Deque prepend:      {deque_prepend_time:.6f} seconds")
        
        print()
        print("Key insights:")
        print(f"- List prepend is {list_prepend_time/list_append_time:.1f}x slower than append")
        print(f"- Deque prepend is {deque_prepend_time/deque_append_time:.1f}x compared to append")
        print(f"- Set operations are {set_add_time/list_append_time:.1f}x compared to list append")


# Step 5: Add deletion performance comparison methods
# ===============================================================================

# Explanation:
# Deletion performance depends on the position and data structure.
# We'll compare removing from different positions and using different methods.

    def compare_deletion_performance(self):
        """Compare deletion performance across different data structures."""
        print("\n" + "=" * 60)
        print("DELETION PERFORMANCE COMPARISON")
        print("=" * 60)
        
        deletion_count = 500
        
        # Prepare data structures with same data
        base_data = list(range(2000))
        random.shuffle(base_data)
        items_to_delete = random.sample(base_data, deletion_count)
        
        print(f"Deleting {deletion_count} items from structures with {len(base_data)} elements...")
        print()
        
        # List remove by value (O(n) per operation)
        test_list = base_data.copy()
        start_time = time.perf_counter()
        for item in items_to_delete:
            if item in test_list:
                test_list.remove(item)
        list_remove_time = time.perf_counter() - start_time
        print(f"List remove by value:    {list_remove_time:.6f} seconds")
        
        # List pop from end (O(1))
        test_list = base_data.copy()
        start_time = time.perf_counter()
        for _ in range(deletion_count):
            if test_list:
                test_list.pop()
        list_pop_end_time = time.perf_counter() - start_time
        print(f"List pop from end:       {list_pop_end_time:.6f} seconds")
        
        # List pop from beginning (O(n))
        test_list = base_data.copy()
        start_time = time.perf_counter()
        for _ in range(deletion_count):
            if test_list:
                test_list.pop(0)
        list_pop_start_time = time.perf_counter() - start_time
        print(f"List pop from start:     {list_pop_start_time:.6f} seconds")
        
        # Set remove (O(1))
        test_set = set(base_data)
        start_time = time.perf_counter()
        for item in items_to_delete:
            test_set.discard(item)  # discard doesn't raise error if item not found
        set_remove_time = time.perf_counter() - start_time
        print(f"Set remove:              {set_remove_time:.6f} seconds")
        
        # Dict delete (O(1))
        test_dict = {item: f"value_{item}" for item in base_data}
        start_time = time.perf_counter()
        for item in items_to_delete:
            test_dict.pop(item, None)  # pop with default doesn't raise error
        dict_delete_time = time.perf_counter() - start_time
        print(f"Dict delete:             {dict_delete_time:.6f} seconds")
        
        # Deque pop from end (O(1))
        test_deque = deque(base_data)
        start_time = time.perf_counter()
        for _ in range(deletion_count):
            if test_deque:
                test_deque.pop()
        deque_pop_end_time = time.perf_counter() - start_time
        print(f"Deque pop from end:      {deque_pop_end_time:.6f} seconds")
        
        # Deque pop from start (O(1))
        test_deque = deque(base_data)
        start_time = time.perf_counter()
        for _ in range(deletion_count):
            if test_deque:
                test_deque.popleft()
        deque_pop_start_time = time.perf_counter() - start_time
        print(f"Deque pop from start:    {deque_pop_start_time:.6f} seconds")
        
        print()
        print("Key insights:")
        print(f"- List remove by value is {list_remove_time/set_remove_time:.1f}x slower than set")
        print(f"- List pop from start is {list_pop_start_time/list_pop_end_time:.1f}x slower than from end")
        print(f"- Deque pop from start is {deque_pop_start_time/deque_pop_end_time:.1f}x compared to from end")


# Step 6: Add memory usage comparison methods
# ===============================================================================

# Explanation:
# Memory usage is crucial for large datasets. Different data structures
# have different memory overhead and storage efficiency.

    def compare_memory_usage(self):
        """Compare memory usage of different data structures."""
        print("\n" + "=" * 60)
        print("MEMORY USAGE COMPARISON")
        print("=" * 60)
        
        # Create test data
        test_size = 10000
        test_data = list(range(test_size))
        
        # Measure memory usage
        test_list = list(test_data)
        test_tuple = tuple(test_data)
        test_set = set(test_data)
        test_dict = {i: f"value_{i}" for i in test_data}
        test_deque = deque(test_data)
        
        # Calculate sizes
        list_size = sys.getsizeof(test_list) + sum(sys.getsizeof(item) for item in test_list)
        tuple_size = sys.getsizeof(test_tuple) + sum(sys.getsizeof(item) for item in test_tuple)
        set_size = sys.getsizeof(test_set) + sum(sys.getsizeof(item) for item in test_set)
        dict_size = sys.getsizeof(test_dict) + sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in test_dict.items())
        deque_size = sys.getsizeof(test_deque) + sum(sys.getsizeof(item) for item in test_deque)
        
        print(f"Memory usage for {test_size} integers:")
        print()
        print(f"List:     {list_size:,} bytes ({list_size/test_size:.1f} bytes per item)")
        print(f"Tuple:    {tuple_size:,} bytes ({tuple_size/test_size:.1f} bytes per item)")
        print(f"Set:      {set_size:,} bytes ({set_size/test_size:.1f} bytes per item)")
        print(f"Dict:     {dict_size:,} bytes ({dict_size/test_size:.1f} bytes per item)")
        print(f"Deque:    {deque_size:,} bytes ({deque_size/test_size:.1f} bytes per item)")
        
        print()
        print("Memory efficiency (compared to list):")
        print(f"Tuple is {tuple_size/list_size:.2f}x list size")
        print(f"Set is {set_size/list_size:.2f}x list size")
        print(f"Dict is {dict_size/list_size:.2f}x list size")
        print(f"Deque is {deque_size/list_size:.2f}x list size")
        
        print()
        print("Memory characteristics:")
        print("- Tuple: Most memory efficient for immutable sequences")
        print("- List: Good balance of memory and functionality")
        print("- Set: Higher overhead due to hash table structure")
        print("- Dict: Highest memory usage due to key-value storage")
        print("- Deque: Similar to list but with double-ended optimization")


# Step 7: Add real-world scenario examples
# ===============================================================================

# Explanation:
# Real-world scenarios help understand when to choose each data structure.
# We'll demonstrate practical use cases with performance implications.

    def demonstrate_real_world_scenarios(self):
        """Demonstrate real-world scenarios for data structure selection."""
        print("\n" + "=" * 60)
        print("REAL-WORLD SCENARIO DEMONSTRATIONS")
        print("=" * 60)
        
        self._scenario_unique_visitors()
        self._scenario_task_queue()
        self._scenario_cache_implementation()
        self._scenario_coordinate_storage()
    
    def _scenario_unique_visitors(self):
        """Scenario: Tracking unique website visitors."""
        print("\nScenario 1: Tracking Unique Website Visitors")
        print("-" * 50)
        
        # Simulate visitor IDs
        visitor_logs = [f"user_{random.randint(1, 1000)}" for _ in range(5000)]
        
        print("Task: Count unique visitors from log entries")
        print(f"Processing {len(visitor_logs)} log entries...")
        
        # Using list (inefficient)
        start_time = time.perf_counter()
        unique_visitors_list = []
        for visitor in visitor_logs:
            if visitor not in unique_visitors_list:
                unique_visitors_list.append(visitor)
        list_time = time.perf_counter() - start_time
        
        # Using set (efficient)
        start_time = time.perf_counter()
        unique_visitors_set = set(visitor_logs)
        set_time = time.perf_counter() - start_time
        
        print(f"List approach: {list_time:.6f} seconds ({len(unique_visitors_list)} unique)")
        print(f"Set approach:  {set_time:.6f} seconds ({len(unique_visitors_set)} unique)")
        print(f"Set is {list_time/set_time:.1f}x faster!")
        print("Recommendation: Use set for uniqueness checking")
    
    def _scenario_task_queue(self):
        """Scenario: Task queue processing."""
        print("\nScenario 2: Task Queue Processing")
        print("-" * 50)
        
        tasks = [f"task_{i}" for i in range(1000)]
        
        print("Task: Process tasks in FIFO order with frequent additions")
        
        # Using list (inefficient for queue operations)
        task_list = tasks.copy()
        start_time = time.perf_counter()
        processed = 0
        while task_list and processed < 500:
            task_list.pop(0)  # Remove from front (O(n))
            if processed % 100 == 0:  # Simulate adding new tasks
                task_list.extend([f"new_task_{i}" for i in range(10)])
            processed += 1
        list_time = time.perf_counter() - start_time
        
        # Using deque (efficient for queue operations)
        task_deque = deque(tasks)
        start_time = time.perf_counter()
        processed = 0
        while task_deque and processed < 500:
            task_deque.popleft()  # Remove from front (O(1))
            if processed % 100 == 0:  # Simulate adding new tasks
                task_deque.extend([f"new_task_{i}" for i in range(10)])
            processed += 1
        deque_time = time.perf_counter() - start_time
        
        print(f"List approach:  {list_time:.6f} seconds")
        print(f"Deque approach: {deque_time:.6f} seconds")
        print(f"Deque is {list_time/deque_time:.1f}x faster!")
        print("Recommendation: Use deque for queue operations")
    
    def _scenario_cache_implementation(self):
        """Scenario: Simple cache implementation."""
        print("\nScenario 3: Cache Implementation")
        print("-" * 50)
        
        print("Task: Implement a simple cache with fast lookups")
        
        # Simulate cache operations
        cache_operations = [(random.choice(['get', 'set']), f"key_{random.randint(1, 100)}") 
                           for _ in range(1000)]
        
        # Using list of tuples (inefficient)
        cache_list = []
        start_time = time.perf_counter()
        for operation, key in cache_operations:
            if operation == 'get':
                found = any(k == key for k, v in cache_list)
            else:  # set
                # Remove existing key if present
                cache_list = [(k, v) for k, v in cache_list if k != key]
                cache_list.append((key, f"value_{key}"))
        list_time = time.perf_counter() - start_time
        
        # Using dictionary (efficient)
        cache_dict = {}
        start_time = time.perf_counter()
        for operation, key in cache_operations:
            if operation == 'get':
                found = key in cache_dict
            else:  # set
                cache_dict[key] = f"value_{key}"
        dict_time = time.perf_counter() - start_time
        
        print(f"List approach: {list_time:.6f} seconds")
        print(f"Dict approach: {dict_time:.6f} seconds")
        print(f"Dict is {list_time/dict_time:.1f}x faster!")
        print("Recommendation: Use dict for key-value caching")
    
    def _scenario_coordinate_storage(self):
        """Scenario: Storing immutable coordinates."""
        print("\nScenario 4: Storing Immutable Coordinates")
        print("-" * 50)
        
        print("Task: Store 2D coordinates efficiently")
        
        # Generate coordinate data
        coordinates_data = [(random.randint(0, 1000), random.randint(0, 1000)) 
                           for _ in range(10000)]
        
        # Using list of lists (mutable, more memory)
        coords_list = [[x, y] for x, y in coordinates_data]
        list_memory = sys.getsizeof(coords_list) + sum(sys.getsizeof(coord) for coord in coords_list)
        
        # Using list of tuples (immutable, less memory)
        coords_tuples = [(x, y) for x, y in coordinates_data]
        tuple_memory = sys.getsizeof(coords_tuples) + sum(sys.getsizeof(coord) for coord in coords_tuples)
        
        print(f"List of lists: {list_memory:,} bytes")
        print(f"List of tuples: {tuple_memory:,} bytes")
        print(f"Tuples use {tuple_memory/list_memory:.2f}x memory of lists")
        print("Recommendation: Use tuples for immutable coordinate pairs")


# Step 8: Add data structure selection guidelines
# ===============================================================================

# Explanation:
# Provide clear guidelines for when to use each data structure based on
# common operations and requirements.

    def print_selection_guidelines(self):
        """Print comprehensive guidelines for data structure selection."""
        print("\n" + "=" * 60)
        print("DATA STRUCTURE SELECTION GUIDELINES")
        print("=" * 60)
        
        print("\n🔍 WHEN TO USE EACH DATA STRUCTURE:")
        print("-" * 40)
        
        print("\n📋 LIST - Use when you need:")
        print("  ✓ Ordered collection with duplicates")
        print("  ✓ Index-based access (my_list[0])")
        print("  ✓ Frequent appending to end")
        print("  ✓ Slicing operations")
        print("  ✗ Avoid for: frequent searching, prepending")
        
        print("\n📦 TUPLE - Use when you need:")
        print("  ✓ Immutable ordered collection")
        print("  ✓ Dictionary keys or set elements")
        print("  ✓ Memory-efficient storage")
        print("  ✓ Coordinates, RGB values, database records")
        print("  ✗ Avoid for: data that needs modification")
        
        print("\n🎯 SET - Use when you need:")
        print("  ✓ Unique elements only")
        print("  ✓ Fast membership testing (item in set)")
        print("  ✓ Set operations (union, intersection)")
        print("  ✓ Removing duplicates")
        print("  ✗ Avoid for: ordered data, index access")
        
        print("\n🗂️  DICT - Use when you need:")
        print("  ✓ Key-value mapping")
        print("  ✓ Fast lookups by key")
        print("  ✓ Caching/memoization")
        print("  ✓ Counting occurrences")
        print("  ✗ Avoid for: simple sequences")
        
        print("\n🔄 DEQUE - Use when you need:")
        print("  ✓ Queue/stack operations")
        print("  ✓ Frequent additions/removals at both ends")
        print("  ✓ FIFO or LIFO processing")
        print("  ✓ Sliding window algorithms")
        print("  ✗ Avoid for: random access by index")
        
        print("\n⚡ PERFORMANCE DECISION TREE:")
        print("-" * 40)
        print("Need fast search? → Use SET or DICT")
        print("Need ordering? → Use LIST or TUPLE")
        print("Need mutability? → Use LIST, SET, or DICT")
        print("Need queue operations? → Use DEQUE")
        print("Need memory efficiency? → Use TUPLE")
        print("Need key-value pairs? → Use DICT")


# Step 9: Create comprehensive demonstration and main execution
# ===============================================================================

# Explanation:
# Bring everything together with a complete demonstration that shows
# all the comparisons and provides a full analysis.

def demonstrate_complete_analysis():
    """Run a complete data structure performance analysis."""
    print("🚀 COMPLETE DATA STRUCTURE PERFORMANCE ANALYSIS")
    print("=" * 80)
    
    # Create analyzer with different sizes for comprehensive testing
    print("\nTesting with different data sizes...")
    
    for size in [1000, 5000, 10000]:
        print(f"\n{'='*20} DATA SIZE: {size:,} {'='*20}")
        analyzer = DataStructureAnalyzer(data_size=size)
        
        # Run all comparisons
        analyzer.print_complexity_info()
        analyzer.compare_search_performance()
        analyzer.compare_insertion_performance()
        analyzer.compare_deletion_performance()
        
        if size == 10000:  # Only run memory test once
            analyzer.compare_memory_usage()
            analyzer.demonstrate_real_world_scenarios()
            analyzer.print_selection_guidelines()


# ===============================================================================
#                              EXAMPLE USAGE
# ===============================================================================

if __name__ == "__main__":
    # Example 1: Quick analysis
    print("Example 1: Quick Performance Analysis")
    print("-" * 50)
    analyzer = DataStructureAnalyzer(data_size=5000)
    analyzer.compare_search_performance()
    analyzer.compare_insertion_performance()
    
    print("\n" + "="*80)
    
    # Example 2: Complete analysis
    print("Example 2: Complete Analysis")
    print("-" * 50)
    demonstrate_complete_analysis()
    
    print("\n" + "="*80)
    
    # Example 3: Specific scenario testing
    print("Example 3: Real-world Scenarios")
    print("-" * 50)
    analyzer = DataStructureAnalyzer(data_size=3000)
    analyzer.demonstrate_real_world_scenarios()
    analyzer.print_selection_guidelines()

