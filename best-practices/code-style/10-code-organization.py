"""Question: Demonstrate proper code organization principles and best practices.

Create a well-organized Python module that showcases proper code structure,
imports, documentation, and organization patterns.

Requirements:
1. Proper import organization and structure
2. Module-level documentation and constants
3. Class organization with proper method ordering
4. Function organization and grouping
5. Proper use of private/public interfaces
6. Documentation standards and type hints
7. Error handling organization
8. Testing structure organization

Example usage:
    from user_manager import UserManager
    manager = UserManager()
    user = manager.create_user("john@example.com", "John Doe")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about how to organize code logically
# - Start with a simple implementation
# - Focus on readability and maintainability
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
# - How should imports be organized?
# - What makes code easy to read and maintain?
# - How should classes and functions be structured?
# - What documentation is needed?
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


# Step 1: Import organization and module documentation
# ===============================================================================

# Explanation:
# Proper import organization is crucial for code readability and maintainability.
# We organize imports in a specific order: standard library, third-party, local.

# Standard library imports (alphabetical order)
import logging
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

# Third-party imports (alphabetical order)
# import requests  # Example third-party import
# import pandas as pd  # Example third-party import

# Local application imports
# from .config import settings  # Example local import
# from .exceptions import UserError  # Example local import

"""
User Management System

This module provides a comprehensive user management system with proper
code organization, documentation, and best practices.

Author: Python Best Practices Team
Version: 1.0.0
Created: 2025-01-01

Example:
    Basic usage of the user management system:
    
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com", "John Doe")
    >>> print(user.name)
    John Doe
"""

# Module-level constants (UPPER_CASE naming)
DEFAULT_USER_ROLE = "user"
MAX_USERNAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 8
VALID_EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "company.com"]

# Module-level configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# What we accomplished in this step:
# - Organized imports in proper order (standard, third-party, local)
# - Added comprehensive module documentation
# - Defined module-level constants with proper naming
# - Set up logging configuration


# Step 2: Custom exceptions and error handling organization
# ===============================================================================

# Explanation:
# Proper exception organization helps with error handling and debugging.
# We define custom exceptions at the module level, organized by hierarchy.

# Standard library imports (alphabetical order)
import logging
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

# Third-party imports (alphabetical order)
# import requests  # Example third-party import
# import pandas as pd  # Example third-party import

# Local application imports
# from .config import settings  # Example local import
# from .exceptions import UserError  # Example local import

"""
User Management System

This module provides a comprehensive user management system with proper
code organization, documentation, and best practices.

Author: Python Best Practices Team
Version: 1.0.0
Created: 2025-01-01

Example:
    Basic usage of the user management system:
    
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com", "John Doe")
    >>> print(user.name)
    John Doe
"""

# Module-level constants (UPPER_CASE naming)
DEFAULT_USER_ROLE = "user"
MAX_USERNAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 8
VALID_EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "company.com"]

# Module-level configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Custom Exception Classes (organized hierarchically)
class UserManagementError(Exception):
    """Base exception for user management operations."""
    
    def __init__(self, message: str, error_code: Optional[str] = None):
        """Initialize the exception with message and optional error code.
        
        Args:
            message: Human-readable error message
            error_code: Optional error code for programmatic handling
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()


class ValidationError(UserManagementError):
    """Raised when user input validation fails."""
    pass


class UserNotFoundError(UserManagementError):
    """Raised when a requested user cannot be found."""
    pass


class DuplicateUserError(UserManagementError):
    """Raised when attempting to create a user that already exists."""
    pass


class AuthenticationError(UserManagementError):
    """Raised when user authentication fails."""
    pass

# What we accomplished in this step:
# - Created hierarchical custom exception classes
# - Added proper exception documentation
# - Included error codes and timestamps for better debugging
# - Organized exceptions by their purpose and relationship


# Step 3: Utility functions and helper functions organization
# ===============================================================================

# Explanation:
# Utility functions should be organized logically and placed before classes.
# Group related functions together and use clear, descriptive names.

# Standard library imports (alphabetical order)
import logging
import os
import re
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

# Third-party imports (alphabetical order)
# import requests  # Example third-party import
# import pandas as pd  # Example third-party import

# Local application imports
# from .config import settings  # Example local import
# from .exceptions import UserError  # Example local import

"""
User Management System

This module provides a comprehensive user management system with proper
code organization, documentation, and best practices.

Author: Python Best Practices Team
Version: 1.0.0
Created: 2025-01-01

Example:
    Basic usage of the user management system:
    
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com", "John Doe")
    >>> print(user.name)
    John Doe
"""

# Module-level constants (UPPER_CASE naming)
DEFAULT_USER_ROLE = "user"
MAX_USERNAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 8
VALID_EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "company.com"]

