"""Question: Implement comprehensive profiling and benchmarking techniques for Python code optimization.

Create a profiling and benchmarking system that can measure performance, identify bottlenecks,
and compare different implementations.

Requirements:
1. Implement basic timing measurements
2. Create memory profiling capabilities
3. Build CPU profiling tools
4. Implement statistical benchmarking
5. Create performance comparison utilities
6. Demonstrate optimization techniques

Example usage:
    profiler = PerformanceProfiler()
    result = profiler.profile_function(my_function, args)
    profiler.generate_report()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what profiling tools you need
# - Start with simple timing measurements
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
# - What timing mechanisms does Python provide?
# - How can you measure memory usage?
# - What statistical measures are important for benchmarking?
# - How do you handle function arguments and return values?
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


# Step 1: Import modules and create basic timing utilities
# ===============================================================================

# Explanation:
# Profiling starts with accurate time measurements. We'll use time.perf_counter()
# for high-resolution timing and create a basic timer context manager.

import time
import functools
import statistics
from typing import Callable, Any, List, Dict, Optional, Tuple
from contextlib import contextmanager

class Timer:
    """Basic timer for measuring execution time."""
    
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
    
    def start(self):
        """Start the timer."""
        self.start_time = time.perf_counter()
    
    def stop(self):
        """Stop the timer and calculate elapsed time."""
        if self.start_time is None:
            raise ValueError("Timer not started")
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        return self.elapsed_time
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

# Example usage of Step 1:
def step1_example():
    """Demonstrate basic timing functionality."""
    print("=== Step 1: Basic Timing ===")
    
    # Using timer manually
    timer = Timer()
    timer.start()
    time.sleep(0.1)  # Simulate work
    elapsed = timer.stop()
    print(f"Manual timing: {elapsed:.4f} seconds")
    
    # Using timer as context manager
    with Timer() as timer:
        time.sleep(0.1)  # Simulate work
    print(f"Context manager timing: {timer.elapsed_time:.4f} seconds")


# Step 2: Add memory profiling capabilities
# ===============================================================================

# Explanation:
# Memory profiling helps identify memory leaks and optimize memory usage.
# We'll use psutil for system memory monitoring and tracemalloc for Python memory tracking.

import psutil
import tracemalloc
import gc

class MemoryProfiler:
    """Memory profiler for tracking memory usage."""
    
    def __init__(self):
        self.start_memory = None
        self.end_memory = None
        self.peak_memory = None
        self.tracemalloc_started = False
    
    def start_memory_tracking(self):
        """Start memory tracking."""
        # Start tracemalloc for detailed Python memory tracking
        if not tracemalloc.is_tracing():
            tracemalloc.start()
            self.tracemalloc_started = True
        
        # Record initial memory usage
        process = psutil.Process()
        self.start_memory = process.memory_info().rss / 1024 / 1024  # MB
        self.peak_memory = self.start_memory
    
    def stop_memory_tracking(self):
        """Stop memory tracking and return memory statistics."""
        process = psutil.Process()
        self.end_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        # Get tracemalloc statistics
        if self.tracemalloc_started and tracemalloc.is_tracing():
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            self.tracemalloc_started = False
            
            return {
                'start_memory_mb': self.start_memory,
                'end_memory_mb': self.end_memory,
                'memory_diff_mb': self.end_memory - self.start_memory,
                'peak_memory_mb': peak / 1024 / 1024,
                'current_traced_mb': current / 1024 / 1024
            }
        
        return {
            'start_memory_mb': self.start_memory,
            'end_memory_mb': self.end_memory,
            'memory_diff_mb': self.end_memory - self.start_memory
        }
    
    def __enter__(self):
        self.start_memory_tracking()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.memory_stats = self.stop_memory_tracking()
        return False

# Example usage of Step 2:
def step2_example():
    """Demonstrate memory profiling functionality."""
    print("\n=== Step 2: Memory Profiling ===")
    
    # Memory profiling with context manager
    with MemoryProfiler() as profiler:
        # Create some data to consume memory
        data = [i ** 2 for i in range(100000)]
        more_data = {str(i): i * 2 for i in range(50000)}
    
    memory_stats = profiler.memory_stats
    print(f"Memory usage: {memory_stats['memory_diff_mb']:.2f} MB")
    if 'peak_memory_mb' in memory_stats:
        print(f"Peak memory: {memory_stats['peak_memory_mb']:.2f} MB")


# Step 3: Add CPU profiling tools
# ===============================================================================

# Explanation:
# CPU profiling helps identify performance bottlenecks by analyzing function calls
# and execution time. We'll use cProfile for detailed function-level profiling.

import cProfile
import pstats
import io
from typing import Union

class CPUProfiler:
    """CPU profiler for analyzing function performance."""
    
    def __init__(self):
        self.profiler = None
        self.stats = None
    
    def start_profiling(self):
        """Start CPU profiling."""
        self.profiler = cProfile.Profile()
        self.profiler.enable()
    
    def stop_profiling(self):
        """Stop CPU profiling and prepare statistics."""
        if self.profiler:
            self.profiler.disable()
            
            # Create statistics object
            stats_stream = io.StringIO()
            self.stats = pstats.Stats(self.profiler, stream=stats_stream)
            return self.stats
        return None
    
    def get_stats_summary(self, sort_by: str = 'cumulative', limit: int = 10) -> str:
        """Get formatted statistics summary."""
        if not self.stats:
            return "No profiling data available"
        
        stats_stream = io.StringIO()
        stats = pstats.Stats(self.profiler, stream=stats_stream)
        stats.sort_stats(sort_by)
        stats.print_stats(limit)
        
        return stats_stream.getvalue()
    
    def profile_function(self, func: Callable, *args, **kwargs) -> Tuple[Any, str]:
        """Profile a single function call."""
        self.start_profiling()
        try:
            result = func(*args, **kwargs)
        finally:
            self.stop_profiling()
        
        stats_summary = self.get_stats_summary()
        return result, stats_summary
    
    def __enter__(self):
        self.start_profiling()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_profiling()

def profile_decorator(sort_by: str = 'cumulative', limit: int = 10):
    """Decorator for profiling function execution."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            profiler = CPUProfiler()
            result, stats = profiler.profile_function(func, *args, **kwargs)
            print(f"\n=== Profile for {func.__name__} ===")
            print(stats)
            return result
        return wrapper
    return decorator

