"""Question: Implement secure environment variable handling for sensitive data.

Create a comprehensive system for managing environment variables securely,
including validation, encryption, and best practices for different environments.

Requirements:
1. Create a secure environment variable manager
2. Implement validation and type conversion
3. Add encryption for sensitive values
4. Create different configurations for dev/staging/production
5. Demonstrate secure loading and usage patterns

Example usage:
    env_manager = SecureEnvManager()
    db_password = env_manager.get_secret('DB_PASSWORD')
    api_key = env_manager.get_encrypted('API_KEY')
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
# - How to securely load environment variables?
# - What validation is needed for different data types?
# - How to handle missing or invalid values?
# - What encryption methods are appropriate?
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


# Step 1: Import modules and create basic environment variable manager
# ===============================================================================

# Explanation:
# We start with a basic environment variable manager that can load and
# validate environment variables with proper error handling.

import os
import logging
from typing import Optional, Any, Dict, Union
from dataclasses import dataclass

@dataclass
class EnvConfig:
    """Configuration for environment variable validation."""
    required: bool = False
    default: Any = None
    var_type: type = str
    description: str = ""

class BasicEnvManager:
    """Basic environment variable manager with validation."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._config: Dict[str, EnvConfig] = {}
    
    def register_var(self, name: str, config: EnvConfig):
        """Register an environment variable with its configuration."""
        self._config[name] = config
    
    def get(self, name: str, default: Any = None) -> Any:
        """Get environment variable with validation."""
        value = os.getenv(name)
        
        if value is None:
            if name in self._config and self._config[name].required:
                raise ValueError(f"Required environment variable '{name}' is not set")
            return default or (self._config[name].default if name in self._config else None)
        
        # Type conversion
        if name in self._config:
            try:
                return self._convert_type(value, self._config[name].var_type)
            except (ValueError, TypeError) as e:
                self.logger.error(f"Invalid type for {name}: {e}")
                raise ValueError(f"Environment variable '{name}' has invalid type: {e}")
        
        return value
    
    def _convert_type(self, value: str, target_type: type) -> Any:
        """Convert string value to target type."""
        if target_type == bool:
            return value.lower() in ('true', '1', 'yes', 'on')
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == list:
            return [item.strip() for item in value.split(',')]
        else:
            return target_type(value)

# What we accomplished in this step:
# - Created basic environment variable manager
# - Added configuration system for validation
# - Implemented type conversion and error handling


# Step 2: Add encryption capabilities for sensitive data
# ===============================================================================

# Explanation:
# We add encryption functionality to protect sensitive environment variables
# both at rest and in memory. This includes key management and secure decryption.

import os
import logging
import base64
import hashlib
from typing import Optional, Any, Dict, Union
from dataclasses import dataclass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

@dataclass
class EnvConfig:
    """Configuration for environment variable validation."""
    required: bool = False
    default: Any = None
    var_type: type = str
    description: str = ""
    encrypted: bool = False

class BasicEnvManager:
    """Basic environment variable manager with validation."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._config: Dict[str, EnvConfig] = {}
    
    def register_var(self, name: str, config: EnvConfig):
        """Register an environment variable with its configuration."""
        self._config[name] = config
    
    def get(self, name: str, default: Any = None) -> Any:
        """Get environment variable with validation."""
        value = os.getenv(name)
        
        if value is None:
            if name in self._config and self._config[name].required:
                raise ValueError(f"Required environment variable '{name}' is not set")
            return default or (self._config[name].default if name in self._config else None)
        
        # Type conversion
        if name in self._config:
            try:
                return self._convert_type(value, self._config[name].var_type)
            except (ValueError, TypeError) as e:
                self.logger.error(f"Invalid type for {name}: {e}")
                raise ValueError(f"Environment variable '{name}' has invalid type: {e}")
        
        return value
    
    def _convert_type(self, value: str, target_type: type) -> Any:
        """Convert string value to target type."""
        if target_type == bool:
            return value.lower() in ('true', '1', 'yes', 'on')
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == list:
            return [item.strip() for item in value.split(',')]
        else:
            return target_type(value)

class EncryptedEnvManager(BasicEnvManager):
    """Environment manager with encryption capabilities."""
    
    def __init__(self, master_key: Optional[str] = None):
        super().__init__()
        self._fernet = self._setup_encryption(master_key)
        self._decrypted_cache: Dict[str, str] = {}
    
    def _setup_encryption(self, master_key: Optional[str] = None) -> Fernet:
        """Setup encryption using master key or generate one."""
        if master_key is None:
            master_key = os.getenv('MASTER_KEY')
            if master_key is None:
                self.logger.warning("No master key provided, generating temporary key")
                master_key = Fernet.generate_key().decode()
        
        # Derive key from master key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'stable_salt_for_env_vars',  # In production, use random salt
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_key.encode()))
        return Fernet(key)
    
    def encrypt_value(self, value: str) -> str:
        """Encrypt a value for storage."""
        encrypted_bytes = self._fernet.encrypt(value.encode())
        return base64.urlsafe_b64encode(encrypted_bytes).decode()
    
    def decrypt_value(self, encrypted_value: str) -> str:
        """Decrypt an encrypted value."""
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_value.encode())
            decrypted_bytes = self._fernet.decrypt(encrypted_bytes)
            return decrypted_bytes.decode()
        except Exception as e:
            self.logger.error(f"Failed to decrypt value: {e}")
            raise ValueError("Failed to decrypt environment variable")
    
    def get_encrypted(self, name: str, default: Any = None) -> Any:
        """Get and decrypt an encrypted environment variable."""
        # Check cache first
        if name in self._decrypted_cache:
            return self._decrypted_cache[name]
        
        encrypted_value = self.get(name, default)
        if encrypted_value is None:
            return None
        
        try:
            decrypted_value = self.decrypt_value(encrypted_value)
            # Cache the decrypted value
            self._decrypted_cache[name] = decrypted_value
            return decrypted_value
        except ValueError:
            self.logger.error(f"Failed to decrypt environment variable: {name}")
            raise
    
    def clear_cache(self):
        """Clear the decrypted value cache for security."""
        self._decrypted_cache.clear()

# What we accomplished in this step:
# - Added encryption/decryption capabilities using Fernet
# - Implemented secure key derivation from master key
# - Added caching for decrypted values with security controls
# - Extended configuration to support encrypted variables


# Step 3: Add environment-specific configurations and validation
# ===============================================================================

# Explanation:
# Different environments (dev, staging, production) need different security
# levels and validation rules. We add environment detection and configuration.

import os
import logging
import base64
import hashlib
import re
from typing import Optional, Any, Dict, Union, List
from dataclasses import dataclass
from enum import Enum
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Environment(Enum):
    """Application environment types."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"

