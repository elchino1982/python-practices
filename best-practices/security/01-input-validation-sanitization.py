"""Question: Implement comprehensive input validation and sanitization techniques.

Create a secure input handling system that validates and sanitizes different types
of user input to prevent security vulnerabilities.

Requirements:
1. Create validators for different data types (email, phone, URL, etc.)
2. Implement sanitization functions for HTML, SQL, and file paths
3. Create a comprehensive input validation framework
4. Demonstrate protection against common attacks (XSS, SQL injection, etc.)
5. Show proper error handling and logging

Example usage:
    validator = InputValidator()
    clean_email = validator.validate_email("user@example.com")
    safe_html = sanitize_html("<script>alert('xss')</script>Hello")
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what types of validation you need
# - Start with simple validation functions
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
# - What are common input validation patterns?
# - How do you sanitize different types of content?
# - What security vulnerabilities should you prevent?
# - How do you handle validation errors gracefully?
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


# Step 1: Import modules and create basic validation functions
# ===============================================================================

# Explanation:
# Input validation starts with basic checks for common data types.
# We'll create simple validators for email, phone numbers, and basic strings.

import re
import html
import urllib.parse
from typing import Optional, Union, List, Dict, Any

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    if not email or not isinstance(email, str):
        return False
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove common separators
    clean_phone = re.sub(r'[\s\-\(\)\+]', '', phone)
    
    # Check if it's all digits and reasonable length
    return clean_phone.isdigit() and 10 <= len(clean_phone) <= 15

def sanitize_string(text: str, max_length: int = 255) -> str:
    """Basic string sanitization."""
    if not isinstance(text, str):
        return ""
    
    # Remove leading/trailing whitespace and limit length
    sanitized = text.strip()[:max_length]
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\t\n\r')
    
    return sanitized

# Test basic validation
print("=== Step 1: Basic Validation ===")
print(f"Valid email: {validate_email('user@example.com')}")
print(f"Invalid email: {validate_email('invalid-email')}")
print(f"Valid phone: {validate_phone('+1-555-123-4567')}")
print(f"Invalid phone: {validate_phone('abc123')}")
print(f"Sanitized string: '{sanitize_string('  Hello World!  ')}'")
print()

# What we accomplished in this step:
# - Created basic validation functions for email and phone
# - Implemented string sanitization with length limits
# - Added protection against control characters


# Step 2: Add HTML sanitization and XSS protection
# ===============================================================================

# Explanation:
# HTML sanitization is crucial for preventing XSS attacks. We need to escape
# or remove dangerous HTML tags and attributes while preserving safe content.

import re
import html
import urllib.parse
from typing import Optional, Union, List, Dict, Any

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    if not email or not isinstance(email, str):
        return False
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove common separators
    clean_phone = re.sub(r'[\s\-\(\)\+]', '', phone)
    
    # Check if it's all digits and reasonable length
    return clean_phone.isdigit() and 10 <= len(clean_phone) <= 15

def sanitize_string(text: str, max_length: int = 255) -> str:
    """Basic string sanitization."""
    if not isinstance(text, str):
        return ""
    
    # Remove leading/trailing whitespace and limit length
    sanitized = text.strip()[:max_length]
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\t\n\r')
    
    return sanitized

def sanitize_html(text: str, allowed_tags: Optional[List[str]] = None) -> str:
    """Sanitize HTML content to prevent XSS attacks."""
    if not isinstance(text, str):
        return ""
    
    if allowed_tags is None:
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'p', 'br']
    
    # First, escape all HTML entities
    sanitized = html.escape(text)
    
    # If we have allowed tags, selectively unescape them
    if allowed_tags:
        for tag in allowed_tags:
            # Allow opening and closing tags
            sanitized = sanitized.replace(f'&lt;{tag}&gt;', f'<{tag}>')
            sanitized = sanitized.replace(f'&lt;/{tag}&gt;', f'</{tag}>')
    
    return sanitized

def remove_dangerous_patterns(text: str) -> str:
    """Remove dangerous patterns that could lead to XSS."""
    if not isinstance(text, str):
        return ""
    
    # Remove javascript: URLs
    text = re.sub(r'javascript\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove data: URLs (can contain scripts)
    text = re.sub(r'data\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove on* event handlers
    text = re.sub(r'\bon\w+\s*=', '', text, flags=re.IGNORECASE)
    
    # Remove script tags completely
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    return text

def validate_url(url: str) -> bool:
    """Validate URL format and check for dangerous schemes."""
    if not url or not isinstance(url, str):
        return False
    
    try:
        parsed = urllib.parse.urlparse(url)
        
        # Check for valid scheme
        allowed_schemes = ['http', 'https', 'ftp', 'ftps']
        if parsed.scheme.lower() not in allowed_schemes:
            return False
        
        # Must have a netloc (domain)
        if not parsed.netloc:
            return False
        
        return True
    except Exception:
        return False

# Test HTML sanitization and XSS protection
print("=== Step 2: HTML Sanitization and XSS Protection ===")
malicious_html = "<script>alert('XSS')</script><b>Bold text</b>"
print(f"Original: {malicious_html}")
print(f"Sanitized: {sanitize_html(malicious_html)}")

dangerous_input = "javascript:alert('XSS') onclick=alert('click')"
print(f"Dangerous input: {dangerous_input}")
print(f"Cleaned: {remove_dangerous_patterns(dangerous_input)}")

print(f"Valid URL: {validate_url('https://example.com')}")
print(f"Invalid URL: {validate_url('javascript:alert(1)')}")
print()

# What we accomplished in this step:
# - Added HTML sanitization with configurable allowed tags
# - Implemented XSS protection by removing dangerous patterns
# - Created URL validation with scheme checking
# - Added protection against javascript: and data: URLs


# Step 3: Add SQL injection protection and file path sanitization
# ===============================================================================

# Explanation:
# SQL injection is prevented by proper escaping and parameterized queries.
# File path sanitization prevents directory traversal attacks.

import re
import html
import urllib.parse
import os
from typing import Optional, Union, List, Dict, Any

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    if not email or not isinstance(email, str):
        return False
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove common separators
    clean_phone = re.sub(r'[\s\-\(\)\+]', '', phone)
    
    # Check if it's all digits and reasonable length
    return clean_phone.isdigit() and 10 <= len(clean_phone) <= 15

def sanitize_string(text: str, max_length: int = 255) -> str:
    """Basic string sanitization."""
    if not isinstance(text, str):
        return ""
    
    # Remove leading/trailing whitespace and limit length
    sanitized = text.strip()[:max_length]
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\t\n\r')
    
    return sanitized

def sanitize_html(text: str, allowed_tags: Optional[List[str]] = None) -> str:
    """Sanitize HTML content to prevent XSS attacks."""
    if not isinstance(text, str):
        return ""
    
    if allowed_tags is None:
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'p', 'br']
    
    # First, escape all HTML entities
    sanitized = html.escape(text)
    
    # If we have allowed tags, selectively unescape them
    if allowed_tags:
        for tag in allowed_tags:
            # Allow opening and closing tags
            sanitized = sanitized.replace(f'&lt;{tag}&gt;', f'<{tag}>')
            sanitized = sanitized.replace(f'&lt;/{tag}&gt;', f'</{tag}>')
    
    return sanitized

def remove_dangerous_patterns(text: str) -> str:
    """Remove dangerous patterns that could lead to XSS."""
    if not isinstance(text, str):
        return ""
    
    # Remove javascript: URLs
    text = re.sub(r'javascript\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove data: URLs (can contain scripts)
    text = re.sub(r'data\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove on* event handlers
    text = re.sub(r'\bon\w+\s*=', '', text, flags=re.IGNORECASE)
    
    # Remove script tags completely
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    return text

def validate_url(url: str) -> bool:
    """Validate URL format and check for dangerous schemes."""
    if not url or not isinstance(url, str):
        return False
    
    try:
        parsed = urllib.parse.urlparse(url)
        
        # Check for valid scheme
        allowed_schemes = ['http', 'https', 'ftp', 'ftps']
        if parsed.scheme.lower() not in allowed_schemes:
            return False
        
        # Must have a netloc (domain)
        if not parsed.netloc:
            return False
        
        return True
    except Exception:
        return False

def escape_sql(text: str) -> str:
    """Escape SQL special characters to prevent injection."""
    if not isinstance(text, str):
        return ""
    
    # Escape single quotes by doubling them
    escaped = text.replace("'", "''")
    
    # Escape backslashes
    escaped = escaped.replace("\\", "\\\\")
    
    # Remove or escape null bytes
    escaped = escaped.replace("\x00", "")
    
    return escaped

def detect_sql_injection(text: str) -> bool:
    """Detect potential SQL injection patterns."""
    if not isinstance(text, str):
        return False
    
    # Common SQL injection patterns
    dangerous_patterns = [
        r"(\b(union|select|insert|update|delete|drop|create|alter|exec|execute)\b)",
        r"(--|#|/\*|\*/)",  # SQL comments
        r"(\bor\b.*=.*=|\band\b.*=.*=)",  # Boolean-based injection
        r"(\bxp_cmdshell\b|\bsp_executesql\b)",  # SQL Server specific
        r"(\bload_file\b|\binto\s+outfile\b)",  # MySQL specific
    ]
    
    text_lower = text.lower()
    for pattern in dangerous_patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    
    return False

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent directory traversal."""
    if not isinstance(filename, str):
        return ""
    
    # Remove directory traversal patterns
    sanitized = filename.replace("..", "").replace("/", "").replace("\\", "")
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32)
    
    # Remove leading/trailing dots and spaces
    sanitized = sanitized.strip('. ')
    
    # Limit length
    sanitized = sanitized[:255]
    
    # Ensure it's not empty after sanitization
    if not sanitized:
        sanitized = "unnamed_file"
    
    return sanitized