# Module-level configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Custom Exception Classes (organized hierarchically)
class UserManagementError(Exception):
    """Base exception for user management operations."""
    
    def __init__(self, message: str, error_code: Optional[str] = None):
        """Initialize the exception with message and optional error code.
        
        Args:
            message: Human-readable error message
            error_code: Optional error code for programmatic handling
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()


class ValidationError(UserManagementError):
    """Raised when user input validation fails."""
    pass


class UserNotFoundError(UserManagementError):
    """Raised when a requested user cannot be found."""
    pass


class DuplicateUserError(UserManagementError):
    """Raised when attempting to create a user that already exists."""
    pass


class AuthenticationError(UserManagementError):
    """Raised when user authentication fails."""
    pass


# Validation Utility Functions
def validate_email(email: str) -> bool:
    """Validate email address format and domain.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email is valid, False otherwise
        
    Raises:
        ValidationError: If email format is invalid
    """
    if not email or not isinstance(email, str):
        raise ValidationError("Email must be a non-empty string")
    
    # Basic email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        raise ValidationError(f"Invalid email format: {email}")
    
    # Check domain whitelist
    domain = email.split('@')[1].lower()
    if domain not in VALID_EMAIL_DOMAINS:
        raise ValidationError(f"Email domain not allowed: {domain}")
    
    return True


def validate_password(password: str) -> bool:
    """Validate password strength requirements.
    
    Args:
        password: Password to validate
        
    Returns:
        True if password meets requirements
        
    Raises:
        ValidationError: If password doesn't meet requirements
    """
    if not password or not isinstance(password, str):
        raise ValidationError("Password must be a non-empty string")
    
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValidationError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters")
    
    # Check for at least one uppercase, lowercase, and digit
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one digit")
    
    return True


def sanitize_username(username: str) -> str:
    """Sanitize and normalize username.
    
    Args:
        username: Raw username input
        
    Returns:
        Sanitized username
        
    Raises:
        ValidationError: If username is invalid
    """
    if not username or not isinstance(username, str):
        raise ValidationError("Username must be a non-empty string")
    
    # Remove leading/trailing whitespace and convert to lowercase
    sanitized = username.strip().lower()
    
    # Check length
    if len(sanitized) > MAX_USERNAME_LENGTH:
        raise ValidationError(f"Username too long (max {MAX_USERNAME_LENGTH} characters)")
    
    # Check for valid characters (alphanumeric and underscore only)
    if not re.match(r'^[a-zA-Z0-9_]+$', sanitized):
        raise ValidationError("Username can only contain letters, numbers, and underscores")
    
    return sanitized


# Utility Functions for Data Processing
def generate_user_id() -> str:
    """Generate a unique user ID.
    
    Returns:
        Unique user identifier string
    """
    import uuid
    return str(uuid.uuid4())


def format_timestamp(dt: datetime) -> str:
    """Format datetime for consistent display.
    
    Args:
        dt: Datetime object to format
        
    Returns:
        Formatted datetime string
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")


def _hash_password(password: str) -> str:
    """Hash password for secure storage (private function).
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password string
        
    Note:
        This is a simplified example. In production, use proper
        password hashing libraries like bcrypt or argon2.
    """
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

# What we accomplished in this step:
# - Organized utility functions by purpose (validation, data processing)
# - Added comprehensive documentation with type hints
# - Used proper naming conventions (public vs private functions)
# - Implemented proper error handling with custom exceptions
# - Grouped related functionality together


# Step 4: Data classes and model organization
# ===============================================================================

# Explanation:
# Data classes should be organized before business logic classes.
# Use proper encapsulation and provide clean interfaces.

# Standard library imports (alphabetical order)
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

# Third-party imports (alphabetical order)
# import requests  # Example third-party import
# import pandas as pd  # Example third-party import

# Local application imports
# from .config import settings  # Example local import
# from .exceptions import UserError  # Example local import

"""
User Management System

This module provides a comprehensive user management system with proper
code organization, documentation, and best practices.

Author: Python Best Practices Team
Version: 1.0.0
Created: 2025-01-01

Example:
    Basic usage of the user management system:
    
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com", "John Doe")
    >>> print(user.name)
    John Doe
"""

# Module-level constants (UPPER_CASE naming)
DEFAULT_USER_ROLE = "user"
MAX_USERNAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 8
VALID_EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "company.com"]

# Module-level configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Custom Exception Classes (organized hierarchically)
class UserManagementError(Exception):
    """Base exception for user management operations."""
    
    def __init__(self, message: str, error_code: Optional[str] = None):
        """Initialize the exception with message and optional error code.
        
        Args:
            message: Human-readable error message
            error_code: Optional error code for programmatic handling
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()


class ValidationError(UserManagementError):
    """Raised when user input validation fails."""
    pass


class UserNotFoundError(UserManagementError):
    """Raised when a requested user cannot be found."""
    pass


class DuplicateUserError(UserManagementError):
    """Raised when attempting to create a user that already exists."""
    pass


class AuthenticationError(UserManagementError):
    """Raised when user authentication fails."""
    pass


# Validation Utility Functions
def validate_email(email: str) -> bool:
    """Validate email address format and domain.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email is valid, False otherwise
        
    Raises:
        ValidationError: If email format is invalid
    """
    if not email or not isinstance(email, str):
        raise ValidationError("Email must be a non-empty string")
    
    # Basic email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        raise ValidationError(f"Invalid email format: {email}")
    
    # Check domain whitelist
    domain = email.split('@')[1].lower()
    if domain not in VALID_EMAIL_DOMAINS:
        raise ValidationError(f"Email domain not allowed: {domain}")
    
    return True


def validate_password(password: str) -> bool:
    """Validate password strength requirements.
    
    Args:
        password: Password to validate
        
    Returns:
        True if password meets requirements
        
    Raises:
        ValidationError: If password doesn't meet requirements
    """
    if not password or not isinstance(password, str):
        raise ValidationError("Password must be a non-empty string")
    
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValidationError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters")
    
    # Check for at least one uppercase, lowercase, and digit
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one digit")
    
    return True


def sanitize_username(username: str) -> str:
    """Sanitize and normalize username.
    
    Args:
        username: Raw username input
        
    Returns:
        Sanitized username
        
    Raises:
        ValidationError: If username is invalid
    """
    if not username or not isinstance(username, str):
        raise ValidationError("Username must be a non-empty string")
    
    # Remove leading/trailing whitespace and convert to lowercase
    sanitized = username.strip().lower()
    
    # Check length
    if len(sanitized) > MAX_USERNAME_LENGTH:
        raise ValidationError(f"Username too long (max {MAX_USERNAME_LENGTH} characters)")
    
    # Check for valid characters (alphanumeric and underscore only)
    if not re.match(r'^[a-zA-Z0-9_]+$', sanitized):
        raise ValidationError("Username can only contain letters, numbers, and underscores")
    
    return sanitized


# Utility Functions for Data Processing
def generate_user_id() -> str:
    """Generate a unique user ID.
    
    Returns:
        Unique user identifier string
    """
    import uuid
    return str(uuid.uuid4())


def format_timestamp(dt: datetime) -> str:
    """Format datetime for consistent display.
    
    Args:
        dt: Datetime object to format
        
    Returns:
        Formatted datetime string
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")