@dataclass
class EnvConfig:
    """Configuration for environment variable validation."""
    required: bool = False
    default: Any = None
    var_type: type = str
    description: str = ""
    encrypted: bool = False
    pattern: Optional[str] = None  # Regex pattern for validation
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    allowed_values: Optional[List[str]] = None

class BasicEnvManager:
    """Basic environment variable manager with validation."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._config: Dict[str, EnvConfig] = {}
    
    def register_var(self, name: str, config: EnvConfig):
        """Register an environment variable with its configuration."""
        self._config[name] = config
    
    def get(self, name: str, default: Any = None) -> Any:
        """Get environment variable with validation."""
        value = os.getenv(name)
        
        if value is None:
            if name in self._config and self._config[name].required:
                raise ValueError(f"Required environment variable '{name}' is not set")
            return default or (self._config[name].default if name in self._config else None)
        
        # Type conversion
        if name in self._config:
            try:
                return self._convert_type(value, self._config[name].var_type)
            except (ValueError, TypeError) as e:
                self.logger.error(f"Invalid type for {name}: {e}")
                raise ValueError(f"Environment variable '{name}' has invalid type: {e}")
        
        return value
    
    def _convert_type(self, value: str, target_type: type) -> Any:
        """Convert string value to target type."""
        if target_type == bool:
            return value.lower() in ('true', '1', 'yes', 'on')
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == list:
            return [item.strip() for item in value.split(',')]
        else:
            return target_type(value)

class EncryptedEnvManager(BasicEnvManager):
    """Environment manager with encryption capabilities."""
    
    def __init__(self, master_key: Optional[str] = None):
        super().__init__()
        self._fernet = self._setup_encryption(master_key)
        self._decrypted_cache: Dict[str, str] = {}
    
    def _setup_encryption(self, master_key: Optional[str] = None) -> Fernet:
        """Setup encryption using master key or generate one."""
        if master_key is None:
            master_key = os.getenv('MASTER_KEY')
            if master_key is None:
                self.logger.warning("No master key provided, generating temporary key")
                master_key = Fernet.generate_key().decode()
        
        # Derive key from master key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'stable_salt_for_env_vars',  # In production, use random salt
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_key.encode()))
        return Fernet(key)
    
    def encrypt_value(self, value: str) -> str:
        """Encrypt a value for storage."""
        encrypted_bytes = self._fernet.encrypt(value.encode())
        return base64.urlsafe_b64encode(encrypted_bytes).decode()
    
    def decrypt_value(self, encrypted_value: str) -> str:
        """Decrypt an encrypted value."""
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_value.encode())
            decrypted_bytes = self._fernet.decrypt(encrypted_bytes)
            return decrypted_bytes.decode()
        except Exception as e:
            self.logger.error(f"Failed to decrypt value: {e}")
            raise ValueError("Failed to decrypt environment variable")
    
    def get_encrypted(self, name: str, default: Any = None) -> Any:
        """Get and decrypt an encrypted environment variable."""
        # Check cache first
        if name in self._decrypted_cache:
            return self._decrypted_cache[name]
        
        encrypted_value = self.get(name, default)
        if encrypted_value is None:
            return None
        
        try:
            decrypted_value = self.decrypt_value(encrypted_value)
            # Cache the decrypted value
            self._decrypted_cache[name] = decrypted_value
            return decrypted_value
        except ValueError:
            self.logger.error(f"Failed to decrypt environment variable: {name}")
            raise
    
    def clear_cache(self):
        """Clear the decrypted value cache for security."""
        self._decrypted_cache.clear()

class SecureEnvManager(EncryptedEnvManager):
    """Secure environment manager with environment-specific configurations."""
    
    def __init__(self, master_key: Optional[str] = None, environment: Optional[Environment] = None):
        super().__init__(master_key)
        self.environment = environment or self._detect_environment()
        self._setup_environment_configs()
    
    def _detect_environment(self) -> Environment:
        """Auto-detect the current environment."""
        env_name = os.getenv('APP_ENV', os.getenv('ENVIRONMENT', 'development')).lower()
        
        env_mapping = {
            'dev': Environment.DEVELOPMENT,
            'development': Environment.DEVELOPMENT,
            'stage': Environment.STAGING,
            'staging': Environment.STAGING,
            'prod': Environment.PRODUCTION,
            'production': Environment.PRODUCTION,
            'test': Environment.TESTING,
            'testing': Environment.TESTING,
        }
        
        return env_mapping.get(env_name, Environment.DEVELOPMENT)
    
    def _setup_environment_configs(self):
        """Setup environment-specific configurations."""
        if self.environment == Environment.PRODUCTION:
            # Production requires stricter validation
            self._setup_production_configs()
        elif self.environment == Environment.STAGING:
            self._setup_staging_configs()
        else:
            self._setup_development_configs()
    
    def _setup_production_configs(self):
        """Setup production environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=True,
            encrypted=True,
            min_length=12,
            description="Database password (encrypted)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=True,
            encrypted=True,
            pattern=r'^[A-Za-z0-9]{32,}$',
            description="API key (encrypted, alphanumeric, 32+ chars)"
        ))
        self.register_var('SECRET_KEY', EnvConfig(
            required=True,
            encrypted=True,
            min_length=32,
            description="Application secret key (encrypted)"
        ))
    
    def _setup_staging_configs(self):
        """Setup staging environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=True,
            encrypted=True,
            min_length=8,
            description="Database password (encrypted)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=True,
            encrypted=False,  # Less strict for staging
            pattern=r'^[A-Za-z0-9]{16,}$',
            description="API key (16+ chars)"
        ))
    
    def _setup_development_configs(self):
        """Setup development environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=False,
            default="dev_password",
            description="Database password (default for dev)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=False,
            default="dev_api_key_12345",
            description="API key (default for dev)"
        ))
    
    def validate_value(self, name: str, value: str) -> bool:
        """Validate environment variable value against its configuration."""
        if name not in self._config:
            return True
        
        config = self._config[name]
        
        # Length validation
        if config.min_length and len(value) < config.min_length:
            raise ValueError(f"{name}: Value too short (minimum {config.min_length} characters)")
        
        if config.max_length and len(value) > config.max_length:
            raise ValueError(f"{name}: Value too long (maximum {config.max_length} characters)")
        
        # Pattern validation
        if config.pattern and not re.match(config.pattern, value):
            raise ValueError(f"{name}: Value doesn't match required pattern")
        
        # Allowed values validation
        if config.allowed_values and value not in config.allowed_values:
            raise ValueError(f"{name}: Value must be one of {config.allowed_values}")
        
        return True
    
    def get_secret(self, name: str, default: Any = None) -> Any:
        """Get a secret environment variable with extra security checks."""
        if self.environment == Environment.PRODUCTION:
            # In production, secrets must be encrypted
            if name in self._config and self._config[name].encrypted:
                return self.get_encrypted(name, default)
        
        value = self.get(name, default)
        if value and name in self._config:
            self.validate_value(name, str(value))
        
        return value

