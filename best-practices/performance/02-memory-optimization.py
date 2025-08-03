"""Memory Optimization Best Practices in Python

This module demonstrates various techniques for optimizing memory usage in Python applications.
Learn how to reduce memory footprint, prevent memory leaks, and write memory-efficient code.

Topics covered:
1. Understanding memory usage patterns
2. Using __slots__ for memory-efficient classes
3. Generators vs lists for large datasets
4. Memory profiling and monitoring
5. Weak references to prevent circular references
6. Memory-efficient data structures
7. Object pooling and reuse
8. Garbage collection optimization

Requirements:
1. Demonstrate memory usage measurement
2. Show __slots__ optimization
3. Compare generators vs lists memory usage
4. Implement weak references
5. Show memory-efficient data structures
6. Demonstrate object pooling
7. Show garbage collection best practices

Example usage:
    # Memory-efficient class
    class Point:
        __slots__ = ['x', 'y']
    
    # Generator for large datasets
    def large_dataset():
        for i in range(1000000):
            yield i * 2
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read about memory optimization techniques
# - Think about when memory usage becomes critical
# - Start with simple examples
# - Test memory usage before and after optimization
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
# - How to measure memory usage in Python?
# - What is __slots__ and when should you use it?
# - When are generators more memory-efficient than lists?
# - How do weak references help prevent memory leaks?
# - What data structures use less memory?
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


# Step 1: Import modules and create memory measurement utilities
# ===============================================================================

# Explanation:
# Before optimizing memory, we need to measure it. We'll create utilities
# to track memory usage and compare different approaches.

import sys
import gc
import weakref
from typing import List, Generator, Optional, Any
from collections import deque
import tracemalloc

class MemoryProfiler:
    """Utility class for measuring memory usage."""
    
    def __init__(self):
        self.start_memory = 0
        self.peak_memory = 0
    
    def start_profiling(self):
        """Start memory profiling."""
        tracemalloc.start()
        gc.collect()  # Clean up before measuring
        self.start_memory = tracemalloc.get_traced_memory()[0]
        return self
    
    def get_current_usage(self) -> tuple:
        """Get current memory usage in bytes."""
        if tracemalloc.is_tracing():
            current, peak = tracemalloc.get_traced_memory()
            return current, peak
        return 0, 0
    
    def stop_profiling(self) -> dict:
        """Stop profiling and return memory statistics."""
        if tracemalloc.is_tracing():
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return {
                'start_memory': self.start_memory,
                'final_memory': current,
                'peak_memory': peak,
                'memory_used': current - self.start_memory,
                'peak_usage': peak - self.start_memory
            }
        return {}

def get_object_size(obj) -> int:
    """Get the size of an object in bytes."""
    return sys.getsizeof(obj)

def format_bytes(bytes_value: int) -> str:
    """Format bytes into human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} TB"

# Example usage of memory profiling
def demonstrate_memory_profiling():
    """Demonstrate how to use memory profiling utilities."""
    print("=== Memory Profiling Demo ===")
    
    profiler = MemoryProfiler()
    profiler.start_profiling()
    
    # Create some objects to measure
    large_list = [i for i in range(100000)]
    
    stats = profiler.stop_profiling()
    print(f"Memory used: {format_bytes(stats['memory_used'])}")
    print(f"Peak memory: {format_bytes(stats['peak_usage'])}")
    print(f"List size: {format_bytes(get_object_size(large_list))}")


# Step 2: Using __slots__ for memory-efficient classes
# ===============================================================================

# Explanation:
# By default, Python stores instance attributes in a dictionary (__dict__).
# __slots__ allows us to explicitly declare which attributes a class will have,
# eliminating the __dict__ and reducing memory usage significantly.

# Previous code from Step 1:
# (All imports and MemoryProfiler class from above)

