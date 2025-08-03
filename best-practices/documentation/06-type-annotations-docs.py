"""Question: Master type annotations and their documentation in Python.

Learn how to use type hints effectively for better code documentation,
IDE support, and static type checking.

Requirements:
1. Basic type annotations for variables, functions, and classes
2. Advanced type annotations with generics and unions
3. Type aliases and custom types
4. Documentation integration with type hints
5. Best practices for type annotation documentation

Example usage:
    user = User("John", 25)
    result = process_user_data(user)
    print(f"Processed: {result}")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what types and annotations you need
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
# - What basic types do you need to annotate?
# - How do you document function parameters and return types?
# - What advanced types like Union, Optional, List are useful?
# - How do type hints improve documentation?
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


# Step 1: Import typing modules and basic type annotations
# ===============================================================================

# Explanation:
# Type annotations start with importing the necessary typing modules.
# We'll begin with basic variable and function annotations.

from typing import List, Dict, Optional, Union, Tuple, Any, Callable
from typing import TypeVar, Generic, Protocol
from dataclasses import dataclass
from enum import Enum

# Basic variable type annotations
name: str = "John Doe"
age: int = 25
height: float = 5.9
is_active: bool = True

# Basic function with type annotations
def greet_user(name: str, age: int) -> str:
    """Greet a user with their name and age.
    
    Args:
        name: The user's name
        age: The user's age
        
    Returns:
        A greeting message
    """
    return f"Hello {name}, you are {age} years old!"


# Step 2: Collection type annotations and Optional types
# ===============================================================================

# Explanation:
# Collections need type annotations for their contents.
# Optional types handle None values gracefully.

# Collection type annotations
names: List[str] = ["Alice", "Bob", "Charlie"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}
coordinates: Tuple[float, float] = (10.5, 20.3)

# Optional and Union types
middle_name: Optional[str] = None  # Can be str or None
user_id: Union[int, str] = "user_123"  # Can be int or str

def process_scores(scores: Dict[str, int], 
                  threshold: Optional[int] = None) -> List[str]:
    """Process student scores and return names above threshold.
    
    Args:
        scores: Dictionary mapping student names to their scores
        threshold: Minimum score to include (default: 80)
        
    Returns:
        List of student names who scored above threshold
        
    Example:
        >>> scores = {"Alice": 95, "Bob": 75}
        >>> process_scores(scores, 80)
        ['Alice']
    """
    if threshold is None:
        threshold = 80
    
    return [name for name, score in scores.items() if score >= threshold]

def find_user(users: List[Dict[str, Any]], 
              user_id: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Find a user by ID in a list of user dictionaries.
    
    Args:
        users: List of user dictionaries
        user_id: User ID to search for (can be int or string)
        
    Returns:
        User dictionary if found, None otherwise
        
    Note:
        This function demonstrates Union types for flexible input
        and Optional return type for cases where user isn't found.
    """
    for user in users:
        if user.get("id") == user_id:
            return user
    return None


# Step 3: Class type annotations and dataclasses
# ===============================================================================

# Explanation:
# Classes benefit greatly from type annotations, especially with dataclasses.
# We'll create typed classes with proper documentation.

from typing import List, Dict, Optional, Union, Tuple, Any, Callable
from typing import TypeVar, Generic, Protocol
from dataclasses import dataclass
from enum import Enum

class UserRole(Enum):
    """Enumeration of user roles with type safety."""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