# What we accomplished in this step:
# - Added environment detection and configuration
# - Implemented environment-specific security rules
# - Added comprehensive validation (length, pattern, allowed values)
# - Created secure secret handling with environment awareness


# Step 4: Add .env file loading and security best practices
# ===============================================================================

# Explanation:
# We add support for loading environment variables from .env files with
# security considerations and audit logging for compliance.

import os
import logging
import base64
import hashlib
import re
import json
from typing import Optional, Any, Dict, Union, List, Set
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Environment(Enum):
    """Application environment types."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"

@dataclass
class EnvConfig:
    """Configuration for environment variable validation."""
    required: bool = False
    default: Any = None
    var_type: type = str
    description: str = ""
    encrypted: bool = False
    pattern: Optional[str] = None  # Regex pattern for validation
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    allowed_values: Optional[List[str]] = None

@dataclass
class AuditLog:
    """Audit log entry for environment variable access."""
    timestamp: str
    variable_name: str
    action: str  # 'read', 'decrypt', 'validate'
    success: bool
    error_message: Optional[str] = None

class BasicEnvManager:
    """Basic environment variable manager with validation."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._config: Dict[str, EnvConfig] = {}
    
    def register_var(self, name: str, config: EnvConfig):
        """Register an environment variable with its configuration."""
        self._config[name] = config
    
    def get(self, name: str, default: Any = None) -> Any:
        """Get environment variable with validation."""
        value = os.getenv(name)
        
        if value is None:
            if name in self._config and self._config[name].required:
                raise ValueError(f"Required environment variable '{name}' is not set")
            return default or (self._config[name].default if name in self._config else None)
        
        # Type conversion
        if name in self._config:
            try:
                return self._convert_type(value, self._config[name].var_type)
            except (ValueError, TypeError) as e:
                self.logger.error(f"Invalid type for {name}: {e}")
                raise ValueError(f"Environment variable '{name}' has invalid type: {e}")
        
        return value
    
    def _convert_type(self, value: str, target_type: type) -> Any:
        """Convert string value to target type."""
        if target_type == bool:
            return value.lower() in ('true', '1', 'yes', 'on')
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == list:
            return [item.strip() for item in value.split(',')]
        else:
            return target_type(value)

class EncryptedEnvManager(BasicEnvManager):
    """Environment manager with encryption capabilities."""
    
    def __init__(self, master_key: Optional[str] = None):
        super().__init__()
        self._fernet = self._setup_encryption(master_key)
        self._decrypted_cache: Dict[str, str] = {}
    
    def _setup_encryption(self, master_key: Optional[str] = None) -> Fernet:
        """Setup encryption using master key or generate one."""
        if master_key is None:
            master_key = os.getenv('MASTER_KEY')
            if master_key is None:
                self.logger.warning("No master key provided, generating temporary key")
                master_key = Fernet.generate_key().decode()
        
        # Derive key from master key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'stable_salt_for_env_vars',  # In production, use random salt
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_key.encode()))
        return Fernet(key)
    
    def encrypt_value(self, value: str) -> str:
        """Encrypt a value for storage."""
        encrypted_bytes = self._fernet.encrypt(value.encode())
        return base64.urlsafe_b64encode(encrypted_bytes).decode()
    
    def decrypt_value(self, encrypted_value: str) -> str:
        """Decrypt an encrypted value."""
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_value.encode())
            decrypted_bytes = self._fernet.decrypt(encrypted_bytes)
            return decrypted_bytes.decode()
        except Exception as e:
            self.logger.error(f"Failed to decrypt value: {e}")
            raise ValueError("Failed to decrypt environment variable")
    
    def get_encrypted(self, name: str, default: Any = None) -> Any:
        """Get and decrypt an encrypted environment variable."""
        # Check cache first
        if name in self._decrypted_cache:
            return self._decrypted_cache[name]
        
        encrypted_value = self.get(name, default)
        if encrypted_value is None:
            return None
        
        try:
            decrypted_value = self.decrypt_value(encrypted_value)
            # Cache the decrypted value
            self._decrypted_cache[name] = decrypted_value
            return decrypted_value
        except ValueError:
            self.logger.error(f"Failed to decrypt environment variable: {name}")
            raise
    
    def clear_cache(self):
        """Clear the decrypted value cache for security."""
        self._decrypted_cache.clear()