class RegularPoint:
    """Regular class without __slots__ - uses more memory."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

class OptimizedPoint:
    """Memory-optimized class using __slots__."""
    __slots__ = ['x', 'y']  # Only these attributes allowed
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

class ComplexRegularClass:
    """Regular class with many attributes."""
    
    def __init__(self):
        self.attr1 = "value1"
        self.attr2 = "value2"
        self.attr3 = 123
        self.attr4 = [1, 2, 3]
        self.attr5 = {"key": "value"}

class ComplexOptimizedClass:
    """Optimized class with __slots__."""
    __slots__ = ['attr1', 'attr2', 'attr3', 'attr4', 'attr5']
    
    def __init__(self):
        self.attr1 = "value1"
        self.attr2 = "value2"
        self.attr3 = 123
        self.attr4 = [1, 2, 3]
        self.attr5 = {"key": "value"}

def compare_slots_memory_usage():
    """Compare memory usage between regular and __slots__ classes."""
    print("\n=== __slots__ Memory Comparison ===")
    
    # Test simple classes
    regular_point = RegularPoint(1.0, 2.0)
    optimized_point = OptimizedPoint(1.0, 2.0)
    
    print(f"Regular Point size: {format_bytes(get_object_size(regular_point))}")
    print(f"Optimized Point size: {format_bytes(get_object_size(optimized_point))}")
    
    # Test with many instances
    profiler = MemoryProfiler()
    
    # Regular classes
    profiler.start_profiling()
    regular_points = [RegularPoint(i, i+1) for i in range(100000)]
    regular_stats = profiler.stop_profiling()
    
    # Optimized classes
    profiler.start_profiling()
    optimized_points = [OptimizedPoint(i, i+1) for i in range(100000)]
    optimized_stats = profiler.stop_profiling()
    
    print(f"\n100,000 Regular Points: {format_bytes(regular_stats['memory_used'])}")
    print(f"100,000 Optimized Points: {format_bytes(optimized_stats['memory_used'])}")
    
    memory_saved = regular_stats['memory_used'] - optimized_stats['memory_used']
    savings_percent = (memory_saved / regular_stats['memory_used']) * 100
    print(f"Memory saved: {format_bytes(memory_saved)} ({savings_percent:.1f}%)")

def demonstrate_slots_limitations():
    """Show limitations and considerations when using __slots__."""
    print("\n=== __slots__ Limitations Demo ===")
    
    # Cannot add new attributes dynamically
    regular = RegularPoint(1, 2)
    optimized = OptimizedPoint(1, 2)
    
    # This works with regular class
    regular.new_attr = "dynamic"
    print(f"Regular class - added dynamic attribute: {regular.new_attr}")
    
    # This would raise AttributeError with __slots__ class
    try:
        optimized.new_attr = "dynamic"
    except AttributeError as e:
        print(f"Optimized class error: {e}")
    
    # __slots__ classes don't have __dict__ by default
    print(f"Regular class has __dict__: {hasattr(regular, '__dict__')}")
    print(f"Optimized class has __dict__: {hasattr(optimized, '__dict__')}")


# Step 3: Generators vs Lists for memory efficiency
# ===============================================================================

# Explanation:
# Generators are memory-efficient because they produce items on-demand rather
# than storing all items in memory at once. This is crucial for large datasets.

# Previous code from Steps 1-2:
# (All imports, MemoryProfiler, and __slots__ classes from above)

def create_large_list(size: int) -> List[int]:
    """Create a large list - stores all items in memory."""
    return [i * 2 for i in range(size)]

def create_large_generator(size: int) -> Generator[int, None, None]:
    """Create a generator - produces items on demand."""
    for i in range(size):
        yield i * 2

def fibonacci_list(n: int) -> List[int]:
    """Generate Fibonacci sequence as a list."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence as a generator."""
    if n <= 0:
        return
    
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def process_data_with_list(data_size: int) -> int:
    """Process data using list comprehension."""
    # Creates entire list in memory first
    numbers = [i for i in range(data_size)]
    squared = [x * x for x in numbers]
    filtered = [x for x in squared if x % 2 == 0]
    return sum(filtered)

def process_data_with_generator(data_size: int) -> int:
    """Process data using generator expressions."""
    # Processes items one at a time
    numbers = (i for i in range(data_size))
    squared = (x * x for x in numbers)
    filtered = (x for x in squared if x % 2 == 0)
    return sum(filtered)

def compare_list_vs_generator_memory():
    """Compare memory usage between lists and generators."""
    print("\n=== Lists vs Generators Memory Comparison ===")
    
    size = 1000000
    
    # Test list creation
    profiler = MemoryProfiler()
    profiler.start_profiling()
    large_list = create_large_list(size)
    list_stats = profiler.stop_profiling()
    
    # Test generator creation
    profiler.start_profiling()
    large_generator = create_large_generator(size)
    generator_stats = profiler.stop_profiling()
    
    print(f"List with {size:,} items: {format_bytes(list_stats['memory_used'])}")
    print(f"Generator object: {format_bytes(generator_stats['memory_used'])}")
    print(f"Generator object size: {format_bytes(get_object_size(large_generator))}")
    
    # Compare processing approaches
    profiler.start_profiling()
    list_result = process_data_with_list(100000)
    list_process_stats = profiler.stop_profiling()
    
    profiler.start_profiling()
    generator_result = process_data_with_generator(100000)
    generator_process_stats = profiler.stop_profiling()
    
    print(f"\nProcessing with lists: {format_bytes(list_process_stats['memory_used'])}")
    print(f"Processing with generators: {format_bytes(generator_process_stats['memory_used'])}")
    print(f"Results are equal: {list_result == generator_result}")

def demonstrate_generator_benefits():
    """Show practical benefits of generators."""
    print("\n=== Generator Benefits Demo ===")
    
    # Memory usage for Fibonacci sequences
    n = 10000
    
    profiler = MemoryProfiler()
    profiler.start_profiling()
    fib_list = fibonacci_list(n)
    list_stats = profiler.stop_profiling()
    
    profiler.start_profiling()
    fib_gen = fibonacci_generator(n)
    # Convert to list to consume the generator for fair comparison
    fib_from_gen = list(fib_gen)
    gen_stats = profiler.stop_profiling()
    
    print(f"Fibonacci list ({n} items): {format_bytes(list_stats['memory_used'])}")
    print(f"Fibonacci from generator: {format_bytes(gen_stats['memory_used'])}")
    
    # Show that generator can be used for infinite sequences
    def infinite_counter():
        """Generator for infinite sequence."""
        count = 0
        while True:
            yield count
            count += 1
    
    counter = infinite_counter()
    print(f"\nInfinite generator first 5 values: {[next(counter) for _ in range(5)]}")
    print(f"Generator size: {format_bytes(get_object_size(counter))}")

