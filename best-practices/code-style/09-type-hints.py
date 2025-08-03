"""Question: Master Python Type Hints for better code quality and IDE support.

Learn how to use type hints effectively to make your code more readable,
maintainable, and catch errors early during development.

Requirements:
1. Basic type annotations for variables and functions
2. Collection types (List, Dict, Set, Tuple)
3. Optional and Union types
4. Generic types and TypeVar
5. Protocol and structural typing
6. Advanced type hints with Callable and Literal

Example usage:
    def process_user_data(users: List[Dict[str, Any]]) -> Optional[str]:
        return users[0]['name'] if users else None
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what types you need to annotate
# - Start with simple type hints
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
# - What are the basic Python types you can annotate?
# - How do you handle collections like lists and dictionaries?
# - When should you use Optional vs Union?
# - How do generics help with reusable code?
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


# Step 1: Basic type annotations for variables and simple functions
# ===============================================================================

# Explanation:
# Type hints help make your code more readable and catch errors early.
# Let's start with the most basic type annotations.

# Basic variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

def greet(name: str) -> str:
    """Simple function with type hints."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area."""
    return length * width

# What we accomplished in this step:
# - Added basic type annotations for variables
# - Created simple functions with parameter and return type hints
# - Used fundamental types: str, int, float, bool


# Step 2: Collection types (List, Dict, Set, Tuple)
# ===============================================================================

# Explanation:
# Collections need type hints for both the container and the elements inside.
# This helps catch errors when working with data structures.

from typing import List, Dict, Set, Tuple

# Basic variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

# Collection type annotations
names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
unique_ids: Set[int] = {1, 2, 3, 4, 5}
coordinates: Tuple[float, float] = (10.5, 20.3)
person_info: Tuple[str, int, bool] = ("Alice", 30, True)

def greet(name: str) -> str:
    """Simple function with type hints."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area."""
    return length * width

def process_names(names: List[str]) -> List[str]:
    """Convert all names to uppercase."""
    return [name.upper() for name in names]

def get_student_grade(grades: Dict[str, int], student: str) -> int:
    """Get a student's grade from the grades dictionary."""
    return grades.get(student, 0)