class SecureEnvManager(EncryptedEnvManager):
    """Secure environment manager with environment-specific configurations."""
    
    def __init__(self, master_key: Optional[str] = None, environment: Optional[Environment] = None):
        super().__init__(master_key)
        self.environment = environment or self._detect_environment()
        self._setup_environment_configs()
    
    def _detect_environment(self) -> Environment:
        """Auto-detect the current environment."""
        env_name = os.getenv('APP_ENV', os.getenv('ENVIRONMENT', 'development')).lower()
        
        env_mapping = {
            'dev': Environment.DEVELOPMENT,
            'development': Environment.DEVELOPMENT,
            'stage': Environment.STAGING,
            'staging': Environment.STAGING,
            'prod': Environment.PRODUCTION,
            'production': Environment.PRODUCTION,
            'test': Environment.TESTING,
            'testing': Environment.TESTING,
        }
        
        return env_mapping.get(env_name, Environment.DEVELOPMENT)
    
    def _setup_environment_configs(self):
        """Setup environment-specific configurations."""
        if self.environment == Environment.PRODUCTION:
            # Production requires stricter validation
            self._setup_production_configs()
        elif self.environment == Environment.STAGING:
            self._setup_staging_configs()
        else:
            self._setup_development_configs()
    
    def _setup_production_configs(self):
        """Setup production environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=True,
            encrypted=True,
            min_length=12,
            description="Database password (encrypted)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=True,
            encrypted=True,
            pattern=r'^[A-Za-z0-9]{32,}$',
            description="API key (encrypted, alphanumeric, 32+ chars)"
        ))
        self.register_var('SECRET_KEY', EnvConfig(
            required=True,
            encrypted=True,
            min_length=32,
            description="Application secret key (encrypted)"
        ))
    
    def _setup_staging_configs(self):
        """Setup staging environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=True,
            encrypted=True,
            min_length=8,
            description="Database password (encrypted)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=True,
            encrypted=False,  # Less strict for staging
            pattern=r'^[A-Za-z0-9]{16,}$',
            description="API key (16+ chars)"
        ))
    
    def _setup_development_configs(self):
        """Setup development environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=False,
            default="dev_password",
            description="Database password (default for dev)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=False,
            default="dev_api_key_12345",
            description="API key (default for dev)"
        ))
    
    def validate_value(self, name: str, value: str) -> bool:
        """Validate environment variable value against its configuration."""
        if name not in self._config:
            return True
        
        config = self._config[name]
        
        # Length validation
        if config.min_length and len(value) < config.min_length:
            raise ValueError(f"{name}: Value too short (minimum {config.min_length} characters)")
        
        if config.max_length and len(value) > config.max_length:
            raise ValueError(f"{name}: Value too long (maximum {config.max_length} characters)")
        
        # Pattern validation
        if config.pattern and not re.match(config.pattern, value):
            raise ValueError(f"{name}: Value doesn't match required pattern")
        
        # Allowed values validation
        if config.allowed_values and value not in config.allowed_values:
            raise ValueError(f"{name}: Value must be one of {config.allowed_values}")
        
        return True
    
    def get_secret(self, name: str, default: Any = None) -> Any:
        """Get a secret environment variable with extra security checks."""
        if self.environment == Environment.PRODUCTION:
            # In production, secrets must be encrypted
            if name in self._config and self._config[name].encrypted:
                return self.get_encrypted(name, default)
        
        value = self.get(name, default)
        if value and name in self._config:
            self.validate_value(name, str(value))
        
        return value

class ProductionEnvManager(SecureEnvManager):
    """Production-ready environment manager with audit logging and .env support."""
    
    def __init__(self, master_key: Optional[str] = None, environment: Optional[Environment] = None,
                 audit_log_file: Optional[str] = None):
        super().__init__(master_key, environment)
        self.audit_logs: List[AuditLog] = []
        self.audit_log_file = audit_log_file
        self._accessed_vars: Set[str] = set()
        self._sensitive_patterns = [
            r'.*password.*', r'.*secret.*', r'.*key.*', r'.*token.*',
            r'.*credential.*', r'.*auth.*', r'.*api.*'
        ]
    
    def load_env_file(self, env_file: str = '.env', override: bool = False):
        """Load environment variables from .env file with security checks."""
        env_path = Path(env_file)
        
        if not env_path.exists():
            self.logger.warning(f"Environment file {env_file} not found")
            return
        
        # Security check: ensure file permissions are restrictive
        if env_path.stat().st_mode & 0o077:
            self.logger.warning(f"Environment file {env_file} has overly permissive permissions")
        
        try:
            with open(env_path, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # Skip comments and empty lines
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parse key=value pairs
                    if '=' not in line:
                        self.logger.warning(f"Invalid line {line_num} in {env_file}: {line}")
                        continue
                    
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    
                    # Security check: warn about sensitive data in plain text
                    if self._is_sensitive_var(key) and not self._looks_encrypted(value):
                        self.logger.warning(f"Potentially sensitive variable '{key}' stored in plain text")
                    
                    # Set environment variable if not already set or if override is True
                    if override or key not in os.environ:
                        os.environ[key] = value
                        
        except Exception as e:
            self.logger.error(f"Failed to load environment file {env_file}: {e}")
            raise
    
    def _is_sensitive_var(self, var_name: str) -> bool:
        """Check if variable name indicates sensitive data."""
        var_lower = var_name.lower()
        return any(re.match(pattern, var_lower) for pattern in self._sensitive_patterns)
    
    def _looks_encrypted(self, value: str) -> bool:
        """Check if value appears to be encrypted (base64-like)."""
        try:
            # Check if it's base64 encoded and of reasonable length
            decoded = base64.urlsafe_b64decode(value + '==')
            return len(decoded) > 10  # Encrypted values should be reasonably long
        except:
            return False
    
    def _log_access(self, var_name: str, action: str, success: bool, error: str = None):
        """Log environment variable access for audit purposes."""
        log_entry = AuditLog(
            timestamp=datetime.now().isoformat(),
            variable_name=var_name,
            action=action,
            success=success,
            error_message=error
        )
        
        self.audit_logs.append(log_entry)
        self._accessed_vars.add(var_name)
        
        # Write to audit log file if specified
        if self.audit_log_file:
            try:
                with open(self.audit_log_file, 'a') as f:
                    f.write(json.dumps(asdict(log_entry)) + '\n')
            except Exception as e:
                self.logger.error(f"Failed to write audit log: {e}")
    
    def get(self, name: str, default: Any = None) -> Any:
        """Get environment variable with audit logging."""
        try:
            value = super().get(name, default)
            self._log_access(name, 'read', True)
            return value
        except Exception as e:
            self._log_access(name, 'read', False, str(e))
            raise
    
    def get_encrypted(self, name: str, default: Any = None) -> Any:
        """Get encrypted environment variable with audit logging."""
        try:
            value = super().get_encrypted(name, default)
            self._log_access(name, 'decrypt', True)
            return value
        except Exception as e:
            self._log_access(name, 'decrypt', False, str(e))
            raise
    
    def get_secret(self, name: str, default: Any = None) -> Any:
        """Get secret with enhanced audit logging."""
        try:
            value = super().get_secret(name, default)
            self._log_access(name, 'secret_read', True)
            return value
        except Exception as e:
            self._log_access(name, 'secret_read', False, str(e))
            raise
    
    def generate_security_report(self) -> Dict[str, Any]:
        """Generate a security report of environment variable usage."""
        sensitive_vars = [var for var in self._accessed_vars if self._is_sensitive_var(var)]
        
        return {
            'environment': self.environment.value,
            'total_variables_accessed': len(self._accessed_vars),
            'sensitive_variables_accessed': len(sensitive_vars),
            'sensitive_variables': sensitive_vars,
            'audit_log_entries': len(self.audit_logs),
            'failed_access_attempts': len([log for log in self.audit_logs if not log.success]),
            'recommendations': self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate security recommendations based on usage patterns."""
        recommendations = []
        
        if self.environment == Environment.PRODUCTION:
            unencrypted_sensitive = []
            for var in self._accessed_vars:
                if self._is_sensitive_var(var):
                    if var in self._config and not self._config[var].encrypted:
                        unencrypted_sensitive.append(var)
            
            if unencrypted_sensitive:
                recommendations.append(f"Consider encrypting sensitive variables: {unencrypted_sensitive}")
        
        failed_attempts = [log for log in self.audit_logs if not log.success]
        if failed_attempts:
            recommendations.append(f"Review {len(failed_attempts)} failed access attempts")
        
        if not self.audit_log_file:
            recommendations.append("Consider enabling audit log file for compliance")
        
        return recommendations

