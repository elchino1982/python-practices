"""Question: Implement algorithm optimization techniques to improve performance.

Create examples demonstrating various algorithm optimization strategies including:
time complexity reduction, space optimization, and efficient data structure usage.

Requirements:
1. Demonstrate O(n²) to O(n log n) optimization for sorting
2. Show space-time tradeoffs with memoization
3. Implement efficient search algorithms
4. Optimize data structure selection
5. Demonstrate algorithmic improvements for common problems

Example usage:
    optimizer = AlgorithmOptimizer()
    result = optimizer.optimized_search(data, target)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about time and space complexity
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
# - What are the most common performance bottlenecks?
# - How can you reduce time complexity?
# - When should you trade space for time?
# - Which data structures are most efficient for different operations?
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


# Step 1: Import modules and create basic optimization examples
# ===============================================================================

# Explanation:
# Algorithm optimization starts with understanding time and space complexity.
# We'll create examples showing inefficient vs efficient approaches.

import time
import functools
from typing import List, Dict, Any, Optional, Tuple
from collections import defaultdict, deque
import heapq
import bisect

class SortingOptimizer:
    """Demonstrates sorting algorithm optimizations."""
    
    def bubble_sort_inefficient(self, arr: List[int]) -> List[int]:
        """O(n²) bubble sort - inefficient approach."""
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def merge_sort_efficient(self, arr: List[int]) -> List[int]:
        """O(n log n) merge sort - efficient approach."""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort_efficient(arr[:mid])
        right = self.merge_sort_efficient(arr[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Helper method to merge two sorted arrays."""
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


# Step 2: Add memoization for space-time tradeoffs
# ===============================================================================

# Explanation:
# Memoization trades space for time by caching results of expensive function calls.
# This is particularly effective for recursive algorithms with overlapping subproblems.

class MemoizationOptimizer:
    """Demonstrates memoization for performance optimization."""
    
    def fibonacci_inefficient(self, n: int) -> int:
        """O(2^n) fibonacci - inefficient recursive approach."""
        if n <= 1:
            return n
        return self.fibonacci_inefficient(n - 1) + self.fibonacci_inefficient(n - 2)
    
    @functools.lru_cache(maxsize=None)
    def fibonacci_memoized(self, n: int) -> int:
        """O(n) fibonacci with memoization - efficient approach."""
        if n <= 1:
            return n
        return self.fibonacci_memoized(n - 1) + self.fibonacci_memoized(n - 2)
    
    def fibonacci_iterative(self, n: int) -> int:
        """O(n) time, O(1) space fibonacci - most efficient approach."""
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Step 3: Implement efficient search algorithms
# ===============================================================================

# Explanation:
# Search algorithms can be optimized by choosing the right approach based on data structure.
# Binary search on sorted data is much more efficient than linear search.

class SearchOptimizer:
    """Demonstrates search algorithm optimizations."""
    
    def linear_search_inefficient(self, arr: List[int], target: int) -> int:
        """O(n) linear search - inefficient for sorted data."""
        for i, value in enumerate(arr):
            if value == target:
                return i
        return -1
    
    def binary_search_efficient(self, arr: List[int], target: int) -> int:
        """O(log n) binary search - efficient for sorted data."""
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
    
    def binary_search_builtin(self, arr: List[int], target: int) -> int:
        """Using Python's built-in bisect module - most efficient."""
        index = bisect.bisect_left(arr, target)
        if index < len(arr) and arr[index] == target:
            return index
        return -1


# Step 4: Optimize data structure selection
# ===============================================================================

# Explanation:
# Choosing the right data structure can dramatically improve performance.
# Different operations have different time complexities on different data structures.

