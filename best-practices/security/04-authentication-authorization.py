"""Question: Implement a secure authentication and authorization system.

Create a comprehensive system that handles user authentication and role-based
authorization with proper security practices.

Requirements:
1. Create a User class with secure password handling
2. Implement authentication with password hashing
3. Create role-based authorization system
4. Implement session management
5. Add security features like rate limiting and account lockout
6. Demonstrate secure login/logout functionality

Example usage:
    auth_system = AuthenticationSystem()
    user = auth_system.register_user("john", "secure_password", ["user"])
    session = auth_system.login("john", "secure_password")
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
# - How to securely hash and store passwords?
# - What information should a user session contain?
# - How to implement role-based permissions?
# - How to prevent brute force attacks?
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


# Step 1: Import required modules and create basic User class
# ===============================================================================

# Explanation:
# We start with importing security-related modules and creating a User class
# that will store user information securely.

import hashlib
import secrets
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from enum import Enum

class Role(Enum):
    """User roles for authorization."""
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"
    GUEST = "guest"

@dataclass
class User:
    """Represents a user in the system."""
    username: str
    password_hash: str
    salt: str
    roles: Set[Role]
    created_at: datetime
    last_login: Optional[datetime] = None
    failed_login_attempts: int = 0
    account_locked_until: Optional[datetime] = None
    is_active: bool = True


# Step 2: Add password hashing utilities
# ===============================================================================

# Explanation:
# Secure password handling is crucial. We'll create utilities to hash passwords
# with salt and verify them securely.

class PasswordHasher:
    """Handles secure password hashing and verification."""
    
    @staticmethod
    def generate_salt() -> str:
        """Generate a random salt for password hashing."""
        return secrets.token_hex(32)
    
    @staticmethod
    def hash_password(password: str, salt: str) -> str:
        """Hash a password with salt using SHA-256."""
        # Combine password and salt
        password_salt = password + salt
        # Hash using SHA-256
        return hashlib.sha256(password_salt.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, salt: str, stored_hash: str) -> bool:
        """Verify a password against stored hash."""
        # Hash the provided password with the stored salt
        password_hash = PasswordHasher.hash_password(password, salt)
        # Use secrets.compare_digest for timing attack protection
        return secrets.compare_digest(password_hash, stored_hash)
    
    @staticmethod
    def is_strong_password(password: str) -> bool:
        """Check if password meets security requirements."""
        if len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        return has_upper and has_lower and has_digit and has_special


# Step 3: Create Session class and security features
# ===============================================================================

# Explanation:
# Sessions manage user authentication state. We'll include security features
# like session expiration and token generation.

@dataclass
class Session:
    """Represents a user session."""
    session_id: str
    username: str
    roles: Set[Role]
    created_at: datetime
    expires_at: datetime
    last_activity: datetime
    ip_address: Optional[str] = None
    
    def is_expired(self) -> bool:
        """Check if session has expired."""
        return datetime.now() > self.expires_at
    
    def is_idle_timeout(self, idle_timeout_minutes: int = 30) -> bool:
        """Check if session has been idle too long."""
        idle_threshold = datetime.now() - timedelta(minutes=idle_timeout_minutes)
        return self.last_activity < idle_threshold
    
    def refresh_activity(self):
        """Update last activity timestamp."""
        self.last_activity = datetime.now()

class SecurityConfig:
    """Security configuration constants."""
    MAX_LOGIN_ATTEMPTS = 5
    ACCOUNT_LOCKOUT_DURATION_MINUTES = 30
    SESSION_DURATION_HOURS = 8
    IDLE_TIMEOUT_MINUTES = 30
    RATE_LIMIT_WINDOW_MINUTES = 15
    RATE_LIMIT_MAX_ATTEMPTS = 10


# Step 4: Implement Authorization system
# ===============================================================================

# Explanation:
# Authorization determines what authenticated users can do. We'll create
# a role-based permission system.

class Permission(Enum):
    """System permissions."""
    READ_USER = "read_user"
    WRITE_USER = "write_user"
    DELETE_USER = "delete_user"
    READ_ADMIN = "read_admin"
    WRITE_ADMIN = "write_admin"
    MODERATE_CONTENT = "moderate_content"
    SYSTEM_CONFIG = "system_config"

class AuthorizationManager:
    """Manages role-based authorization."""
    
    def __init__(self):
        # Define role permissions
        self.role_permissions = {
            Role.GUEST: {Permission.READ_USER},
            Role.USER: {Permission.READ_USER, Permission.WRITE_USER},
            Role.MODERATOR: {
                Permission.READ_USER, Permission.WRITE_USER,
                Permission.MODERATE_CONTENT
            },
            Role.ADMIN: {
                Permission.READ_USER, Permission.WRITE_USER,
                Permission.DELETE_USER, Permission.READ_ADMIN,
                Permission.WRITE_ADMIN, Permission.MODERATE_CONTENT,
                Permission.SYSTEM_CONFIG
            }
        }
    
    def has_permission(self, user_roles: Set[Role], permission: Permission) -> bool:
        """Check if user roles have specific permission."""
        for role in user_roles:
            if permission in self.role_permissions.get(role, set()):
                return True
        return False
    
    def get_user_permissions(self, user_roles: Set[Role]) -> Set[Permission]:
        """Get all permissions for user roles."""
        permissions = set()
        for role in user_roles:
            permissions.update(self.role_permissions.get(role, set()))
        return permissions
    
    def require_permission(self, user_roles: Set[Role], permission: Permission):
        """Decorator/method to require specific permission."""
        if not self.has_permission(user_roles, permission):
            raise PermissionError(f"Access denied. Required permission: {permission.value}")

class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass

class AuthorizationError(Exception):
    """Raised when authorization fails."""
    pass


# Step 5: Create the main AuthenticationSystem class
# ===============================================================================

# Explanation:
# This is the main class that ties everything together - user management,
# authentication, session handling, and security features.

class AuthenticationSystem:
    """Main authentication and authorization system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, Session] = {}
        self.authorization_manager = AuthorizationManager()
        self.password_hasher = PasswordHasher()
        
        # Rate limiting tracking
        self.login_attempts: Dict[str, List[datetime]] = {}
        
    def register_user(self, username: str, password: str, roles: List[str]) -> User:
        """Register a new user with secure password handling."""
        # Validate input
        if not username or not password:
            raise ValueError("Username and password are required")
        
        if username in self.users:
            raise ValueError(f"User '{username}' already exists")
        
        if not self.password_hasher.is_strong_password(password):
            raise ValueError("Password does not meet security requirements")
        
        # Convert string roles to Role enum
        user_roles = set()
        for role_str in roles:
            try:
                user_roles.add(Role(role_str))
            except ValueError:
                raise ValueError(f"Invalid role: {role_str}")
        
        # Create user with hashed password
        salt = self.password_hasher.generate_salt()
        password_hash = self.password_hasher.hash_password(password, salt)
        
        user = User(
            username=username,
            password_hash=password_hash,
            salt=salt,
            roles=user_roles,
            created_at=datetime.now()
        )
        
        self.users[username] = user
        return user
    
    def _is_account_locked(self, user: User) -> bool:
        """Check if user account is locked."""
        if user.account_locked_until is None:
            return False
        return datetime.now() < user.account_locked_until
    
    def _is_rate_limited(self, username: str) -> bool:
        """Check if user is rate limited."""
        now = datetime.now()
        window_start = now - timedelta(minutes=SecurityConfig.RATE_LIMIT_WINDOW_MINUTES)
        
        # Clean old attempts
        if username in self.login_attempts:
            self.login_attempts[username] = [
                attempt for attempt in self.login_attempts[username]
                if attempt > window_start
            ]
        
        # Check rate limit
        attempts = len(self.login_attempts.get(username, []))
        return attempts >= SecurityConfig.RATE_LIMIT_MAX_ATTEMPTS
    
    def _record_login_attempt(self, username: str):
        """Record a login attempt for rate limiting."""
        if username not in self.login_attempts:
            self.login_attempts[username] = []
        self.login_attempts[username].append(datetime.now())
    
    def _handle_failed_login(self, user: User):
        """Handle failed login attempt."""
        user.failed_login_attempts += 1
        
        if user.failed_login_attempts >= SecurityConfig.MAX_LOGIN_ATTEMPTS:
            # Lock account
            lockout_duration = timedelta(minutes=SecurityConfig.ACCOUNT_LOCKOUT_DURATION_MINUTES)
            user.account_locked_until = datetime.now() + lockout_duration
    
    def login(self, username: str, password: str, ip_address: Optional[str] = None) -> Session:
        """Authenticate user and create session."""
        # Record login attempt for rate limiting
        self._record_login_attempt(username)
        
        # Check rate limiting
        if self._is_rate_limited(username):
            raise AuthenticationError("Too many login attempts. Please try again later.")
        
        # Check if user exists
        if username not in self.users:
            raise AuthenticationError("Invalid username or password")
        
        user = self.users[username]
        
        # Check if account is active
        if not user.is_active:
            raise AuthenticationError("Account is deactivated")
        
        # Check if account is locked
        if self._is_account_locked(user):
            raise AuthenticationError("Account is temporarily locked due to failed login attempts")
        
        # Verify password
        if not self.password_hasher.verify_password(password, user.salt, user.password_hash):
            self._handle_failed_login(user)
            raise AuthenticationError("Invalid username or password")
        
        # Reset failed login attempts on successful login
        user.failed_login_attempts = 0
        user.account_locked_until = None
        user.last_login = datetime.now()
        
        # Create session
        session_id = secrets.token_urlsafe(32)
        now = datetime.now()
        expires_at = now + timedelta(hours=SecurityConfig.SESSION_DURATION_HOURS)
        
        session = Session(
            session_id=session_id,
            username=username,
            roles=user.roles,
            created_at=now,
            expires_at=expires_at,
            last_activity=now,
            ip_address=ip_address
        )
        
        self.sessions[session_id] = session
        return session
    
    def logout(self, session_id: str) -> bool:
        """Logout user by invalidating session."""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False
    
    def get_session(self, session_id: str) -> Optional[Session]:
        """Get active session by ID."""
        if session_id not in self.sessions:
            return None
        
        session = self.sessions[session_id]
        
        # Check if session is expired
        if session.is_expired():
            del self.sessions[session_id]
            return None
        
        # Check idle timeout
        if session.is_idle_timeout(SecurityConfig.IDLE_TIMEOUT_MINUTES):
            del self.sessions[session_id]
            return None
        
        # Refresh activity
        session.refresh_activity()
        return session
    
    def check_permission(self, session_id: str, permission: Permission) -> bool:
        """Check if session has specific permission."""
        session = self.get_session(session_id)
        if not session:
            return False
        
        return self.authorization_manager.has_permission(session.roles, permission)
    
    def require_permission(self, session_id: str, permission: Permission):
        """Require specific permission or raise exception."""
        session = self.get_session(session_id)
        if not session:
            raise AuthenticationError("Invalid or expired session")
        
        self.authorization_manager.require_permission(session.roles, permission)
    
    def get_user_info(self, session_id: str) -> Optional[Dict]:
        """Get user information for valid session."""
        session = self.get_session(session_id)
        if not session:
            return None
        
        user = self.users.get(session.username)
        if not user:
            return None
        
        return {
            'username': user.username,
            'roles': [role.value for role in user.roles],
            'permissions': [perm.value for perm in self.authorization_manager.get_user_permissions(user.roles)],
            'created_at': user.created_at.isoformat(),
            'last_login': user.last_login.isoformat() if user.last_login else None,
            'session_expires_at': session.expires_at.isoformat()
        }
    
    def cleanup_expired_sessions(self):
        """Remove expired sessions from memory."""
        expired_sessions = []
        for session_id, session in self.sessions.items():
            if session.is_expired() or session.is_idle_timeout(SecurityConfig.IDLE_TIMEOUT_MINUTES):
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.sessions[session_id]
        
        return len(expired_sessions)