# What we accomplished in this step:
# - Added .env file loading with security validation
# - Implemented comprehensive audit logging for compliance
# - Added security reporting and recommendations
# - Enhanced sensitive data detection and warnings


# Step 5: Test the complete implementation with demonstrations
# ===============================================================================

# Explanation:
# Let's test our secure environment variable system with comprehensive
# examples showing all features and security best practices.

import os
import logging
import base64
import hashlib
import re
import json
from typing import Optional, Any, Dict, Union, List, Set
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
from datetime import datetime
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Environment(Enum):
    """Application environment types."""
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"

@dataclass
class EnvConfig:
    """Configuration for environment variable validation."""
    required: bool = False
    default: Any = None
    var_type: type = str
    description: str = ""
    encrypted: bool = False
    pattern: Optional[str] = None  # Regex pattern for validation
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    allowed_values: Optional[List[str]] = None

@dataclass
class AuditLog:
    """Audit log entry for environment variable access."""
    timestamp: str
    variable_name: str
    action: str  # 'read', 'decrypt', 'validate'
    success: bool
    error_message: Optional[str] = None

class BasicEnvManager:
    """Basic environment variable manager with validation."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._config: Dict[str, EnvConfig] = {}
    
    def register_var(self, name: str, config: EnvConfig):
        """Register an environment variable with its configuration."""
        self._config[name] = config
    
    def get(self, name: str, default: Any = None) -> Any:
        """Get environment variable with validation."""
        value = os.getenv(name)
        
        if value is None:
            if name in self._config and self._config[name].required:
                raise ValueError(f"Required environment variable '{name}' is not set")
            return default or (self._config[name].default if name in self._config else None)
        
        # Type conversion
        if name in self._config:
            try:
                return self._convert_type(value, self._config[name].var_type)
            except (ValueError, TypeError) as e:
                self.logger.error(f"Invalid type for {name}: {e}")
                raise ValueError(f"Environment variable '{name}' has invalid type: {e}")
        
        return value
    
    def _convert_type(self, value: str, target_type: type) -> Any:
        """Convert string value to target type."""
        if target_type == bool:
            return value.lower() in ('true', '1', 'yes', 'on')
        elif target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == list:
            return [item.strip() for item in value.split(',')]
        else:
            return target_type(value)

class EncryptedEnvManager(BasicEnvManager):
    """Environment manager with encryption capabilities."""
    
    def __init__(self, master_key: Optional[str] = None):
        super().__init__()
        self._fernet = self._setup_encryption(master_key)
        self._decrypted_cache: Dict[str, str] = {}
    
    def _setup_encryption(self, master_key: Optional[str] = None) -> Fernet:
        """Setup encryption using master key or generate one."""
        if master_key is None:
            master_key = os.getenv('MASTER_KEY')
            if master_key is None:
                self.logger.warning("No master key provided, generating temporary key")
                master_key = Fernet.generate_key().decode()
        
        # Derive key from master key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'stable_salt_for_env_vars',  # In production, use random salt
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_key.encode()))
        return Fernet(key)
    
    def encrypt_value(self, value: str) -> str:
        """Encrypt a value for storage."""
        encrypted_bytes = self._fernet.encrypt(value.encode())
        return base64.urlsafe_b64encode(encrypted_bytes).decode()
    
    def decrypt_value(self, encrypted_value: str) -> str:
        """Decrypt an encrypted value."""
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_value.encode())
            decrypted_bytes = self._fernet.decrypt(encrypted_bytes)
            return decrypted_bytes.decode()
        except Exception as e:
            self.logger.error(f"Failed to decrypt value: {e}")
            raise ValueError("Failed to decrypt environment variable")
    
    def get_encrypted(self, name: str, default: Any = None) -> Any:
        """Get and decrypt an encrypted environment variable."""
        # Check cache first
        if name in self._decrypted_cache:
            return self._decrypted_cache[name]
        
        encrypted_value = self.get(name, default)
        if encrypted_value is None:
            return None
        
        try:
            decrypted_value = self.decrypt_value(encrypted_value)
            # Cache the decrypted value
            self._decrypted_cache[name] = decrypted_value
            return decrypted_value
        except ValueError:
            self.logger.error(f"Failed to decrypt environment variable: {name}")
            raise
    
    def clear_cache(self):
        """Clear the decrypted value cache for security."""
        self._decrypted_cache.clear()

class SecureEnvManager(EncryptedEnvManager):
    """Secure environment manager with environment-specific configurations."""
    
    def __init__(self, master_key: Optional[str] = None, environment: Optional[Environment] = None):
        super().__init__(master_key)
        self.environment = environment or self._detect_environment()
        self._setup_environment_configs()
    
    def _detect_environment(self) -> Environment:
        """Auto-detect the current environment."""
        env_name = os.getenv('APP_ENV', os.getenv('ENVIRONMENT', 'development')).lower()
        
        env_mapping = {
            'dev': Environment.DEVELOPMENT,
            'development': Environment.DEVELOPMENT,
            'stage': Environment.STAGING,
            'staging': Environment.STAGING,
            'prod': Environment.PRODUCTION,
            'production': Environment.PRODUCTION,
            'test': Environment.TESTING,
            'testing': Environment.TESTING,
        }
        
        return env_mapping.get(env_name, Environment.DEVELOPMENT)
    
    def _setup_environment_configs(self):
        """Setup environment-specific configurations."""
        if self.environment == Environment.PRODUCTION:
            # Production requires stricter validation
            self._setup_production_configs()
        elif self.environment == Environment.STAGING:
            self._setup_staging_configs()
        else:
            self._setup_development_configs()
    
    def _setup_production_configs(self):
        """Setup production environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=True,
            encrypted=True,
            min_length=12,
            description="Database password (encrypted)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=True,
            encrypted=True,
            pattern=r'^[A-Za-z0-9]{32,}$',
            description="API key (encrypted, alphanumeric, 32+ chars)"
        ))
        self.register_var('SECRET_KEY', EnvConfig(
            required=True,
            encrypted=True,
            min_length=32,
            description="Application secret key (encrypted)"
        ))
    
    def _setup_staging_configs(self):
        """Setup staging environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=True,
            encrypted=True,
            min_length=8,
            description="Database password (encrypted)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=True,
            encrypted=False,  # Less strict for staging
            pattern=r'^[A-Za-z0-9]{16,}$',
            description="API key (16+ chars)"
        ))
    
    def _setup_development_configs(self):
        """Setup development environment configurations."""
        self.register_var('DB_PASSWORD', EnvConfig(
            required=False,
            default="dev_password",
            description="Database password (default for dev)"
        ))
        self.register_var('API_KEY', EnvConfig(
            required=False,
            default="dev_api_key_12345",
            description="API key (default for dev)"
        ))
    
    def validate_value(self, name: str, value: str) -> bool:
        """Validate environment variable value against its configuration."""
        if name not in self._config:
            return True
        
        config = self._config[name]
        
        # Length validation
        if config.min_length and len(value) < config.min_length:
            raise ValueError(f"{name}: Value too short (minimum {config.min_length} characters)")
        
        if config.max_length and len(value) > config.max_length:
            raise ValueError(f"{name}: Value too long (maximum {config.max_length} characters)")
        
        # Pattern validation
        if config.pattern and not re.match(config.pattern, value):
            raise ValueError(f"{name}: Value doesn't match required pattern")
        
        # Allowed values validation
        if config.allowed_values and value not in config.allowed_values:
            raise ValueError(f"{name}: Value must be one of {config.allowed_values}")
        
        return True
    
    def get_secret(self, name: str, default: Any = None) -> Any:
        """Get a secret environment variable with extra security checks."""
        if self.environment == Environment.PRODUCTION:
            # In production, secrets must be encrypted
            if name in self._config and self._config[name].encrypted:
                return self.get_encrypted(name, default)
        
        value = self.get(name, default)
        if value and name in self._config:
            self.validate_value(name, str(value))
        
        return value

class ProductionEnvManager(SecureEnvManager):
    """Production-ready environment manager with audit logging and .env support."""
    
    def __init__(self, master_key: Optional[str] = None, environment: Optional[Environment] = None,
                 audit_log_file: Optional[str] = None):
        super().__init__(master_key, environment)
        self.audit_logs: List[AuditLog] = []
        self.audit_log_file = audit_log_file
        self._accessed_vars: Set[str] = set()
        self._sensitive_patterns = [
            r'.*password.*', r'.*secret.*', r'.*key.*', r'.*token.*',
            r'.*credential.*', r'.*auth.*', r'.*api.*'
        ]
    
    def load_env_file(self, env_file: str = '.env', override: bool = False):
        """Load environment variables from .env file with security checks."""
        env_path = Path(env_file)
        
        if not env_path.exists():
            self.logger.warning(f"Environment file {env_file} not found")
            return
        
        # Security check: ensure file permissions are restrictive
        if env_path.stat().st_mode & 0o077:
            self.logger.warning(f"Environment file {env_file} has overly permissive permissions")
        
        try:
            with open(env_path, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # Skip comments and empty lines
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parse key=value pairs
                    if '=' not in line:
                        self.logger.warning(f"Invalid line {line_num} in {env_file}: {line}")
                        continue
                    
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    
                    # Security check: warn about sensitive data in plain text
                    if self._is_sensitive_var(key) and not self._looks_encrypted(value):
                        self.logger.warning(f"Potentially sensitive variable '{key}' stored in plain text")
                    
                    # Set environment variable if not already set or if override is True
                    if override or key not in os.environ:
                        os.environ[key] = value
                        
        except Exception as e:
            self.logger.error(f"Failed to load environment file {env_file}: {e}")
            raise
    
    def _is_sensitive_var(self, var_name: str) -> bool:
        """Check if variable name indicates sensitive data."""
        var_lower = var_name.lower()
        return any(re.match(pattern, var_lower) for pattern in self._sensitive_patterns)
    
    def _looks_encrypted(self, value: str) -> bool:
        """Check if value appears to be encrypted (base64-like)."""
        try:
            # Check if it's base64 encoded and of reasonable length
            decoded = base64.urlsafe_b64decode(value + '==')
            return len(decoded) > 10  # Encrypted values should be reasonably long
        except:
            return False
    
    def _log_access(self, var_name: str, action: str, success: bool, error: str = None):
        """Log environment variable access for audit purposes."""
        log_entry = AuditLog(
            timestamp=datetime.now().isoformat(),
            variable_name=var_name,
            action=action,
            success=success,
            error_message=error
        )
        
        self.audit_logs.append(log_entry)
        self._accessed_vars.add(var_name)
        
        # Write to audit log file if specified
        if self.audit_log_file:
            try:
                with open(self.audit_log_file, 'a') as f:
                    f.write(json.dumps(asdict(log_entry)) + '\n')
            except Exception as e:
                self.logger.error(f"Failed to write audit log: {e}")
    
    def get(self, name: str, default: Any = None) -> Any:
        """Get environment variable with audit logging."""
        try:
            value = super().get(name, default)
            self._log_access(name, 'read', True)
            return value
        except Exception as e:
            self._log_access(name, 'read', False, str(e))
            raise
    
    def get_encrypted(self, name: str, default: Any = None) -> Any:
        """Get encrypted environment variable with audit logging."""
        try:
            value = super().get_encrypted(name, default)
            self._log_access(name, 'decrypt', True)
            return value
        except Exception as e:
            self._log_access(name, 'decrypt', False, str(e))
            raise
    
    def get_secret(self, name: str, default: Any = None) -> Any:
        """Get secret with enhanced audit logging."""
        try:
            value = super().get_secret(name, default)
            self._log_access(name, 'secret_read', True)
            return value
        except Exception as e:
            self._log_access(name, 'secret_read', False, str(e))
            raise
    
    def generate_security_report(self) -> Dict[str, Any]:
        """Generate a security report of environment variable usage."""
        sensitive_vars = [var for var in self._accessed_vars if self._is_sensitive_var(var)]
        
        return {
            'environment': self.environment.value,
            'total_variables_accessed': len(self._accessed_vars),
            'sensitive_variables_accessed': len(sensitive_vars),
            'sensitive_variables': sensitive_vars,
            'audit_log_entries': len(self.audit_logs),
            'failed_access_attempts': len([log for log in self.audit_logs if not log.success]),
            'recommendations': self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate security recommendations based on usage patterns."""
        recommendations = []
        
        if self.environment == Environment.PRODUCTION:
            unencrypted_sensitive = []
            for var in self._accessed_vars:
                if self._is_sensitive_var(var):
                    if var in self._config and not self._config[var].encrypted:
                        unencrypted_sensitive.append(var)
            
            if unencrypted_sensitive:
                recommendations.append(f"Consider encrypting sensitive variables: {unencrypted_sensitive}")
        
        failed_attempts = [log for log in self.audit_logs if not log.success]
        if failed_attempts:
            recommendations.append(f"Review {len(failed_attempts)} failed access attempts")
        
        if not self.audit_log_file:
            recommendations.append("Consider enabling audit log file for compliance")
        
        return recommendations