# Example usage of Step 3:
def step3_example():
    """Demonstrate CPU profiling functionality."""
    print("\n=== Step 3: CPU Profiling ===")
    
    # Function to profile
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    def optimized_fibonacci(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = optimized_fibonacci(n-1, memo) + optimized_fibonacci(n-2, memo)
        return memo[n]
    
    # Profile using context manager
    print("Profiling recursive fibonacci:")
    with CPUProfiler() as profiler:
        result = fibonacci(20)
    
    stats_summary = profiler.get_stats_summary(limit=5)
    print(f"Result: {result}")
    print("Top 5 functions by cumulative time:")
    print(stats_summary)
    
    # Profile using decorator
    @profile_decorator(limit=3)
    def test_function():
        return optimized_fibonacci(30)
    
    print("\nProfiling optimized fibonacci with decorator:")
    test_function()


# Step 4: Implement statistical benchmarking
# ===============================================================================

# Explanation:
# Statistical benchmarking runs functions multiple times to get reliable measurements
# and provides statistical analysis of the results including mean, median, and variance.

class BenchmarkResult:
    """Container for benchmark results with statistical analysis."""
    
    def __init__(self, times: List[float], function_name: str = ""):
        self.times = times
        self.function_name = function_name
        self._calculate_statistics()
    
    def _calculate_statistics(self):
        """Calculate statistical measures from timing data."""
        if not self.times:
            return
        
        self.mean = statistics.mean(self.times)
        self.median = statistics.median(self.times)
        self.min_time = min(self.times)
        self.max_time = max(self.times)
        
        if len(self.times) > 1:
            self.std_dev = statistics.stdev(self.times)
            self.variance = statistics.variance(self.times)
        else:
            self.std_dev = 0.0
            self.variance = 0.0
        
        # Calculate confidence intervals (95%)
        if len(self.times) > 1:
            import math
            margin_of_error = 1.96 * (self.std_dev / math.sqrt(len(self.times)))
            self.confidence_interval = (self.mean - margin_of_error, self.mean + margin_of_error)
        else:
            self.confidence_interval = (self.mean, self.mean)
    
    def __str__(self):
        return f"""Benchmark Results for {self.function_name}:
  Runs: {len(self.times)}
  Mean: {self.mean:.6f}s
  Median: {self.median:.6f}s
  Min: {self.min_time:.6f}s
  Max: {self.max_time:.6f}s
  Std Dev: {self.std_dev:.6f}s
  95% CI: [{self.confidence_interval[0]:.6f}s, {self.confidence_interval[1]:.6f}s]"""

class StatisticalBenchmark:
    """Statistical benchmarking tool for reliable performance measurements."""
    
    def __init__(self, warmup_runs: int = 3, benchmark_runs: int = 10):
        self.warmup_runs = warmup_runs
        self.benchmark_runs = benchmark_runs
        self.results = {}
    
    def benchmark_function(self, func: Callable, *args, **kwargs) -> BenchmarkResult:
        """Benchmark a function with statistical analysis."""
        function_name = func.__name__
        
        # Warmup runs to stabilize performance
        print(f"Warming up {function_name}...")
        for _ in range(self.warmup_runs):
            func(*args, **kwargs)
        
        # Actual benchmark runs
        print(f"Benchmarking {function_name} ({self.benchmark_runs} runs)...")
        times = []
        
        for i in range(self.benchmark_runs):
            with Timer() as timer:
                func(*args, **kwargs)
            times.append(timer.elapsed_time)
            
            # Progress indicator
            if (i + 1) % max(1, self.benchmark_runs // 4) == 0:
                print(f"  Progress: {i + 1}/{self.benchmark_runs}")
        
        result = BenchmarkResult(times, function_name)
        self.results[function_name] = result
        return result
    
    def compare_functions(self, functions: List[Tuple[Callable, str]], *args, **kwargs) -> Dict[str, BenchmarkResult]:
        """Compare multiple functions with the same arguments."""
        results = {}
        
        for func, name in functions:
            print(f"\n--- Benchmarking {name} ---")
            result = self.benchmark_function(func, *args, **kwargs)
            results[name] = result
        
        return results
    
    def print_comparison(self, results: Dict[str, BenchmarkResult]):
        """Print a comparison of benchmark results."""
        print("\n" + "="*60)
        print("BENCHMARK COMPARISON")
        print("="*60)
        
        # Sort by mean time
        sorted_results = sorted(results.items(), key=lambda x: x[1].mean)
        
        fastest_time = sorted_results[0][1].mean
        
        for name, result in sorted_results:
            speedup = result.mean / fastest_time
            print(f"\n{name}:")
            print(f"  Mean time: {result.mean:.6f}s")
            print(f"  Speedup: {speedup:.2f}x slower than fastest" if speedup > 1 else "  FASTEST")
            print(f"  Std dev: {result.std_dev:.6f}s ({result.std_dev/result.mean*100:.1f}%)")

# Example usage of Step 4:
def step4_example():
    """Demonstrate statistical benchmarking functionality."""
    print("\n=== Step 4: Statistical Benchmarking ===")
    
    # Functions to benchmark
    def list_comprehension(n):
        return [i**2 for i in range(n)]
    
    def generator_expression(n):
        return list(i**2 for i in range(n))
    
    def map_function(n):
        return list(map(lambda x: x**2, range(n)))
    
    def for_loop(n):
        result = []
        for i in range(n):
            result.append(i**2)
        return result
    
    # Create benchmark
    benchmark = StatisticalBenchmark(warmup_runs=2, benchmark_runs=5)
    
    # Compare different implementations
    functions_to_compare = [
        (list_comprehension, "List Comprehension"),
        (generator_expression, "Generator Expression"),
        (map_function, "Map Function"),
        (for_loop, "For Loop")
    ]
    
    n = 10000
    results = benchmark.compare_functions(functions_to_compare, n)
    benchmark.print_comparison(results)


# Step 5: Create performance comparison utilities
# ===============================================================================

# Explanation:
# Performance comparison utilities help analyze and visualize performance differences
# between implementations, including scaling analysis and regression detection.

import json
from datetime import datetime

class PerformanceComparator:
    """Advanced performance comparison and analysis tool."""
    
    def __init__(self):
        self.comparison_history = []
        self.baseline_results = {}
    
    def set_baseline(self, name: str, result: BenchmarkResult):
        """Set a baseline for performance comparisons."""
        self.baseline_results[name] = result
        print(f"Baseline set for '{name}': {result.mean:.6f}s")
    
    def compare_to_baseline(self, name: str, current_result: BenchmarkResult) -> Dict[str, float]:
        """Compare current result to baseline."""
        if name not in self.baseline_results:
            raise ValueError(f"No baseline set for '{name}'")
        
        baseline = self.baseline_results[name]
        
        performance_ratio = current_result.mean / baseline.mean
        improvement_percent = ((baseline.mean - current_result.mean) / baseline.mean) * 100
        
        comparison = {
            'baseline_mean': baseline.mean,
            'current_mean': current_result.mean,
            'performance_ratio': performance_ratio,
            'improvement_percent': improvement_percent,
            'is_regression': performance_ratio > 1.05,  # 5% threshold
            'is_improvement': performance_ratio < 0.95   # 5% threshold
        }
        
        return comparison
    
    def analyze_scaling(self, func: Callable, input_sizes: List[int], 
                       runs_per_size: int = 5) -> Dict[str, Any]:
        """Analyze how function performance scales with input size."""
        print(f"\nAnalyzing scaling for {func.__name__}...")
        
        scaling_results = []
        
        for size in input_sizes:
            print(f"Testing input size: {size}")
            
            # Run benchmark for this size
            benchmark = StatisticalBenchmark(warmup_runs=1, benchmark_runs=runs_per_size)
            result = benchmark.benchmark_function(func, size)
            
            scaling_results.append({
                'input_size': size,
                'mean_time': result.mean,
                'std_dev': result.std_dev,
                'operations_per_second': size / result.mean if result.mean > 0 else 0
            })
        
        # Analyze complexity
        complexity_analysis = self._analyze_complexity(scaling_results)
        
        return {
            'function_name': func.__name__,
            'scaling_results': scaling_results,
            'complexity_analysis': complexity_analysis
        }
    
    def _analyze_complexity(self, results: List[Dict]) -> Dict[str, Any]:
        """Analyze algorithmic complexity from scaling results."""
        if len(results) < 3:
            return {'analysis': 'Insufficient data for complexity analysis'}
        
        # Calculate growth ratios
        growth_ratios = []
        for i in range(1, len(results)):
            size_ratio = results[i]['input_size'] / results[i-1]['input_size']
            time_ratio = results[i]['mean_time'] / results[i-1]['mean_time']
            growth_ratios.append(time_ratio / size_ratio)
        
        avg_growth = statistics.mean(growth_ratios)
        
        # Estimate complexity
        if avg_growth < 1.2:
            complexity = "O(1) - Constant"
        elif avg_growth < 2.0:
            complexity = "O(log n) - Logarithmic"
        elif avg_growth < 3.0:
            complexity = "O(n) - Linear"
        elif avg_growth < 5.0:
            complexity = "O(n log n) - Linearithmic"
        else:
            complexity = "O(n²) or worse - Polynomial/Exponential"
        
        return {
            'estimated_complexity': complexity,
            'average_growth_ratio': avg_growth,
            'growth_ratios': growth_ratios
        }
    
    def generate_performance_report(self, results: Dict[str, Any], 
                                  output_file: Optional[str] = None) -> str:
        """Generate a comprehensive performance report."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = f"""
PERFORMANCE ANALYSIS REPORT
Generated: {timestamp}
{'='*60}

"""
        
        if 'benchmark_results' in results:
            report += "BENCHMARK RESULTS:\n"
            for name, result in results['benchmark_results'].items():
                report += f"\n{name}:\n"
                report += f"  Mean: {result.mean:.6f}s\n"
                report += f"  Std Dev: {result.std_dev:.6f}s\n"
                report += f"  Min/Max: {result.min_time:.6f}s / {result.max_time:.6f}s\n"
        
        if 'scaling_analysis' in results:
            scaling = results['scaling_analysis']
            report += f"\nSCALING ANALYSIS for {scaling['function_name']}:\n"
            report += f"  Estimated Complexity: {scaling['complexity_analysis']['estimated_complexity']}\n"
            report += f"  Average Growth Ratio: {scaling['complexity_analysis']['average_growth_ratio']:.2f}\n"
            
            report += "\n  Input Size vs Performance:\n"
            for result in scaling['scaling_results']:
                ops_per_sec = result['operations_per_second']
                report += f"    Size {result['input_size']:>6}: {result['mean_time']:.6f}s ({ops_per_sec:>8.0f} ops/sec)\n"
        
        if 'baseline_comparison' in results:
            comp = results['baseline_comparison']
            report += f"\nBASELINE COMPARISON:\n"
            report += f"  Performance Ratio: {comp['performance_ratio']:.3f}x\n"
            report += f"  Change: {comp['improvement_percent']:+.1f}%\n"
            
            if comp['is_improvement']:
                report += "  Status: IMPROVEMENT ✓\n"
            elif comp['is_regression']:
                report += "  Status: REGRESSION ⚠\n"
            else:
                report += "  Status: No significant change\n"
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"Report saved to {output_file}")
        
        return report

# Example usage of Step 5:
def step5_example():
    """Demonstrate performance comparison utilities."""
    print("\n=== Step 5: Performance Comparison Utilities ===")
    
    # Create comparator
    comparator = PerformanceComparator()
    
    # Functions for scaling analysis
    def linear_search(arr, target):
        for i, item in enumerate(arr):
            if item == target:
                return i
        return -1
    
    def binary_search(arr, target):
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
    
    # Scaling analysis
    input_sizes = [100, 500, 1000, 2000]
    
    def test_linear_search(n):
        arr = list(range(n))
        return linear_search(arr, n-1)  # Search for last element
    
    def test_binary_search(n):
        arr = list(range(n))
        return binary_search(arr, n-1)  # Search for last element
    
    # Analyze scaling for both algorithms
    linear_scaling = comparator.analyze_scaling(test_linear_search, input_sizes, runs_per_size=3)
    binary_scaling = comparator.analyze_scaling(test_binary_search, input_sizes, runs_per_size=3)
    
    # Generate comprehensive report
    report_data = {
        'scaling_analysis': linear_scaling,
        'binary_scaling_analysis': binary_scaling
    }
    
    report = comparator.generate_performance_report(report_data)
    print(report)
    
    # Demonstrate baseline comparison
    print("\n--- Baseline Comparison Demo ---")
    benchmark = StatisticalBenchmark(warmup_runs=1, benchmark_runs=3)
    
    # Set baseline
    baseline_result = benchmark.benchmark_function(test_linear_search, 1000)
    comparator.set_baseline("linear_search_1000", baseline_result)
    
    # Compare current performance
    current_result = benchmark.benchmark_function(test_linear_search, 1000)
    comparison = comparator.compare_to_baseline("linear_search_1000", current_result)
    
    print(f"Performance comparison:")
    print(f"  Change: {comparison['improvement_percent']:+.1f}%")
    print(f"  Status: {'REGRESSION' if comparison['is_regression'] else 'OK'}")


# Step 6: Demonstrate optimization techniques
# ===============================================================================

# Explanation:
# This final step demonstrates common optimization techniques and how to measure
# their effectiveness using the profiling tools we've built.

class PerformanceProfiler:
    """Comprehensive performance profiler combining all previous tools."""
    
    def __init__(self):
        self.timer = Timer()
        self.memory_profiler = MemoryProfiler()
        self.cpu_profiler = CPUProfiler()
        self.benchmark = StatisticalBenchmark()
        self.comparator = PerformanceComparator()
        self.results = {}
    
    def profile_function(self, func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """Comprehensive profiling of a function."""
        function_name = func.__name__
        print(f"\n=== Profiling {function_name} ===")
        
        # Time profiling
        with Timer() as timer:
            result = func(*args, **kwargs)
        
        # Memory profiling
        with MemoryProfiler() as mem_profiler:
            func(*args, **kwargs)
        memory_stats = mem_profiler
        
        # CPU profiling
        _, cpu_stats = self.cpu_profiler.profile_function(func, *args, **kwargs)
        
        # Statistical benchmarking
        benchmark_result = self.benchmark.benchmark_function(func, *args, **kwargs)
        
        profile_data = {
            'function_name': function_name,
            'execution_time': timer.elapsed_time,
            'memory_usage': memory_stats,
            'cpu_profile': cpu_stats,
            'benchmark_result': benchmark_result,
            'return_value': result
        }
        
        self.results[function_name] = profile_data
        return profile_data
    
    def generate_report(self) -> str:
        """Generate comprehensive performance report."""
        return self.comparator.generate_performance_report({'benchmark_results': self.results})

# Optimization examples
class OptimizationExamples:
    """Examples of common optimization techniques."""
    
    @staticmethod
    def slow_string_concatenation(n: int) -> str:
        """Inefficient string concatenation using +."""
        result = ""
        for i in range(n):
            result += str(i)
        return result
    
    @staticmethod
    def fast_string_concatenation(n: int) -> str:
        """Efficient string concatenation using join."""
        return "".join(str(i) for i in range(n))
    
    @staticmethod
    def slow_list_operations(n: int) -> List[int]:
        """Inefficient list operations with repeated append."""
        result = []
        for i in range(n):
            result.append(i * 2)
        return result
    
    @staticmethod
    def fast_list_operations(n: int) -> List[int]:
        """Efficient list operations using list comprehension."""
        return [i * 2 for i in range(n)]
    
    @staticmethod
    def slow_dictionary_lookup(data: Dict[str, int], keys: List[str]) -> List[int]:
        """Inefficient dictionary lookups with exception handling."""
        result = []
        for key in keys:
            try:
                result.append(data[key])
            except KeyError:
                result.append(0)
        return result
    
    @staticmethod
    def fast_dictionary_lookup(data: Dict[str, int], keys: List[str]) -> List[int]:
        """Efficient dictionary lookups using get method."""
        return [data.get(key, 0) for key in keys]
    
    @staticmethod
    def slow_set_operations(list1: List[int], list2: List[int]) -> List[int]:
        """Inefficient set operations using nested loops."""
        result = []
        for item in list1:
            if item in list2 and item not in result:
                result.append(item)
        return result
    
    @staticmethod
    def fast_set_operations(list1: List[int], list2: List[int]) -> List[int]:
        """Efficient set operations using set intersection."""
        return list(set(list1) & set(list2))

# Example usage of Step 6:
def step6_example():
    """Demonstrate optimization techniques and comprehensive profiling."""
    print("\n=== Step 6: Optimization Techniques ===")
    
    # Create comprehensive profiler
    profiler = PerformanceProfiler()
    
    # Test data
    n = 1000
    test_dict = {str(i): i for i in range(n)}
    test_keys = [str(i) for i in range(0, n, 2)]  # Every other key
    list1 = list(range(n))
    list2 = list(range(n//2, n + n//2))
    
    print("Comparing optimization techniques...")
    
    # String concatenation comparison
    print("\n1. String Concatenation:")
    slow_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.slow_string_concatenation, n//10
    )
    fast_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.fast_string_concatenation, n//10
    )
    
    improvement = ((slow_result.mean - fast_result.mean) / slow_result.mean) * 100
    print(f"   Slow method: {slow_result.mean:.6f}s")
    print(f"   Fast method: {fast_result.mean:.6f}s")
    print(f"   Improvement: {improvement:.1f}%")
    
    # List operations comparison
    print("\n2. List Operations:")
    slow_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.slow_list_operations, n
    )
    fast_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.fast_list_operations, n
    )
    
    improvement = ((slow_result.mean - fast_result.mean) / slow_result.mean) * 100
    print(f"   Slow method: {slow_result.mean:.6f}s")
    print(f"   Fast method: {fast_result.mean:.6f}s")
    print(f"   Improvement: {improvement:.1f}%")
    
    # Dictionary lookup comparison
    print("\n3. Dictionary Lookups:")
    slow_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.slow_dictionary_lookup, test_dict, test_keys
    )
    fast_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.fast_dictionary_lookup, test_dict, test_keys
    )
    
    improvement = ((slow_result.mean - fast_result.mean) / slow_result.mean) * 100
    print(f"   Slow method: {slow_result.mean:.6f}s")
    print(f"   Fast method: {fast_result.mean:.6f}s")
    print(f"   Improvement: {improvement:.1f}%")
    
    # Set operations comparison
    print("\n4. Set Operations:")
    slow_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.slow_set_operations, list1[:100], list2[:100]
    )
    fast_result = profiler.benchmark.benchmark_function(
        OptimizationExamples.fast_set_operations, list1[:100], list2[:100]
    )
    
    improvement = ((slow_result.mean - fast_result.mean) / slow_result.mean) * 100
    print(f"   Slow method: {slow_result.mean:.6f}s")
    print(f"   Fast method: {fast_result.mean:.6f}s")
    print(f"   Improvement: {improvement:.1f}%")
    
    print("\n" + "="*60)
    print("OPTIMIZATION SUMMARY")
    print("="*60)
    print("Key takeaways:")
    print("1. Use join() instead of += for string concatenation")
    print("2. Prefer list comprehensions over explicit loops")
    print("3. Use dict.get() instead of try/except for lookups")
    print("4. Leverage set operations for intersection/union tasks")
    print("5. Always profile before and after optimization!")

if __name__ == "__main__":
    step1_example()
    step2_example()
    step3_example()
    step4_example()
    step5_example()
    step6_example()