def _hash_password(password: str) -> str:
    """Hash password for secure storage (private function).
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password string
        
    Note:
        This is a simplified example. In production, use proper
        password hashing libraries like bcrypt or argon2.
    """
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()


# Data Classes and Models
@dataclass
class UserProfile:
    """User profile data model.
    
    Represents user profile information with proper encapsulation
    and validation.
    """
    user_id: str
    email: str
    username: str
    full_name: str
    role: str = DEFAULT_USER_ROLE
    created_at: datetime = field(default_factory=datetime.now)
    last_login: Optional[datetime] = None
    is_active: bool = True
    metadata: Dict[str, str] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate data after initialization."""
        validate_email(self.email)
        self.username = sanitize_username(self.username)
        
        if not self.full_name or not self.full_name.strip():
            raise ValidationError("Full name cannot be empty")
        
        self.full_name = self.full_name.strip()
    
    @property
    def display_name(self) -> str:
        """Get user's display name."""
        return self.full_name or self.username
    
    @property
    def is_admin(self) -> bool:
        """Check if user has admin role."""
        return self.role.lower() == "admin"
    
    def update_last_login(self) -> None:
        """Update the last login timestamp."""
        self.last_login = datetime.now()
        logger.info(f"Updated last login for user {self.username}")
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self.is_active = False
        logger.info(f"Deactivated user account: {self.username}")
    
    def activate(self) -> None:
        """Activate the user account."""
        self.is_active = True
        logger.info(f"Activated user account: {self.username}")
    
    def to_dict(self) -> Dict[str, Union[str, bool, datetime, None]]:
        """Convert user profile to dictionary representation.
        
        Returns:
            Dictionary representation of user profile
        """
        return {
            'user_id': self.user_id,
            'email': self.email,
            'username': self.username,
            'full_name': self.full_name,
            'role': self.role,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'is_active': self.is_active,
            'metadata': self.metadata.copy()
        }
    
    def __str__(self) -> str:
        """String representation of user profile."""
        status = "Active" if self.is_active else "Inactive"
        return f"User({self.username}, {self.email}, {status})"


@dataclass
class UserCredentials:
    """User authentication credentials (private data).
    
    Handles password storage and authentication securely.
    """
    user_id: str
    password_hash: str
    salt: str = field(default_factory=lambda: os.urandom(32).hex())
    created_at: datetime = field(default_factory=datetime.now)
    last_password_change: datetime = field(default_factory=datetime.now)
    
    @classmethod
    def create_from_password(cls, user_id: str, password: str) -> 'UserCredentials':
        """Create credentials from plain text password.
        
        Args:
            user_id: User identifier
            password: Plain text password
            
        Returns:
            UserCredentials instance with hashed password
        """
        validate_password(password)
        password_hash = _hash_password(password)
        
        return cls(
            user_id=user_id,
            password_hash=password_hash
        )
    
    def verify_password(self, password: str) -> bool:
        """Verify password against stored hash.
        
        Args:
            password: Plain text password to verify
            
        Returns:
            True if password matches, False otherwise
        """
        return _hash_password(password) == self.password_hash
    
    def update_password(self, new_password: str) -> None:
        """Update user password.
        
        Args:
            new_password: New plain text password
        """
        validate_password(new_password)
        self.password_hash = _hash_password(new_password)
        self.last_password_change = datetime.now()
        logger.info(f"Password updated for user {self.user_id}")

# What we accomplished in this step:
# - Created well-structured data classes with proper validation
# - Used dataclasses for clean, readable code
# - Implemented proper encapsulation with private and public methods
# - Added comprehensive documentation and type hints
# - Separated concerns (profile vs credentials)
# - Included proper logging and error handling


# Step 5: Main business logic class with proper organization
# ===============================================================================

# Explanation:
# Business logic classes should follow a consistent organization pattern:
# 1. Class docstring and type hints
# 2. Class attributes and __init__
# 3. Properties
# 4. Public methods (organized by functionality)
# 5. Private methods
# 6. Special methods (__str__, __repr__, etc.)

# Standard library imports (alphabetical order)
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

# Third-party imports (alphabetical order)
# import requests  # Example third-party import
# import pandas as pd  # Example third-party import

# Local application imports
# from .config import settings  # Example local import
# from .exceptions import UserError  # Example local import

"""
User Management System

This module provides a comprehensive user management system with proper
code organization, documentation, and best practices.

Author: Python Best Practices Team
Version: 1.0.0
Created: 2025-01-01

Example:
    Basic usage of the user management system:
    
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com", "John Doe")
    >>> print(user.name)
    John Doe
"""

# Module-level constants (UPPER_CASE naming)
DEFAULT_USER_ROLE = "user"
MAX_USERNAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 8
VALID_EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "company.com"]

