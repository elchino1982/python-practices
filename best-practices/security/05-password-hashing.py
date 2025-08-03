"""Question: Implement secure password hashing and verification using modern cryptographic techniques.

Create a comprehensive password security system that demonstrates proper hashing,
salting, and verification practices.

Requirements:
1. Create a PasswordHasher class with secure hashing methods
2. Implement different hashing algorithms (bcrypt, scrypt, argon2)
3. Create password strength validation
4. Implement secure password verification
5. Demonstrate timing attack resistance

Example usage:
    hasher = PasswordHasher()
    hashed = hasher.hash_password("my_secure_password")
    is_valid = hasher.verify_password("my_secure_password", hashed)
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what security principles you need to implement
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
# - What makes a password hash secure?
# - Why do we need salts?
# - How to prevent timing attacks?
# - What are the differences between hashing algorithms?
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


# Step 1: Import modules and create basic password validation
# ===============================================================================

# Explanation:
# Password security starts with basic validation. We need to ensure passwords
# meet minimum security requirements before we even hash them.

import hashlib
import secrets
import re
from typing import Optional, Dict, Any

class PasswordValidator:
    """Validates password strength and security requirements."""
    
    def __init__(self, min_length: int = 8):
        self.min_length = min_length
    
    def validate_password(self, password: str) -> Dict[str, Any]:
        """Validate password strength and return detailed results."""
        results = {
            'is_valid': True,
            'score': 0,
            'issues': [],
            'suggestions': []
        }
        
        # Check minimum length
        if len(password) < self.min_length:
            results['is_valid'] = False
            results['issues'].append(f'Password must be at least {self.min_length} characters long')
            results['suggestions'].append('Use a longer password')
        else:
            results['score'] += 1
        
        # Check for uppercase letters
        if not re.search(r'[A-Z]', password):
            results['issues'].append('Password should contain uppercase letters')
            results['suggestions'].append('Add uppercase letters (A-Z)')
        else:
            results['score'] += 1
        
        # Check for lowercase letters
        if not re.search(r'[a-z]', password):
            results['issues'].append('Password should contain lowercase letters')
            results['suggestions'].append('Add lowercase letters (a-z)')
        else:
            results['score'] += 1
        
        # Check for numbers
        if not re.search(r'\d', password):
            results['issues'].append('Password should contain numbers')
            results['suggestions'].append('Add numbers (0-9)')
        else:
            results['score'] += 1
        
        # Check for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            results['issues'].append('Password should contain special characters')
            results['suggestions'].append('Add special characters (!@#$%^&*)')
        else:
            results['score'] += 1
        
        # Check for common patterns
        if self._has_common_patterns(password):
            results['issues'].append('Password contains common patterns')
            results['suggestions'].append('Avoid sequential characters or repeated patterns')
        
        return results
    
    def _has_common_patterns(self, password: str) -> bool:
        """Check for common weak patterns in passwords."""
        password_lower = password.lower()
        
        # Check for sequential characters
        sequences = ['123', 'abc', 'qwe', 'asd', 'zxc']
        for seq in sequences:
            if seq in password_lower:
                return True
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            return True
        
        return False

# What we accomplished in this step:
# - Created password validation with strength checking
# - Implemented common security requirements
# - Added pattern detection for weak passwords


# Step 2: Create basic password hasher with salt generation
# ===============================================================================

# Explanation:
# Now we'll create a basic password hasher that uses proper salting.
# Salts prevent rainbow table attacks and ensure unique hashes for identical passwords.

import hashlib
import secrets
import re
from typing import Optional, Dict, Any

class PasswordValidator:
    """Validates password strength and security requirements."""
    
    def __init__(self, min_length: int = 8):
        self.min_length = min_length
    
    def validate_password(self, password: str) -> Dict[str, Any]:
        """Validate password strength and return detailed results."""
        results = {
            'is_valid': True,
            'score': 0,
            'issues': [],
            'suggestions': []
        }
        
        # Check minimum length
        if len(password) < self.min_length:
            results['is_valid'] = False
            results['issues'].append(f'Password must be at least {self.min_length} characters long')
            results['suggestions'].append('Use a longer password')
        else:
            results['score'] += 1
        
        # Check for uppercase letters
        if not re.search(r'[A-Z]', password):
            results['issues'].append('Password should contain uppercase letters')
            results['suggestions'].append('Add uppercase letters (A-Z)')
        else:
            results['score'] += 1
        
        # Check for lowercase letters
        if not re.search(r'[a-z]', password):
            results['issues'].append('Password should contain lowercase letters')
            results['suggestions'].append('Add lowercase letters (a-z)')
        else:
            results['score'] += 1
        
        # Check for numbers
        if not re.search(r'\d', password):
            results['issues'].append('Password should contain numbers')
            results['suggestions'].append('Add numbers (0-9)')
        else:
            results['score'] += 1
        
        # Check for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            results['issues'].append('Password should contain special characters')
            results['suggestions'].append('Add special characters (!@#$%^&*)')
        else:
            results['score'] += 1
        
        # Check for common patterns
        if self._has_common_patterns(password):
            results['issues'].append('Password contains common patterns')
            results['suggestions'].append('Avoid sequential characters or repeated patterns')
        
        return results
    
    def _has_common_patterns(self, password: str) -> bool:
        """Check for common weak patterns in passwords."""
        password_lower = password.lower()
        
        # Check for sequential characters
        sequences = ['123', 'abc', 'qwe', 'asd', 'zxc']
        for seq in sequences:
            if seq in password_lower:
                return True
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            return True
        
        return False

class BasicPasswordHasher:
    """Basic password hasher using PBKDF2 with SHA-256."""
    
    def __init__(self, iterations: int = 100000):
        self.iterations = iterations
        self.validator = PasswordValidator()
    
    def generate_salt(self, length: int = 32) -> bytes:
        """Generate a cryptographically secure random salt."""
        return secrets.token_bytes(length)
    
    def hash_password(self, password: str, salt: Optional[bytes] = None) -> str:
        """Hash a password with salt using PBKDF2."""
        # Validate password first
        validation = self.validator.validate_password(password)
        if not validation['is_valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['issues'])}")
        
        # Generate salt if not provided
        if salt is None:
            salt = self.generate_salt()
        
        # Hash the password
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            self.iterations
        )
        
        # Combine salt and hash for storage
        # Format: iterations:salt:hash (all base64 encoded)
        import base64
        salt_b64 = base64.b64encode(salt).decode('ascii')
        hash_b64 = base64.b64encode(password_hash).decode('ascii')
        
        return f"{self.iterations}:{salt_b64}:{hash_b64}"
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a stored hash."""
        try:
            # Parse the stored hash
            parts = stored_hash.split(':')
            if len(parts) != 3:
                return False
            
            iterations = int(parts[0])
            salt = base64.b64decode(parts[1])
            stored_password_hash = base64.b64decode(parts[2])
            
            # Hash the provided password with the same salt and iterations
            password_hash = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                iterations
            )
            
            # Compare hashes using constant-time comparison
            return secrets.compare_digest(password_hash, stored_password_hash)
            
        except (ValueError, TypeError):
            return False