class DataProcessor:
    """Class demonstrating memory-efficient data processing."""
    
    def __init__(self):
        self.processed_count = 0
    
    def process_large_file_inefficient(self, filename: str) -> List[str]:
        """Inefficient: loads entire file into memory."""
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()  # Loads all lines into memory
                processed = []
                for line in lines:
                    if line.strip():  # Process non-empty lines
                        processed.append(line.upper().strip())
                        self.processed_count += 1
                return processed
        except FileNotFoundError:
            return []
    
    def process_large_file_efficient(self, filename: str) -> Generator[str, None, None]:
        """Efficient: processes file line by line."""
        try:
            with open(filename, 'r') as file:
                for line in file:  # Generator - one line at a time
                    if line.strip():  # Process non-empty lines
                        self.processed_count += 1
                        yield line.upper().strip()
        except FileNotFoundError:
            return


# Step 4: Weak references to prevent circular references and memory leaks
# ===============================================================================

# Explanation:
# Weak references allow you to refer to an object without preventing it from
# being garbage collected. This is crucial for breaking circular references
# and preventing memory leaks.

# Previous code from Steps 1-3:
# (All imports, MemoryProfiler, __slots__ classes, and generator functions from above)

class Parent:
    """Parent class that can create circular references."""
    
    def __init__(self, name: str):
        self.name = name
        self.children = []
        self._observers = []  # Regular references
        self._weak_observers = []  # Weak references
    
    def add_child(self, child):
        """Add a child - creates potential circular reference."""
        self.children.append(child)
        child.parent = self  # Circular reference!
    
    def add_observer(self, observer):
        """Add observer with strong reference."""
        self._observers.append(observer)
    
    def add_weak_observer(self, observer):
        """Add observer with weak reference."""
        self._weak_observers.append(weakref.ref(observer))
    
    def notify_observers(self, message: str):
        """Notify all observers."""
        # Strong references
        for observer in self._observers:
            observer.notify(message)
        
        # Weak references - need to check if still alive
        for weak_ref in self._weak_observers[:]:  # Copy list to avoid modification during iteration
            observer = weak_ref()  # Get the actual object
            if observer is not None:
                observer.notify(message)
            else:
                # Remove dead weak references
                self._weak_observers.remove(weak_ref)

class Child:
    """Child class that references parent."""
    
    def __init__(self, name: str):
        self.name = name
        self.parent = None  # Will be set by parent.add_child()
    
    def get_family_info(self) -> str:
        if self.parent:
            return f"{self.name} is child of {self.parent.name}"
        return f"{self.name} has no parent"

class Observer:
    """Observer class for demonstration."""
    
    def __init__(self, name: str):
        self.name = name
    
    def notify(self, message: str):
        print(f"Observer {self.name} received: {message}")

class WeakParent:
    """Parent class using weak references to prevent circular references."""
    
    def __init__(self, name: str):
        self.name = name
        self.children = []
    
    def add_child(self, child):
        """Add child with weak reference to parent."""
        self.children.append(child)
        child.parent_ref = weakref.ref(self)  # Weak reference!
    
    def get_info(self) -> str:
        return f"Parent {self.name} has {len(self.children)} children"

class WeakChild:
    """Child class using weak reference to parent."""
    
    def __init__(self, name: str):
        self.name = name
        self.parent_ref = None  # Will hold weak reference
    
    def get_parent(self):
        """Get parent object if still alive."""
        if self.parent_ref:
            return self.parent_ref()  # Returns None if parent was garbage collected
        return None
    
    def get_family_info(self) -> str:
        parent = self.get_parent()
        if parent:
            return f"{self.name} is child of {parent.name}"
        return f"{self.name}'s parent was garbage collected"

def demonstrate_circular_reference_problem():
    """Show how circular references can cause memory issues."""
    print("\n=== Circular Reference Problem Demo ===")
    
    profiler = MemoryProfiler()
    profiler.start_profiling()
    
    # Create circular references
    families = []
    for i in range(1000):
        parent = Parent(f"Parent{i}")
        child1 = Child(f"Child{i}A")
        child2 = Child(f"Child{i}B")
        
        parent.add_child(child1)
        parent.add_child(child2)
        
        families.append((parent, child1, child2))
    
    stats_with_circular = profiler.stop_profiling()
    
    # Clear references
    del families
    gc.collect()  # Force garbage collection
    
    print(f"Memory used with circular references: {format_bytes(stats_with_circular['memory_used'])}")

def demonstrate_weak_reference_solution():
    """Show how weak references solve circular reference problems."""
    print("\n=== Weak Reference Solution Demo ===")
    
    profiler = MemoryProfiler()
    profiler.start_profiling()
    
    # Create families with weak references
    families = []
    for i in range(1000):
        parent = WeakParent(f"Parent{i}")
        child1 = WeakChild(f"Child{i}A")
        child2 = WeakChild(f"Child{i}B")
        
        parent.add_child(child1)
        parent.add_child(child2)
        
        families.append((parent, child1, child2))
    
    stats_with_weak = profiler.stop_profiling()
    
    # Test that weak references work
    parent, child1, child2 = families[0]
    print(f"Before deletion: {child1.get_family_info()}")
    
    # Delete parent
    del parent
    gc.collect()
    
    print(f"After parent deletion: {child1.get_family_info()}")
    print(f"Memory used with weak references: {format_bytes(stats_with_weak['memory_used'])}")