# Module-level configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Custom Exception Classes (organized hierarchically)
class UserManagementError(Exception):
    """Base exception for user management operations."""
    
    def __init__(self, message: str, error_code: Optional[str] = None):
        """Initialize the exception with message and optional error code.
        
        Args:
            message: Human-readable error message
            error_code: Optional error code for programmatic handling
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()


class ValidationError(UserManagementError):
    """Raised when user input validation fails."""
    pass


class UserNotFoundError(UserManagementError):
    """Raised when a requested user cannot be found."""
    pass


class DuplicateUserError(UserManagementError):
    """Raised when attempting to create a user that already exists."""
    pass


class AuthenticationError(UserManagementError):
    """Raised when user authentication fails."""
    pass


# Validation Utility Functions
def validate_email(email: str) -> bool:
    """Validate email address format and domain.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email is valid, False otherwise
        
    Raises:
        ValidationError: If email format is invalid
    """
    if not email or not isinstance(email, str):
        raise ValidationError("Email must be a non-empty string")
    
    # Basic email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        raise ValidationError(f"Invalid email format: {email}")
    
    # Check domain whitelist
    domain = email.split('@')[1].lower()
    if domain not in VALID_EMAIL_DOMAINS:
        raise ValidationError(f"Email domain not allowed: {domain}")
    
    return True


def validate_password(password: str) -> bool:
    """Validate password strength requirements.
    
    Args:
        password: Password to validate
        
    Returns:
        True if password meets requirements
        
    Raises:
        ValidationError: If password doesn't meet requirements
    """
    if not password or not isinstance(password, str):
        raise ValidationError("Password must be a non-empty string")
    
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValidationError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters")
    
    # Check for at least one uppercase, lowercase, and digit
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one digit")
    
    return True


def sanitize_username(username: str) -> str:
    """Sanitize and normalize username.
    
    Args:
        username: Raw username input
        
    Returns:
        Sanitized username
        
    Raises:
        ValidationError: If username is invalid
    """
    if not username or not isinstance(username, str):
        raise ValidationError("Username must be a non-empty string")
    
    # Remove leading/trailing whitespace and convert to lowercase
    sanitized = username.strip().lower()
    
    # Check length
    if len(sanitized) > MAX_USERNAME_LENGTH:
        raise ValidationError(f"Username too long (max {MAX_USERNAME_LENGTH} characters)")
    
    # Check for valid characters (alphanumeric and underscore only)
    if not re.match(r'^[a-zA-Z0-9_]+$', sanitized):
        raise ValidationError("Username can only contain letters, numbers, and underscores")
    
    return sanitized


# Utility Functions for Data Processing
def generate_user_id() -> str:
    """Generate a unique user ID.
    
    Returns:
        Unique user identifier string
    """
    import uuid
    return str(uuid.uuid4())


def format_timestamp(dt: datetime) -> str:
    """Format datetime for consistent display.
    
    Args:
        dt: Datetime object to format
        
    Returns:
        Formatted datetime string
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")


def _hash_password(password: str) -> str:
    """Hash password for secure storage (private function).
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password string
        
    Note:
        This is a simplified example. In production, use proper
        password hashing libraries like bcrypt or argon2.
    """
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()


# Data Classes and Models
@dataclass
class UserProfile:
    """User profile data model.
    
    Represents user profile information with proper encapsulation
    and validation.
    """
    user_id: str
    email: str
    username: str
    full_name: str
    role: str = DEFAULT_USER_ROLE
    created_at: datetime = field(default_factory=datetime.now)
    last_login: Optional[datetime] = None
    is_active: bool = True
    metadata: Dict[str, str] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate data after initialization."""
        validate_email(self.email)
        self.username = sanitize_username(self.username)
        
        if not self.full_name or not self.full_name.strip():
            raise ValidationError("Full name cannot be empty")
        
        self.full_name = self.full_name.strip()
    
    @property
    def display_name(self) -> str:
        """Get user's display name."""
        return self.full_name or self.username
    
    @property
    def is_admin(self) -> bool:
        """Check if user has admin role."""
        return self.role.lower() == "admin"
    
    def update_last_login(self) -> None:
        """Update the last login timestamp."""
        self.last_login = datetime.now()
        logger.info(f"Updated last login for user {self.username}")
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self.is_active = False
        logger.info(f"Deactivated user account: {self.username}")
    
    def activate(self) -> None:
        """Activate the user account."""
        self.is_active = True
        logger.info(f"Activated user account: {self.username}")
    
    def to_dict(self) -> Dict[str, Union[str, bool, datetime, None]]:
        """Convert user profile to dictionary representation.
        
        Returns:
            Dictionary representation of user profile
        """
        return {
            'user_id': self.user_id,
            'email': self.email,
            'username': self.username,
            'full_name': self.full_name,
            'role': self.role,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'is_active': self.is_active,
            'metadata': self.metadata.copy()
        }
    
    def __str__(self) -> str:
        """String representation of user profile."""
        status = "Active" if self.is_active else "Inactive"
        return f"User({self.username}, {self.email}, {status})"


@dataclass
class UserCredentials:
    """User authentication credentials (private data).
    
    Handles password storage and authentication securely.
    """
    user_id: str
    password_hash: str
    salt: str = field(default_factory=lambda: os.urandom(32).hex())
    created_at: datetime = field(default_factory=datetime.now)
    last_password_change: datetime = field(default_factory=datetime.now)
    
    @classmethod
    def create_from_password(cls, user_id: str, password: str) -> 'UserCredentials':
        """Create credentials from plain text password.
        
        Args:
            user_id: User identifier
            password: Plain text password
            
        Returns:
            UserCredentials instance with hashed password
        """
        validate_password(password)
        password_hash = _hash_password(password)
        
        return cls(
            user_id=user_id,
            password_hash=password_hash
        )
    
    def verify_password(self, password: str) -> bool:
        """Verify password against stored hash.
        
        Args:
            password: Plain text password to verify
            
        Returns:
            True if password matches, False otherwise
        """
        return _hash_password(password) == self.password_hash
    
    def update_password(self, new_password: str) -> None:
        """Update user password.
        
        Args:
            new_password: New plain text password
        """
        validate_password(new_password)
        self.password_hash = _hash_password(new_password)
        self.last_password_change = datetime.now()
        logger.info(f"Password updated for user {self.user_id}")