# What we accomplished in this step:
# - Created basic password hasher with PBKDF2
# - Implemented proper salt generation and storage
# - Added constant-time comparison to prevent timing attacks
# - Integrated password validation before hashing


# Step 3: Add bcrypt support for stronger password hashing
# ===============================================================================

# Explanation:
# Bcrypt is specifically designed for password hashing and includes adaptive cost.
# It's slower than PBKDF2 but provides better security against brute force attacks.

import hashlib
import secrets
import re
import base64
from typing import Optional, Dict, Any

class PasswordValidator:
    """Validates password strength and security requirements."""
    
    def __init__(self, min_length: int = 8):
        self.min_length = min_length
    
    def validate_password(self, password: str) -> Dict[str, Any]:
        """Validate password strength and return detailed results."""
        results = {
            'is_valid': True,
            'score': 0,
            'issues': [],
            'suggestions': []
        }
        
        # Check minimum length
        if len(password) < self.min_length:
            results['is_valid'] = False
            results['issues'].append(f'Password must be at least {self.min_length} characters long')
            results['suggestions'].append('Use a longer password')
        else:
            results['score'] += 1
        
        # Check for uppercase letters
        if not re.search(r'[A-Z]', password):
            results['issues'].append('Password should contain uppercase letters')
            results['suggestions'].append('Add uppercase letters (A-Z)')
        else:
            results['score'] += 1
        
        # Check for lowercase letters
        if not re.search(r'[a-z]', password):
            results['issues'].append('Password should contain lowercase letters')
            results['suggestions'].append('Add lowercase letters (a-z)')
        else:
            results['score'] += 1
        
        # Check for numbers
        if not re.search(r'\d', password):
            results['issues'].append('Password should contain numbers')
            results['suggestions'].append('Add numbers (0-9)')
        else:
            results['score'] += 1
        
        # Check for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            results['issues'].append('Password should contain special characters')
            results['suggestions'].append('Add special characters (!@#$%^&*)')
        else:
            results['score'] += 1
        
        # Check for common patterns
        if self._has_common_patterns(password):
            results['issues'].append('Password contains common patterns')
            results['suggestions'].append('Avoid sequential characters or repeated patterns')
        
        return results
    
    def _has_common_patterns(self, password: str) -> bool:
        """Check for common weak patterns in passwords."""
        password_lower = password.lower()
        
        # Check for sequential characters
        sequences = ['123', 'abc', 'qwe', 'asd', 'zxc']
        for seq in sequences:
            if seq in password_lower:
                return True
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            return True
        
        return False