def validate_file_path(file_path: str, allowed_dirs: Optional[List[str]] = None) -> bool:
    """Validate file path to prevent directory traversal attacks."""
    if not isinstance(file_path, str):
        return False
    
    try:
        # Normalize the path
        normalized = os.path.normpath(file_path)
        
        # Check for directory traversal
        if ".." in normalized or normalized.startswith("/"):
            return False
        
        # If allowed directories are specified, check against them
        if allowed_dirs:
            for allowed_dir in allowed_dirs:
                if normalized.startswith(allowed_dir):
                    return True
            return False
        
        return True
    except Exception:
        return False

# Test SQL injection protection and file path sanitization
print("=== Step 3: SQL Injection Protection and File Path Sanitization ===")

# SQL injection tests
malicious_sql = "'; DROP TABLE users; --"
print(f"Malicious SQL: {malicious_sql}")
print(f"Escaped: {escape_sql(malicious_sql)}")
print(f"Is SQL injection: {detect_sql_injection(malicious_sql)}")

# File path tests
dangerous_filename = "../../../etc/passwd"
print(f"Dangerous filename: {dangerous_filename}")
print(f"Sanitized: {sanitize_filename(dangerous_filename)}")
print(f"Valid path: {validate_file_path('uploads/image.jpg', ['uploads/'])}")
print(f"Invalid path: {validate_file_path('../config/secrets.txt', ['uploads/'])}")
print()