@dataclass
class User:
    """User class with comprehensive type annotations.
    
    Attributes:
        name: Full name of the user
        age: Age in years
        email: Email address
        role: User role from UserRole enum
        preferences: Dictionary of user preferences
        is_active: Whether the user account is active
    """
    name: str
    age: int
    email: str
    role: UserRole = UserRole.USER
    preferences: Dict[str, Any] = None
    is_active: bool = True
    
    def __post_init__(self) -> None:
        """Initialize default preferences if None."""
        if self.preferences is None:
            self.preferences = {}
    
    def update_preferences(self, new_prefs: Dict[str, Any]) -> None:
        """Update user preferences.
        
        Args:
            new_prefs: Dictionary of new preference values
            
        Example:
            >>> user = User("John", 25, "john@example.com")
            >>> user.update_preferences({"theme": "dark", "notifications": True})
        """
        self.preferences.update(new_prefs)
    
    def get_preference(self, key: str, default: Any = None) -> Any:
        """Get a specific preference value.
        
        Args:
            key: Preference key to retrieve
            default: Default value if key not found
            
        Returns:
            Preference value or default
        """
        return self.preferences.get(key, default)

class UserManager:
    """Manages a collection of users with type-safe operations."""
    
    def __init__(self) -> None:
        """Initialize empty user collection."""
        self._users: Dict[str, User] = {}
    
    def add_user(self, user: User) -> bool:
        """Add a user to the collection.
        
        Args:
            user: User instance to add
            
        Returns:
            True if user was added, False if email already exists
        """
        if user.email in self._users:
            return False
        self._users[user.email] = user
        return True
    
    def get_user(self, email: str) -> Optional[User]:
        """Retrieve a user by email.
        
        Args:
            email: Email address to search for
            
        Returns:
            User instance if found, None otherwise
        """
        return self._users.get(email)
    
    def get_users_by_role(self, role: UserRole) -> List[User]:
        """Get all users with a specific role.
        
        Args:
            role: UserRole to filter by
            
        Returns:
            List of users with the specified role
        """
        return [user for user in self._users.values() if user.role == role]
    
    def get_active_users(self) -> List[User]:
        """Get all active users.
        
        Returns:
            List of active users
        """
        return [user for user in self._users.values() if user.is_active]


# Step 4: Advanced type annotations - Generics and TypeVars
# ===============================================================================

# Explanation:
# Advanced typing includes generics, type variables, and protocols.
# These provide more flexible and reusable type-safe code.

# Import all previous imports plus new ones
from typing import List, Dict, Optional, Union, Tuple, Any, Callable
from typing import TypeVar, Generic, Protocol
from dataclasses import dataclass
from enum import Enum

# Type variables for generic programming
T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class Repository(Generic[T]):
    """Generic repository pattern with type safety.
    
    Type Parameters:
        T: The type of objects stored in this repository
        
    Example:
        >>> user_repo = Repository[User]()
        >>> user_repo.add(User("John", 25, "john@example.com"))
    """
    
    def __init__(self) -> None:
        """Initialize empty repository."""
        self._items: Dict[str, T] = {}
    
    def add(self, key: str, item: T) -> None:
        """Add an item to the repository.
        
        Args:
            key: Unique identifier for the item
            item: Item to store
        """
        self._items[key] = item
    
    def get(self, key: str) -> Optional[T]:
        """Retrieve an item by key.
        
        Args:
            key: Key to search for
            
        Returns:
            Item if found, None otherwise
        """
        return self._items.get(key)
    
    def get_all(self) -> List[T]:
        """Get all items in the repository.
        
        Returns:
            List of all stored items
        """
        return list(self._items.values())
    
    def filter_by(self, predicate: Callable[[T], bool]) -> List[T]:
        """Filter items using a predicate function.
        
        Args:
            predicate: Function that returns True for items to include
            
        Returns:
            List of items that match the predicate
            
        Example:
            >>> active_users = user_repo.filter_by(lambda u: u.is_active)
        """
        return [item for item in self._items.values() if predicate(item)]

class Cache(Generic[K, V]):
    """Generic cache with key-value type safety.
    
    Type Parameters:
        K: Type of cache keys
        V: Type of cache values
    """
    
    def __init__(self, max_size: int = 100) -> None:
        """Initialize cache with maximum size.
        
        Args:
            max_size: Maximum number of items to cache
        """
        self._cache: Dict[K, V] = {}
        self._max_size = max_size
    
    def get(self, key: K) -> Optional[V]:
        """Get value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value if found, None otherwise
        """
        return self._cache.get(key)
    
    def put(self, key: K, value: V) -> None:
        """Store value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
        """
        if len(self._cache) >= self._max_size:
            # Remove oldest item (simplified LRU)
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        
        self._cache[key] = value
    
    def clear(self) -> None:
        """Clear all cached items."""
        self._cache.clear()