class BasicPasswordHasher:
    """Basic password hasher using PBKDF2 with SHA-256."""
    
    def __init__(self, iterations: int = 100000):
        self.iterations = iterations
        self.validator = PasswordValidator()
    
    def generate_salt(self, length: int = 32) -> bytes:
        """Generate a cryptographically secure random salt."""
        return secrets.token_bytes(length)
    
    def hash_password(self, password: str, salt: Optional[bytes] = None) -> str:
        """Hash a password with salt using PBKDF2."""
        # Validate password first
        validation = self.validator.validate_password(password)
        if not validation['is_valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['issues'])}")
        
        # Generate salt if not provided
        if salt is None:
            salt = self.generate_salt()
        
        # Hash the password
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            self.iterations
        )
        
        # Combine salt and hash for storage
        # Format: iterations:salt:hash (all base64 encoded)
        salt_b64 = base64.b64encode(salt).decode('ascii')
        hash_b64 = base64.b64encode(password_hash).decode('ascii')
        
        return f"{self.iterations}:{salt_b64}:{hash_b64}"
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a stored hash."""
        try:
            # Parse the stored hash
            parts = stored_hash.split(':')
            if len(parts) != 3:
                return False
            
            iterations = int(parts[0])
            salt = base64.b64decode(parts[1])
            stored_password_hash = base64.b64decode(parts[2])
            
            # Hash the provided password with the same salt and iterations
            password_hash = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                iterations
            )
            
            # Compare hashes using constant-time comparison
            return secrets.compare_digest(password_hash, stored_password_hash)
            
        except (ValueError, TypeError):
            return False

class BcryptPasswordHasher:
    """Password hasher using bcrypt algorithm."""
    
    def __init__(self, rounds: int = 12):
        self.rounds = rounds
        self.validator = PasswordValidator()
        
        # Try to import bcrypt, provide fallback if not available
        try:
            import bcrypt
            self.bcrypt = bcrypt
            self.available = True
        except ImportError:
            self.available = False
            print("Warning: bcrypt not available. Install with: pip install bcrypt")
    
    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        if not self.available:
            raise ImportError("bcrypt library not available")
        
        # Validate password first
        validation = self.validator.validate_password(password)
        if not validation['is_valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['issues'])}")
        
        # Generate salt and hash password
        salt = self.bcrypt.gensalt(rounds=self.rounds)
        password_hash = self.bcrypt.hashpw(password.encode('utf-8'), salt)
        
        return password_hash.decode('utf-8')
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a bcrypt hash."""
        if not self.available:
            return False
        
        try:
            return self.bcrypt.checkpw(
                password.encode('utf-8'),
                stored_hash.encode('utf-8')
            )
        except (ValueError, TypeError):
            return False