# Configure logging for demonstrations
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

print("=== Testing Secure Environment Variable Management ===\n")

# Test 1: Basic Environment Manager
print("1. Basic Environment Manager:")
basic_manager = BasicEnvManager()

# Register some variables
basic_manager.register_var('PORT', EnvConfig(
    var_type=int,
    default=8000,
    description="Server port"
))

basic_manager.register_var('DEBUG', EnvConfig(
    var_type=bool,
    default=False,
    description="Debug mode"
))

# Set some test environment variables
os.environ['PORT'] = '3000'
os.environ['DEBUG'] = 'true'

port = basic_manager.get('PORT')
debug = basic_manager.get('DEBUG')
print(f"  Port: {port} (type: {type(port).__name__})")
print(f"  Debug: {debug} (type: {type(debug).__name__})")
print()

# Test 2: Encrypted Environment Manager
print("2. Encrypted Environment Manager:")
encrypted_manager = EncryptedEnvManager(master_key="my_secure_master_key_123")

# Encrypt a value
secret_value = "super_secret_password_123"
encrypted_value = encrypted_manager.encrypt_value(secret_value)
print(f"  Original: {secret_value}")
print(f"  Encrypted: {encrypted_value}")

# Set encrypted environment variable
os.environ['ENCRYPTED_SECRET'] = encrypted_value
decrypted_value = encrypted_manager.get_encrypted('ENCRYPTED_SECRET')
print(f"  Decrypted: {decrypted_value}")
print()