# Protocol for type-safe duck typing
class Drawable(Protocol):
    """Protocol defining drawable objects.
    
    Any class implementing draw() method satisfies this protocol.
    """
    
    def draw(self) -> str:
        """Draw the object and return string representation."""
        ...

class Circle:
    """Circle class that implements Drawable protocol."""
    
    def __init__(self, radius: float) -> None:
        """Initialize circle with radius.
        
        Args:
            radius: Circle radius
        """
        self.radius = radius
    
    def draw(self) -> str:
        """Draw the circle.
        
        Returns:
            String representation of the circle
        """
        return f"Circle with radius {self.radius}"

class Rectangle:
    """Rectangle class that implements Drawable protocol."""
    
    def __init__(self, width: float, height: float) -> None:
        """Initialize rectangle with dimensions.
        
        Args:
            width: Rectangle width
            height: Rectangle height
        """
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        """Draw the rectangle.
        
        Returns:
            String representation of the rectangle
        """
        return f"Rectangle {self.width}x{self.height}"

def render_shapes(shapes: List[Drawable]) -> List[str]:
    """Render a list of drawable shapes.
    
    Args:
        shapes: List of objects implementing Drawable protocol
        
    Returns:
        List of string representations of the shapes
        
    Note:
        This function accepts any object with a draw() method,
        demonstrating protocol-based typing.
    """
    return [shape.draw() for shape in shapes]


# Step 5: Type aliases and custom types
# ===============================================================================

# Explanation:
# Type aliases make complex types more readable and maintainable.
# Custom types provide semantic meaning to basic types.

# Import all previous imports
from typing import List, Dict, Optional, Union, Tuple, Any, Callable
from typing import TypeVar, Generic, Protocol, NewType
from dataclasses import dataclass
from enum import Enum

# Type aliases for complex types
UserID = NewType('UserID', int)
Email = NewType('Email', str)
JSON = Dict[str, Any]
Headers = Dict[str, str]
QueryParams = Dict[str, Union[str, int, bool]]

# Complex type aliases
UserData = Dict[str, Union[str, int, bool, List[str]]]
APIResponse = Tuple[int, JSON, Headers]
EventHandler = Callable[[str, JSON], None]
ValidationResult = Tuple[bool, Optional[str]]

# Type alias for configuration
DatabaseConfig = Dict[str, Union[str, int, bool]]
ServerConfig = Dict[str, Union[str, int, List[str]]]
AppConfig = Dict[str, Union[DatabaseConfig, ServerConfig, str]]

@dataclass
class APIClient:
    """API client with comprehensive type annotations.
    
    Demonstrates use of type aliases and custom types for clarity.
    """
    base_url: str
    default_headers: Headers
    timeout: int = 30
    
    def get(self, endpoint: str, 
            params: Optional[QueryParams] = None,
            headers: Optional[Headers] = None) -> APIResponse:
        """Make GET request to API endpoint.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters to include
            headers: Additional headers to send
            
        Returns:
            Tuple of (status_code, response_data, response_headers)
            
        Example:
            >>> client = APIClient("https://api.example.com", {})
            >>> status, data, headers = client.get("/users", {"limit": 10})
        """
        # Simulate API call
        final_headers = {**self.default_headers}
        if headers:
            final_headers.update(headers)
        
        # Mock response
        return (200, {"users": []}, {"content-type": "application/json"})
    
    def post(self, endpoint: str, 
             data: JSON,
             headers: Optional[Headers] = None) -> APIResponse:
        """Make POST request to API endpoint.
        
        Args:
            endpoint: API endpoint path
            data: JSON data to send in request body
            headers: Additional headers to send
            
        Returns:
            Tuple of (status_code, response_data, response_headers)
        """
        final_headers = {**self.default_headers, "content-type": "application/json"}
        if headers:
            final_headers.update(headers)
        
        # Mock response
        return (201, {"id": 123, "status": "created"}, final_headers)