# Main Business Logic Class
class UserManager:
    """Main user management class with proper organization.
    
    Handles all user-related operations including creation, authentication,
    and profile management. Demonstrates proper class organization and
    code structure best practices.
    
    Attributes:
        _users: Dictionary storing user profiles by user_id
        _credentials: Dictionary storing user credentials by user_id
        _email_index: Dictionary for email-to-user_id mapping
        _username_index: Dictionary for username-to-user_id mapping
    """
    
    def __init__(self):
        """Initialize the user manager with empty storage."""
        # Private attributes (use underscore prefix)
        self._users: Dict[str, UserProfile] = {}
        self._credentials: Dict[str, UserCredentials] = {}
        self._email_index: Dict[str, str] = {}
        self._username_index: Dict[str, str] = {}
        
        logger.info("UserManager initialized")
    
    # Properties (read-only access to internal state)
    @property
    def user_count(self) -> int:
        """Get total number of users."""
        return len(self._users)
    
    @property
    def active_user_count(self) -> int:
        """Get number of active users."""
        return sum(1 for user in self._users.values() if user.is_active)
    
    # User Creation Methods
    def create_user(self, email: str, full_name: str, password: str, 
                   username: Optional[str] = None, role: str = DEFAULT_USER_ROLE) -> UserProfile:
        """Create a new user account.
        
        Args:
            email: User's email address
            full_name: User's full name
            password: User's password
            username: Optional username (generated from email if not provided)
            role: User's role (defaults to DEFAULT_USER_ROLE)
            
        Returns:
            Created UserProfile instance
            
        Raises:
            DuplicateUserError: If user with email already exists
            ValidationError: If input validation fails
        """
        # Validate inputs
        validate_email(email)
        validate_password(password)
        
        if email.lower() in self._email_index:
            raise DuplicateUserError(f"User with email {email} already exists")
        
        # Generate username if not provided
        if username is None:
            username = email.split('@')[0]
        
        username = sanitize_username(username)
        
        # Check username uniqueness
        if username in self._username_index:
            # Generate unique username by appending number
            base_username = username
            counter = 1
            while f"{base_username}_{counter}" in self._username_index:
                counter += 1
            username = f"{base_username}_{counter}"
        
        # Generate user ID and create profile
        user_id = generate_user_id()
        
        try:
            user_profile = UserProfile(
                user_id=user_id,
                email=email.lower(),
                username=username,
                full_name=full_name,
                role=role
            )
            
            # Create credentials
            credentials = UserCredentials.create_from_password(user_id, password)
            
            # Store user data
            self._users[user_id] = user_profile
            self._credentials[user_id] = credentials
            self._email_index[email.lower()] = user_id
            self._username_index[username] = user_id
            
            logger.info(f"Created new user: {username} ({email})")
            return user_profile
            
        except Exception as e:
            # Clean up partial state if creation fails
            self._cleanup_failed_user_creation(user_id, email, username)
            raise UserManagementError(f"Failed to create user: {str(e)}")
    
    # User Retrieval Methods
    def get_user_by_id(self, user_id: str) -> UserProfile:
        """Get user by user ID.
        
        Args:
            user_id: User identifier
            
        Returns:
            UserProfile instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        if user_id not in self._users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        return self._users[user_id]
    
    def get_user_by_email(self, email: str) -> UserProfile:
        """Get user by email address.
        
        Args:
            email: User's email address
            
        Returns:
            UserProfile instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        email_lower = email.lower()
        if email_lower not in self._email_index:
            raise UserNotFoundError(f"User with email {email} not found")
        
        user_id = self._email_index[email_lower]
        return self._users[user_id]
    
    def get_user_by_username(self, username: str) -> UserProfile:
        """Get user by username.
        
        Args:
            username: Username
            
        Returns:
            UserProfile instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        username_lower = username.lower()
        if username_lower not in self._username_index:
            raise UserNotFoundError(f"User with username {username} not found")
        
        user_id = self._username_index[username_lower]
        return self._users[user_id]
    
    # Authentication Methods
    def authenticate_user(self, email: str, password: str) -> UserProfile:
        """Authenticate user with email and password.
        
        Args:
            email: User's email address
            password: User's password
            
        Returns:
            UserProfile if authentication successful
            
        Raises:
            AuthenticationError: If authentication fails
            UserNotFoundError: If user doesn't exist
        """
        try:
            user = self.get_user_by_email(email)
            
            if not user.is_active:
                raise AuthenticationError("User account is deactivated")
            
            credentials = self._credentials[user.user_id]
            
            if not credentials.verify_password(password):
                raise AuthenticationError("Invalid password")
            
            # Update last login
            user.update_last_login()
            
            logger.info(f"User authenticated successfully: {user.username}")
            return user
            
        except UserNotFoundError:
            raise AuthenticationError("Invalid email or password")
    
    # User Management Methods
    def list_users(self, active_only: bool = False) -> List[UserProfile]:
        """List all users.
        
        Args:
            active_only: If True, return only active users
            
        Returns:
            List of UserProfile instances
        """
        users = list(self._users.values())
        
        if active_only:
            users = [user for user in users if user.is_active]
        
        # Sort by creation date
        users.sort(key=lambda u: u.created_at)
        
        return users
    
    def update_user_password(self, user_id: str, new_password: str) -> None:
        """Update user's password.
        
        Args:
            user_id: User identifier
            new_password: New password
            
        Raises:
            UserNotFoundError: If user doesn't exist
            ValidationError: If password is invalid
        """
        if user_id not in self._users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        credentials = self._credentials[user_id]
        credentials.update_password(new_password)
        
        logger.info(f"Password updated for user {user_id}")
    
    def deactivate_user(self, user_id: str) -> None:
        """Deactivate user account.
        
        Args:
            user_id: User identifier
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        user = self.get_user_by_id(user_id)
        user.deactivate()
    
    def activate_user(self, user_id: str) -> None:
        """Activate user account.
        
        Args:
            user_id: User identifier
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        user = self.get_user_by_id(user_id)
        user.activate()
    
    # Private Helper Methods
    def _cleanup_failed_user_creation(self, user_id: str, email: str, username: str) -> None:
        """Clean up partial state after failed user creation.
        
        Args:
            user_id: User ID to clean up
            email: Email to remove from index
            username: Username to remove from index
        """
        self._users.pop(user_id, None)
        self._credentials.pop(user_id, None)
        self._email_index.pop(email.lower(), None)
        self._username_index.pop(username.lower(), None)
    
    # Special Methods
    def __len__(self) -> int:
        """Return number of users."""
        return len(self._users)
    
    def __contains__(self, email: str) -> bool:
        """Check if user with email exists."""
        return email.lower() in self._email_index
    
    def __str__(self) -> str:
        """String representation of UserManager."""
        return f"UserManager(users={len(self._users)}, active={self.active_user_count})"

# What we accomplished in this step:
# - Created a well-organized main business logic class
# - Followed consistent method organization (public, then private)
# - Used proper encapsulation with private attributes
# - Implemented comprehensive error handling
# - Added proper logging throughout
# - Used type hints and documentation consistently
# - Separated concerns (authentication, user management, etc.)


# Step 6: Testing and demonstration code
# ===============================================================================

# Explanation:
# Demonstration code should be organized at the end of the module.
# This shows how to use the classes and validates the implementation.

# Standard library imports (alphabetical order)
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union

# Third-party imports (alphabetical order)
# import requests  # Example third-party import
# import pandas as pd  # Example third-party import

# Local application imports
# from .config import settings  # Example local import
# from .exceptions import UserError  # Example local import

"""
User Management System

