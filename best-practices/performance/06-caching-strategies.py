"""Question: Implement various caching strategies to improve application performance.

Create different caching mechanisms including memoization, LRU cache, TTL cache,
and custom cache implementations for different use cases.

Requirements:
1. Implement function memoization with decorators
2. Create LRU (Least Recently Used) cache implementation
3. Implement TTL (Time To Live) cache with expiration
4. Create a multi-level cache system
5. Demonstrate performance improvements with benchmarks

Example usage:
    @memoize
    def fibonacci(n):
        return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)
    
    cache = LRUCache(maxsize=100)
    result = cache.get_or_compute(key, expensive_function)
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
# - What are the different types of caching strategies?
# - How can you implement memoization using decorators?
# - What data structures work best for LRU cache?
# - How do you handle cache expiration with TTL?
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


# Step 1: Import modules and create basic memoization decorator
# ===============================================================================

# Explanation:
# Memoization is the simplest form of caching where we store function results
# to avoid recomputing them. We'll start with a basic decorator implementation.

import time
import threading
from collections import OrderedDict
from typing import Any, Callable, Dict, Optional, Tuple
from functools import wraps
from weakref import WeakKeyDictionary

def memoize(func: Callable) -> Callable:
    """Basic memoization decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: f"Cache size: {len(cache)}"
    
    return wrapper

# Example usage of basic memoization
@memoize
def fibonacci_step1(n: int) -> int:
    """Fibonacci function with basic memoization."""
    if n < 2:
        return n
    return fibonacci_step1(n - 1) + fibonacci_step1(n - 2)

def demo_step1():
    """Demonstrate basic memoization."""
    print("=== Step 1: Basic Memoization ===")
    
    start_time = time.time()
    result = fibonacci_step1(30)
    end_time = time.time()
    
    print(f"fibonacci_step1(30) = {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Cache info: {fibonacci_step1.cache_info()}")
    
    # Second call should be much faster
    start_time = time.time()
    result = fibonacci_step1(30)
    end_time = time.time()
    
    print(f"Second call time: {end_time - start_time:.6f} seconds")
    print()

if __name__ == "__main__":
    demo_step1()


# Step 2: Add improved memoization and LRU Cache implementation
# ===============================================================================

# Explanation:
# Now we'll add all code from Step 1 plus an improved memoization decorator
# that handles unhashable arguments and implement a proper LRU cache.

# All imports from Step 1
import time
import threading
from collections import OrderedDict
from typing import Any, Callable, Dict, Optional, Tuple
from functools import wraps
from weakref import WeakKeyDictionary

# Step 1 code: Basic memoization decorator
def memoize_step2(func: Callable) -> Callable:
    """Basic memoization decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: f"Cache size: {len(cache)}"
    
    return wrapper

# Step 1 example function
@memoize_step2
def fibonacci_step2(n: int) -> int:
    """Fibonacci function with basic memoization."""
    if n < 2:
        return n
    return fibonacci_step2(n - 1) + fibonacci_step2(n - 2)

# New in Step 2: Improved memoization with better key handling
def advanced_memoize(func: Callable) -> Callable:
    """Advanced memoization decorator with better key handling."""
    cache = {}
    
    def make_key(*args, **kwargs):
        """Create a hashable key from function arguments."""
        try:
            # Try to create a simple tuple key
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            return key
        except TypeError:
            # Handle unhashable types by converting to string
            return str(args) + str(sorted(kwargs.items()))
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = make_key(*args, **kwargs)
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: f"Cache size: {len(cache)}, hits: {getattr(wrapper, '_hits', 0)}, misses: {getattr(wrapper, '_misses', 0)}"
    wrapper._hits = 0
    wrapper._misses = 0
    
    # Track hits and misses
    original_wrapper = wrapper
    
    @wraps(func)
    def tracking_wrapper(*args, **kwargs):
        key = make_key(*args, **kwargs)
        
        if key in cache:
            tracking_wrapper._hits += 1
        else:
            tracking_wrapper._misses += 1
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    tracking_wrapper.cache = cache
    tracking_wrapper.cache_clear = lambda: cache.clear()
    tracking_wrapper.cache_info = lambda: f"Cache size: {len(cache)}, hits: {tracking_wrapper._hits}, misses: {tracking_wrapper._misses}"
    tracking_wrapper._hits = 0
    tracking_wrapper._misses = 0
    
    return tracking_wrapper

# New in Step 2: LRU Cache implementation
class LRUCache:
    """Least Recently Used cache implementation."""
    
    def __init__(self, maxsize: int = 128):
        self.maxsize = maxsize
        self.cache = OrderedDict()
        self._hits = 0
        self._misses = 0
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache, return None if not found."""
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            self._hits += 1
            return self.cache[key]
        
        self._misses += 1
        return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache."""
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        else:
            # Add new key
            if len(self.cache) >= self.maxsize:
                # Remove least recently used item
                self.cache.popitem(last=False)
        
        self.cache[key] = value
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear the cache."""
        self.cache.clear()
        self._hits = 0
        self._misses = 0
    
    def cache_info(self) -> str:
        """Get cache statistics."""
        return f"LRU Cache - Size: {len(self.cache)}/{self.maxsize}, Hits: {self._hits}, Misses: {self._misses}"

# New in Step 2: LRU cache decorator
def lru_cache(maxsize: int = 128):
    """LRU cache decorator."""
    def decorator(func: Callable) -> Callable:
        cache = LRUCache(maxsize)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# Example usage of LRU cache
@lru_cache(maxsize=50)
def expensive_computation_step2(n: int) -> int:
    """Simulate an expensive computation."""
    time.sleep(0.01)  # Simulate work
    return n * n * n

def demo_step2():
    """Demonstrate Step 1 and Step 2 functionality."""
    print("=== Step 2: Advanced Memoization and LRU Cache ===")
    
    # Demo Step 1 functionality
    print("Step 1 - Basic Memoization:")
    start_time = time.time()
    result = fibonacci_step2(30)
    end_time = time.time()
    print(f"fibonacci_step2(30) = {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Cache info: {fibonacci_step2.cache_info()}")
    print()
    
    # Demo LRU cache
    print("Step 2 - LRU Cache:")
    
    # Test LRU cache with expensive computation
    start_time = time.time()
    for i in range(10):
        result = expensive_computation_step2(i % 5)  # Only 5 unique values
    end_time = time.time()
    
    print(f"10 computations (5 unique) took: {end_time - start_time:.4f} seconds")
    print(f"Cache info: {expensive_computation_step2.cache_info()}")
    
    # Test cache eviction
    print("\nTesting cache eviction:")
    cache = LRUCache(maxsize=3)
    
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    print(f"After adding a,b,c: {list(cache.cache.keys())}")
    
    cache.put("d", 4)  # Should evict 'a'
    print(f"After adding d: {list(cache.cache.keys())}")
    
    cache.get("b")  # Access 'b' to make it recently used
    cache.put("e", 5)  # Should evict 'c' (least recently used)
    print(f"After accessing b and adding e: {list(cache.cache.keys())}")
    print()