# What we accomplished in this step:
# - Added bcrypt password hasher with adaptive cost
# - Implemented graceful fallback when bcrypt is not available
# - Maintained consistent interface with validation
# - Used bcrypt's built-in salt generation and verification


# Step 4: Create unified password hasher with multiple algorithms
# ===============================================================================

# Explanation:
# Now we'll create a unified interface that supports multiple hashing algorithms
# and can automatically detect which algorithm was used for verification.

import hashlib
import secrets
import re
import base64
import time
from typing import Optional, Dict, Any, Literal

class PasswordValidator:
    """Validates password strength and security requirements."""
    
    def __init__(self, min_length: int = 8):
        self.min_length = min_length
    
    def validate_password(self, password: str) -> Dict[str, Any]:
        """Validate password strength and return detailed results."""
        results = {
            'is_valid': True,
            'score': 0,
            'issues': [],
            'suggestions': []
        }
        
        # Check minimum length
        if len(password) < self.min_length:
            results['is_valid'] = False
            results['issues'].append(f'Password must be at least {self.min_length} characters long')
            results['suggestions'].append('Use a longer password')
        else:
            results['score'] += 1
        
        # Check for uppercase letters
        if not re.search(r'[A-Z]', password):
            results['issues'].append('Password should contain uppercase letters')
            results['suggestions'].append('Add uppercase letters (A-Z)')
        else:
            results['score'] += 1
        
        # Check for lowercase letters
        if not re.search(r'[a-z]', password):
            results['issues'].append('Password should contain lowercase letters')
            results['suggestions'].append('Add lowercase letters (a-z)')
        else:
            results['score'] += 1
        
        # Check for numbers
        if not re.search(r'\d', password):
            results['issues'].append('Password should contain numbers')
            results['suggestions'].append('Add numbers (0-9)')
        else:
            results['score'] += 1
        
        # Check for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            results['issues'].append('Password should contain special characters')
            results['suggestions'].append('Add special characters (!@#$%^&*)')
        else:
            results['score'] += 1
        
        # Check for common patterns
        if self._has_common_patterns(password):
            results['issues'].append('Password contains common patterns')
            results['suggestions'].append('Avoid sequential characters or repeated patterns')
        
        return results
    
    def _has_common_patterns(self, password: str) -> bool:
        """Check for common weak patterns in passwords."""
        password_lower = password.lower()
        
        # Check for sequential characters
        sequences = ['123', 'abc', 'qwe', 'asd', 'zxc']
        for seq in sequences:
            if seq in password_lower:
                return True
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            return True
        
        return False