def find_common_elements(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Find common elements between two sets."""
    return set1.intersection(set2)

def get_coordinates() -> Tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)

# What we accomplished in this step:
# - Added collection type annotations: List, Dict, Set, Tuple
# - Showed how to specify element types within collections
# - Created functions that work with typed collections


# Step 3: Optional and Union types
# ===============================================================================

# Explanation:
# Optional is used when a value can be None. Union allows multiple types.
# These are essential for handling real-world scenarios with missing data.

from typing import List, Dict, Set, Tuple, Optional, Union

# Basic variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

# Collection type annotations
names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
unique_ids: Set[int] = {1, 2, 3, 4, 5}
coordinates: Tuple[float, float] = (10.5, 20.3)
person_info: Tuple[str, int, bool] = ("Alice", 30, True)

# Optional and Union type annotations
middle_name: Optional[str] = None  # Can be str or None
user_id: Union[int, str] = "user123"  # Can be int or str
mixed_data: List[Union[int, str]] = [1, "hello", 2, "world"]

def greet(name: str) -> str:
    """Simple function with type hints."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area."""
    return length * width

def process_names(names: List[str]) -> List[str]:
    """Convert all names to uppercase."""
    return [name.upper() for name in names]

def get_student_grade(grades: Dict[str, int], student: str) -> int:
    """Get a student's grade from the grades dictionary."""
    return grades.get(student, 0)

def find_common_elements(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Find common elements between two sets."""
    return set1.intersection(set2)

def get_coordinates() -> Tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)

def find_user(user_id: Union[int, str]) -> Optional[str]:
    """Find user by ID (can be int or str), return name or None."""
    users = {1: "Alice", "user123": "Bob", 2: "Charlie"}
    return users.get(user_id)

def get_full_name(first: str, last: str, middle: Optional[str] = None) -> str:
    """Create full name with optional middle name."""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

def process_mixed_data(data: List[Union[int, str]]) -> List[str]:
    """Convert mixed data to strings."""
    return [str(item) for item in data]

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers, return None if division by zero."""
    if b == 0:
        return None
    return a / b

# What we accomplished in this step:
# - Added Optional type for values that can be None
# - Used Union type for values that can be multiple types
# - Created functions that handle optional parameters and return values


# Step 4: Generic types and TypeVar
# ===============================================================================

# Explanation:
# Generic types allow you to write reusable code that works with multiple types.
# TypeVar creates type variables for generic programming.

from typing import List, Dict, Set, Tuple, Optional, Union, TypeVar, Generic

# Type variables for generic programming
T = TypeVar('T')  # Generic type variable
K = TypeVar('K')  # Key type variable
V = TypeVar('V')  # Value type variable

# Basic variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

# Collection type annotations
names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
unique_ids: Set[int] = {1, 2, 3, 4, 5}
coordinates: Tuple[float, float] = (10.5, 20.3)
person_info: Tuple[str, int, bool] = ("Alice", 30, True)

# Optional and Union type annotations
middle_name: Optional[str] = None  # Can be str or None
user_id: Union[int, str] = "user123"  # Can be int or str
mixed_data: List[Union[int, str]] = [1, "hello", 2, "world"]

def greet(name: str) -> str:
    """Simple function with type hints."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area."""
    return length * width

def process_names(names: List[str]) -> List[str]:
    """Convert all names to uppercase."""
    return [name.upper() for name in names]

def get_student_grade(grades: Dict[str, int], student: str) -> int:
    """Get a student's grade from the grades dictionary."""
    return grades.get(student, 0)

def find_common_elements(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Find common elements between two sets."""
    return set1.intersection(set2)

def get_coordinates() -> Tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)

def find_user(user_id: Union[int, str]) -> Optional[str]:
    """Find user by ID (can be int or str), return name or None."""
    users = {1: "Alice", "user123": "Bob", 2: "Charlie"}
    return users.get(user_id)

def get_full_name(first: str, last: str, middle: Optional[str] = None) -> str:
    """Create full name with optional middle name."""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

def process_mixed_data(data: List[Union[int, str]]) -> List[str]:
    """Convert mixed data to strings."""
    return [str(item) for item in data]

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers, return None if division by zero."""
    if b == 0:
        return None
    return a / b

# Generic functions using TypeVar
def get_first_item(items: List[T]) -> Optional[T]:
    """Get the first item from a list of any type."""
    return items[0] if items else None

def swap_pair(a: T, b: T) -> Tuple[T, T]:
    """Swap two items of the same type."""
    return b, a

def create_pair(item: T) -> Tuple[T, T]:
    """Create a pair from a single item."""
    return item, item

# Generic class example
class Stack(Generic[T]):
    """Generic stack implementation."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Pop an item from the stack."""
        return self._items.pop() if self._items else None
    
    def peek(self) -> Optional[T]:
        """Peek at the top item without removing it."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0

# Generic function with multiple type variables
def merge_dicts(dict1: Dict[K, V], dict2: Dict[K, V]) -> Dict[K, V]:
    """Merge two dictionaries with the same key and value types."""
    result = dict1.copy()
    result.update(dict2)
    return result

# What we accomplished in this step:
# - Introduced TypeVar for creating generic type variables
# - Created generic functions that work with any type
# - Built a generic Stack class using Generic[T]
# - Showed how to use multiple type variables in one function


# Step 5: Protocol and structural typing
# ===============================================================================

# Explanation:
# Protocol allows structural typing - defining interfaces based on what methods
# an object has rather than inheritance. This is like duck typing but with type hints.

from typing import List, Dict, Set, Tuple, Optional, Union, TypeVar, Generic, Protocol

# Type variables for generic programming
T = TypeVar('T')  # Generic type variable
K = TypeVar('K')  # Key type variable
V = TypeVar('V')  # Value type variable

# Protocol definitions for structural typing
class Drawable(Protocol):
    """Protocol for objects that can be drawn."""
    
    def draw(self) -> str:
        """Draw the object and return a string representation."""
        ...

class Comparable(Protocol):
    """Protocol for objects that can be compared."""
    
    def __lt__(self, other: 'Comparable') -> bool:
        """Less than comparison."""
        ...

class Serializable(Protocol):
    """Protocol for objects that can be serialized."""
    
    def to_dict(self) -> Dict[str, any]:
        """Convert object to dictionary."""
        ...
    
    def from_dict(self, data: Dict[str, any]) -> None:
        """Load object from dictionary."""
        ...

# Basic variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

# Collection type annotations
names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
unique_ids: Set[int] = {1, 2, 3, 4, 5}
coordinates: Tuple[float, float] = (10.5, 20.3)
person_info: Tuple[str, int, bool] = ("Alice", 30, True)

# Optional and Union type annotations
middle_name: Optional[str] = None  # Can be str or None
user_id: Union[int, str] = "user123"  # Can be int or str
mixed_data: List[Union[int, str]] = [1, "hello", 2, "world"]

def greet(name: str) -> str:
    """Simple function with type hints."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area."""
    return length * width

def process_names(names: List[str]) -> List[str]:
    """Convert all names to uppercase."""
    return [name.upper() for name in names]

def get_student_grade(grades: Dict[str, int], student: str) -> int:
    """Get a student's grade from the grades dictionary."""
    return grades.get(student, 0)

def find_common_elements(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Find common elements between two sets."""
    return set1.intersection(set2)

def get_coordinates() -> Tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)

def find_user(user_id: Union[int, str]) -> Optional[str]:
    """Find user by ID (can be int or str), return name or None."""
    users = {1: "Alice", "user123": "Bob", 2: "Charlie"}
    return users.get(user_id)

def get_full_name(first: str, last: str, middle: Optional[str] = None) -> str:
    """Create full name with optional middle name."""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

def process_mixed_data(data: List[Union[int, str]]) -> List[str]:
    """Convert mixed data to strings."""
    return [str(item) for item in data]

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers, return None if division by zero."""
    if b == 0:
        return None
    return a / b

# Generic functions using TypeVar
def get_first_item(items: List[T]) -> Optional[T]:
    """Get the first item from a list of any type."""
    return items[0] if items else None

def swap_pair(a: T, b: T) -> Tuple[T, T]:
    """Swap two items of the same type."""
    return b, a

def create_pair(item: T) -> Tuple[T, T]:
    """Create a pair from a single item."""
    return item, item

# Generic class example
class Stack(Generic[T]):
    """Generic stack implementation."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Pop an item from the stack."""
        return self._items.pop() if self._items else None
    
    def peek(self) -> Optional[T]:
        """Peek at the top item without removing it."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0

# Generic function with multiple type variables
def merge_dicts(dict1: Dict[K, V], dict2: Dict[K, V]) -> Dict[K, V]:
    """Merge two dictionaries with the same key and value types."""
    result = dict1.copy()
    result.update(dict2)
    return result

# Functions using Protocol types
def render_objects(objects: List[Drawable]) -> List[str]:
    """Render a list of drawable objects."""
    return [obj.draw() for obj in objects]

def sort_items(items: List[Comparable]) -> List[Comparable]:
    """Sort a list of comparable items."""
    return sorted(items)

def save_objects(objects: List[Serializable]) -> List[Dict[str, any]]:
    """Save a list of serializable objects to dictionaries."""
    return [obj.to_dict() for obj in objects]

# Example classes that implement protocols
class Circle:
    """Circle class that implements Drawable protocol."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Circle with radius {self.radius}"

class Rectangle:
    """Rectangle class that implements Drawable protocol."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        return f"Rectangle {self.width}x{self.height}"

class Person:
    """Person class that implements Serializable protocol."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def to_dict(self) -> Dict[str, any]:
        return {"name": self.name, "age": self.age}
    
    def from_dict(self, data: Dict[str, any]) -> None:
        self.name = data["name"]
        self.age = data["age"]

# What we accomplished in this step:
# - Introduced Protocol for structural typing
# - Created protocols for common interfaces (Drawable, Comparable, Serializable)
# - Showed how classes can implement protocols without inheritance
# - Demonstrated functions that work with protocol types


# Step 6: Advanced type hints with Callable and Literal
# ===============================================================================

# Explanation:
# Callable is used for function types, and Literal restricts values to specific literals.
# These provide even more precise type information for complex scenarios.

from typing import List, Dict, Set, Tuple, Optional, Union, TypeVar, Generic, Protocol, Callable, Literal, Any

# Type variables for generic programming
T = TypeVar('T')  # Generic type variable
K = TypeVar('K')  # Key type variable
V = TypeVar('V')  # Value type variable

# Protocol definitions for structural typing
class Drawable(Protocol):
    """Protocol for objects that can be drawn."""
    
    def draw(self) -> str:
        """Draw the object and return a string representation."""
        ...

class Comparable(Protocol):
    """Protocol for objects that can be compared."""
    
    def __lt__(self, other: 'Comparable') -> bool:
        """Less than comparison."""
        ...

class Serializable(Protocol):
    """Protocol for objects that can be serialized."""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert object to dictionary."""
        ...
    
    def from_dict(self, data: Dict[str, Any]) -> None:
        """Load object from dictionary."""
        ...

# Literal types for restricted values
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]
HttpMethod = Literal["GET", "POST", "PUT", "DELETE"]
SortOrder = Literal["asc", "desc"]

# Basic variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

# Collection type annotations
names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
unique_ids: Set[int] = {1, 2, 3, 4, 5}
coordinates: Tuple[float, float] = (10.5, 20.3)
person_info: Tuple[str, int, bool] = ("Alice", 30, True)

# Optional and Union type annotations
middle_name: Optional[str] = None  # Can be str or None
user_id: Union[int, str] = "user123"  # Can be int or str
mixed_data: List[Union[int, str]] = [1, "hello", 2, "world"]

# Callable type annotations
simple_func: Callable[[int, int], int] = lambda x, y: x + y
string_processor: Callable[[str], str] = str.upper
validator: Callable[[Any], bool] = lambda x: x is not None

def greet(name: str) -> str:
    """Simple function with type hints."""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area."""
    return length * width

def process_names(names: List[str]) -> List[str]:
    """Convert all names to uppercase."""
    return [name.upper() for name in names]

def get_student_grade(grades: Dict[str, int], student: str) -> int:
    """Get a student's grade from the grades dictionary."""
    return grades.get(student, 0)

def find_common_elements(set1: Set[int], set2: Set[int]) -> Set[int]:
    """Find common elements between two sets."""
    return set1.intersection(set2)

def get_coordinates() -> Tuple[float, float]:
    """Return x, y coordinates."""
    return (10.5, 20.3)

def find_user(user_id: Union[int, str]) -> Optional[str]:
    """Find user by ID (can be int or str), return name or None."""
    users = {1: "Alice", "user123": "Bob", 2: "Charlie"}
    return users.get(user_id)

def get_full_name(first: str, last: str, middle: Optional[str] = None) -> str:
    """Create full name with optional middle name."""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

def process_mixed_data(data: List[Union[int, str]]) -> List[str]:
    """Convert mixed data to strings."""
    return [str(item) for item in data]

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers, return None if division by zero."""
    if b == 0:
        return None
    return a / b

# Generic functions using TypeVar
def get_first_item(items: List[T]) -> Optional[T]:
    """Get the first item from a list of any type."""
    return items[0] if items else None

def swap_pair(a: T, b: T) -> Tuple[T, T]:
    """Swap two items of the same type."""
    return b, a

def create_pair(item: T) -> Tuple[T, T]:
    """Create a pair from a single item."""
    return item, item

# Generic class example
class Stack(Generic[T]):
    """Generic stack implementation."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Pop an item from the stack."""
        return self._items.pop() if self._items else None
    
    def peek(self) -> Optional[T]:
        """Peek at the top item without removing it."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0

# Generic function with multiple type variables
def merge_dicts(dict1: Dict[K, V], dict2: Dict[K, V]) -> Dict[K, V]:
    """Merge two dictionaries with the same key and value types."""
    result = dict1.copy()
    result.update(dict2)
    return result

# Functions using Protocol types
def render_objects(objects: List[Drawable]) -> List[str]:
    """Render a list of drawable objects."""
    return [obj.draw() for obj in objects]

def sort_items(items: List[Comparable]) -> List[Comparable]:
    """Sort a list of comparable items."""
    return sorted(items)

def save_objects(objects: List[Serializable]) -> List[Dict[str, Any]]:
    """Save a list of serializable objects to dictionaries."""
    return [obj.to_dict() for obj in objects]

# Example classes that implement protocols
class Circle:
    """Circle class that implements Drawable protocol."""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Circle with radius {self.radius}"

class Rectangle:
    """Rectangle class that implements Drawable protocol."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        return f"Rectangle {self.width}x{self.height}"

class Person:
    """Person class that implements Serializable protocol."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name, "age": self.age}
    
    def from_dict(self, data: Dict[str, Any]) -> None:
        self.name = data["name"]
        self.age = data["age"]

# Advanced functions using Callable and Literal
def apply_operation(numbers: List[int], operation: Callable[[int, int], int]) -> int:
    """Apply a binary operation to a list of numbers."""
    result = numbers[0]
    for num in numbers[1:]:
        result = operation(result, num)
    return result

def log_message(message: str, level: LogLevel = "INFO") -> str:
    """Log a message with a specific level."""
    return f"[{level}] {message}"

def make_request(url: str, method: HttpMethod = "GET") -> str:
    """Make an HTTP request with specified method."""
    return f"{method} request to {url}"

def sort_data(data: List[T], order: SortOrder = "asc") -> List[T]:
    """Sort data in ascending or descending order."""
    return sorted(data, reverse=(order == "desc"))

def filter_data(data: List[T], predicate: Callable[[T], bool]) -> List[T]:
    """Filter data using a predicate function."""
    return [item for item in data if predicate(item)]

def transform_data(data: List[T], transformer: Callable[[T], V]) -> List[V]:
    """Transform data using a transformer function."""
    return [transformer(item) for item in data]

# Higher-order function examples
def create_multiplier(factor: int) -> Callable[[int], int]:
    """Create a multiplier function."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

def compose_functions(f: Callable[[T], V], g: Callable[[V], K]) -> Callable[[T], K]:
    """Compose two functions."""
    def composed(x: T) -> K:
        return g(f(x))
    return composed

# Decorator with type hints
def retry(max_attempts: int) -> Callable[[Callable[..., T]], Callable[..., Optional[T]]]:
    """Decorator that retries a function on failure."""
    def decorator(func: Callable[..., T]) -> Callable[..., Optional[T]]:
        def wrapper(*args: Any, **kwargs: Any) -> Optional[T]:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts - 1:
                        return None
                    continue
            return None
        return wrapper
    return decorator

# What we accomplished in this step:
# - Added Callable type for function parameters and return values
# - Used Literal types to restrict values to specific literals
# - Created higher-order functions with proper type hints
# - Showed decorator typing with complex Callable signatures
# - Demonstrated real-world examples of advanced type hints


# ===============================================================================
#                           COMPLETE DEMONSTRATION
# ===============================================================================

# Example usage of all type hint concepts
def main() -> None:
    """Demonstrate all type hint concepts."""
    
    # Basic types
    print(greet("World"))
    print(add_numbers(5, 3))
    
    # Collections
    student_names = ["Alice", "Bob", "Charlie"]
    print(process_names(student_names))
    
    # Optional and Union
    print(get_full_name("John", "Doe", "Smith"))
    print(find_user("user123"))
    
    # Generics
    string_stack: Stack[str] = Stack()
    string_stack.push("hello")
    string_stack.push("world")
    print(string_stack.pop())
    
    # Protocols
    shapes: List[Drawable] = [Circle(5.0), Rectangle(3.0, 4.0)]
    print(render_objects(shapes))
    
    # Callable and Literal
    numbers = [1, 2, 3, 4, 5]
    result = apply_operation(numbers, lambda x, y: x + y)
    print(f"Sum: {result}")
    
    print(log_message("System started", "INFO"))
    print(make_request("https://api.example.com", "POST"))
    
    # Higher-order functions
    double = create_multiplier(2)
    print(f"Double of 5: {double(5)}")
    
    # Filter and transform
    even_numbers = filter_data(numbers, lambda x: x % 2 == 0)
    squared_numbers = transform_data(numbers, lambda x: x ** 2)
    print(f"Even numbers: {even_numbers}")
    print(f"Squared numbers: {squared_numbers}")

if __name__ == "__main__":
    main()

# FINAL SUMMARY
# =============
# 
# This comprehensive type hints tutorial covered:
# 1. Basic type annotations for variables and functions
# 2. Collection types (List, Dict, Set, Tuple) with element types
# 3. Optional and Union types for handling None and multiple types
# 4. Generic types and TypeVar for reusable, type-safe code
# 5. Protocol for structural typing and duck typing with type safety
# 6. Advanced types like Callable and Literal for precise type control
#
# Type hints make your code more readable, help catch errors early,
# and provide better IDE support with autocomplete and error detection.
# They're especially valuable in larger codebases and team environments.