if __name__ == "__main__":
    demo_step1()
    demo_step2()


# Step 3: Add TTL (Time To Live) Cache implementation
# ===============================================================================

# Explanation:
# Now we'll add all code from Steps 1-2 plus TTL cache that automatically
# expires entries after a specified time period.

# All imports from previous steps
import time
import threading
from collections import OrderedDict
from typing import Any, Callable, Dict, Optional, Tuple
from functools import wraps
from weakref import WeakKeyDictionary

# Step 1 code: Basic memoization decorator
def memoize_step3(func: Callable) -> Callable:
    """Basic memoization decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: f"Cache size: {len(cache)}"
    
    return wrapper

# Step 1 example function
@memoize_step3
def fibonacci_step3(n: int) -> int:
    """Fibonacci function with basic memoization."""
    if n < 2:
        return n
    return fibonacci_step3(n - 1) + fibonacci_step3(n - 2)

# Step 2 code: Improved memoization with better key handling
def advanced_memoize_step3(func: Callable) -> Callable:
    """Advanced memoization decorator with better key handling."""
    cache = {}
    
    def make_key(*args, **kwargs):
        """Create a hashable key from function arguments."""
        try:
            # Try to create a simple tuple key
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            return key
        except TypeError:
            # Handle unhashable types by converting to string
            return str(args) + str(sorted(kwargs.items()))
    
    @wraps(func)
    def tracking_wrapper(*args, **kwargs):
        key = make_key(*args, **kwargs)
        
        if key in cache:
            tracking_wrapper._hits += 1
        else:
            tracking_wrapper._misses += 1
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    tracking_wrapper.cache = cache
    tracking_wrapper.cache_clear = lambda: cache.clear()
    tracking_wrapper.cache_info = lambda: f"Cache size: {len(cache)}, hits: {tracking_wrapper._hits}, misses: {tracking_wrapper._misses}"
    tracking_wrapper._hits = 0
    tracking_wrapper._misses = 0
    
    return tracking_wrapper

# Step 2 code: LRU Cache implementation
class LRUCache_step3:
    """Least Recently Used cache implementation."""
    
    def __init__(self, maxsize: int = 128):
        self.maxsize = maxsize
        self.cache = OrderedDict()
        self._hits = 0
        self._misses = 0
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache, return None if not found."""
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            self._hits += 1
            return self.cache[key]
        
        self._misses += 1
        return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache."""
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        else:
            # Add new key
            if len(self.cache) >= self.maxsize:
                # Remove least recently used item
                self.cache.popitem(last=False)
        
        self.cache[key] = value
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear the cache."""
        self.cache.clear()
        self._hits = 0
        self._misses = 0
    
    def cache_info(self) -> str:
        """Get cache statistics."""
        return f"LRU Cache - Size: {len(self.cache)}/{self.maxsize}, Hits: {self._hits}, Misses: {self._misses}"

# Step 2 code: LRU cache decorator
def lru_cache_step3(maxsize: int = 128):
    """LRU cache decorator."""
    def decorator(func: Callable) -> Callable:
        cache = LRUCache_step3(maxsize)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# Step 2 example function
@lru_cache_step3(maxsize=50)
def expensive_computation_step3(n: int) -> int:
    """Simulate an expensive computation."""
    time.sleep(0.01)  # Simulate work
    return n * n * n

