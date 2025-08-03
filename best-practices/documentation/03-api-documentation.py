"""Question: Create comprehensive API documentation for a REST API service.

Create a well-documented API service with proper docstrings, type hints, and examples
that demonstrates best practices for API documentation.

Requirements:
1. Create a User management API with CRUD operations
2. Use proper docstrings with parameters, returns, and examples
3. Include type hints for all functions and methods
4. Add error handling documentation
5. Demonstrate different documentation formats (Google, NumPy, Sphinx)

Example usage:
    api = UserAPI()
    user = api.create_user("john_doe", "john@example.com")
    users = api.get_all_users()
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
# - What data models do you need for users?
# - What CRUD operations should your API support?
# - How to structure comprehensive docstrings?
# - What type hints are needed for clarity?
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


# Step 1: Import modules and create basic data models
# ===============================================================================

# Explanation:
# Good API documentation starts with clear data models and proper imports.
# We'll use type hints and dataclasses for clean, documented data structures.

from typing import Dict, List, Optional, Union, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import json

@dataclass
class User:
    """User data model with comprehensive documentation.
    
    This class represents a user in our system with all necessary attributes
    and validation methods.
    
    Attributes:
        user_id (int): Unique identifier for the user
        username (str): Unique username for login
        email (str): User's email address
        full_name (str): User's full display name
        created_at (datetime): Timestamp when user was created
        is_active (bool): Whether the user account is active
        metadata (Dict[str, Any]): Additional user metadata
    
    Example:
        >>> user = User(
        ...     user_id=1,
        ...     username="john_doe",
        ...     email="john@example.com",
        ...     full_name="John Doe"
        ... )
        >>> print(user.username)
        john_doe
    """
    user_id: int
    username: str
    email: str
    full_name: str
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user object to dictionary representation.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the user
            
        Example:
            >>> user = User(1, "john", "john@test.com", "John Doe")
            >>> user_dict = user.to_dict()
            >>> isinstance(user_dict, dict)
            True
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active,
            'metadata': self.metadata
        }


# Step 2: Create error handling classes with documentation
# ===============================================================================

# Explanation:
# Good APIs need comprehensive error handling. We'll create custom exceptions
# with clear documentation about when they're raised and how to handle them.

class APIError(Exception):
    """Base exception class for API errors.
    
    This is the base class for all API-related exceptions. It provides
    a consistent interface for error handling across the API.
    
    Attributes:
        message (str): Human-readable error message
        error_code (str): Machine-readable error code
        status_code (int): HTTP status code for the error
    
    Args:
        message (str): Error message describing what went wrong
        error_code (str, optional): Specific error code. Defaults to "API_ERROR"
        status_code (int, optional): HTTP status code. Defaults to 500
    
    Example:
        >>> try:
        ...     raise APIError("Something went wrong", "GENERIC_ERROR", 500)
        ... except APIError as e:
        ...     print(f"Error: {e.message}")
        Error: Something went wrong
    """
    
    def __init__(self, message: str, error_code: str = "API_ERROR", status_code: int = 500):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        super().__init__(self.message)


class UserNotFoundError(APIError):
    """Exception raised when a requested user cannot be found.
    
    This exception is raised when attempting to access, update, or delete
    a user that doesn't exist in the system.
    
    Args:
        user_identifier (Union[int, str]): The ID or username that wasn't found
        
    Example:
        >>> try:
        ...     raise UserNotFoundError("nonexistent_user")
        ... except UserNotFoundError as e:
        ...     print(e.error_code)
        USER_NOT_FOUND
    """
    
    def __init__(self, user_identifier: Union[int, str]):
        message = f"User '{user_identifier}' not found"
        super().__init__(message, "USER_NOT_FOUND", 404)


class UserAlreadyExistsError(APIError):
    """Exception raised when trying to create a user that already exists.
    
    This exception is raised when attempting to create a user with a username
    or email that's already taken.
    
    Args:
        field (str): The field that conflicts (username or email)
        value (str): The conflicting value
        
    Example:
        >>> try:
        ...     raise UserAlreadyExistsError("username", "john_doe")
        ... except UserAlreadyExistsError as e:
        ...     print(e.status_code)
        409
    """
    
    def __init__(self, field: str, value: str):
        message = f"User with {field} '{value}' already exists"
        super().__init__(message, "USER_ALREADY_EXISTS", 409)


class ValidationError(APIError):
    """Exception raised when input validation fails.
    
    This exception is raised when user input doesn't meet the required
    validation criteria (e.g., invalid email format, empty required fields).
    
    Args:
        field (str): The field that failed validation
        reason (str): Why the validation failed
        
    Example:
        >>> try:
        ...     raise ValidationError("email", "Invalid email format")
        ... except ValidationError as e:
        ...     print(e.error_code)
        VALIDATION_ERROR
    """
    
    def __init__(self, field: str, reason: str):
        message = f"Validation failed for '{field}': {reason}"
        super().__init__(message, "VALIDATION_ERROR", 400)


# Step 3: Add validation utilities with comprehensive documentation
# ===============================================================================

# Explanation:
# We need validation functions that are well-documented with clear examples
# of what constitutes valid input and what will raise exceptions.

import re

class UserValidator:
    """Utility class for validating user input data.
    
    This class provides static methods for validating various user fields
    according to business rules and data constraints.
    
    Note:
        All validation methods raise ValidationError if validation fails.
        
    Example:
        >>> UserValidator.validate_email("user@example.com")  # No exception
        >>> try:
        ...     UserValidator.validate_email("invalid-email")
        ... except ValidationError as e:
        ...     print("Invalid email")
        Invalid email
    """
    
    @staticmethod
    def validate_email(email: str) -> None:
        """Validate email address format.
        
        Validates that the email follows standard email format patterns.
        
        Args:
            email (str): Email address to validate
            
        Raises:
            ValidationError: If email format is invalid
            
        Example:
            >>> UserValidator.validate_email("test@example.com")  # Valid
            >>> UserValidator.validate_email("user+tag@domain.co.uk")  # Valid
            
        Note:
            Uses RFC 5322 compliant regex pattern for validation.
        """
        if not email or not isinstance(email, str):
            raise ValidationError("email", "Email is required and must be a string")
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValidationError("email", "Invalid email format")
    
    @staticmethod
    def validate_username(username: str) -> None:
        """Validate username format and constraints.
        
        Validates username according to the following rules:
        - Must be 3-30 characters long
        - Can contain letters, numbers, underscores, and hyphens
        - Must start with a letter or number
        - Cannot end with underscore or hyphen
        
        Args:
            username (str): Username to validate
            
        Raises:
            ValidationError: If username doesn't meet requirements
            
        Examples:
            >>> UserValidator.validate_username("john_doe")  # Valid
            >>> UserValidator.validate_username("user123")   # Valid
            >>> UserValidator.validate_username("test-user") # Valid
            
        Note:
            Username validation is case-sensitive.
        """
        if not username or not isinstance(username, str):
            raise ValidationError("username", "Username is required and must be a string")
        
        if len(username) < 3 or len(username) > 30:
            raise ValidationError("username", "Username must be between 3 and 30 characters")
        
        username_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]$|^[a-zA-Z0-9]$'
        if not re.match(username_pattern, username):
            raise ValidationError(
                "username", 
                "Username must start and end with alphanumeric characters, "
                "and can contain letters, numbers, underscores, and hyphens"
            )
    
    @staticmethod
    def validate_full_name(full_name: str) -> None:
        """Validate full name format.
        
        Validates that the full name meets basic requirements:
        - Must not be empty
        - Must be between 1 and 100 characters
        - Can contain letters, spaces, hyphens, and apostrophes
        
        Args:
            full_name (str): Full name to validate
            
        Raises:
            ValidationError: If full name doesn't meet requirements
            
        Examples:
            >>> UserValidator.validate_full_name("John Doe")      # Valid
            >>> UserValidator.validate_full_name("Mary O'Connor") # Valid
            >>> UserValidator.validate_full_name("Jean-Pierre")   # Valid
        """
        if not full_name or not isinstance(full_name, str):
            raise ValidationError("full_name", "Full name is required and must be a string")
        
        full_name = full_name.strip()
        if len(full_name) < 1 or len(full_name) > 100:
            raise ValidationError("full_name", "Full name must be between 1 and 100 characters")
        
        name_pattern = r"^[a-zA-Z\s\-'.]+$"
        if not re.match(name_pattern, full_name):
            raise ValidationError(
                "full_name", 
                "Full name can only contain letters, spaces, hyphens, apostrophes, and periods"
            )


# Step 4: Create the main UserAPI class with comprehensive documentation
# ===============================================================================

# Explanation:
# This is the main API class that provides CRUD operations for users.
# We'll use different docstring styles to demonstrate various documentation formats.

class UserAPI:
    """User management API with comprehensive CRUD operations.
    
    This class provides a complete interface for managing users in the system.
    It includes methods for creating, reading, updating, and deleting users,
    with comprehensive error handling and validation.
    
    The API maintains an in-memory store of users and provides thread-safe
    operations for concurrent access.
    
    Attributes:
        users (Dict[int, User]): Internal storage for user objects
        next_id (int): Counter for generating unique user IDs
        username_index (Dict[str, int]): Index for fast username lookups
        email_index (Dict[str, int]): Index for fast email lookups
    
    Example:
        >>> api = UserAPI()
        >>> user = api.create_user("john_doe", "john@example.com", "John Doe")
        >>> print(user.username)
        john_doe
        >>> users = api.get_all_users()
        >>> len(users) >= 1
        True
    
    Note:
        This implementation uses in-memory storage. In production,
        you would typically use a database backend.
    """
    
    def __init__(self):
        """Initialize the UserAPI with empty storage.
        
        Sets up the internal data structures for storing users and
        maintaining indexes for efficient lookups.
        """
        self.users: Dict[int, User] = {}
        self.next_id: int = 1
        self.username_index: Dict[str, int] = {}
        self.email_index: Dict[str, int] = {}
    
    def create_user(
        self, 
        username: str, 
        email: str, 
        full_name: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> User:
        """Create a new user in the system.
        
        Creates a new user with the provided information after validating
        all input fields and checking for uniqueness constraints.
        
        Args:
            username (str): Unique username for the user (3-30 chars)
            email (str): Valid email address for the user
            full_name (str): Full display name (1-100 chars)
            metadata (Dict[str, Any], optional): Additional user data
        
        Returns:
            User: The newly created user object
        
        Raises:
            ValidationError: If any input validation fails
            UserAlreadyExistsError: If username or email already exists
        
        Examples:
            >>> api = UserAPI()
            >>> user = api.create_user(
            ...     "john_doe", 
            ...     "john@example.com", 
            ...     "John Doe"
            ... )
            >>> user.username
            'john_doe'
            
            >>> # With metadata
            >>> user = api.create_user(
            ...     "jane_doe",
            ...     "jane@example.com", 
            ...     "Jane Doe",
            ...     {"department": "Engineering", "role": "Developer"}
            ... )
            >>> user.metadata["department"]
            'Engineering'
        
        Note:
            User IDs are automatically generated and guaranteed to be unique.
            Created timestamp is automatically set to current time.
        """
        # Validate input
        UserValidator.validate_username(username)
        UserValidator.validate_email(email)
        UserValidator.validate_full_name(full_name)
        
        # Check uniqueness
        if username in self.username_index:
            raise UserAlreadyExistsError("username", username)
        
        if email in self.email_index:
            raise UserAlreadyExistsError("email", email)
        
        # Create user
        user = User(
            user_id=self.next_id,
            username=username,
            email=email,
            full_name=full_name,
            metadata=metadata or {}
        )
        
        # Store user and update indexes
        self.users[self.next_id] = user
        self.username_index[username] = self.next_id
        self.email_index[email] = self.next_id
        self.next_id += 1
        
        return user
    
    def get_user_by_id(self, user_id: int) -> User:
        """Retrieve a user by their unique ID.
        
        Parameters
        ----------
        user_id : int
            The unique identifier of the user to retrieve
        
        Returns
        -------
        User
            The user object with the specified ID
        
        Raises
        ------
        UserNotFoundError
            If no user exists with the given ID
        ValidationError
            If user_id is not a positive integer
        
        Examples
        --------
        >>> api = UserAPI()
        >>> user = api.create_user("john", "john@test.com", "John Doe")
        >>> retrieved = api.get_user_by_id(user.user_id)
        >>> retrieved.username
        'john'
        
        Notes
        -----
        This method uses NumPy-style docstring format for demonstration.
        User IDs are always positive integers starting from 1.
        """
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValidationError("user_id", "User ID must be a positive integer")
        
        if user_id not in self.users:
            raise UserNotFoundError(user_id)
        
        return self.users[user_id]
    
    def get_user_by_username(self, username: str) -> User:
        """Retrieve a user by their username.
        
        :param username: The username to search for
        :type username: str
        :returns: The user object with the specified username
        :rtype: User
        :raises UserNotFoundError: If no user exists with the given username
        :raises ValidationError: If username is invalid
        
        .. note::
           This method uses Sphinx-style docstring format for demonstration.
           Username lookups are case-sensitive.
        
        .. example::
           >>> api = UserAPI()
           >>> user = api.create_user("jane", "jane@test.com", "Jane Doe")
           >>> retrieved = api.get_user_by_username("jane")
           >>> retrieved.email
           'jane@test.com'
        """
        if not username or not isinstance(username, str):
            raise ValidationError("username", "Username must be a non-empty string")
        
        if username not in self.username_index:
            raise UserNotFoundError(username)
        
        user_id = self.username_index[username]
        return self.users[user_id]
    
    def get_all_users(self, include_inactive: bool = False) -> List[User]:
        """Retrieve all users from the system.
        
        Gets a list of all users, optionally filtering by active status.
        
        Args:
            include_inactive (bool): Whether to include inactive users.
                                   Defaults to False.
        
        Returns:
            List[User]: List of user objects matching the criteria
        
        Example:
            >>> api = UserAPI()
            >>> api.create_user("user1", "user1@test.com", "User One")
            >>> api.create_user("user2", "user2@test.com", "User Two")
            >>> users = api.get_all_users()
            >>> len(users)
            2
            
            >>> # Get all users including inactive
            >>> all_users = api.get_all_users(include_inactive=True)
            >>> len(all_users) >= len(users)
            True
        
        Note:
            Returns a copy of the user list to prevent external modification.
            Users are returned in order of creation (by user_id).
        """
        if include_inactive:
            return list(self.users.values())
        else:
            return [user for user in self.users.values() if user.is_active]
    
    def update_user(
        self,
        user_id: int,
        username: Optional[str] = None,
        email: Optional[str] = None,
        full_name: Optional[str] = None,
        is_active: Optional[bool] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> User:
        """Update an existing user's information.
        
        Updates the specified fields of an existing user. Only provided
        fields will be updated; others remain unchanged.
        
        Args:
            user_id (int): ID of the user to update
            username (str, optional): New username (must be unique)
            email (str, optional): New email address (must be unique)
            full_name (str, optional): New full name
            is_active (bool, optional): New active status
            metadata (Dict[str, Any], optional): New metadata (replaces existing)
        
        Returns:
            User: The updated user object
        
        Raises:
            UserNotFoundError: If user with given ID doesn't exist
            ValidationError: If any new values fail validation
            UserAlreadyExistsError: If new username/email conflicts with existing user
        
        Examples:
            >>> api = UserAPI()
            >>> user = api.create_user("john", "john@test.com", "John Doe")
            >>> updated = api.update_user(user.user_id, full_name="John Smith")
            >>> updated.full_name
            'John Smith'
            
            >>> # Update multiple fields
            >>> updated = api.update_user(
            ...     user.user_id,
            ...     email="john.smith@test.com",
            ...     metadata={"department": "Sales"}
            ... )
            >>> updated.email
            'john.smith@test.com'
        
        Warning:
            Updating username or email will affect login capabilities.
            Ensure users are notified of credential changes.
        """
        # Get existing user
        user = self.get_user_by_id(user_id)
        
        # Validate new values if provided
        if username is not None:
            UserValidator.validate_username(username)
            if username != user.username and username in self.username_index:
                raise UserAlreadyExistsError("username", username)
        
        if email is not None:
            UserValidator.validate_email(email)
            if email != user.email and email in self.email_index:
                raise UserAlreadyExistsError("email", email)
        
        if full_name is not None:
            UserValidator.validate_full_name(full_name)
        
        # Update indexes if username or email changed
        if username is not None and username != user.username:
            del self.username_index[user.username]
            self.username_index[username] = user_id
            user.username = username
        
        if email is not None and email != user.email:
            del self.email_index[user.email]
            self.email_index[email] = user_id
            user.email = email
        
        # Update other fields
        if full_name is not None:
            user.full_name = full_name
        
        if is_active is not None:
            user.is_active = is_active
        
        if metadata is not None:
            user.metadata = metadata
        
        return user
    
    def delete_user(self, user_id: int) -> bool:
        """Delete a user from the system.
        
        Permanently removes a user and all associated data from the system.
        This operation cannot be undone.
        
        Args:
            user_id (int): ID of the user to delete
        
        Returns:
            bool: True if user was successfully deleted
        
        Raises:
            UserNotFoundError: If user with given ID doesn't exist
            ValidationError: If user_id is invalid
        
        Examples:
            >>> api = UserAPI()
            >>> user = api.create_user("temp", "temp@test.com", "Temp User")
            >>> success = api.delete_user(user.user_id)
            >>> success
            True
            
            >>> # Verify user is gone
            >>> try:
            ...     api.get_user_by_id(user.user_id)
            ... except UserNotFoundError:
            ...     print("User successfully deleted")
            User successfully deleted
        
        Warning:
            This operation is irreversible. Consider deactivating users
            instead of deleting them to preserve data integrity.
        """
        # Get user to ensure it exists and get username/email for index cleanup
        user = self.get_user_by_id(user_id)
        
        # Remove from all indexes and storage
        del self.users[user_id]
        del self.username_index[user.username]
        del self.email_index[user.email]
        
        return True
    
    def deactivate_user(self, user_id: int) -> User:
        """Deactivate a user account without deleting data.
        
        Marks a user as inactive, preventing login while preserving
        all user data for potential future reactivation.
        
        Args:
            user_id (int): ID of the user to deactivate
        
        Returns:
            User: The deactivated user object
        
        Raises:
            UserNotFoundError: If user with given ID doesn't exist
        
        Example:
            >>> api = UserAPI()
            >>> user = api.create_user("john", "john@test.com", "John Doe")
            >>> deactivated = api.deactivate_user(user.user_id)
            >>> deactivated.is_active
            False
        
        Note:
            Deactivated users won't appear in get_all_users() by default.
            Use get_all_users(include_inactive=True) to include them.
        """
        return self.update_user(user_id, is_active=False)


# Step 5: Add comprehensive examples and usage demonstrations
# ===============================================================================

# Explanation:
# This section demonstrates how to use the API with real-world examples,
# error handling patterns, and best practices for API consumers.

def demonstrate_api_usage():
    """Comprehensive demonstration of the UserAPI functionality.
    
    This function showcases all major API operations with proper error
    handling and demonstrates best practices for API usage.
    
    Returns:
        Dict[str, Any]: Summary of operations performed
    
    Example:
        >>> results = demonstrate_api_usage()
        >>> results['users_created'] > 0
        True
        >>> results['operations_successful']
        True
    """
    print("=== UserAPI Demonstration ===\n")
    
    # Initialize API
    api = UserAPI()
    results = {
        'users_created': 0,
        'users_updated': 0,
        'users_deleted': 0,
        'operations_successful': True,
        'errors_handled': []
    }
    
    try:
        # 1. Create users with different scenarios
        print("1. Creating users...")
        
        # Basic user creation
        user1 = api.create_user(
            username="john_doe",
            email="john@example.com",
            full_name="John Doe"
        )
        print(f"   Created user: {user1.username} (ID: {user1.user_id})")
        results['users_created'] += 1
        
        # User with metadata
        user2 = api.create_user(
            username="jane_smith",
            email="jane@example.com",
            full_name="Jane Smith",
            metadata={
                "department": "Engineering",
                "role": "Senior Developer",
                "hire_date": "2025-01-15"
            }
        )
        print(f"   Created user with metadata: {user2.username}")
        results['users_created'] += 1
        
        # 2. Demonstrate error handling
        print("\n2. Demonstrating error handling...")
        
        try:
            # Try to create duplicate username
            api.create_user("john_doe", "different@email.com", "Different Person")
        except UserAlreadyExistsError as e:
            print(f"   ✓ Caught expected error: {e.message}")
            results['errors_handled'].append("duplicate_username")
        
        try:
            # Try invalid email
            api.create_user("invalid_user", "not-an-email", "Invalid User")
        except ValidationError as e:
            print(f"   ✓ Caught validation error: {e.message}")
            results['errors_handled'].append("invalid_email")
        
        # 3. Read operations
        print("\n3. Reading user data...")
        
        # Get by ID
        retrieved_user = api.get_user_by_id(user1.user_id)
        print(f"   Retrieved by ID: {retrieved_user.username}")
        
        # Get by username
        retrieved_user2 = api.get_user_by_username("jane_smith")
        print(f"   Retrieved by username: {retrieved_user2.full_name}")
        
        # Get all users
        all_users = api.get_all_users()
        print(f"   Total active users: {len(all_users)}")
        
        # 4. Update operations
        print("\n4. Updating user data...")
        
        updated_user = api.update_user(
            user1.user_id,
            full_name="John D. Doe",
            metadata={"title": "Software Engineer", "location": "Remote"}
        )
        print(f"   Updated user: {updated_user.full_name}")
        results['users_updated'] += 1
        
        # 5. Deactivate user
        print("\n5. Deactivating user...")
        
        deactivated = api.deactivate_user(user2.user_id)
        print(f"   Deactivated user: {deactivated.username} (active: {deactivated.is_active})")
        
        # Check active users count
        active_users = api.get_all_users()
        all_users_including_inactive = api.get_all_users(include_inactive=True)
        print(f"   Active users: {len(active_users)}")
        print(f"   Total users (including inactive): {len(all_users_including_inactive)}")
        
        # 6. Delete user
        print("\n6. Deleting user...")
        
        success = api.delete_user(user1.user_id)
        print(f"   User deletion successful: {success}")
        results['users_deleted'] += 1
        
        # Verify deletion
        try:
            api.get_user_by_id(user1.user_id)
        except UserNotFoundError:
            print("   ✓ Confirmed user was deleted")
        
        print("\n=== Demonstration Complete ===")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        results['operations_successful'] = False
    
    return results


def demonstrate_error_handling_patterns():
    """Demonstrate best practices for handling API errors.
    
    Shows different approaches to error handling when using the UserAPI,
    including specific exception handling and generic error handling.
    
    Examples:
        >>> demonstrate_error_handling_patterns()
        === Error Handling Patterns ===
        ...
    """
    print("=== Error Handling Patterns ===\n")
    
    api = UserAPI()
    
    # Pattern 1: Specific exception handling
    print("1. Specific exception handling:")
    
    def safe_create_user(username: str, email: str, full_name: str) -> Optional[User]:
        """Safely create a user with comprehensive error handling."""
        try:
            return api.create_user(username, email, full_name)
        except ValidationError as e:
            print(f"   Validation failed: {e.message}")
            return None
        except UserAlreadyExistsError as e:
            print(f"   User already exists: {e.message}")
            return None
        except APIError as e:
            print(f"   API error: {e.message}")
            return None
    
    # Test the safe creation
    user = safe_create_user("test_user", "test@example.com", "Test User")
    if user:
        print(f"   ✓ User created successfully: {user.username}")
    
    # Try to create duplicate
    duplicate = safe_create_user("test_user", "different@email.com", "Different User")
    if not duplicate:
        print("   ✓ Duplicate creation properly handled")
    
    # Pattern 2: Generic error handling with logging
    print("\n2. Generic error handling with context:")
    
    def api_operation_with_context(operation_name: str, operation_func):
        """Execute an API operation with context and error logging."""
        try:
            result = operation_func()
            print(f"   ✓ {operation_name} completed successfully")
            return result
        except APIError as e:
            print(f"   ✗ {operation_name} failed: {e.message} (Code: {e.error_code})")
            return None
        except Exception as e:
            print(f"   ✗ {operation_name} failed with unexpected error: {e}")
            return None
    
    # Test operations with context
    api_operation_with_context(
        "Get user by ID",
        lambda: api.get_user_by_id(999)  # Non-existent user
    )
    
    api_operation_with_context(
        "Update user",
        lambda: api.update_user(999, full_name="New Name")  # Non-existent user
    )
    
    print("\n=== Error Handling Demo Complete ===")


# Step 6: Add utility functions and helper methods
# ===============================================================================

# Explanation:
# Additional utility functions that complement the main API and demonstrate
# advanced documentation techniques for helper functions.

class UserAPIUtils:
    """Utility functions for working with UserAPI data.
    
    This class provides helper methods for common operations like
    data export, import, and bulk operations.
    """
    
    @staticmethod
    def export_users_to_dict(api: UserAPI, include_inactive: bool = False) -> Dict[str, Any]:
        """Export all users to a dictionary format suitable for JSON serialization.
        
        Args:
            api (UserAPI): The UserAPI instance to export from
            include_inactive (bool): Whether to include inactive users
        
        Returns:
            Dict[str, Any]: Dictionary containing user data and metadata
        
        Example:
            >>> api = UserAPI()
            >>> api.create_user("john", "john@test.com", "John Doe")
            >>> data = UserAPIUtils.export_users_to_dict(api)
            >>> 'users' in data
            True
            >>> 'metadata' in data
            True
        """
        users = api.get_all_users(include_inactive=include_inactive)
        
        return {
            'users': [user.to_dict() for user in users],
            'metadata': {
                'export_timestamp': datetime.now().isoformat(),
                'total_users': len(users),
                'include_inactive': include_inactive
            }
        }
    
    @staticmethod
    def bulk_create_users(api: UserAPI, user_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create multiple users in a single operation.
        
        Args:
            api (UserAPI): The UserAPI instance to use
            user_data (List[Dict[str, Any]]): List of user data dictionaries
        
        Returns:
            Dict[str, Any]: Results summary with created users and errors
        
        Example:
            >>> api = UserAPI()
            >>> users_data = [
            ...     {"username": "user1", "email": "user1@test.com", "full_name": "User One"},
            ...     {"username": "user2", "email": "user2@test.com", "full_name": "User Two"}
            ... ]
            >>> results = UserAPIUtils.bulk_create_users(api, users_data)
            >>> results['successful_count']
            2
        """
        results = {
            'successful_count': 0,
            'failed_count': 0,
            'created_users': [],
            'errors': []
        }
        
        for i, data in enumerate(user_data):
            try:
                user = api.create_user(
                    username=data['username'],
                    email=data['email'],
                    full_name=data['full_name'],
                    metadata=data.get('metadata')
                )
                results['created_users'].append(user.to_dict())
                results['successful_count'] += 1
            except Exception as e:
                results['errors'].append({
                    'index': i,
                    'data': data,
                    'error': str(e)
                })
                results['failed_count'] += 1
        
        return results