class BasicPasswordHasher:
    """Basic password hasher using PBKDF2 with SHA-256."""
    
    def __init__(self, iterations: int = 100000):
        self.iterations = iterations
        self.validator = PasswordValidator()
    
    def generate_salt(self, length: int = 32) -> bytes:
        """Generate a cryptographically secure random salt."""
        return secrets.token_bytes(length)
    
    def hash_password(self, password: str, salt: Optional[bytes] = None) -> str:
        """Hash a password with salt using PBKDF2."""
        # Validate password first
        validation = self.validator.validate_password(password)
        if not validation['is_valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['issues'])}")
        
        # Generate salt if not provided
        if salt is None:
            salt = self.generate_salt()
        
        # Hash the password
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            self.iterations
        )
        
        # Combine salt and hash for storage
        # Format: iterations:salt:hash (all base64 encoded)
        salt_b64 = base64.b64encode(salt).decode('ascii')
        hash_b64 = base64.b64encode(password_hash).decode('ascii')
        
        return f"{self.iterations}:{salt_b64}:{hash_b64}"
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a stored hash."""
        try:
            # Parse the stored hash
            parts = stored_hash.split(':')
            if len(parts) != 3:
                return False
            
            iterations = int(parts[0])
            salt = base64.b64decode(parts[1])
            stored_password_hash = base64.b64decode(parts[2])
            
            # Hash the provided password with the same salt and iterations
            password_hash = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                iterations
            )
            
            # Compare hashes using constant-time comparison
            return secrets.compare_digest(password_hash, stored_password_hash)
            
        except (ValueError, TypeError):
            return False

class BcryptPasswordHasher:
    """Password hasher using bcrypt algorithm."""
    
    def __init__(self, rounds: int = 12):
        self.rounds = rounds
        self.validator = PasswordValidator()
        
        # Try to import bcrypt, provide fallback if not available
        try:
            import bcrypt
            self.bcrypt = bcrypt
            self.available = True
        except ImportError:
            self.available = False
            print("Warning: bcrypt not available. Install with: pip install bcrypt")
    
    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        if not self.available:
            raise ImportError("bcrypt library not available")
        
        # Validate password first
        validation = self.validator.validate_password(password)
        if not validation['is_valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['issues'])}")
        
        # Generate salt and hash password
        salt = self.bcrypt.gensalt(rounds=self.rounds)
        password_hash = self.bcrypt.hashpw(password.encode('utf-8'), salt)
        
        return password_hash.decode('utf-8')
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a bcrypt hash."""
        if not self.available:
            return False
        
        try:
            return self.bcrypt.checkpw(
                password.encode('utf-8'),
                stored_hash.encode('utf-8')
            )
        except (ValueError, TypeError):
            return False