# New in Step 3: TTL Cache implementation
class TTLCache:
    """Time To Live cache implementation with automatic expiration."""
    
    def __init__(self, maxsize: int = 128, ttl: float = 300.0):
        """
        Initialize TTL cache.
        
        Args:
            maxsize: Maximum number of items in cache
            ttl: Time to live in seconds (default 5 minutes)
        """
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = {}  # key -> (value, timestamp)
        self.access_order = OrderedDict()  # For LRU behavior when at capacity
        self._hits = 0
        self._misses = 0
        self._lock = threading.Lock()
    
    def _is_expired(self, timestamp: float) -> bool:
        """Check if an entry has expired."""
        return time.time() - timestamp > self.ttl
    
    def _cleanup_expired(self) -> None:
        """Remove expired entries from cache."""
        current_time = time.time()
        expired_keys = [
            key for key, (_, timestamp) in self.cache.items()
            if current_time - timestamp > self.ttl
        ]
        
        for key in expired_keys:
            del self.cache[key]
            if key in self.access_order:
                del self.access_order[key]
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache, return None if not found or expired."""
        with self._lock:
            if key not in self.cache:
                self._misses += 1
                return None
            
            value, timestamp = self.cache[key]
            
            if self._is_expired(timestamp):
                # Entry has expired, remove it
                del self.cache[key]
                if key in self.access_order:
                    del self.access_order[key]
                self._misses += 1
                return None
            
            # Update access order for LRU
            self.access_order[key] = True
            self.access_order.move_to_end(key)
            self._hits += 1
            return value
    
    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache with current timestamp."""
        with self._lock:
            current_time = time.time()
            
            # Clean up expired entries periodically
            if len(self.cache) > self.maxsize * 0.8:  # Cleanup when 80% full
                self._cleanup_expired()
            
            # If at capacity and key is new, remove LRU item
            if key not in self.cache and len(self.cache) >= self.maxsize:
                if self.access_order:
                    lru_key = next(iter(self.access_order))
                    del self.cache[lru_key]
                    del self.access_order[lru_key]
            
            # Add/update the entry
            self.cache[key] = (value, current_time)
            self.access_order[key] = True
            self.access_order.move_to_end(key)
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear the cache."""
        with self._lock:
            self.cache.clear()
            self.access_order.clear()
            self._hits = 0
            self._misses = 0
    
    def cache_info(self) -> str:
        """Get cache statistics."""
        with self._lock:
            self._cleanup_expired()  # Clean up before reporting
            return f"TTL Cache - Size: {len(self.cache)}/{self.maxsize}, TTL: {self.ttl}s, Hits: {self._hits}, Misses: {self._misses}"

# New in Step 3: TTL cache decorator
def ttl_cache(maxsize: int = 128, ttl: float = 300.0):
    """TTL cache decorator with automatic expiration."""
    def decorator(func: Callable) -> Callable:
        cache = TTLCache(maxsize, ttl)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# New in Step 3: Example functions with TTL cache
@ttl_cache(maxsize=100, ttl=2.0)  # 2 second TTL for demo
def time_sensitive_computation(n: int) -> str:
    """Computation that should expire after 2 seconds."""
    current_time = time.strftime("%H:%M:%S")
    return f"Result for {n} computed at {current_time}"

@ttl_cache(maxsize=50, ttl=5.0)  # 5 second TTL
def weather_data(city: str) -> dict:
    """Simulate fetching weather data that expires after 5 seconds."""
    time.sleep(0.1)  # Simulate API call
    return {
        "city": city,
        "temperature": 20 + hash(city) % 15,  # Fake temperature
        "timestamp": time.time()
    }

def demo_step3():
    """Demonstrate Steps 1, 2, and 3 functionality."""
    print("=== Step 3: TTL Cache Implementation ===")
    
    # Demo Step 1 functionality
    print("Step 1 - Basic Memoization:")
    start_time = time.time()
    result = fibonacci_step3(30)
    end_time = time.time()
    print(f"fibonacci_step3(30) = {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Cache info: {fibonacci_step3.cache_info()}")
    print()
    
    # Demo Step 2 functionality
    print("Step 2 - LRU Cache:")
    start_time = time.time()
    for i in range(10):
        result = expensive_computation_step3(i % 5)  # Only 5 unique values
    end_time = time.time()
    print(f"10 computations (5 unique) took: {end_time - start_time:.4f} seconds")
    print(f"Cache info: {expensive_computation_step3.cache_info()}")
    print()
    
    # Demo Step 3 - TTL Cache
    print("Step 3 - TTL Cache:")
    
    # Test TTL cache with time-sensitive data
    print("Testing TTL expiration:")
    result1 = time_sensitive_computation(42)
    print(f"First call: {result1}")
    
    result2 = time_sensitive_computation(42)  # Should be cached
    print(f"Second call (cached): {result2}")
    
    print("Waiting 2.5 seconds for cache to expire...")
    time.sleep(2.5)
    
    result3 = time_sensitive_computation(42)  # Should be recomputed
    print(f"Third call (after expiration): {result3}")
    print(f"Cache info: {time_sensitive_computation.cache_info()}")
    print()
    
    # Test TTL cache with multiple entries
    print("Testing TTL cache with multiple entries:")
    cities = ["New York", "London", "Tokyo", "Sydney"]
    
    for city in cities:
        weather = weather_data(city)
        print(f"{city}: {weather['temperature']}°C")
    
    print(f"Weather cache info: {weather_data.cache_info()}")
    
    # Test manual TTL cache
    print("\nTesting manual TTL cache:")
    manual_cache = TTLCache(maxsize=3, ttl=1.0)  # 1 second TTL
    
    manual_cache.put("key1", "value1")
    manual_cache.put("key2", "value2")
    print(f"Added key1, key2. Cache info: {manual_cache.cache_info()}")
    
    print(f"Get key1: {manual_cache.get('key1')}")
    
    print("Waiting 1.5 seconds for expiration...")
    time.sleep(1.5)
    
    print(f"Get key1 after expiration: {manual_cache.get('key1')}")
    print(f"Final cache info: {manual_cache.cache_info()}")
    print()

if __name__ == "__main__":
    demo_step1()
    demo_step2()
    demo_step3()


# Step 4: Add Multi-Level Cache System
# ===============================================================================

# Explanation:
# Now we'll add all code from Steps 1-3 plus a sophisticated multi-level cache
# system that combines different caching strategies for optimal performance.

# All imports from previous steps
import time
import threading
from collections import OrderedDict
from typing import Any, Callable, Dict, Optional, Tuple, List
from functools import wraps
from weakref import WeakKeyDictionary

# Step 1 code: Basic memoization decorator
def memoize_step4(func: Callable) -> Callable:
    """Basic memoization decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: f"Cache size: {len(cache)}"
    
    return wrapper

# Step 1 example function
@memoize_step4
def fibonacci_step4(n: int) -> int:
    """Fibonacci function with basic memoization."""
    if n < 2:
        return n
    return fibonacci_step4(n - 1) + fibonacci_step4(n - 2)

# Step 2 code: Improved memoization with better key handling
def advanced_memoize_step4(func: Callable) -> Callable:
    """Advanced memoization decorator with better key handling."""
    cache = {}
    
    def make_key(*args, **kwargs):
        """Create a hashable key from function arguments."""
        try:
            # Try to create a simple tuple key
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            return key
        except TypeError:
            # Handle unhashable types by converting to string
            return str(args) + str(sorted(kwargs.items()))
    
    @wraps(func)
    def tracking_wrapper(*args, **kwargs):
        key = make_key(*args, **kwargs)
        
        if key in cache:
            tracking_wrapper._hits += 1
        else:
            tracking_wrapper._misses += 1
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    tracking_wrapper.cache = cache
    tracking_wrapper.cache_clear = lambda: cache.clear()
    tracking_wrapper.cache_info = lambda: f"Cache size: {len(cache)}, hits: {tracking_wrapper._hits}, misses: {tracking_wrapper._misses}"
    tracking_wrapper._hits = 0
    tracking_wrapper._misses = 0
    
    return tracking_wrapper