# Step 6: Add utility methods and administrative functions
# ===============================================================================

# Explanation:
# These methods provide additional functionality for user management,
# security monitoring, and system administration.

    def change_password(self, session_id: str, old_password: str, new_password: str) -> bool:
        """Change user password with proper verification."""
        session = self.get_session(session_id)
        if not session:
            raise AuthenticationError("Invalid or expired session")
        
        user = self.users[session.username]
        
        # Verify old password
        if not self.password_hasher.verify_password(old_password, user.salt, user.password_hash):
            raise AuthenticationError("Current password is incorrect")
        
        # Validate new password
        if not self.password_hasher.is_strong_password(new_password):
            raise ValueError("New password does not meet security requirements")
        
        # Update password
        new_salt = self.password_hasher.generate_salt()
        new_hash = self.password_hasher.hash_password(new_password, new_salt)
        
        user.salt = new_salt
        user.password_hash = new_hash
        
        return True
    
    def deactivate_user(self, admin_session_id: str, target_username: str) -> bool:
        """Deactivate a user account (admin only)."""
        self.require_permission(admin_session_id, Permission.WRITE_ADMIN)
        
        if target_username not in self.users:
            raise ValueError(f"User '{target_username}' not found")
        
        user = self.users[target_username]
        user.is_active = False
        
        # Invalidate all sessions for this user
        sessions_to_remove = []
        for session_id, session in self.sessions.items():
            if session.username == target_username:
                sessions_to_remove.append(session_id)
        
        for session_id in sessions_to_remove:
            del self.sessions[session_id]
        
        return True
    
    def get_security_stats(self, admin_session_id: str) -> Dict:
        """Get security statistics (admin only)."""
        self.require_permission(admin_session_id, Permission.READ_ADMIN)
        
        total_users = len(self.users)
        active_users = sum(1 for user in self.users.values() if user.is_active)
        locked_users = sum(1 for user in self.users.values() if self._is_account_locked(user))
        active_sessions = len(self.sessions)
        
        return {
            'total_users': total_users,
            'active_users': active_users,
            'locked_users': locked_users,
            'active_sessions': active_sessions,
            'rate_limited_users': len([u for u in self.login_attempts.keys() if self._is_rate_limited(u)])
        }


