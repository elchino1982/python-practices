"""Question: Implement the Composite pattern to treat individual objects and compositions uniformly.

Create a file system structure where files and directories can be treated uniformly,
allowing operations on both individual files and entire directory trees.

Requirements:
1. Create FileSystemComponent interface
2. Implement File (leaf) and Directory (composite) classes
3. Allow adding/removing components from directories
4. Implement operations that work on both files and directories
5. Demonstrate recursive operations on directory trees
6. Show uniform treatment of individual and composite objects

Example usage:
    root = Directory("root")
    file1 = File("document.txt", 100)
    folder1 = Directory("photos")
    root.add(file1)
    root.add(folder1)
    print(f"Total size: {root.get_size()}")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!

# Try to implement your solution here:
# (Write your code below this line)


















































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What is the common interface for files and directories?
# - How do files (leaves) behave differently from directories (composites)?
# - How can directories contain both files and other directories?
# - What operations should work uniformly on both?
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


# Step 1: Import modules and create the component interface
# ===============================================================================

# Explanation:
# The Composite pattern starts with a common interface that both leaf and
# composite objects implement. This allows uniform treatment of both types.

from abc import ABC, abstractmethod
from typing import List, Optional

class FileSystemComponent(ABC):
    """Abstract base class for file system components."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display the component with proper indentation."""
        pass
    
    def add(self, component: 'FileSystemComponent') -> None:
        """Add a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")
    
    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")
    
    def get_child(self, index: int) -> Optional['FileSystemComponent']:
        """Get child at index (only meaningful for composites)."""
        raise NotImplementedError("Leaf components have no children")

# What we accomplished in this step:
# - Created the common interface for all file system components
# - Defined abstract methods that both files and directories must implement
# - Added default implementations for composite-specific operations


# Step 2: Create the File class (leaf component)
# ===============================================================================

# Explanation:
# Leaf components represent end objects in the composition. They have no children
# and implement the component interface directly.

from abc import ABC, abstractmethod
from typing import List, Optional

class FileSystemComponent(ABC):
    """Abstract base class for file system components."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display the component with proper indentation."""
        pass
    
    def add(self, component: 'FileSystemComponent') -> None:
        """Add a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")
    
    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")
    
    def get_child(self, index: int) -> Optional['FileSystemComponent']:
        """Get child at index (only meaningful for composites)."""
        raise NotImplementedError("Leaf components have no children")

class File(FileSystemComponent):
    """Leaf component representing a file."""
    
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def get_size(self) -> int:
        """Return the file size."""
        return self.size
    
    def display(self, indent: int = 0) -> str:
        """Display the file with indentation."""
        return " " * indent + f"📄 {self.name} ({self.size} bytes)"

# What we accomplished in this step:
# - Created File class as a leaf component
# - Implemented required abstract methods
# - Files have a fixed size and cannot contain other components


# Step 3: Create the Directory class (composite component)
# ===============================================================================

# Explanation:
# Composite components can contain other components (both leaves and composites).
# They delegate operations to their children and aggregate results.

from abc import ABC, abstractmethod
from typing import List, Optional

class FileSystemComponent(ABC):
    """Abstract base class for file system components."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display the component with proper indentation."""
        pass
    
    def add(self, component: 'FileSystemComponent') -> None:
        """Add a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")
    
    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")
    
    def get_child(self, index: int) -> Optional['FileSystemComponent']:
        """Get child at index (only meaningful for composites)."""
        raise NotImplementedError("Leaf components have no children")

class File(FileSystemComponent):
    """Leaf component representing a file."""
    
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def get_size(self) -> int:
        """Return the file size."""
        return self.size
    
    def display(self, indent: int = 0) -> str:
        """Display the file with indentation."""
        return " " * indent + f"📄 {self.name} ({self.size} bytes)"

class Directory(FileSystemComponent):
    """Composite component representing a directory."""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent) -> None:
        """Add a component to this directory."""
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        """Remove a component from this directory."""
        if component in self.children:
            self.children.remove(component)
    
    def get_child(self, index: int) -> Optional[FileSystemComponent]:
        """Get child at the specified index."""
        if 0 <= index < len(self.children):
            return self.children[index]
        return None
    
    def get_size(self) -> int:
        """Return the total size of all contents."""
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
    
    def display(self, indent: int = 0) -> str:
        """Display the directory and its contents."""
        result = " " * indent + f"📁 {self.name}/ ({self.get_size()} bytes total)\n"
        for child in self.children:
            result += child.display(indent + 2) + "\n"
        return result.rstrip()

# What we accomplished in this step:
# - Created Directory class as a composite component
# - Implemented child management methods (add, remove, get_child)
# - Directory size is calculated by summing all children
# - Display method recursively shows all contents with proper indentation


# Step 4: Add additional file system operations
# ===============================================================================

# Explanation:
# Let's add more operations that demonstrate the power of the Composite pattern.
# These operations work uniformly on both files and directories.

from abc import ABC, abstractmethod
from typing import List, Optional

class FileSystemComponent(ABC):
    """Abstract base class for file system components."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display the component with proper indentation."""
        pass
    
    @abstractmethod
    def count_files(self) -> int:
        """Count the number of files in this component."""
        pass
    
    @abstractmethod
    def find(self, name: str) -> Optional['FileSystemComponent']:
        """Find a component by name."""
        pass
    
    def add(self, component: 'FileSystemComponent') -> None:
        """Add a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")
    
    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")
    
    def get_child(self, index: int) -> Optional['FileSystemComponent']:
        """Get child at index (only meaningful for composites)."""
        raise NotImplementedError("Leaf components have no children")

class File(FileSystemComponent):
    """Leaf component representing a file."""
    
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def get_size(self) -> int:
        """Return the file size."""
        return self.size
    
    def display(self, indent: int = 0) -> str:
        """Display the file with indentation."""
        return " " * indent + f"📄 {self.name} ({self.size} bytes)"
    
    def count_files(self) -> int:
        """A file counts as 1 file."""
        return 1
    
    def find(self, name: str) -> Optional['FileSystemComponent']:
        """Find this file if name matches."""
        return self if self.name == name else None

class Directory(FileSystemComponent):
    """Composite component representing a directory."""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent) -> None:
        """Add a component to this directory."""
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        """Remove a component from this directory."""
        if component in self.children:
            self.children.remove(component)
    
    def get_child(self, index: int) -> Optional[FileSystemComponent]:
        """Get child at the specified index."""
        if 0 <= index < len(self.children):
            return self.children[index]
        return None
    
    def get_size(self) -> int:
        """Return the total size of all contents."""
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
    
    def display(self, indent: int = 0) -> str:
        """Display the directory and its contents."""
        result = " " * indent + f"📁 {self.name}/ ({self.get_size()} bytes total)\n"
        for child in self.children:
            result += child.display(indent + 2) + "\n"
        return result.rstrip()
    
    def count_files(self) -> int:
        """Count all files in this directory and subdirectories."""
        total_files = 0
        for child in self.children:
            total_files += child.count_files()
        return total_files
    
    def find(self, name: str) -> Optional[FileSystemComponent]:
        """Find a component by name in this directory tree."""
        if self.name == name:
            return self
        
        for child in self.children:
            result = child.find(name)
            if result:
                return result
        
        return None

# What we accomplished in this step:
# - Added count_files() method that works recursively
# - Added find() method for searching the file system tree
# - Both operations work uniformly on files and directories
# - Demonstrated how composite pattern enables recursive operations


# Step 5: Basic demonstration of the Composite pattern
# ===============================================================================

# Explanation:
# Let's create a simple file system structure and demonstrate the uniform
# treatment of individual files and composite directories.

from abc import ABC, abstractmethod
from typing import List, Optional

class FileSystemComponent(ABC):
    """Abstract base class for file system components."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display the component with proper indentation."""
        pass
    
    @abstractmethod
    def count_files(self) -> int:
        """Count the number of files in this component."""
        pass
    
    @abstractmethod
    def find(self, name: str) -> Optional['FileSystemComponent']:
        """Find a component by name."""
        pass
    
    def add(self, component: 'FileSystemComponent') -> None:
        """Add a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")
    
    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")
    
    def get_child(self, index: int) -> Optional['FileSystemComponent']:
        """Get child at index (only meaningful for composites)."""
        raise NotImplementedError("Leaf components have no children")

class File(FileSystemComponent):
    """Leaf component representing a file."""
    
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def get_size(self) -> int:
        """Return the file size."""
        return self.size
    
    def display(self, indent: int = 0) -> str:
        """Display the file with indentation."""
        return " " * indent + f"📄 {self.name} ({self.size} bytes)"
    
    def count_files(self) -> int:
        """A file counts as 1 file."""
        return 1
    
    def find(self, name: str) -> Optional['FileSystemComponent']:
        """Find this file if name matches."""
        return self if self.name == name else None

class Directory(FileSystemComponent):
    """Composite component representing a directory."""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent) -> None:
        """Add a component to this directory."""
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        """Remove a component from this directory."""
        if component in self.children:
            self.children.remove(component)
    
    def get_child(self, index: int) -> Optional[FileSystemComponent]:
        """Get child at the specified index."""
        if 0 <= index < len(self.children):
            return self.children[index]
        return None
    
    def get_size(self) -> int:
        """Return the total size of all contents."""
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
    
    def display(self, indent: int = 0) -> str:
        """Display the directory and its contents."""
        result = " " * indent + f"📁 {self.name}/ ({self.get_size()} bytes total)\n"
        for child in self.children:
            result += child.display(indent + 2) + "\n"
        return result.rstrip()
    
    def count_files(self) -> int:
        """Count all files in this directory and subdirectories."""
        total_files = 0
        for child in self.children:
            total_files += child.count_files()
        return total_files
    
    def find(self, name: str) -> Optional[FileSystemComponent]:
        """Find a component by name in this directory tree."""
        if self.name == name:
            return self
        
        for child in self.children:
            result = child.find(name)
            if result:
                return result
        
        return None

print("=== Basic Composite Pattern Demo ===\n")

# Create individual files
file1 = File("document.txt", 1024)
file2 = File("image.jpg", 2048)
file3 = File("readme.md", 512)

# Create directories
root = Directory("root")
photos = Directory("photos")
documents = Directory("documents")

# Build the file system structure
root.add(file1)
root.add(photos)
root.add(documents)

photos.add(file2)
documents.add(file3)

# Demonstrate uniform treatment
print("1. File System Structure:")
print(root.display())
print()

print("2. Individual File Operations:")
print(f"File size: {file1.get_size()} bytes")
print(f"File count: {file1.count_files()}")
print()

print("3. Directory Operations (same interface!):")
print(f"Total size: {root.get_size()} bytes")
print(f"Total files: {root.count_files()}")

# What we accomplished in this step:
# - Created a basic file system structure
# - Demonstrated uniform treatment of files and directories
# - Showed how the same operations work on both leaf and composite objects


# Step 6: Complete demonstration with complex operations
# ===============================================================================

# Explanation:
# Let's create a more complex file system and demonstrate advanced operations
# like searching, adding/removing components, and recursive operations.

from abc import ABC, abstractmethod
from typing import List, Optional

class FileSystemComponent(ABC):
    """Abstract base class for file system components."""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display the component with proper indentation."""
        pass
    
    @abstractmethod
    def count_files(self) -> int:
        """Count the number of files in this component."""
        pass
    
    @abstractmethod
    def find(self, name: str) -> Optional['FileSystemComponent']:
        """Find a component by name."""
        pass
    
    def add(self, component: 'FileSystemComponent') -> None:
        """Add a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot add to a leaf component")
    
    def remove(self, component: 'FileSystemComponent') -> None:
        """Remove a component (only meaningful for composites)."""
        raise NotImplementedError("Cannot remove from a leaf component")
    
    def get_child(self, index: int) -> Optional['FileSystemComponent']:
        """Get child at index (only meaningful for composites)."""
        raise NotImplementedError("Leaf components have no children")

class File(FileSystemComponent):
    """Leaf component representing a file."""
    
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def get_size(self) -> int:
        """Return the file size."""
        return self.size
    
    def display(self, indent: int = 0) -> str:
        """Display the file with indentation."""
        return " " * indent + f"📄 {self.name} ({self.size} bytes)"
    
    def count_files(self) -> int:
        """A file counts as 1 file."""
        return 1
    
    def find(self, name: str) -> Optional['FileSystemComponent']:
        """Find this file if name matches."""
        return self if self.name == name else None

class Directory(FileSystemComponent):
    """Composite component representing a directory."""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent) -> None:
        """Add a component to this directory."""
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        """Remove a component from this directory."""
        if component in self.children:
            self.children.remove(component)
    
    def get_child(self, index: int) -> Optional[FileSystemComponent]:
        """Get child at the specified index."""
        if 0 <= index < len(self.children):
            return self.children[index]
        return None
    
    def get_size(self) -> int:
        """Return the total size of all contents."""
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size
    
    def display(self, indent: int = 0) -> str:
        """Display the directory and its contents."""
        result = " " * indent + f"📁 {self.name}/ ({self.get_size()} bytes total)\n"
        for child in self.children:
            result += child.display(indent + 2) + "\n"
        return result.rstrip()
    
    def count_files(self) -> int:
        """Count all files in this directory and subdirectories."""
        total_files = 0
        for child in self.children:
            total_files += child.count_files()
        return total_files
    
    def find(self, name: str) -> Optional[FileSystemComponent]:
        """Find a component by name in this directory tree."""
        if self.name == name:
            return self
        
        for child in self.children:
            result = child.find(name)
            if result:
                return result
        
        return None

print("=== Complete Composite Pattern Demo ===\n")

# Create a complex file system structure
root = Directory("root")
home = Directory("home")
user = Directory("user")
projects = Directory("projects")
photos = Directory("photos")
documents = Directory("documents")

# Create files
config_file = File("config.txt", 256)
readme_file = File("README.md", 1024)
photo1 = File("vacation.jpg", 3072)
photo2 = File("family.png", 2048)
doc1 = File("report.pdf", 4096)
doc2 = File("notes.txt", 512)
project_file = File("main.py", 2048)

# Build the directory structure
root.add(config_file)
root.add(home)
home.add(user)
user.add(projects)
user.add(photos)
user.add(documents)

projects.add(readme_file)
projects.add(project_file)
photos.add(photo1)
photos.add(photo2)
documents.add(doc1)
documents.add(doc2)

print("1. Complete File System Structure:")
print(root.display())
print()

print("2. Recursive Operations:")
print(f"Total size of entire system: {root.get_size()} bytes")
print(f"Total files in system: {root.count_files()}")
print(f"Size of user directory: {user.get_size()} bytes")
print(f"Files in photos directory: {photos.count_files()}")
print()

print("3. Search Operations:")
found_file = root.find("main.py")
if found_file:
    print(f"Found file: {found_file.name} ({found_file.get_size()} bytes)")

found_dir = root.find("photos")
if found_dir:
    print(f"Found directory: {found_dir.name} ({found_dir.get_size()} bytes total)")
print()

print("4. Dynamic Operations:")
# Add a new file to photos
new_photo = File("sunset.jpg", 1536)
photos.add(new_photo)
print(f"After adding sunset.jpg:")
print(f"Photos directory size: {photos.get_size()} bytes")
print(f"Total system size: {root.get_size()} bytes")
print()

# Remove a file
photos.remove(photo1)
print(f"After removing vacation.jpg:")
print(f"Photos directory size: {photos.get_size()} bytes")
print(f"Files in photos: {photos.count_files()}")
print()

print("5. Uniform Treatment Demonstration:")
components = [config_file, photos, user, root]
for component in components:
    print(f"{component.name}: {component.get_size()} bytes, {component.count_files()} files")

# What we accomplished in this step:
# - Created a complex nested file system structure
# - Demonstrated recursive operations working at any level
# - Showed dynamic addition and removal of components
# - Illustrated uniform treatment of all component types
# - Proved that the same interface works for both simple and complex structures


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step Composite pattern solution!
#
# Key concepts learned:
# - Composite pattern structure: Component, Leaf, Composite
# - Uniform treatment of individual objects and compositions
# - Recursive operations that work on tree structures
# - Dynamic composition and decomposition
# - Transparent interface for clients
# - Tree traversal and search operations
#
# The Composite pattern is powerful because:
# - Clients can treat individual objects and compositions uniformly
# - You can build complex tree structures from simple components
# - Operations work recursively without client knowledge of structure
# - Easy to add new component types
# - Simplifies client code by providing a consistent interface
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding file permissions!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