# Step 2 code: LRU Cache implementation
class LRUCache_step4:
    """Least Recently Used cache implementation."""
    
    def __init__(self, maxsize: int = 128):
        self.maxsize = maxsize
        self.cache = OrderedDict()
        self._hits = 0
        self._misses = 0
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache, return None if not found."""
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            self._hits += 1
            return self.cache[key]
        
        self._misses += 1
        return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache."""
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        else:
            # Add new key
            if len(self.cache) >= self.maxsize:
                # Remove least recently used item
                self.cache.popitem(last=False)
        
        self.cache[key] = value
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear the cache."""
        self.cache.clear()
        self._hits = 0
        self._misses = 0
    
    def cache_info(self) -> str:
        """Get cache statistics."""
        return f"LRU Cache - Size: {len(self.cache)}/{self.maxsize}, Hits: {self._hits}, Misses: {self._misses}"

# Step 2 code: LRU cache decorator
def lru_cache_step4(maxsize: int = 128):
    """LRU cache decorator."""
    def decorator(func: Callable) -> Callable:
        cache = LRUCache_step4(maxsize)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# Step 2 example function
@lru_cache_step4(maxsize=50)
def expensive_computation_step4(n: int) -> int:
    """Simulate an expensive computation."""
    time.sleep(0.01)  # Simulate work
    return n * n * n

# Step 3 code: TTL Cache implementation
class TTLCache_step4:
    """Time To Live cache implementation with automatic expiration."""
    
    def __init__(self, maxsize: int = 128, ttl: float = 300.0):
        """
        Initialize TTL cache.
        
        Args:
            maxsize: Maximum number of items in cache
            ttl: Time to live in seconds (default 5 minutes)
        """
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = {}  # key -> (value, timestamp)
        self.access_order = OrderedDict()  # For LRU behavior when at capacity
        self._hits = 0
        self._misses = 0
        self._lock = threading.Lock()
    
    def _is_expired(self, timestamp: float) -> bool:
        """Check if an entry has expired."""
        return time.time() - timestamp > self.ttl
    
    def _cleanup_expired(self) -> None:
        """Remove expired entries from cache."""
        current_time = time.time()
        expired_keys = [
            key for key, (_, timestamp) in self.cache.items()
            if current_time - timestamp > self.ttl
        ]
        
        for key in expired_keys:
            del self.cache[key]
            if key in self.access_order:
                del self.access_order[key]
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache, return None if not found or expired."""
        with self._lock:
            if key not in self.cache:
                self._misses += 1
                return None
            
            value, timestamp = self.cache[key]
            
            if self._is_expired(timestamp):
                # Entry has expired, remove it
                del self.cache[key]
                if key in self.access_order:
                    del self.access_order[key]
                self._misses += 1
                return None
            
            # Update access order for LRU
            self.access_order[key] = True
            self.access_order.move_to_end(key)
            self._hits += 1
            return value
    
    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache with current timestamp."""
        with self._lock:
            current_time = time.time()
            
            # Clean up expired entries periodically
            if len(self.cache) > self.maxsize * 0.8:  # Cleanup when 80% full
                self._cleanup_expired()
            
            # If at capacity and key is new, remove LRU item
            if key not in self.cache and len(self.cache) >= self.maxsize:
                if self.access_order:
                    lru_key = next(iter(self.access_order))
                    del self.cache[lru_key]
                    del self.access_order[lru_key]
            
            # Add/update the entry
            self.cache[key] = (value, current_time)
            self.access_order[key] = True
            self.access_order.move_to_end(key)
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear the cache."""
        with self._lock:
            self.cache.clear()
            self.access_order.clear()
            self._hits = 0
            self._misses = 0
    
    def cache_info(self) -> str:
        """Get cache statistics."""
        with self._lock:
            self._cleanup_expired()  # Clean up before reporting
            return f"TTL Cache - Size: {len(self.cache)}/{self.maxsize}, TTL: {self.ttl}s, Hits: {self._hits}, Misses: {self._misses}"

# Step 3 code: TTL cache decorator
def ttl_cache_step4(maxsize: int = 128, ttl: float = 300.0):
    """TTL cache decorator with automatic expiration."""
    def decorator(func: Callable) -> Callable:
        cache = TTLCache_step4(maxsize, ttl)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# Step 3 example functions
@ttl_cache_step4(maxsize=100, ttl=2.0)  # 2 second TTL for demo
def time_sensitive_computation_step4(n: int) -> str:
    """Computation that should expire after 2 seconds."""
    current_time = time.strftime("%H:%M:%S")
    return f"Result for {n} computed at {current_time}"

@ttl_cache_step4(maxsize=50, ttl=5.0)  # 5 second TTL
def weather_data_step4(city: str) -> dict:
    """Simulate fetching weather data that expires after 5 seconds."""
    time.sleep(0.1)  # Simulate API call
    return {
        "city": city,
        "temperature": 20 + hash(city) % 15,  # Fake temperature
        "timestamp": time.time()
    }

