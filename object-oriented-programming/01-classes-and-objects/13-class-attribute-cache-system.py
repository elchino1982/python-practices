"""Question: Define a class Cache with a private class attribute _cache
to store cached values. Use class methods to add, retrieve, and clear cache entries.
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
# - What is a cache? (temporary storage for frequently accessed data)
# - Why use class methods for cache operations? (shared across all instances)
# - What data structure should store cache entries? (dictionary)
# - How do you handle missing keys? (return None or default value)
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


# Step 1: Define the Cache class with private class attribute
# ===============================================================================

# Explanation:
# Let's start by creating our Cache class with a private class attribute to store cached data.
# Using a class attribute means the cache is shared across all instances.

class Cache:
    _cache = {}

# What we accomplished in this step:
# - Created Cache class with private class attribute _cache


# Step 2: Add class method to add cache entries
# ===============================================================================

# Explanation:
# Class methods take 'cls' as the first parameter and can access class attributes.
# The add method stores key-value pairs in our cache.

class Cache:
    _cache = {}

    @classmethod
    def add(cls, key, value):
        cls._cache[key] = value

# What we accomplished in this step:
# - Added class method to add entries to the cache


# Step 3: Add class method to retrieve cache entries
# ===============================================================================

# Explanation:
# The get method retrieves values from the cache. We use dict.get() to safely
# handle missing keys by returning None instead of raising an exception.

class Cache:
    _cache = {}

    @classmethod
    def add(cls, key, value):
        cls._cache[key] = value

    @classmethod
    def get(cls, key):
        return cls._cache.get(key, None)

# What we accomplished in this step:
# - Added class method to retrieve cache entries safely


# Step 4: Add class method to clear cache
# ===============================================================================

# Explanation:
# The clear method removes all entries from the cache. This is useful for
# cache invalidation or memory management.

class Cache:
    _cache = {}

    @classmethod
    def add(cls, key, value):
        cls._cache[key] = value

    @classmethod
    def get(cls, key):
        return cls._cache.get(key, None)

    @classmethod
    def clear(cls):
        cls._cache.clear()

# What we accomplished in this step:
# - Added class method to clear all cache entries


# Step 5: Add additional cache management methods
# ===============================================================================

# Explanation:
# Let's add more functionality to make our cache more complete, including
# methods to check existence, remove specific entries, and get cache statistics.

class Cache:
    _cache = {}

    @classmethod
    def add(cls, key, value):
        cls._cache[key] = value

    @classmethod
    def get(cls, key, default=None):
        return cls._cache.get(key, default)

    @classmethod
    def remove(cls, key):
        if key in cls._cache:
            del cls._cache[key]
            return True
        return False

    @classmethod
    def exists(cls, key):
        return key in cls._cache

    @classmethod
    def clear(cls):
        cls._cache.clear()

    @classmethod
    def size(cls):
        return len(cls._cache)

    @classmethod
    def keys(cls):
        return list(cls._cache.keys())

    @classmethod
    def values(cls):
        return list(cls._cache.values())

    @classmethod
    def items(cls):
        return list(cls._cache.items())

# What we accomplished in this step:
# - Enhanced get method with default parameter
# - Added remove method for specific key deletion
# - Added exists method to check key presence
# - Added size, keys, values, and items methods for cache inspection


# Step 6: Add cache statistics and advanced features
# ===============================================================================

# Explanation:
# Let's add some advanced features like cache statistics and expiration handling
# to make our cache more production-ready.

import time

class Cache:
    _cache = {}
    _stats = {'hits': 0, 'misses': 0, 'adds': 0, 'removes': 0}

    @classmethod
    def add(cls, key, value, ttl=None):
        """Add a value to cache with optional time-to-live"""
        if ttl:
            expiry_time = time.time() + ttl
            cls._cache[key] = {'value': value, 'expiry': expiry_time}
        else:
            cls._cache[key] = {'value': value, 'expiry': None}
        cls._stats['adds'] += 1

    @classmethod
    def get(cls, key, default=None):
        """Get a value from cache, handling expiration"""
        if key in cls._cache:
            entry = cls._cache[key]
            # Check if entry has expired
            if entry['expiry'] and time.time() > entry['expiry']:
                del cls._cache[key]
                cls._stats['misses'] += 1
                return default
            cls._stats['hits'] += 1
            return entry['value']
        cls._stats['misses'] += 1
        return default

    @classmethod
    def remove(cls, key):
        if key in cls._cache:
            del cls._cache[key]
            cls._stats['removes'] += 1
            return True
        return False

    @classmethod
    def exists(cls, key):
        if key in cls._cache:
            entry = cls._cache[key]
            # Check if entry has expired
            if entry['expiry'] and time.time() > entry['expiry']:
                del cls._cache[key]
                return False
            return True
        return False

    @classmethod
    def clear(cls):
        cls._cache.clear()

    @classmethod
    def size(cls):
        return len(cls._cache)

    @classmethod
    def get_stats(cls):
        return cls._stats.copy()

    @classmethod
    def reset_stats(cls):
        cls._stats = {'hits': 0, 'misses': 0, 'adds': 0, 'removes': 0}

# What we accomplished in this step:
# - Added TTL (time-to-live) support for cache entries
# - Added cache statistics tracking
# - Added automatic expiration handling


# Step 7: Test the cache system
# ===============================================================================

# Explanation:
# Finally, let's test our complete cache system to make sure all functionality
# works correctly, including TTL and statistics.

import time

class Cache:
    _cache = {}
    _stats = {'hits': 0, 'misses': 0, 'adds': 0, 'removes': 0}

    @classmethod
    def add(cls, key, value, ttl=None):
        if ttl:
            expiry_time = time.time() + ttl
            cls._cache[key] = {'value': value, 'expiry': expiry_time}
        else:
            cls._cache[key] = {'value': value, 'expiry': None}
        cls._stats['adds'] += 1

    @classmethod
    def get(cls, key, default=None):
        if key in cls._cache:
            entry = cls._cache[key]
            if entry['expiry'] and time.time() > entry['expiry']:
                del cls._cache[key]
                cls._stats['misses'] += 1
                return default
            cls._stats['hits'] += 1
            return entry['value']
        cls._stats['misses'] += 1
        return default

    @classmethod
    def remove(cls, key):
        if key in cls._cache:
            del cls._cache[key]
            cls._stats['removes'] += 1
            return True
        return False

    @classmethod
    def exists(cls, key):
        if key in cls._cache:
            entry = cls._cache[key]
            if entry['expiry'] and time.time() > entry['expiry']:
                del cls._cache[key]
                return False
            return True
        return False

    @classmethod
    def clear(cls):
        cls._cache.clear()

    @classmethod
    def size(cls):
        return len(cls._cache)

    @classmethod
    def get_stats(cls):
        return cls._stats.copy()

    @classmethod
    def reset_stats(cls):
        cls._stats = {'hits': 0, 'misses': 0, 'adds': 0, 'removes': 0}

# Test our cache system:
print("Testing Cache System:")

# Test basic operations
Cache.add("user:1", {"name": "Alice", "age": 30})
Cache.add("user:2", {"name": "Bob", "age": 25})
Cache.add("config", {"theme": "dark", "language": "en"})

print(f"Cache size: {Cache.size()}")
print(f"User 1: {Cache.get('user:1')}")
print(f"User 2: {Cache.get('user:2')}")
print(f"Config: {Cache.get('config')}")

# Test missing key
print(f"Missing key: {Cache.get('user:3', 'Not found')}")

# Test existence check
print(f"User 1 exists: {Cache.exists('user:1')}")
print(f"User 3 exists: {Cache.exists('user:3')}")

# Test TTL functionality
print(f"\nTesting TTL (Time-To-Live):")
Cache.add("temp_data", "This will expire", ttl=2)  # 2 seconds TTL
print(f"Temp data (immediately): {Cache.get('temp_data')}")

print("Waiting 3 seconds for expiration...")
time.sleep(3)
print(f"Temp data (after expiration): {Cache.get('temp_data', 'Expired')}")

# Test statistics
print(f"\nCache statistics: {Cache.get_stats()}")

# Test removal
Cache.remove("user:2")
print(f"After removing user:2, size: {Cache.size()}")
print(f"User 2 after removal: {Cache.get('user:2', 'Not found')}")

# Test clear
Cache.clear()
print(f"After clearing cache, size: {Cache.size()}")

print(f"Final statistics: {Cache.get_stats()}")

# What we accomplished in this step:
# - Created and tested our complete cache system
# - Demonstrated basic operations, TTL, and statistics


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Class-level caching with shared state
# - Class methods for cache operations
# - TTL (time-to-live) implementation
# - Cache statistics and monitoring
# - Automatic expiration handling
# - Production-ready cache features
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding LRU eviction or size limits!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================