# Step 7: Main execution and testing section
# ===============================================================================

# Explanation:
# This final section provides a complete example of how to run and test
# the API, demonstrating all features in a real-world scenario.

def main():
    """Main function demonstrating complete API usage.
    
    This function serves as both a demonstration and a basic test suite
    for the UserAPI functionality.
    
    Returns:
        bool: True if all demonstrations completed successfully
    """
    print("🚀 Starting UserAPI Documentation Demonstration\n")
    
    try:
        # Run basic API demonstration
        print("📋 Running basic API operations...")
        demo_results = demonstrate_api_usage()
        
        if demo_results['operations_successful']:
            print("✅ Basic operations completed successfully")
        else:
            print("❌ Some basic operations failed")
            return False
        
        print("\n" + "="*50 + "\n")
        
        # Run error handling demonstration
        print("🛡️ Running error handling demonstration...")
        demonstrate_error_handling_patterns()
        print("✅ Error handling demonstration completed")
        
        print("\n" + "="*50 + "\n")
        
        # Run utility functions demonstration
        print("🔧 Running utility functions demonstration...")
        
        # Create a fresh API instance for utilities demo
        api = UserAPI()
        
        # Create some test users
        test_users = [
            {"username": "alice", "email": "alice@test.com", "full_name": "Alice Johnson"},
            {"username": "bob", "email": "bob@test.com", "full_name": "Bob Wilson"},
            {"username": "charlie", "email": "charlie@test.com", "full_name": "Charlie Brown"}
        ]
        
        # Bulk create users
        bulk_results = UserAPIUtils.bulk_create_users(api, test_users)
        print(f"   Bulk creation: {bulk_results['successful_count']} successful, {bulk_results['failed_count']} failed")
        
        # Export users
        export_data = UserAPIUtils.export_users_to_dict(api)
        print(f"   Export: {len(export_data['users'])} users exported")
        print(f"   Export timestamp: {export_data['metadata']['export_timestamp']}")
        
        print("✅ Utility functions demonstration completed")
        
        print("\n" + "="*50 + "\n")
        
        # Summary
        print("📊 DEMONSTRATION SUMMARY:")
        print(f"   • Users created in demo: {demo_results['users_created']}")
        print(f"   • Users updated in demo: {demo_results['users_updated']}")
        print(f"   • Users deleted in demo: {demo_results['users_deleted']}")
        print(f"   • Errors properly handled: {len(demo_results['errors_handled'])}")
        print(f"   • Bulk users created: {bulk_results['successful_count']}")
        print(f"   • Total users exported: {len(export_data['users'])}")
        
        print("\n🎉 All demonstrations completed successfully!")
        print("\n📚 This example demonstrates:")
        print("   ✓ Comprehensive API documentation with multiple docstring styles")
        print("   ✓ Proper type hints for all functions and methods")
        print("   ✓ Detailed error handling with custom exceptions")
        print("   ✓ Real-world usage examples and patterns")
        print("   ✓ Utility functions and helper methods")
        print("   ✓ Best practices for API design and documentation")
        
        return True
        
    except Exception as e:
        print(f"❌ Demonstration failed with error: {e}")
        return False