# New in Step 4: Multi-Level Cache System
class MultiLevelCache:
    """Multi-level cache system combining different caching strategies."""
    
    def __init__(self, 
                 l1_maxsize: int = 50,     # Fast, small cache
                 l2_maxsize: int = 200,    # Medium cache with LRU
                 l3_maxsize: int = 1000,   # Large cache with TTL
                 l3_ttl: float = 3600.0):  # 1 hour TTL for L3
        """
        Initialize multi-level cache system.
        
        L1: Small, fast in-memory cache (dict)
        L2: Medium LRU cache
        L3: Large TTL cache with expiration
        """
        # Level 1: Fast dictionary cache (most recently accessed)
        self.l1_cache = {}
        self.l1_maxsize = l1_maxsize
        self.l1_access_order = []
        
        # Level 2: LRU cache
        self.l2_cache = LRUCache_step4(l2_maxsize)
        
        # Level 3: TTL cache
        self.l3_cache = TTLCache_step4(l3_maxsize, l3_ttl)
        
        # Statistics
        self.l1_hits = 0
        self.l2_hits = 0
        self.l3_hits = 0
        self.misses = 0
        self._lock = threading.Lock()
    
    def _promote_to_l1(self, key: Any, value: Any) -> None:
        """Promote a value to L1 cache."""
        if len(self.l1_cache) >= self.l1_maxsize:
            # Remove least recently accessed item
            if self.l1_access_order:
                old_key = self.l1_access_order.pop(0)
                if old_key in self.l1_cache:
                    del self.l1_cache[old_key]
        
        self.l1_cache[key] = value
        if key in self.l1_access_order:
            self.l1_access_order.remove(key)
        self.l1_access_order.append(key)
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from multi-level cache."""
        with self._lock:
            # Try L1 cache first (fastest)
            if key in self.l1_cache:
                # Update access order
                if key in self.l1_access_order:
                    self.l1_access_order.remove(key)
                self.l1_access_order.append(key)
                self.l1_hits += 1
                return self.l1_cache[key]
            
            # Try L2 cache (LRU)
            value = self.l2_cache.get(key)
            if value is not None:
                self.l2_hits += 1
                # Promote to L1
                self._promote_to_l1(key, value)
                return value
            
            # Try L3 cache (TTL)
            value = self.l3_cache.get(key)
            if value is not None:
                self.l3_hits += 1
                # Promote to L2 and L1
                self.l2_cache.put(key, value)
                self._promote_to_l1(key, value)
                return value
            
            # Cache miss
            self.misses += 1
            return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put value in multi-level cache."""
        with self._lock:
            # Store in all levels
            self._promote_to_l1(key, value)
            self.l2_cache.put(key, value)
            self.l3_cache.put(key, value)
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear all cache levels."""
        with self._lock:
            self.l1_cache.clear()
            self.l1_access_order.clear()
            self.l2_cache.clear()
            self.l3_cache.clear()
            self.l1_hits = 0
            self.l2_hits = 0
            self.l3_hits = 0
            self.misses = 0
    
    def cache_info(self) -> str:
        """Get comprehensive cache statistics."""
        with self._lock:
            total_requests = self.l1_hits + self.l2_hits + self.l3_hits + self.misses
            hit_rate = ((self.l1_hits + self.l2_hits + self.l3_hits) / total_requests * 100) if total_requests > 0 else 0
            
            return (f"Multi-Level Cache Stats:\n"
                   f"  L1: {len(self.l1_cache)}/{self.l1_maxsize} items, {self.l1_hits} hits\n"
                   f"  L2: {self.l2_cache.cache_info()}\n"
                   f"  L3: {self.l3_cache.cache_info()}\n"
                   f"  Total: {self.l1_hits + self.l2_hits + self.l3_hits} hits, {self.misses} misses\n"
                   f"  Hit Rate: {hit_rate:.1f}%")

# New in Step 4: Multi-level cache decorator
def multi_level_cache(l1_maxsize: int = 50, l2_maxsize: int = 200, 
                     l3_maxsize: int = 1000, l3_ttl: float = 3600.0):
    """Multi-level cache decorator."""
    def decorator(func: Callable) -> Callable:
        cache = MultiLevelCache(l1_maxsize, l2_maxsize, l3_maxsize, l3_ttl)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# New in Step 4: Example functions with multi-level cache
@multi_level_cache(l1_maxsize=10, l2_maxsize=50, l3_maxsize=200, l3_ttl=60.0)
def complex_computation(n: int, operation: str = "square") -> int:
    """Complex computation with multi-level caching."""
    time.sleep(0.05)  # Simulate expensive computation
    
    if operation == "square":
        return n * n
    elif operation == "cube":
        return n * n * n
    elif operation == "factorial":
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    else:
        return n

@multi_level_cache(l1_maxsize=5, l2_maxsize=20, l3_maxsize=100, l3_ttl=30.0)
def database_query_simulation(table: str, id: int) -> dict:
    """Simulate database query with multi-level caching."""
    time.sleep(0.1)  # Simulate database latency
    return {
        "table": table,
        "id": id,
        "data": f"Record {id} from {table}",
        "timestamp": time.time()
    }

def demo_step4():
    """Demonstrate Steps 1, 2, 3, and 4 functionality."""
    print("=== Step 4: Multi-Level Cache System ===")
    
    # Demo Step 1 functionality
    print("Step 1 - Basic Memoization:")
    start_time = time.time()
    result = fibonacci_step4(30)
    end_time = time.time()
    print(f"fibonacci_step4(30) = {result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"Cache info: {fibonacci_step4.cache_info()}")
    print()
    
    # Demo Step 2 functionality
    print("Step 2 - LRU Cache:")
    start_time = time.time()
    for i in range(10):
        result = expensive_computation_step4(i % 5)  # Only 5 unique values
    end_time = time.time()
    print(f"10 computations (5 unique) took: {end_time - start_time:.4f} seconds")
    print(f"Cache info: {expensive_computation_step4.cache_info()}")
    print()
    
    # Demo Step 3 functionality
    print("Step 3 - TTL Cache:")
    result1 = time_sensitive_computation_step4(42)
    print(f"TTL cache result: {result1}")
    print(f"Cache info: {time_sensitive_computation_step4.cache_info()}")
    print()
    
    # Demo Step 4 - Multi-Level Cache
    print("Step 4 - Multi-Level Cache:")
    
    # Test multi-level cache with various access patterns
    print("Testing multi-level cache with complex computations:")
    
    # First, populate cache with different operations
    operations = ["square", "cube", "factorial"]
    numbers = [5, 10, 15, 20, 5, 10]  # Some repeats
    
    start_time = time.time()
    for i, num in enumerate(numbers):
        op = operations[i % len(operations)]
        result = complex_computation(num, op)
        print(f"complex_computation({num}, '{op}') = {result}")
    end_time = time.time()
    
    print(f"\nFirst round took: {end_time - start_time:.4f} seconds")
    print(f"Cache info:\n{complex_computation.cache_info()}")
    print()
    
    # Second round - should hit cache more often
    print("Second round (should hit cache):")
    start_time = time.time()
    for i, num in enumerate(numbers):
        op = operations[i % len(operations)]
        result = complex_computation(num, op)
    end_time = time.time()
    
    print(f"Second round took: {end_time - start_time:.4f} seconds")
    print(f"Cache info:\n{complex_computation.cache_info()}")
    print()
    
    # Test database simulation
    print("Testing database query simulation:")
    tables = ["users", "orders", "products"]
    ids = [1, 2, 3, 1, 2, 4, 1]  # Some repeats
    
    start_time = time.time()
    for i, table_id in enumerate(ids):
        table = tables[i % len(tables)]
        result = database_query_simulation(table, table_id)
        print(f"Query {table}[{table_id}]: {result['data']}")
    end_time = time.time()
    
    print(f"\nDatabase queries took: {end_time - start_time:.4f} seconds")
    print(f"Database cache info:\n{database_query_simulation.cache_info()}")
    print()
    
    # Test manual multi-level cache
    print("Testing manual multi-level cache:")
    manual_cache = MultiLevelCache(l1_maxsize=2, l2_maxsize=5, l3_maxsize=10, l3_ttl=60.0)
    
    # Add some values
    for i in range(8):
        manual_cache.put(f"key{i}", f"value{i}")
    
    print("After adding 8 items:")
    print(manual_cache.cache_info())
    print()
    
    # Access some values to test promotion
    print("Accessing some values:")
    for key in ["key0", "key3", "key7", "key0", "key3"]:
        value = manual_cache.get(key)
        print(f"Get {key}: {value}")
    
    print("\nAfter accessing values:")
    print(manual_cache.cache_info())
    print()

if __name__ == "__main__":
    demo_step1()
    demo_step2()
    demo_step3()
    demo_step4()


# Step 5: Add Performance Benchmarks and Comprehensive Examples
# ===============================================================================

# Explanation:
# Now we'll add all code from Steps 1-4 plus comprehensive performance benchmarks
# and real-world examples that demonstrate the effectiveness of different caching strategies.

# All imports from previous steps
import time
import threading
import random
from collections import OrderedDict
from typing import Any, Callable, Dict, Optional, Tuple, List
from functools import wraps
from weakref import WeakKeyDictionary

# Step 1 code: Basic memoization decorator
def memoize_final(func: Callable) -> Callable:
    """Basic memoization decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    # Add cache inspection methods
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: f"Cache size: {len(cache)}"
    
    return wrapper

# Step 1 example function
@memoize_final
def fibonacci_final(n: int) -> int:
    """Fibonacci function with basic memoization."""
    if n < 2:
        return n
    return fibonacci_final(n - 1) + fibonacci_final(n - 2)