class CacheWithWeakRefs:
    """Cache implementation using weak references."""
    
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
        self._access_count = {}
    
    def get(self, key: str, factory_func=None):
        """Get item from cache or create it."""
        obj = self._cache.get(key)
        if obj is not None:
            self._access_count[key] = self._access_count.get(key, 0) + 1
            return obj
        
        if factory_func:
            obj = factory_func()
            self._cache[key] = obj
            self._access_count[key] = 1
            return obj
        
        return None
    
    def size(self) -> int:
        """Get current cache size."""
        return len(self._cache)
    
    def cleanup(self):
        """Clean up access counts for dead objects."""
        live_keys = set(self._cache.keys())
        dead_keys = set(self._access_count.keys()) - live_keys
        for key in dead_keys:
            del self._access_count[key]

class ExpensiveObject:
    """Simulate an expensive-to-create object."""
    
    def __init__(self, data: str):
        self.data = data
        self.creation_time = id(self)  # Simulate expensive computation
    
    def __repr__(self):
        return f"ExpensiveObject({self.data})"

def demonstrate_weak_cache():
    """Demonstrate cache with weak references."""
    print("\n=== Weak Reference Cache Demo ===")
    
    cache = CacheWithWeakRefs()
    
    # Create objects through cache
    obj1 = cache.get("key1", lambda: ExpensiveObject("data1"))
    obj2 = cache.get("key2", lambda: ExpensiveObject("data2"))
    obj3 = cache.get("key1")  # Should return same object
    
    print(f"obj1 is obj3: {obj1 is obj3}")
    print(f"Cache size: {cache.size()}")
    
    # Delete references
    del obj1, obj3
    gc.collect()
    
    print(f"Cache size after deletion: {cache.size()}")
    
    # Try to get deleted object
    obj4 = cache.get("key1")
    print(f"Getting deleted object: {obj4}")
    
    # Create new object with same key
    obj5 = cache.get("key1", lambda: ExpensiveObject("new_data1"))
    print(f"New object: {obj5}")


# Step 5: Memory-efficient data structures
# ===============================================================================

# Explanation:
# Choosing the right data structure can significantly impact memory usage.
# Some structures are more memory-efficient than others for specific use cases.

# Previous code from Steps 1-4:
# (All imports, MemoryProfiler, __slots__ classes, generators, and weak references from above)

import array
from collections import namedtuple, defaultdict

def compare_data_structure_memory():
    """Compare memory usage of different data structures."""
    print("\n=== Data Structure Memory Comparison ===")
    
    size = 100000
    
    # Lists vs Arrays for numeric data
    profiler = MemoryProfiler()
    
    # Regular list
    profiler.start_profiling()
    number_list = [i for i in range(size)]
    list_stats = profiler.stop_profiling()
    
    # Array (more memory efficient for numbers)
    profiler.start_profiling()
    number_array = array.array('i', range(size))  # 'i' for integers
    array_stats = profiler.stop_profiling()
    
    print(f"List of {size:,} integers: {format_bytes(list_stats['memory_used'])}")
    print(f"Array of {size:,} integers: {format_bytes(array_stats['memory_used'])}")
    
    list_size = get_object_size(number_list)
    array_size = get_object_size(number_array)
    print(f"List object size: {format_bytes(list_size)}")
    print(f"Array object size: {format_bytes(array_size)}")
    
    savings = ((list_size - array_size) / list_size) * 100
    print(f"Array saves: {savings:.1f}% memory")

# Named tuples vs regular classes
class RegularCoordinate:
    """Regular class for coordinates."""
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

# Named tuple (more memory efficient)
Coordinate = namedtuple('Coordinate', ['x', 'y', 'z'])

# Coordinate with __slots__
class SlottedCoordinate:
    """Coordinate class with __slots__."""
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

def compare_coordinate_structures():
    """Compare different ways to store coordinates."""
    print("\n=== Coordinate Structure Comparison ===")
    
    size = 50000
    profiler = MemoryProfiler()
    
    # Regular class
    profiler.start_profiling()
    regular_coords = [RegularCoordinate(i, i+1, i+2) for i in range(size)]
    regular_stats = profiler.stop_profiling()
    
    # Named tuple
    profiler.start_profiling()
    named_coords = [Coordinate(i, i+1, i+2) for i in range(size)]
    named_stats = profiler.stop_profiling()
    
    # Slotted class
    profiler.start_profiling()
    slotted_coords = [SlottedCoordinate(i, i+1, i+2) for i in range(size)]
    slotted_stats = profiler.stop_profiling()
    
    print(f"Regular class coordinates: {format_bytes(regular_stats['memory_used'])}")
    print(f"Named tuple coordinates: {format_bytes(named_stats['memory_used'])}")
    print(f"Slotted class coordinates: {format_bytes(slotted_stats['memory_used'])}")
    
    # Single object comparison
    regular_coord = RegularCoordinate(1, 2, 3)
    named_coord = Coordinate(1, 2, 3)
    slotted_coord = SlottedCoordinate(1, 2, 3)
    
    print(f"\nSingle object sizes:")
    print(f"Regular: {format_bytes(get_object_size(regular_coord))}")
    print(f"Named tuple: {format_bytes(get_object_size(named_coord))}")
    print(f"Slotted: {format_bytes(get_object_size(slotted_coord))}")