This module provides a comprehensive user management system with proper
code organization, documentation, and best practices.

Author: Python Best Practices Team
Version: 1.0.0
Created: 2025-01-01

Example:
    Basic usage of the user management system:
    
    >>> from user_manager import UserManager
    >>> manager = UserManager()
    >>> user = manager.create_user("john@example.com", "John Doe")
    >>> print(user.name)
    John Doe
"""

# Module-level constants (UPPER_CASE naming)
DEFAULT_USER_ROLE = "user"
MAX_USERNAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 8
VALID_EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "company.com"]

# Module-level configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Custom Exception Classes (organized hierarchically)
class UserManagementError(Exception):
    """Base exception for user management operations."""
    
    def __init__(self, message: str, error_code: Optional[str] = None):
        """Initialize the exception with message and optional error code.
        
        Args:
            message: Human-readable error message
            error_code: Optional error code for programmatic handling
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()


class ValidationError(UserManagementError):
    """Raised when user input validation fails."""
    pass


class UserNotFoundError(UserManagementError):
    """Raised when a requested user cannot be found."""
    pass


class DuplicateUserError(UserManagementError):
    """Raised when attempting to create a user that already exists."""
    pass


class AuthenticationError(UserManagementError):
    """Raised when user authentication fails."""
    pass


# Validation Utility Functions
def validate_email(email: str) -> bool:
    """Validate email address format and domain.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email is valid, False otherwise
        
    Raises:
        ValidationError: If email format is invalid
    """
    if not email or not isinstance(email, str):
        raise ValidationError("Email must be a non-empty string")
    
    # Basic email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        raise ValidationError(f"Invalid email format: {email}")
    
    # Check domain whitelist
    domain = email.split('@')[1].lower()
    if domain not in VALID_EMAIL_DOMAINS:
        raise ValidationError(f"Email domain not allowed: {domain}")
    
    return True


def validate_password(password: str) -> bool:
    """Validate password strength requirements.
    
    Args:
        password: Password to validate
        
    Returns:
        True if password meets requirements
        
    Raises:
        ValidationError: If password doesn't meet requirements
    """
    if not password or not isinstance(password, str):
        raise ValidationError("Password must be a non-empty string")
    
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValidationError(f"Password must be at least {MIN_PASSWORD_LENGTH} characters")
    
    # Check for at least one uppercase, lowercase, and digit
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one digit")
    
    return True


def sanitize_username(username: str) -> str:
    """Sanitize and normalize username.
    
    Args:
        username: Raw username input
        
    Returns:
        Sanitized username
        
    Raises:
        ValidationError: If username is invalid
    """
    if not username or not isinstance(username, str):
        raise ValidationError("Username must be a non-empty string")
    
    # Remove leading/trailing whitespace and convert to lowercase
    sanitized = username.strip().lower()
    
    # Check length
    if len(sanitized) > MAX_USERNAME_LENGTH:
        raise ValidationError(f"Username too long (max {MAX_USERNAME_LENGTH} characters)")
    
    # Check for valid characters (alphanumeric and underscore only)
    if not re.match(r'^[a-zA-Z0-9_]+$', sanitized):
        raise ValidationError("Username can only contain letters, numbers, and underscores")
    
    return sanitized


# Utility Functions for Data Processing
def generate_user_id() -> str:
    """Generate a unique user ID.
    
    Returns:
        Unique user identifier string
    """
    import uuid
    return str(uuid.uuid4())


def format_timestamp(dt: datetime) -> str:
    """Format datetime for consistent display.
    
    Args:
        dt: Datetime object to format
        
    Returns:
        Formatted datetime string
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")


def _hash_password(password: str) -> str:
    """Hash password for secure storage (private function).
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password string
        
    Note:
        This is a simplified example. In production, use proper
        password hashing libraries like bcrypt or argon2.
    """
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()


# Data Classes and Models
@dataclass
class UserProfile:
    """User profile data model.
    
    Represents user profile information with proper encapsulation
    and validation.
    """
    user_id: str
    email: str
    username: str
    full_name: str
    role: str = DEFAULT_USER_ROLE
    created_at: datetime = field(default_factory=datetime.now)
    last_login: Optional[datetime] = None
    is_active: bool = True
    metadata: Dict[str, str] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate data after initialization."""
        validate_email(self.email)
        self.username = sanitize_username(self.username)
        
        if not self.full_name or not self.full_name.strip():
            raise ValidationError("Full name cannot be empty")
        
        self.full_name = self.full_name.strip()
    
    @property
    def display_name(self) -> str:
        """Get user's display name."""
        return self.full_name or self.username
    
    @property
    def is_admin(self) -> bool:
        """Check if user has admin role."""
        return self.role.lower() == "admin"
    
    def update_last_login(self) -> None:
        """Update the last login timestamp."""
        self.last_login = datetime.now()
        logger.info(f"Updated last login for user {self.username}")
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self.is_active = False
        logger.info(f"Deactivated user account: {self.username}")
    
    def activate(self) -> None:
        """Activate the user account."""
        self.is_active = True
        logger.info(f"Activated user account: {self.username}")
    
    def to_dict(self) -> Dict[str, Union[str, bool, datetime, None]]:
        """Convert user profile to dictionary representation.
        
        Returns:
            Dictionary representation of user profile
        """
        return {
            'user_id': self.user_id,
            'email': self.email,
            'username': self.username,
            'full_name': self.full_name,
            'role': self.role,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'is_active': self.is_active,
            'metadata': self.metadata.copy()
        }
    
    def __str__(self) -> str:
        """String representation of user profile."""
        status = "Active" if self.is_active else "Inactive"
        return f"User({self.username}, {self.email}, {status})"