# What we accomplished in this step:
# - Added SQL injection detection and prevention
# - Implemented file path sanitization against directory traversal
# - Created filename sanitization for safe file uploads
# - Added path validation with allowed directory restrictions


# Step 4: Create comprehensive input validation framework
# ===============================================================================

# Explanation:
# A validation framework provides a unified interface for all validation
# and sanitization operations with proper error handling and logging.

import re
import html
import urllib.parse
import os
import logging
from typing import Optional, Union, List, Dict, Any
from dataclasses import dataclass
from enum import Enum

# Configure logging for security events
logging.basicConfig(level=logging.INFO)
security_logger = logging.getLogger('security')

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

class SanitizationLevel(Enum):
    """Levels of sanitization strictness."""
    BASIC = "basic"
    STRICT = "strict"
    PARANOID = "paranoid"

@dataclass
class ValidationResult:
    """Result of validation operation."""
    is_valid: bool
    sanitized_value: Any
    errors: List[str]
    warnings: List[str]

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    if not email or not isinstance(email, str):
        return False
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove common separators
    clean_phone = re.sub(r'[\s\-\(\)\+]', '', phone)
    
    # Check if it's all digits and reasonable length
    return clean_phone.isdigit() and 10 <= len(clean_phone) <= 15

def sanitize_string(text: str, max_length: int = 255) -> str:
    """Basic string sanitization."""
    if not isinstance(text, str):
        return ""
    
    # Remove leading/trailing whitespace and limit length
    sanitized = text.strip()[:max_length]
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\t\n\r')
    
    return sanitized

def sanitize_html(text: str, allowed_tags: Optional[List[str]] = None) -> str:
    """Sanitize HTML content to prevent XSS attacks."""
    if not isinstance(text, str):
        return ""
    
    if allowed_tags is None:
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'p', 'br']
    
    # First, escape all HTML entities
    sanitized = html.escape(text)
    
    # If we have allowed tags, selectively unescape them
    if allowed_tags:
        for tag in allowed_tags:
            # Allow opening and closing tags
            sanitized = sanitized.replace(f'&lt;{tag}&gt;', f'<{tag}>')
            sanitized = sanitized.replace(f'&lt;/{tag}&gt;', f'</{tag}>')
    
    return sanitized