# Additional documentation examples showing different styles
# ===============================================================================

class DocumentationStyleExamples:
    """Examples of different documentation styles for reference.
    
    This class demonstrates various docstring formats that can be used
    in Python projects, each with their own advantages and use cases.
    """
    
    def google_style_example(self, param1: str, param2: int = 10) -> bool:
        """Example of Google-style docstring format.
        
        This is the most commonly used format, especially in Google's
        Python projects and many open-source libraries.
        
        Args:
            param1 (str): Description of the first parameter
            param2 (int, optional): Description of the second parameter. 
                                   Defaults to 10.
        
        Returns:
            bool: Description of the return value
        
        Raises:
            ValueError: If param1 is empty
            TypeError: If param2 is not an integer
        
        Example:
            >>> obj = DocumentationStyleExamples()
            >>> result = obj.google_style_example("test", 5)
            >>> isinstance(result, bool)
            True
        
        Note:
            This format is clean, readable, and well-supported by
            documentation generation tools like Sphinx.
        """
        if not param1:
            raise ValueError("param1 cannot be empty")
        if not isinstance(param2, int):
            raise TypeError("param2 must be an integer")
        return len(param1) > param2
    
    def numpy_style_example(self, data: List[float]) -> float:
        """Example of NumPy-style docstring format.
        
        This format is commonly used in scientific Python libraries
        and provides a more structured approach to documentation.
        
        Parameters
        ----------
        data : List[float]
            A list of numerical values to process
        
        Returns
        -------
        float
            The calculated average of the input data
        
        Raises
        ------
        ValueError
            If the data list is empty
        TypeError
            If data contains non-numeric values
        
        Examples
        --------
        >>> obj = DocumentationStyleExamples()
        >>> result = obj.numpy_style_example([1.0, 2.0, 3.0])
        >>> result
        2.0
        
        See Also
        --------
        statistics.mean : Built-in function for calculating means
        numpy.mean : NumPy function for array means
        
        Notes
        -----
        This format is particularly good for mathematical functions
        and scientific computing applications.
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("All data elements must be numeric")
        return sum(data) / len(data)
    
    def sphinx_style_example(self, text: str, encoding: str = 'utf-8') -> bytes:
        """Example of Sphinx-style docstring format.
        
        This format uses reStructuredText markup and is particularly
        well-suited for projects that use Sphinx for documentation.
        
        :param text: The text string to encode
        :type text: str
        :param encoding: The character encoding to use
        :type encoding: str
        :returns: The encoded bytes representation
        :rtype: bytes
        :raises UnicodeEncodeError: If encoding fails
        :raises TypeError: If text is not a string
        
        .. note::
           This format allows for rich markup and cross-references
           in the generated documentation.
        
        .. example::
           >>> obj = DocumentationStyleExamples()
           >>> result = obj.sphinx_style_example("hello")
           >>> isinstance(result, bytes)
           True
        
        .. seealso::
           :func:`str.encode` for the underlying encoding method
        """
        if not isinstance(text, str):
            raise TypeError("Text must be a string")
        return text.encode(encoding)


# Run the demonstration if this file is executed directly
if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