# Step 2 code: Improved memoization with better key handling
def advanced_memoize_final(func: Callable) -> Callable:
    """Advanced memoization decorator with better key handling."""
    cache = {}
    
    def make_key(*args, **kwargs):
        """Create a hashable key from function arguments."""
        try:
            # Try to create a simple tuple key
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            return key
        except TypeError:
            # Handle unhashable types by converting to string
            return str(args) + str(sorted(kwargs.items()))
    
    @wraps(func)
    def tracking_wrapper(*args, **kwargs):
        key = make_key(*args, **kwargs)
        
        if key in cache:
            tracking_wrapper._hits += 1
        else:
            tracking_wrapper._misses += 1
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    tracking_wrapper.cache = cache
    tracking_wrapper.cache_clear = lambda: cache.clear()
    tracking_wrapper.cache_info = lambda: f"Cache size: {len(cache)}, hits: {tracking_wrapper._hits}, misses: {tracking_wrapper._misses}"
    tracking_wrapper._hits = 0
    tracking_wrapper._misses = 0
    
    return tracking_wrapper

# Step 2 code: LRU Cache implementation
class LRUCache_final:
    """Least Recently Used cache implementation."""
    
    def __init__(self, maxsize: int = 128):
        self.maxsize = maxsize
        self.cache = OrderedDict()
        self._hits = 0
        self._misses = 0
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache, return None if not found."""
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            self._hits += 1
            return self.cache[key]
        
        self._misses += 1
        return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache."""
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        else:
            # Add new key
            if len(self.cache) >= self.maxsize:
                # Remove least recently used item
                self.cache.popitem(last=False)
        
        self.cache[key] = value
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear the cache."""
        self.cache.clear()
        self._hits = 0
        self._misses = 0
    
    def cache_info(self) -> str:
        """Get cache statistics."""
        return f"LRU Cache - Size: {len(self.cache)}/{self.maxsize}, Hits: {self._hits}, Misses: {self._misses}"

# Step 2 code: LRU cache decorator
def lru_cache_final(maxsize: int = 128):
    """LRU cache decorator."""
    def decorator(func: Callable) -> Callable:
        cache = LRUCache_final(maxsize)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# Step 2 example function
@lru_cache_final(maxsize=50)
def expensive_computation_final(n: int) -> int:
    """Simulate an expensive computation."""
    time.sleep(0.01)  # Simulate work
    return n * n * n

# Step 3 code: TTL Cache implementation
class TTLCache_final:
    """Time To Live cache implementation with automatic expiration."""
    
    def __init__(self, maxsize: int = 128, ttl: float = 300.0):
        """
        Initialize TTL cache.
        
        Args:
            maxsize: Maximum number of items in cache
            ttl: Time to live in seconds (default 5 minutes)
        """
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = {}  # key -> (value, timestamp)
        self.access_order = OrderedDict()  # For LRU behavior when at capacity
        self._hits = 0
        self._misses = 0
        self._lock = threading.Lock()
    
    def _is_expired(self, timestamp: float) -> bool:
        """Check if an entry has expired."""
        return time.time() - timestamp > self.ttl
    
    def _cleanup_expired(self) -> None:
        """Remove expired entries from cache."""
        current_time = time.time()
        expired_keys = [
            key for key, (_, timestamp) in self.cache.items()
            if current_time - timestamp > self.ttl
        ]
        
        for key in expired_keys:
            del self.cache[key]
            if key in self.access_order:
                del self.access_order[key]
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from cache, return None if not found or expired."""
        with self._lock:
            if key not in self.cache:
                self._misses += 1
                return None
            
            value, timestamp = self.cache[key]
            
            if self._is_expired(timestamp):
                # Entry has expired, remove it
                del self.cache[key]
                if key in self.access_order:
                    del self.access_order[key]
                self._misses += 1
                return None
            
            # Update access order for LRU
            self.access_order[key] = True
            self.access_order.move_to_end(key)
            self._hits += 1
            return value
    
    def put(self, key: Any, value: Any) -> None:
        """Put key-value pair in cache with current timestamp."""
        with self._lock:
            current_time = time.time()
            
            # Clean up expired entries periodically
            if len(self.cache) > self.maxsize * 0.8:  # Cleanup when 80% full
                self._cleanup_expired()
            
            # If at capacity and key is new, remove LRU item
            if key not in self.cache and len(self.cache) >= self.maxsize:
                if self.access_order:
                    lru_key = next(iter(self.access_order))
                    del self.cache[lru_key]
                    del self.access_order[lru_key]
            
            # Add/update the entry
            self.cache[key] = (value, current_time)
            self.access_order[key] = True
            self.access_order.move_to_end(key)
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear the cache."""
        with self._lock:
            self.cache.clear()
            self.access_order.clear()
            self._hits = 0
            self._misses = 0
    
    def cache_info(self) -> str:
        """Get cache statistics."""
        with self._lock:
            self._cleanup_expired()  # Clean up before reporting
            return f"TTL Cache - Size: {len(self.cache)}/{self.maxsize}, TTL: {self.ttl}s, Hits: {self._hits}, Misses: {self._misses}"

# Step 3 code: TTL cache decorator
def ttl_cache_final(maxsize: int = 128, ttl: float = 300.0):
    """TTL cache decorator with automatic expiration."""
    def decorator(func: Callable) -> Callable:
        cache = TTLCache_final(maxsize, ttl)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# Step 3 example functions
@ttl_cache_final(maxsize=100, ttl=2.0)  # 2 second TTL for demo
def time_sensitive_computation_final(n: int) -> str:
    """Computation that should expire after 2 seconds."""
    current_time = time.strftime("%H:%M:%S")
    return f"Result for {n} computed at {current_time}"

@ttl_cache_final(maxsize=50, ttl=5.0)  # 5 second TTL
def weather_data_final(city: str) -> dict:
    """Simulate fetching weather data that expires after 5 seconds."""
    time.sleep(0.1)  # Simulate API call
    return {
        "city": city,
        "temperature": 20 + hash(city) % 15,  # Fake temperature
        "timestamp": time.time()
    }

# Step 4 code: Multi-Level Cache System
class MultiLevelCache_final:
    """Multi-level cache system combining different caching strategies."""
    
    def __init__(self, 
                 l1_maxsize: int = 50,     # Fast, small cache
                 l2_maxsize: int = 200,    # Medium cache with LRU
                 l3_maxsize: int = 1000,   # Large cache with TTL
                 l3_ttl: float = 3600.0):  # 1 hour TTL for L3
        """
        Initialize multi-level cache system.
        
        L1: Small, fast in-memory cache (dict)
        L2: Medium LRU cache
        L3: Large TTL cache with expiration
        """
        # Level 1: Fast dictionary cache (most recently accessed)
        self.l1_cache = {}
        self.l1_maxsize = l1_maxsize
        self.l1_access_order = []
        
        # Level 2: LRU cache
        self.l2_cache = LRUCache_final(l2_maxsize)
        
        # Level 3: TTL cache
        self.l3_cache = TTLCache_final(l3_maxsize, l3_ttl)
        
        # Statistics
        self.l1_hits = 0
        self.l2_hits = 0
        self.l3_hits = 0
        self.misses = 0
        self._lock = threading.Lock()
    
    def _promote_to_l1(self, key: Any, value: Any) -> None:
        """Promote a value to L1 cache."""
        if len(self.l1_cache) >= self.l1_maxsize:
            # Remove least recently accessed item
            if self.l1_access_order:
                old_key = self.l1_access_order.pop(0)
                if old_key in self.l1_cache:
                    del self.l1_cache[old_key]
        
        self.l1_cache[key] = value
        if key in self.l1_access_order:
            self.l1_access_order.remove(key)
        self.l1_access_order.append(key)
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value from multi-level cache."""
        with self._lock:
            # Try L1 cache first (fastest)
            if key in self.l1_cache:
                # Update access order
                if key in self.l1_access_order:
                    self.l1_access_order.remove(key)
                self.l1_access_order.append(key)
                self.l1_hits += 1
                return self.l1_cache[key]
            
            # Try L2 cache (LRU)
            value = self.l2_cache.get(key)
            if value is not None:
                self.l2_hits += 1
                # Promote to L1
                self._promote_to_l1(key, value)
                return value
            
            # Try L3 cache (TTL)
            value = self.l3_cache.get(key)
            if value is not None:
                self.l3_hits += 1
                # Promote to L2 and L1
                self.l2_cache.put(key, value)
                self._promote_to_l1(key, value)
                return value
            
            # Cache miss
            self.misses += 1
            return None
    
    def put(self, key: Any, value: Any) -> None:
        """Put value in multi-level cache."""
        with self._lock:
            # Store in all levels
            self._promote_to_l1(key, value)
            self.l2_cache.put(key, value)
            self.l3_cache.put(key, value)
    
    def get_or_compute(self, key: Any, compute_func: Callable, *args, **kwargs) -> Any:
        """Get value from cache or compute and cache it."""
        value = self.get(key)
        if value is not None:
            return value
        
        # Compute value and cache it
        value = compute_func(*args, **kwargs)
        self.put(key, value)
        return value
    
    def clear(self) -> None:
        """Clear all cache levels."""
        with self._lock:
            self.l1_cache.clear()
            self.l1_access_order.clear()
            self.l2_cache.clear()
            self.l3_cache.clear()
            self.l1_hits = 0
            self.l2_hits = 0
            self.l3_hits = 0
            self.misses = 0
    
    def cache_info(self) -> str:
        """Get comprehensive cache statistics."""
        with self._lock:
            total_requests = self.l1_hits + self.l2_hits + self.l3_hits + self.misses
            hit_rate = ((self.l1_hits + self.l2_hits + self.l3_hits) / total_requests * 100) if total_requests > 0 else 0
            
            return (f"Multi-Level Cache Stats:\n"
                   f"  L1: {len(self.l1_cache)}/{self.l1_maxsize} items, {self.l1_hits} hits\n"
                   f"  L2: {self.l2_cache.cache_info()}\n"
                   f"  L3: {self.l3_cache.cache_info()}\n"
                   f"  Total: {self.l1_hits + self.l2_hits + self.l3_hits} hits, {self.misses} misses\n"
                   f"  Hit Rate: {hit_rate:.1f}%")