def demonstrate_efficient_collections():
    """Show memory-efficient collection patterns."""
    print("\n=== Efficient Collections Demo ===")
    
    # Using deque for efficient append/pop operations
    from collections import deque
    
    # Compare list vs deque for queue operations
    profiler = MemoryProfiler()
    
    # List as queue (inefficient)
    profiler.start_profiling()
    list_queue = []
    for i in range(100000):
        list_queue.append(i)
        if len(list_queue) > 1000:
            list_queue.pop(0)  # Expensive operation for lists
    list_queue_stats = profiler.stop_profiling()
    
    # Deque as queue (efficient)
    profiler.start_profiling()
    deque_queue = deque(maxlen=1000)  # Automatically limits size
    for i in range(100000):
        deque_queue.append(i)  # Automatically removes from left when full
    deque_queue_stats = profiler.stop_profiling()
    
    print(f"List as queue: {format_bytes(list_queue_stats['memory_used'])}")
    print(f"Deque as queue: {format_bytes(deque_queue_stats['memory_used'])}")

class MemoryEfficientCounter:
    """Memory-efficient counter using __slots__ and defaultdict."""
    __slots__ = ['_counts']
    
    def __init__(self):
        self._counts = defaultdict(int)
    
    def increment(self, key: str):
        self._counts[key] += 1
    
    def get_count(self, key: str) -> int:
        return self._counts[key]
    
    def get_size(self) -> int:
        return len(self._counts)

class RegularCounter:
    """Regular counter for comparison."""
    
    def __init__(self):
        self._counts = {}
    
    def increment(self, key: str):
        if key in self._counts:
            self._counts[key] += 1
        else:
            self._counts[key] = 1
    
    def get_count(self, key: str) -> int:
        return self._counts.get(key, 0)
    
    def get_size(self) -> int:
        return len(self._counts)

def compare_counter_implementations():
    """Compare different counter implementations."""
    print("\n=== Counter Implementation Comparison ===")
    
    keys = [f"key_{i % 1000}" for i in range(100000)]  # Reuse keys
    
    profiler = MemoryProfiler()
    
    # Regular counter
    profiler.start_profiling()
    regular_counter = RegularCounter()
    for key in keys:
        regular_counter.increment(key)
    regular_stats = profiler.stop_profiling()
    
    # Efficient counter
    profiler.start_profiling()
    efficient_counter = MemoryEfficientCounter()
    for key in keys:
        efficient_counter.increment(key)
    efficient_stats = profiler.stop_profiling()
    
    print(f"Regular counter: {format_bytes(regular_stats['memory_used'])}")
    print(f"Efficient counter: {format_bytes(efficient_stats['memory_used'])}")
    print(f"Both have {regular_counter.get_size()} unique keys")

def demonstrate_string_interning():
    """Show how string interning can save memory."""
    print("\n=== String Interning Demo ===")
    
    # Without interning
    profiler = MemoryProfiler()
    profiler.start_profiling()
    
    strings_without_interning = []
    for i in range(10000):
        # Create many copies of the same strings
        strings_without_interning.extend([
            f"common_string_{i % 100}",
            f"another_string_{i % 50}",
            f"third_string_{i % 25}"
        ])
    
    without_interning_stats = profiler.stop_profiling()
    
    # With interning
    profiler.start_profiling()
    
    # Use a cache to simulate interning
    string_cache = {}
    strings_with_interning = []
    
    for i in range(10000):
        for pattern in [f"common_string_{i % 100}", f"another_string_{i % 50}", f"third_string_{i % 25}"]:
            if pattern not in string_cache:
                string_cache[pattern] = pattern
            strings_with_interning.append(string_cache[pattern])
    
    with_interning_stats = profiler.stop_profiling()
    
    print(f"Without interning: {format_bytes(without_interning_stats['memory_used'])}")
    print(f"With interning: {format_bytes(with_interning_stats['memory_used'])}")
    print(f"Unique strings cached: {len(string_cache)}")
    
    memory_saved = without_interning_stats['memory_used'] - with_interning_stats['memory_used']
    savings_percent = (memory_saved / without_interning_stats['memory_used']) * 100
    print(f"Memory saved: {format_bytes(memory_saved)} ({savings_percent:.1f}%)")


# Step 6: Object pooling and reuse
# ===============================================================================

# Explanation:
# Object pooling reuses objects instead of creating new ones, reducing
# memory allocation overhead and garbage collection pressure.

# Previous code from Steps 1-5:
# (All imports, MemoryProfiler, __slots__ classes, generators, weak references, and data structures from above)

from threading import Lock
from queue import Queue
import time

class ExpensiveResource:
    """Simulate an expensive-to-create resource."""
    
    def __init__(self, resource_id: int):
        self.resource_id = resource_id
        self.created_at = time.time()
        self.usage_count = 0
        # Simulate expensive initialization
        self._data = [i for i in range(1000)]  # Some expensive data
    
    def use(self):
        """Use the resource."""
        self.usage_count += 1
        return f"Using resource {self.resource_id} (used {self.usage_count} times)"
    
    def reset(self):
        """Reset resource for reuse."""
        self.usage_count = 0
        # Reset any state that needs to be clean for reuse

class ObjectPool:
    """Generic object pool implementation."""
    
    def __init__(self, factory_func, max_size: int = 10):
        self._factory_func = factory_func
        self._max_size = max_size
        self._pool = Queue(maxsize=max_size)
        self._created_count = 0
        self._lock = Lock()
    
    def acquire(self):
        """Get an object from the pool."""
        try:
            # Try to get from pool first
            obj = self._pool.get_nowait()
            return obj
        except:
            # Pool is empty, create new object
            with self._lock:
                if self._created_count < self._max_size:
                    obj = self._factory_func(self._created_count)
                    self._created_count += 1
                    return obj
                else:
                    # Wait for an object to be returned
                    return self._pool.get()
    
    def release(self, obj):
        """Return an object to the pool."""
        obj.reset()  # Reset object state
        try:
            self._pool.put_nowait(obj)
        except:
            # Pool is full, object will be garbage collected
            pass
    
    def size(self) -> int:
        """Get current pool size."""
        return self._pool.qsize()
    
    def total_created(self) -> int:
        """Get total number of objects created."""
        return self._created_count