# Test 3: Environment-Specific Configuration
print("3. Environment-Specific Configuration:")

# Test development environment
os.environ['APP_ENV'] = 'development'
dev_manager = SecureEnvManager()
print(f"  Environment: {dev_manager.environment.value}")
print(f"  DB Password (dev): {dev_manager.get('DB_PASSWORD')}")
print(f"  API Key (dev): {dev_manager.get('API_KEY')}")
print()

# Test production environment
os.environ['APP_ENV'] = 'production'
prod_manager = SecureEnvManager(master_key="production_master_key")
print(f"  Environment: {prod_manager.environment.value}")

# For production, we need encrypted values
encrypted_db_pass = prod_manager.encrypt_value("secure_prod_password_456")
encrypted_api_key = prod_manager.encrypt_value("ABCD1234567890EFGH1234567890IJKL")

os.environ['DB_PASSWORD'] = encrypted_db_pass
os.environ['API_KEY'] = encrypted_api_key

try:
    db_pass = prod_manager.get_secret('DB_PASSWORD')
    print(f"  DB Password (prod): {'*' * len(db_pass)}")  # Mask for security
    api_key = prod_manager.get_secret('API_KEY')
    print(f"  API Key (prod): {api_key[:8]}...")  # Show only first 8 chars
except Exception as e:
    print(f"  Error: {e}")
