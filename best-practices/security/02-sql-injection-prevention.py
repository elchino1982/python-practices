"""Question: Implement SQL injection prevention techniques to secure database operations.

Create a secure database interface that demonstrates various SQL injection prevention methods
including parameterized queries, input validation, and ORM usage.

Requirements:
1. Create a vulnerable database class to show SQL injection risks
2. Create a secure database class with parameterized queries
3. Implement input validation and sanitization
4. Demonstrate ORM-based approaches
5. Show different attack vectors and their prevention

Example usage:
    secure_db = SecureDatabase()
    user = secure_db.get_user_by_credentials("john", "password123")
    secure_db.create_user("jane", "jane@example.com", "securepass")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what makes SQL queries vulnerable
# - Consider different types of SQL injection attacks
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
# - What makes SQL queries vulnerable to injection?
# - How can parameterized queries prevent injection?
# - What input validation techniques can you use?
# - How do ORMs help prevent SQL injection?
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


# Step 1: Import modules and create a vulnerable database class
# ===============================================================================

# Explanation:
# First, we'll create a vulnerable database class to demonstrate SQL injection risks.
# This shows what NOT to do and helps understand the security issues.

import sqlite3
import re
import hashlib
import secrets
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

@dataclass
class User:
    """User data class."""
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    password_hash: str = ""

class VulnerableDatabase:
    """VULNERABLE database class - DO NOT USE IN PRODUCTION!
    
    This class demonstrates common SQL injection vulnerabilities.
    It's included for educational purposes only.
    """
    
    def __init__(self, db_path: str = ":memory:"):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._create_tables()
    
    def _create_tables(self):
        """Create user table."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        self.connection.commit()
    
    def get_user_by_credentials_vulnerable(self, username: str, password: str) -> Optional[User]:
        """VULNERABLE: Uses string concatenation - susceptible to SQL injection."""
        cursor = self.connection.cursor()
        
        # VULNERABLE CODE - DO NOT USE!
        query = f"SELECT * FROM users WHERE username = '{username}' AND password_hash = '{password}'"
        
        try:
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                return User(id=row['id'], username=row['username'], 
                          email=row['email'], password_hash=row['password_hash'])
            return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

# Step 2: Add more vulnerable methods to show different attack vectors
# ===============================================================================