class EventSystem:
    """Event system demonstrating function type annotations."""
    
    def __init__(self) -> None:
        """Initialize event system."""
        self._handlers: Dict[str, List[EventHandler]] = {}
    
    def register_handler(self, event_type: str, handler: EventHandler) -> None:
        """Register an event handler.
        
        Args:
            event_type: Type of event to handle
            handler: Function to call when event occurs
            
        Example:
            >>> def user_created(event: str, data: JSON) -> None:
            ...     print(f"User {data['name']} was created")
            >>> events = EventSystem()
            >>> events.register_handler("user_created", user_created)
        """
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
    
    def emit_event(self, event_type: str, data: JSON) -> None:
        """Emit an event to all registered handlers.
        
        Args:
            event_type: Type of event to emit
            data: Event data to pass to handlers
        """
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                handler(event_type, data)

def validate_email(email: Email) -> ValidationResult:
    """Validate an email address.
    
    Args:
        email: Email address to validate
        
    Returns:
        Tuple of (is_valid, error_message)
        
    Example:
        >>> email = Email("user@example.com")
        >>> is_valid, error = validate_email(email)
    """
    if "@" not in email:
        return (False, "Email must contain @ symbol")
    if "." not in email.split("@")[1]:
        return (False, "Email domain must contain a dot")
    return (True, None)

def create_user_id() -> UserID:
    """Create a new user ID.
    
    Returns:
        New unique user ID
        
    Note:
        Using NewType ensures type safety - UserID cannot be
        accidentally mixed with regular integers.
    """
    import random
    return UserID(random.randint(1000, 9999))

def process_config(config: AppConfig) -> ValidationResult:
    """Process application configuration.
    
    Args:
        config: Application configuration dictionary
        
    Returns:
        Tuple of (is_valid, error_message)
        
    Example:
        >>> config = {
        ...     "database": {"host": "localhost", "port": 5432},
        ...     "server": {"host": "0.0.0.0", "port": 8000},
        ...     "debug": True
        ... }
        >>> is_valid, error = process_config(config)
    """
    required_keys = ["database", "server"]
    for key in required_keys:
        if key not in config:
            return (False, f"Missing required config key: {key}")
    return (True, None)


# Step 6: Comprehensive examples and best practices
# ===============================================================================

# Explanation:
# This final step demonstrates comprehensive type annotation patterns,
# best practices, and real-world usage examples.

# Import all previous imports
from typing import List, Dict, Optional, Union, Tuple, Any, Callable
from typing import TypeVar, Generic, Protocol, NewType, Literal, Final
from dataclasses import dataclass, field
from enum import Enum
import asyncio
from pathlib import Path

# Advanced type annotations with Literal and Final
LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR"]
API_VERSION: Final[str] = "v1"

class DataProcessor(Generic[T]):
    """Comprehensive data processor demonstrating advanced typing patterns.
    
    This class showcases:
    - Generic types with constraints
    - Complex method signatures
    - Proper documentation integration
    - Real-world usage patterns
    """
    
    def __init__(self, 
                 validator: Callable[[T], bool],
                 transformer: Optional[Callable[[T], T]] = None) -> None:
        """Initialize data processor.
        
        Args:
            validator: Function to validate data items
            transformer: Optional function to transform data items
        """
        self._validator = validator
        self._transformer = transformer
        self._processed_count: int = 0
    
    def process_batch(self, 
                     items: List[T],
                     on_error: Callable[[T, Exception], None] = None) -> Tuple[List[T], List[T]]:
        """Process a batch of items with error handling.
        
        Args:
            items: List of items to process
            on_error: Optional error handler function
            
        Returns:
            Tuple of (successful_items, failed_items)
            
        Example:
            >>> processor = DataProcessor[str](lambda x: len(x) > 0)
            >>> success, failed = processor.process_batch(["hello", "", "world"])
            >>> print(f"Processed {len(success)} items successfully")
        """
        successful: List[T] = []
        failed: List[T] = []
        
        for item in items:
            try:
                if self._validator(item):
                    processed_item = item
                    if self._transformer:
                        processed_item = self._transformer(item)
                    successful.append(processed_item)
                    self._processed_count += 1
                else:
                    failed.append(item)
            except Exception as e:
                failed.append(item)
                if on_error:
                    on_error(item, e)
        
        return successful, failed
    
    @property
    def processed_count(self) -> int:
        """Get total number of successfully processed items."""
        return self._processed_count

