# Python Security Best Practices - Comprehensive Tutorial

## Table of Contents

1. [Introduction to Python Security](#introduction)
2. [Security Fundamentals](#fundamentals)
3. [Input Validation and Sanitization](#input-validation)
4. [SQL Injection Prevention](#sql-injection)
5. [Cross-Site Scripting (XSS) Prevention](#xss-prevention)
6. [Authentication and Authorization](#auth)
7. [Password Security and Hashing](#password-security)
8. [Cryptography Basics](#cryptography)
9. [Secure File Handling](#file-handling)
10. [Environment Variables and Configuration](#environment)
11. [Secure Communication](#communication)
12. [Code Injection Prevention](#code-injection)
13. [Dependency Security](#dependency-security)
14. [Logging Security](#logging-security)
15. [Security Testing](#security-testing)
16. [Advanced Security Patterns](#advanced-patterns)
17. [Security Checklist](#checklist)
18. [Resources and Further Reading](#resources)

---

## Introduction to Python Security {#introduction}

Security in Python applications is crucial for protecting sensitive data, preventing unauthorized access, and maintaining system integrity. This comprehensive tutorial covers security best practices from beginner to expert level.

### Why Security Matters

- **Data Protection**: Safeguard user information and business data
- **Compliance**: Meet regulatory requirements (GDPR, HIPAA, etc.)
- **Trust**: Maintain user confidence and business reputation
- **Cost Prevention**: Avoid expensive security breaches and downtime

### Security Mindset

Security should be:
- **Built-in from the start** (Security by Design)
- **Layered** (Defense in Depth)
- **Continuously monitored** and updated
- **Everyone's responsibility** in the development team

---

## Security Fundamentals {#fundamentals}

### Core Security Principles

#### 1. **Confidentiality**
Ensuring that information is accessible only to authorized individuals.

```python
# Example: Encrypting sensitive data
from cryptography.fernet import Fernet

def encrypt_sensitive_data(data: str) -> bytes:
    """Encrypt sensitive information before storage."""
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data, key
```

#### 2. **Integrity**
Maintaining the accuracy and completeness of data.

```python
import hashlib

def verify_data_integrity(data: str, expected_hash: str) -> bool:
    """Verify data hasn't been tampered with."""
    actual_hash = hashlib.sha256(data.encode()).hexdigest()
    return actual_hash == expected_hash
```

#### 3. **Availability**
Ensuring that information and resources are accessible when needed.

```python
import time
from functools import wraps

def rate_limit(max_calls: int, time_window: int):
    """Rate limiting decorator to prevent DoS attacks."""
    calls = []
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove old calls outside time window
            calls[:] = [call_time for call_time in calls if now - call_time < time_window]
            
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded")
            
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Common Security Vulnerabilities

#### OWASP Top 10 for Python Applications:

1. **Injection** (SQL, NoSQL, OS, LDAP)
2. **Broken Authentication**
3. **Sensitive Data Exposure**
4. **XML External Entities (XXE)**
5. **Broken Access Control**
6. **Security Misconfiguration**
7. **Cross-Site Scripting (XSS)**
8. **Insecure Deserialization**
9. **Using Components with Known Vulnerabilities**
10. **Insufficient Logging & Monitoring**

---

## Input Validation and Sanitization {#input-validation}

Input validation is the first line of defense against many security vulnerabilities. Never trust user input!

### 🔰 Beginner Level: Basic Input Validation

#### String Validation

```python
import re
from typing import Optional

def validate_email(email: str) -> bool:
    """Basic email validation using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone_number(phone: str) -> bool:
    """Validate phone number format."""
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    # Check if it's 10 digits (US format)
    return len(digits_only) == 10

def sanitize_string(input_str: str, max_length: int = 255) -> str:
    """Basic string sanitization."""
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")
    
    # Remove leading/trailing whitespace
    sanitized = input_str.strip()
    
    # Limit length
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    # Remove potentially dangerous characters
    dangerous_chars = ['<', '>', '"', "'", '&', '\x00']
    for char in dangerous_chars:
        sanitized = sanitized.replace(char, '')
    
    return sanitized
```

#### Numeric Validation

```python
def validate_integer_range(value: str, min_val: int, max_val: int) -> Optional[int]:
    """Validate and convert string to integer within range."""
    try:
        num = int(value)
        if min_val <= num <= max_val:
            return num
        else:
            raise ValueError(f"Value must be between {min_val} and {max_val}")
    except ValueError:
        return None

def validate_positive_float(value: str) -> Optional[float]:
    """Validate and convert string to positive float."""
    try:
        num = float(value)
        return num if num > 0 else None
    except ValueError:
        return None
```

### 🔶 Intermediate Level: Advanced Validation

#### Using Pydantic for Data Validation

```python
from pydantic import BaseModel, validator, EmailStr
from typing import Optional
import re

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    age: int
    password: str
    confirm_password: str
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', v):
            raise ValueError('Username must be 3-20 characters, alphanumeric and underscore only')
        return v
    
    @validator('age')
    def validate_age(cls, v):
        if not 13 <= v <= 120:
            raise ValueError('Age must be between 13 and 120')
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v
    
    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v

# Usage example
try:
    user_data = UserRegistration(
        username="john_doe",
        email="john@example.com",
        age=25,
        password="SecurePass123!",
        confirm_password="SecurePass123!"
    )
    print("Validation successful!")
except ValueError as e:
    print(f"Validation error: {e}")
```

---

## SQL Injection Prevention {#sql-injection}

SQL injection is one of the most dangerous web application vulnerabilities. It occurs when user input is directly concatenated into SQL queries.

### 🔰 Beginner Level: Understanding SQL Injection

#### What is SQL Injection?

```python
# ❌ VULNERABLE CODE - Never do this!
def get_user_by_id_vulnerable(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # If user_id = "1; DROP TABLE users; --"
    # Query becomes: SELECT * FROM users WHERE id = 1; DROP TABLE users; --
    return execute_query(query)

# ❌ VULNERABLE CODE - String concatenation
def login_vulnerable(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    # If username = "admin' --"
    # Query becomes: SELECT * FROM users WHERE username = 'admin' -- AND password = '...'
    return execute_query(query)
```

#### ✅ Safe Approach: Parameterized Queries

```python
import sqlite3
from typing import Optional, Dict, Any

class SafeDatabase:
    def __init__(self, db_path: str):
        self.db_path = db_path
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Safe way to get user by ID using parameterized query."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Use ? placeholder for SQLite, %s for MySQL/PostgreSQL
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            result = cursor.fetchone()
            
            if result:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, result))
            return None
    
    def authenticate_user(self, username: str, password_hash: str) -> Optional[Dict[str, Any]]:
        """Safe user authentication."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, username, email FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            )
            result = cursor.fetchone()
            
            if result:
                columns = [description[0] for description in cursor.description]
                return dict(zip(columns, result))
            return None
    
    def create_user(self, username: str, email: str, password_hash: str) -> int:
        """Safely create a new user."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                (username, email, password_hash)
            )
            conn.commit()
            return cursor.lastrowid
```

### 🔶 Intermediate Level: ORM and Advanced Protection

#### Using SQLAlchemy ORM

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)

class UserRepository:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username using ORM (automatically safe from SQL injection)."""
        session = self.SessionLocal()
        try:
            # ORM automatically handles parameterization
            user = session.query(User).filter(User.username == username).first()
            return user
        except SQLAlchemyError as e:
            self.logger.error(f"Database error: {e}")
            return None
        finally:
            session.close()
    
    def search_users(self, search_term: str) -> List[User]:
        """Safe text search using ORM."""
        session = self.SessionLocal()
        try:
            # Use ORM methods for safe searching
            users = session.query(User).filter(
                User.username.contains(search_term) |
                User.email.contains(search_term)
            ).limit(50).all()
            return users
        except SQLAlchemyError as e:
            self.logger.error(f"Database error: {e}")
            return []
        finally:
            session.close()
    
    def execute_safe_raw_query(self, query: str, params: Dict[str, Any]) -> List[Dict]:
        """When you must use raw SQL, do it safely."""
        session = self.SessionLocal()
        try:
            # Use text() with bound parameters for raw SQL
            result = session.execute(text(query), params)
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result.fetchall()]
        except SQLAlchemyError as e:
            self.logger.error(f"Database error: {e}")
            return []
        finally:
            session.close()

# Usage example
repo = UserRepository("sqlite:///example.db")

# Safe search
users = repo.search_users("john")

# Safe raw query when needed
complex_query = """
    SELECT u.username, COUNT(p.id) as post_count 
    FROM users u 
    LEFT JOIN posts p ON u.id = p.user_id 
    WHERE u.created_at > :start_date 
    GROUP BY u.id, u.username
"""
results = repo.execute_safe_raw_query(complex_query, {"start_date": "2025-01-01"})
```

#### Input Sanitization for Dynamic Queries

```python
import re
from typing import List, Dict, Any

class QueryBuilder:
    """Safe dynamic query builder with whitelist approach."""
    
    ALLOWED_COLUMNS = {
        'users': ['id', 'username', 'email', 'created_at'],
        'posts': ['id', 'title', 'content', 'user_id', 'created_at']
    }
    
    ALLOWED_OPERATORS = ['=', '!=', '>', '<', '>=', '<=', 'LIKE', 'IN']
    ALLOWED_ORDER_DIRECTIONS = ['ASC', 'DESC']
    
    @staticmethod
    def validate_column_name(table: str, column: str) -> bool:
        """Validate column name against whitelist."""
        return column in QueryBuilder.ALLOWED_COLUMNS.get(table, [])
    
    @staticmethod
    def validate_operator(operator: str) -> bool:
        """Validate SQL operator against whitelist."""
        return operator.upper() in QueryBuilder.ALLOWED_OPERATORS
    
    @staticmethod
    def build_safe_where_clause(table: str, conditions: List[Dict[str, Any]]) -> tuple:
        """Build WHERE clause safely with parameterized values."""
        where_parts = []
        params = {}
        param_counter = 0
        
        for condition in conditions:
            column = condition.get('column')
            operator = condition.get('operator', '=')
            value = condition.get('value')
            
            # Validate column and operator
            if not QueryBuilder.validate_column_name(table, column):
                raise ValueError(f"Invalid column: {column}")
            
            if not QueryBuilder.validate_operator(operator):
                raise ValueError(f"Invalid operator: {operator}")
            
            # Create parameterized condition
            param_name = f"param_{param_counter}"
            where_parts.append(f"{column} {operator.upper()} :{param_name}")
            params[param_name] = value
            param_counter += 1
        
        where_clause = " AND ".join(where_parts) if where_parts else "1=1"
        return where_clause, params
    
    @staticmethod
    def build_safe_order_clause(table: str, order_by: List[Dict[str, str]]) -> str:
        """Build ORDER BY clause safely."""
        order_parts = []
        
        for order_item in order_by:
            column = order_item.get('column')
            direction = order_item.get('direction', 'ASC').upper()
            
            # Validate column and direction
            if not QueryBuilder.validate_column_name(table, column):
                raise ValueError(f"Invalid column: {column}")
            
            if direction not in QueryBuilder.ALLOWED_ORDER_DIRECTIONS:
                raise ValueError(f"Invalid order direction: {direction}")
            
            order_parts.append(f"{column} {direction}")
        
        return "ORDER BY " + ", ".join(order_parts) if order_parts else ""

# Usage example
def search_users_advanced(conditions: List[Dict], order_by: List[Dict] = None, limit: int = 50):
    """Advanced user search with dynamic conditions."""
    try:
        where_clause, params = QueryBuilder.build_safe_where_clause('users', conditions)
        order_clause = QueryBuilder.build_safe_order_clause('users', order_by or [])
        
        # Validate limit
        if not isinstance(limit, int) or limit <= 0 or limit > 1000:
            limit = 50
        
        query = f"""
            SELECT id, username, email, created_at 
            FROM users 
            WHERE {where_clause} 
            {order_clause}
            LIMIT :limit
        """
        
        params['limit'] = limit
        
        # Execute with your preferred database method
        return execute_safe_query(query, params)
        
    except ValueError as e:
        logging.error(f"Invalid query parameters: {e}")
        return []

# Example usage
search_conditions = [
    {'column': 'username', 'operator': 'LIKE', 'value': '%john%'},
    {'column': 'created_at', 'operator': '>', 'value': '2025-01-01'}
]

order_conditions = [
    {'column': 'created_at', 'direction': 'DESC'},
    {'column': 'username', 'direction': 'ASC'}
]

results = search_users_advanced(search_conditions, order_conditions, 25)
```

### 🔴 Expert Level: Advanced SQL Injection Defense

#### Stored Procedures and Functions

```python
import psycopg2
from psycopg2 import sql
from contextlib import contextmanager

class PostgreSQLSecureDB:
    """Advanced PostgreSQL security implementation."""
    
    def __init__(self, connection_params: Dict[str, str]):
        self.connection_params = connection_params
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_params)
            yield conn
        except psycopg2.Error as e:
            if conn:
                conn.rollback()
            raise
        finally:
            if conn:
                conn.close()
    
    def call_stored_procedure(self, procedure_name: str, params: tuple) -> List[Dict]:
        """Safely call stored procedures."""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                # Use sql.Identifier for procedure names to prevent injection
                query = sql.SQL("CALL {}({})").format(
                    sql.Identifier(procedure_name),
                    sql.SQL(',').join(sql.Placeholder() * len(params))
                )
                
                cursor.execute(query, params)
                
                if cursor.description:
                    columns = [desc[0] for desc in cursor.description]
                    return [dict(zip(columns, row)) for row in cursor.fetchall()]
                return []
    
    def execute_function(self, function_name: str, params: tuple) -> Any:
        """Safely execute database functions."""
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                query = sql.SQL("SELECT {}({})").format(
                    sql.Identifier(function_name),
                    sql.SQL(',').join(sql.Placeholder() * len(params))
                )
                
                cursor.execute(query, params)
                result = cursor.fetchone()
                return result[0] if result else None
```

---

## Password Security and Hashing {#password-security}

Proper password handling is critical for application security. Never store passwords in plain text!

### 🔰 Beginner Level: Basic Password Hashing

#### Why Hash Passwords?

```python
# ❌ NEVER DO THIS - Storing plain text passwords
def store_password_bad(username: str, password: str):
    # This is extremely dangerous!
    query = "INSERT INTO users (username, password) VALUES (?, ?)"
    execute_query(query, (username, password))

# ✅ CORRECT - Hash passwords before storing
import hashlib
import secrets

def hash_password_basic(password: str) -> str:
    """Basic password hashing (not recommended for production)."""
    # Add salt to prevent rainbow table attacks
    salt = secrets.token_hex(16)
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{password_hash}"

def verify_password_basic(password: str, stored_hash: str) -> bool:
    """Verify password against basic hash."""
    try:
        salt, hash_value = stored_hash.split(':')
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash == hash_value
    except ValueError:
        return False
```

#### ✅ Better Approach: Using bcrypt

```python
import bcrypt
from typing import Optional

class PasswordManager:
    """Secure password management using bcrypt."""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using bcrypt."""
        # Generate salt and hash password
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return password_hash.decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """Verify a password against its hash."""
        try:
            return bcrypt.checkpw(
                password.encode('utf-8'), 
                hashed_password.encode('utf-8')
            )
        except Exception:
            return False
    
    @staticmethod
    def is_password_strong(password: str) -> tuple[bool, list[str]]:
        """Check if password meets security requirements."""
        errors = []
        
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")
        
        if not any(c.isupper() for c in password):
            errors.append("Password must contain at least one uppercase letter")
        
        if not any(c.islower() for c in password):
            errors.append("Password must contain at least one lowercase letter")
        
        if not any(c.isdigit() for c in password):
            errors.append("Password must contain at least one digit")
        
        if not any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
            errors.append("Password must contain at least one special character")
        
        return len(errors) == 0, errors

# Usage example
password_manager = PasswordManager()

# Register new user
def register_user(username: str, password: str) -> bool:
    # Check password strength
    is_strong, errors = password_manager.is_password_strong(password)
    if not is_strong:
        print("Password errors:", errors)
        return False
    
    # Hash password
    hashed_password = password_manager.hash_password(password)
    
    # Store in database
    store_user(username, hashed_password)
    return True

# Login user
def login_user(username: str, password: str) -> bool:
    stored_hash = get_user_password_hash(username)
    if stored_hash:
        return password_manager.verify_password(password, stored_hash)
    return False
```

### 🔶 Intermediate Level: Advanced Password Security

#### Password Policy Enforcement

```python
import re
import zxcvbn
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class AdvancedPasswordPolicy:
    """Advanced password policy with comprehensive checks."""
    
    def __init__(self):
        self.min_length = 12
        self.max_length = 128
        self.require_uppercase = True
        self.require_lowercase = True
        self.require_digits = True
        self.require_special = True
        self.min_unique_chars = 8
        self.max_repeated_chars = 2
        self.password_history_count = 5
        self.password_expiry_days = 90
        
        # Common weak passwords
        self.weak_passwords = {
            'password', 'password123', '123456', 'qwerty', 'admin',
            'letmein', 'welcome', 'monkey', '1234567890'
        }
        
        # Common patterns to avoid
        self.forbidden_patterns = [
            r'(.)\1{3,}',  # 4 or more repeated characters
            r'(012|123|234|345|456|567|678|789|890)',  # Sequential numbers
            r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',  # Sequential letters
        ]
    
    def validate_password(self, password: str, username: str = None, 
                         user_info: Dict[str, str] = None) -> tuple[bool, List[str]]:
        """Comprehensive password validation."""
        errors = []
        
        # Basic length check
        if len(password) < self.min_length:
            errors.append(f"Password must be at least {self.min_length} characters long")
        
        if len(password) > self.max_length:
            errors.append(f"Password must not exceed {self.max_length} characters")
        
        # Character requirements
        if self.require_uppercase and not any(c.isupper() for c in password):
            errors.append("Password must contain at least one uppercase letter")
        
        if self.require_lowercase and not any(c.islower() for c in password):
            errors.append("Password must contain at least one lowercase letter")
        
        if self.require_digits and not any(c.isdigit() for c in password):
            errors.append("Password must contain at least one digit")
        
        if self.require_special and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("Password must contain at least one special character")
        
        # Unique characters check
        unique_chars = len(set(password.lower()))
        if unique_chars < self.min_unique_chars:
            errors.append(f"Password must contain at least {self.min_unique_chars} unique characters")
        
        # Check for forbidden patterns
        for pattern in self.forbidden_patterns:
            if re.search(pattern, password.lower()):
                errors.append("Password contains forbidden patterns (repeated or sequential characters)")
                break
        
        # Check against weak passwords
        if password.lower() in self.weak_passwords:
            errors.append("Password is too common and easily guessable")
        
        # Check if password contains username
        if username and username.lower() in password.lower():
            errors.append("Password must not contain the username")
        
        # Check if password contains personal information
        if user_info:
            for key, value in user_info.items():
                if value and len(value) > 2 and value.lower() in password.lower():
                    errors.append(f"Password must not contain personal information ({key})")
        
        # Use zxcvbn for advanced password strength analysis
        try:
            result = zxcvbn.zxcvbn(password, user_inputs=[username] if username else [])
            if result['score'] < 3:  # Score 0-4, we want at least 3
                errors.append(f"Password is too weak. {result['feedback']['warning']}")
                if result['feedback']['suggestions']:
                    errors.extend(result['feedback']['suggestions'])
        except ImportError:
            # zxcvbn not available, skip advanced analysis
            pass
        
        return len(errors) == 0, errors
    
    def check_password_history(self, user_id: int, new_password: str) -> bool:
        """Check if password was used recently."""
        # This would typically query your database
        recent_passwords = get_user_password_history(user_id, self.password_history_count)
        
        for old_hash in recent_passwords:
            if bcrypt.checkpw(new_password.encode('utf-8'), old_hash.encode('utf-8')):
                return False
        
        return True
    
    def is_password_expired(self, last_changed: datetime) -> bool:
        """Check if password has expired."""
        expiry_date = last_changed + timedelta(days=self.password_expiry_days)
        return datetime.now() > expiry_date

# Usage example
policy = AdvancedPasswordPolicy()

def change_password(user_id: int, username: str, old_password: str, 
                   new_password: str, user_info: Dict[str, str] = None) -> tuple[bool, List[str]]:
    """Secure password change process."""
    
    # Verify old password
    if not verify_current_password(user_id, old_password):
        return False, ["Current password is incorrect"]
    
    # Validate new password
    is_valid, errors = policy.validate_password(new_password, username, user_info)
    if not is_valid:
        return False, errors
    
    # Check password history
    if not policy.check_password_history(user_id, new_password):
        return False, ["Password was used recently. Please choose a different password."]
    
    # Hash and store new password
    new_hash = PasswordManager.hash_password(new_password)
    
    # Update database
    update_user_password(user_id, new_hash)
    add_to_password_history(user_id, new_hash)
    
    return True, ["Password changed successfully"]
```

#### Multi-Factor Authentication (MFA)

```python
import pyotp
import qrcode
from io import BytesIO
import base64

class MFAManager:
    """Multi-Factor Authentication management."""
    
    @staticmethod
    def generate_secret() -> str:
        """Generate a new TOTP secret."""
        return pyotp.random_base32()
    
    @staticmethod
    def generate_qr_code(username: str, secret: str, issuer: str = "MyApp") -> str:
        """Generate QR code for TOTP setup."""
        totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
            name=username,
            issuer_name=issuer
        )
        
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(totp_uri)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to base64 for web display
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return f"data:image/png;base64,{img_str}"
    
    @staticmethod
    def verify_totp(secret: str, token: str) -> bool:
        """Verify TOTP token."""
        totp = pyotp.TOTP(secret)
        return totp.verify(token, valid_window=1)  # Allow 1 time step tolerance
    
    @staticmethod
    def generate_backup_codes(count: int = 10) -> List[str]:
        """Generate backup codes for account recovery."""
        return [secrets.token_hex(4).upper() for _ in range(count)]

class SecureAuthenticationSystem:
    """Complete secure authentication system."""
    
    def __init__(self):
        self.password_manager = PasswordManager()
        self.mfa_manager = MFAManager()
        self.max_login_attempts = 5
        self.lockout_duration = timedelta(minutes=15)
    
    def register_user(self, username: str, password: str, email: str) -> Dict[str, Any]:
        """Register new user with MFA setup."""
        
        # Validate password
        is_strong, errors = PasswordManager.is_password_strong(password)
        if not is_strong:
            return {"success": False, "errors": errors}
        
        # Hash password
        password_hash = self.password_manager.hash_password(password)
        
        # Generate MFA secret
        mfa_secret = self.mfa_manager.generate_secret()
        backup_codes = self.mfa_manager.generate_backup_codes()
        
        # Generate QR code
        qr_code = self.mfa_manager.generate_qr_code(username, mfa_secret)
        
        # Store user (implement your database logic)
        user_id = create_user(username, email, password_hash, mfa_secret, backup_codes)
        
        return {
            "success": True,
            "user_id": user_id,
            "qr_code": qr_code,
            "backup_codes": backup_codes,
            "message": "Please scan the QR code with your authenticator app"
        }
    
    def authenticate_user(self, username: str, password: str, totp_token: str = None) -> Dict[str, Any]:
        """Authenticate user with password and optional MFA."""
        
        # Check if account is locked
        if self.is_account_locked(username):
            return {"success": False, "error": "Account is temporarily locked"}
        
        # Verify password
        user = get_user_by_username(username)
        if not user or not self.password_manager.verify_password(password, user['password_hash']):
            self.record_failed_attempt(username)
            return {"success": False, "error": "Invalid credentials"}
        
        # Check if MFA is required
        if user['mfa_enabled']:
            if not totp_token:
                return {"success": False, "error": "MFA token required", "mfa_required": True}
            
            if not self.mfa_manager.verify_totp(user['mfa_secret'], totp_token):
                self.record_failed_attempt(username)
                return {"success": False, "error": "Invalid MFA token"}
        
        # Clear failed attempts on successful login
        self.clear_failed_attempts(username)
        
        return {
            "success": True,
            "user_id": user['id'],
            "username": user['username']
        }
```

### 🔴 Expert Level: Enterprise Password Security

#### Password-less Authentication

```python
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import jwt
from datetime import datetime, timedelta

class WebAuthnManager:
    """WebAuthn (FIDO2) implementation for passwordless authentication."""
    
    def __init__(self):
        self.rp_id = "example.com"
        self.rp_name = "Example Corp"
    
    def generate_challenge(self) -> str:
        """Generate cryptographic challenge for authentication."""
        return secrets.token_urlsafe(32)
    
    def create_credential_options(self, username: str, user_id: str) -> Dict[str, Any]:
        """Create credential creation options for registration."""
        challenge = self.generate_challenge()
        
        return {
            "challenge": challenge,
            "rp": {"id": self.rp_id, "name": self.rp_name},
            "user": {
                "id": user_id,
                "name": username,
                "displayName": username
            },
            "pubKeyCredParams": [
                {"alg": -7, "type": "public-key"},  # ES256
                {"alg": -257, "type": "public-key"}  # RS256
            ],
            "authenticatorSelection": {
                "authenticatorAttachment": "platform",
                "userVerification": "required"
            },
            "timeout": 60000,
            "attestation": "direct"
        }
    
    def verify_registration(self, credential_data: Dict[str, Any]) -> bool:
        """Verify WebAuthn registration response."""
        # This is a simplified version - real implementation would be more complex
        try:
            # Verify challenge, origin, and credential data
            # Store public key for future authentication
            return True
        except Exception:
            return False

class AdvancedPasswordSecurity:
    """Enterprise-grade password security system."""
    
    def __init__(self):
        self.breach_checker = PasswordBreachChecker()
        self.entropy_calculator = PasswordEntropyCalculator()
    
    def check_password_breach(self, password: str) -> bool:
        """Check if password appears in known breaches using k-anonymity."""
        # Use HaveIBeenPwned API with k-anonymity
        password_hash = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = password_hash[:5]
        suffix = password_hash[5:]
        
        try:
            response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
            if response.status_code == 200:
                hashes = response.text.split('\n')
                for hash_line in hashes:
                    hash_suffix, count = hash_line.split(':')
                    if hash_suffix == suffix:
                        return True, int(count)
            return False, 0
        except Exception:
            # If service is unavailable, don't block password change
            return False, 0
    
    def calculate_password_entropy(self, password: str) -> float:
        """Calculate password entropy in bits."""
        charset_size = 0
        
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
            charset_size += 32
        
        import math
        entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
        return entropy
    
    def generate_secure_password(self, length: int = 16, 
                                include_symbols: bool = True) -> str:
        """Generate cryptographically secure password."""
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        symbols = "!@#$%^&*(),.?\":{}|<>" if include_symbols else ""
        
        charset = lowercase + uppercase + digits + symbols
        
        # Ensure at least one character from each required set
        password = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits)
        ]
        
        if include_symbols:
            password.append(secrets.choice(symbols))
        
        # Fill remaining length
        for _ in range(length - len(password)):
            password.append(secrets.choice(charset))
        
        # Shuffle the password
        secrets.SystemRandom().shuffle(password)
        
        return ''.join(password)
```

---

## Cryptography Basics {#cryptography}

Understanding cryptography is essential for securing data in transit and at rest.

### 🔰 Beginner Level: Basic Encryption and Hashing

#### Symmetric Encryption with Fernet

```python
from cryptography.fernet import Fernet
import base64
import os

class SimpleEncryption:
    """Simple symmetric encryption using Fernet."""
    
    @staticmethod
    def generate_key() -> bytes:
        """Generate a new encryption key."""
        return Fernet.generate_key()
    
    @staticmethod
    def encrypt_data(data: str, key: bytes) -> str:
        """Encrypt string data."""
        f = Fernet(key)
        encrypted_data = f.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted_data).decode()
    
    @staticmethod
    def decrypt_data(encrypted_data: str, key: bytes) -> str:
        """Decrypt string data."""
        f = Fernet(key)
        encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
        decrypted_data = f.decrypt(encrypted_bytes)
        return decrypted_data.decode()

# Usage example
encryption = SimpleEncryption()

# Generate key (store this securely!)
key = encryption.generate_key()
print(f"Key: {key.decode()}")

# Encrypt sensitive data
sensitive_data = "This is confidential information"
encrypted = encryption.encrypt_data(sensitive_data, key)
print(f"Encrypted: {encrypted}")

# Decrypt data
decrypted = encryption.decrypt_data(encrypted, key)
print(f"Decrypted: {decrypted}")
```

#### Secure Hashing

```python
import hashlib
import hmac
import secrets

class SecureHashing:
    """Secure hashing utilities."""
    
    @staticmethod
    def hash_data(data: str, algorithm: str = 'sha256') -> str:
        """Hash data using specified algorithm."""
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(data.encode())
        return hash_obj.hexdigest()
    
    @staticmethod
    def hash_with_salt(data: str, salt: bytes = None) -> tuple[str, bytes]:
        """Hash data with salt for password storage."""
        if salt is None:
            salt = secrets.token_bytes(32)
        
        hash_obj = hashlib.pbkdf2_hmac('sha256', data.encode(), salt, 100000)
        return hash_obj.hex(), salt
    
    @staticmethod
    def verify_hash(data: str, stored_hash: str, salt: bytes) -> bool:
        """Verify data against stored hash."""
        hash_obj = hashlib.pbkdf2_hmac('sha256', data.encode(), salt, 100000)
        return hash_obj.hex() == stored_hash
    
    @staticmethod
    def create_hmac(data: str, secret_key: bytes) -> str:
        """Create HMAC for data integrity."""
        return hmac.new(secret_key, data.encode(), hashlib.sha256).hexdigest()
    
    @staticmethod
    def verify_hmac(data: str, signature: str, secret_key: bytes) -> bool:
        """Verify HMAC signature."""
        expected_signature = hmac.new(secret_key, data.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(signature, expected_signature)

# Usage examples
hasher = SecureHashing()

# Simple hashing
data = "Hello, World!"
hash_value = hasher.hash_data(data)
print(f"SHA256 hash: {hash_value}")

# Password hashing with salt
password = "my_secure_password"
password_hash, salt = hasher.hash_with_salt(password)
print(f"Password hash: {password_hash}")
print(f"Salt: {salt.hex()}")

# Verify password
is_valid = hasher.verify_hash(password, password_hash, salt)
print(f"Password valid: {is_valid}")

# HMAC for data integrity
secret_key = secrets.token_bytes(32)
message = "Important message"
signature = hasher.create_hmac(message, secret_key)
print(f"HMAC signature: {signature}")

# Verify HMAC
is_authentic = hasher.verify_hmac(message, signature, secret_key)
print(f"Message authentic: {is_authentic}")
```

### 🔶 Intermediate Level: Advanced Cryptography

#### Asymmetric Encryption (RSA)

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import base64

class RSAEncryption:
    """RSA asymmetric encryption implementation."""
    
    def __init__(self, key_size: int = 2048):
        self.key_size = key_size
        self.private_key = None
        self.public_key = None
    
    def generate_key_pair(self) -> tuple[bytes, bytes]:
        """Generate RSA key pair."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        
        # Serialize keys
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return private_pem, public_pem
    
    def load_private_key(self, private_key_pem: bytes, password: bytes = None):
        """Load private key from PEM format."""
        self.private_key = serialization.load_pem_private_key(
            private_key_pem, password=password, backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
    
    def load_public_key(self, public_key_pem: bytes):
        """Load public key from PEM format."""
        self.public_key = serialization.load_pem_public_key(
            public_key_pem, backend=default_backend()
        )
    
    def encrypt(self, data: str) -> str:
        """Encrypt data with public key."""
        if not self.public_key:
            raise ValueError("Public key not loaded")
        
        encrypted = self.public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(encrypted).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """Decrypt data with private key."""
        if not self.private_key:
            raise ValueError("Private key not loaded")
        
        encrypted_bytes = base64.b64decode(encrypted_data.encode())
        decrypted = self.private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()
    
    def sign(self, data: str) -> str:
        """Sign data with private key."""
        if not self.private_key:
            raise ValueError("Private key not loaded")
        
        signature = self.private_key.sign(
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode()
    
    def verify_signature(self, data: str, signature: str) -> bool:
        """Verify signature with public key."""
        if not self.public_key:
            raise ValueError("Public key not loaded")
        
        try:
            signature_bytes = base64.b64decode(signature.encode())
            self.public_key.verify(
                signature_bytes,
                data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

# Usage example
rsa_crypto = RSAEncryption()

# Generate key pair
private_key, public_key = rsa_crypto.generate_key_pair()
print("Keys generated successfully")

# Encrypt and decrypt
message = "This is a secret message"
encrypted = rsa_crypto.encrypt(message)
print(f"Encrypted: {encrypted[:50]}...")

decrypted = rsa_crypto.decrypt(encrypted)
print(f"Decrypted: {decrypted}")

# Sign and verify
signature = rsa_crypto.sign(message)
print(f"Signature: {signature[:50]}...")

is_valid = rsa_crypto.verify_signature(message, signature)
print(f"Signature valid: {is_valid}")
```

#### Elliptic Curve Cryptography (ECC)

```python
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

class ECCCryptography:
    """Elliptic Curve Cryptography implementation."""
    
    def __init__(self):
        self.private_key = None
        self.public_key = None
    
    def generate_key_pair(self):
        """Generate ECC key pair using secp256r1 curve."""
        self.private_key = ec.generate_private_key(
            ec.SECP256R1(), default_backend()
        )
        self.public_key = self.private_key.public_key()
    
    def perform_ecdh(self, peer_public_key) -> bytes:
        """Perform Elliptic Curve Diffie-Hellman key exchange."""
        if not self.private_key:
            raise ValueError("Private key not generated")
        
        shared_key = self.private_key.exchange(ec.ECDH(), peer_public_key)
        
        # Derive a key from the shared secret
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(shared_key)
        
        return derived_key
    
    def sign_data(self, data: str) -> bytes:
        """Sign data using ECDSA."""
        if not self.private_key:
            raise ValueError("Private key not generated")
        
        signature = self.private_key.sign(
            data.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return signature
    
    def verify_signature(self, data: str, signature: bytes, public_key) -> bool:
        """Verify ECDSA signature."""
        try:
            public_key.verify(
                signature,
                data.encode(),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False

# Usage example
alice = ECCCryptography()
bob = ECCCryptography()

# Generate key pairs
alice.generate_key_pair()
bob.generate_key_pair()

# Perform key exchange
alice_shared_key = alice.perform_ecdh(bob.public_key)
bob_shared_key = bob.perform_ecdh(alice.public_key)

print(f"Shared keys match: {alice_shared_key == bob_shared_key}")

# Digital signatures
message = "Hello from Alice"
signature = alice.sign_data(message)
is_valid = bob.verify_signature(message, signature, alice.public_key)
print(f"Signature valid: {is_valid}")
```

### 🔴 Expert Level: Advanced Cryptographic Protocols

#### Authenticated Encryption with ChaCha20-Poly1305

```python
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os

class AuthenticatedEncryption:
    """Authenticated encryption using ChaCha20-Poly1305."""
    
    def __init__(self):
        self.key = None
    
    def generate_key(self) -> bytes:
        """Generate a new encryption key."""
        self.key = ChaCha20Poly1305.generate_key()
        return self.key
    
    def set_key(self, key: bytes):
        """Set encryption key."""
        self.key = key
    
    def encrypt(self, data: str, associated_data: str = None) -> tuple[bytes, bytes]:
        """Encrypt data with authentication."""
        if not self.key:
            raise ValueError("Key not set")
        
        cipher = ChaCha20Poly1305(self.key)
        nonce = os.urandom(12)  # 96-bit nonce for ChaCha20
        
        associated_bytes = associated_data.encode() if associated_data else None
        ciphertext = cipher.encrypt(nonce, data.encode(), associated_bytes)
        
        return nonce, ciphertext
    
    def decrypt(self, nonce: bytes, ciphertext: bytes, associated_data: str = None) -> str:
        """Decrypt and verify authentication."""
        if not self.key:
            raise ValueError("Key not set")
        
        cipher = ChaCha20Poly1305(self.key)
        associated_bytes = associated_data.encode() if associated_data else None
        
        try:
            plaintext = cipher.decrypt(nonce, ciphertext, associated_bytes)
            return plaintext.decode()
        except Exception as e:
            raise ValueError("Decryption failed - data may be corrupted or tampered with")

# Usage example
auth_enc = AuthenticatedEncryption()
key = auth_enc.generate_key()

# Encrypt with associated data
message = "Confidential document content"
associated_data = "document_id:12345,user_id:67890"

nonce, ciphertext = auth_enc.encrypt(message, associated_data)
print(f"Encrypted successfully. Nonce: {nonce.hex()}")

# Decrypt and verify
try:
    decrypted = auth_enc.decrypt(nonce, ciphertext, associated_data)
    print(f"Decrypted: {decrypted}")
except ValueError as e:
    print(f"Decryption failed: {e}")
```

#### Key Derivation and Management

```python
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import secrets
import json
from typing import Dict, Any

class KeyManager:
    """Advanced key derivation and management."""
    
    @staticmethod
    def derive_key_pbkdf2(password: str, salt: bytes = None, iterations: int = 100000) -> tuple[bytes, bytes]:
        """Derive key using PBKDF2."""
        if salt is None:
            salt = secrets.token_bytes(32)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
        )
        key = kdf.derive(password.encode())
        return key, salt
    
    @staticmethod
    def derive_key_scrypt(password: str, salt: bytes = None, n: int = 2**14, r: int = 8, p: int = 1) -> tuple[bytes, bytes]:
        """Derive key using Scrypt (more memory-hard)."""
        if salt is None:
            salt = secrets.token_bytes(32)
        
        kdf = Scrypt(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            n=n,
            r=r,
            p=p,
        )
        key = kdf.derive(password.encode())
        return key, salt
    
    @staticmethod
    def derive_multiple_keys(master_key: bytes, info_list: list[str]) -> Dict[str, bytes]:
        """Derive multiple keys from a master key using HKDF."""
        derived_keys = {}
        
        for info in info_list:
            hkdf = HKDF(
                algorithm=hashes.SHA256(),
                length=32,
                salt=None,
                info=info.encode(),
            )
            derived_keys[info] = hkdf.derive(master_key)
        
        return derived_keys
    
    @staticmethod
    def create_key_hierarchy(master_password: str, purposes: list[str]) -> Dict[str, Any]:
        """Create a hierarchical key structure."""
        # Derive master key from password
        master_key, salt = KeyManager.derive_key_scrypt(master_password)
        
        # Derive purpose-specific keys
        purpose_keys = KeyManager.derive_multiple_keys(master_key, purposes)
        
        return {
            'master_salt': salt.hex(),
            'purposes': {purpose: key.hex() for purpose, key in purpose_keys.items()}
        }

# Usage example
key_manager = KeyManager()

# Create key hierarchy
master_password = "very_secure_master_password_123!"
purposes = ["encryption", "authentication", "signing", "database"]

key_hierarchy = key_manager.create_key_hierarchy(master_password, purposes)
print("Key hierarchy created:")
print(json.dumps({k: v if k == 'purposes' else v for k, v in key_hierarchy.items()}, indent=2))

# Use derived keys
encryption_key = bytes.fromhex(key_hierarchy['purposes']['encryption'])
auth_key = bytes.fromhex(key_hierarchy['purposes']['authentication'])

print(f"Encryption key: {encryption_key.hex()[:32]}...")
print(f"Authentication key: {auth_key.hex()[:32]}...")
```

#### Secure Random Number Generation

```python
import secrets
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SecureRandom:
    """Cryptographically secure random number generation."""
    
    @staticmethod
    def generate_token(length: int = 32) -> str:
        """Generate secure random token."""
        return secrets.token_urlsafe(length)
    
    @staticmethod
    def generate_hex(length: int = 32) -> str:
        """Generate secure random hex string."""
        return secrets.token_hex(length)
    
    @staticmethod
    def generate_bytes(length: int = 32) -> bytes:
        """Generate secure random bytes."""
        return secrets.token_bytes(length)
    
    @staticmethod
    def generate_password(length: int = 16, include_symbols: bool = True) -> str:
        """Generate cryptographically secure password."""
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if include_symbols:
            alphabet += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    
    @staticmethod
    def generate_uuid() -> str:
        """Generate cryptographically secure UUID."""
        return secrets.token_hex(16)
    
    @staticmethod
    def secure_choice(sequence):
        """Securely choose random element from sequence."""
        return secrets.choice(sequence)
    
    @staticmethod
    def secure_randint(min_val: int, max_val: int) -> int:
        """Generate secure random integer in range."""
        return secrets.randbelow(max_val - min_val + 1) + min_val

# Usage examples
secure_random = SecureRandom()

# Generate various secure random values
api_key = secure_random.generate_token(32)
session_id = secure_random.generate_hex(16)
encryption_key = secure_random.generate_bytes(32)
password = secure_random.generate_password(20, True)
uuid = secure_random.generate_uuid()

print(f"API Key: {api_key}")
print(f"Session ID: {session_id}")
print(f"Encryption Key: {encryption_key.hex()}")
print(f"Password: {password}")
print(f"UUID: {uuid}")

# Secure random choices
colors = ["red", "green", "blue", "yellow", "purple"]
random_color = secure_random.secure_choice(colors)
random_number = secure_random.secure_randint(1, 100)

print(f"Random color: {random_color}")
print(f"Random number: {random_number}")
```

---

## Security Checklist {#checklist}

Use this comprehensive checklist to ensure your Python applications follow security best practices.

### 🔍 Development Phase

#### Input Validation & Sanitization
- [ ] All user inputs are validated and sanitized
- [ ] Input length limits are enforced
- [ ] File upload restrictions are implemented
- [ ] Data type validation is performed
- [ ] Whitelist validation is used where possible
- [ ] Regular expressions are secure and tested

#### Authentication & Authorization
- [ ] Strong password policies are enforced
- [ ] Passwords are properly hashed (bcrypt/scrypt/Argon2)
- [ ] Multi-factor authentication is implemented
- [ ] Session management is secure
- [ ] Account lockout mechanisms are in place
- [ ] Password reset flows are secure

#### Data Protection
- [ ] Sensitive data is encrypted at rest
- [ ] Data is encrypted in transit (TLS/SSL)
- [ ] Encryption keys are properly managed
- [ ] Personal data handling complies with regulations
- [ ] Data retention policies are implemented
- [ ] Secure deletion methods are used

#### Database Security
- [ ] Parameterized queries are used exclusively
- [ ] Database connections are encrypted
- [ ] Least privilege principle is applied
- [ ] Database credentials are secured
- [ ] Regular security updates are applied
- [ ] Database backups are encrypted

#### Error Handling & Logging
- [ ] Error messages don't leak sensitive information
- [ ] Comprehensive logging is implemented
- [ ] Log files are secured and monitored
- [ ] Security events are logged
- [ ] Log injection attacks are prevented
- [ ] Centralized logging is configured

### 🚀 Deployment Phase

#### Infrastructure Security
- [ ] Secure hosting environment is configured
- [ ] Network security controls are in place
- [ ] Firewall rules are properly configured
- [ ] Regular security updates are applied
- [ ] Monitoring and alerting are configured
- [ ] Backup and recovery procedures are tested

#### Configuration Security
- [ ] Default credentials are changed
- [ ] Unnecessary services are disabled
- [ ] Security headers are configured
- [ ] HTTPS is enforced
- [ ] Environment variables are secured
- [ ] Debug mode is disabled in production

#### Dependency Management
- [ ] Dependencies are regularly updated
- [ ] Vulnerability scanning is automated
- [ ] Only necessary dependencies are included
- [ ] Dependency sources are trusted
- [ ] License compliance is verified
- [ ] Supply chain security is considered

### 🔄 Maintenance Phase

#### Ongoing Security
- [ ] Regular security assessments are conducted
- [ ] Penetration testing is performed
- [ ] Security training is provided to team
- [ ] Incident response plan is in place
- [ ] Security metrics are tracked
- [ ] Compliance requirements are met

#### Monitoring & Response
- [ ] Real-time monitoring is implemented
- [ ] Anomaly detection is configured
- [ ] Incident response procedures are documented
- [ ] Security patches are applied promptly
- [ ] Regular security reviews are conducted
- [ ] Threat intelligence is incorporated

---

## Security Testing {#security-testing}

### Automated Security Testing

```python
import unittest
import requests
import time
from unittest.mock import patch, MagicMock

class SecurityTestSuite(unittest.TestCase):
    """Comprehensive security test suite."""
    
    def setUp(self):
        self.base_url = "http://localhost:8000"
        self.test_user = {
            "username": "testuser",
            "password": "TestPass123!",
            "email": "test@example.com"
        }
    
    def test_sql_injection_protection(self):
        """Test SQL injection protection."""
        malicious_inputs = [
            "'; DROP TABLE users; --",
            "' OR '1'='1",
            "admin'--",
            "' UNION SELECT * FROM users --"
        ]
        
        for payload in malicious_inputs:
            response = requests.post(f"{self.base_url}/login", data={
                "username": payload,
                "password": "password"
            })
            
            # Should not return successful login or error revealing DB structure
            self.assertNotIn("syntax error", response.text.lower())
            self.assertNotIn("mysql", response.text.lower())
            self.assertNotIn("postgresql", response.text.lower())
            self.assertEqual(response.status_code, 401)
    
    def test_xss_protection(self):
        """Test XSS protection."""
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "javascript:alert('XSS')",
            "<img src=x onerror=alert('XSS')>",
            "';alert('XSS');//"
        ]
        
        for payload in xss_payloads:
            response = requests.post(f"{self.base_url}/comment", data={
                "content": payload
            })
            
            # Check that script tags are escaped or removed
            self.assertNotIn("<script>", response.text)
            self.assertNotIn("javascript:", response.text)
            self.assertNotIn("onerror=", response.text)
    
    def test_password_strength_enforcement(self):
        """Test password strength requirements."""
        weak_passwords = [
            "123456",
            "password",
            "abc123",
            "qwerty",
            "short"
        ]
        
        for weak_password in weak_passwords:
            response = requests.post(f"{self.base_url}/register", data={
                "username": "testuser",
                "password": weak_password,
                "email": "test@example.com"
            })
            
            self.assertEqual(response.status_code, 400)
            self.assertIn("password", response.json().get("errors", {}).keys())
    
    def test_rate_limiting(self):
        """Test rate limiting protection."""
        # Attempt multiple rapid requests
        for i in range(10):
            response = requests.post(f"{self.base_url}/login", data={
                "username": "testuser",
                "password": "wrongpassword"
            })
            
            if i > 5:  # After several attempts
                self.assertIn(response.status_code, [429, 403])  # Rate limited
    
    def test_session_security(self):
        """Test session security."""
        # Login to get session
        login_response = requests.post(f"{self.base_url}/login", data=self.test_user)
        
        if login_response.status_code == 200:
            cookies = login_response.cookies
            
            # Check for secure cookie attributes
            session_cookie = cookies.get('session')
            if session_cookie:
                self.assertTrue(session_cookie.secure)  # Should be secure
                self.assertTrue(session_cookie.httponly)  # Should be HTTP-only
    
    def test_file_upload_security(self):
        """Test file upload security."""
        malicious_files = [
            ("test.php", "<?php system($_GET['cmd']); ?>", "application/x-php"),
            ("test.exe", b"\x4d\x5a", "application/x-executable"),
            ("test.jsp", "<%@ page import=\"java.io.*\" %>", "application/x-jsp")
        ]
        
        for filename, content, content_type in malicious_files:
            files = {'file': (filename, content, content_type)}
            response = requests.post(f"{self.base_url}/upload", files=files)
            
            # Should reject dangerous file types
            self.assertNotEqual(response.status_code, 200)
    
    def test_information_disclosure(self):
        """Test for information disclosure."""
        # Test error pages don't reveal sensitive info
        response = requests.get(f"{self.base_url}/nonexistent")
        
        # Should not reveal server information
        self.assertNotIn("apache", response.text.lower())
        self.assertNotIn("nginx", response.text.lower())
        self.assertNotIn("python", response.text.lower())
        self.assertNotIn("traceback", response.text.lower())
    
    def test_csrf_protection(self):
        """Test CSRF protection."""
        # Attempt request without CSRF token
        response = requests.post(f"{self.base_url}/change-password", data={
            "new_password": "NewPass123!"
        })
        
        # Should be rejected due to missing CSRF token
        self.assertIn(response.status_code, [403, 400])

if __name__ == "__main__":
    unittest.main()
```

### Security Scanning Tools Integration

```python
import subprocess
import json
import sys
from typing import Dict, List, Any

class SecurityScanner:
    """Integrate security scanning tools."""
    
    @staticmethod
    def run_bandit_scan(project_path: str) -> Dict[str, Any]:
        """Run Bandit security scanner."""
        try:
            result = subprocess.run([
                'bandit', '-r', project_path, '-f', 'json'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                return json.loads(result.stdout)
            else:
                return {"error": result.stderr}
        except FileNotFoundError:
            return {"error": "Bandit not installed"}
    
    @staticmethod
    def run_safety_check() -> Dict[str, Any]:
        """Check for known vulnerabilities in dependencies."""
        try:
            result = subprocess.run([
                'safety', 'check', '--json'
            ], capture_output=True, text=True)
            
            return json.loads(result.stdout)
        except FileNotFoundError:
            return {"error": "Safety not installed"}
    
    @staticmethod
    def run_semgrep_scan(project_path: str) -> Dict[str, Any]:
        """Run Semgrep security scanner."""
        try:
            result = subprocess.run([
                'semgrep', '--config=auto', '--json', project_path
            ], capture_output=True, text=True)
            
            return json.loads(result.stdout)
        except FileNotFoundError:
            return {"error": "Semgrep not installed"}
    
    @staticmethod
    def generate_security_report(project_path: str) -> Dict[str, Any]:
        """Generate comprehensive security report."""
        report = {
            "timestamp": time.time(),
            "project_path": project_path,
            "scans": {}
        }
        
        # Run all scanners
        report["scans"]["bandit"] = SecurityScanner.run_bandit_scan(project_path)
        report["scans"]["safety"] = SecurityScanner.run_safety_check()
        report["scans"]["semgrep"] = SecurityScanner.run_semgrep_scan(project_path)
        
        # Summarize findings
        total_issues = 0
        high_severity = 0
        
        for scanner, results in report["scans"].items():
            if "error" not in results:
                if scanner == "bandit" and "results" in results:
                    total_issues += len(results["results"])
                    high_severity += len([r for r in results["results"] 
                                        if r.get("issue_severity") == "HIGH"])
        
        report["summary"] = {
            "total_issues": total_issues,
            "high_severity_issues": high_severity,
            "scanners_run": len([s for s in report["scans"] if "error" not in report["scans"][s]])
        }
        
        return report

# Usage
if __name__ == "__main__":
    scanner = SecurityScanner()
    report = scanner.generate_security_report(".")
    
    print(json.dumps(report, indent=2))
    
    # Exit with error code if high severity issues found
    if report["summary"]["high_severity_issues"] > 0:
        sys.exit(1)
```

---

## Resources and Further Reading {#resources}

### 📚 Essential Books

1. **"The Web Application Hacker's Handbook"** by Dafydd Stuttard
2. **"Cryptography Engineering"** by Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno
3. **"The Tangled Web"** by Michal Zalewski
4. **"Security Engineering"** by Ross Anderson
5. **"Practical Cryptography"** by Niels Ferguson and Bruce Schneier

### 🌐 Online Resources

#### Security Guidelines & Standards
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Python Security](https://owasp.org/www-project-python-security/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)

#### Python Security Resources
- [Python Security Documentation](https://docs.python.org/3/library/security_warnings.html)
- [Bandit Security Linter](https://bandit.readthedocs.io/)
- [Safety - Dependency Vulnerability Scanner](https://pyup.io/safety/)
- [Python Cryptographic Authority](https://cryptography.io/)

#### Security Tools & Libraries
- [cryptography](https://cryptography.io/) - Modern cryptography for Python
- [bcrypt](https://pypi.org/project/bcrypt/) - Password hashing
- [PyJWT](https://pyjwt.readthedocs.io/) - JSON Web Tokens
- [requests](https://requests.readthedocs.io/) - HTTP library with security features
- [Werkzeug](https://werkzeug.palletsprojects.com/) - Security utilities

### 🛠️ Security Testing Tools

#### Static Analysis
- **Bandit** - Python security linter
- **Semgrep** - Static analysis for security bugs
- **CodeQL** - Semantic code analysis
- **SonarQube** - Code quality and security

#### Dynamic Analysis
- **OWASP ZAP** - Web application security scanner
- **Burp Suite** - Web vulnerability scanner
- **SQLMap** - SQL injection testing
- **Nikto** - Web server scanner

#### Dependency Scanning
- **Safety** - Python dependency vulnerability scanner
- **Snyk** - Vulnerability scanning for dependencies
- **OWASP Dependency-Check** - Dependency vulnerability scanner
- **GitHub Security Advisories** - Automated dependency alerts

### 📋 Security Checklists & Standards

#### Compliance Frameworks
- **SOC 2** - Security, availability, and confidentiality
- **ISO 27001** - Information security management
- **GDPR** - General Data Protection Regulation
- **HIPAA** - Health Insurance Portability and Accountability Act
- **PCI DSS** - Payment Card Industry Data Security Standard

#### Security Assessment Methodologies
- **OWASP Testing Guide** - Web application security testing
- **NIST SP 800-115** - Technical guide to information security testing
- **PTES** - Penetration Testing Execution Standard
- **OSSTMM** - Open Source Security Testing Methodology Manual

### 🎓 Training & Certification

#### Online Courses
- **Cybrary** - Free cybersecurity training
- **SANS** - Professional security training
- **Coursera** - University cybersecurity courses
- **edX** - MIT and other university security courses

#### Certifications
- **CISSP** - Certified Information Systems Security Professional
- **CEH** - Certified Ethical Hacker
- **OSCP** - Offensive Security Certified Professional
- **GSEC** - GIAC Security Essentials

### 🔗 Community & Updates

#### Security Communities
- **r/netsec** - Network security discussions
- **OWASP Local Chapters** - Local security meetups
- **DEF CON Groups** - Hacker conferences and meetups
- **2600 Meetings** - Hacker meetups worldwide

#### Security News & Blogs
- **Krebs on Security** - Security news and investigation
- **Schneier on Security** - Bruce Schneier's security blog
- **The Hacker News** - Cybersecurity news
- **Dark Reading** - Enterprise security news

#### Vulnerability Databases
- **CVE** - Common Vulnerabilities and Exposures
- **NVD** - National Vulnerability Database
- **Exploit-DB** - Exploit database
- **Security Focus** - Vulnerability database

### 📊 Security Metrics & KPIs

Track these metrics to measure your security posture:

1. **Vulnerability Metrics**
   - Time to patch critical vulnerabilities
   - Number of unpatched vulnerabilities
   - Vulnerability density (vulnerabilities per KLOC)

2. **Incident Response Metrics**
   - Mean time to detection (MTTD)
   - Mean time to response (MTTR)
   - Number of security incidents

3. **Security Testing Metrics**
   - Code coverage of security tests
   - Number of security issues found in testing
   - False positive rate of security tools

4. **Compliance Metrics**
   - Compliance score percentage
   - Number of compliance violations
   - Time to remediate compliance issues

---

## Conclusion

Security is not a destination but a continuous journey. This tutorial has covered the essential security practices for Python development, from basic input validation to advanced cryptographic implementations. Remember:

1. **Security by Design** - Build security into your applications from the start
2. **Defense in Depth** - Use multiple layers of security controls
3. **Continuous Learning** - Stay updated with the latest security threats and best practices
4. **Regular Testing** - Continuously test and validate your security measures
5. **Team Education** - Ensure your entire team understands security principles

The security landscape is constantly evolving, so make sure to:
- Subscribe to security advisories
- Regularly update dependencies
- Conduct security reviews
- Practice incident response
- Learn from security incidents

Stay secure, and happy coding! 🔒

---

*Last updated: December 2025*
*For questions or contributions, please refer to the project's contribution guidelines.*