class PasswordHasher:
    """Unified password hasher supporting multiple algorithms."""
    
    def __init__(self, algorithm: Literal['pbkdf2', 'bcrypt'] = 'bcrypt'):
        self.algorithm = algorithm
        self.validator = PasswordValidator()
        
        # Initialize hashers
        self.pbkdf2_hasher = BasicPasswordHasher()
        self.bcrypt_hasher = BcryptPasswordHasher()
        
        # Set default hasher
        if algorithm == 'bcrypt' and self.bcrypt_hasher.available:
            self.default_hasher = self.bcrypt_hasher
        else:
            self.default_hasher = self.pbkdf2_hasher
            if algorithm == 'bcrypt':
                print("Warning: bcrypt not available, falling back to PBKDF2")
    
    def hash_password(self, password: str) -> str:
        """Hash a password using the configured algorithm."""
        return self.default_hasher.hash_password(password)
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a stored hash (auto-detects algorithm)."""
        # Auto-detect algorithm based on hash format
        if stored_hash.startswith('$2'):  # bcrypt format
            return self.bcrypt_hasher.verify_password(password, stored_hash)
        elif ':' in stored_hash:  # PBKDF2 format
            return self.pbkdf2_hasher.verify_password(password, stored_hash)
        else:
            # Try both algorithms
            return (self.bcrypt_hasher.verify_password(password, stored_hash) or
                    self.pbkdf2_hasher.verify_password(password, stored_hash))
    
    def verify_password_with_timing_protection(self, password: str, stored_hash: str) -> bool:
        """Verify password with protection against timing attacks."""
        start_time = time.time()
        
        try:
            result = self.verify_password(password, stored_hash)
        except Exception:
            result = False
        
        # Ensure minimum time to prevent timing attacks
        elapsed = time.time() - start_time
        min_time = 0.1  # 100ms minimum
        if elapsed < min_time:
            time.sleep(min_time - elapsed)
        
        return result
    
    def get_hash_info(self, stored_hash: str) -> Dict[str, Any]:
        """Get information about a stored hash."""
        info = {'algorithm': 'unknown', 'valid_format': False}
        
        if stored_hash.startswith('$2'):
            info['algorithm'] = 'bcrypt'
            info['valid_format'] = True
            # Extract bcrypt parameters
            parts = stored_hash.split('$')
            if len(parts) >= 4:
                info['rounds'] = int(parts[2])
        elif ':' in stored_hash:
            info['algorithm'] = 'pbkdf2'
            parts = stored_hash.split(':')
            if len(parts) == 3:
                info['valid_format'] = True
                info['iterations'] = int(parts[0])
        
        return info

# What we accomplished in this step:
# - Created unified password hasher with algorithm auto-detection
# - Added timing attack protection for verification
# - Implemented hash format analysis
# - Provided fallback mechanisms for missing libraries


# Step 5: Add comprehensive testing and security demonstrations
# ===============================================================================

# Explanation:
# Let's test our complete password security system and demonstrate
# various security features and attack resistance.

import hashlib
import secrets
import re
import base64
import time
from typing import Optional, Dict, Any, Literal

class PasswordValidator:
    """Validates password strength and security requirements."""
    
    def __init__(self, min_length: int = 8):
        self.min_length = min_length
    
    def validate_password(self, password: str) -> Dict[str, Any]:
        """Validate password strength and return detailed results."""
        results = {
            'is_valid': True,
            'score': 0,
            'issues': [],
            'suggestions': []
        }
        
        # Check minimum length
        if len(password) < self.min_length:
            results['is_valid'] = False
            results['issues'].append(f'Password must be at least {self.min_length} characters long')
            results['suggestions'].append('Use a longer password')
        else:
            results['score'] += 1
        
        # Check for uppercase letters
        if not re.search(r'[A-Z]', password):
            results['issues'].append('Password should contain uppercase letters')
            results['suggestions'].append('Add uppercase letters (A-Z)')
        else:
            results['score'] += 1
        
        # Check for lowercase letters
        if not re.search(r'[a-z]', password):
            results['issues'].append('Password should contain lowercase letters')
            results['suggestions'].append('Add lowercase letters (a-z)')
        else:
            results['score'] += 1
        
        # Check for numbers
        if not re.search(r'\d', password):
            results['issues'].append('Password should contain numbers')
            results['suggestions'].append('Add numbers (0-9)')
        else:
            results['score'] += 1
        
        # Check for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            results['issues'].append('Password should contain special characters')
            results['suggestions'].append('Add special characters (!@#$%^&*)')
        else:
            results['score'] += 1
        
        # Check for common patterns
        if self._has_common_patterns(password):
            results['issues'].append('Password contains common patterns')
            results['suggestions'].append('Avoid sequential characters or repeated patterns')
        
        return results
    
    def _has_common_patterns(self, password: str) -> bool:
        """Check for common weak patterns in passwords."""
        password_lower = password.lower()
        
        # Check for sequential characters
        sequences = ['123', 'abc', 'qwe', 'asd', 'zxc']
        for seq in sequences:
            if seq in password_lower:
                return True
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            return True
        
        return False

class BasicPasswordHasher:
    """Basic password hasher using PBKDF2 with SHA-256."""
    
    def __init__(self, iterations: int = 100000):
        self.iterations = iterations
        self.validator = PasswordValidator()
    
    def generate_salt(self, length: int = 32) -> bytes:
        """Generate a cryptographically secure random salt."""
        return secrets.token_bytes(length)
    
    def hash_password(self, password: str, salt: Optional[bytes] = None) -> str:
        """Hash a password with salt using PBKDF2."""
        # Validate password first
        validation = self.validator.validate_password(password)
        if not validation['is_valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['issues'])}")
        
        # Generate salt if not provided
        if salt is None:
            salt = self.generate_salt()
        
        # Hash the password
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            self.iterations
        )
        
        # Combine salt and hash for storage
        # Format: iterations:salt:hash (all base64 encoded)
        salt_b64 = base64.b64encode(salt).decode('ascii')
        hash_b64 = base64.b64encode(password_hash).decode('ascii')
        
        return f"{self.iterations}:{salt_b64}:{hash_b64}"
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a stored hash."""
        try:
            # Parse the stored hash
            parts = stored_hash.split(':')
            if len(parts) != 3:
                return False
            
            iterations = int(parts[0])
            salt = base64.b64decode(parts[1])
            stored_password_hash = base64.b64decode(parts[2])
            
            # Hash the provided password with the same salt and iterations
            password_hash = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                iterations
            )
            
            # Compare hashes using constant-time comparison
            return secrets.compare_digest(password_hash, stored_password_hash)
            
        except (ValueError, TypeError):
            return False