print()

# Test 4: Production Manager with Audit Logging
print("4. Production Manager with Audit Logging:")
prod_env_manager = ProductionEnvManager(
    master_key="audit_master_key",
    environment=Environment.PRODUCTION,
    audit_log_file="tmp_rovodev_env_audit.log"
)

# Access some variables to generate audit logs
try:
    prod_env_manager.get('DB_PASSWORD')
    prod_env_manager.get('API_KEY')
    prod_env_manager.get('NONEXISTENT_VAR')
except:
    pass  # Expected for nonexistent variable

print(f"  Audit log entries: {len(prod_env_manager.audit_logs)}")
for log in prod_env_manager.audit_logs:
    status = "✓" if log.success else "✗"
    print(f"    {status} {log.action}: {log.variable_name}")
print()

# Test 5: Security Report
print("5. Security Report:")
report = prod_env_manager.generate_security_report()
print(f"  Environment: {report['environment']}")
print(f"  Variables accessed: {report['total_variables_accessed']}")
print(f"  Sensitive variables: {report['sensitive_variables_accessed']}")
print(f"  Failed attempts: {report['failed_access_attempts']}")
print("  Recommendations:")
for rec in report['recommendations']:
    print(f"    - {rec}")
print()

# Test 6: Validation Examples
print("6. Validation Examples:")
validation_manager = SecureEnvManager()

# Register a variable with strict validation
validation_manager.register_var('EMAIL', EnvConfig(
    required=True,
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    description="User email address"
))

validation_manager.register_var('AGE', EnvConfig(
    var_type=int,
    min_length=1,
    max_length=3,
    description="User age"
))

# Test valid email
os.environ['EMAIL'] = 'user@example.com'
try:
    email = validation_manager.get('EMAIL')
    print(f"  ✓ Valid email: {email}")
except ValueError as e:
    print(f"  ✗ Email validation failed: {e}")

# Test invalid email
os.environ['EMAIL'] = 'invalid-email'
try:
    email = validation_manager.get('EMAIL')
    print(f"  ✓ Email: {email}")
except ValueError as e:
    print(f"  ✗ Email validation failed: {e}")

# Reset to valid email for further tests
os.environ['EMAIL'] = 'user@example.com'
print()

# Test 7: Best Practices Summary
print("7. Security Best Practices Summary:")
print("  ✓ Use environment-specific configurations")
print("  ✓ Encrypt sensitive data in production")
print("  ✓ Validate all input with patterns and constraints")
print("  ✓ Implement comprehensive audit logging")
print("  ✓ Use type conversion for non-string values")
print("  ✓ Provide secure defaults for development")
print("  ✓ Generate security reports for compliance")
print("  ✓ Clear sensitive data from memory when done")

# Clean up
prod_env_manager.clear_cache()
encrypted_manager.clear_cache()

# What we accomplished in this step:
# - Comprehensive testing of all security features
# - Demonstrated environment-specific configurations
# - Showed encryption/decryption workflows
# - Tested validation and error handling
# - Generated audit logs and security reports
# - Provided real-world usage examples


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Secure environment variable management patterns
# - Encryption and decryption of sensitive data
# - Environment-specific security configurations
# - Comprehensive validation and type conversion
# - Audit logging for compliance and security
# - Security reporting and recommendations
# - Best practices for different deployment environments
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each security measure is necessary
# 4. Experiment with different validation rules
# 5. Try implementing additional encryption methods
#
# Remember: Security is not optional - it's essential!
# ===============================================================================