@dataclass
class LogEntry:
    """Log entry with comprehensive type annotations."""
    timestamp: float
    level: LogLevel
    message: str
    context: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert log entry to dictionary.
        
        Returns:
            Dictionary representation of the log entry
        """
        return {
            "timestamp": self.timestamp,
            "level": self.level,
            "message": self.message,
            "context": self.context,
            "tags": self.tags
        }

class Logger:
    """Type-safe logger with comprehensive documentation."""
    
    def __init__(self, name: str, min_level: LogLevel = "INFO") -> None:
        """Initialize logger.
        
        Args:
            name: Logger name
            min_level: Minimum log level to record
        """
        self.name = name
        self.min_level = min_level
        self._entries: List[LogEntry] = []
        self._level_priority = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}
    
    def log(self, 
            level: LogLevel, 
            message: str,
            context: Optional[Dict[str, Any]] = None,
            tags: Optional[List[str]] = None) -> None:
        """Log a message with specified level.
        
        Args:
            level: Log level
            message: Log message
            context: Additional context data
            tags: List of tags for categorization
        """
        if self._level_priority[level] >= self._level_priority[self.min_level]:
            import time
            entry = LogEntry(
                timestamp=time.time(),
                level=level,
                message=message,
                context=context or {},
                tags=tags or []
            )
            self._entries.append(entry)
    
    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug message."""
        self.log("DEBUG", message, kwargs)
    
    def info(self, message: str, **kwargs: Any) -> None:
        """Log info message."""
        self.log("INFO", message, kwargs)
    
    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning message."""
        self.log("WARNING", message, kwargs)
    
    def error(self, message: str, **kwargs: Any) -> None:
        """Log error message."""
        self.log("ERROR", message, kwargs)
    
    def get_entries(self, 
                   level: Optional[LogLevel] = None,
                   tags: Optional[List[str]] = None) -> List[LogEntry]:
        """Get log entries with optional filtering.
        
        Args:
            level: Filter by specific log level
            tags: Filter by tags (entries must have all specified tags)
            
        Returns:
            List of matching log entries
        """
        entries = self._entries
        
        if level:
            entries = [e for e in entries if e.level == level]
        
        if tags:
            entries = [e for e in entries if all(tag in e.tags for tag in tags)]
        
        return entries

# Async function type annotations
async def fetch_user_data(user_id: UserID, 
                         timeout: float = 5.0) -> Optional[UserData]:
    """Fetch user data asynchronously.
    
    Args:
        user_id: ID of user to fetch
        timeout: Request timeout in seconds
        
    Returns:
        User data if found, None otherwise
        
    Example:
        >>> user_id = UserID(123)
        >>> data = await fetch_user_data(user_id)
    """
    # Simulate async operation
    await asyncio.sleep(0.1)
    return {
        "id": user_id,
        "name": "John Doe",
        "email": "john@example.com",
        "active": True,
        "roles": ["user"]
    }

def process_file(file_path: Union[str, Path],
                encoding: str = "utf-8") -> Tuple[bool, Optional[str]]:
    """Process a file with proper type annotations.
    
    Args:
        file_path: Path to file (string or Path object)
        encoding: File encoding
        
    Returns:
        Tuple of (success, error_message)
        
    Example:
        >>> success, error = process_file("data.txt")
        >>> if success:
        ...     print("File processed successfully")
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return False, f"File not found: {file_path}"
        
        with path.open(encoding=encoding) as f:
            content = f.read()
            # Process content here
            
        return True, None
    except Exception as e:
        return False, str(e)