@dataclass
class UserCredentials:
    """User authentication credentials (private data).
    
    Handles password storage and authentication securely.
    """
    user_id: str
    password_hash: str
    salt: str = field(default_factory=lambda: os.urandom(32).hex())
    created_at: datetime = field(default_factory=datetime.now)
    last_password_change: datetime = field(default_factory=datetime.now)
    
    @classmethod
    def create_from_password(cls, user_id: str, password: str) -> 'UserCredentials':
        """Create credentials from plain text password.
        
        Args:
            user_id: User identifier
            password: Plain text password
            
        Returns:
            UserCredentials instance with hashed password
        """
        validate_password(password)
        password_hash = _hash_password(password)
        
        return cls(
            user_id=user_id,
            password_hash=password_hash
        )
    
    def verify_password(self, password: str) -> bool:
        """Verify password against stored hash.
        
        Args:
            password: Plain text password to verify
            
        Returns:
            True if password matches, False otherwise
        """
        return _hash_password(password) == self.password_hash
    
    def update_password(self, new_password: str) -> None:
        """Update user password.
        
        Args:
            new_password: New plain text password
        """
        validate_password(new_password)
        self.password_hash = _hash_password(new_password)
        self.last_password_change = datetime.now()
        logger.info(f"Password updated for user {self.user_id}")