# Step 4 code: Multi-level cache decorator
def multi_level_cache_final(l1_maxsize: int = 50, l2_maxsize: int = 200, 
                           l3_maxsize: int = 1000, l3_ttl: float = 3600.0):
    """Multi-level cache decorator."""
    def decorator(func: Callable) -> Callable:
        cache = MultiLevelCache_final(l1_maxsize, l2_maxsize, l3_maxsize, l3_ttl)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create key from arguments
            try:
                key = args
                if kwargs:
                    key += tuple(sorted(kwargs.items()))
            except TypeError:
                key = str(args) + str(sorted(kwargs.items()))
            
            return cache.get_or_compute(key, func, *args, **kwargs)
        
        wrapper.cache_info = cache.cache_info
        wrapper.cache_clear = cache.clear
        wrapper.cache = cache
        
        return wrapper
    return decorator

# Step 4 example functions
@multi_level_cache_final(l1_maxsize=10, l2_maxsize=50, l3_maxsize=200, l3_ttl=60.0)
def complex_computation_final(n: int, operation: str = "square") -> int:
    """Complex computation with multi-level caching."""
    time.sleep(0.05)  # Simulate expensive computation
    
    if operation == "square":
        return n * n
    elif operation == "cube":
        return n * n * n
    elif operation == "factorial":
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    else:
        return n

@multi_level_cache_final(l1_maxsize=5, l2_maxsize=20, l3_maxsize=100, l3_ttl=30.0)
def database_query_simulation_final(table: str, id: int) -> dict:
    """Simulate database query with multi-level caching."""
    time.sleep(0.1)  # Simulate database latency
    return {
        "table": table,
        "id": id,
        "data": f"Record {id} from {table}",
        "timestamp": time.time()
    }

# New in Step 5: Performance Benchmark Functions
def benchmark_cache_performance():
    """Comprehensive benchmark comparing different caching strategies."""
    print("=== Performance Benchmark: Cache Strategies Comparison ===")
    
    # Test functions without caching
    def slow_fibonacci(n):
        if n < 2:
            return n
        return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    
    def slow_computation(n):
        time.sleep(0.001)  # Simulate work
        return n * n * n
    
    # Test functions with different caching strategies
    @memoize_final
    def memoized_fibonacci(n):
        if n < 2:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    
    @lru_cache_final(maxsize=100)
    def lru_computation(n):
        time.sleep(0.001)
        return n * n * n
    
    @ttl_cache_final(maxsize=100, ttl=60.0)
    def ttl_computation(n):
        time.sleep(0.001)
        return n * n * n
    
    @multi_level_cache_final(l1_maxsize=10, l2_maxsize=50, l3_maxsize=100)
    def multilevel_computation(n):
        time.sleep(0.001)
        return n * n * n
    
    # Benchmark 1: Fibonacci computation
    print("Benchmark 1: Fibonacci Computation")
    print("-" * 40)
    
    # Without caching
    start_time = time.time()
    result = slow_fibonacci(25)
    no_cache_time = time.time() - start_time
    print(f"No cache: fibonacci(25) = {result}, Time: {no_cache_time:.4f}s")
    
    # With memoization
    start_time = time.time()
    result = memoized_fibonacci(25)
    memo_time = time.time() - start_time
    print(f"Memoized: fibonacci(25) = {result}, Time: {memo_time:.4f}s")
    print(f"Speedup: {no_cache_time / memo_time:.1f}x faster")
    print()
    
    # Benchmark 2: Repeated computations with different cache strategies
    print("Benchmark 2: Repeated Computations (1000 calls, 50 unique values)")
    print("-" * 70)
    
    test_values = [random.randint(1, 50) for _ in range(1000)]
    
    # No cache
    start_time = time.time()
    for val in test_values:
        slow_computation(val)
    no_cache_time = time.time() - start_time
    print(f"No cache: {no_cache_time:.4f}s")
    
    # LRU cache
    start_time = time.time()
    for val in test_values:
        lru_computation(val)
    lru_time = time.time() - start_time
    print(f"LRU cache: {lru_time:.4f}s (speedup: {no_cache_time / lru_time:.1f}x)")
    print(f"LRU stats: {lru_computation.cache_info()}")
    
    # TTL cache
    start_time = time.time()
    for val in test_values:
        ttl_computation(val)
    ttl_time = time.time() - start_time
    print(f"TTL cache: {ttl_time:.4f}s (speedup: {no_cache_time / ttl_time:.1f}x)")
    print(f"TTL stats: {ttl_computation.cache_info()}")
    
    # Multi-level cache
    start_time = time.time()
    for val in test_values:
        multilevel_computation(val)
    multilevel_time = time.time() - start_time
    print(f"Multi-level: {multilevel_time:.4f}s (speedup: {no_cache_time / multilevel_time:.1f}x)")
    print(f"Multi-level stats:\n{multilevel_computation.cache_info()}")
    print()