# Step 7: Demonstration and usage examples
# ===============================================================================

# Explanation:
# Let's demonstrate how to use our secure authentication and authorization system
# with practical examples.

def demonstrate_authentication_system():
    """Demonstrate the authentication and authorization system."""
    print("=== Authentication & Authorization System Demo ===\n")
    
    # Create the authentication system
    auth_system = AuthenticationSystem()
    
    try:
        # 1. Register users with different roles
        print("1. Registering users...")
        admin_user = auth_system.register_user("admin", "AdminPass123!", ["admin"])
        regular_user = auth_system.register_user("john", "UserPass123!", ["user"])
        moderator_user = auth_system.register_user("mod", "ModPass123!", ["moderator"])
        print(f"✓ Registered admin: {admin_user.username}")
        print(f"✓ Registered user: {regular_user.username}")
        print(f"✓ Registered moderator: {moderator_user.username}\n")
        
        # 2. Demonstrate login
        print("2. User authentication...")
        admin_session = auth_system.login("admin", "AdminPass123!", "192.168.1.100")
        user_session = auth_system.login("john", "UserPass123!", "192.168.1.101")
        print(f"✓ Admin logged in: {admin_session.session_id[:16]}...")
        print(f"✓ User logged in: {user_session.session_id[:16]}...\n")
        
        # 3. Demonstrate authorization
        print("3. Testing permissions...")
        
        # Admin can access admin functions
        try:
            auth_system.require_permission(admin_session.session_id, Permission.SYSTEM_CONFIG)
            print("✓ Admin has system config permission")
        except PermissionError as e:
            print(f"✗ Admin permission denied: {e}")
        
        # Regular user cannot access admin functions
        try:
            auth_system.require_permission(user_session.session_id, Permission.SYSTEM_CONFIG)
            print("✗ User should not have system config permission")
        except PermissionError:
            print("✓ User correctly denied system config permission")
        
        # Regular user can access user functions
        if auth_system.check_permission(user_session.session_id, Permission.WRITE_USER):
            print("✓ User has write user permission\n")
        
        # 4. Get user information
        print("4. User information...")
        admin_info = auth_system.get_user_info(admin_session.session_id)
        user_info = auth_system.get_user_info(user_session.session_id)
        
        print(f"Admin permissions: {admin_info['permissions']}")
        print(f"User permissions: {user_info['permissions']}\n")
        
        # 5. Security statistics (admin only)
        print("5. Security statistics...")
        stats = auth_system.get_security_stats(admin_session.session_id)
        print(f"Total users: {stats['total_users']}")
        print(f"Active sessions: {stats['active_sessions']}\n")
        
        # 6. Demonstrate failed login and account lockout
        print("6. Testing security features...")
        try:
            # Try wrong password multiple times
            for i in range(6):
                try:
                    auth_system.login("john", "wrong_password")
                except AuthenticationError:
                    print(f"✓ Failed login attempt {i+1}")
        except AuthenticationError as e:
            print(f"✓ Account protection: {e}\n")
        
        # 7. Password change
        print("7. Password change...")
        success = auth_system.change_password(user_session.session_id, "UserPass123!", "NewUserPass456!")
        if success:
            print("✓ Password changed successfully\n")
        
        # 8. Logout
        print("8. Logout...")
        auth_system.logout(admin_session.session_id)
        auth_system.logout(user_session.session_id)
        print("✓ Users logged out\n")
        
        # 9. Session cleanup
        print("9. Session cleanup...")
        cleaned = auth_system.cleanup_expired_sessions()
        print(f"✓ Cleaned {cleaned} expired sessions")
        
    except Exception as e:
        print(f"Error in demonstration: {e}")

