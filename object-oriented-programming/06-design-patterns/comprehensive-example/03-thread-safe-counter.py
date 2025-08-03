"""Question: Create a class ThreadSafeCounter that uses threading to ensure
thread-safe increment and decrement operations.
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
# - What is thread safety and why is it important?
# - How do you use threading.Lock() to protect shared resources?
# - What operations need to be protected in a counter?
# - How do you use the 'with' statement for automatic lock management?
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


# Step 1: Import threading and define the ThreadSafeCounter class
# ===============================================================================

# Explanation:
# Let's start by importing the threading module and creating our ThreadSafeCounter class.
# We need threading to create locks that will protect our counter from race conditions.

import threading

class ThreadSafeCounter:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Imported the threading module
# - Created the basic ThreadSafeCounter class structure


# Step 2: Add the constructor
# ===============================================================================

# Explanation:
# The constructor should initialize the counter value and create a lock object
# that will be used to synchronize access to the counter.

import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

# What we accomplished in this step:
# - Initialized counter value to 0
# - Created a Lock object to protect the counter value


# Step 3: Add the increment method
# ===============================================================================

# Explanation:
# The increment method should increase the counter value by 1. We use the lock
# to ensure that only one thread can modify the value at a time.

import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

# What we accomplished in this step:
# - Added increment method that safely increases the counter
# - Used 'with' statement for automatic lock acquisition and release


# Step 4: Add the decrement method
# ===============================================================================

# Explanation:
# The decrement method should decrease the counter value by 1. Like increment,
# it needs to be protected by the lock.

import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

    def decrement(self):
        with self._lock:
            self.value -= 1

# What we accomplished in this step:
# - Added decrement method that safely decreases the counter
# - Used the same lock to ensure thread safety


# Step 5: Add the get_value method
# ===============================================================================

# Explanation:
# The get_value method should return the current counter value. Even reading
# should be protected to ensure we get a consistent value.

import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

    def decrement(self):
        with self._lock:
            self.value -= 1

    def get_value(self):
        with self._lock:
            return self.value

# What we accomplished in this step:
# - Added get_value method that safely reads the counter value
# - Protected read operations with the same lock


# Step 6: Test our ThreadSafeCounter with multiple threads
# ===============================================================================

# Explanation:
# Now let's test our ThreadSafeCounter by creating multiple threads that
# increment the counter simultaneously. This will demonstrate thread safety.

import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

    def decrement(self):
        with self._lock:
            self.value -= 1

    def get_value(self):
        with self._lock:
            return self.value

# Test our ThreadSafeCounter:
print("=== Testing ThreadSafeCounter ===")
counter = ThreadSafeCounter()

def increment_counter():
    for _ in range(1000):
        counter.increment()

# Create and start multiple threads
print("Creating 10 threads, each incrementing 1000 times...")
threads = [threading.Thread(target=increment_counter) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter.get_value()}")
print("Expected: 10000 (10 threads × 1000 increments)")

# What we accomplished in this step:
# - Created multiple threads that increment the counter simultaneously
# - Demonstrated that the final result is correct due to thread safety
# - Showed how to properly start and join threads


# Step 7: Enhanced version with more operations and statistics
# ===============================================================================

# Explanation:
# Let's create an enhanced version that includes more operations and keeps
# statistics about thread usage.

import threading
import time

class EnhancedThreadSafeCounter:
    def __init__(self, initial_value=0):
        self.value = initial_value
        self._lock = threading.Lock()
        self.operation_count = 0
        self.thread_ids = set()

    def increment(self, amount=1):
        with self._lock:
            self.value += amount
            self.operation_count += 1
            self.thread_ids.add(threading.current_thread().ident)

    def decrement(self, amount=1):
        with self._lock:
            self.value -= amount
            self.operation_count += 1
            self.thread_ids.add(threading.current_thread().ident)

    def get_value(self):
        with self._lock:
            return self.value

    def reset(self, new_value=0):
        with self._lock:
            old_value = self.value
            self.value = new_value
            self.operation_count += 1
            self.thread_ids.add(threading.current_thread().ident)
            return old_value

    def get_statistics(self):
        with self._lock:
            return {
                'current_value': self.value,
                'total_operations': self.operation_count,
                'unique_threads': len(self.thread_ids),
                'thread_ids': list(self.thread_ids)
            }

# Test enhanced version:
print("\n=== Enhanced ThreadSafeCounter with Statistics ===")

enhanced_counter = EnhancedThreadSafeCounter(100)

def worker_increment(worker_id, iterations):
    for i in range(iterations):
        enhanced_counter.increment()
        if i % 100 == 0:
            time.sleep(0.001)  # Small delay to encourage thread switching

def worker_decrement(worker_id, iterations):
    for i in range(iterations):
        enhanced_counter.decrement()
        if i % 100 == 0:
            time.sleep(0.001)

# Create mixed workload
print("Creating mixed workload with increment and decrement operations...")
threads = []

# 3 threads incrementing
for i in range(3):
    t = threading.Thread(target=worker_increment, args=(f"inc_{i}", 500))
    threads.append(t)

# 2 threads decrementing
for i in range(2):
    t = threading.Thread(target=worker_decrement, args=(f"dec_{i}", 300))
    threads.append(t)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Display results
stats = enhanced_counter.get_statistics()
print(f"\nFinal Results:")
print(f"Counter value: {stats['current_value']}")
print(f"Expected: 100 + (3×500) - (2×300) = 100 + 1500 - 600 = 1000")
print(f"Total operations: {stats['total_operations']}")
print(f"Unique threads used: {stats['unique_threads']}")

# What we accomplished in this step:
# - Enhanced the counter with more operations and statistics
# - Added operation counting and thread tracking
# - Demonstrated mixed workloads with multiple thread types
# - Showed how to track which threads accessed the counter


# Step 8: Demonstration of race conditions without locks
# ===============================================================================

# Explanation:
# Let's demonstrate what happens when we don't use locks by creating an
# unsafe counter and comparing the results.

class UnsafeCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        # No lock - this is unsafe!
        temp = self.value
        time.sleep(0.0001)  # Simulate some processing time
        self.value = temp + 1

    def get_value(self):
        return self.value

# Compare safe vs unsafe:
print("\n=== Comparing Safe vs Unsafe Counter ===")

# Test unsafe counter
unsafe_counter = UnsafeCounter()

def unsafe_increment():
    for _ in range(100):
        unsafe_counter.increment()

print("Testing unsafe counter with race conditions...")
unsafe_threads = [threading.Thread(target=unsafe_increment) for _ in range(5)]

for thread in unsafe_threads:
    thread.start()
for thread in unsafe_threads:
    thread.join()

print(f"Unsafe counter result: {unsafe_counter.get_value()}")
print(f"Expected: 500 (5 threads × 100 increments)")
print("Notice: The unsafe counter likely shows a value less than 500 due to race conditions!")

# Test safe counter for comparison
safe_counter = ThreadSafeCounter()

def safe_increment():
    for _ in range(100):
        safe_counter.increment()

print("\nTesting safe counter...")
safe_threads = [threading.Thread(target=safe_increment) for _ in range(5)]

for thread in safe_threads:
    thread.start()
for thread in safe_threads:
    thread.join()

print(f"Safe counter result: {safe_counter.get_value()}")
print(f"Expected: 500 (5 threads × 100 increments)")
print("Notice: The safe counter shows exactly 500 due to proper synchronization!")

# What we accomplished in this step:
# - Demonstrated the importance of thread safety
# - Showed what happens when locks are not used (race conditions)
# - Compared safe vs unsafe implementations
# - Highlighted the value of proper synchronization


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding thread safety and race conditions
# - Using threading.Lock() for synchronization
# - Protecting shared resources with locks
# - Using 'with' statement for automatic lock management
# - Creating thread-safe classes and methods
# - Comparing safe vs unsafe implementations
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding atomic operations!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
