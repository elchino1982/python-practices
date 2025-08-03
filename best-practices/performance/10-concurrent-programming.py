"""Question: Implement concurrent programming patterns for improved performance.

Create examples demonstrating threading, multiprocessing, and async programming
to handle CPU-bound and I/O-bound tasks efficiently.

Requirements:
1. Demonstrate threading for I/O-bound tasks
2. Show multiprocessing for CPU-bound tasks
3. Implement async/await for concurrent I/O operations
4. Compare performance of different approaches
5. Show proper synchronization and resource management

Example usage:
    # Threading example
    result = run_io_bound_tasks_threaded(urls)
    
    # Multiprocessing example
    result = run_cpu_bound_tasks_multiprocessing(data)
    
    # Async example
    result = await run_async_io_tasks(urls)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about when to use threading vs multiprocessing vs async
# - Start with simple examples
# - Test your code step by step
# - Consider thread safety and resource sharing
#
# Remember: The best way to learn programming is by doing, not by reading solutions!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)


























# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - When to use threading (I/O-bound tasks)
# - When to use multiprocessing (CPU-bound tasks)
# - When to use async/await (concurrent I/O operations)
# - How to handle shared resources safely
# - Performance measurement and comparison
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


# Step 1: Import modules and create basic task simulation functions
# ===============================================================================

# Explanation:
# We'll start by importing necessary modules and creating functions that simulate
# different types of tasks (I/O-bound and CPU-bound) for demonstration.

import time
import threading
import multiprocessing
import asyncio
import aiohttp
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List, Any
import math

def simulate_io_task(task_id: int, duration: float = 1.0) -> str:
    """Simulate an I/O-bound task (like file reading or network request)."""
    print(f"Starting I/O task {task_id}")
    time.sleep(duration)  # Simulate I/O wait time
    print(f"Completed I/O task {task_id}")
    return f"Result from I/O task {task_id}"

def simulate_cpu_task(n: int) -> int:
    """Simulate a CPU-bound task (like mathematical computation)."""
    print(f"Starting CPU task with n={n}")
    # Calculate factorial to simulate CPU work
    result = math.factorial(n)
    print(f"Completed CPU task with n={n}")
    return result


# Step 2: Sequential execution (baseline for comparison)
# ===============================================================================

# Explanation:
# Before implementing concurrent solutions, let's create sequential versions
# to establish a performance baseline for comparison.

def run_io_tasks_sequential(task_count: int = 5, duration: float = 1.0) -> List[str]:
    """Run I/O tasks sequentially (one after another)."""
    print("=== Running I/O tasks sequentially ===")
    start_time = time.time()
    
    results = []
    for i in range(task_count):
        result = simulate_io_task(i, duration)
        results.append(result)
    
    end_time = time.time()
    print(f"Sequential I/O tasks completed in {end_time - start_time:.2f} seconds")
    return results

def run_cpu_tasks_sequential(numbers: List[int]) -> List[int]:
    """Run CPU tasks sequentially."""
    print("=== Running CPU tasks sequentially ===")
    start_time = time.time()
    
    results = []
    for n in numbers:
        result = simulate_cpu_task(n)
        results.append(result)
    
    end_time = time.time()
    print(f"Sequential CPU tasks completed in {end_time - start_time:.2f} seconds")
    return results


# Step 3: Threading for I/O-bound tasks
# ===============================================================================

# Explanation:
# Threading is ideal for I/O-bound tasks because threads can wait for I/O
# operations while other threads continue working. Python's GIL doesn't
# significantly impact I/O-bound tasks.

def run_io_tasks_threaded(task_count: int = 5, duration: float = 1.0, max_workers: int = 3) -> List[str]:
    """Run I/O tasks using threading."""
    print("=== Running I/O tasks with threading ===")
    start_time = time.time()
    
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks to the thread pool
        future_to_task = {
            executor.submit(simulate_io_task, i, duration): i 
            for i in range(task_count)
        }
        
        # Collect results as they complete
        for future in future_to_task:
            result = future.result()
            results.append(result)
    
    end_time = time.time()
    print(f"Threaded I/O tasks completed in {end_time - start_time:.2f} seconds")
    return results

def run_io_tasks_manual_threading(task_count: int = 5, duration: float = 1.0) -> List[str]:
    """Run I/O tasks using manual thread creation."""
    print("=== Running I/O tasks with manual threading ===")
    start_time = time.time()
    
    results = [None] * task_count
    threads = []
    
    def worker(task_id: int):
        result = simulate_io_task(task_id, duration)
        results[task_id] = result
    
    # Create and start threads
    for i in range(task_count):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"Manual threaded I/O tasks completed in {end_time - start_time:.2f} seconds")
    return results


# Step 4: Multiprocessing for CPU-bound tasks
# ===============================================================================

# Explanation:
# Multiprocessing is ideal for CPU-bound tasks because it bypasses Python's GIL
# by using separate processes. Each process has its own Python interpreter
# and memory space.

def run_cpu_tasks_multiprocessing(numbers: List[int], max_workers: int = None) -> List[int]:
    """Run CPU tasks using multiprocessing."""
    print("=== Running CPU tasks with multiprocessing ===")
    start_time = time.time()
    
    if max_workers is None:
        max_workers = multiprocessing.cpu_count()
    
    results = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks to the process pool
        future_to_number = {
            executor.submit(simulate_cpu_task, n): n 
            for n in numbers
        }
        
        # Collect results as they complete
        for future in future_to_number:
            result = future.result()
            results.append(result)
    
    end_time = time.time()
    print(f"Multiprocessing CPU tasks completed in {end_time - start_time:.2f} seconds")
    return results

def cpu_intensive_function(data: tuple) -> int:
    """CPU-intensive function that can be used with multiprocessing.Pool."""
    start, end = data
    total = 0
    for i in range(start, end):
        total += i * i
    return total

def run_cpu_tasks_with_pool(data_ranges: List[tuple], processes: int = None) -> List[int]:
    """Run CPU tasks using multiprocessing.Pool."""
    print("=== Running CPU tasks with multiprocessing.Pool ===")
    start_time = time.time()
    
    if processes is None:
        processes = multiprocessing.cpu_count()
    
    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.map(cpu_intensive_function, data_ranges)
    
    end_time = time.time()
    print(f"Pool CPU tasks completed in {end_time - start_time:.2f} seconds")
    return results


# Step 5: Async/await for concurrent I/O operations
# ===============================================================================

# Explanation:
# Async/await is excellent for I/O-bound tasks that can be awaited.
# It provides concurrency without the overhead of threads or processes.

async def simulate_async_io_task(task_id: int, duration: float = 1.0) -> str:
    """Simulate an async I/O-bound task."""
    print(f"Starting async I/O task {task_id}")
    await asyncio.sleep(duration)  # Simulate async I/O wait time
    print(f"Completed async I/O task {task_id}")
    return f"Result from async I/O task {task_id}"

async def run_async_io_tasks(task_count: int = 5, duration: float = 1.0) -> List[str]:
    """Run I/O tasks using async/await."""
    print("=== Running I/O tasks with async/await ===")
    start_time = time.time()
    
    # Create all tasks
    tasks = [
        simulate_async_io_task(i, duration) 
        for i in range(task_count)
    ]
    
    # Run all tasks concurrently
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"Async I/O tasks completed in {end_time - start_time:.2f} seconds")
    return results

async def fetch_url_async(session: aiohttp.ClientSession, url: str) -> str:
    """Fetch a URL asynchronously."""
    try:
        async with session.get(url) as response:
            content = await response.text()
            return f"Fetched {len(content)} characters from {url}"
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"

async def run_async_web_requests(urls: List[str]) -> List[str]:
    """Run web requests using async/await."""
    print("=== Running web requests with async/await ===")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"Async web requests completed in {end_time - start_time:.2f} seconds")
    return results


# Step 6: Thread synchronization and shared resources
# ===============================================================================

# Explanation:
# When threads share resources, we need synchronization mechanisms to prevent
# race conditions and ensure thread safety.

class ThreadSafeCounter:
    """A thread-safe counter using locks."""
    
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def get_value(self):
        with self._lock:
            return self._value

def worker_with_shared_counter(counter: ThreadSafeCounter, iterations: int):
    """Worker function that increments a shared counter."""
    for _ in range(iterations):
        counter.increment()
        time.sleep(0.001)  # Simulate some work

def demonstrate_thread_synchronization():
    """Demonstrate thread synchronization with shared resources."""
    print("=== Demonstrating thread synchronization ===")
    
    counter = ThreadSafeCounter()
    threads = []
    iterations_per_thread = 100
    num_threads = 5
    
    start_time = time.time()
    
    # Create and start threads
    for i in range(num_threads):
        thread = threading.Thread(
            target=worker_with_shared_counter, 
            args=(counter, iterations_per_thread)
        )
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    expected_value = num_threads * iterations_per_thread
    actual_value = counter.get_value()
    
    print(f"Expected counter value: {expected_value}")
    print(f"Actual counter value: {actual_value}")
    print(f"Thread synchronization completed in {end_time - start_time:.2f} seconds")
    
    return actual_value == expected_value

class ProducerConsumerExample:
    """Demonstrate producer-consumer pattern with threading."""
    
    def __init__(self, buffer_size: int = 5):
        self.buffer = []
        self.buffer_size = buffer_size
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)
        self.stop_event = threading.Event()
    
    def producer(self, producer_id: int):
        """Producer function that adds items to the buffer."""
        item_count = 0
        while not self.stop_event.is_set():
            with self.not_full:
                while len(self.buffer) >= self.buffer_size and not self.stop_event.is_set():
                    self.not_full.wait()
                
                if self.stop_event.is_set():
                    break
                
                item = f"item-{producer_id}-{item_count}"
                self.buffer.append(item)
                print(f"Producer {producer_id} produced {item}")
                item_count += 1
                self.not_empty.notify()
            
            time.sleep(0.1)  # Simulate production time
    
    def consumer(self, consumer_id: int):
        """Consumer function that removes items from the buffer."""
        while not self.stop_event.is_set():
            with self.not_empty:
                while len(self.buffer) == 0 and not self.stop_event.is_set():
                    self.not_empty.wait()
                
                if self.stop_event.is_set():
                    break
                
                item = self.buffer.pop(0)
                print(f"Consumer {consumer_id} consumed {item}")
                self.not_full.notify()
            
            time.sleep(0.15)  # Simulate consumption time


# Step 7: Performance comparison and demonstration
# ===============================================================================

# Explanation:
# Let's create functions to compare the performance of different approaches
# and demonstrate when to use each concurrency method.

def compare_io_performance():
    """Compare performance of different approaches for I/O-bound tasks."""
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON: I/O-BOUND TASKS")
    print("="*60)
    
    task_count = 5
    duration = 1.0
    
    # Sequential
    sequential_results = run_io_tasks_sequential(task_count, duration)
    print()
    
    # Threading
    threaded_results = run_io_tasks_threaded(task_count, duration)
    print()
    
    # Manual threading
    manual_threaded_results = run_io_tasks_manual_threading(task_count, duration)
    print()
    
    # Async (need to run in event loop)
    async def run_async_comparison():
        return await run_async_io_tasks(task_count, duration)
    
    async_results = asyncio.run(run_async_comparison())
    
    print("\nSummary: For I/O-bound tasks, threading and async provide significant speedup!")

def compare_cpu_performance():
    """Compare performance of different approaches for CPU-bound tasks."""
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON: CPU-BOUND TASKS")
    print("="*60)
    
    # Use smaller numbers to avoid long computation times
    numbers = [8, 9, 10, 11, 12]
    
    # Sequential
    sequential_results = run_cpu_tasks_sequential(numbers)
    print()
    
    # Multiprocessing
    multiprocessing_results = run_cpu_tasks_multiprocessing(numbers)
    print()
    
    # Pool example
    data_ranges = [(0, 100000), (100000, 200000), (200000, 300000), (300000, 400000)]
    pool_results = run_cpu_tasks_with_pool(data_ranges)
    
    print("\nSummary: For CPU-bound tasks, multiprocessing provides significant speedup!")

def demonstrate_producer_consumer():
    """Demonstrate the producer-consumer pattern."""
    print("\n" + "="*60)
    print("PRODUCER-CONSUMER PATTERN DEMONSTRATION")
    print("="*60)
    
    pc_example = ProducerConsumerExample(buffer_size=3)
    
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=pc_example.producer, args=(1,))
    consumer_thread1 = threading.Thread(target=pc_example.consumer, args=(1,))
    consumer_thread2 = threading.Thread(target=pc_example.consumer, args=(2,))
    
    # Start threads
    producer_thread.start()
    consumer_thread1.start()
    consumer_thread2.start()
    
    # Let them run for a few seconds
    time.sleep(3)
    
    # Stop the threads
    pc_example.stop_event.set()
    
    # Wait for threads to finish
    producer_thread.join()
    consumer_thread1.join()
    consumer_thread2.join()
    
    print("Producer-consumer demonstration completed!")

def when_to_use_what():
    """Guidelines for choosing the right concurrency approach."""
    print("\n" + "="*60)
    print("WHEN TO USE WHAT: CONCURRENCY GUIDELINES")
    print("="*60)
    
    guidelines = {
        "Threading": [
            "I/O-bound tasks (file reading, network requests)",
            "Tasks that spend time waiting",
            "When you need shared memory between workers",
            "GUI applications to keep UI responsive"
        ],
        "Multiprocessing": [
            "CPU-bound tasks (mathematical computations)",
            "Tasks that can be parallelized",
            "When you want to utilize multiple CPU cores",
            "When you need true parallelism"
        ],
        "Async/Await": [
            "I/O-bound tasks with async libraries",
            "Web scraping with aiohttp",
            "Database operations with async drivers",
            "High-concurrency network applications"
        ]
    }
    
    for approach, use_cases in guidelines.items():
        print(f"\n{approach}:")
        for use_case in use_cases:
            print(f"  • {use_case}")
    
    print("\nKey Points:")
    print("  • Python's GIL limits threading for CPU-bound tasks")
    print("  • Multiprocessing has higher overhead but true parallelism")
    print("  • Async is very efficient for I/O-bound tasks")
    print("  • Choose based on your specific use case!")

def demonstrate_all_examples():
    """Run all demonstration examples."""
    print("CONCURRENT PROGRAMMING DEMONSTRATIONS")
    print("="*60)
    
    # I/O performance comparison
    compare_io_performance()
    
    # CPU performance comparison
    compare_cpu_performance()
    
    # Thread synchronization
    print("\n" + "="*60)
    print("THREAD SYNCHRONIZATION DEMONSTRATION")
    print("="*60)
    success = demonstrate_thread_synchronization()
    print(f"Thread synchronization test: {'PASSED' if success else 'FAILED'}")
    
    # Producer-consumer pattern
    demonstrate_producer_consumer()
    
    # Guidelines
    when_to_use_what()


# Step 8: Main execution and testing
# ===============================================================================

# Explanation:
# Finally, let's create a main execution block that demonstrates all the
# concurrent programming concepts we've implemented.

def main():
    """Main function to demonstrate all concurrent programming concepts."""
    print("🚀 CONCURRENT PROGRAMMING IN PYTHON")
    print("="*80)
    print("This demonstration shows different approaches to concurrent programming:")
    print("• Threading for I/O-bound tasks")
    print("• Multiprocessing for CPU-bound tasks") 
    print("• Async/await for concurrent I/O operations")
    print("• Thread synchronization and shared resources")
    print("• Performance comparisons and best practices")
    print("="*80)
    
    try:
        # Run all demonstrations
        demonstrate_all_examples()
        
        print("\n" + "="*80)
        print("✅ ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
        print("="*80)
        
        print("\n📚 KEY TAKEAWAYS:")
        print("1. Use threading for I/O-bound tasks")
        print("2. Use multiprocessing for CPU-bound tasks")
        print("3. Use async/await for high-concurrency I/O")
        print("4. Always consider thread safety with shared resources")
        print("5. Measure performance to choose the best approach")
        
    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        print("Note: Some examples require additional packages (aiohttp, requests)")

# Additional utility functions for specific use cases
def quick_threading_example():
    """Quick example of threading for I/O tasks."""
    print("Quick Threading Example:")
    results = run_io_tasks_threaded(3, 0.5)
    print(f"Results: {results}")

def quick_multiprocessing_example():
    """Quick example of multiprocessing for CPU tasks."""
    print("Quick Multiprocessing Example:")
    results = run_cpu_tasks_multiprocessing([5, 6, 7])
    print(f"Results: {len(results)} factorial calculations completed")

def quick_async_example():
    """Quick example of async programming."""
    async def async_demo():
        print("Quick Async Example:")
        results = await run_async_io_tasks(3, 0.5)
        print(f"Results: {results}")
    
    asyncio.run(async_demo())

# ===============================================================================
#                              EXECUTION BLOCK
# ===============================================================================

if __name__ == "__main__":
    # Run the main demonstration
    main()
    
    print("\n" + "="*80)
    print("🎯 QUICK EXAMPLES (uncomment to run individually)")
    print("="*80)
    
    # Uncomment these lines to run quick examples individually:
    # quick_threading_example()
    # quick_multiprocessing_example() 
    # quick_async_example()
    
    print("\n💡 TIP: Try modifying the parameters in the functions above")
    print("   to see how different configurations affect performance!")

# ===============================================================================
#                           ADDITIONAL RESOURCES
# ===============================================================================

"""
FURTHER READING AND RESOURCES:

1. Python Threading:
   - threading module documentation
   - concurrent.futures.ThreadPoolExecutor
   - Thread synchronization primitives

2. Python Multiprocessing:
   - multiprocessing module documentation
   - concurrent.futures.ProcessPoolExecutor
   - Shared memory and communication

3. Async Programming:
   - asyncio module documentation
   - aiohttp for async HTTP requests
   - async/await syntax and patterns

4. Performance Considerations:
   - Python's Global Interpreter Lock (GIL)
   - When to use each approach
   - Profiling and benchmarking tools

5. Best Practices:
   - Thread safety and race conditions
   - Resource management and cleanup
   - Error handling in concurrent code
   - Testing concurrent applications

Remember: The choice between threading, multiprocessing, and async depends
on your specific use case. Always profile and measure performance!
"""