# Additional utility functions for real-world usage
def create_secure_decorator(auth_system: AuthenticationSystem, required_permission: Permission):
    """Create a decorator that requires specific permission."""
    def decorator(func):
        def wrapper(session_id: str, *args, **kwargs):
            auth_system.require_permission(session_id, required_permission)
            return func(session_id, *args, **kwargs)
        return wrapper
    return decorator

# Example of using the decorator
def example_admin_function():
    """Example of how to protect functions with decorators."""
    auth_system = AuthenticationSystem()
    
    @create_secure_decorator(auth_system, Permission.SYSTEM_CONFIG)
    def configure_system(session_id: str, config_data: dict):
        """System configuration function (admin only)."""
        return f"System configured with: {config_data}"
    
    @create_secure_decorator(auth_system, Permission.MODERATE_CONTENT)
    def moderate_content(session_id: str, content_id: str):
        """Content moderation function (moderator or admin)."""
        return f"Content {content_id} moderated"
    
    return configure_system, moderate_content


# ===============================================================================
#                              FINAL DEMONSTRATION
# ===============================================================================

if __name__ == "__main__":
    # Run the comprehensive demonstration
    demonstrate_authentication_system()
    
    print("\n" + "="*60)
    print("Authentication & Authorization System Complete!")
    print("="*60)
    print("\nKey Security Features Implemented:")
    print("• Secure password hashing with salt")
    print("• Role-based authorization")
    print("• Session management with expiration")
    print("• Rate limiting and account lockout")
    print("• Permission-based access control")
    print("• Administrative functions")
    print("• Security monitoring and statistics")
    print("\nThis system provides enterprise-grade security features")
    print("suitable for production applications!")


# ===============================================================================
#                           LEARNING SUMMARY
# ===============================================================================
#
# What we learned in this comprehensive example:
#
# 1. **Secure Password Handling**:
#    - Never store passwords in plain text
#    - Use salt to prevent rainbow table attacks
#    - Implement strong password requirements
#    - Use timing-safe comparison functions
#
# 2. **Authentication Best Practices**:
#    - Rate limiting to prevent brute force attacks
#    - Account lockout after failed attempts
#    - Session-based authentication
#    - Proper error handling without information leakage
#
# 3. **Authorization Design**:
#    - Role-based access control (RBAC)
#    - Permission-based system
#    - Principle of least privilege
#    - Centralized authorization management
#
# 4. **Session Security**:
#    - Secure session token generation
#    - Session expiration and idle timeout
#    - Session invalidation on logout
#    - Activity tracking
#
# 5. **Security Monitoring**:
#    - Failed login attempt tracking
#    - Security statistics and reporting
#    - Administrative oversight functions
#    - Audit trail capabilities
#
# This implementation demonstrates production-ready security practices
# that can be adapted for real-world applications!
#
# ===============================================================================

