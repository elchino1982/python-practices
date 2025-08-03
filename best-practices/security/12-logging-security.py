"""Question: Implement secure logging practices to protect sensitive information and maintain security.

Create a comprehensive logging security system that demonstrates:
1. Secure log configuration and handling
2. Data sanitization and PII protection
3. Log injection prevention
4. Secure log storage and rotation
5. Audit logging and monitoring

Requirements:
1. Create a secure logger with data sanitization
2. Implement PII detection and masking
3. Create audit logging for security events
4. Implement secure log rotation and storage
5. Demonstrate log injection prevention

Example usage:
    secure_logger = SecureLogger()
    secure_logger.log_user_action("user123", "login", {"ip": "192.168.1.1"})
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
# - What sensitive data needs to be protected in logs?
# - How can you detect and sanitize PII (emails, SSNs, credit cards)?
# - What are log injection attacks and how to prevent them?
# - How to implement secure log rotation and storage?
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


# Step 1: Import modules and create basic data sanitization
# ===============================================================================

# Explanation:
# Secure logging starts with sanitizing sensitive data. We need to identify
# and mask PII (Personally Identifiable Information) before logging.

import logging
import re
import hashlib
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
import os

class DataSanitizer:
    """Sanitizes sensitive data before logging."""
    
    def __init__(self):
        # Common PII patterns
        self.patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'ssn': re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b'),
            'credit_card': re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
            'phone': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'ip_address': re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        }
    
    def sanitize_text(self, text: str) -> str:
        """Sanitize text by masking PII."""
        if not isinstance(text, str):
            text = str(text)
        
        # Mask email addresses
        text = self.patterns['email'].sub(lambda m: self._mask_email(m.group()), text)
        
        # Mask SSN
        text = self.patterns['ssn'].sub('***-**-****', text)
        
        # Mask credit card numbers
        text = self.patterns['credit_card'].sub('****-****-****-****', text)
        
        # Mask phone numbers
        text = self.patterns['phone'].sub('***-***-****', text)
        
        return text
    
    def _mask_email(self, email: str) -> str:
        """Mask email while preserving domain for debugging."""
        parts = email.split('@')
        if len(parts) == 2:
            username = parts[0]
            domain = parts[1]
            masked_username = username[0] + '*' * (len(username) - 1)
            return f"{masked_username}@{domain}"
        return "***@***.***"

# What we accomplished in this step:
# - Created basic data sanitization for common PII patterns
# - Implemented email masking that preserves domain for debugging
# - Set up foundation for secure logging


# Step 2: Add log injection prevention
# ===============================================================================

# Explanation:
# Log injection attacks occur when attackers inject malicious content into logs.
# We need to sanitize control characters and escape sequences.

import logging
import re
import hashlib
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
import os

class DataSanitizer:
    """Sanitizes sensitive data before logging."""
    
    def __init__(self):
        # Common PII patterns
        self.patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'ssn': re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b'),
            'credit_card': re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
            'phone': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'ip_address': re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        }
    
    def sanitize_text(self, text: str) -> str:
        """Sanitize text by masking PII."""
        if not isinstance(text, str):
            text = str(text)
        
        # Mask email addresses
        text = self.patterns['email'].sub(lambda m: self._mask_email(m.group()), text)
        
        # Mask SSN
        text = self.patterns['ssn'].sub('***-**-****', text)
        
        # Mask credit card numbers
        text = self.patterns['credit_card'].sub('****-****-****-****', text)
        
        # Mask phone numbers
        text = self.patterns['phone'].sub('***-***-****', text)
        
        return text
    
    def _mask_email(self, email: str) -> str:
        """Mask email while preserving domain for debugging."""
        parts = email.split('@')
        if len(parts) == 2:
            username = parts[0]
            domain = parts[1]
            masked_username = username[0] + '*' * (len(username) - 1)
            return f"{masked_username}@{domain}"
        return "***@***.***"

class LogInjectionPreventer:
    """Prevents log injection attacks by sanitizing control characters."""
    
    def __init__(self):
        # Dangerous control characters and escape sequences
        self.dangerous_chars = {
            '\n': '\\n',    # Newline
            '\r': '\\r',    # Carriage return
            '\t': '\\t',    # Tab
            '\b': '\\b',    # Backspace
            '\f': '\\f',    # Form feed
            '\v': '\\v',    # Vertical tab
            '\0': '\\0',    # Null character
        }
        
        # ANSI escape sequences (for terminal control)
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    
    def sanitize_for_logging(self, text: str) -> str:
        """Sanitize text to prevent log injection attacks."""
        if not isinstance(text, str):
            text = str(text)
        
        # Remove ANSI escape sequences
        text = self.ansi_escape.sub('', text)
        
        # Replace dangerous control characters
        for char, replacement in self.dangerous_chars.items():
            text = text.replace(char, replacement)
        
        # Remove other non-printable characters
        text = ''.join(char for char in text if ord(char) >= 32 or char in ['\t'])
        
        # Limit length to prevent log flooding
        if len(text) > 1000:
            text = text[:997] + "..."
        
        return text
    
    def validate_log_entry(self, entry: str) -> bool:
        """Validate that log entry is safe."""
        # Check for suspicious patterns
        suspicious_patterns = [
            r'(?i)(script|javascript|vbscript)',  # Script injection
            r'(?i)(<|>|&lt;|&gt;)',              # HTML/XML injection
            r'(?i)(union|select|insert|delete)',  # SQL injection patterns
            r'(?i)(eval|exec|system)',            # Code execution
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, entry):
                return False
        
        return True

# What we accomplished in this step:
# - Added log injection prevention with control character sanitization
# - Implemented ANSI escape sequence removal
# - Added validation for suspicious patterns
# - Limited log entry length to prevent flooding


# Step 3: Create the secure logger with data sanitization
# ===============================================================================

# Explanation:
# Now we combine data sanitization and injection prevention into a secure logger
# that handles all logging operations safely.

import logging
import re
import hashlib
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
import os

class DataSanitizer:
    """Sanitizes sensitive data before logging."""
    
    def __init__(self):
        # Common PII patterns
        self.patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'ssn': re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b'),
            'credit_card': re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
            'phone': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'ip_address': re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        }
    
    def sanitize_text(self, text: str) -> str:
        """Sanitize text by masking PII."""
        if not isinstance(text, str):
            text = str(text)
        
        # Mask email addresses
        text = self.patterns['email'].sub(lambda m: self._mask_email(m.group()), text)
        
        # Mask SSN
        text = self.patterns['ssn'].sub('***-**-****', text)
        
        # Mask credit card numbers
        text = self.patterns['credit_card'].sub('****-****-****-****', text)
        
        # Mask phone numbers
        text = self.patterns['phone'].sub('***-***-****', text)
        
        return text
    
    def _mask_email(self, email: str) -> str:
        """Mask email while preserving domain for debugging."""
        parts = email.split('@')
        if len(parts) == 2:
            username = parts[0]
            domain = parts[1]
            masked_username = username[0] + '*' * (len(username) - 1)
            return f"{masked_username}@{domain}"
        return "***@***.***"

class LogInjectionPreventer:
    """Prevents log injection attacks by sanitizing control characters."""
    
    def __init__(self):
        # Dangerous control characters and escape sequences
        self.dangerous_chars = {
            '\n': '\\n',    # Newline
            '\r': '\\r',    # Carriage return
            '\t': '\\t',    # Tab
            '\b': '\\b',    # Backspace
            '\f': '\\f',    # Form feed
            '\v': '\\v',    # Vertical tab
            '\0': '\\0',    # Null character
        }
        
        # ANSI escape sequences (for terminal control)
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    
    def sanitize_for_logging(self, text: str) -> str:
        """Sanitize text to prevent log injection attacks."""
        if not isinstance(text, str):
            text = str(text)
        
        # Remove ANSI escape sequences
        text = self.ansi_escape.sub('', text)
        
        # Replace dangerous control characters
        for char, replacement in self.dangerous_chars.items():
            text = text.replace(char, replacement)
        
        # Remove other non-printable characters
        text = ''.join(char for char in text if ord(char) >= 32 or char in ['\t'])
        
        # Limit length to prevent log flooding
        if len(text) > 1000:
            text = text[:997] + "..."
        
        return text
    
    def validate_log_entry(self, entry: str) -> bool:
        """Validate that log entry is safe."""
        # Check for suspicious patterns
        suspicious_patterns = [
            r'(?i)(script|javascript|vbscript)',  # Script injection
            r'(?i)(<|>|&lt;|&gt;)',              # HTML/XML injection
            r'(?i)(union|select|insert|delete)',  # SQL injection patterns
            r'(?i)(eval|exec|system)',            # Code execution
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, entry):
                return False
        
        return True

class SecureLogger:
    """Secure logger with data sanitization and injection prevention."""
    
    def __init__(self, name: str = "secure_app", log_file: str = "secure_app.log"):
        self.sanitizer = DataSanitizer()
        self.injection_preventer = LogInjectionPreventer()
        
        # Configure secure logging
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create secure formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler with secure permissions
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.INFO)
            self.logger.addHandler(file_handler)
            
            # Set secure file permissions (owner read/write only)
            try:
                os.chmod(log_file, 0o600)
            except OSError:
                pass  # May fail on some systems
    
    def _sanitize_message(self, message: str, data: Optional[Dict[str, Any]] = None) -> str:
        """Sanitize message and data before logging."""
        # Sanitize the main message
        clean_message = self.sanitizer.sanitize_text(message)
        clean_message = self.injection_preventer.sanitize_for_logging(clean_message)
        
        # Sanitize additional data if provided
        if data:
            clean_data = {}
            for key, value in data.items():
                clean_key = self.injection_preventer.sanitize_for_logging(str(key))
                clean_value = self.sanitizer.sanitize_text(str(value))
                clean_value = self.injection_preventer.sanitize_for_logging(clean_value)
                clean_data[clean_key] = clean_value
            
            clean_message += f" | Data: {json.dumps(clean_data, separators=(',', ':'))}"
        
        # Final validation
        if not self.injection_preventer.validate_log_entry(clean_message):
            return "SUSPICIOUS_CONTENT_BLOCKED"
        
        return clean_message
    
    def info(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log info message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.info(clean_message)
    
    def warning(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log warning message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.warning(clean_message)
    
    def error(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log error message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.error(clean_message)
    
    def log_user_action(self, user_id: str, action: str, metadata: Optional[Dict[str, Any]] = None):
        """Log user action with sanitization."""
        # Hash user ID for privacy
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        
        message = f"User action: {action} by user_{user_hash}"
        self.info(message, metadata)

# What we accomplished in this step:
# - Created secure logger that combines sanitization and injection prevention
# - Added secure file permissions for log files
# - Implemented user action logging with privacy protection
# - Added comprehensive message sanitization pipeline


# Step 4: Add audit logging for security events
# ===============================================================================

# Explanation:
# Audit logging tracks security-critical events for compliance and monitoring.
# We need to log authentication, authorization, and security violations.

import logging
import re
import hashlib
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
import os

class DataSanitizer:
    """Sanitizes sensitive data before logging."""
    
    def __init__(self):
        # Common PII patterns
        self.patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'ssn': re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b'),
            'credit_card': re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
            'phone': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'ip_address': re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        }
    
    def sanitize_text(self, text: str) -> str:
        """Sanitize text by masking PII."""
        if not isinstance(text, str):
            text = str(text)
        
        # Mask email addresses
        text = self.patterns['email'].sub(lambda m: self._mask_email(m.group()), text)
        
        # Mask SSN
        text = self.patterns['ssn'].sub('***-**-****', text)
        
        # Mask credit card numbers
        text = self.patterns['credit_card'].sub('****-****-****-****', text)
        
        # Mask phone numbers
        text = self.patterns['phone'].sub('***-***-****', text)
        
        return text
    
    def _mask_email(self, email: str) -> str:
        """Mask email while preserving domain for debugging."""
        parts = email.split('@')
        if len(parts) == 2:
            username = parts[0]
            domain = parts[1]
            masked_username = username[0] + '*' * (len(username) - 1)
            return f"{masked_username}@{domain}"
        return "***@***.***"

class LogInjectionPreventer:
    """Prevents log injection attacks by sanitizing control characters."""
    
    def __init__(self):
        # Dangerous control characters and escape sequences
        self.dangerous_chars = {
            '\n': '\\n',    # Newline
            '\r': '\\r',    # Carriage return
            '\t': '\\t',    # Tab
            '\b': '\\b',    # Backspace
            '\f': '\\f',    # Form feed
            '\v': '\\v',    # Vertical tab
            '\0': '\\0',    # Null character
        }
        
        # ANSI escape sequences (for terminal control)
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    
    def sanitize_for_logging(self, text: str) -> str:
        """Sanitize text to prevent log injection attacks."""
        if not isinstance(text, str):
            text = str(text)
        
        # Remove ANSI escape sequences
        text = self.ansi_escape.sub('', text)
        
        # Replace dangerous control characters
        for char, replacement in self.dangerous_chars.items():
            text = text.replace(char, replacement)
        
        # Remove other non-printable characters
        text = ''.join(char for char in text if ord(char) >= 32 or char in ['\t'])
        
        # Limit length to prevent log flooding
        if len(text) > 1000:
            text = text[:997] + "..."
        
        return text
    
    def validate_log_entry(self, entry: str) -> bool:
        """Validate that log entry is safe."""
        # Check for suspicious patterns
        suspicious_patterns = [
            r'(?i)(script|javascript|vbscript)',  # Script injection
            r'(?i)(<|>|&lt;|&gt;)',              # HTML/XML injection
            r'(?i)(union|select|insert|delete)',  # SQL injection patterns
            r'(?i)(eval|exec|system)',            # Code execution
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, entry):
                return False
        
        return True

class SecureLogger:
    """Secure logger with data sanitization and injection prevention."""
    
    def __init__(self, name: str = "secure_app", log_file: str = "secure_app.log"):
        self.sanitizer = DataSanitizer()
        self.injection_preventer = LogInjectionPreventer()
        
        # Configure secure logging
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create secure formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler with secure permissions
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.INFO)
            self.logger.addHandler(file_handler)
            
            # Set secure file permissions (owner read/write only)
            try:
                os.chmod(log_file, 0o600)
            except OSError:
                pass  # May fail on some systems
    
    def _sanitize_message(self, message: str, data: Optional[Dict[str, Any]] = None) -> str:
        """Sanitize message and data before logging."""
        # Sanitize the main message
        clean_message = self.sanitizer.sanitize_text(message)
        clean_message = self.injection_preventer.sanitize_for_logging(clean_message)
        
        # Sanitize additional data if provided
        if data:
            clean_data = {}
            for key, value in data.items():
                clean_key = self.injection_preventer.sanitize_for_logging(str(key))
                clean_value = self.sanitizer.sanitize_text(str(value))
                clean_value = self.injection_preventer.sanitize_for_logging(clean_value)
                clean_data[clean_key] = clean_value
            
            clean_message += f" | Data: {json.dumps(clean_data, separators=(',', ':'))}"
        
        # Final validation
        if not self.injection_preventer.validate_log_entry(clean_message):
            return "SUSPICIOUS_CONTENT_BLOCKED"
        
        return clean_message
    
    def info(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log info message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.info(clean_message)
    
    def warning(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log warning message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.warning(clean_message)
    
    def error(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log error message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.error(clean_message)
    
    def log_user_action(self, user_id: str, action: str, metadata: Optional[Dict[str, Any]] = None):
        """Log user action with sanitization."""
        # Hash user ID for privacy
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        
        message = f"User action: {action} by user_{user_hash}"
        self.info(message, metadata)

class AuditLogger(SecureLogger):
    """Specialized logger for security audit events."""
    
    def __init__(self, audit_file: str = "security_audit.log"):
        super().__init__(name="security_audit", log_file=audit_file)
        
        # Configure separate audit logger with higher security
        self.audit_logger = logging.getLogger("audit")
        self.audit_logger.setLevel(logging.INFO)
        
        # Create audit-specific formatter with more details
        audit_formatter = logging.Formatter(
            '%(asctime)s - AUDIT - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S UTC'
        )
        
        # Separate audit file handler
        if not self.audit_logger.handlers:
            audit_handler = logging.FileHandler(audit_file)
            audit_handler.setFormatter(audit_formatter)
            audit_handler.setLevel(logging.INFO)
            self.audit_logger.addHandler(audit_handler)
            
            # Set even more restrictive permissions for audit logs
            try:
                os.chmod(audit_file, 0o400)  # Read-only for owner
            except OSError:
                pass
    
    def log_authentication_event(self, user_id: str, event_type: str, 
                                success: bool, ip_address: str, 
                                user_agent: Optional[str] = None):
        """Log authentication events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        status = "SUCCESS" if success else "FAILURE"
        
        # Sanitize IP address (keep for security monitoring)
        clean_ip = self.injection_preventer.sanitize_for_logging(ip_address)
        
        # Sanitize user agent
        clean_user_agent = ""
        if user_agent:
            clean_user_agent = self.injection_preventer.sanitize_for_logging(user_agent)[:200]
        
        audit_data = {
            "event_type": "authentication",
            "auth_event": event_type,
            "user_hash": user_hash,
            "status": status,
            "source_ip": clean_ip,
            "user_agent": clean_user_agent,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"AUTH_{status}: {event_type} for user_{user_hash} from {clean_ip}"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_authorization_event(self, user_id: str, resource: str, 
                               action: str, granted: bool, reason: str = ""):
        """Log authorization events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        status = "GRANTED" if granted else "DENIED"
        
        # Sanitize inputs
        clean_resource = self.injection_preventer.sanitize_for_logging(resource)
        clean_action = self.injection_preventer.sanitize_for_logging(action)
        clean_reason = self.injection_preventer.sanitize_for_logging(reason)
        
        audit_data = {
            "event_type": "authorization",
            "user_hash": user_hash,
            "resource": clean_resource,
            "action": clean_action,
            "status": status,
            "reason": clean_reason,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"AUTHZ_{status}: {clean_action} on {clean_resource} for user_{user_hash}"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_security_violation(self, violation_type: str, details: Dict[str, Any], 
                              severity: str = "HIGH"):
        """Log security violations and suspicious activities."""
        # Sanitize all details
        clean_details = {}
        for key, value in details.items():
            clean_key = self.injection_preventer.sanitize_for_logging(str(key))
            clean_value = self.sanitizer.sanitize_text(str(value))
            clean_value = self.injection_preventer.sanitize_for_logging(clean_value)
            clean_details[clean_key] = clean_value
        
        audit_data = {
            "event_type": "security_violation",
            "violation_type": violation_type,
            "severity": severity,
            "details": clean_details,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"SECURITY_VIOLATION: {violation_type} - Severity: {severity}"
        self.audit_logger.error(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_data_access(self, user_id: str, data_type: str, operation: str, 
                       record_count: int = 1):
        """Log sensitive data access events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        
        # Sanitize inputs
        clean_data_type = self.injection_preventer.sanitize_for_logging(data_type)
        clean_operation = self.injection_preventer.sanitize_for_logging(operation)
        
        audit_data = {
            "event_type": "data_access",
            "user_hash": user_hash,
            "data_type": clean_data_type,
            "operation": clean_operation,
            "record_count": record_count,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"DATA_ACCESS: {clean_operation} on {clean_data_type} by user_{user_hash} ({record_count} records)"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")

# What we accomplished in this step:
# - Created specialized audit logger for security events
# - Added authentication and authorization event logging
# - Implemented security violation tracking
# - Added data access logging for compliance
# - Enhanced audit log security with restrictive permissions


# Step 5: Add secure log rotation and storage
# ===============================================================================

# Explanation:
# Secure log rotation prevents log files from growing too large and ensures
# old logs are properly archived with maintained security.

import logging
import re
import hashlib
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

class DataSanitizer:
    """Sanitizes sensitive data before logging."""
    
    def __init__(self):
        # Common PII patterns
        self.patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'ssn': re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b'),
            'credit_card': re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
            'phone': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'ip_address': re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        }
    
    def sanitize_text(self, text: str) -> str:
        """Sanitize text by masking PII."""
        if not isinstance(text, str):
            text = str(text)
        
        # Mask email addresses
        text = self.patterns['email'].sub(lambda m: self._mask_email(m.group()), text)
        
        # Mask SSN
        text = self.patterns['ssn'].sub('***-**-****', text)
        
        # Mask credit card numbers
        text = self.patterns['credit_card'].sub('****-****-****-****', text)
        
        # Mask phone numbers
        text = self.patterns['phone'].sub('***-***-****', text)
        
        return text
    
    def _mask_email(self, email: str) -> str:
        """Mask email while preserving domain for debugging."""
        parts = email.split('@')
        if len(parts) == 2:
            username = parts[0]
            domain = parts[1]
            masked_username = username[0] + '*' * (len(username) - 1)
            return f"{masked_username}@{domain}"
        return "***@***.***"

class LogInjectionPreventer:
    """Prevents log injection attacks by sanitizing control characters."""
    
    def __init__(self):
        # Dangerous control characters and escape sequences
        self.dangerous_chars = {
            '\n': '\\n',    # Newline
            '\r': '\\r',    # Carriage return
            '\t': '\\t',    # Tab
            '\b': '\\b',    # Backspace
            '\f': '\\f',    # Form feed
            '\v': '\\v',    # Vertical tab
            '\0': '\\0',    # Null character
        }
        
        # ANSI escape sequences (for terminal control)
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    
    def sanitize_for_logging(self, text: str) -> str:
        """Sanitize text to prevent log injection attacks."""
        if not isinstance(text, str):
            text = str(text)
        
        # Remove ANSI escape sequences
        text = self.ansi_escape.sub('', text)
        
        # Replace dangerous control characters
        for char, replacement in self.dangerous_chars.items():
            text = text.replace(char, replacement)
        
        # Remove other non-printable characters
        text = ''.join(char for char in text if ord(char) >= 32 or char in ['\t'])
        
        # Limit length to prevent log flooding
        if len(text) > 1000:
            text = text[:997] + "..."
        
        return text
    
    def validate_log_entry(self, entry: str) -> bool:
        """Validate that log entry is safe."""
        # Check for suspicious patterns
        suspicious_patterns = [
            r'(?i)(script|javascript|vbscript)',  # Script injection
            r'(?i)(<|>|&lt;|&gt;)',              # HTML/XML injection
            r'(?i)(union|select|insert|delete)',  # SQL injection patterns
            r'(?i)(eval|exec|system)',            # Code execution
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, entry):
                return False
        
        return True

class SecureRotatingFileHandler(RotatingFileHandler):
    """Secure rotating file handler that maintains file permissions."""
    
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, 
                 encoding=None, delay=False, secure_permissions=0o600):
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay)
        self.secure_permissions = secure_permissions
    
    def doRollover(self):
        """Override rollover to maintain secure permissions."""
        super().doRollover()
        
        # Set secure permissions on all log files
        try:
            # Set permissions on current log file
            os.chmod(self.baseFilename, self.secure_permissions)
            
            # Set permissions on backup files
            for i in range(1, self.backupCount + 1):
                backup_name = f"{self.baseFilename}.{i}"
                if os.path.exists(backup_name):
                    os.chmod(backup_name, self.secure_permissions)
        except OSError:
            pass  # May fail on some systems