# Final comprehensive example combining all concepts
def demonstrate_type_annotations() -> None:
    """Comprehensive demonstration of type annotation best practices.
    
    This function showcases all the concepts covered in previous steps:
    - Basic type annotations
    - Collection types
    - Optional and Union types
    - Class annotations
    - Generic types
    - Type aliases
    - Custom types
    - Documentation integration
    """
    # Basic types
    user_name: str = "Alice"
    user_age: int = 30
    
    # Custom types
    user_id = create_user_id()
    email = Email("alice@example.com")
    
    # Validate email
    is_valid, error = validate_email(email)
    print(f"Email validation: {is_valid}, Error: {error}")
    
    # Create user with dataclass
    user = User(
        name=user_name,
        age=user_age,
        email=email,
        role=UserRole.USER
    )
    
    # Use generic repository
    user_repo: Repository[User] = Repository()
    user_repo.add(email, user)
    
    # Use cache
    cache: Cache[str, User] = Cache(max_size=100)
    cache.put("current_user", user)
    
    # Use logger
    logger = Logger("demo", "DEBUG")
    logger.info("User created", user_id=user_id, email=email)
    
    # Process data
    processor: DataProcessor[str] = DataProcessor(
        validator=lambda x: len(x) > 0,
        transformer=lambda x: x.upper()
    )
    
    success, failed = processor.process_batch(["hello", "", "world"])
    logger.info(f"Processed {len(success)} items, {len(failed)} failed")
    
    print("Type annotation demonstration completed!")

if __name__ == "__main__":
    demonstrate_type_annotations()


# ===============================================================================
#                              SUMMARY AND BEST PRACTICES
# ===============================================================================

"""
TYPE ANNOTATION BEST PRACTICES SUMMARY:

1. BASIC PRINCIPLES:
   - Always annotate function parameters and return types
   - Use meaningful type aliases for complex types
   - Prefer specific types over Any when possible
   - Use Optional for values that can be None

2. DOCUMENTATION INTEGRATION:
   - Type hints serve as inline documentation
   - Combine with docstrings for complete documentation
   - Use descriptive variable names with type annotations
   - Include examples in docstrings showing type usage

3. ADVANCED PATTERNS:
   - Use Generics for reusable, type-safe code
   - Protocols for duck typing and interfaces
   - NewType for semantic type safety
   - Literal types for restricted string/number values

4. TOOLS AND WORKFLOW:
   - Use mypy for static type checking
   - Configure IDE for type hint support
   - Use dataclasses for structured data
   - Consider using typing_extensions for newer features

5. COMMON PITFALLS TO AVOID:
   - Don't overuse Any - be specific
   - Don't ignore type checker warnings
   - Don't mix typed and untyped code inconsistently
   - Don't forget to handle Optional types properly

6. REAL-WORLD BENEFITS:
   - Better IDE autocomplete and error detection
   - Easier code maintenance and refactoring
   - Self-documenting code
   - Reduced runtime errors
   - Better team collaboration

Remember: Type annotations are about making your code more readable,
maintainable, and less error-prone. Start simple and gradually adopt
more advanced patterns as your codebase grows.
"""

# ===============================================================================
#                                   EXERCISES
# ===============================================================================

"""
PRACTICE EXERCISES:

1. Create a typed function that processes a list of dictionaries
2. Implement a generic Stack class with proper type annotations
3. Design a typed API client with proper error handling
4. Create a configuration system using type aliases and validation
5. Build a typed event system with protocol-based handlers

Try implementing these exercises to reinforce your understanding!
"""