def compare_with_without_pooling():
    """Compare memory usage with and without object pooling."""
    print("\n=== Object Pooling Comparison ===")
    
    iterations = 10000
    
    # Without pooling - create new objects each time
    profiler = MemoryProfiler()
    profiler.start_profiling()
    
    results_without_pool = []
    for i in range(iterations):
        resource = ExpensiveResource(i)
        result = resource.use()
        results_without_pool.append(result)
        # Object goes out of scope and becomes eligible for GC
    
    without_pool_stats = profiler.stop_profiling()
    
    # With pooling - reuse objects
    profiler.start_profiling()
    
    pool = ObjectPool(lambda id: ExpensiveResource(id), max_size=100)
    results_with_pool = []
    
    for i in range(iterations):
        resource = pool.acquire()
        result = resource.use()
        results_with_pool.append(result)
        pool.release(resource)
    
    with_pool_stats = profiler.stop_profiling()
    
    print(f"Without pooling: {format_bytes(without_pool_stats['memory_used'])}")
    print(f"With pooling: {format_bytes(with_pool_stats['memory_used'])}")
    print(f"Objects created without pooling: {iterations}")
    print(f"Objects created with pooling: {pool.total_created()}")
    
    memory_saved = without_pool_stats['memory_used'] - with_pool_stats['memory_used']
    if without_pool_stats['memory_used'] > 0:
        savings_percent = (memory_saved / without_pool_stats['memory_used']) * 100
        print(f"Memory saved: {format_bytes(memory_saved)} ({savings_percent:.1f}%)")

class ConnectionPool:
    """Example of a database connection pool."""
    
    def __init__(self, max_connections: int = 5):
        self._max_connections = max_connections
        self._available = Queue(maxsize=max_connections)
        self._in_use = set()
        self._created_count = 0
        self._lock = Lock()
    
    def get_connection(self):
        """Get a database connection."""
        try:
            conn = self._available.get_nowait()
            self._in_use.add(conn)
            return conn
        except:
            with self._lock:
                if self._created_count < self._max_connections:
                    conn = self._create_connection()
                    self._created_count += 1
                    self._in_use.add(conn)
                    return conn
                else:
                    # Wait for a connection to be released
                    conn = self._available.get()
                    self._in_use.add(conn)
                    return conn
    
    def release_connection(self, conn):
        """Release a connection back to the pool."""
        if conn in self._in_use:
            self._in_use.remove(conn)
            self._available.put(conn)
    
    def _create_connection(self):
        """Create a new database connection (simulated)."""
        return f"Connection_{self._created_count}"
    
    def stats(self) -> dict:
        """Get pool statistics."""
        return {
            'total_created': self._created_count,
            'available': self._available.qsize(),
            'in_use': len(self._in_use)
        }


# Step 7: Garbage collection optimization
# ===============================================================================

# Explanation:
# Understanding and optimizing garbage collection can significantly improve
# memory usage patterns and application performance.

# Previous code from Steps 1-6:
# (All imports, MemoryProfiler, __slots__ classes, generators, weak references, data structures, and object pooling from above)

def demonstrate_gc_optimization():
    """Demonstrate garbage collection optimization techniques."""
    print("\n=== Garbage Collection Optimization ===")
    
    # Show current GC settings
    print(f"GC thresholds: {gc.get_threshold()}")
    print(f"GC counts: {gc.get_count()}")
    
    # Create objects that will trigger GC
    profiler = MemoryProfiler()
    profiler.start_profiling()
    
    # Create many objects to trigger garbage collection
    objects = []
    for i in range(100000):
        obj = {'id': i, 'data': [j for j in range(10)]}
        objects.append(obj)
        
        # Periodically remove references to create garbage
        if i % 1000 == 0:
            objects = objects[-500:]  # Keep only last 500 objects
    
    before_gc_stats = profiler.get_current_usage()
    
    # Force garbage collection
    collected = gc.collect()
    
    after_gc_stats = profiler.get_current_usage()
    final_stats = profiler.stop_profiling()
    
    print(f"Objects collected by GC: {collected}")
    print(f"Memory before GC: {format_bytes(before_gc_stats[0])}")
    print(f"Memory after GC: {format_bytes(after_gc_stats[0])}")
    print(f"Memory freed: {format_bytes(before_gc_stats[0] - after_gc_stats[0])}")

def demonstrate_gc_generations():
    """Show how GC generations work."""
    print("\n=== GC Generations Demo ===")
    
    # Show initial GC stats
    print("Initial GC stats:")
    for i, count in enumerate(gc.get_count()):
        print(f"  Generation {i}: {count} objects")
    
    # Create short-lived objects (generation 0)
    short_lived = []
    for i in range(10000):
        short_lived.append([i, i*2, i*3])
    
    print("\nAfter creating short-lived objects:")
    for i, count in enumerate(gc.get_count()):
        print(f"  Generation {i}: {count} objects")
    
    # Create long-lived objects
    long_lived = []
    for i in range(1000):
        long_lived.append({'id': i, 'persistent': True})
    
    # Force a collection to move objects to higher generations
    gc.collect()
    
    print("\nAfter GC collection:")
    for i, count in enumerate(gc.get_count()):
        print(f"  Generation {i}: {count} objects")
    
    # Clear short-lived objects
    del short_lived
    gc.collect()
    
    print("\nAfter clearing short-lived objects:")
    for i, count in enumerate(gc.get_count()):
        print(f"  Generation {i}: {count} objects")