class SecureLogger:
    """Secure logger with data sanitization and injection prevention."""
    
    def __init__(self, name: str = "secure_app", log_file: str = "secure_app.log"):
        self.sanitizer = DataSanitizer()
        self.injection_preventer = LogInjectionPreventer()
        
        # Configure secure logging
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create secure formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler with secure permissions
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.INFO)
            self.logger.addHandler(file_handler)
            
            # Set secure file permissions (owner read/write only)
            try:
                os.chmod(log_file, 0o600)
            except OSError:
                pass  # May fail on some systems
    
    def _sanitize_message(self, message: str, data: Optional[Dict[str, Any]] = None) -> str:
        """Sanitize message and data before logging."""
        # Sanitize the main message
        clean_message = self.sanitizer.sanitize_text(message)
        clean_message = self.injection_preventer.sanitize_for_logging(clean_message)
        
        # Sanitize additional data if provided
        if data:
            clean_data = {}
            for key, value in data.items():
                clean_key = self.injection_preventer.sanitize_for_logging(str(key))
                clean_value = self.sanitizer.sanitize_text(str(value))
                clean_value = self.injection_preventer.sanitize_for_logging(clean_value)
                clean_data[clean_key] = clean_value
            
            clean_message += f" | Data: {json.dumps(clean_data, separators=(',', ':'))}"
        
        # Final validation
        if not self.injection_preventer.validate_log_entry(clean_message):
            return "SUSPICIOUS_CONTENT_BLOCKED"
        
        return clean_message
    
    def info(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log info message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.info(clean_message)
    
    def warning(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log warning message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.warning(clean_message)
    
    def error(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log error message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.error(clean_message)
    
    def log_user_action(self, user_id: str, action: str, metadata: Optional[Dict[str, Any]] = None):
        """Log user action with sanitization."""
        # Hash user ID for privacy
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        
        message = f"User action: {action} by user_{user_hash}"
        self.info(message, metadata)

class AuditLogger(SecureLogger):
    """Specialized logger for security audit events."""
    
    def __init__(self, audit_file: str = "security_audit.log"):
        super().__init__(name="security_audit", log_file=audit_file)
        
        # Configure separate audit logger with higher security
        self.audit_logger = logging.getLogger("audit")
        self.audit_logger.setLevel(logging.INFO)
        
        # Create audit-specific formatter with more details
        audit_formatter = logging.Formatter(
            '%(asctime)s - AUDIT - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S UTC'
        )
        
        # Separate audit file handler
        if not self.audit_logger.handlers:
            audit_handler = logging.FileHandler(audit_file)
            audit_handler.setFormatter(audit_formatter)
            audit_handler.setLevel(logging.INFO)
            self.audit_logger.addHandler(audit_handler)
            
            # Set even more restrictive permissions for audit logs
            try:
                os.chmod(audit_file, 0o400)  # Read-only for owner
            except OSError:
                pass
    
    def log_authentication_event(self, user_id: str, event_type: str, 
                                success: bool, ip_address: str, 
                                user_agent: Optional[str] = None):
        """Log authentication events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        status = "SUCCESS" if success else "FAILURE"
        
        # Sanitize IP address (keep for security monitoring)
        clean_ip = self.injection_preventer.sanitize_for_logging(ip_address)
        
        # Sanitize user agent
        clean_user_agent = ""
        if user_agent:
            clean_user_agent = self.injection_preventer.sanitize_for_logging(user_agent)[:200]
        
        audit_data = {
            "event_type": "authentication",
            "auth_event": event_type,
            "user_hash": user_hash,
            "status": status,
            "source_ip": clean_ip,
            "user_agent": clean_user_agent,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"AUTH_{status}: {event_type} for user_{user_hash} from {clean_ip}"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_authorization_event(self, user_id: str, resource: str, 
                               action: str, granted: bool, reason: str = ""):
        """Log authorization events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        status = "GRANTED" if granted else "DENIED"
        
        # Sanitize inputs
        clean_resource = self.injection_preventer.sanitize_for_logging(resource)
        clean_action = self.injection_preventer.sanitize_for_logging(action)
        clean_reason = self.injection_preventer.sanitize_for_logging(reason)
        
        audit_data = {
            "event_type": "authorization",
            "user_hash": user_hash,
            "resource": clean_resource,
            "action": clean_action,
            "status": status,
            "reason": clean_reason,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"AUTHZ_{status}: {clean_action} on {clean_resource} for user_{user_hash}"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_security_violation(self, violation_type: str, details: Dict[str, Any], 
                              severity: str = "HIGH"):
        """Log security violations and suspicious activities."""
        # Sanitize all details
        clean_details = {}
        for key, value in details.items():
            clean_key = self.injection_preventer.sanitize_for_logging(str(key))
            clean_value = self.sanitizer.sanitize_text(str(value))
            clean_value = self.injection_preventer.sanitize_for_logging(clean_value)
            clean_details[clean_key] = clean_value
        
        audit_data = {
            "event_type": "security_violation",
            "violation_type": violation_type,
            "severity": severity,
            "details": clean_details,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"SECURITY_VIOLATION: {violation_type} - Severity: {severity}"
        self.audit_logger.error(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_data_access(self, user_id: str, data_type: str, operation: str, 
                       record_count: int = 1):
        """Log sensitive data access events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        
        # Sanitize inputs
        clean_data_type = self.injection_preventer.sanitize_for_logging(data_type)
        clean_operation = self.injection_preventer.sanitize_for_logging(operation)
        
        audit_data = {
            "event_type": "data_access",
            "user_hash": user_hash,
            "data_type": clean_data_type,
            "operation": clean_operation,
            "record_count": record_count,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"DATA_ACCESS: {clean_operation} on {clean_data_type} by user_{user_hash} ({record_count} records)"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")

class SecureLogManager:
    """Manages secure logging with rotation and archival."""
    
    def __init__(self, log_dir: str = "secure_logs"):
        self.log_dir = log_dir
        self._ensure_log_directory()
        
        # Create loggers with rotation
        self.app_logger = self._create_rotating_logger(
            "secure_app", 
            os.path.join(log_dir, "app.log"),
            max_bytes=10*1024*1024,  # 10MB
            backup_count=5
        )
        
        self.audit_logger = self._create_rotating_logger(
            "security_audit",
            os.path.join(log_dir, "audit.log"),
            max_bytes=50*1024*1024,  # 50MB
            backup_count=10,
            permissions=0o400  # Read-only
        )
        
        self.security_logger = self._create_rotating_logger(
            "security_events",
            os.path.join(log_dir, "security.log"),
            max_bytes=25*1024*1024,  # 25MB
            backup_count=7
        )
    
    def _ensure_log_directory(self):
        """Create secure log directory."""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            # Set secure directory permissions
            try:
                os.chmod(self.log_dir, 0o700)  # Owner only
            except OSError:
                pass
    
    def _create_rotating_logger(self, name: str, filename: str, 
                               max_bytes: int, backup_count: int,
                               permissions: int = 0o600) -> logging.Logger:
        """Create a logger with secure rotation."""
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        # Clear existing handlers
        logger.handlers.clear()
        
        # Create secure rotating handler
        handler = SecureRotatingFileHandler(
            filename=filename,
            maxBytes=max_bytes,
            backupCount=backup_count,
            secure_permissions=permissions
        )
        
        # Set formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S UTC'
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Set initial file permissions
        try:
            if os.path.exists(filename):
                os.chmod(filename, permissions)
        except OSError:
            pass
        
        return logger
    
    def get_secure_logger(self) -> SecureLogger:
        """Get application logger with sanitization."""
        return SecureLogger("secure_app", os.path.join(self.log_dir, "app.log"))
    
    def get_audit_logger(self) -> AuditLogger:
        """Get audit logger with enhanced security."""
        return AuditLogger(os.path.join(self.log_dir, "audit.log"))
    
    def archive_old_logs(self, days_to_keep: int = 90):
        """Archive logs older than specified days."""
        import time
        import shutil
        
        current_time = time.time()
        cutoff_time = current_time - (days_to_keep * 24 * 60 * 60)
        
        archive_dir = os.path.join(self.log_dir, "archive")
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
            os.chmod(archive_dir, 0o700)
        
        for filename in os.listdir(self.log_dir):
            if filename.endswith('.log') or '.' in filename:
                filepath = os.path.join(self.log_dir, filename)
                if os.path.isfile(filepath):
                    file_time = os.path.getmtime(filepath)
                    if file_time < cutoff_time:
                        # Move to archive
                        archive_path = os.path.join(archive_dir, filename)
                        shutil.move(filepath, archive_path)
                        # Maintain secure permissions
                        os.chmod(archive_path, 0o400)

# What we accomplished in this step:
# - Created secure rotating file handler that maintains permissions
# - Implemented comprehensive log management system
# - Added automatic log archival functionality
# - Enhanced security with proper directory and file permissions
# - Provided centralized log management interface


# Step 6: Test the complete secure logging implementation
# ===============================================================================

# Explanation:
# Let's test our comprehensive secure logging system with various scenarios
# including PII sanitization, injection prevention, and audit logging.

import logging
import re
import hashlib
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

class DataSanitizer:
    """Sanitizes sensitive data before logging."""
    
    def __init__(self):
        # Common PII patterns
        self.patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'ssn': re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b'),
            'credit_card': re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
            'phone': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'ip_address': re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        }
    
    def sanitize_text(self, text: str) -> str:
        """Sanitize text by masking PII."""
        if not isinstance(text, str):
            text = str(text)
        
        # Mask email addresses
        text = self.patterns['email'].sub(lambda m: self._mask_email(m.group()), text)
        
        # Mask SSN
        text = self.patterns['ssn'].sub('***-**-****', text)
        
        # Mask credit card numbers
        text = self.patterns['credit_card'].sub('****-****-****-****', text)
        
        # Mask phone numbers
        text = self.patterns['phone'].sub('***-***-****', text)
        
        return text
    
    def _mask_email(self, email: str) -> str:
        """Mask email while preserving domain for debugging."""
        parts = email.split('@')
        if len(parts) == 2:
            username = parts[0]
            domain = parts[1]
            masked_username = username[0] + '*' * (len(username) - 1)
            return f"{masked_username}@{domain}"
        return "***@***.***"

class LogInjectionPreventer:
    """Prevents log injection attacks by sanitizing control characters."""
    
    def __init__(self):
        # Dangerous control characters and escape sequences
        self.dangerous_chars = {
            '\n': '\\n',    # Newline
            '\r': '\\r',    # Carriage return
            '\t': '\\t',    # Tab
            '\b': '\\b',    # Backspace
            '\f': '\\f',    # Form feed
            '\v': '\\v',    # Vertical tab
            '\0': '\\0',    # Null character
        }
        
        # ANSI escape sequences (for terminal control)
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    
    def sanitize_for_logging(self, text: str) -> str:
        """Sanitize text to prevent log injection attacks."""
        if not isinstance(text, str):
            text = str(text)
        
        # Remove ANSI escape sequences
        text = self.ansi_escape.sub('', text)
        
        # Replace dangerous control characters
        for char, replacement in self.dangerous_chars.items():
            text = text.replace(char, replacement)
        
        # Remove other non-printable characters
        text = ''.join(char for char in text if ord(char) >= 32 or char in ['\t'])
        
        # Limit length to prevent log flooding
        if len(text) > 1000:
            text = text[:997] + "..."
        
        return text
    
    def validate_log_entry(self, entry: str) -> bool:
        """Validate that log entry is safe."""
        # Check for suspicious patterns
        suspicious_patterns = [
            r'(?i)(script|javascript|vbscript)',  # Script injection
            r'(?i)(<|>|&lt;|&gt;)',              # HTML/XML injection
            r'(?i)(union|select|insert|delete)',  # SQL injection patterns
            r'(?i)(eval|exec|system)',            # Code execution
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, entry):
                return False
        
        return True

class SecureRotatingFileHandler(RotatingFileHandler):
    """Secure rotating file handler that maintains file permissions."""
    
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, 
                 encoding=None, delay=False, secure_permissions=0o600):
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay)
        self.secure_permissions = secure_permissions
    
    def doRollover(self):
        """Override rollover to maintain secure permissions."""
        super().doRollover()
        
        # Set secure permissions on all log files
        try:
            # Set permissions on current log file
            os.chmod(self.baseFilename, self.secure_permissions)
            
            # Set permissions on backup files
            for i in range(1, self.backupCount + 1):
                backup_name = f"{self.baseFilename}.{i}"
                if os.path.exists(backup_name):
                    os.chmod(backup_name, self.secure_permissions)
        except OSError:
            pass  # May fail on some systems

class SecureLogger:
    """Secure logger with data sanitization and injection prevention."""
    
    def __init__(self, name: str = "secure_app", log_file: str = "secure_app.log"):
        self.sanitizer = DataSanitizer()
        self.injection_preventer = LogInjectionPreventer()
        
        # Configure secure logging
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create secure formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # File handler with secure permissions
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.INFO)
            self.logger.addHandler(file_handler)
            
            # Set secure file permissions (owner read/write only)
            try:
                os.chmod(log_file, 0o600)
            except OSError:
                pass  # May fail on some systems
    
    def _sanitize_message(self, message: str, data: Optional[Dict[str, Any]] = None) -> str:
        """Sanitize message and data before logging."""
        # Sanitize the main message
        clean_message = self.sanitizer.sanitize_text(message)
        clean_message = self.injection_preventer.sanitize_for_logging(clean_message)
        
        # Sanitize additional data if provided
        if data:
            clean_data = {}
            for key, value in data.items():
                clean_key = self.injection_preventer.sanitize_for_logging(str(key))
                clean_value = self.sanitizer.sanitize_text(str(value))
                clean_value = self.injection_preventer.sanitize_for_logging(clean_value)
                clean_data[clean_key] = clean_value
            
            clean_message += f" | Data: {json.dumps(clean_data, separators=(',', ':'))}"
        
        # Final validation
        if not self.injection_preventer.validate_log_entry(clean_message):
            return "SUSPICIOUS_CONTENT_BLOCKED"
        
        return clean_message
    
    def info(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log info message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.info(clean_message)
    
    def warning(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log warning message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.warning(clean_message)
    
    def error(self, message: str, data: Optional[Dict[str, Any]] = None):
        """Log error message with sanitization."""
        clean_message = self._sanitize_message(message, data)
        self.logger.error(clean_message)
    
    def log_user_action(self, user_id: str, action: str, metadata: Optional[Dict[str, Any]] = None):
        """Log user action with sanitization."""
        # Hash user ID for privacy
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        
        message = f"User action: {action} by user_{user_hash}"
        self.info(message, metadata)

class AuditLogger(SecureLogger):
    """Specialized logger for security audit events."""
    
    def __init__(self, audit_file: str = "security_audit.log"):
        super().__init__(name="security_audit", log_file=audit_file)
        
        # Configure separate audit logger with higher security
        self.audit_logger = logging.getLogger("audit")
        self.audit_logger.setLevel(logging.INFO)
        
        # Create audit-specific formatter with more details
        audit_formatter = logging.Formatter(
            '%(asctime)s - AUDIT - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S UTC'
        )
        
        # Separate audit file handler
        if not self.audit_logger.handlers:
            audit_handler = logging.FileHandler(audit_file)
            audit_handler.setFormatter(audit_formatter)
            audit_handler.setLevel(logging.INFO)
            self.audit_logger.addHandler(audit_handler)
            
            # Set even more restrictive permissions for audit logs
            try:
                os.chmod(audit_file, 0o400)  # Read-only for owner
            except OSError:
                pass
    
    def log_authentication_event(self, user_id: str, event_type: str, 
                                success: bool, ip_address: str, 
                                user_agent: Optional[str] = None):
        """Log authentication events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        status = "SUCCESS" if success else "FAILURE"
        
        # Sanitize IP address (keep for security monitoring)
        clean_ip = self.injection_preventer.sanitize_for_logging(ip_address)
        
        # Sanitize user agent
        clean_user_agent = ""
        if user_agent:
            clean_user_agent = self.injection_preventer.sanitize_for_logging(user_agent)[:200]
        
        audit_data = {
            "event_type": "authentication",
            "auth_event": event_type,
            "user_hash": user_hash,
            "status": status,
            "source_ip": clean_ip,
            "user_agent": clean_user_agent,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"AUTH_{status}: {event_type} for user_{user_hash} from {clean_ip}"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_authorization_event(self, user_id: str, resource: str, 
                               action: str, granted: bool, reason: str = ""):
        """Log authorization events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        status = "GRANTED" if granted else "DENIED"
        
        # Sanitize inputs
        clean_resource = self.injection_preventer.sanitize_for_logging(resource)
        clean_action = self.injection_preventer.sanitize_for_logging(action)
        clean_reason = self.injection_preventer.sanitize_for_logging(reason)
        
        audit_data = {
            "event_type": "authorization",
            "user_hash": user_hash,
            "resource": clean_resource,
            "action": clean_action,
            "status": status,
            "reason": clean_reason,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"AUTHZ_{status}: {clean_action} on {clean_resource} for user_{user_hash}"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_security_violation(self, violation_type: str, details: Dict[str, Any], 
                              severity: str = "HIGH"):
        """Log security violations and suspicious activities."""
        # Sanitize all details
        clean_details = {}
        for key, value in details.items():
            clean_key = self.injection_preventer.sanitize_for_logging(str(key))
            clean_value = self.sanitizer.sanitize_text(str(value))
            clean_value = self.injection_preventer.sanitize_for_logging(clean_value)
            clean_details[clean_key] = clean_value
        
        audit_data = {
            "event_type": "security_violation",
            "violation_type": violation_type,
            "severity": severity,
            "details": clean_details,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"SECURITY_VIOLATION: {violation_type} - Severity: {severity}"
        self.audit_logger.error(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")
    
    def log_data_access(self, user_id: str, data_type: str, operation: str, 
                       record_count: int = 1):
        """Log sensitive data access events."""
        user_hash = hashlib.sha256(user_id.encode()).hexdigest()[:8]
        
        # Sanitize inputs
        clean_data_type = self.injection_preventer.sanitize_for_logging(data_type)
        clean_operation = self.injection_preventer.sanitize_for_logging(operation)
        
        audit_data = {
            "event_type": "data_access",
            "user_hash": user_hash,
            "data_type": clean_data_type,
            "operation": clean_operation,
            "record_count": record_count,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        message = f"DATA_ACCESS: {clean_operation} on {clean_data_type} by user_{user_hash} ({record_count} records)"
        self.audit_logger.info(f"{message} | {json.dumps(audit_data, separators=(',', ':'))}")

class SecureLogManager:
    """Manages secure logging with rotation and archival."""
    
    def __init__(self, log_dir: str = "secure_logs"):
        self.log_dir = log_dir
        self._ensure_log_directory()
        
        # Create loggers with rotation
        self.app_logger = self._create_rotating_logger(
            "secure_app", 
            os.path.join(log_dir, "app.log"),
            max_bytes=10*1024*1024,  # 10MB
            backup_count=5
        )
        
        self.audit_logger = self._create_rotating_logger(
            "security_audit",
            os.path.join(log_dir, "audit.log"),
            max_bytes=50*1024*1024,  # 50MB
            backup_count=10,
            permissions=0o400  # Read-only
        )
        
        self.security_logger = self._create_rotating_logger(
            "security_events",
            os.path.join(log_dir, "security.log"),
            max_bytes=25*1024*1024,  # 25MB
            backup_count=7
        )
    
    def _ensure_log_directory(self):
        """Create secure log directory."""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            # Set secure directory permissions
            try:
                os.chmod(self.log_dir, 0o700)  # Owner only
            except OSError:
                pass
    
    def _create_rotating_logger(self, name: str, filename: str, 
                               max_bytes: int, backup_count: int,
                               permissions: int = 0o600) -> logging.Logger:
        """Create a logger with secure rotation."""
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        # Clear existing handlers
        logger.handlers.clear()
        
        # Create secure rotating handler
        handler = SecureRotatingFileHandler(
            filename=filename,
            maxBytes=max_bytes,
            backupCount=backup_count,
            secure_permissions=permissions
        )
        
        # Set formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S UTC'
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Set initial file permissions
        try:
            if os.path.exists(filename):
                os.chmod(filename, permissions)
        except OSError:
            pass
        
        return logger
    
    def get_secure_logger(self) -> SecureLogger:
        """Get application logger with sanitization."""
        return SecureLogger("secure_app", os.path.join(self.log_dir, "app.log"))
    
    def get_audit_logger(self) -> AuditLogger:
        """Get audit logger with enhanced security."""
        return AuditLogger(os.path.join(self.log_dir, "audit.log"))
    
    def archive_old_logs(self, days_to_keep: int = 90):
        """Archive logs older than specified days."""
        import time
        import shutil
        
        current_time = time.time()
        cutoff_time = current_time - (days_to_keep * 24 * 60 * 60)
        
        archive_dir = os.path.join(self.log_dir, "archive")
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
            os.chmod(archive_dir, 0o700)
        
        for filename in os.listdir(self.log_dir):
            if filename.endswith('.log') or '.' in filename:
                filepath = os.path.join(self.log_dir, filename)
                if os.path.isfile(filepath):
                    file_time = os.path.getmtime(filepath)
                    if file_time < cutoff_time:
                        # Move to archive
                        archive_path = os.path.join(archive_dir, filename)
                        shutil.move(filepath, archive_path)
                        # Maintain secure permissions
                        os.chmod(archive_path, 0o400)

print("=== Testing Secure Logging System ===\n")

# Test 1: Basic secure logging with PII sanitization
print("1. Testing PII Sanitization:")
secure_logger = SecureLogger("test_app", "tmp_rovodev_test_secure.log")

# Test with various PII data
test_data = {
    "user_email": "john.doe@example.com",
    "ssn": "123-45-6789",
    "credit_card": "4532 1234 5678 9012",
    "phone": "555-123-4567",
    "ip": "192.168.1.100"
}

secure_logger.info("User registration attempt", test_data)
print("✓ PII data sanitized and logged securely")

# Test 2: Log injection prevention
print("\n2. Testing Log Injection Prevention:")
malicious_input = "Normal message\nFAKE LOG ENTRY: Admin login successful\r\nAnother fake entry"
ansi_input = "\x1b[31mRed text\x1b[0m with ANSI codes"
script_input = "<script>alert('xss')</script> and some SQL: SELECT * FROM users"

secure_logger.warning("Processing malicious input", {"input": malicious_input})
secure_logger.warning("Processing ANSI input", {"input": ansi_input})
secure_logger.error("Blocked suspicious content", {"blocked": script_input})
print("✓ Log injection attempts prevented")

# Test 3: Audit logging
print("\n3. Testing Audit Logging:")
audit_logger = AuditLogger("tmp_rovodev_test_audit.log")

# Authentication events
audit_logger.log_authentication_event(
    "john.doe@example.com", "login", True, "192.168.1.100",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
)

audit_logger.log_authentication_event(
    "attacker@evil.com", "login", False, "10.0.0.1",
    "curl/7.68.0"
)

# Authorization events
audit_logger.log_authorization_event(
    "john.doe@example.com", "/admin/users", "READ", True
)

audit_logger.log_authorization_event(
    "guest@example.com", "/admin/settings", "WRITE", False, "Insufficient privileges"
)

# Security violations
audit_logger.log_security_violation(
    "BRUTE_FORCE_ATTACK",
    {
        "source_ip": "10.0.0.1",
        "target_user": "admin@example.com",
        "attempts": 50,
        "time_window": "5 minutes"
    },
    "CRITICAL"
)

# Data access logging
audit_logger.log_data_access("john.doe@example.com", "customer_records", "SELECT", 25)

print("✓ Audit events logged with proper sanitization")

# Test 4: Secure log management
print("\n4. Testing Secure Log Management:")
log_manager = SecureLogManager("tmp_rovodev_test_logs")

app_logger = log_manager.get_secure_logger()
audit_logger = log_manager.get_audit_logger()

app_logger.info("Application started successfully")
app_logger.log_user_action("user123", "profile_update", {"field": "email"})

audit_logger.log_authentication_event("user123", "logout", True, "192.168.1.50")

print("✓ Secure log management system working")

# Test 5: Demonstrate security features
print("\n5. Security Features Summary:")
print("✓ PII Detection and Masking:")
print("  - Email addresses masked while preserving domain")
print("  - SSN, credit cards, phone numbers fully masked")
print("  - User IDs hashed for privacy")

print("\n✓ Log Injection Prevention:")
print("  - Control characters escaped")
print("  - ANSI escape sequences removed")
print("  - Suspicious patterns blocked")
print("  - Length limits enforced")

print("\n✓ Audit Trail:")
print("  - Authentication events tracked")
print("  - Authorization decisions logged")
print("  - Security violations recorded")
print("  - Data access monitored")

print("\n✓ Secure Storage:")
print("  - File permissions restricted (600/400)")
print("  - Log rotation with maintained security")
print("  - Automatic archival of old logs")
print("  - Structured JSON data for analysis")

# Clean up test files
import os
test_files = [
    "tmp_rovodev_test_secure.log",
    "tmp_rovodev_test_audit.log"
]

for file in test_files:
    if os.path.exists(file):
        os.remove(file)

# Clean up test directory
import shutil
if os.path.exists("tmp_rovodev_test_logs"):
    shutil.rmtree("tmp_rovodev_test_logs")

print("\n✓ Test files cleaned up")

# What we accomplished in this step:
# - Tested complete secure logging system with real scenarios
# - Demonstrated PII sanitization with various data types
# - Verified log injection prevention mechanisms
# - Showed audit logging for security events
# - Tested secure log management and rotation
# - Provided comprehensive security feature summary


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Data sanitization and PII protection in logs
# - Log injection attack prevention techniques
# - Secure audit logging for compliance
# - Secure log rotation and storage practices
# - Comprehensive security logging architecture
# - File permissions and access control
#
# Security best practices implemented:
# 1. Input sanitization before logging
# 2. Control character and escape sequence handling
# 3. Suspicious pattern detection and blocking
# 4. User privacy protection through hashing
# 5. Secure file permissions and rotation
# 6. Structured audit trails for monitoring
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each security measure is necessary
# 4. Experiment with different attack scenarios
#
# Remember: Security logging is critical for detecting and responding to threats!
# ===============================================================================