# Main Business Logic Class
class UserManager:
    """Main user management class with proper organization.
    
    Handles all user-related operations including creation, authentication,
    and profile management. Demonstrates proper class organization and
    code structure best practices.
    
    Attributes:
        _users: Dictionary storing user profiles by user_id
        _credentials: Dictionary storing user credentials by user_id
        _email_index: Dictionary for email-to-user_id mapping
        _username_index: Dictionary for username-to-user_id mapping
    """
    
    def __init__(self):
        """Initialize the user manager with empty storage."""
        # Private attributes (use underscore prefix)
        self._users: Dict[str, UserProfile] = {}
        self._credentials: Dict[str, UserCredentials] = {}
        self._email_index: Dict[str, str] = {}
        self._username_index: Dict[str, str] = {}
        
        logger.info("UserManager initialized")
    
    # Properties (read-only access to internal state)
    @property
    def user_count(self) -> int:
        """Get total number of users."""
        return len(self._users)
    
    @property
    def active_user_count(self) -> int:
        """Get number of active users."""
        return sum(1 for user in self._users.values() if user.is_active)
    
    # User Creation Methods
    def create_user(self, email: str, full_name: str, password: str, 
                   username: Optional[str] = None, role: str = DEFAULT_USER_ROLE) -> UserProfile:
        """Create a new user account.
        
        Args:
            email: User's email address
            full_name: User's full name
            password: User's password
            username: Optional username (generated from email if not provided)
            role: User's role (defaults to DEFAULT_USER_ROLE)
            
        Returns:
            Created UserProfile instance
            
        Raises:
            DuplicateUserError: If user with email already exists
            ValidationError: If input validation fails
        """
        # Validate inputs
        validate_email(email)
        validate_password(password)
        
        if email.lower() in self._email_index:
            raise DuplicateUserError(f"User with email {email} already exists")
        
        # Generate username if not provided
        if username is None:
            username = email.split('@')[0]
        
        username = sanitize_username(username)
        
        # Check username uniqueness
        if username in self._username_index:
            # Generate unique username by appending number
            base_username = username
            counter = 1
            while f"{base_username}_{counter}" in self._username_index:
                counter += 1
            username = f"{base_username}_{counter}"
        
        # Generate user ID and create profile
        user_id = generate_user_id()
        
        try:
            user_profile = UserProfile(
                user_id=user_id,
                email=email.lower(),
                username=username,
                full_name=full_name,
                role=role
            )
            
            # Create credentials
            credentials = UserCredentials.create_from_password(user_id, password)
            
            # Store user data
            self._users[user_id] = user_profile
            self._credentials[user_id] = credentials
            self._email_index[email.lower()] = user_id
            self._username_index[username] = user_id
            
            logger.info(f"Created new user: {username} ({email})")
            return user_profile
            
        except Exception as e:
            # Clean up partial state if creation fails
            self._cleanup_failed_user_creation(user_id, email, username)
            raise UserManagementError(f"Failed to create user: {str(e)}")
    
    # User Retrieval Methods
    def get_user_by_id(self, user_id: str) -> UserProfile:
        """Get user by user ID.
        
        Args:
            user_id: User identifier
            
        Returns:
            UserProfile instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        if user_id not in self._users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        return self._users[user_id]
    
    def get_user_by_email(self, email: str) -> UserProfile:
        """Get user by email address.
        
        Args:
            email: User's email address
            
        Returns:
            UserProfile instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        email_lower = email.lower()
        if email_lower not in self._email_index:
            raise UserNotFoundError(f"User with email {email} not found")
        
        user_id = self._email_index[email_lower]
        return self._users[user_id]
    
    def get_user_by_username(self, username: str) -> UserProfile:
        """Get user by username.
        
        Args:
            username: Username
            
        Returns:
            UserProfile instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        username_lower = username.lower()
        if username_lower not in self._username_index:
            raise UserNotFoundError(f"User with username {username} not found")
        
        user_id = self._username_index[username_lower]
        return self._users[user_id]
    
    # Authentication Methods
    def authenticate_user(self, email: str, password: str) -> UserProfile:
        """Authenticate user with email and password.
        
        Args:
            email: User's email address
            password: User's password
            
        Returns:
            UserProfile if authentication successful
            
        Raises:
            AuthenticationError: If authentication fails
            UserNotFoundError: If user doesn't exist
        """
        try:
            user = self.get_user_by_email(email)
            
            if not user.is_active:
                raise AuthenticationError("User account is deactivated")
            
            credentials = self._credentials[user.user_id]
            
            if not credentials.verify_password(password):
                raise AuthenticationError("Invalid password")
            
            # Update last login
            user.update_last_login()
            
            logger.info(f"User authenticated successfully: {user.username}")
            return user
            
        except UserNotFoundError:
            raise AuthenticationError("Invalid email or password")
    
    # User Management Methods
    def list_users(self, active_only: bool = False) -> List[UserProfile]:
        """List all users.
        
        Args:
            active_only: If True, return only active users
            
        Returns:
            List of UserProfile instances
        """
        users = list(self._users.values())
        
        if active_only:
            users = [user for user in users if user.is_active]
        
        # Sort by creation date
        users.sort(key=lambda u: u.created_at)
        
        return users
    
    def update_user_password(self, user_id: str, new_password: str) -> None:
        """Update user's password.
        
        Args:
            user_id: User identifier
            new_password: New password
            
        Raises:
            UserNotFoundError: If user doesn't exist
            ValidationError: If password is invalid
        """
        if user_id not in self._users:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        
        credentials = self._credentials[user_id]
        credentials.update_password(new_password)
        
        logger.info(f"Password updated for user {user_id}")
    
    def deactivate_user(self, user_id: str) -> None:
        """Deactivate user account.
        
        Args:
            user_id: User identifier
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        user = self.get_user_by_id(user_id)
        user.deactivate()
    
    def activate_user(self, user_id: str) -> None:
        """Activate user account.
        
        Args:
            user_id: User identifier
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        user = self.get_user_by_id(user_id)
        user.activate()
    
    # Private Helper Methods
    def _cleanup_failed_user_creation(self, user_id: str, email: str, username: str) -> None:
        """Clean up partial state after failed user creation.
        
        Args:
            user_id: User ID to clean up
            email: Email to remove from index
            username: Username to remove from index
        """
        self._users.pop(user_id, None)
        self._credentials.pop(user_id, None)
        self._email_index.pop(email.lower(), None)
        self._username_index.pop(username.lower(), None)
    
    # Special Methods
    def __len__(self) -> int:
        """Return number of users."""
        return len(self._users)
    
    def __contains__(self, email: str) -> bool:
        """Check if user with email exists."""
        return email.lower() in self._email_index
    
    def __str__(self) -> str:
        """String representation of UserManager."""
        return f"UserManager(users={len(self._users)}, active={self.active_user_count})"


# Demonstration and Testing Code
def demonstrate_user_management_system():
    """Demonstrate the user management system functionality."""
    print("=== User Management System Demonstration ===\n")
    
    # Create user manager instance
    manager = UserManager()
    print(f"1. Created UserManager: {manager}")
    print()
    
    # Create some users
    print("2. Creating users:")
    try:
        user1 = manager.create_user(
            email="john.doe@gmail.com",
            full_name="John Doe",
            password="SecurePass123",
            role="admin"
        )
        print(f"   Created: {user1}")
        
        user2 = manager.create_user(
            email="jane.smith@yahoo.com",
            full_name="Jane Smith",
            password="MyPassword456"
        )
        print(f"   Created: {user2}")
        
        user3 = manager.create_user(
            email="bob.wilson@company.com",
            full_name="Bob Wilson",
            password="BobPass789",
            username="bobw"
        )
        print(f"   Created: {user3}")
        
    except UserManagementError as e:
        print(f"   Error creating user: {e}")
    
    print(f"\n   Total users: {len(manager)}")
    print()
    
    # Test authentication
    print("3. Testing authentication:")
    try:
        authenticated_user = manager.authenticate_user("john.doe@gmail.com", "SecurePass123")
        print(f"   Authentication successful: {authenticated_user.display_name}")
        
        # Test wrong password
        try:
            manager.authenticate_user("john.doe@gmail.com", "WrongPassword")
        except AuthenticationError as e:
            print(f"   Authentication failed (expected): {e}")
            
    except UserManagementError as e:
        print(f"   Authentication error: {e}")
    
    print()
    
    # Test user retrieval
    print("4. Testing user retrieval:")
    try:
        user_by_email = manager.get_user_by_email("jane.smith@yahoo.com")
        print(f"   Found by email: {user_by_email}")
        
        user_by_username = manager.get_user_by_username("bobw")
        print(f"   Found by username: {user_by_username}")
        
    except UserNotFoundError as e:
        print(f"   User not found: {e}")
    
    print()
    
    # Test user management
    print("5. Testing user management:")
    users = manager.list_users()
    print(f"   All users ({len(users)}):")
    for user in users:
        print(f"     - {user}")
    
    # Deactivate a user
    if users:
        user_to_deactivate = users[1]  # Jane Smith
        manager.deactivate_user(user_to_deactivate.user_id)
        print(f"   Deactivated: {user_to_deactivate.username}")
    
    active_users = manager.list_users(active_only=True)
    print(f"   Active users ({len(active_users)}):")
    for user in active_users:
        print(f"     - {user}")
    
    print()
    
    # Test error handling
    print("6. Testing error handling:")
    try:
        # Try to create duplicate user
        manager.create_user("john.doe@gmail.com", "John Duplicate", "Password123")
    except DuplicateUserError as e:
        print(f"   Duplicate user error (expected): {e}")
    
    try:
        # Try invalid email
        manager.create_user("invalid-email", "Invalid User", "Password123")
    except ValidationError as e:
        print(f"   Validation error (expected): {e}")
    
    try:
        # Try to find non-existent user
        manager.get_user_by_email("nonexistent@example.com")
    except UserNotFoundError as e:
        print(f"   User not found error (expected): {e}")
    
    print()
    print("=== Demonstration Complete ===")


# Run demonstration if script is executed directly
if __name__ == "__main__":
    demonstrate_user_management_system()

# What we accomplished in this step:
# - Created comprehensive demonstration code
# - Showed proper error handling and testing
# - Demonstrated all major functionality
# - Used proper organization for test/demo code
# - Included both positive and negative test cases
# - Showed real-world usage patterns