def remove_dangerous_patterns(text: str) -> str:
    """Remove dangerous patterns that could lead to XSS."""
    if not isinstance(text, str):
        return ""
    
    # Remove javascript: URLs
    text = re.sub(r'javascript\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove data: URLs (can contain scripts)
    text = re.sub(r'data\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove on* event handlers
    text = re.sub(r'\bon\w+\s*=', '', text, flags=re.IGNORECASE)
    
    # Remove script tags completely
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    return text

def validate_url(url: str) -> bool:
    """Validate URL format and check for dangerous schemes."""
    if not url or not isinstance(url, str):
        return False
    
    try:
        parsed = urllib.parse.urlparse(url)
        
        # Check for valid scheme
        allowed_schemes = ['http', 'https', 'ftp', 'ftps']
        if parsed.scheme.lower() not in allowed_schemes:
            return False
        
        # Must have a netloc (domain)
        if not parsed.netloc:
            return False
        
        return True
    except Exception:
        return False

def escape_sql(text: str) -> str:
    """Escape SQL special characters to prevent injection."""
    if not isinstance(text, str):
        return ""
    
    # Escape single quotes by doubling them
    escaped = text.replace("'", "''")
    
    # Escape backslashes
    escaped = escaped.replace("\\", "\\\\")
    
    # Remove or escape null bytes
    escaped = escaped.replace("\x00", "")
    
    return escaped

def detect_sql_injection(text: str) -> bool:
    """Detect potential SQL injection patterns."""
    if not isinstance(text, str):
        return False
    
    # Common SQL injection patterns
    dangerous_patterns = [
        r"(\b(union|select|insert|update|delete|drop|create|alter|exec|execute)\b)",
        r"(--|#|/\*|\*/)",  # SQL comments
        r"(\bor\b.*=.*=|\band\b.*=.*=)",  # Boolean-based injection
        r"(\bxp_cmdshell\b|\bsp_executesql\b)",  # SQL Server specific
        r"(\bload_file\b|\binto\s+outfile\b)",  # MySQL specific
    ]
    
    text_lower = text.lower()
    for pattern in dangerous_patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    
    return False

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent directory traversal."""
    if not isinstance(filename, str):
        return ""
    
    # Remove directory traversal patterns
    sanitized = filename.replace("..", "").replace("/", "").replace("\\", "")
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32)
    
    # Remove leading/trailing dots and spaces
    sanitized = sanitized.strip('. ')
    
    # Limit length
    sanitized = sanitized[:255]
    
    # Ensure it's not empty after sanitization
    if not sanitized:
        sanitized = "unnamed_file"
    
    return sanitized

def validate_file_path(file_path: str, allowed_dirs: Optional[List[str]] = None) -> bool:
    """Validate file path to prevent directory traversal attacks."""
    if not isinstance(file_path, str):
        return False
    
    try:
        # Normalize the path
        normalized = os.path.normpath(file_path)
        
        # Check for directory traversal
        if ".." in normalized or normalized.startswith("/"):
            return False
        
        # If allowed directories are specified, check against them
        if allowed_dirs:
            for allowed_dir in allowed_dirs:
                if normalized.startswith(allowed_dir):
                    return True
            return False
        
        return True
    except Exception:
        return False

class InputValidator:
    """Comprehensive input validation and sanitization framework."""
    
    def __init__(self, sanitization_level: SanitizationLevel = SanitizationLevel.STRICT):
        self.sanitization_level = sanitization_level
        self.logger = security_logger
    
    def validate_and_sanitize(self, value: Any, data_type: str, **kwargs) -> ValidationResult:
        """Main validation and sanitization method."""
        errors = []
        warnings = []
        sanitized_value = value
        
        try:
            if data_type == "email":
                sanitized_value = self._process_email(value, errors, warnings)
            elif data_type == "phone":
                sanitized_value = self._process_phone(value, errors, warnings)
            elif data_type == "url":
                sanitized_value = self._process_url(value, errors, warnings)
            elif data_type == "html":
                sanitized_value = self._process_html(value, errors, warnings, **kwargs)
            elif data_type == "sql":
                sanitized_value = self._process_sql(value, errors, warnings)
            elif data_type == "filename":
                sanitized_value = self._process_filename(value, errors, warnings)
            elif data_type == "filepath":
                sanitized_value = self._process_filepath(value, errors, warnings, **kwargs)
            else:
                sanitized_value = self._process_string(value, errors, warnings, **kwargs)
            
            is_valid = len(errors) == 0
            
            # Log security events
            if errors:
                self.logger.warning(f"Validation failed for {data_type}: {errors}")
            if warnings:
                self.logger.info(f"Validation warnings for {data_type}: {warnings}")
            
            return ValidationResult(is_valid, sanitized_value, errors, warnings)
            
        except Exception as e:
            errors.append(f"Validation error: {str(e)}")
            self.logger.error(f"Validation exception for {data_type}: {str(e)}")
            return ValidationResult(False, value, errors, warnings)
    
    def _process_email(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process email validation."""
        if not validate_email(value):
            errors.append("Invalid email format")
            return ""
        return sanitize_string(value, 254)  # RFC 5321 limit
    
    def _process_phone(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process phone validation."""
        if not validate_phone(value):
            errors.append("Invalid phone number format")
            return ""
        return re.sub(r'[\s\-\(\)\+]', '', value)
    
    def _process_url(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process URL validation."""
        if not validate_url(value):
            errors.append("Invalid or dangerous URL")
            return ""
        return sanitize_string(value, 2048)
    
    def _process_html(self, value: str, errors: List[str], warnings: List[str], **kwargs) -> str:
        """Process HTML sanitization."""
        allowed_tags = kwargs.get('allowed_tags', ['b', 'i', 'u', 'em', 'strong'])
        
        if self.sanitization_level == SanitizationLevel.PARANOID:
            # Strip all HTML
            return html.escape(value)
        elif self.sanitization_level == SanitizationLevel.STRICT:
            # Remove dangerous patterns first
            cleaned = remove_dangerous_patterns(value)
            return sanitize_html(cleaned, allowed_tags)
        else:
            # Basic sanitization
            return sanitize_html(value, allowed_tags)
    
    def _process_sql(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process SQL input."""
        if detect_sql_injection(value):
            errors.append("Potential SQL injection detected")
            warnings.append("Input contains SQL-like patterns")
        
        return escape_sql(value)
    
    def _process_filename(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process filename sanitization."""
        original = value
        sanitized = sanitize_filename(value)
        
        if original != sanitized:
            warnings.append("Filename was modified during sanitization")
        
        return sanitized
    
    def _process_filepath(self, value: str, errors: List[str], warnings: List[str], **kwargs) -> str:
        """Process file path validation."""
        allowed_dirs = kwargs.get('allowed_dirs', [])
        
        if not validate_file_path(value, allowed_dirs):
            errors.append("Invalid or dangerous file path")
            return ""
        
        return sanitize_string(value)
    
    def _process_string(self, value: str, errors: List[str], warnings: List[str], **kwargs) -> str:
        """Process general string sanitization."""
        max_length = kwargs.get('max_length', 255)
        return sanitize_string(value, max_length)

# Test the comprehensive validation framework
print("=== Step 4: Comprehensive Input Validation Framework ===")

validator = InputValidator(SanitizationLevel.STRICT)

# Test various input types
test_cases = [
    ("user@example.com", "email"),
    ("invalid-email", "email"),
    ("<script>alert('xss')</script><b>Bold</b>", "html"),
    ("'; DROP TABLE users; --", "sql"),
    ("../../../etc/passwd", "filename"),
]

for test_input, data_type in test_cases:
    result = validator.validate_and_sanitize(test_input, data_type)
    print(f"Input: {test_input}")
    print(f"Type: {data_type}")
    print(f"Valid: {result.is_valid}")
    print(f"Sanitized: {result.sanitized_value}")
    if result.errors:
        print(f"Errors: {result.errors}")
    if result.warnings:
        print(f"Warnings: {result.warnings}")
    print("-" * 50)

# What we accomplished in this step:
# - Created a comprehensive validation framework with unified interface
# - Added proper error handling and logging
# - Implemented different sanitization levels
# - Created structured validation results with errors and warnings


# Step 5: Add advanced security features and complete testing
# ===============================================================================

# Explanation:
# Advanced security includes rate limiting, input length validation,
# encoding detection, and comprehensive testing of all security features.

import re
import html
import urllib.parse
import os
import logging
import time
import hashlib
from typing import Optional, Union, List, Dict, Any
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict

# Configure logging for security events
logging.basicConfig(level=logging.INFO)
security_logger = logging.getLogger('security')

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

class SanitizationLevel(Enum):
    """Levels of sanitization strictness."""
    BASIC = "basic"
    STRICT = "strict"
    PARANOID = "paranoid"

@dataclass
class ValidationResult:
    """Result of validation operation."""
    is_valid: bool
    sanitized_value: Any
    errors: List[str]
    warnings: List[str]

class RateLimiter:
    """Simple rate limiter for validation requests."""
    
    def __init__(self, max_requests: int = 100, time_window: int = 60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)
    
    def is_allowed(self, identifier: str) -> bool:
        """Check if request is allowed based on rate limit."""
        now = time.time()
        
        # Clean old requests
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier]
            if now - req_time < self.time_window
        ]
        
        # Check if under limit
        if len(self.requests[identifier]) >= self.max_requests:
            return False
        
        # Add current request
        self.requests[identifier].append(now)
        return True

def validate_email(email: str) -> bool:
    """Validate email format using regex."""
    if not email or not isinstance(email, str):
        return False
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email.strip()))