class DataStructureOptimizer:
    """Demonstrates data structure optimization for different use cases."""
    
    def frequent_lookups_list_inefficient(self, items: List[str], lookups: List[str]) -> List[bool]:
        """O(n*m) using list for frequent lookups - inefficient."""
        results = []
        for lookup in lookups:
            results.append(lookup in items)
        return results
    
    def frequent_lookups_set_efficient(self, items: List[str], lookups: List[str]) -> List[bool]:
        """O(n+m) using set for frequent lookups - efficient."""
        item_set = set(items)  # O(n) conversion
        results = []
        for lookup in lookups:  # O(m) lookups, each O(1)
            results.append(lookup in item_set)
        return results
    
    def counting_elements_list_inefficient(self, items: List[str]) -> Dict[str, int]:
        """O(n²) counting with list operations - inefficient."""
        counts = {}
        for item in items:
            counts[item] = items.count(item)  # O(n) for each item
        return counts
    
    def counting_elements_dict_efficient(self, items: List[str]) -> Dict[str, int]:
        """O(n) counting with dictionary - efficient."""
        counts = defaultdict(int)
        for item in items:
            counts[item] += 1
        return dict(counts)
    
    def priority_queue_list_inefficient(self, tasks: List[Tuple[int, str]]) -> List[str]:
        """O(n²) priority queue with list - inefficient."""
        result = []
        remaining = tasks.copy()
        
        while remaining:
            # Find minimum priority (O(n))
            min_idx = 0
            for i, (priority, _) in enumerate(remaining):
                if priority < remaining[min_idx][0]:
                    min_idx = i
            
            # Remove and add to result (O(n) for removal)
            priority, task = remaining.pop(min_idx)
            result.append(task)
        
        return result
    
    def priority_queue_heap_efficient(self, tasks: List[Tuple[int, str]]) -> List[str]:
        """O(n log n) priority queue with heap - efficient."""
        heap = tasks.copy()
        heapq.heapify(heap)  # O(n)
        
        result = []
        while heap:
            priority, task = heapq.heappop(heap)  # O(log n)
            result.append(task)
        
        return result


# Step 5: Create comprehensive AlgorithmOptimizer and demonstrations
# ===============================================================================

# Explanation:
# Now we combine all optimization techniques into a comprehensive class
# and provide practical demonstrations with timing comparisons.

