"""Question: Implement a class ThreadSafeSingleton using threading to ensure
thread-safe singleton behavior.
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
# - What are race conditions? (multiple threads accessing shared resources)
# - What is threading.Lock()? (mechanism to prevent concurrent access)
# - Where should you use the lock? (around the instance creation check)
# - Why is thread safety important for singletons?
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


# Step 1: Import threading and understand the problem
# ===============================================================================

# Explanation:
# In multi-threaded environments, regular singleton implementations can fail.
# Multiple threads might simultaneously check if an instance exists and create multiple instances.

import threading
import time

print("Step 1: Understanding thread safety issues")

# What we accomplished in this step:
# - Imported necessary threading module
# - Identified the thread safety problem


# Step 2: Create basic ThreadSafeSingleton class structure
# ===============================================================================

# Explanation:
# Let's start with the basic structure including a class attribute for the instance
# and a threading lock to control access.

import threading
import time

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

print("Step 2: Basic ThreadSafeSingleton structure created")

# What we accomplished in this step:
# - Created class with instance storage and lock


# Step 3: Implement thread-safe __new__ method
# ===============================================================================

# Explanation:
# The __new__ method controls object creation. We use a lock to ensure only one thread
# can check and create the instance at a time.

import threading
import time

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # Double-checked locking pattern
        if cls._instance is None:
            with cls._lock:
                # Check again inside the lock
                if cls._instance is None:
                    print(f"Creating new instance in thread {threading.current_thread().name}")
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

print("Step 3: Thread-safe __new__ method implemented")

# What we accomplished in this step:
# - Implemented double-checked locking pattern
# - Added thread identification for testing


# Step 4: Add initialization with thread safety
# ===============================================================================

# Explanation:
# We need to ensure that __init__ is only called once, even in multi-threaded environments.
# We'll use a flag to track initialization.

import threading
import time

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print(f"Creating new instance in thread {threading.current_thread().name}")
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not ThreadSafeSingleton._initialized:
            with ThreadSafeSingleton._lock:
                if not ThreadSafeSingleton._initialized:
                    print(f"Initializing instance in thread {threading.current_thread().name}")
                    self.value = None
                    self.created_at = time.time()
                    ThreadSafeSingleton._initialized = True

print("Step 4: Thread-safe initialization added")

# What we accomplished in this step:
# - Added thread-safe initialization
# - Prevented multiple initialization calls


# Step 5: Add useful methods and properties
# ===============================================================================

# Explanation:
# Let's add some methods to make our singleton more useful and demonstrate
# that state is shared across all "instances".

import threading
import time

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print(f"Creating new instance in thread {threading.current_thread().name}")
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not ThreadSafeSingleton._initialized:
            with ThreadSafeSingleton._lock:
                if not ThreadSafeSingleton._initialized:
                    print(f"Initializing instance in thread {threading.current_thread().name}")
                    self.value = None
                    self.created_at = time.time()
                    self.access_count = 0
                    ThreadSafeSingleton._initialized = True

    def set_value(self, value):
        with ThreadSafeSingleton._lock:
            self.value = value

    def get_value(self):
        with ThreadSafeSingleton._lock:
            self.access_count += 1
            return self.value

    def get_info(self):
        with ThreadSafeSingleton._lock:
            return {
                'id': id(self),
                'value': self.value,
                'created_at': self.created_at,
                'access_count': self.access_count,
                'thread': threading.current_thread().name
            }

print("Step 5: Added useful methods with thread safety")

# What we accomplished in this step:
# - Added thread-safe methods for value manipulation
# - Added access counting and information retrieval


# Step 6: Create test functions for multi-threading
# ===============================================================================

# Explanation:
# Let's create functions to test our thread-safe singleton in a multi-threaded environment.

import threading
import time
import random

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print(f"Creating new instance in thread {threading.current_thread().name}")
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not ThreadSafeSingleton._initialized:
            with ThreadSafeSingleton._lock:
                if not ThreadSafeSingleton._initialized:
                    print(f"Initializing instance in thread {threading.current_thread().name}")
                    self.value = None
                    self.created_at = time.time()
                    self.access_count = 0
                    ThreadSafeSingleton._initialized = True

    def set_value(self, value):
        with ThreadSafeSingleton._lock:
            self.value = value

    def get_value(self):
        with ThreadSafeSingleton._lock:
            self.access_count += 1
            return self.value

    def get_info(self):
        with ThreadSafeSingleton._lock:
            return {
                'id': id(self),
                'value': self.value,
                'created_at': self.created_at,
                'access_count': self.access_count,
                'thread': threading.current_thread().name
            }

def create_and_test_singleton(thread_id):
    """Function to be run in multiple threads"""
    print(f"Thread {thread_id} starting...")
    
    # Simulate some work before creating singleton
    time.sleep(random.uniform(0.01, 0.1))
    
    # Create singleton instance
    singleton = ThreadSafeSingleton()
    
    # Test setting and getting values
    singleton.set_value(f"Value from thread {thread_id}")
    time.sleep(0.01)  # Small delay
    
    value = singleton.get_value()
    info = singleton.get_info()
    
    print(f"Thread {thread_id} - Instance ID: {info['id']}, Value: {value}")
    return singleton

print("Step 6: Test functions created")

# What we accomplished in this step:
# - Created test function for multi-threaded testing
# - Added random delays to simulate real-world conditions


# Step 7: Test the thread-safe singleton
# ===============================================================================

# Explanation:
# Finally, let's test our thread-safe singleton with multiple threads to verify
# that only one instance is created and shared properly.

import threading
import time
import random

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print(f"Creating new instance in thread {threading.current_thread().name}")
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not ThreadSafeSingleton._initialized:
            with ThreadSafeSingleton._lock:
                if not ThreadSafeSingleton._initialized:
                    print(f"Initializing instance in thread {threading.current_thread().name}")
                    self.value = None
                    self.created_at = time.time()
                    self.access_count = 0
                    ThreadSafeSingleton._initialized = True

    def set_value(self, value):
        with ThreadSafeSingleton._lock:
            self.value = value

    def get_value(self):
        with ThreadSafeSingleton._lock:
            self.access_count += 1
            return self.value

    def get_info(self):
        with ThreadSafeSingleton._lock:
            return {
                'id': id(self),
                'value': self.value,
                'created_at': self.created_at,
                'access_count': self.access_count,
                'thread': threading.current_thread().name
            }

def create_and_test_singleton(thread_id):
    print(f"Thread {thread_id} starting...")
    time.sleep(random.uniform(0.01, 0.1))
    
    singleton = ThreadSafeSingleton()
    singleton.set_value(f"Value from thread {thread_id}")
    time.sleep(0.01)
    
    value = singleton.get_value()
    info = singleton.get_info()
    print(f"Thread {thread_id} - Instance ID: {info['id']}, Value: {value}")
    return singleton

# Test our thread-safe singleton:
print("Testing ThreadSafeSingleton with multiple threads:")

# Create and start multiple threads
threads = []
results = []

def thread_worker(thread_id, results_list):
    result = create_and_test_singleton(thread_id)
    results_list.append(result)

# Start 5 threads simultaneously
for i in range(5):
    thread = threading.Thread(target=thread_worker, args=(i, results))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Verify all instances are the same
print(f"\nVerification:")
print(f"Number of results: {len(results)}")
first_instance_id = id(results[0])
all_same = all(id(instance) == first_instance_id for instance in results)
print(f"All instances are the same object: {all_same}")

# Get final state
final_singleton = ThreadSafeSingleton()
final_info = final_singleton.get_info()
print(f"Final singleton info: {final_info}")

# What we accomplished in this step:
# - Created and tested our complete thread-safe singleton
# - Verified that only one instance exists across multiple threads
# - Demonstrated shared state in multi-threaded environment


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Thread safety and race conditions
# - Double-checked locking pattern
# - Threading locks and synchronization
# - Multi-threaded singleton implementation
# - Thread-safe method design
# - Testing concurrent code
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding performance monitoring or different locking strategies!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================