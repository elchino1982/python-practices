"""Question: Optimize string operations for better performance in Python.

Learn and implement efficient string manipulation techniques to improve
application performance and memory usage.

Requirements:
1. Understand string concatenation performance issues
2. Learn efficient string building techniques
3. Implement string formatting optimizations
4. Use appropriate string methods for different scenarios
5. Demonstrate memory-efficient string operations

Example usage:
    # Efficient string building
    builder = StringBuilder()
    result = builder.build_from_list(items)
    
    # Optimized string formatting
    formatter = StringFormatter()
    output = formatter.format_template(template, data)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about string performance bottlenecks
# - Start with simple implementations
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
# - Why is string concatenation with + operator slow?
# - When should you use join() vs other methods?
# - What are the benefits of f-strings vs other formatting?
# - How can you minimize string object creation?
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


# Step 1: Import modules and understand string concatenation performance
# ===============================================================================

# Explanation:
# String concatenation performance is crucial in Python because strings are immutable.
# Each concatenation creates a new string object, which can be very inefficient.

import time
import sys
from typing import List, Dict, Any
from io import StringIO

def demonstrate_concatenation_performance():
    """Show the performance difference between concatenation methods."""
    
    # Inefficient: Using + operator in a loop
    def inefficient_concatenation(items: List[str]) -> str:
        result = ""
        for item in items:
            result += item  # Creates new string object each time
        return result
    
    # Efficient: Using join method
    def efficient_concatenation(items: List[str]) -> str:
        return "".join(items)  # Single operation, much faster
    
    # Test data
    test_items = ["item" + str(i) for i in range(1000)]
    
    # Time inefficient method
    start_time = time.time()
    result1 = inefficient_concatenation(test_items)
    inefficient_time = time.time() - start_time
    
    # Time efficient method
    start_time = time.time()
    result2 = efficient_concatenation(test_items)
    efficient_time = time.time() - start_time
    
    print(f"Inefficient concatenation time: {inefficient_time:.6f} seconds")
    print(f"Efficient concatenation time: {efficient_time:.6f} seconds")
    print(f"Performance improvement: {inefficient_time / efficient_time:.2f}x faster")
    
    return result1, result2


# Step 2: Build upon Step 1 - Add StringBuilder class for efficient building
# ===============================================================================

# Explanation:
# We'll create a StringBuilder class that uses efficient methods internally
# and provides a clean interface for string building operations.

# All code from Step 1:
import time
import sys
from typing import List, Dict, Any
from io import StringIO

def demonstrate_concatenation_performance():
    """Show the performance difference between concatenation methods."""
    
    # Inefficient: Using + operator in a loop
    def inefficient_concatenation(items: List[str]) -> str:
        result = ""
        for item in items:
            result += item  # Creates new string object each time
        return result
    
    # Efficient: Using join method
    def efficient_concatenation(items: List[str]) -> str:
        return "".join(items)  # Single operation, much faster
    
    # Test data
    test_items = ["item" + str(i) for i in range(1000)]
    
    # Time inefficient method
    start_time = time.time()
    result1 = inefficient_concatenation(test_items)
    inefficient_time = time.time() - start_time
    
    # Time efficient method
    start_time = time.time()
    result2 = efficient_concatenation(test_items)
    efficient_time = time.time() - start_time
    
    print(f"Inefficient concatenation time: {inefficient_time:.6f} seconds")
    print(f"Efficient concatenation time: {efficient_time:.6f} seconds")
    print(f"Performance improvement: {inefficient_time / efficient_time:.2f}x faster")
    
    return result1, result2

# New code for Step 2:
class StringBuilder:
    """Efficient string builder using list accumulation."""
    
    def __init__(self):
        self._parts = []
    
    def append(self, text: str) -> 'StringBuilder':
        """Add text to the builder."""
        self._parts.append(text)
        return self  # Enable method chaining
    
    def append_line(self, text: str = "") -> 'StringBuilder':
        """Add text with a newline."""
        self._parts.append(text + "\n")
        return self
    
    def build_from_list(self, items: List[str], separator: str = "") -> str:
        """Build string from a list of items."""
        return separator.join(items)
    
    def build(self) -> str:
        """Build the final string."""
        return "".join(self._parts)
    
    def clear(self) -> 'StringBuilder':
        """Clear the builder for reuse."""
        self._parts.clear()
        return self
    
    def __len__(self) -> int:
        """Get the number of parts in the builder."""
        return len(self._parts)

def demonstrate_string_builder():
    """Show StringBuilder usage and performance."""
    builder = StringBuilder()
    
    # Method chaining example
    result = (builder
              .append("Hello ")
              .append("World")
              .append_line("!")
              .append("This is efficient")
              .build())
    
    print("StringBuilder result:")
    print(result)
    
    # Performance comparison
    items = ["line" + str(i) for i in range(1000)]
    
    # Using StringBuilder
    start_time = time.time()
    builder.clear()
    for item in items:
        builder.append(item)
    result_builder = builder.build()
    builder_time = time.time() - start_time
    
    # Using join directly
    start_time = time.time()
    result_join = "".join(items)
    join_time = time.time() - start_time
    
    print(f"\nStringBuilder time: {builder_time:.6f} seconds")
    print(f"Direct join time: {join_time:.6f} seconds")
    print(f"StringBuilder overhead: {builder_time / join_time:.2f}x")
    
    return result_builder, result_join


# Step 3: Build upon Steps 1-2 - Add string formatting optimizations
# ===============================================================================

# Explanation:
# String formatting performance varies significantly between different methods.
# f-strings are generally the fastest, followed by .format(), then % formatting.

# All code from Steps 1-2:
import time
import sys
from typing import List, Dict, Any
from io import StringIO

def demonstrate_concatenation_performance():
    """Show the performance difference between concatenation methods."""
    
    # Inefficient: Using + operator in a loop
    def inefficient_concatenation(items: List[str]) -> str:
        result = ""
        for item in items:
            result += item  # Creates new string object each time
        return result
    
    # Efficient: Using join method
    def efficient_concatenation(items: List[str]) -> str:
        return "".join(items)  # Single operation, much faster
    
    # Test data
    test_items = ["item" + str(i) for i in range(1000)]
    
    # Time inefficient method
    start_time = time.time()
    result1 = inefficient_concatenation(test_items)
    inefficient_time = time.time() - start_time
    
    # Time efficient method
    start_time = time.time()
    result2 = efficient_concatenation(test_items)
    efficient_time = time.time() - start_time
    
    print(f"Inefficient concatenation time: {inefficient_time:.6f} seconds")
    print(f"Efficient concatenation time: {efficient_time:.6f} seconds")
    print(f"Performance improvement: {inefficient_time / efficient_time:.2f}x faster")
    
    return result1, result2

class StringBuilder:
    """Efficient string builder using list accumulation."""
    
    def __init__(self):
        self._parts = []
    
    def append(self, text: str) -> 'StringBuilder':
        """Add text to the builder."""
        self._parts.append(text)
        return self  # Enable method chaining
    
    def append_line(self, text: str = "") -> 'StringBuilder':
        """Add text with a newline."""
        self._parts.append(text + "\n")
        return self
    
    def build_from_list(self, items: List[str], separator: str = "") -> str:
        """Build string from a list of items."""
        return separator.join(items)
    
    def build(self) -> str:
        """Build the final string."""
        return "".join(self._parts)
    
    def clear(self) -> 'StringBuilder':
        """Clear the builder for reuse."""
        self._parts.clear()
        return self
    
    def __len__(self) -> int:
        """Get the number of parts in the builder."""
        return len(self._parts)

def demonstrate_string_builder():
    """Show StringBuilder usage and performance."""
    builder = StringBuilder()
    
    # Method chaining example
    result = (builder
              .append("Hello ")
              .append("World")
              .append_line("!")
              .append("This is efficient")
              .build())
    
    print("StringBuilder result:")
    print(result)
    
    # Performance comparison
    items = ["line" + str(i) for i in range(1000)]
    
    # Using StringBuilder
    start_time = time.time()
    builder.clear()
    for item in items:
        builder.append(item)
    result_builder = builder.build()
    builder_time = time.time() - start_time
    
    # Using join directly
    start_time = time.time()
    result_join = "".join(items)
    join_time = time.time() - start_time
    
    print(f"\nStringBuilder time: {builder_time:.6f} seconds")
    print(f"Direct join time: {join_time:.6f} seconds")
    print(f"StringBuilder overhead: {builder_time / join_time:.2f}x")
    
    return result_builder, result_join

# New code for Step 3:
class StringFormatter:
    """Optimized string formatting utilities."""
    
    @staticmethod
    def compare_formatting_methods(name: str, age: int, score: float, iterations: int = 10000):
        """Compare different string formatting methods."""
        
        # Method 1: f-strings (fastest)
        start_time = time.time()
        for _ in range(iterations):
            result = f"Name: {name}, Age: {age}, Score: {score:.2f}"
        fstring_time = time.time() - start_time
        
        # Method 2: .format() method
        start_time = time.time()
        for _ in range(iterations):
            result = "Name: {}, Age: {}, Score: {:.2f}".format(name, age, score)
        format_time = time.time() - start_time
        
        # Method 3: % formatting (oldest, slowest)
        start_time = time.time()
        for _ in range(iterations):
            result = "Name: %s, Age: %d, Score: %.2f" % (name, age, score)
        percent_time = time.time() - start_time
        
        # Method 4: Template strings (safe but slower)
        from string import Template
        template = Template("Name: $name, Age: $age, Score: $score")
        start_time = time.time()
        for _ in range(iterations):
            result = template.substitute(name=name, age=age, score=f"{score:.2f}")
        template_time = time.time() - start_time
        
        print(f"Formatting performance comparison ({iterations} iterations):")
        print(f"f-strings:     {fstring_time:.6f} seconds (baseline)")
        print(f".format():     {format_time:.6f} seconds ({format_time/fstring_time:.2f}x slower)")
        print(f"% formatting:  {percent_time:.6f} seconds ({percent_time/fstring_time:.2f}x slower)")
        print(f"Template:      {template_time:.6f} seconds ({template_time/fstring_time:.2f}x slower)")
        
        return fstring_time, format_time, percent_time, template_time
    
    @staticmethod
    def format_template(template: str, data: Dict[str, Any]) -> str:
        """Efficiently format a template with data using f-strings when possible."""
        # For dynamic templates, .format() is often the best choice
        return template.format(**data)
    
    @staticmethod
    def build_csv_line(values: List[Any], delimiter: str = ",") -> str:
        """Efficiently build a CSV line."""
        # Convert all values to strings and join
        return delimiter.join(str(value) for value in values)
    
    @staticmethod
    def build_sql_query(table: str, columns: List[str], conditions: Dict[str, Any]) -> str:
        """Build SQL query efficiently."""
        # Use f-strings for static parts, join for dynamic lists
        columns_str = ", ".join(columns)
        where_parts = [f"{key} = '{value}'" for key, value in conditions.items()]
        where_clause = " AND ".join(where_parts)
        
        return f"SELECT {columns_str} FROM {table} WHERE {where_clause}"

def demonstrate_string_formatting():
    """Show string formatting optimizations."""
    formatter = StringFormatter()
    
    # Compare formatting methods
    formatter.compare_formatting_methods("Alice", 30, 95.5)
    
    # Template formatting
    template = "Hello {name}, your score is {score} out of {total}"
    data = {"name": "Bob", "score": 85, "total": 100}
    result = formatter.format_template(template, data)
    print(f"\nTemplate result: {result}")
    
    # CSV building
    csv_line = formatter.build_csv_line(["John", 25, 87.5, "Engineer"])
    print(f"CSV line: {csv_line}")
    
    # SQL query building
    query = formatter.build_sql_query(
        "users", 
        ["name", "age", "score"], 
        {"department": "Engineering", "active": True}
    )
    print(f"SQL query: {query}")
    
    return result, csv_line, query


# Step 4: Build upon Steps 1-3 - Add memory-efficient string operations
# ===============================================================================

# Explanation:
# Memory efficiency is crucial for large string operations. We'll explore
# techniques like StringIO, generators, and lazy evaluation.

# All code from Steps 1-3:
import time
import sys
from typing import List, Dict, Any
from io import StringIO

def demonstrate_concatenation_performance():
    """Show the performance difference between concatenation methods."""
    
    # Inefficient: Using + operator in a loop
    def inefficient_concatenation(items: List[str]) -> str:
        result = ""
        for item in items:
            result += item  # Creates new string object each time
        return result
    
    # Efficient: Using join method
    def efficient_concatenation(items: List[str]) -> str:
        return "".join(items)  # Single operation, much faster
    
    # Test data
    test_items = ["item" + str(i) for i in range(1000)]
    
    # Time inefficient method
    start_time = time.time()
    result1 = inefficient_concatenation(test_items)
    inefficient_time = time.time() - start_time
    
    # Time efficient method
    start_time = time.time()
    result2 = efficient_concatenation(test_items)
    efficient_time = time.time() - start_time
    
    print(f"Inefficient concatenation time: {inefficient_time:.6f} seconds")
    print(f"Efficient concatenation time: {efficient_time:.6f} seconds")
    print(f"Performance improvement: {inefficient_time / efficient_time:.2f}x faster")
    
    return result1, result2

class StringBuilder:
    """Efficient string builder using list accumulation."""
    
    def __init__(self):
        self._parts = []
    
    def append(self, text: str) -> 'StringBuilder':
        """Add text to the builder."""
        self._parts.append(text)
        return self  # Enable method chaining
    
    def append_line(self, text: str = "") -> 'StringBuilder':
        """Add text with a newline."""
        self._parts.append(text + "\n")
        return self
    
    def build_from_list(self, items: List[str], separator: str = "") -> str:
        """Build string from a list of items."""
        return separator.join(items)
    
    def build(self) -> str:
        """Build the final string."""
        return "".join(self._parts)
    
    def clear(self) -> 'StringBuilder':
        """Clear the builder for reuse."""
        self._parts.clear()
        return self
    
    def __len__(self) -> int:
        """Get the number of parts in the builder."""
        return len(self._parts)

def demonstrate_string_builder():
    """Show StringBuilder usage and performance."""
    builder = StringBuilder()
    
    # Method chaining example
    result = (builder
              .append("Hello ")
              .append("World")
              .append_line("!")
              .append("This is efficient")
              .build())
    
    print("StringBuilder result:")
    print(result)
    
    # Performance comparison
    items = ["line" + str(i) for i in range(1000)]
    
    # Using StringBuilder
    start_time = time.time()
    builder.clear()
    for item in items:
        builder.append(item)
    result_builder = builder.build()
    builder_time = time.time() - start_time
    
    # Using join directly
    start_time = time.time()
    result_join = "".join(items)
    join_time = time.time() - start_time
    
    print(f"\nStringBuilder time: {builder_time:.6f} seconds")
    print(f"Direct join time: {join_time:.6f} seconds")
    print(f"StringBuilder overhead: {builder_time / join_time:.2f}x")
    
    return result_builder, result_join

class StringFormatter:
    """Optimized string formatting utilities."""
    
    @staticmethod
    def compare_formatting_methods(name: str, age: int, score: float, iterations: int = 10000):
        """Compare different string formatting methods."""
        
        # Method 1: f-strings (fastest)
        start_time = time.time()
        for _ in range(iterations):
            result = f"Name: {name}, Age: {age}, Score: {score:.2f}"
        fstring_time = time.time() - start_time
        
        # Method 2: .format() method
        start_time = time.time()
        for _ in range(iterations):
            result = "Name: {}, Age: {}, Score: {:.2f}".format(name, age, score)
        format_time = time.time() - start_time
        
        # Method 3: % formatting (oldest, slowest)
        start_time = time.time()
        for _ in range(iterations):
            result = "Name: %s, Age: %d, Score: %.2f" % (name, age, score)
        percent_time = time.time() - start_time
        
        # Method 4: Template strings (safe but slower)
        from string import Template
        template = Template("Name: $name, Age: $age, Score: $score")
        start_time = time.time()
        for _ in range(iterations):
            result = template.substitute(name=name, age=age, score=f"{score:.2f}")
        template_time = time.time() - start_time
        
        print(f"Formatting performance comparison ({iterations} iterations):")
        print(f"f-strings:     {fstring_time:.6f} seconds (baseline)")
        print(f".format():     {format_time:.6f} seconds ({format_time/fstring_time:.2f}x slower)")
        print(f"% formatting:  {percent_time:.6f} seconds ({percent_time/fstring_time:.2f}x slower)")
        print(f"Template:      {template_time:.6f} seconds ({template_time/fstring_time:.2f}x slower)")
        
        return fstring_time, format_time, percent_time, template_time
    
    @staticmethod
    def format_template(template: str, data: Dict[str, Any]) -> str:
        """Efficiently format a template with data using f-strings when possible."""
        # For dynamic templates, .format() is often the best choice
        return template.format(**data)
    
    @staticmethod
    def build_csv_line(values: List[Any], delimiter: str = ",") -> str:
        """Efficiently build a CSV line."""
        # Convert all values to strings and join
        return delimiter.join(str(value) for value in values)
    
    @staticmethod
    def build_sql_query(table: str, columns: List[str], conditions: Dict[str, Any]) -> str:
        """Build SQL query efficiently."""
        # Use f-strings for static parts, join for dynamic lists
        columns_str = ", ".join(columns)
        where_parts = [f"{key} = '{value}'" for key, value in conditions.items()]
        where_clause = " AND ".join(where_parts)
        
        return f"SELECT {columns_str} FROM {table} WHERE {where_clause}"

def demonstrate_string_formatting():
    """Show string formatting optimizations."""
    formatter = StringFormatter()
    
    # Compare formatting methods
    formatter.compare_formatting_methods("Alice", 30, 95.5)
    
    # Template formatting
    template = "Hello {name}, your score is {score} out of {total}"
    data = {"name": "Bob", "score": 85, "total": 100}
    result = formatter.format_template(template, data)
    print(f"\nTemplate result: {result}")
    
    # CSV building
    csv_line = formatter.build_csv_line(["John", 25, 87.5, "Engineer"])
    print(f"CSV line: {csv_line}")
    
    # SQL query building
    query = formatter.build_sql_query(
        "users", 
        ["name", "age", "score"], 
        {"department": "Engineering", "active": True}
    )
    print(f"SQL query: {query}")
    
    return result, csv_line, query

# New code for Step 4:
class MemoryEfficientStringProcessor:
    """Memory-efficient string processing utilities."""
    
    @staticmethod
    def compare_memory_usage():
        """Compare memory usage of different string building methods."""
        import tracemalloc
        
        # Test data
        items = [f"line{i}" for i in range(10000)]
        
        # Method 1: String concatenation (memory inefficient)
        tracemalloc.start()
        result1 = ""
        for item in items:
            result1 += item
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        concat_memory = peak
        
        # Method 2: Join method (memory efficient)
        tracemalloc.start()
        result2 = "".join(items)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        join_memory = peak
        
        # Method 3: StringIO (good for incremental building)
        tracemalloc.start()
        buffer = StringIO()
        for item in items:
            buffer.write(item)
        result3 = buffer.getvalue()
        buffer.close()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        stringio_memory = peak
        
        print(f"Memory usage comparison:")
        print(f"String concatenation: {concat_memory / 1024 / 1024:.2f} MB")
        print(f"Join method:          {join_memory / 1024 / 1024:.2f} MB")
        print(f"StringIO:             {stringio_memory / 1024 / 1024:.2f} MB")
        print(f"Join vs concat:       {concat_memory / join_memory:.2f}x more memory")
        
        return concat_memory, join_memory, stringio_memory
    
    @staticmethod
    def process_large_text_generator(lines: List[str]):
        """Process large text using generators for memory efficiency."""
        def process_line(line: str) -> str:
            # Simulate some processing
            return line.strip().upper()
        
        # Generator approach - processes one line at a time
        for line in lines:
            yield process_line(line)
    
    @staticmethod
    def build_report_with_stringio(data: List[Dict[str, Any]]) -> str:
        """Build a report using StringIO for memory efficiency."""
        buffer = StringIO()
        
        # Header
        buffer.write("PERFORMANCE REPORT\n")
        buffer.write("=" * 50 + "\n\n")
        
        # Data rows
        for i, record in enumerate(data, 1):
            buffer.write(f"Record {i}:\n")
            for key, value in record.items():
                buffer.write(f"  {key}: {value}\n")
            buffer.write("\n")
        
        # Footer
        buffer.write(f"Total records: {len(data)}\n")
        
        result = buffer.getvalue()
        buffer.close()
        return result
    
    @staticmethod
    def lazy_string_processor(text: str, chunk_size: int = 1000):
        """Process large strings lazily in chunks."""
        def process_chunk(chunk: str) -> str:
            # Example processing: remove extra whitespace
            return " ".join(chunk.split())
        
        # Process in chunks to avoid loading entire string in memory
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            yield process_chunk(chunk)
    
    @staticmethod
    def efficient_string_search(text: str, patterns: List[str]) -> Dict[str, List[int]]:
        """Efficiently search for multiple patterns in text."""
        results = {pattern: [] for pattern in patterns}
        
        # Single pass through text for all patterns
        for i, char in enumerate(text):
            for pattern in patterns:
                if text[i:].startswith(pattern):
                    results[pattern].append(i)
        
        return results

def demonstrate_memory_efficiency():
    """Show memory-efficient string operations."""
    processor = MemoryEfficientStringProcessor()
    
    # Memory usage comparison
    print("Memory Usage Comparison:")
    processor.compare_memory_usage()
    
    # Generator processing
    print("\nGenerator Processing:")
    lines = ["  hello world  ", "  PYTHON rocks  ", "  efficiency matters  "]
    processed = list(processor.process_large_text_generator(lines))
    print(f"Processed lines: {processed}")
    
    # StringIO report building
    print("\nStringIO Report Building:")
    data = [
        {"name": "Alice", "score": 95, "department": "Engineering"},
        {"name": "Bob", "score": 87, "department": "Marketing"},
        {"name": "Charlie", "score": 92, "department": "Engineering"}
    ]
    report = processor.build_report_with_stringio(data)
    print("Report preview:")
    print(report[:200] + "..." if len(report) > 200 else report)
    
    # Lazy processing
    print("\nLazy String Processing:")
    large_text = "This is a sample text with lots of   extra    spaces   everywhere."
    processed_chunks = list(processor.lazy_string_processor(large_text, 20))
    print(f"Processed chunks: {processed_chunks}")
    
    # Efficient search
    print("\nEfficient String Search:")
    search_text = "The quick brown fox jumps over the lazy dog. The fox is quick."
    patterns = ["the", "fox", "quick"]
    search_results = processor.efficient_string_search(search_text.lower(), patterns)
    print(f"Search results: {search_results}")
    
    return processed, report, processed_chunks, search_results


# Step 5: Build upon Steps 1-4 - Complete string operations optimization suite
# ===============================================================================

# Explanation:
# This final step combines all previous techniques into a comprehensive
# string operations optimization suite with real-world examples.

# All code from Steps 1-4:
import time
import sys
from typing import List, Dict, Any, Generator, Iterator
from io import StringIO
import re

def demonstrate_concatenation_performance():
    """Show the performance difference between concatenation methods."""
    
    # Inefficient: Using + operator in a loop
    def inefficient_concatenation(items: List[str]) -> str:
        result = ""
        for item in items:
            result += item  # Creates new string object each time
        return result
    
    # Efficient: Using join method
    def efficient_concatenation(items: List[str]) -> str:
        return "".join(items)  # Single operation, much faster
    
    # Test data
    test_items = ["item" + str(i) for i in range(1000)]
    
    # Time inefficient method
    start_time = time.time()
    result1 = inefficient_concatenation(test_items)
    inefficient_time = time.time() - start_time
    
    # Time efficient method
    start_time = time.time()
    result2 = efficient_concatenation(test_items)
    efficient_time = time.time() - start_time
    
    print(f"Inefficient concatenation time: {inefficient_time:.6f} seconds")
    print(f"Efficient concatenation time: {efficient_time:.6f} seconds")
    print(f"Performance improvement: {inefficient_time / efficient_time:.2f}x faster")
    
    return result1, result2

class StringBuilder:
    """Efficient string builder using list accumulation."""
    
    def __init__(self):
        self._parts = []
    
    def append(self, text: str) -> 'StringBuilder':
        """Add text to the builder."""
        self._parts.append(text)
        return self  # Enable method chaining
    
    def append_line(self, text: str = "") -> 'StringBuilder':
        """Add text with a newline."""
        self._parts.append(text + "\n")
        return self
    
    def build_from_list(self, items: List[str], separator: str = "") -> str:
        """Build string from a list of items."""
        return separator.join(items)
    
    def build(self) -> str:
        """Build the final string."""
        return "".join(self._parts)
    
    def clear(self) -> 'StringBuilder':
        """Clear the builder for reuse."""
        self._parts.clear()
        return self
    
    def __len__(self) -> int:
        """Get the number of parts in the builder."""
        return len(self._parts)

def demonstrate_string_builder():
    """Show StringBuilder usage and performance."""
    builder = StringBuilder()
    
    # Method chaining example
    result = (builder
              .append("Hello ")
              .append("World")
              .append_line("!")
              .append("This is efficient")
              .build())
    
    print("StringBuilder result:")
    print(result)
    
    # Performance comparison
    items = ["line" + str(i) for i in range(1000)]
    
    # Using StringBuilder
    start_time = time.time()
    builder.clear()
    for item in items:
        builder.append(item)
    result_builder = builder.build()
    builder_time = time.time() - start_time
    
    # Using join directly
    start_time = time.time()
    result_join = "".join(items)
    join_time = time.time() - start_time
    
    print(f"\nStringBuilder time: {builder_time:.6f} seconds")
    print(f"Direct join time: {join_time:.6f} seconds")
    print(f"StringBuilder overhead: {builder_time / join_time:.2f}x")
    
    return result_builder, result_join

class StringFormatter:
    """Optimized string formatting utilities."""
    
    @staticmethod
    def compare_formatting_methods(name: str, age: int, score: float, iterations: int = 10000):
        """Compare different string formatting methods."""
        
        # Method 1: f-strings (fastest)
        start_time = time.time()
        for _ in range(iterations):
            result = f"Name: {name}, Age: {age}, Score: {score:.2f}"
        fstring_time = time.time() - start_time
        
        # Method 2: .format() method
        start_time = time.time()
        for _ in range(iterations):
            result = "Name: {}, Age: {}, Score: {:.2f}".format(name, age, score)
        format_time = time.time() - start_time
        
        # Method 3: % formatting (oldest, slowest)
        start_time = time.time()
        for _ in range(iterations):
            result = "Name: %s, Age: %d, Score: %.2f" % (name, age, score)
        percent_time = time.time() - start_time
        
        # Method 4: Template strings (safe but slower)
        from string import Template
        template = Template("Name: $name, Age: $age, Score: $score")
        start_time = time.time()
        for _ in range(iterations):
            result = template.substitute(name=name, age=age, score=f"{score:.2f}")
        template_time = time.time() - start_time
        
        print(f"Formatting performance comparison ({iterations} iterations):")
        print(f"f-strings:     {fstring_time:.6f} seconds (baseline)")
        print(f".format():     {format_time:.6f} seconds ({format_time/fstring_time:.2f}x slower)")
        print(f"% formatting:  {percent_time:.6f} seconds ({percent_time/fstring_time:.2f}x slower)")
        print(f"Template:      {template_time:.6f} seconds ({template_time/fstring_time:.2f}x slower)")
        
        return fstring_time, format_time, percent_time, template_time
    
    @staticmethod
    def format_template(template: str, data: Dict[str, Any]) -> str:
        """Efficiently format a template with data using f-strings when possible."""
        # For dynamic templates, .format() is often the best choice
        return template.format(**data)
    
    @staticmethod
    def build_csv_line(values: List[Any], delimiter: str = ",") -> str:
        """Efficiently build a CSV line."""
        # Convert all values to strings and join
        return delimiter.join(str(value) for value in values)
    
    @staticmethod
    def build_sql_query(table: str, columns: List[str], conditions: Dict[str, Any]) -> str:
        """Build SQL query efficiently."""
        # Use f-strings for static parts, join for dynamic lists
        columns_str = ", ".join(columns)
        where_parts = [f"{key} = '{value}'" for key, value in conditions.items()]
        where_clause = " AND ".join(where_parts)
        
        return f"SELECT {columns_str} FROM {table} WHERE {where_clause}"

def demonstrate_string_formatting():
    """Show string formatting optimizations."""
    formatter = StringFormatter()
    
    # Compare formatting methods
    formatter.compare_formatting_methods("Alice", 30, 95.5)
    
    # Template formatting
    template = "Hello {name}, your score is {score} out of {total}"
    data = {"name": "Bob", "score": 85, "total": 100}
    result = formatter.format_template(template, data)
    print(f"\nTemplate result: {result}")
    
    # CSV building
    csv_line = formatter.build_csv_line(["John", 25, 87.5, "Engineer"])
    print(f"CSV line: {csv_line}")
    
    # SQL query building
    query = formatter.build_sql_query(
        "users", 
        ["name", "age", "score"], 
        {"department": "Engineering", "active": True}
    )
    print(f"SQL query: {query}")
    
    return result, csv_line, query

class MemoryEfficientStringProcessor:
    """Memory-efficient string processing utilities."""
    
    @staticmethod
    def compare_memory_usage():
        """Compare memory usage of different string building methods."""
        import tracemalloc
        
        # Test data
        items = [f"line{i}" for i in range(10000)]
        
        # Method 1: String concatenation (memory inefficient)
        tracemalloc.start()
        result1 = ""
        for item in items:
            result1 += item
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        concat_memory = peak
        
        # Method 2: Join method (memory efficient)
        tracemalloc.start()
        result2 = "".join(items)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        join_memory = peak
        
        # Method 3: StringIO (good for incremental building)
        tracemalloc.start()
        buffer = StringIO()
        for item in items:
            buffer.write(item)
        result3 = buffer.getvalue()
        buffer.close()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        stringio_memory = peak
        
        print(f"Memory usage comparison:")
        print(f"String concatenation: {concat_memory / 1024 / 1024:.2f} MB")
        print(f"Join method:          {join_memory / 1024 / 1024:.2f} MB")
        print(f"StringIO:             {stringio_memory / 1024 / 1024:.2f} MB")
        print(f"Join vs concat:       {concat_memory / join_memory:.2f}x more memory")
        
        return concat_memory, join_memory, stringio_memory
    
    @staticmethod
    def process_large_text_generator(lines: List[str]):
        """Process large text using generators for memory efficiency."""
        def process_line(line: str) -> str:
            # Simulate some processing
            return line.strip().upper()
        
        # Generator approach - processes one line at a time
        for line in lines:
            yield process_line(line)
    
    @staticmethod
    def build_report_with_stringio(data: List[Dict[str, Any]]) -> str:
        """Build a report using StringIO for memory efficiency."""
        buffer = StringIO()
        
        # Header
        buffer.write("PERFORMANCE REPORT\n")
        buffer.write("=" * 50 + "\n\n")
        
        # Data rows
        for i, record in enumerate(data, 1):
            buffer.write(f"Record {i}:\n")
            for key, value in record.items():
                buffer.write(f"  {key}: {value}\n")
            buffer.write("\n")
        
        # Footer
        buffer.write(f"Total records: {len(data)}\n")
        
        result = buffer.getvalue()
        buffer.close()
        return result
    
    @staticmethod
    def lazy_string_processor(text: str, chunk_size: int = 1000):
        """Process large strings lazily in chunks."""
        def process_chunk(chunk: str) -> str:
            # Example processing: remove extra whitespace
            return " ".join(chunk.split())
        
        # Process in chunks to avoid loading entire string in memory
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]
            yield process_chunk(chunk)
    
    @staticmethod
    def efficient_string_search(text: str, patterns: List[str]) -> Dict[str, List[int]]:
        """Efficiently search for multiple patterns in text."""
        results = {pattern: [] for pattern in patterns}
        
        # Single pass through text for all patterns
        for i, char in enumerate(text):
            for pattern in patterns:
                if text[i:].startswith(pattern):
                    results[pattern].append(i)
        
        return results

def demonstrate_memory_efficiency():
    """Show memory-efficient string operations."""
    processor = MemoryEfficientStringProcessor()
    
    # Memory usage comparison
    print("Memory Usage Comparison:")
    processor.compare_memory_usage()
    
    # Generator processing
    print("\nGenerator Processing:")
    lines = ["  hello world  ", "  PYTHON rocks  ", "  efficiency matters  "]
    processed = list(processor.process_large_text_generator(lines))
    print(f"Processed lines: {processed}")
    
    # StringIO report building
    print("\nStringIO Report Building:")
    data = [
        {"name": "Alice", "score": 95, "department": "Engineering"},
        {"name": "Bob", "score": 87, "department": "Marketing"},
        {"name": "Charlie", "score": 92, "department": "Engineering"}
    ]
    report = processor.build_report_with_stringio(data)
    print("Report preview:")
    print(report[:200] + "..." if len(report) > 200 else report)
    
    # Lazy processing
    print("\nLazy String Processing:")
    large_text = "This is a sample text with lots of   extra    spaces   everywhere."
    processed_chunks = list(processor.lazy_string_processor(large_text, 20))
    print(f"Processed chunks: {processed_chunks}")
    
    # Efficient search
    print("\nEfficient String Search:")
    search_text = "The quick brown fox jumps over the lazy dog. The fox is quick."
    patterns = ["the", "fox", "quick"]
    search_results = processor.efficient_string_search(search_text.lower(), patterns)
    print(f"Search results: {search_results}")
    
    return processed, report, processed_chunks, search_results

# New code for Step 5:
class StringOptimizationSuite:
    """Complete string optimization suite combining all techniques."""
    
    def __init__(self):
        self.builder = StringBuilder()
        self.formatter = StringFormatter()
        self.processor = MemoryEfficientStringProcessor()
    
    def optimize_log_processing(self, log_lines: List[str]) -> Dict[str, Any]:
        """Optimize log file processing using all techniques."""
        start_time = time.time()
        
        # Use generator for memory efficiency
        def parse_log_line(line: str) -> Dict[str, str]:
            # Simple log parsing: timestamp level message
            parts = line.strip().split(' ', 2)
            if len(parts) >= 3:
                return {
                    'timestamp': parts[0],
                    'level': parts[1],
                    'message': parts[2]
                }
            return {'timestamp': '', 'level': '', 'message': line.strip()}
        
        # Process logs efficiently
        parsed_logs = [parse_log_line(line) for line in log_lines]
        
        # Build summary report using StringBuilder
        self.builder.clear()
        self.builder.append_line("LOG ANALYSIS REPORT")
        self.builder.append_line("=" * 40)
        self.builder.append_line()
        
        # Count log levels
        level_counts = {}
        for log in parsed_logs:
            level = log['level']
            level_counts[level] = level_counts.get(level, 0) + 1
        
        # Add statistics using efficient formatting
        for level, count in level_counts.items():
            line = f"{level}: {count} entries"
            self.builder.append_line(line)
        
        self.builder.append_line()
        self.builder.append_line(f"Total entries: {len(parsed_logs)}")
        
        processing_time = time.time() - start_time
        self.builder.append_line(f"Processing time: {processing_time:.4f} seconds")
        
        return {
            'report': self.builder.build(),
            'parsed_logs': parsed_logs,
            'level_counts': level_counts,
            'processing_time': processing_time
        }
    
    def generate_html_report(self, data: List[Dict[str, Any]]) -> str:
        """Generate HTML report using optimized string operations."""
        # Use StringIO for efficient building
        buffer = StringIO()
        
        # HTML header
        buffer.write("<!DOCTYPE html>\n")
        buffer.write("<html><head><title>Performance Report</title></head><body>\n")
        buffer.write("<h1>Performance Report</h1>\n")
        buffer.write("<table border='1'>\n")
        
        # Table header
        if data:
            buffer.write("<tr>")
            for key in data[0].keys():
                buffer.write(f"<th>{key}</th>")
            buffer.write("</tr>\n")
            
            # Table rows using efficient formatting
            for record in data:
                buffer.write("<tr>")
                for value in record.values():
                    buffer.write(f"<td>{value}</td>")
                buffer.write("</tr>\n")
        
        # HTML footer
        buffer.write("</table>\n")
        buffer.write("</body></html>\n")
        
        result = buffer.getvalue()
        buffer.close()
        return result
    
    def process_csv_data(self, csv_lines: List[str]) -> Dict[str, Any]:
        """Process CSV data with optimized string operations."""
        if not csv_lines:
            return {'headers': [], 'rows': [], 'summary': ''}
        
        # Parse header
        headers = csv_lines[0].split(',')
        
        # Process rows efficiently
        rows = []
        for line in csv_lines[1:]:
            row = line.split(',')
            rows.append(row)
        
        # Generate summary using StringBuilder
        self.builder.clear()
        self.builder.append_line("CSV DATA SUMMARY")
        self.builder.append_line("-" * 30)
        self.builder.append_line(f"Headers: {', '.join(headers)}")
        self.builder.append_line(f"Total rows: {len(rows)}")
        
        # Column statistics
        if rows:
            for i, header in enumerate(headers):
                values = [row[i] if i < len(row) else '' for row in rows]
                non_empty = len([v for v in values if v.strip()])
                self.builder.append_line(f"{header}: {non_empty} non-empty values")
        
        return {
            'headers': headers,
            'rows': rows,
            'summary': self.builder.build()
        }
    
    def benchmark_all_operations(self) -> Dict[str, float]:
        """Benchmark all string operations."""
        benchmarks = {}
        
        # Test data
        test_items = [f"item{i}" for i in range(5000)]
        
        # Benchmark concatenation
        start_time = time.time()
        result = "".join(test_items)
        benchmarks['join_concatenation'] = time.time() - start_time
        
        # Benchmark StringBuilder
        start_time = time.time()
        self.builder.clear()
        for item in test_items:
            self.builder.append(item)
        result = self.builder.build()
        benchmarks['string_builder'] = time.time() - start_time
        
        # Benchmark formatting
        start_time = time.time()
        for i in range(1000):
            result = f"Item {i}: value_{i}"
        benchmarks['f_string_formatting'] = time.time() - start_time
        
        # Benchmark StringIO
        start_time = time.time()
        buffer = StringIO()
        for item in test_items:
            buffer.write(item)
        result = buffer.getvalue()
        buffer.close()
        benchmarks['stringio_building'] = time.time() - start_time
        
        return benchmarks

def demonstrate_complete_optimization():
    """Demonstrate the complete string optimization suite."""
    suite = StringOptimizationSuite()
    
    print("=== COMPLETE STRING OPTIMIZATION DEMONSTRATION ===\n")
    
    # 1. Log processing optimization
    print("1. Log Processing Optimization:")
    log_lines = [
        "2025-01-01 INFO Application started",
        "2025-01-01 DEBUG Loading configuration",
        "2025-01-01 ERROR Database connection failed",
        "2025-01-01 INFO Retrying connection",
        "2025-01-01 INFO Connection successful"
    ]
    log_result = suite.optimize_log_processing(log_lines)
    print(log_result['report'])
    
    # 2. HTML report generation
    print("\n2. HTML Report Generation:")
    data = [
        {"name": "Alice", "score": 95, "department": "Engineering"},
        {"name": "Bob", "score": 87, "department": "Marketing"}
    ]
    html_report = suite.generate_html_report(data)
    print("HTML report generated (first 200 chars):")
    print(html_report[:200] + "...")
    
    # 3. CSV processing
    print("\n3. CSV Data Processing:")
    csv_lines = [
        "name,age,score,department",
        "Alice,30,95,Engineering",
        "Bob,25,87,Marketing",
        "Charlie,35,92,Engineering"
    ]
    csv_result = suite.process_csv_data(csv_lines)
    print(csv_result['summary'])
    
    # 4. Performance benchmarks
    print("\n4. Performance Benchmarks:")
    benchmarks = suite.benchmark_all_operations()
    for operation, time_taken in benchmarks.items():
        print(f"{operation}: {time_taken:.6f} seconds")
    
    return log_result, html_report, csv_result, benchmarks

# ===============================================================================
#                              MAIN DEMONSTRATION
# ===============================================================================

if __name__ == "__main__":
    print("STRING OPERATIONS PERFORMANCE OPTIMIZATION")
    print("=" * 60)
    
    # Run all demonstrations
    print("\n--- Step 1: Basic Concatenation Performance ---")
    demonstrate_concatenation_performance()
    
    print("\n--- Step 2: StringBuilder Usage ---")
    demonstrate_string_builder()
    
    print("\n--- Step 3: String Formatting Optimization ---")
    demonstrate_string_formatting()
    
    print("\n--- Step 4: Memory-Efficient Operations ---")
    demonstrate_memory_efficiency()
    
    print("\n--- Step 5: Complete Optimization Suite ---")
    demonstrate_complete_optimization()
    
    print("\n" + "=" * 60)
    print("STRING OPTIMIZATION COMPLETE!")
    print("Key takeaways:")
    print("- Use join() instead of + for concatenation")
    print("- Prefer f-strings for formatting")
    print("- Use StringIO for incremental building")
    print("- Apply generators for memory efficiency")
    print("- Combine techniques for maximum performance")
    print("=" * 60)

