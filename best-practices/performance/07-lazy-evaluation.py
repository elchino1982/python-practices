"""Question: Implement lazy evaluation techniques to improve performance by deferring computation.

Create examples demonstrating various lazy evaluation patterns including:
lazy properties, lazy iterators, lazy data loading, and lazy computation chains.

Requirements:
1. Create lazy property decorators for expensive computations
2. Implement lazy iterators for large datasets
3. Create lazy data loading mechanisms
4. Demonstrate lazy computation chains
5. Show performance comparisons between eager and lazy evaluation

Example usage:
    lazy_data = LazyDataProcessor(large_dataset)
    result = lazy_data.filter(condition).map(transform).take(10)
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
# - How can you defer computation until it's actually needed?
# - What's the difference between eager and lazy evaluation?
# - How can you cache results to avoid recomputation?
# - What are generators and how do they provide lazy evaluation?
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


# Step 1: Import modules and create basic lazy property decorator
# ===============================================================================

# Explanation:
# Lazy evaluation defers computation until the result is actually needed.
# We'll start with a lazy property that computes expensive values only once.

import time
import functools
from typing import Iterator, Callable, Any, Optional, List
from collections.abc import Iterable

class LazyProperty:
    """A descriptor that implements lazy evaluation for properties."""
    
    def __init__(self, func: Callable):
        self.func = func
        self.name = func.__name__
        
    def __get__(self, obj, owner):
        if obj is None:
            return self
        
        # Check if value is already computed and cached
        if not hasattr(obj, f'_lazy_{self.name}'):
            print(f"Computing {self.name}...")
            # Compute and cache the value
            value = self.func(obj)
            setattr(obj, f'_lazy_{self.name}', value)
        
        return getattr(obj, f'_lazy_{self.name}')

# Example class using lazy property
class ExpensiveComputation:
    """Example class with expensive computations."""
    
    def __init__(self, data: List[int]):
        self.data = data
    
    @LazyProperty
    def expensive_sum(self) -> int:
        """Simulate an expensive computation."""
        time.sleep(1)  # Simulate expensive operation
        return sum(self.data)
    
    @LazyProperty
    def expensive_average(self) -> float:
        """Another expensive computation."""
        time.sleep(0.5)
        return sum(self.data) / len(self.data) if self.data else 0

# Step 1 demonstration
print("=== Step 1: Basic Lazy Property ===")
obj = ExpensiveComputation([1, 2, 3, 4, 5])
print("Object created (no computation yet)")

print("First access to expensive_sum:")
print(f"Sum: {obj.expensive_sum}")  # Computation happens here

print("Second access to expensive_sum:")
print(f"Sum: {obj.expensive_sum}")  # Uses cached value


# Step 2: Lazy Iterators and Generators
# ===============================================================================

# Explanation:
# Generators provide natural lazy evaluation - they produce values on demand
# rather than computing all values upfront.

class LazyRange:
    """A lazy range implementation that generates values on demand."""
    
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self) -> Iterator[int]:
        """Return a generator that produces values lazily."""
        current = self.start
        while current < self.end:
            print(f"Generating value: {current}")
            yield current
            current += self.step

def fibonacci_lazy(n: int) -> Iterator[int]:
    """Generate Fibonacci numbers lazily up to n terms."""
    a, b = 0, 1
    count = 0
    while count < n:
        print(f"Generating Fibonacci number {count + 1}: {a}")
        yield a
        a, b = b, a + b
        count += 1

def process_large_file_lazy(filename: str) -> Iterator[str]:
    """Process a large file lazily, line by line."""
    print(f"Opening file: {filename}")
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                print(f"Processing line {line_num}")
                yield line.strip().upper()
    except FileNotFoundError:
        print(f"File {filename} not found, using sample data")
        # Simulate file content for demonstration
        sample_lines = ["line 1", "line 2", "line 3", "line 4", "line 5"]
        for line_num, line in enumerate(sample_lines, 1):
            print(f"Processing sample line {line_num}")
            yield line.upper()

# Step 2 demonstration
print("\n=== Step 2: Lazy Iterators and Generators ===")

print("Lazy Range (only generates values when needed):")
lazy_range = LazyRange(1, 5)
print("LazyRange created (no values generated yet)")

print("Iterating through first 3 values:")
for i, value in enumerate(lazy_range):
    if i >= 2:
        break
    print(f"Got value: {value}")

print("\nFibonacci sequence (lazy generation):")
fib_gen = fibonacci_lazy(5)
print("Generator created (no computation yet)")

print("Getting first 3 Fibonacci numbers:")
for i, fib in enumerate(fib_gen):
    if i >= 2:
        break
    print(f"Fibonacci {i+1}: {fib}")

print("\nLazy file processing:")
file_processor = process_large_file_lazy("nonexistent.txt")
print("File processor created (file not opened yet)")

print("Processing first 2 lines:")
for i, processed_line in enumerate(file_processor):
    if i >= 1:
        break
    print(f"Processed: {processed_line}")


# Step 3: Lazy Data Loading and Caching
# ===============================================================================

# Explanation:
# Lazy data loading defers expensive operations like database queries,
# API calls, or file I/O until the data is actually needed.

class LazyDataLoader:
    """Lazy data loader that fetches data only when accessed."""
    
    def __init__(self, data_source: str):
        self.data_source = data_source
        self._data = None
        self._loaded = False
    
    def _load_data(self):
        """Simulate expensive data loading operation."""
        if not self._loaded:
            print(f"Loading data from {self.data_source}...")
            time.sleep(0.5)  # Simulate network/disk delay
            
            # Simulate different data sources
            if "database" in self.data_source:
                self._data = [{"id": i, "name": f"User {i}"} for i in range(1, 6)]
            elif "api" in self.data_source:
                self._data = [{"product": f"Product {i}", "price": i * 10} for i in range(1, 4)]
            else:
                self._data = [f"Item {i}" for i in range(1, 8)]
            
            self._loaded = True
            print(f"Data loaded: {len(self._data)} items")
    
    @property
    def data(self):
        """Get data, loading it lazily if needed."""
        self._load_data()
        return self._data
    
    def get_item(self, index: int):
        """Get a specific item, loading data only if needed."""
        self._load_data()
        return self._data[index] if 0 <= index < len(self._data) else None

class LazyCache:
    """A cache that computes values lazily and stores them."""
    
    def __init__(self):
        self._cache = {}
    
    def get(self, key: str, compute_func: Callable[[], Any]) -> Any:
        """Get value from cache, computing it lazily if not present."""
        if key not in self._cache:
            print(f"Cache miss for '{key}', computing value...")
            self._cache[key] = compute_func()
        else:
            print(f"Cache hit for '{key}'")
        return self._cache[key]
    
    def clear(self):
        """Clear the cache."""
        self._cache.clear()

def expensive_computation(x: int) -> int:
    """Simulate an expensive computation."""
    print(f"Performing expensive computation for {x}")
    time.sleep(0.3)
    return x ** 2 + x * 10

# Step 3 demonstration
print("\n=== Step 3: Lazy Data Loading and Caching ===")

print("Creating lazy data loaders (no data loaded yet):")
db_loader = LazyDataLoader("database_users")
api_loader = LazyDataLoader("api_products")
file_loader = LazyDataLoader("file_data")

print("\nAccessing data from database loader:")
print(f"First item: {db_loader.get_item(0)}")
print(f"Data length: {len(db_loader.data)}")

print("\nUsing lazy cache:")
cache = LazyCache()

print("First computation:")
result1 = cache.get("compute_5", lambda: expensive_computation(5))
print(f"Result: {result1}")

print("Second computation (should use cache):")
result2 = cache.get("compute_5", lambda: expensive_computation(5))
print(f"Result: {result2}")

print("Different computation:")
result3 = cache.get("compute_10", lambda: expensive_computation(10))
print(f"Result: {result3}")


# Step 4: Lazy Computation Chains
# ===============================================================================

# Explanation:
# Lazy computation chains allow you to build complex data processing pipelines
# that only execute when the final result is needed.

class LazyDataProcessor:
    """A lazy data processor that chains operations without immediate execution."""
    
    def __init__(self, data: Iterable):
        self._data = data
        self._operations = []
    
    def filter(self, predicate: Callable[[Any], bool]) -> 'LazyDataProcessor':
        """Add a filter operation to the chain."""
        new_processor = LazyDataProcessor(self._data)
        new_processor._operations = self._operations + [('filter', predicate)]
        return new_processor
    
    def map(self, transform: Callable[[Any], Any]) -> 'LazyDataProcessor':
        """Add a map operation to the chain."""
        new_processor = LazyDataProcessor(self._data)
        new_processor._operations = self._operations + [('map', transform)]
        return new_processor
    
    def take(self, n: int) -> List[Any]:
        """Execute the chain and take the first n results."""
        print(f"Executing lazy chain with {len(self._operations)} operations...")
        
        # Start with the original data
        result = iter(self._data)
        
        # Apply each operation in the chain
        for operation, func in self._operations:
            if operation == 'filter':
                result = filter(func, result)
            elif operation == 'map':
                result = map(func, result)
        
        # Take only the requested number of items
        return list(self._take_n(result, n))
    
    def _take_n(self, iterable: Iterator, n: int) -> Iterator:
        """Take the first n items from an iterator."""
        for i, item in enumerate(iterable):
            if i >= n:
                break
            yield item
    
    def collect(self) -> List[Any]:
        """Execute the chain and collect all results."""
        print(f"Executing lazy chain with {len(self._operations)} operations...")
        
        result = iter(self._data)
        for operation, func in self._operations:
            if operation == 'filter':
                result = filter(func, result)
            elif operation == 'map':
                result = map(func, result)
        
        return list(result)

class LazySequence:
    """A more advanced lazy sequence with method chaining."""
    
    def __init__(self, generator_func: Callable[[], Iterator]):
        self._generator_func = generator_func
    
    def map(self, func: Callable[[Any], Any]) -> 'LazySequence':
        """Transform each element lazily."""
        def new_generator():
            for item in self._generator_func():
                print(f"Mapping: {item} -> {func(item)}")
                yield func(item)
        return LazySequence(new_generator)
    
    def filter(self, predicate: Callable[[Any], bool]) -> 'LazySequence':
        """Filter elements lazily."""
        def new_generator():
            for item in self._generator_func():
                if predicate(item):
                    print(f"Filtering: {item} (kept)")
                    yield item
                else:
                    print(f"Filtering: {item} (removed)")
        return LazySequence(new_generator)
    
    def take(self, n: int) -> List[Any]:
        """Take the first n elements."""
        result = []
        for i, item in enumerate(self._generator_func()):
            if i >= n:
                break
            result.append(item)
        return result
    
    def to_list(self) -> List[Any]:
        """Convert to a list (forces evaluation)."""
        return list(self._generator_func())

def create_lazy_range(start: int, end: int) -> LazySequence:
    """Create a lazy sequence from a range."""
    def generator():
        for i in range(start, end):
            print(f"Generating: {i}")
            yield i
    return LazySequence(generator)

# Step 4 demonstration
print("\n=== Step 4: Lazy Computation Chains ===")

print("Creating lazy data processor:")
data = range(1, 11)  # Numbers 1 to 10
processor = LazyDataProcessor(data)

print("Building computation chain (no execution yet):")
result_chain = (processor
                .filter(lambda x: x % 2 == 0)  # Keep even numbers
                .map(lambda x: x * x)          # Square them
                .filter(lambda x: x > 10))     # Keep squares > 10

print("Chain built, now executing to get first 3 results:")
results = result_chain.take(3)
print(f"Results: {results}")

print("\nUsing LazySequence with method chaining:")
lazy_seq = create_lazy_range(1, 8)
print("LazySequence created (no generation yet)")

print("Building chain: filter odd -> square -> take 3")
chained_results = (lazy_seq
                   .filter(lambda x: x % 2 == 1)  # Keep odd numbers
                   .map(lambda x: x ** 2)          # Square them
                   .take(3))                       # Take first 3

print(f"Final results: {chained_results}")


# Step 5: Performance Comparisons and Advanced Examples
# ===============================================================================

# Explanation:
# Let's compare eager vs lazy evaluation to see the performance benefits
# and demonstrate more advanced lazy evaluation patterns.

def eager_processing(data: List[int]) -> List[int]:
    """Eager processing - all operations happen immediately."""
    print("Eager processing: Starting...")
    
    # Filter even numbers
    print("Eager: Filtering all data...")
    filtered = [x for x in data if x % 2 == 0]
    print(f"Eager: Filtered {len(filtered)} items")
    
    # Square all numbers
    print("Eager: Squaring all filtered data...")
    squared = [x * x for x in filtered]
    print(f"Eager: Squared {len(squared)} items")
    
    # Filter squares > 50
    print("Eager: Final filtering...")
    final = [x for x in squared if x > 50]
    print(f"Eager: Final result has {len(final)} items")
    
    return final[:3]  # Take first 3

def lazy_processing(data: List[int]) -> List[int]:
    """Lazy processing - operations happen on demand."""
    print("Lazy processing: Starting...")
    
    def lazy_pipeline():
        for x in data:
            if x % 2 == 0:  # Filter even
                squared = x * x
                if squared > 50:  # Filter > 50
                    print(f"Lazy: Processing {x} -> {squared}")
                    yield squared
    
    # Only process until we get 3 results
    result = []
    for item in lazy_pipeline():
        result.append(item)
        if len(result) >= 3:
            break
    
    return result

class LazyMemoization:
    """Advanced lazy evaluation with memoization."""
    
    def __init__(self):
        self._memo = {}
    
    def lazy_fibonacci(self, n: int) -> int:
        """Compute Fibonacci with lazy memoization."""
        if n in self._memo:
            print(f"Memo hit for fib({n})")
            return self._memo[n]
        
        print(f"Computing fib({n})")
        if n <= 1:
            result = n
        else:
            result = self.lazy_fibonacci(n-1) + self.lazy_fibonacci(n-2)
        
        self._memo[n] = result
        return result

class LazyInfiniteSequence:
    """Demonstrate lazy evaluation with infinite sequences."""
    
    @staticmethod
    def primes() -> Iterator[int]:
        """Generate prime numbers lazily (infinite sequence)."""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        n = 2
        while True:
            if is_prime(n):
                print(f"Found prime: {n}")
                yield n
            n += 1
    
    @staticmethod
    def fibonacci_infinite() -> Iterator[int]:
        """Generate Fibonacci sequence lazily (infinite)."""
        a, b = 0, 1
        while True:
            print(f"Fibonacci: {a}")
            yield a
            a, b = b, a + b

# Step 5 demonstration
print("\n=== Step 5: Performance Comparisons ===")

print("Comparing eager vs lazy processing:")
test_data = list(range(1, 101))  # Numbers 1 to 100

print("\n--- Eager Processing ---")
start_time = time.time()
eager_result = eager_processing(test_data)
eager_time = time.time() - start_time
print(f"Eager result: {eager_result}")
print(f"Eager time: {eager_time:.4f} seconds")

print("\n--- Lazy Processing ---")
start_time = time.time()
lazy_result = lazy_processing(test_data)
lazy_time = time.time() - start_time
print(f"Lazy result: {lazy_result}")
print(f"Lazy time: {lazy_time:.4f} seconds")

print(f"\nPerformance difference: {(eager_time - lazy_time):.4f} seconds")

print("\n--- Lazy Memoization ---")
memo = LazyMemoization()
print("Computing Fibonacci numbers with memoization:")
print(f"fib(10) = {memo.lazy_fibonacci(10)}")
print(f"fib(8) = {memo.lazy_fibonacci(8)}")  # Should use memoized values

print("\n--- Infinite Lazy Sequences ---")
print("First 5 prime numbers:")
prime_gen = LazyInfiniteSequence.primes()
primes = []
for prime in prime_gen:
    primes.append(prime)
    if len(primes) >= 5:
        break
print(f"Primes: {primes}")

print("\nFirst 7 Fibonacci numbers:")
fib_gen = LazyInfiniteSequence.fibonacci_infinite()
fibs = []
for fib in fib_gen:
    fibs.append(fib)
    if len(fibs) >= 7:
        break
print(f"Fibonacci: {fibs}")


# ===============================================================================
#                              COMPLETE EXAMPLE
# ===============================================================================

print("\n=== Complete Lazy Evaluation Example ===")

# Combining all concepts
class AdvancedLazyProcessor:
    """Advanced lazy processor combining all techniques."""
    
    def __init__(self, data_source: str):
        self.data_source = data_source
        self._cache = LazyCache()
        self._data_loader = LazyDataLoader(data_source)
    
    @LazyProperty
    def processed_data(self):
        """Lazily process and cache the data."""
        return self._cache.get(
            f"processed_{self.data_source}",
            lambda: self._process_data()
        )
    
    def _process_data(self):
        """Internal data processing."""
        raw_data = self._data_loader.data
        # Simulate complex processing
        return [item for item in raw_data if isinstance(item, dict)]
    
    def lazy_query(self, condition: Callable[[Any], bool]) -> LazySequence:
        """Create a lazy query on the data."""
        def generator():
            for item in self.processed_data:
                if condition(item):
                    yield item
        return LazySequence(generator)

# Final demonstration
print("Creating advanced lazy processor:")
processor = AdvancedLazyProcessor("database_users")

print("Creating lazy query (no execution yet):")
user_query = processor.lazy_query(lambda user: user.get('id', 0) > 2)

print("Executing query to get first 2 results:")
results = user_query.take(2)
print(f"Query results: {results}")

print("\n🎉 Lazy Evaluation Implementation Complete!")
print("Key benefits demonstrated:")
print("- Deferred computation until needed")
print("- Memory efficiency with large datasets")
print("- Performance optimization through caching")
print("- Composable operation chains")
print("- Support for infinite sequences")