# Explanation:
# Let's add more vulnerable methods to demonstrate different types of SQL injection
# attacks including search functionality and user creation.

    def search_users_vulnerable(self, search_term: str) -> List[User]:
        """VULNERABLE: Search users by username - susceptible to SQL injection."""
        cursor = self.connection.cursor()
        
        # VULNERABLE CODE - DO NOT USE!
        query = f"SELECT * FROM users WHERE username LIKE '%{search_term}%'"
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return [User(id=row['id'], username=row['username'], 
                        email=row['email'], password_hash=row['password_hash']) 
                   for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def create_user_vulnerable(self, username: str, email: str, password: str) -> bool:
        """VULNERABLE: Create user - susceptible to SQL injection."""
        cursor = self.connection.cursor()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # VULNERABLE CODE - DO NOT USE!
        query = f"INSERT INTO users (username, email, password_hash) VALUES ('{username}', '{email}', '{password_hash}')"
        
        try:
            cursor.execute(query)
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

# Step 3: Create input validation utilities
# ===============================================================================

# Explanation:
# Before creating secure database methods, we need input validation utilities
# to sanitize and validate user input.

class InputValidator:
    """Utility class for input validation and sanitization."""
    
    @staticmethod
    def validate_username(username: str) -> bool:
        """Validate username format."""
        if not username or len(username) < 3 or len(username) > 50:
            return False
        # Allow only alphanumeric characters and underscores
        return re.match(r'^[a-zA-Z0-9_]+$', username) is not None
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        if not email or len(email) > 254:
            return False
        # Basic email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_password(password: str) -> bool:
        """Validate password strength."""
        if not password or len(password) < 8 or len(password) > 128:
            return False
        # Require at least one uppercase, lowercase, digit, and special character
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        return has_upper and has_lower and has_digit and has_special
    
    @staticmethod
    def sanitize_search_term(search_term: str) -> str:
        """Sanitize search term by removing potentially dangerous characters."""
        if not search_term:
            return ""
        # Remove SQL special characters
        sanitized = re.sub(r'[\'";\\%_]', '', search_term)
        return sanitized[:100]  # Limit length

# Step 4: Create secure database class with parameterized queries
# ===============================================================================

# Explanation:
# Now we'll create a secure database class that uses parameterized queries,
# input validation, and proper error handling to prevent SQL injection.

class SecureDatabase:
    """Secure database class with SQL injection prevention."""
    
    def __init__(self, db_path: str = ":memory:"):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._create_tables()
        self.validator = InputValidator()
    
    def _create_tables(self):
        """Create user table."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()
    
    def _hash_password(self, password: str, salt: str = None) -> tuple[str, str]:
        """Hash password with salt."""
        if salt is None:
            salt = secrets.token_hex(32)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), 
                                          salt.encode(), 100000)
        return password_hash.hex(), salt
    
    def create_user(self, username: str, email: str, password: str) -> bool:
        """SECURE: Create user with input validation and parameterized queries."""
        # Input validation
        if not self.validator.validate_username(username):
            raise ValueError("Invalid username format")
        if not self.validator.validate_email(email):
            raise ValueError("Invalid email format")
        if not self.validator.validate_password(password):
            raise ValueError("Password does not meet security requirements")
        
        cursor = self.connection.cursor()
        password_hash, salt = self._hash_password(password)
        
        try:
            # SECURE: Using parameterized query
            cursor.execute("""
                INSERT INTO users (username, email, password_hash, salt) 
                VALUES (?, ?, ?, ?)
            """, (username, email, password_hash, salt))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            raise ValueError("Username or email already exists")
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {e}")
    
    def get_user_by_credentials(self, username: str, password: str) -> Optional[User]:
        """SECURE: Authenticate user with parameterized queries."""
        # Input validation
        if not username or not password:
            return None
        if not self.validator.validate_username(username):
            return None
        
        cursor = self.connection.cursor()
        
        try:
            # SECURE: Using parameterized query
            cursor.execute("""
                SELECT id, username, email, password_hash, salt 
                FROM users WHERE username = ?
            """, (username,))
            
            row = cursor.fetchone()
            if not row:
                return None
            
            # Verify password
            stored_hash = row['password_hash']
            salt = row['salt']
            password_hash, _ = self._hash_password(password, salt)
            
            if password_hash == stored_hash:
                return User(id=row['id'], username=row['username'], 
                          email=row['email'], password_hash=stored_hash)
            return None
            
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {e}")
    
    def search_users(self, search_term: str) -> List[User]:
        """SECURE: Search users with input sanitization and parameterized queries."""
        # Input sanitization
        sanitized_term = self.validator.sanitize_search_term(search_term)
        if not sanitized_term:
            return []
        
        cursor = self.connection.cursor()
        
        try:
            # SECURE: Using parameterized query with LIKE
            search_pattern = f"%{sanitized_term}%"
            cursor.execute("""
                SELECT id, username, email, password_hash 
                FROM users WHERE username LIKE ?
            """, (search_pattern,))
            
            rows = cursor.fetchall()
            return [User(id=row['id'], username=row['username'], 
                        email=row['email'], password_hash=row['password_hash']) 
                   for row in rows]
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {e}")
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """SECURE: Get user by ID with parameterized query."""
        if not isinstance(user_id, int) or user_id <= 0:
            return None
        
        cursor = self.connection.cursor()
        
        try:
            # SECURE: Using parameterized query
            cursor.execute("""
                SELECT id, username, email, password_hash 
                FROM users WHERE id = ?
            """, (user_id,))
            
            row = cursor.fetchone()
            if row:
                return User(id=row['id'], username=row['username'], 
                          email=row['email'], password_hash=row['password_hash'])
            return None
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error: {e}")

# Step 5: Create ORM-based secure database class
# ===============================================================================

# Explanation:
# ORMs (Object-Relational Mappers) provide another layer of protection against
# SQL injection by abstracting SQL query construction.

try:
    from sqlalchemy import create_engine, Column, Integer, String, DateTime
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from datetime import datetime
    
    Base = declarative_base()
    
    class UserORM(Base):
        """SQLAlchemy ORM model for users."""
        __tablename__ = 'users_orm'
        
        id = Column(Integer, primary_key=True)
        username = Column(String(50), unique=True, nullable=False)
        email = Column(String(254), unique=True, nullable=False)
        password_hash = Column(String(128), nullable=False)
        salt = Column(String(64), nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow)
    
    class ORMDatabase:
        """ORM-based secure database class."""
        
        def __init__(self, db_url: str = "sqlite:///:memory:"):
            self.engine = create_engine(db_url)
            Base.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            self.validator = InputValidator()
        
        def _hash_password(self, password: str, salt: str = None) -> tuple[str, str]:
            """Hash password with salt."""
            if salt is None:
                salt = secrets.token_hex(32)
            password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), 
                                              salt.encode(), 100000)
            return password_hash.hex(), salt
        
        def create_user(self, username: str, email: str, password: str) -> bool:
            """SECURE: Create user using ORM."""
            # Input validation
            if not self.validator.validate_username(username):
                raise ValueError("Invalid username format")
            if not self.validator.validate_email(email):
                raise ValueError("Invalid email format")
            if not self.validator.validate_password(password):
                raise ValueError("Password does not meet security requirements")
            
            password_hash, salt = self._hash_password(password)
            
            try:
                # ORM automatically handles parameterization
                user = UserORM(username=username, email=email, 
                             password_hash=password_hash, salt=salt)
                self.session.add(user)
                self.session.commit()
                return True
            except Exception as e:
                self.session.rollback()
                if "UNIQUE constraint failed" in str(e):
                    raise ValueError("Username or email already exists")
                raise RuntimeError(f"Database error: {e}")
        
        def get_user_by_credentials(self, username: str, password: str) -> Optional[User]:
            """SECURE: Authenticate user using ORM."""
            if not username or not password:
                return None
            if not self.validator.validate_username(username):
                return None
            
            try:
                # ORM automatically handles parameterization
                user_orm = self.session.query(UserORM).filter(
                    UserORM.username == username
                ).first()
                
                if not user_orm:
                    return None
                
                # Verify password
                password_hash, _ = self._hash_password(password, user_orm.salt)
                
                if password_hash == user_orm.password_hash:
                    return User(id=user_orm.id, username=user_orm.username, 
                              email=user_orm.email, password_hash=user_orm.password_hash)
                return None
                
            except Exception as e:
                raise RuntimeError(f"Database error: {e}")

except ImportError:
    # SQLAlchemy not available
    class ORMDatabase:
        def __init__(self, *args, **kwargs):
            raise ImportError("SQLAlchemy is required for ORM functionality")

# Step 6: Demonstration and testing
# ===============================================================================

# Explanation:
# Let's demonstrate the differences between vulnerable and secure implementations
# and show how SQL injection attacks work and how to prevent them.

def demonstrate_sql_injection_attack():
    """Demonstrate SQL injection attack on vulnerable database."""
    print("=== SQL Injection Attack Demonstration ===")
    
    # Create vulnerable database and add test user
    vuln_db = VulnerableDatabase()
    vuln_db.create_user_vulnerable("admin", "admin@example.com", "password123")
    vuln_db.create_user_vulnerable("user1", "user1@example.com", "userpass")
    
    print("\n1. Normal login attempt:")
    user = vuln_db.get_user_by_credentials_vulnerable("admin", "password123")
    print(f"Login result: {user.username if user else 'Failed'}")
    
    print("\n2. SQL Injection attack (bypassing authentication):")
    # This malicious input bypasses authentication
    malicious_username = "admin' OR '1'='1' --"
    malicious_password = "anything"
    
    user = vuln_db.get_user_by_credentials_vulnerable(malicious_username, malicious_password)
    print(f"Attack result: {user.username if user else 'Failed'}")
    print("⚠️  ATTACK SUCCESSFUL! Authentication bypassed!")
    
    print("\n3. SQL Injection attack (data extraction):")
    # This attack attempts to extract all usernames
    malicious_search = "' UNION SELECT username, email, password_hash, id FROM users --"
    
    try:
        users = vuln_db.search_users_vulnerable(malicious_search)
        print(f"Extracted {len(users)} users through injection")
        for user in users:
            print(f"  - {user.username}: {user.email}")
    except Exception as e:
        print(f"Attack failed: {e}")

def demonstrate_secure_implementation():
    """Demonstrate secure database implementation."""
    print("\n=== Secure Implementation Demonstration ===")
    
    # Create secure database
    secure_db = SecureDatabase()
    
    print("\n1. Creating users with validation:")
    try:
        secure_db.create_user("john_doe", "john@example.com", "SecurePass123!")
        print("✅ User created successfully")
    except ValueError as e:
        print(f"❌ Validation error: {e}")
    
    try:
        secure_db.create_user("invalid user", "invalid-email", "weak")
        print("✅ User created successfully")
    except ValueError as e:
        print(f"❌ Validation error: {e}")
    
    print("\n2. Attempting SQL injection on secure database:")
    malicious_username = "admin' OR '1'='1' --"
    malicious_password = "anything"
    
    user = secure_db.get_user_by_credentials(malicious_username, malicious_password)
    print(f"Attack result: {user.username if user else 'Failed'}")
    print("✅ Attack prevented by input validation and parameterized queries!")
    
    print("\n3. Secure search functionality:")
    malicious_search = "' UNION SELECT username, email, password_hash, id FROM users --"
    
    try:
        users = secure_db.search_users(malicious_search)
        print(f"Search returned {len(users)} users")
        print("✅ Malicious SQL removed by input sanitization!")
    except Exception as e:
        print(f"Error: {e}")

# Step 7: Best practices and additional security measures
# ===============================================================================

# Explanation:
# Let's document best practices and additional security measures for preventing
# SQL injection and other database security issues.

class SecurityBestPractices:
    """Collection of security best practices for database operations."""
    
    @staticmethod
    def get_sql_injection_prevention_tips() -> List[str]:
        """Get list of SQL injection prevention tips."""
        return [
            "1. Always use parameterized queries or prepared statements",
            "2. Validate and sanitize all user input",
            "3. Use whitelist validation for expected input formats",
            "4. Implement proper error handling without exposing database details",
            "5. Use least privilege principle for database accounts",
            "6. Regularly update database software and dependencies",
            "7. Use stored procedures when appropriate",
            "8. Implement input length limits",
            "9. Use ORMs that handle parameterization automatically",
            "10. Never concatenate user input directly into SQL queries",
            "11. Use database-specific escaping functions as a last resort",
            "12. Implement logging and monitoring for suspicious activities"
        ]
    
    @staticmethod
    def get_password_security_tips() -> List[str]:
        """Get list of password security tips."""
        return [
            "1. Use strong hashing algorithms (bcrypt, scrypt, or Argon2)",
            "2. Always use salt for password hashing",
            "3. Use sufficient iteration counts for key derivation",
            "4. Implement password complexity requirements",
            "5. Use secure random number generators for salts",
            "6. Never store passwords in plain text",
            "7. Implement account lockout mechanisms",
            "8. Use multi-factor authentication when possible",
            "9. Regularly audit password policies",
            "10. Implement secure password reset mechanisms"
        ]
    
    @staticmethod
    def get_general_database_security_tips() -> List[str]:
        """Get list of general database security tips."""
        return [
            "1. Use connection pooling and connection limits",
            "2. Implement database firewalls and network security",
            "3. Encrypt sensitive data at rest and in transit",
            "4. Regular security audits and penetration testing",
            "5. Implement proper backup and recovery procedures",
            "6. Use database activity monitoring",
            "7. Implement role-based access control",
            "8. Regular security updates and patches",
            "9. Use secure configuration settings",
            "10. Implement data masking for non-production environments"
        ]

# Step 8: Complete example with error handling and logging
# ===============================================================================

# Explanation:
# A complete, production-ready example that includes proper error handling,
# logging, and security measures.

import logging
from contextlib import contextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProductionSecureDatabase:
    """Production-ready secure database class with comprehensive security measures."""
    
    def __init__(self, db_path: str = ":memory:"):
        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self._create_tables()
        self.validator = InputValidator()
        self._setup_security()
    
    def _setup_security(self):
        """Setup additional security measures."""
        # Enable foreign key constraints
        self.connection.execute("PRAGMA foreign_keys = ON")
        # Set secure temp store
        self.connection.execute("PRAGMA secure_delete = ON")
        self.connection.commit()
    
    def _create_tables(self):
        """Create user table with additional security fields."""
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                failed_login_attempts INTEGER DEFAULT 0,
                account_locked_until TIMESTAMP NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP NULL
            )
        """)
        
        # Create audit log table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action TEXT NOT NULL,
                details TEXT,
                ip_address TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        self.connection.commit()
    
    @contextmanager
    def _get_cursor(self):
        """Context manager for database operations."""
        cursor = self.connection.cursor()
        try:
            yield cursor
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise
        finally:
            cursor.close()
    
    def _log_security_event(self, action: str, details: str, user_id: int = None, ip_address: str = None):
        """Log security-related events."""
        logger.info(f"Security event: {action} - {details}")
        
        with self._get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO audit_log (user_id, action, details, ip_address)
                VALUES (?, ?, ?, ?)
            """, (user_id, action, details, ip_address))
    
    def create_user_secure(self, username: str, email: str, password: str, ip_address: str = None) -> bool:
        """Create user with comprehensive security measures."""
        try:
            # Input validation
            if not self.validator.validate_username(username):
                self._log_security_event("USER_CREATION_FAILED", f"Invalid username: {username}", ip_address=ip_address)
                raise ValueError("Invalid username format")
            
            if not self.validator.validate_email(email):
                self._log_security_event("USER_CREATION_FAILED", f"Invalid email: {email}", ip_address=ip_address)
                raise ValueError("Invalid email format")
            
            if not self.validator.validate_password(password):
                self._log_security_event("USER_CREATION_FAILED", f"Weak password for user: {username}", ip_address=ip_address)
                raise ValueError("Password does not meet security requirements")
            
            password_hash, salt = self._hash_password(password)
            
            with self._get_cursor() as cursor:
                cursor.execute("""
                    INSERT INTO users (username, email, password_hash, salt) 
                    VALUES (?, ?, ?, ?)
                """, (username, email, password_hash, salt))
            
            self._log_security_event("USER_CREATED", f"User created: {username}", ip_address=ip_address)
            return True
            
        except sqlite3.IntegrityError:
            self._log_security_event("USER_CREATION_FAILED", f"Duplicate user: {username}", ip_address=ip_address)
            raise ValueError("Username or email already exists")
        except sqlite3.Error as e:
            self._log_security_event("DATABASE_ERROR", f"Error creating user: {str(e)}", ip_address=ip_address)
            raise RuntimeError(f"Database error: {e}")
    
    def _hash_password(self, password: str, salt: str = None) -> tuple[str, str]:
        """Hash password with salt using secure method."""
        if salt is None:
            salt = secrets.token_hex(32)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), 
                                          salt.encode(), 100000)
        return password_hash.hex(), salt

def main():
    """Main function to demonstrate all concepts."""
    print("SQL Injection Prevention Demonstration")
    print("=" * 50)
    
    # Demonstrate vulnerable implementation
    demonstrate_sql_injection_attack()
    
    # Demonstrate secure implementation
    demonstrate_secure_implementation()
    
    # Show best practices
    print("\n=== Security Best Practices ===")
    practices = SecurityBestPractices()
    
    print("\nSQL Injection Prevention:")
    for tip in practices.get_sql_injection_prevention_tips()[:5]:
        print(f"  {tip}")
    
    print("\nPassword Security:")
    for tip in practices.get_password_security_tips()[:5]:
        print(f"  {tip}")
    
    print("\n✅ Remember: Security is a continuous process, not a one-time implementation!")

if __name__ == "__main__":
    main()

# ===============================================================================
#                                   SUMMARY
# ===============================================================================
#
# Key Concepts Covered:
# 1. SQL Injection vulnerabilities and attack vectors
# 2. Parameterized queries for prevention
# 3. Input validation and sanitization
# 4. Secure password hashing with salt
# 5. ORM-based approaches for additional security
# 6. Error handling and logging for security events
# 7. Best practices for database security
#
# Security Principles Applied:
# - Defense in depth (multiple layers of security)
# - Least privilege principle
# - Input validation and sanitization
# - Secure coding practices
# - Proper error handling
# - Audit logging
#
# Remember: Security is not just about preventing SQL injection - it's about
# implementing a comprehensive security strategy that includes proper
# authentication, authorization, encryption, and monitoring.
#
# ===============================================================================