# New in Step 5: Real-world examples
class WebAPICache:
    """Real-world example: Web API response caching."""
    
    def __init__(self):
        self.cache = TTLCache_final(maxsize=1000, ttl=300.0)  # 5 minute TTL
        self.request_count = 0
    
    def fetch_user_data(self, user_id: int) -> dict:
        """Simulate fetching user data from external API."""
        cached_data = self.cache.get(f"user_{user_id}")
        if cached_data is not None:
            return cached_data
        
        # Simulate API call
        self.request_count += 1
        time.sleep(0.1)  # Simulate network latency
        
        user_data = {
            "id": user_id,
            "name": f"User {user_id}",
            "email": f"user{user_id}@example.com",
            "last_login": time.time()
        }
        
        self.cache.put(f"user_{user_id}", user_data)
        return user_data
    
    def get_stats(self) -> str:
        return f"API calls made: {self.request_count}, {self.cache.cache_info()}"

class DatabaseQueryCache:
    """Real-world example: Database query result caching."""
    
    def __init__(self):
        self.cache = MultiLevelCache_final(
            l1_maxsize=20,    # Hot data
            l2_maxsize=100,   # Warm data
            l3_maxsize=500,   # Cold data
            l3_ttl=1800.0     # 30 minute TTL
        )
        self.query_count = 0
    
    def execute_query(self, table: str, conditions: dict) -> list:
        """Simulate database query execution."""
        # Create cache key from query parameters
        key = f"{table}_{hash(str(sorted(conditions.items())))}"
        
        cached_result = self.cache.get(key)
        if cached_result is not None:
            return cached_result
        
        # Simulate database query
        self.query_count += 1
        time.sleep(0.05)  # Simulate query execution time
        
        # Mock result based on conditions
        result = [
            {"id": i, "data": f"Record {i} from {table}"}
            for i in range(1, random.randint(5, 20))
        ]
        
        self.cache.put(key, result)
        return result
    
    def get_stats(self) -> str:
        return f"DB queries executed: {self.query_count}\n{self.cache.cache_info()}"

def demo_step5():
    """Demonstrate all steps plus performance benchmarks and real-world examples."""
    print("=== Step 5: Performance Benchmarks and Real-World Examples ===")
    
    # Demo all previous steps functionality
    print("Quick demo of all previous steps:")
    print("Step 1 - Basic Memoization:")
    result = fibonacci_final(20)
    print(f"fibonacci_final(20) = {result}")
    
    print("\nStep 2 - LRU Cache:")
    for i in range(5):
        expensive_computation_final(i)
    print(f"LRU cache info: {expensive_computation_final.cache_info()}")
    
    print("\nStep 3 - TTL Cache:")
    result = time_sensitive_computation_final(42)
    print(f"TTL result: {result}")
    
    print("\nStep 4 - Multi-Level Cache:")
    result = complex_computation_final(10, "factorial")
    print(f"Multi-level result: {result}")
    print()
    
    # Run performance benchmarks
    benchmark_cache_performance()
    
    # Real-world examples
    print("=== Real-World Examples ===")
    
    # Web API caching example
    print("Example 1: Web API Response Caching")
    print("-" * 40)
    api_cache = WebAPICache()
    
    # Simulate multiple requests for same users
    user_ids = [1, 2, 3, 1, 2, 4, 1, 3, 5, 1]
    
    start_time = time.time()
    for user_id in user_ids:
        user_data = api_cache.fetch_user_data(user_id)
        print(f"User {user_id}: {user_data['name']}")
    
    api_time = time.time() - start_time
    print(f"Total time: {api_time:.4f}s")
    print(f"API stats: {api_cache.get_stats()}")
    print()
    
    # Database query caching example
    print("Example 2: Database Query Result Caching")
    print("-" * 45)
    db_cache = DatabaseQueryCache()
    
    # Simulate various database queries
    queries = [
        ("users", {"status": "active"}),
        ("orders", {"date": "2025-01-01"}),
        ("products", {"category": "electronics"}),
        ("users", {"status": "active"}),  # Repeat
        ("orders", {"date": "2025-01-02"}),
        ("users", {"status": "active"}),  # Repeat
        ("products", {"category": "books"}),
        ("orders", {"date": "2025-01-01"}),  # Repeat
    ]
    
    start_time = time.time()
    for table, conditions in queries:
        results = db_cache.execute_query(table, conditions)
        print(f"Query {table} with {conditions}: {len(results)} results")
    
    db_time = time.time() - start_time
    print(f"Total time: {db_time:.4f}s")
    print(f"DB stats: {db_cache.get_stats()}")
    print()
    
    # Cache strategy recommendations
    print("=== Cache Strategy Recommendations ===")
    print("1. Use basic memoization for:")
    print("   - Pure functions with expensive computations")
    print("   - Recursive algorithms (like Fibonacci)")
    print("   - Mathematical calculations")
    print()
    print("2. Use LRU cache for:")
    print("   - Limited memory scenarios")
    print("   - When you need to control cache size")
    print("   - Frequently accessed recent data")
    print()
    print("3. Use TTL cache for:")
    print("   - Time-sensitive data (API responses, weather)")
    print("   - Data that becomes stale over time")
    print("   - External service responses")
    print()
    print("4. Use multi-level cache for:")
    print("   - Complex applications with varied access patterns")
    print("   - When you need both speed and capacity")
    print("   - High-performance systems")
    print()

if __name__ == "__main__":
    demo_step1()
    demo_step2()
    demo_step3()
    demo_step4()
    demo_step5()