def validate_phone(phone: str) -> bool:
    """Validate phone number format."""
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove common separators
    clean_phone = re.sub(r'[\s\-\(\)\+]', '', phone)
    
    # Check if it's all digits and reasonable length
    return clean_phone.isdigit() and 10 <= len(clean_phone) <= 15

def sanitize_string(text: str, max_length: int = 255) -> str:
    """Basic string sanitization."""
    if not isinstance(text, str):
        return ""
    
    # Remove leading/trailing whitespace and limit length
    sanitized = text.strip()[:max_length]
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\t\n\r')
    
    return sanitized

def sanitize_html(text: str, allowed_tags: Optional[List[str]] = None) -> str:
    """Sanitize HTML content to prevent XSS attacks."""
    if not isinstance(text, str):
        return ""
    
    if allowed_tags is None:
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'p', 'br']
    
    # First, escape all HTML entities
    sanitized = html.escape(text)
    
    # If we have allowed tags, selectively unescape them
    if allowed_tags:
        for tag in allowed_tags:
            # Allow opening and closing tags
            sanitized = sanitized.replace(f'&lt;{tag}&gt;', f'<{tag}>')
            sanitized = sanitized.replace(f'&lt;/{tag}&gt;', f'</{tag}>')
    
    return sanitized

def remove_dangerous_patterns(text: str) -> str:
    """Remove dangerous patterns that could lead to XSS."""
    if not isinstance(text, str):
        return ""
    
    # Remove javascript: URLs
    text = re.sub(r'javascript\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove data: URLs (can contain scripts)
    text = re.sub(r'data\s*:', '', text, flags=re.IGNORECASE)
    
    # Remove on* event handlers
    text = re.sub(r'\bon\w+\s*=', '', text, flags=re.IGNORECASE)
    
    # Remove script tags completely
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    return text

def validate_url(url: str) -> bool:
    """Validate URL format and check for dangerous schemes."""
    if not url or not isinstance(url, str):
        return False
    
    try:
        parsed = urllib.parse.urlparse(url)
        
        # Check for valid scheme
        allowed_schemes = ['http', 'https', 'ftp', 'ftps']
        if parsed.scheme.lower() not in allowed_schemes:
            return False
        
        # Must have a netloc (domain)
        if not parsed.netloc:
            return False
        
        return True
    except Exception:
        return False

def escape_sql(text: str) -> str:
    """Escape SQL special characters to prevent injection."""
    if not isinstance(text, str):
        return ""
    
    # Escape single quotes by doubling them
    escaped = text.replace("'", "''")
    
    # Escape backslashes
    escaped = escaped.replace("\\", "\\\\")
    
    # Remove or escape null bytes
    escaped = escaped.replace("\x00", "")
    
    return escaped

def detect_sql_injection(text: str) -> bool:
    """Detect potential SQL injection patterns."""
    if not isinstance(text, str):
        return False
    
    # Common SQL injection patterns
    dangerous_patterns = [
        r"(\b(union|select|insert|update|delete|drop|create|alter|exec|execute)\b)",
        r"(--|#|/\*|\*/)",  # SQL comments
        r"(\bor\b.*=.*=|\band\b.*=.*=)",  # Boolean-based injection
        r"(\bxp_cmdshell\b|\bsp_executesql\b)",  # SQL Server specific
        r"(\bload_file\b|\binto\s+outfile\b)",  # MySQL specific
    ]
    
    text_lower = text.lower()
    for pattern in dangerous_patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    
    return False

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent directory traversal."""
    if not isinstance(filename, str):
        return ""
    
    # Remove directory traversal patterns
    sanitized = filename.replace("..", "").replace("/", "").replace("\\", "")
    
    # Remove null bytes and control characters
    sanitized = ''.join(char for char in sanitized if ord(char) >= 32)
    
    # Remove leading/trailing dots and spaces
    sanitized = sanitized.strip('. ')
    
    # Limit length
    sanitized = sanitized[:255]
    
    # Ensure it's not empty after sanitization
    if not sanitized:
        sanitized = "unnamed_file"
    
    return sanitized

def validate_file_path(file_path: str, allowed_dirs: Optional[List[str]] = None) -> bool:
    """Validate file path to prevent directory traversal attacks."""
    if not isinstance(file_path, str):
        return False
    
    try:
        # Normalize the path
        normalized = os.path.normpath(file_path)
        
        # Check for directory traversal
        if ".." in normalized or normalized.startswith("/"):
            return False
        
        # If allowed directories are specified, check against them
        if allowed_dirs:
            for allowed_dir in allowed_dirs:
                if normalized.startswith(allowed_dir):
                    return True
            return False
        
        return True
    except Exception:
        return False

def detect_encoding_attacks(text: str) -> bool:
    """Detect potential encoding-based attacks."""
    if not isinstance(text, str):
        return False
    
    # Check for various encoding attacks
    dangerous_encodings = [
        r'%[0-9a-fA-F]{2}',  # URL encoding
        r'&#[0-9]+;',        # HTML numeric entities
        r'&#x[0-9a-fA-F]+;', # HTML hex entities
        r'\\u[0-9a-fA-F]{4}', # Unicode escapes
        r'\\x[0-9a-fA-F]{2}', # Hex escapes
    ]
    
    for pattern in dangerous_encodings:
        if re.search(pattern, text):
            return True
    
    return False

def validate_input_length(text: str, min_length: int = 0, max_length: int = 1000) -> bool:
    """Validate input length to prevent buffer overflow attacks."""
    if not isinstance(text, str):
        return False
    
    return min_length <= len(text) <= max_length

class AdvancedInputValidator:
    """Advanced input validation with security features."""
    
    def __init__(self, sanitization_level: SanitizationLevel = SanitizationLevel.STRICT):
        self.sanitization_level = sanitization_level
        self.logger = security_logger
        self.rate_limiter = RateLimiter()
        self.blocked_ips = set()
        self.suspicious_patterns = []
    
    def validate_and_sanitize(self, value: Any, data_type: str, client_id: str = "default", **kwargs) -> ValidationResult:
        """Advanced validation with rate limiting and threat detection."""
        errors = []
        warnings = []
        sanitized_value = value
        
        # Check rate limiting
        if not self.rate_limiter.is_allowed(client_id):
            errors.append("Rate limit exceeded")
            self.logger.warning(f"Rate limit exceeded for client: {client_id}")
            return ValidationResult(False, value, errors, warnings)
        
        # Check if client is blocked
        if client_id in self.blocked_ips:
            errors.append("Client is blocked")
            self.logger.warning(f"Blocked client attempted access: {client_id}")
            return ValidationResult(False, value, errors, warnings)
        
        try:
            # Advanced security checks
            if isinstance(value, str):
                # Check input length
                max_length = kwargs.get('max_length', 1000)
                if not validate_input_length(value, 0, max_length):
                    errors.append(f"Input length exceeds maximum of {max_length}")
                
                # Check for encoding attacks
                if detect_encoding_attacks(value):
                    warnings.append("Potential encoding attack detected")
                    self.logger.warning(f"Encoding attack detected from {client_id}: {value[:100]}")
                
                # Check for suspicious patterns
                if self._detect_suspicious_patterns(value):
                    warnings.append("Suspicious patterns detected")
                    self._track_suspicious_activity(client_id, value)
            
            # Perform standard validation
            if data_type == "email":
                sanitized_value = self._process_email(value, errors, warnings)
            elif data_type == "phone":
                sanitized_value = self._process_phone(value, errors, warnings)
            elif data_type == "url":
                sanitized_value = self._process_url(value, errors, warnings)
            elif data_type == "html":
                sanitized_value = self._process_html(value, errors, warnings, **kwargs)
            elif data_type == "sql":
                sanitized_value = self._process_sql(value, errors, warnings)
            elif data_type == "filename":
                sanitized_value = self._process_filename(value, errors, warnings)
            elif data_type == "filepath":
                sanitized_value = self._process_filepath(value, errors, warnings, **kwargs)
            else:
                sanitized_value = self._process_string(value, errors, warnings, **kwargs)
            
            is_valid = len(errors) == 0
            
            # Log security events
            if errors:
                self.logger.warning(f"Validation failed for {data_type} from {client_id}: {errors}")
            if warnings:
                self.logger.info(f"Validation warnings for {data_type} from {client_id}: {warnings}")
            
            return ValidationResult(is_valid, sanitized_value, errors, warnings)
            
        except Exception as e:
            errors.append(f"Validation error: {str(e)}")
            self.logger.error(f"Validation exception for {data_type} from {client_id}: {str(e)}")
            return ValidationResult(False, value, errors, warnings)
    
    def _detect_suspicious_patterns(self, text: str) -> bool:
        """Detect suspicious patterns that might indicate attacks."""
        suspicious_patterns = [
            r'<script[^>]*>',  # Script tags
            r'javascript:',    # JavaScript URLs
            r'vbscript:',      # VBScript URLs
            r'onload=',        # Event handlers
            r'onerror=',
            r'onclick=',
            r'eval\(',         # JavaScript eval
            r'document\.cookie', # Cookie access
            r'window\.location', # Location manipulation
        ]
        
        text_lower = text.lower()
        for pattern in suspicious_patterns:
            if re.search(pattern, text_lower):
                return True
        
        return False
    
    def _track_suspicious_activity(self, client_id: str, input_value: str):
        """Track suspicious activity for potential blocking."""
        # Hash the input for privacy
        input_hash = hashlib.sha256(input_value.encode()).hexdigest()[:16]
        
        self.suspicious_patterns.append({
            'client_id': client_id,
            'input_hash': input_hash,
            'timestamp': time.time()
        })
        
        # Block client if too many suspicious activities
        client_suspicious_count = sum(1 for p in self.suspicious_patterns 
                                    if p['client_id'] == client_id)
        
        if client_suspicious_count >= 5:
            self.blocked_ips.add(client_id)
            self.logger.error(f"Client {client_id} blocked due to suspicious activity")
    
    def _process_email(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process email validation."""
        if not validate_email(value):
            errors.append("Invalid email format")
            return ""
        return sanitize_string(value, 254)  # RFC 5321 limit
    
    def _process_phone(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process phone validation."""
        if not validate_phone(value):
            errors.append("Invalid phone number format")
            return ""
        return re.sub(r'[\s\-\(\)\+]', '', value)
    
    def _process_url(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process URL validation."""
        if not validate_url(value):
            errors.append("Invalid or dangerous URL")
            return ""
        return sanitize_string(value, 2048)
    
    def _process_html(self, value: str, errors: List[str], warnings: List[str], **kwargs) -> str:
        """Process HTML sanitization."""
        allowed_tags = kwargs.get('allowed_tags', ['b', 'i', 'u', 'em', 'strong'])
        
        if self.sanitization_level == SanitizationLevel.PARANOID:
            # Strip all HTML
            return html.escape(value)
        elif self.sanitization_level == SanitizationLevel.STRICT:
            # Remove dangerous patterns first
            cleaned = remove_dangerous_patterns(value)
            return sanitize_html(cleaned, allowed_tags)
        else:
            # Basic sanitization
            return sanitize_html(value, allowed_tags)
    
    def _process_sql(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process SQL input."""
        if detect_sql_injection(value):
            errors.append("Potential SQL injection detected")
            warnings.append("Input contains SQL-like patterns")
        
        return escape_sql(value)
    
    def _process_filename(self, value: str, errors: List[str], warnings: List[str]) -> str:
        """Process filename sanitization."""
        original = value
        sanitized = sanitize_filename(value)
        
        if original != sanitized:
            warnings.append("Filename was modified during sanitization")
        
        return sanitized
    
    def _process_filepath(self, value: str, errors: List[str], warnings: List[str], **kwargs) -> str:
        """Process file path validation."""
        allowed_dirs = kwargs.get('allowed_dirs', [])
        
        if not validate_file_path(value, allowed_dirs):
            errors.append("Invalid or dangerous file path")
            return ""
        
        return sanitize_string(value)
    
    def _process_string(self, value: str, errors: List[str], warnings: List[str], **kwargs) -> str:
        """Process general string sanitization."""
        max_length = kwargs.get('max_length', 255)
        return sanitize_string(value, max_length)

# Test the complete advanced validation system
print("=== Step 5: Advanced Security Features and Complete Testing ===")

advanced_validator = AdvancedInputValidator(SanitizationLevel.STRICT)

# Comprehensive test cases
test_cases = [
    # Basic validation tests
    ("user@example.com", "email", "client1"),
    ("invalid-email", "email", "client1"),
    ("+1-555-123-4567", "phone", "client1"),
    ("abc123", "phone", "client1"),
    
    # XSS attack tests
    ("<script>alert('xss')</script>", "html", "client2"),
    ("javascript:alert('xss')", "url", "client2"),
    ("<img src=x onerror=alert('xss')>", "html", "client2"),
    
    # SQL injection tests
    ("'; DROP TABLE users; --", "sql", "client3"),
    ("admin' OR '1'='1", "sql", "client3"),
    ("UNION SELECT * FROM passwords", "sql", "client3"),
    
    # File path traversal tests
    ("../../../etc/passwd", "filename", "client4"),
    ("..\\..\\windows\\system32\\config\\sam", "filepath", "client4"),
    
    # Encoding attack tests
    ("%3Cscript%3Ealert('xss')%3C/script%3E", "html", "client5"),
    ("&#60;script&#62;alert('xss')&#60;/script&#62;", "html", "client5"),
]

print("Running comprehensive security tests...\n")

for test_input, data_type, client_id in test_cases:
    result = advanced_validator.validate_and_sanitize(test_input, data_type, client_id)
    print(f"Client: {client_id}")
    print(f"Input: {test_input}")
    print(f"Type: {data_type}")
    print(f"Valid: {result.is_valid}")
    print(f"Sanitized: {result.sanitized_value}")
    if result.errors:
        print(f"Errors: {result.errors}")
    if result.warnings:
        print(f"Warnings: {result.warnings}")
    print("-" * 60)

print("\n=== Security Summary ===")
print(f"Blocked clients: {len(advanced_validator.blocked_ips)}")
print(f"Suspicious activities tracked: {len(advanced_validator.suspicious_patterns)}")

# What we accomplished in this step:
# - Added advanced security features including rate limiting
# - Implemented suspicious activity tracking and client blocking
# - Added encoding attack detection and input length validation
# - Created comprehensive testing for all security vulnerabilities
# - Demonstrated complete protection against common web attacks


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the comprehensive input validation and sanitization system!
#
# Key security concepts learned:
# - Input validation for different data types (email, phone, URL, etc.)
# - HTML sanitization and XSS prevention
# - SQL injection detection and prevention
# - File path sanitization and directory traversal protection
# - Rate limiting and suspicious activity tracking
# - Encoding attack detection
# - Comprehensive error handling and security logging
# - Different levels of sanitization strictness
#
# Security best practices implemented:
# - Defense in depth with multiple validation layers
# - Proper input sanitization before processing
# - Logging and monitoring of security events
# - Rate limiting to prevent abuse
# - Client blocking for repeated suspicious activity
# - Structured error handling without information leakage
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each security feature thoroughly
# 3. Understand WHY each protection is necessary
# 4. Experiment with different attack vectors
# 5. Add your own validation rules and sanitization methods
#
# Remember: Security is an ongoing process, not a one-time implementation!
# ===============================================================================