class GCOptimizedClass:
    """Class designed to minimize GC pressure."""
    __slots__ = ['_data', '_cache']
    
    def __init__(self):
        self._data = {}
        self._cache = None
    
    def add_data(self, key: str, value: Any):
        """Add data without creating unnecessary references."""
        self._data[key] = value
        self._cache = None  # Invalidate cache
    
    def get_processed_data(self):
        """Get processed data with caching to avoid recreating objects."""
        if self._cache is None:
            # Process data once and cache result
            self._cache = {k: v * 2 if isinstance(v, (int, float)) else v 
                          for k, v in self._data.items()}
        return self._cache
    
    def clear_cache(self):
        """Manually clear cache to help GC."""
        self._cache = None

def demonstrate_gc_friendly_patterns():
    """Show GC-friendly programming patterns."""
    print("\n=== GC-Friendly Patterns Demo ===")
    
    profiler = MemoryProfiler()
    
    # Pattern 1: Avoid creating unnecessary intermediate objects
    profiler.start_profiling()
    
    # Bad: creates many intermediate lists
    result_bad = []
    for i in range(10000):
        temp_list = [j for j in range(10)]
        processed = [x * 2 for x in temp_list]
        filtered = [x for x in processed if x % 4 == 0]
        result_bad.extend(filtered)
    
    bad_stats = profiler.stop_profiling()
    
    # Good: use generators to avoid intermediate objects
    profiler.start_profiling()
    
    def process_efficiently(n):
        for i in range(n):
            for j in range(10):
                processed = j * 2
                if processed % 4 == 0:
                    yield processed
    
    result_good = list(process_efficiently(10000))
    
    good_stats = profiler.stop_profiling()
    
    print(f"Memory with intermediate objects: {format_bytes(bad_stats['memory_used'])}")
    print(f"Memory with generators: {format_bytes(good_stats['memory_used'])}")
    print(f"Results are equal: {len(result_bad) == len(result_good)}")
    
    # Pattern 2: Manual cleanup for large objects
    large_data = [i for i in range(1000000)]
    print(f"Large data size: {format_bytes(get_object_size(large_data))}")
    
    # Process data
    processed_count = len([x for x in large_data if x % 2 == 0])
    
    # Manual cleanup
    del large_data
    gc.collect()
    
    print(f"Processed {processed_count} even numbers")
    print("Large data manually cleaned up")


# Step 8: Comprehensive memory optimization demonstration
# ===============================================================================

# Explanation:
# This final step combines all the techniques we've learned to create a
# comprehensive memory optimization example that demonstrates real-world usage.

# Previous code from Steps 1-7:
# (All imports, MemoryProfiler, __slots__ classes, generators, weak references, 
#  data structures, object pooling, and GC optimization from above)

class MemoryOptimizedDataProcessor:
    """A comprehensive example combining all memory optimization techniques."""
    __slots__ = ['_data_cache', '_object_pool', '_weak_observers', '_stats']
    
    def __init__(self, pool_size: int = 50):
        self._data_cache = weakref.WeakValueDictionary()
        self._object_pool = ObjectPool(
            lambda id: ExpensiveResource(id), 
            max_size=pool_size
        )
        self._weak_observers = []
        self._stats = defaultdict(int)
    
    def process_large_dataset_efficiently(self, data_size: int) -> Generator[dict, None, None]:
        """Process large dataset using memory-efficient techniques."""
        # Use generator to avoid loading all data into memory
        for i in range(data_size):
            # Use object pool for expensive resources
            resource = self._object_pool.acquire()
            
            try:
                # Process data efficiently
                if i % 2 == 0:  # Only process even numbers
                    result = {
                        'id': i,
                        'processed_value': i * 2,
                        'resource_id': resource.resource_id
                    }
                    self._stats['processed'] += 1
                    yield result
                else:
                    self._stats['skipped'] += 1
            finally:
                # Always return resource to pool
                self._object_pool.release(resource)
    
    def cache_expensive_computation(self, key: str, compute_func):
        """Cache expensive computations with weak references."""
        result = self._data_cache.get(key)
        if result is None:
            result = compute_func()
            self._data_cache[key] = result
            self._stats['cache_miss'] += 1
        else:
            self._stats['cache_hit'] += 1
        return result
    
    def add_observer(self, observer):
        """Add observer with weak reference to prevent memory leaks."""
        self._weak_observers.append(weakref.ref(observer))
    
    def notify_observers(self, message: str):
        """Notify observers, cleaning up dead references."""
        live_observers = []
        for weak_ref in self._weak_observers:
            observer = weak_ref()
            if observer is not None:
                observer.notify(message)
                live_observers.append(weak_ref)
        self._weak_observers = live_observers
    
    def get_stats(self) -> dict:
        """Get processing statistics."""
        return dict(self._stats)
    
    def cleanup(self):
        """Manual cleanup to help garbage collection."""
        self._data_cache.clear()
        self._stats.clear()
        gc.collect()