class BcryptPasswordHasher:
    """Password hasher using bcrypt algorithm."""
    
    def __init__(self, rounds: int = 12):
        self.rounds = rounds
        self.validator = PasswordValidator()
        
        # Try to import bcrypt, provide fallback if not available
        try:
            import bcrypt
            self.bcrypt = bcrypt
            self.available = True
        except ImportError:
            self.available = False
            print("Warning: bcrypt not available. Install with: pip install bcrypt")
    
    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        if not self.available:
            raise ImportError("bcrypt library not available")
        
        # Validate password first
        validation = self.validator.validate_password(password)
        if not validation['is_valid']:
            raise ValueError(f"Password validation failed: {', '.join(validation['issues'])}")
        
        # Generate salt and hash password
        salt = self.bcrypt.gensalt(rounds=self.rounds)
        password_hash = self.bcrypt.hashpw(password.encode('utf-8'), salt)
        
        return password_hash.decode('utf-8')
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a bcrypt hash."""
        if not self.available:
            return False
        
        try:
            return self.bcrypt.checkpw(
                password.encode('utf-8'),
                stored_hash.encode('utf-8')
            )
        except (ValueError, TypeError):
            return False

class PasswordHasher:
    """Unified password hasher supporting multiple algorithms."""
    
    def __init__(self, algorithm: Literal['pbkdf2', 'bcrypt'] = 'bcrypt'):
        self.algorithm = algorithm
        self.validator = PasswordValidator()
        
        # Initialize hashers
        self.pbkdf2_hasher = BasicPasswordHasher()
        self.bcrypt_hasher = BcryptPasswordHasher()
        
        # Set default hasher
        if algorithm == 'bcrypt' and self.bcrypt_hasher.available:
            self.default_hasher = self.bcrypt_hasher
        else:
            self.default_hasher = self.pbkdf2_hasher
            if algorithm == 'bcrypt':
                print("Warning: bcrypt not available, falling back to PBKDF2")
    
    def hash_password(self, password: str) -> str:
        """Hash a password using the configured algorithm."""
        return self.default_hasher.hash_password(password)
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify a password against a stored hash (auto-detects algorithm)."""
        # Auto-detect algorithm based on hash format
        if stored_hash.startswith('$2'):  # bcrypt format
            return self.bcrypt_hasher.verify_password(password, stored_hash)
        elif ':' in stored_hash:  # PBKDF2 format
            return self.pbkdf2_hasher.verify_password(password, stored_hash)
        else:
            # Try both algorithms
            return (self.bcrypt_hasher.verify_password(password, stored_hash) or
                    self.pbkdf2_hasher.verify_password(password, stored_hash))
    
    def verify_password_with_timing_protection(self, password: str, stored_hash: str) -> bool:
        """Verify password with protection against timing attacks."""
        start_time = time.time()
        
        try:
            result = self.verify_password(password, stored_hash)
        except Exception:
            result = False
        
        # Ensure minimum time to prevent timing attacks
        elapsed = time.time() - start_time
        min_time = 0.1  # 100ms minimum
        if elapsed < min_time:
            time.sleep(min_time - elapsed)
        
        return result
    
    def get_hash_info(self, stored_hash: str) -> Dict[str, Any]:
        """Get information about a stored hash."""
        info = {'algorithm': 'unknown', 'valid_format': False}
        
        if stored_hash.startswith('$2'):
            info['algorithm'] = 'bcrypt'
            info['valid_format'] = True
            # Extract bcrypt parameters
            parts = stored_hash.split('$')
            if len(parts) >= 4:
                info['rounds'] = int(parts[2])
        elif ':' in stored_hash:
            info['algorithm'] = 'pbkdf2'
            parts = stored_hash.split(':')
            if len(parts) == 3:
                info['valid_format'] = True
                info['iterations'] = int(parts[0])
        
        return info