class AlgorithmOptimizer:
    """Main class combining all optimization techniques."""
    
    def __init__(self):
        self.sorting = SortingOptimizer()
        self.memoization = MemoizationOptimizer()
        self.search = SearchOptimizer()
        self.data_structures = DataStructureOptimizer()
    
    def benchmark_function(self, func, *args, **kwargs) -> Tuple[Any, float]:
        """Benchmark a function and return result with execution time."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    
    def compare_sorting_algorithms(self, data: List[int]) -> Dict[str, float]:
        """Compare sorting algorithm performance."""
        results = {}
        
        # Bubble sort (for small datasets only)
        if len(data) <= 1000:
            _, time_taken = self.benchmark_function(self.sorting.bubble_sort_inefficient, data)
            results['bubble_sort'] = time_taken
        
        # Merge sort
        _, time_taken = self.benchmark_function(self.sorting.merge_sort_efficient, data)
        results['merge_sort'] = time_taken
        
        # Built-in sort (Timsort)
        _, time_taken = self.benchmark_function(sorted, data)
        results['builtin_sort'] = time_taken
        
        return results
    
    def compare_fibonacci_algorithms(self, n: int) -> Dict[str, float]:
        """Compare fibonacci algorithm performance."""
        results = {}
        
        # Iterative (most efficient)
        _, time_taken = self.benchmark_function(self.memoization.fibonacci_iterative, n)
        results['iterative'] = time_taken
        
        # Memoized (efficient for repeated calls)
        _, time_taken = self.benchmark_function(self.memoization.fibonacci_memoized, n)
        results['memoized'] = time_taken
        
        # Naive recursive (only for small n)
        if n <= 35:
            _, time_taken = self.benchmark_function(self.memoization.fibonacci_inefficient, n)
            results['recursive'] = time_taken
        
        return results
    
    def compare_search_algorithms(self, data: List[int], target: int) -> Dict[str, float]:
        """Compare search algorithm performance."""
        results = {}
        sorted_data = sorted(data)
        
        # Linear search
        _, time_taken = self.benchmark_function(self.search.linear_search_inefficient, data, target)
        results['linear_search'] = time_taken
        
        # Binary search
        _, time_taken = self.benchmark_function(self.search.binary_search_efficient, sorted_data, target)
        results['binary_search'] = time_taken
        
        # Built-in binary search
        _, time_taken = self.benchmark_function(self.search.binary_search_builtin, sorted_data, target)
        results['builtin_binary_search'] = time_taken
        
        return results
    
    def demonstrate_optimizations(self):
        """Demonstrate all optimization techniques with examples."""
        print("=== Algorithm Optimization Demonstrations ===\n")
        
        # 1. Sorting optimization
        print("1. Sorting Algorithm Comparison:")
        test_data = list(range(1000, 0, -1))  # Reverse sorted data
        sorting_results = self.compare_sorting_algorithms(test_data)
        for algorithm, time_taken in sorting_results.items():
            print(f"   {algorithm}: {time_taken:.6f} seconds")
        print()
        
        # 2. Fibonacci optimization
        print("2. Fibonacci Algorithm Comparison (n=30):")
        fib_results = self.compare_fibonacci_algorithms(30)
        for algorithm, time_taken in fib_results.items():
            print(f"   {algorithm}: {time_taken:.6f} seconds")
        print()
        
        # 3. Search optimization
        print("3. Search Algorithm Comparison:")
        search_data = list(range(10000))
        target = 7500
        search_results = self.compare_search_algorithms(search_data, target)
        for algorithm, time_taken in search_results.items():
            print(f"   {algorithm}: {time_taken:.6f} seconds")
        print()
        
        # 4. Data structure optimization
        print("4. Data Structure Optimization Examples:")
        
        # Frequent lookups
        items = [f"item_{i}" for i in range(1000)]
        lookups = [f"item_{i}" for i in range(0, 1000, 10)]
        
        _, list_time = self.benchmark_function(
            self.data_structures.frequent_lookups_list_inefficient, items, lookups
        )
        _, set_time = self.benchmark_function(
            self.data_structures.frequent_lookups_set_efficient, items, lookups
        )
        
        print(f"   Frequent lookups - List: {list_time:.6f} seconds")
        print(f"   Frequent lookups - Set: {set_time:.6f} seconds")
        print(f"   Speedup: {list_time/set_time:.2f}x faster with set")
        print()
        
        # Element counting
        count_items = ["apple", "banana", "apple", "cherry", "banana", "apple"] * 100
        
        _, list_count_time = self.benchmark_function(
            self.data_structures.counting_elements_list_inefficient, count_items
        )
        _, dict_count_time = self.benchmark_function(
            self.data_structures.counting_elements_dict_efficient, count_items
        )
        
        print(f"   Element counting - List: {list_count_time:.6f} seconds")
        print(f"   Element counting - Dict: {dict_count_time:.6f} seconds")
        print(f"   Speedup: {list_count_time/dict_count_time:.2f}x faster with dict")


# ===============================================================================
#                           DEMONSTRATION AND TESTING
# ===============================================================================

def main():
    """Demonstrate algorithm optimization techniques."""
    optimizer = AlgorithmOptimizer()
    optimizer.demonstrate_optimizations()
    
    print("\n=== Key Optimization Principles ===")
    print("1. Choose the right algorithm for your data size and characteristics")
    print("2. Use appropriate data structures for your access patterns")
    print("3. Consider space-time tradeoffs (memoization, caching)")
    print("4. Leverage built-in optimized functions when available")
    print("5. Profile your code to identify actual bottlenecks")
    print("6. Optimize the most critical paths first")


if __name__ == "__main__":
    main()