class MemoryEfficientObserver:
    """Observer using __slots__ for memory efficiency."""
    __slots__ = ['name', 'notification_count']
    
    def __init__(self, name: str):
        self.name = name
        self.notification_count = 0
    
    def notify(self, message: str):
        self.notification_count += 1

def comprehensive_memory_optimization_demo():
    """Demonstrate all memory optimization techniques together."""
    print("\n" + "="*60)
    print("COMPREHENSIVE MEMORY OPTIMIZATION DEMONSTRATION")
    print("="*60)
    
    profiler = MemoryProfiler()
    profiler.start_profiling()
    
    # Create memory-optimized processor
    processor = MemoryOptimizedDataProcessor(pool_size=20)
    
    # Add observers
    observers = [MemoryEfficientObserver(f"Observer_{i}") for i in range(5)]
    for observer in observers:
        processor.add_observer(observer)
    
    # Process large dataset efficiently
    print("Processing large dataset with memory optimization...")
    processed_data = []
    
    for result in processor.process_large_dataset_efficiently(50000):
        processed_data.append(result)
        
        # Periodically notify observers and cache computations
        if len(processed_data) % 10000 == 0:
            processor.notify_observers(f"Processed {len(processed_data)} items")
            
            # Use cache for expensive computations
            cache_key = f"computation_{len(processed_data)}"
            cached_result = processor.cache_expensive_computation(
                cache_key,
                lambda: sum(range(1000))  # Expensive computation
            )
    
    # Get final statistics
    stats = processor.get_stats()
    final_stats = profiler.stop_profiling()
    
    print(f"\nProcessing completed!")
    print(f"Total items processed: {stats['processed']}")
    print(f"Items skipped: {stats['skipped']}")
    print(f"Cache hits: {stats['cache_hit']}")
    print(f"Cache misses: {stats['cache_miss']}")
    print(f"Memory used: {format_bytes(final_stats['memory_used'])}")
    print(f"Peak memory: {format_bytes(final_stats['peak_usage'])}")
    
    # Show observer notification counts
    print(f"\nObserver notifications:")
    for observer in observers:
        print(f"  {observer.name}: {observer.notification_count} notifications")
    
    # Cleanup
    processor.cleanup()
    del processed_data, observers, processor
    gc.collect()
    
    print(f"\nMemory optimization demonstration completed!")

def run_all_demonstrations():
    """Run all memory optimization demonstrations."""
    print("PYTHON MEMORY OPTIMIZATION BEST PRACTICES")
    print("="*50)
    
    try:
        # Step 1: Memory profiling
        demonstrate_memory_profiling()
        
        # Step 2: __slots__ optimization
        compare_slots_memory_usage()
        demonstrate_slots_limitations()
        
        # Step 3: Generators vs lists
        compare_list_vs_generator_memory()
        demonstrate_generator_benefits()
        
        # Step 4: Weak references
        demonstrate_circular_reference_problem()
        demonstrate_weak_reference_solution()
        demonstrate_weak_cache()
        
        # Step 5: Memory-efficient data structures
        compare_data_structure_memory()
        compare_coordinate_structures()
        demonstrate_efficient_collections()
        compare_counter_implementations()
        demonstrate_string_interning()
        
        # Step 6: Object pooling
        compare_with_without_pooling()
        
        # Step 7: Garbage collection optimization
        demonstrate_gc_optimization()
        demonstrate_gc_generations()
        demonstrate_gc_friendly_patterns()
        
        # Step 8: Comprehensive demonstration
        comprehensive_memory_optimization_demo()
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()

# ===============================================================================
#                                MAIN EXECUTION
# ===============================================================================

if __name__ == "__main__":
    # Run all demonstrations
    run_all_demonstrations()
    
    print("\n" + "="*60)
    print("MEMORY OPTIMIZATION SUMMARY")
    print("="*60)
    print("""
Key Memory Optimization Techniques Demonstrated:

1. Memory Profiling and Measurement
   - Use tracemalloc to monitor memory usage
   - Measure before and after optimizations
   - Track peak memory usage

2. __slots__ for Memory-Efficient Classes
   - Eliminates __dict__ overhead
   - Significant memory savings for many instances
   - Trade-off: less flexibility

3. Generators vs Lists
   - Use generators for large datasets
   - Process data on-demand instead of loading all
   - Especially important for infinite sequences

4. Weak References
   - Prevent circular reference memory leaks
   - Use for observer patterns and caches
   - Allow objects to be garbage collected

5. Memory-Efficient Data Structures
   - Use arrays instead of lists for numeric data
   - Choose namedtuples for simple data containers
   - Use deque for queue operations
   - Consider string interning for repeated strings

6. Object Pooling
   - Reuse expensive objects instead of recreating
   - Reduces allocation overhead and GC pressure
   - Useful for database connections, heavy resources

7. Garbage Collection Optimization
   - Understand GC generations
   - Avoid creating unnecessary intermediate objects
   - Manual cleanup for large objects
   - Use generators to reduce GC pressure

8. Combined Techniques
   - Real applications benefit from multiple techniques
   - Profile first, then optimize based on measurements
   - Consider trade-offs between memory and complexity

Best Practices:
- Always measure before and after optimization
- Profile your specific use case
- Consider the trade-offs (memory vs speed vs complexity)
- Use the right tool for the job
- Clean up resources explicitly when possible
- Understand your application's memory patterns
    """)
    
    print("\nMemory optimization tutorial completed successfully!")
    print("Remember: Profile first, optimize second, measure results!")

