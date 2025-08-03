"""Question: Implement I/O optimization techniques for better performance.

Create examples demonstrating various I/O optimization strategies including
buffering, async I/O, memory mapping, and efficient file operations.

Requirements:
1. Demonstrate file reading/writing optimizations
2. Show buffering strategies
3. Implement async I/O operations
4. Use memory mapping for large files
5. Compare performance of different approaches

Example usage:
    optimizer = IOOptimizer()
    optimizer.compare_file_operations()
    optimizer.demonstrate_async_io()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about different I/O bottlenecks
# - Start with simple file operations
# - Test performance differences
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
# - What are common I/O bottlenecks?
# - How does buffering improve performance?
# - When should you use async I/O?
# - What are the benefits of memory mapping?
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


# Step 1: Import modules and create basic file operations
# ===============================================================================

# Explanation:
# I/O optimization starts with understanding basic file operations and their
# performance characteristics. We'll create a foundation for testing.

import os
import time
import tempfile
from typing import List, Dict, Any

class BasicFileOperations:
    """Basic file operations for performance comparison."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_file.txt")
    
    def create_test_file(self, size_mb: int = 10) -> str:
        """Create a test file of specified size."""
        content = "This is a test line for I/O performance testing.\n" * (size_mb * 1024 * 10)
        
        with open(self.test_file, 'w') as f:
            f.write(content)
        
        return self.test_file
    
    def read_file_basic(self, filename: str) -> str:
        """Basic file reading without optimization."""
        with open(filename, 'r') as f:
            return f.read()
    
    def write_file_basic(self, filename: str, content: str) -> None:
        """Basic file writing without optimization."""
        with open(filename, 'w') as f:
            f.write(content)
    
    def cleanup(self):
        """Clean up temporary files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)

# What we accomplished in this step:
# - Created basic file operations class
# - Added test file creation functionality
# - Established foundation for performance testing


# Step 2: Add buffered I/O operations
# ===============================================================================

# Explanation:
# Buffering reduces the number of system calls by reading/writing larger chunks
# of data at once. This significantly improves performance for large files.

import os
import time
import tempfile
from typing import List, Dict, Any

class BasicFileOperations:
    """Basic file operations for performance comparison."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_file.txt")
    
    def create_test_file(self, size_mb: int = 10) -> str:
        """Create a test file of specified size."""
        content = "This is a test line for I/O performance testing.\n" * (size_mb * 1024 * 10)
        
        with open(self.test_file, 'w') as f:
            f.write(content)
        
        return self.test_file
    
    def read_file_basic(self, filename: str) -> str:
        """Basic file reading without optimization."""
        with open(filename, 'r') as f:
            return f.read()
    
    def write_file_basic(self, filename: str, content: str) -> None:
        """Basic file writing without optimization."""
        with open(filename, 'w') as f:
            f.write(content)
    
    def cleanup(self):
        """Clean up temporary files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)

class BufferedFileOperations:
    """Buffered file operations for improved performance."""
    
    def __init__(self, buffer_size: int = 8192):
        self.buffer_size = buffer_size
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_buffered(self, filename: str) -> str:
        """Read file using custom buffer size."""
        content = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            while True:
                chunk = f.read(self.buffer_size)
                if not chunk:
                    break
                content.append(chunk)
        return ''.join(content)
    
    def write_file_buffered(self, filename: str, content: str) -> None:
        """Write file using buffered operations."""
        with open(filename, 'w', buffering=self.buffer_size) as f:
            # Write in chunks to demonstrate buffering
            for i in range(0, len(content), self.buffer_size):
                f.write(content[i:i + self.buffer_size])
    
    def copy_file_buffered(self, source: str, destination: str) -> None:
        """Copy file using buffered operations."""
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            while True:
                chunk = src.read(self.buffer_size)
                if not chunk:
                    break
                dst.write(chunk)
    
    def read_lines_buffered(self, filename: str) -> List[str]:
        """Read file line by line with buffering."""
        lines = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            for line in f:
                lines.append(line.strip())
        return lines
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

# What we accomplished in this step:
# - Added buffered file operations with custom buffer sizes
# - Implemented chunked reading and writing
# - Added line-by-line reading with buffering


# Step 3: Add async I/O operations
# ===============================================================================

# Explanation:
# Async I/O allows non-blocking operations, enabling concurrent processing
# of multiple I/O operations for better performance in I/O-bound applications.

import os
import time
import tempfile
import asyncio
import aiofiles
from typing import List, Dict, Any

class BasicFileOperations:
    """Basic file operations for performance comparison."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_file.txt")
    
    def create_test_file(self, size_mb: int = 10) -> str:
        """Create a test file of specified size."""
        content = "This is a test line for I/O performance testing.\n" * (size_mb * 1024 * 10)
        
        with open(self.test_file, 'w') as f:
            f.write(content)
        
        return self.test_file
    
    def read_file_basic(self, filename: str) -> str:
        """Basic file reading without optimization."""
        with open(filename, 'r') as f:
            return f.read()
    
    def write_file_basic(self, filename: str, content: str) -> None:
        """Basic file writing without optimization."""
        with open(filename, 'w') as f:
            f.write(content)
    
    def cleanup(self):
        """Clean up temporary files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)

class BufferedFileOperations:
    """Buffered file operations for improved performance."""
    
    def __init__(self, buffer_size: int = 8192):
        self.buffer_size = buffer_size
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_buffered(self, filename: str) -> str:
        """Read file using custom buffer size."""
        content = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            while True:
                chunk = f.read(self.buffer_size)
                if not chunk:
                    break
                content.append(chunk)
        return ''.join(content)
    
    def write_file_buffered(self, filename: str, content: str) -> None:
        """Write file using buffered operations."""
        with open(filename, 'w', buffering=self.buffer_size) as f:
            # Write in chunks to demonstrate buffering
            for i in range(0, len(content), self.buffer_size):
                f.write(content[i:i + self.buffer_size])
    
    def copy_file_buffered(self, source: str, destination: str) -> None:
        """Copy file using buffered operations."""
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            while True:
                chunk = src.read(self.buffer_size)
                if not chunk:
                    break
                dst.write(chunk)
    
    def read_lines_buffered(self, filename: str) -> List[str]:
        """Read file line by line with buffering."""
        lines = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            for line in f:
                lines.append(line.strip())
        return lines
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class AsyncFileOperations:
    """Async file operations for concurrent I/O."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    async def read_file_async(self, filename: str) -> str:
        """Read file asynchronously."""
        async with aiofiles.open(filename, 'r') as f:
            return await f.read()
    
    async def write_file_async(self, filename: str, content: str) -> None:
        """Write file asynchronously."""
        async with aiofiles.open(filename, 'w') as f:
            await f.write(content)
    
    async def read_multiple_files_async(self, filenames: List[str]) -> List[str]:
        """Read multiple files concurrently."""
        tasks = [self.read_file_async(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    async def write_multiple_files_async(self, file_data: Dict[str, str]) -> None:
        """Write multiple files concurrently."""
        tasks = [
            self.write_file_async(filename, content)
            for filename, content in file_data.items()
        ]
        await asyncio.gather(*tasks)
    
    async def copy_file_async(self, source: str, destination: str, chunk_size: int = 8192) -> None:
        """Copy file asynchronously with chunked reading."""
        async with aiofiles.open(source, 'rb') as src:
            async with aiofiles.open(destination, 'wb') as dst:
                while True:
                    chunk = await src.read(chunk_size)
                    if not chunk:
                        break
                    await dst.write(chunk)
    
    async def process_files_concurrently(self, filenames: List[str], processor_func) -> List[Any]:
        """Process multiple files concurrently with a custom function."""
        tasks = [processor_func(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

# What we accomplished in this step:
# - Added async file operations using aiofiles
# - Implemented concurrent file reading and writing
# - Added support for processing multiple files simultaneously


# Step 4: Add memory mapping operations
# ===============================================================================

# Explanation:
# Memory mapping allows direct access to file contents in memory, providing
# very fast random access and efficient handling of large files.

import os
import time
import tempfile
import asyncio
import aiofiles
import mmap
from typing import List, Dict, Any

class BasicFileOperations:
    """Basic file operations for performance comparison."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_file.txt")
    
    def create_test_file(self, size_mb: int = 10) -> str:
        """Create a test file of specified size."""
        content = "This is a test line for I/O performance testing.\n" * (size_mb * 1024 * 10)
        
        with open(self.test_file, 'w') as f:
            f.write(content)
        
        return self.test_file
    
    def read_file_basic(self, filename: str) -> str:
        """Basic file reading without optimization."""
        with open(filename, 'r') as f:
            return f.read()
    
    def write_file_basic(self, filename: str, content: str) -> None:
        """Basic file writing without optimization."""
        with open(filename, 'w') as f:
            f.write(content)
    
    def cleanup(self):
        """Clean up temporary files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)

class BufferedFileOperations:
    """Buffered file operations for improved performance."""
    
    def __init__(self, buffer_size: int = 8192):
        self.buffer_size = buffer_size
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_buffered(self, filename: str) -> str:
        """Read file using custom buffer size."""
        content = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            while True:
                chunk = f.read(self.buffer_size)
                if not chunk:
                    break
                content.append(chunk)
        return ''.join(content)
    
    def write_file_buffered(self, filename: str, content: str) -> None:
        """Write file using buffered operations."""
        with open(filename, 'w', buffering=self.buffer_size) as f:
            # Write in chunks to demonstrate buffering
            for i in range(0, len(content), self.buffer_size):
                f.write(content[i:i + self.buffer_size])
    
    def copy_file_buffered(self, source: str, destination: str) -> None:
        """Copy file using buffered operations."""
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            while True:
                chunk = src.read(self.buffer_size)
                if not chunk:
                    break
                dst.write(chunk)
    
    def read_lines_buffered(self, filename: str) -> List[str]:
        """Read file line by line with buffering."""
        lines = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            for line in f:
                lines.append(line.strip())
        return lines
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class AsyncFileOperations:
    """Async file operations for concurrent I/O."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    async def read_file_async(self, filename: str) -> str:
        """Read file asynchronously."""
        async with aiofiles.open(filename, 'r') as f:
            return await f.read()
    
    async def write_file_async(self, filename: str, content: str) -> None:
        """Write file asynchronously."""
        async with aiofiles.open(filename, 'w') as f:
            await f.write(content)
    
    async def read_multiple_files_async(self, filenames: List[str]) -> List[str]:
        """Read multiple files concurrently."""
        tasks = [self.read_file_async(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    async def write_multiple_files_async(self, file_data: Dict[str, str]) -> None:
        """Write multiple files concurrently."""
        tasks = [
            self.write_file_async(filename, content)
            for filename, content in file_data.items()
        ]
        await asyncio.gather(*tasks)
    
    async def copy_file_async(self, source: str, destination: str, chunk_size: int = 8192) -> None:
        """Copy file asynchronously with chunked reading."""
        async with aiofiles.open(source, 'rb') as src:
            async with aiofiles.open(destination, 'wb') as dst:
                while True:
                    chunk = await src.read(chunk_size)
                    if not chunk:
                        break
                    await dst.write(chunk)
    
    async def process_files_concurrently(self, filenames: List[str], processor_func) -> List[Any]:
        """Process multiple files concurrently with a custom function."""
        tasks = [processor_func(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class MemoryMappedOperations:
    """Memory-mapped file operations for large file handling."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_mmap(self, filename: str) -> str:
        """Read file using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                return mm.read().decode('utf-8')
    
    def search_in_file_mmap(self, filename: str, pattern: bytes) -> List[int]:
        """Search for pattern in file using memory mapping."""
        positions = []
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                start = 0
                while True:
                    pos = mm.find(pattern, start)
                    if pos == -1:
                        break
                    positions.append(pos)
                    start = pos + 1
        return positions
    
    def read_file_slice_mmap(self, filename: str, start: int, length: int) -> str:
        """Read a specific slice of file using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                mm.seek(start)
                return mm.read(length).decode('utf-8')
    
    def modify_file_mmap(self, filename: str, position: int, new_data: bytes) -> None:
        """Modify file at specific position using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0) as mm:
                mm.seek(position)
                mm.write(new_data)
                mm.flush()
    
    def copy_file_mmap(self, source: str, destination: str) -> None:
        """Copy file using memory mapping."""
        with open(source, 'r+b') as src_f:
            with mmap.mmap(src_f.fileno(), 0, access=mmap.ACCESS_READ) as src_mm:
                with open(destination, 'w+b') as dst_f:
                    dst_f.write(src_mm.read())
    
    def analyze_file_mmap(self, filename: str) -> Dict[str, Any]:
        """Analyze file content using memory mapping."""
        stats = {
            'size': 0,
            'lines': 0,
            'words': 0,
            'chars': 0
        }
        
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                stats['size'] = len(mm)
                content = mm.read().decode('utf-8')
                stats['lines'] = content.count('\n')
                stats['words'] = len(content.split())
                stats['chars'] = len(content)
        
        return stats
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

# What we accomplished in this step:
# - Added memory-mapped file operations for large files
# - Implemented efficient file searching and slicing
# - Added in-place file modification capabilities


# Step 5: Create performance comparison and optimization manager
# ===============================================================================

# Explanation:
# The IOOptimizer class brings together all optimization techniques and provides
# performance comparisons to demonstrate the benefits of each approach.

import os
import time
import tempfile
import asyncio
import aiofiles
import mmap
from typing import List, Dict, Any, Callable

class BasicFileOperations:
    """Basic file operations for performance comparison."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_file.txt")
    
    def create_test_file(self, size_mb: int = 10) -> str:
        """Create a test file of specified size."""
        content = "This is a test line for I/O performance testing.\n" * (size_mb * 1024 * 10)
        
        with open(self.test_file, 'w') as f:
            f.write(content)
        
        return self.test_file
    
    def read_file_basic(self, filename: str) -> str:
        """Basic file reading without optimization."""
        with open(filename, 'r') as f:
            return f.read()
    
    def write_file_basic(self, filename: str, content: str) -> None:
        """Basic file writing without optimization."""
        with open(filename, 'w') as f:
            f.write(content)
    
    def cleanup(self):
        """Clean up temporary files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)

class BufferedFileOperations:
    """Buffered file operations for improved performance."""
    
    def __init__(self, buffer_size: int = 8192):
        self.buffer_size = buffer_size
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_buffered(self, filename: str) -> str:
        """Read file using custom buffer size."""
        content = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            while True:
                chunk = f.read(self.buffer_size)
                if not chunk:
                    break
                content.append(chunk)
        return ''.join(content)
    
    def write_file_buffered(self, filename: str, content: str) -> None:
        """Write file using buffered operations."""
        with open(filename, 'w', buffering=self.buffer_size) as f:
            # Write in chunks to demonstrate buffering
            for i in range(0, len(content), self.buffer_size):
                f.write(content[i:i + self.buffer_size])
    
    def copy_file_buffered(self, source: str, destination: str) -> None:
        """Copy file using buffered operations."""
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            while True:
                chunk = src.read(self.buffer_size)
                if not chunk:
                    break
                dst.write(chunk)
    
    def read_lines_buffered(self, filename: str) -> List[str]:
        """Read file line by line with buffering."""
        lines = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            for line in f:
                lines.append(line.strip())
        return lines
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class AsyncFileOperations:
    """Async file operations for concurrent I/O."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    async def read_file_async(self, filename: str) -> str:
        """Read file asynchronously."""
        async with aiofiles.open(filename, 'r') as f:
            return await f.read()
    
    async def write_file_async(self, filename: str, content: str) -> None:
        """Write file asynchronously."""
        async with aiofiles.open(filename, 'w') as f:
            await f.write(content)
    
    async def read_multiple_files_async(self, filenames: List[str]) -> List[str]:
        """Read multiple files concurrently."""
        tasks = [self.read_file_async(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    async def write_multiple_files_async(self, file_data: Dict[str, str]) -> None:
        """Write multiple files concurrently."""
        tasks = [
            self.write_file_async(filename, content)
            for filename, content in file_data.items()
        ]
        await asyncio.gather(*tasks)
    
    async def copy_file_async(self, source: str, destination: str, chunk_size: int = 8192) -> None:
        """Copy file asynchronously with chunked reading."""
        async with aiofiles.open(source, 'rb') as src:
            async with aiofiles.open(destination, 'wb') as dst:
                while True:
                    chunk = await src.read(chunk_size)
                    if not chunk:
                        break
                    await dst.write(chunk)
    
    async def process_files_concurrently(self, filenames: List[str], processor_func) -> List[Any]:
        """Process multiple files concurrently with a custom function."""
        tasks = [processor_func(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class MemoryMappedOperations:
    """Memory-mapped file operations for large file handling."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_mmap(self, filename: str) -> str:
        """Read file using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                return mm.read().decode('utf-8')
    
    def search_in_file_mmap(self, filename: str, pattern: bytes) -> List[int]:
        """Search for pattern in file using memory mapping."""
        positions = []
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                start = 0
                while True:
                    pos = mm.find(pattern, start)
                    if pos == -1:
                        break
                    positions.append(pos)
                    start = pos + 1
        return positions
    
    def read_file_slice_mmap(self, filename: str, start: int, length: int) -> str:
        """Read a specific slice of file using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                mm.seek(start)
                return mm.read(length).decode('utf-8')
    
    def modify_file_mmap(self, filename: str, position: int, new_data: bytes) -> None:
        """Modify file at specific position using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0) as mm:
                mm.seek(position)
                mm.write(new_data)
                mm.flush()
    
    def copy_file_mmap(self, source: str, destination: str) -> None:
        """Copy file using memory mapping."""
        with open(source, 'r+b') as src_f:
            with mmap.mmap(src_f.fileno(), 0, access=mmap.ACCESS_READ) as src_mm:
                with open(destination, 'w+b') as dst_f:
                    dst_f.write(src_mm.read())
    
    def analyze_file_mmap(self, filename: str) -> Dict[str, Any]:
        """Analyze file content using memory mapping."""
        stats = {
            'size': 0,
            'lines': 0,
            'words': 0,
            'chars': 0
        }
        
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                stats['size'] = len(mm)
                content = mm.read().decode('utf-8')
                stats['lines'] = content.count('\n')
                stats['words'] = len(content.split())
                stats['chars'] = len(content)
        
        return stats
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class IOOptimizer:
    """Main class that demonstrates and compares I/O optimization techniques."""
    
    def __init__(self):
        self.basic_ops = BasicFileOperations()
        self.buffered_ops = BufferedFileOperations()
        self.async_ops = AsyncFileOperations()
        self.mmap_ops = MemoryMappedOperations()
        self.test_files = []
    
    def measure_time(self, func: Callable, *args, **kwargs) -> tuple:
        """Measure execution time of a function."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    
    async def measure_time_async(self, coro, *args, **kwargs) -> tuple:
        """Measure execution time of an async function."""
        start_time = time.time()
        result = await coro(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    
    def compare_file_operations(self, file_size_mb: int = 5) -> Dict[str, float]:
        """Compare performance of different file reading methods."""
        print(f"=== Comparing File Reading Performance ({file_size_mb}MB file) ===\n")
        
        # Create test file
        test_file = self.basic_ops.create_test_file(file_size_mb)
        self.test_files.append(test_file)
        
        results = {}
        
        # Basic reading
        _, basic_time = self.measure_time(self.basic_ops.read_file_basic, test_file)
        results['Basic'] = basic_time
        print(f"Basic reading: {basic_time:.4f} seconds")
        
        # Buffered reading
        _, buffered_time = self.measure_time(self.buffered_ops.read_file_buffered, test_file)
        results['Buffered'] = buffered_time
        print(f"Buffered reading: {buffered_time:.4f} seconds")
        
        # Memory mapped reading
        _, mmap_time = self.measure_time(self.mmap_ops.read_file_mmap, test_file)
        results['Memory Mapped'] = mmap_time
        print(f"Memory mapped reading: {mmap_time:.4f} seconds")
        
        print(f"\nPerformance improvement:")
        print(f"Buffered vs Basic: {(basic_time/buffered_time):.2f}x faster")
        print(f"Memory Mapped vs Basic: {(basic_time/mmap_time):.2f}x faster")
        print()
        
        return results
    
    async def demonstrate_async_io(self) -> None:
        """Demonstrate async I/O performance benefits."""
        print("=== Demonstrating Async I/O Performance ===\n")
        
        # Create multiple test files
        file_data = {}
        for i in range(5):
            filename = os.path.join(self.async_ops.temp_dir, f"async_test_{i}.txt")
            content = f"Test file {i} content\n" * 1000
            file_data[filename] = content
            self.test_files.append(filename)
        
        # Sequential writing
        start_time = time.time()
        for filename, content in file_data.items():
            with open(filename, 'w') as f:
                f.write(content)
        sequential_time = time.time() - start_time
        
        # Async concurrent writing
        _, async_time = await self.measure_time_async(
            self.async_ops.write_multiple_files_async, file_data
        )
        
        print(f"Sequential writing: {sequential_time:.4f} seconds")
        print(f"Async concurrent writing: {async_time:.4f} seconds")
        print(f"Async improvement: {(sequential_time/async_time):.2f}x faster")
        print()
    
    def demonstrate_memory_mapping_benefits(self) -> None:
        """Demonstrate memory mapping benefits for large file operations."""
        print("=== Demonstrating Memory Mapping Benefits ===\n")
        
        # Create a large test file
        large_file = self.basic_ops.create_test_file(20)  # 20MB file
        self.test_files.append(large_file)
        
        # Search for pattern using basic method
        pattern = b"performance"
        
        def basic_search():
            with open(large_file, 'rb') as f:
                content = f.read()
                positions = []
                start = 0
                while True:
                    pos = content.find(pattern, start)
                    if pos == -1:
                        break
                    positions.append(pos)
                    start = pos + 1
                return positions
        
        _, basic_search_time = self.measure_time(basic_search)
        _, mmap_search_time = self.measure_time(
            self.mmap_ops.search_in_file_mmap, large_file, pattern
        )
        
        print(f"Basic pattern search: {basic_search_time:.4f} seconds")
        print(f"Memory mapped search: {mmap_search_time:.4f} seconds")
        print(f"Memory mapping improvement: {(basic_search_time/mmap_search_time):.2f}x faster")
        
        # Demonstrate file analysis
        stats = self.mmap_ops.analyze_file_mmap(large_file)
        print(f"\nFile analysis results:")
        print(f"Size: {stats['size']:,} bytes")
        print(f"Lines: {stats['lines']:,}")
        print(f"Words: {stats['words']:,}")
        print(f"Characters: {stats['chars']:,}")
        print()
    
    def cleanup(self):
        """Clean up all temporary files and directories."""
        self.basic_ops.cleanup()
        self.buffered_ops.cleanup()
        self.async_ops.cleanup()
        self.mmap_ops.cleanup()
        
        # Clean up additional test files
        for file_path in self.test_files:
            if os.path.exists(file_path):
                os.remove(file_path)

# What we accomplished in this step:
# - Created comprehensive IOOptimizer class
# - Added performance measurement and comparison tools
# - Implemented demonstrations for all optimization techniques


# Step 6: Test the complete implementation
# ===============================================================================

# Explanation:
# Let's test our I/O optimization implementation with comprehensive demonstrations
# of all techniques and their performance benefits.

import os
import time
import tempfile
import asyncio
import aiofiles
import mmap
from typing import List, Dict, Any, Callable

class BasicFileOperations:
    """Basic file operations for performance comparison."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_file.txt")
    
    def create_test_file(self, size_mb: int = 10) -> str:
        """Create a test file of specified size."""
        content = "This is a test line for I/O performance testing.\n" * (size_mb * 1024 * 10)
        
        with open(self.test_file, 'w') as f:
            f.write(content)
        
        return self.test_file
    
    def read_file_basic(self, filename: str) -> str:
        """Basic file reading without optimization."""
        with open(filename, 'r') as f:
            return f.read()
    
    def write_file_basic(self, filename: str, content: str) -> None:
        """Basic file writing without optimization."""
        with open(filename, 'w') as f:
            f.write(content)
    
    def cleanup(self):
        """Clean up temporary files."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)

class BufferedFileOperations:
    """Buffered file operations for improved performance."""
    
    def __init__(self, buffer_size: int = 8192):
        self.buffer_size = buffer_size
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_buffered(self, filename: str) -> str:
        """Read file using custom buffer size."""
        content = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            while True:
                chunk = f.read(self.buffer_size)
                if not chunk:
                    break
                content.append(chunk)
        return ''.join(content)
    
    def write_file_buffered(self, filename: str, content: str) -> None:
        """Write file using buffered operations."""
        with open(filename, 'w', buffering=self.buffer_size) as f:
            # Write in chunks to demonstrate buffering
            for i in range(0, len(content), self.buffer_size):
                f.write(content[i:i + self.buffer_size])
    
    def copy_file_buffered(self, source: str, destination: str) -> None:
        """Copy file using buffered operations."""
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            while True:
                chunk = src.read(self.buffer_size)
                if not chunk:
                    break
                dst.write(chunk)
    
    def read_lines_buffered(self, filename: str) -> List[str]:
        """Read file line by line with buffering."""
        lines = []
        with open(filename, 'r', buffering=self.buffer_size) as f:
            for line in f:
                lines.append(line.strip())
        return lines
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class AsyncFileOperations:
    """Async file operations for concurrent I/O."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    async def read_file_async(self, filename: str) -> str:
        """Read file asynchronously."""
        async with aiofiles.open(filename, 'r') as f:
            return await f.read()
    
    async def write_file_async(self, filename: str, content: str) -> None:
        """Write file asynchronously."""
        async with aiofiles.open(filename, 'w') as f:
            await f.write(content)
    
    async def read_multiple_files_async(self, filenames: List[str]) -> List[str]:
        """Read multiple files concurrently."""
        tasks = [self.read_file_async(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    async def write_multiple_files_async(self, file_data: Dict[str, str]) -> None:
        """Write multiple files concurrently."""
        tasks = [
            self.write_file_async(filename, content)
            for filename, content in file_data.items()
        ]
        await asyncio.gather(*tasks)
    
    async def copy_file_async(self, source: str, destination: str, chunk_size: int = 8192) -> None:
        """Copy file asynchronously with chunked reading."""
        async with aiofiles.open(source, 'rb') as src:
            async with aiofiles.open(destination, 'wb') as dst:
                while True:
                    chunk = await src.read(chunk_size)
                    if not chunk:
                        break
                    await dst.write(chunk)
    
    async def process_files_concurrently(self, filenames: List[str], processor_func) -> List[Any]:
        """Process multiple files concurrently with a custom function."""
        tasks = [processor_func(filename) for filename in filenames]
        return await asyncio.gather(*tasks)
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class MemoryMappedOperations:
    """Memory-mapped file operations for large file handling."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def read_file_mmap(self, filename: str) -> str:
        """Read file using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                return mm.read().decode('utf-8')
    
    def search_in_file_mmap(self, filename: str, pattern: bytes) -> List[int]:
        """Search for pattern in file using memory mapping."""
        positions = []
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                start = 0
                while True:
                    pos = mm.find(pattern, start)
                    if pos == -1:
                        break
                    positions.append(pos)
                    start = pos + 1
        return positions
    
    def read_file_slice_mmap(self, filename: str, start: int, length: int) -> str:
        """Read a specific slice of file using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                mm.seek(start)
                return mm.read(length).decode('utf-8')
    
    def modify_file_mmap(self, filename: str, position: int, new_data: bytes) -> None:
        """Modify file at specific position using memory mapping."""
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0) as mm:
                mm.seek(position)
                mm.write(new_data)
                mm.flush()
    
    def copy_file_mmap(self, source: str, destination: str) -> None:
        """Copy file using memory mapping."""
        with open(source, 'r+b') as src_f:
            with mmap.mmap(src_f.fileno(), 0, access=mmap.ACCESS_READ) as src_mm:
                with open(destination, 'w+b') as dst_f:
                    dst_f.write(src_mm.read())
    
    def analyze_file_mmap(self, filename: str) -> Dict[str, Any]:
        """Analyze file content using memory mapping."""
        stats = {
            'size': 0,
            'lines': 0,
            'words': 0,
            'chars': 0
        }
        
        with open(filename, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                stats['size'] = len(mm)
                content = mm.read().decode('utf-8')
                stats['lines'] = content.count('\n')
                stats['words'] = len(content.split())
                stats['chars'] = len(content)
        
        return stats
    
    def cleanup(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

class IOOptimizer:
    """Main class that demonstrates and compares I/O optimization techniques."""
    
    def __init__(self):
        self.basic_ops = BasicFileOperations()
        self.buffered_ops = BufferedFileOperations()
        self.async_ops = AsyncFileOperations()
        self.mmap_ops = MemoryMappedOperations()
        self.test_files = []
    
    def measure_time(self, func: Callable, *args, **kwargs) -> tuple:
        """Measure execution time of a function."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    
    async def measure_time_async(self, coro, *args, **kwargs) -> tuple:
        """Measure execution time of an async function."""
        start_time = time.time()
        result = await coro(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    
    def compare_file_operations(self, file_size_mb: int = 5) -> Dict[str, float]:
        """Compare performance of different file reading methods."""
        print(f"=== Comparing File Reading Performance ({file_size_mb}MB file) ===\n")
        
        # Create test file
        test_file = self.basic_ops.create_test_file(file_size_mb)
        self.test_files.append(test_file)
        
        results = {}
        
        # Basic reading
        _, basic_time = self.measure_time(self.basic_ops.read_file_basic, test_file)
        results['Basic'] = basic_time
        print(f"Basic reading: {basic_time:.4f} seconds")
        
        # Buffered reading
        _, buffered_time = self.measure_time(self.buffered_ops.read_file_buffered, test_file)
        results['Buffered'] = buffered_time
        print(f"Buffered reading: {buffered_time:.4f} seconds")
        
        # Memory mapped reading
        _, mmap_time = self.measure_time(self.mmap_ops.read_file_mmap, test_file)
        results['Memory Mapped'] = mmap_time
        print(f"Memory mapped reading: {mmap_time:.4f} seconds")
        
        print(f"\nPerformance improvement:")
        print(f"Buffered vs Basic: {(basic_time/buffered_time):.2f}x faster")
        print(f"Memory Mapped vs Basic: {(basic_time/mmap_time):.2f}x faster")
        print()
        
        return results
    
    async def demonstrate_async_io(self) -> None:
        """Demonstrate async I/O performance benefits."""
        print("=== Demonstrating Async I/O Performance ===\n")
        
        # Create multiple test files
        file_data = {}
        for i in range(5):
            filename = os.path.join(self.async_ops.temp_dir, f"async_test_{i}.txt")
            content = f"Test file {i} content\n" * 1000
            file_data[filename] = content
            self.test_files.append(filename)
        
        # Sequential writing
        start_time = time.time()
        for filename, content in file_data.items():
            with open(filename, 'w') as f:
                f.write(content)
        sequential_time = time.time() - start_time
        
        # Async concurrent writing
        _, async_time = await self.measure_time_async(
            self.async_ops.write_multiple_files_async, file_data
        )
        
        print(f"Sequential writing: {sequential_time:.4f} seconds")
        print(f"Async concurrent writing: {async_time:.4f} seconds")
        print(f"Async improvement: {(sequential_time/async_time):.2f}x faster")
        print()
    
    def demonstrate_memory_mapping_benefits(self) -> None:
        """Demonstrate memory mapping benefits for large file operations."""
        print("=== Demonstrating Memory Mapping Benefits ===\n")
        
        # Create a large test file
        large_file = self.basic_ops.create_test_file(20)  # 20MB file
        self.test_files.append(large_file)
        
        # Search for pattern using basic method
        pattern = b"performance"
        
        def basic_search():
            with open(large_file, 'rb') as f:
                content = f.read()
                positions = []
                start = 0
                while True:
                    pos = content.find(pattern, start)
                    if pos == -1:
                        break
                    positions.append(pos)
                    start = pos + 1
                return positions
        
        _, basic_search_time = self.measure_time(basic_search)
        _, mmap_search_time = self.measure_time(
            self.mmap_ops.search_in_file_mmap, large_file, pattern
        )
        
        print(f"Basic pattern search: {basic_search_time:.4f} seconds")
        print(f"Memory mapped search: {mmap_search_time:.4f} seconds")
        print(f"Memory mapping improvement: {(basic_search_time/mmap_search_time):.2f}x faster")
        
        # Demonstrate file analysis
        stats = self.mmap_ops.analyze_file_mmap(large_file)
        print(f"\nFile analysis results:")
        print(f"Size: {stats['size']:,} bytes")
        print(f"Lines: {stats['lines']:,}")
        print(f"Words: {stats['words']:,}")
        print(f"Characters: {stats['chars']:,}")
        print()
    
    def cleanup(self):
        """Clean up all temporary files and directories."""
        self.basic_ops.cleanup()
        self.buffered_ops.cleanup()
        self.async_ops.cleanup()
        self.mmap_ops.cleanup()
        
        # Clean up additional test files
        for file_path in self.test_files:
            if os.path.exists(file_path):
                os.remove(file_path)

# Test the complete I/O optimization implementation
async def main():
    """Main function to test all I/O optimization techniques."""
    print("=== Testing I/O Optimization Techniques ===\n")
    
    optimizer = IOOptimizer()
    
    try:
        # Test file reading performance
        optimizer.compare_file_operations(file_size_mb=3)
        
        # Test async I/O performance
        await optimizer.demonstrate_async_io()
        
        # Test memory mapping benefits
        optimizer.demonstrate_memory_mapping_benefits()
        
        # Additional demonstrations
        print("=== Additional I/O Optimization Tips ===\n")
        print("1. Use appropriate buffer sizes (8KB-64KB typically optimal)")
        print("2. Consider async I/O for I/O-bound applications")
        print("3. Memory mapping is excellent for large files and random access")
        print("4. Batch operations when possible to reduce system call overhead")
        print("5. Use binary mode for non-text files to avoid encoding overhead")
        print("6. Consider using pathlib for path operations")
        print("7. Use context managers to ensure proper file closure")
        print("8. Profile your specific use case to choose the best approach")
        
    finally:
        # Always clean up resources
        optimizer.cleanup()
        print("\n=== Cleanup completed ===")

# Run the demonstration
if __name__ == "__main__":
    # Note: In real usage, you might need to install aiofiles:
    # pip install aiofiles
    
    try:
        asyncio.run(main())
    except ImportError:
        print("Note: aiofiles not available. Running synchronous tests only.")
        optimizer = IOOptimizer()
        try:
            optimizer.compare_file_operations(file_size_mb=3)
            optimizer.demonstrate_memory_mapping_benefits()
        finally:
            optimizer.cleanup()

# What we accomplished in this step:
# - Created comprehensive test suite for all I/O optimization techniques
# - Added main function with complete demonstrations
# - Included practical tips for I/O optimization
# - Added proper error handling and cleanup


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Basic vs optimized file operations
# - Buffering strategies and their impact
# - Async I/O for concurrent operations
# - Memory mapping for large file handling
# - Performance measurement and comparison
# - Practical optimization techniques
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each optimization technique
# 3. Understand WHY each approach is faster
# 4. Experiment with different file sizes and buffer sizes
# 5. Try implementing your own optimization strategies
#
# Remember: The best way to learn is by doing!
# ===============================================================================