def demonstrate_password_security():
    """Comprehensive demonstration of password security features."""
    print("=== Password Security Demonstration ===\n")
    
    # Test password validation
    print("1. Password Validation:")
    validator = PasswordValidator()
    
    test_passwords = [
        "weak",
        "password123",
        "StrongPass123!",
        "MySecureP@ssw0rd2025"
    ]
    
    for password in test_passwords:
        result = validator.validate_password(password)
        print(f"Password: '{password}'")
        print(f"  Valid: {result['is_valid']}")
        print(f"  Score: {result['score']}/5")
        if result['issues']:
            print(f"  Issues: {', '.join(result['issues'])}")
        print()
    
    # Test password hashing
    print("2. Password Hashing:")
    hasher = PasswordHasher()
    test_password = "MySecureP@ssw0rd2025"
    
    # Hash the password
    hashed = hasher.hash_password(test_password)
    print(f"Original password: {test_password}")
    print(f"Hashed password: {hashed}")
    print(f"Hash info: {hasher.get_hash_info(hashed)}")
    print()
    
    # Test verification
    print("3. Password Verification:")
    print(f"Correct password: {hasher.verify_password(test_password, hashed)}")
    print(f"Wrong password: {hasher.verify_password('wrongpassword', hashed)}")
    print()
    
    # Test different algorithms
    print("4. Algorithm Comparison:")
    pbkdf2_hasher = PasswordHasher('pbkdf2')
    
    pbkdf2_hash = pbkdf2_hasher.hash_password(test_password)
    print(f"PBKDF2 hash: {pbkdf2_hash}")
    print(f"PBKDF2 info: {pbkdf2_hasher.get_hash_info(pbkdf2_hash)}")
    
    # Test cross-verification
    print(f"Cross-verification works: {hasher.verify_password(test_password, pbkdf2_hash)}")
    print()
    
    # Test timing attack protection
    print("5. Timing Attack Protection:")
    start_time = time.time()
    hasher.verify_password_with_timing_protection("wrong", hashed)
    elapsed1 = time.time() - start_time
    
    start_time = time.time()
    hasher.verify_password_with_timing_protection(test_password, hashed)
    elapsed2 = time.time() - start_time
    
    print(f"Wrong password time: {elapsed1:.3f}s")
    print(f"Correct password time: {elapsed2:.3f}s")
    print(f"Time difference: {abs(elapsed1 - elapsed2):.3f}s (should be minimal)")
    print()
    
    # Test salt uniqueness
    print("6. Salt Uniqueness:")
    hash1 = hasher.hash_password(test_password)
    hash2 = hasher.hash_password(test_password)
    print(f"Same password, different hashes:")
    print(f"Hash 1: {hash1}")
    print(f"Hash 2: {hash2}")
    print(f"Hashes are different: {hash1 != hash2}")

# Run the demonstration
demonstrate_password_security()

# What we accomplished in this step:
# - Created comprehensive testing suite
# - Demonstrated password validation features
# - Showed algorithm comparison and cross-verification
# - Tested timing attack protection
# - Verified salt uniqueness for security


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Password validation and strength checking
# - Secure password hashing with salts
# - Multiple hashing algorithms (PBKDF2, bcrypt)
# - Timing attack prevention
# - Constant-time comparison
# - Algorithm auto-detection
# - Security best practices for password storage
#
# Security principles demonstrated:
# - Never store passwords in plain text
# - Always use cryptographically secure salts
# - Use slow hashing algorithms designed for passwords
# - Implement timing attack protection
# - Validate password strength before hashing
# - Use constant-time comparison for verification
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each security measure is necessary
# 4. Experiment with modifications (try adding argon2 support!)
#
# Remember: Security is not optional - it's essential!
# ===============================================================================
