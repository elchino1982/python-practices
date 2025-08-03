"""Question: Implement basic cryptography operations for secure data handling.

Create a comprehensive cryptography system that demonstrates various encryption
and hashing techniques for secure data protection.

Requirements:
1. Implement symmetric encryption (AES)
2. Implement asymmetric encryption (RSA)
3. Implement digital signatures
4. Implement secure hashing
5. Demonstrate key management best practices

Example usage:
    crypto = CryptoManager()
    encrypted = crypto.encrypt_symmetric("secret data", "password")
    decrypted = crypto.decrypt_symmetric(encrypted, "password")
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
# - What cryptographic libraries are available in Python?
# - How do you generate secure keys?
# - What's the difference between symmetric and asymmetric encryption?
# - How do you handle key derivation from passwords?
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


# Step 1: Import required modules and set up basic structure
# ===============================================================================

# Explanation:
# We'll start by importing the necessary cryptographic libraries and setting up
# the basic structure for our cryptography manager.

import os
import base64
import hashlib
from typing import Tuple, Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class CryptoManager:
    """Basic cryptography manager for secure operations."""
    
    def __init__(self):
        self.backend = default_backend()
    
    def generate_salt(self, length: int = 16) -> bytes:
        """Generate a random salt for key derivation."""
        return os.urandom(length)

# What we accomplished in this step:
# - Imported necessary cryptographic libraries
# - Created basic CryptoManager class structure
# - Added salt generation for secure key derivation


# Step 2: Implement symmetric encryption (AES)
# ===============================================================================

# Explanation:
# Symmetric encryption uses the same key for encryption and decryption.
# We'll implement AES encryption with proper key derivation from passwords.

import os
import base64
import hashlib
from typing import Tuple, Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class CryptoManager:
    """Basic cryptography manager for secure operations."""
    
    def __init__(self):
        self.backend = default_backend()
    
    def generate_salt(self, length: int = 16) -> bytes:
        """Generate a random salt for key derivation."""
        return os.urandom(length)
    
    def derive_key_from_password(self, password: str, salt: bytes) -> bytes:
        """Derive a cryptographic key from a password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits for AES-256
            salt=salt,
            iterations=100000,  # Recommended minimum
            backend=self.backend
        )
        return kdf.derive(password.encode('utf-8'))
    
    def encrypt_symmetric(self, data: str, password: str) -> str:
        """Encrypt data using AES symmetric encryption."""
        # Generate random salt and IV
        salt = self.generate_salt()
        iv = os.urandom(16)  # 128-bit IV for AES
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and encrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        
        # Pad data to block size (16 bytes for AES)
        data_bytes = data.encode('utf-8')
        padding_length = 16 - (len(data_bytes) % 16)
        padded_data = data_bytes + bytes([padding_length] * padding_length)
        
        # Encrypt the data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine salt + iv + encrypted_data and encode as base64
        combined = salt + iv + encrypted_data
        return base64.b64encode(combined).decode('utf-8')
    
    def decrypt_symmetric(self, encrypted_data: str, password: str) -> str:
        """Decrypt data using AES symmetric encryption."""
        # Decode from base64
        combined = base64.b64decode(encrypted_data.encode('utf-8'))
        
        # Extract salt, IV, and encrypted data
        salt = combined[:16]
        iv = combined[16:32]
        ciphertext = combined[32:]
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and decrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        
        # Decrypt the data
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        padding_length = padded_data[-1]
        data = padded_data[:-padding_length]
        
        return data.decode('utf-8')

# What we accomplished in this step:
# - Added password-based key derivation using PBKDF2
# - Implemented AES-256-CBC encryption with proper padding
# - Added secure random salt and IV generation
# - Created encrypt/decrypt methods for symmetric encryption


# Step 3: Implement asymmetric encryption (RSA)
# ===============================================================================

# Explanation:
# Asymmetric encryption uses a pair of keys: public key for encryption,
# private key for decryption. We'll implement RSA key generation and encryption.

import os
import base64
import hashlib
from typing import Tuple, Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class CryptoManager:
    """Basic cryptography manager for secure operations."""
    
    def __init__(self):
        self.backend = default_backend()
        self.private_key = None
        self.public_key = None
    
    def generate_salt(self, length: int = 16) -> bytes:
        """Generate a random salt for key derivation."""
        return os.urandom(length)
    
    def derive_key_from_password(self, password: str, salt: bytes) -> bytes:
        """Derive a cryptographic key from a password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits for AES-256
            salt=salt,
            iterations=100000,  # Recommended minimum
            backend=self.backend
        )
        return kdf.derive(password.encode('utf-8'))
    
    def encrypt_symmetric(self, data: str, password: str) -> str:
        """Encrypt data using AES symmetric encryption."""
        # Generate random salt and IV
        salt = self.generate_salt()
        iv = os.urandom(16)  # 128-bit IV for AES
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and encrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        
        # Pad data to block size (16 bytes for AES)
        data_bytes = data.encode('utf-8')
        padding_length = 16 - (len(data_bytes) % 16)
        padded_data = data_bytes + bytes([padding_length] * padding_length)
        
        # Encrypt the data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine salt + iv + encrypted_data and encode as base64
        combined = salt + iv + encrypted_data
        return base64.b64encode(combined).decode('utf-8')
    
    def decrypt_symmetric(self, encrypted_data: str, password: str) -> str:
        """Decrypt data using AES symmetric encryption."""
        # Decode from base64
        combined = base64.b64decode(encrypted_data.encode('utf-8'))
        
        # Extract salt, IV, and encrypted data
        salt = combined[:16]
        iv = combined[16:32]
        ciphertext = combined[32:]
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and decrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        
        # Decrypt the data
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        padding_length = padded_data[-1]
        data = padded_data[:-padding_length]
        
        return data.decode('utf-8')
    
    def generate_rsa_keypair(self, key_size: int = 2048) -> Tuple[bytes, bytes]:
        """Generate RSA public/private key pair."""
        # Generate private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=self.backend
        )
        
        # Get public key
        self.public_key = self.private_key.public_key()
        
        # Serialize keys to PEM format
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
    
    def load_rsa_keys(self, private_pem: bytes, public_pem: bytes):
        """Load RSA keys from PEM format."""
        self.private_key = serialization.load_pem_private_key(
            private_pem, password=None, backend=self.backend
        )
        self.public_key = serialization.load_pem_public_key(
            public_pem, backend=self.backend
        )
    
    def encrypt_asymmetric(self, data: str, public_key_pem: Optional[bytes] = None) -> str:
        """Encrypt data using RSA public key."""
        # Use provided public key or instance public key
        if public_key_pem:
            public_key = serialization.load_pem_public_key(
                public_key_pem, backend=self.backend
            )
        else:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("No public key available for encryption")
        
        # Encrypt data
        encrypted = public_key.encrypt(
            data.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return base64.b64encode(encrypted).decode('utf-8')
    
    def decrypt_asymmetric(self, encrypted_data: str) -> str:
        """Decrypt data using RSA private key."""
        if not self.private_key:
            raise ValueError("No private key available for decryption")
        
        # Decode and decrypt
        encrypted_bytes = base64.b64decode(encrypted_data.encode('utf-8'))
        decrypted = self.private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode('utf-8')

# What we accomplished in this step:
# - Added RSA key pair generation with proper key sizes
# - Implemented RSA encryption/decryption with OAEP padding
# - Added key serialization and loading functionality
# - Used secure padding schemes for RSA operations


# Step 4: Implement digital signatures
# ===============================================================================

# Explanation:
# Digital signatures provide authentication and non-repudiation.
# We'll implement RSA-based digital signatures with proper hashing.

import os
import base64
import hashlib
from typing import Tuple, Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class CryptoManager:
    """Basic cryptography manager for secure operations."""
    
    def __init__(self):
        self.backend = default_backend()
        self.private_key = None
        self.public_key = None
    
    def generate_salt(self, length: int = 16) -> bytes:
        """Generate a random salt for key derivation."""
        return os.urandom(length)
    
    def derive_key_from_password(self, password: str, salt: bytes) -> bytes:
        """Derive a cryptographic key from a password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits for AES-256
            salt=salt,
            iterations=100000,  # Recommended minimum
            backend=self.backend
        )
        return kdf.derive(password.encode('utf-8'))
    
    def encrypt_symmetric(self, data: str, password: str) -> str:
        """Encrypt data using AES symmetric encryption."""
        # Generate random salt and IV
        salt = self.generate_salt()
        iv = os.urandom(16)  # 128-bit IV for AES
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and encrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        
        # Pad data to block size (16 bytes for AES)
        data_bytes = data.encode('utf-8')
        padding_length = 16 - (len(data_bytes) % 16)
        padded_data = data_bytes + bytes([padding_length] * padding_length)
        
        # Encrypt the data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine salt + iv + encrypted_data and encode as base64
        combined = salt + iv + encrypted_data
        return base64.b64encode(combined).decode('utf-8')
    
    def decrypt_symmetric(self, encrypted_data: str, password: str) -> str:
        """Decrypt data using AES symmetric encryption."""
        # Decode from base64
        combined = base64.b64decode(encrypted_data.encode('utf-8'))
        
        # Extract salt, IV, and encrypted data
        salt = combined[:16]
        iv = combined[16:32]
        ciphertext = combined[32:]
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and decrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        
        # Decrypt the data
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        padding_length = padded_data[-1]
        data = padded_data[:-padding_length]
        
        return data.decode('utf-8')
    
    def generate_rsa_keypair(self, key_size: int = 2048) -> Tuple[bytes, bytes]:
        """Generate RSA public/private key pair."""
        # Generate private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=self.backend
        )
        
        # Get public key
        self.public_key = self.private_key.public_key()
        
        # Serialize keys to PEM format
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
    
    def load_rsa_keys(self, private_pem: bytes, public_pem: bytes):
        """Load RSA keys from PEM format."""
        self.private_key = serialization.load_pem_private_key(
            private_pem, password=None, backend=self.backend
        )
        self.public_key = serialization.load_pem_public_key(
            public_pem, backend=self.backend
        )
    
    def encrypt_asymmetric(self, data: str, public_key_pem: Optional[bytes] = None) -> str:
        """Encrypt data using RSA public key."""
        # Use provided public key or instance public key
        if public_key_pem:
            public_key = serialization.load_pem_public_key(
                public_key_pem, backend=self.backend
            )
        else:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("No public key available for encryption")
        
        # Encrypt data
        encrypted = public_key.encrypt(
            data.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return base64.b64encode(encrypted).decode('utf-8')
    
    def decrypt_asymmetric(self, encrypted_data: str) -> str:
        """Decrypt data using RSA private key."""
        if not self.private_key:
            raise ValueError("No private key available for decryption")
        
        # Decode and decrypt
        encrypted_bytes = base64.b64decode(encrypted_data.encode('utf-8'))
        decrypted = self.private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode('utf-8')
    
    def sign_data(self, data: str) -> str:
        """Create a digital signature for the data."""
        if not self.private_key:
            raise ValueError("No private key available for signing")
        
        # Sign the data
        signature = self.private_key.sign(
            data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature).decode('utf-8')
    
    def verify_signature(self, data: str, signature: str, public_key_pem: Optional[bytes] = None) -> bool:
        """Verify a digital signature."""
        # Use provided public key or instance public key
        if public_key_pem:
            public_key = serialization.load_pem_public_key(
                public_key_pem, backend=self.backend
            )
        else:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("No public key available for verification")
        
        try:
            # Verify the signature
            signature_bytes = base64.b64decode(signature.encode('utf-8'))
            public_key.verify(
                signature_bytes,
                data.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

# What we accomplished in this step:
# - Added digital signature creation using RSA private key
# - Implemented signature verification using RSA public key
# - Used PSS padding for enhanced security
# - Added proper error handling for signature verification


# Step 5: Implement secure hashing
# ===============================================================================

# Explanation:
# Secure hashing is essential for data integrity, password storage,
# and digital fingerprinting. We'll implement various hash functions.

import os
import base64
import hashlib
from typing import Tuple, Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class CryptoManager:
    """Basic cryptography manager for secure operations."""
    
    def __init__(self):
        self.backend = default_backend()
        self.private_key = None
        self.public_key = None
    
    def generate_salt(self, length: int = 16) -> bytes:
        """Generate a random salt for key derivation."""
        return os.urandom(length)
    
    def derive_key_from_password(self, password: str, salt: bytes) -> bytes:
        """Derive a cryptographic key from a password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits for AES-256
            salt=salt,
            iterations=100000,  # Recommended minimum
            backend=self.backend
        )
        return kdf.derive(password.encode('utf-8'))
    
    def encrypt_symmetric(self, data: str, password: str) -> str:
        """Encrypt data using AES symmetric encryption."""
        # Generate random salt and IV
        salt = self.generate_salt()
        iv = os.urandom(16)  # 128-bit IV for AES
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and encrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        
        # Pad data to block size (16 bytes for AES)
        data_bytes = data.encode('utf-8')
        padding_length = 16 - (len(data_bytes) % 16)
        padded_data = data_bytes + bytes([padding_length] * padding_length)
        
        # Encrypt the data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine salt + iv + encrypted_data and encode as base64
        combined = salt + iv + encrypted_data
        return base64.b64encode(combined).decode('utf-8')
    
    def decrypt_symmetric(self, encrypted_data: str, password: str) -> str:
        """Decrypt data using AES symmetric encryption."""
        # Decode from base64
        combined = base64.b64decode(encrypted_data.encode('utf-8'))
        
        # Extract salt, IV, and encrypted data
        salt = combined[:16]
        iv = combined[16:32]
        ciphertext = combined[32:]
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and decrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        
        # Decrypt the data
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        padding_length = padded_data[-1]
        data = padded_data[:-padding_length]
        
        return data.decode('utf-8')
    
    def generate_rsa_keypair(self, key_size: int = 2048) -> Tuple[bytes, bytes]:
        """Generate RSA public/private key pair."""
        # Generate private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=self.backend
        )
        
        # Get public key
        self.public_key = self.private_key.public_key()
        
        # Serialize keys to PEM format
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
    
    def load_rsa_keys(self, private_pem: bytes, public_pem: bytes):
        """Load RSA keys from PEM format."""
        self.private_key = serialization.load_pem_private_key(
            private_pem, password=None, backend=self.backend
        )
        self.public_key = serialization.load_pem_public_key(
            public_pem, backend=self.backend
        )
    
    def encrypt_asymmetric(self, data: str, public_key_pem: Optional[bytes] = None) -> str:
        """Encrypt data using RSA public key."""
        # Use provided public key or instance public key
        if public_key_pem:
            public_key = serialization.load_pem_public_key(
                public_key_pem, backend=self.backend
            )
        else:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("No public key available for encryption")
        
        # Encrypt data
        encrypted = public_key.encrypt(
            data.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return base64.b64encode(encrypted).decode('utf-8')
    
    def decrypt_asymmetric(self, encrypted_data: str) -> str:
        """Decrypt data using RSA private key."""
        if not self.private_key:
            raise ValueError("No private key available for decryption")
        
        # Decode and decrypt
        encrypted_bytes = base64.b64decode(encrypted_data.encode('utf-8'))
        decrypted = self.private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode('utf-8')
    
    def sign_data(self, data: str) -> str:
        """Create a digital signature for the data."""
        if not self.private_key:
            raise ValueError("No private key available for signing")
        
        # Sign the data
        signature = self.private_key.sign(
            data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature).decode('utf-8')
    
    def verify_signature(self, data: str, signature: str, public_key_pem: Optional[bytes] = None) -> bool:
        """Verify a digital signature."""
        # Use provided public key or instance public key
        if public_key_pem:
            public_key = serialization.load_pem_public_key(
                public_key_pem, backend=self.backend
            )
        else:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("No public key available for verification")
        
        try:
            # Verify the signature
            signature_bytes = base64.b64decode(signature.encode('utf-8'))
            public_key.verify(
                signature_bytes,
                data.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    
    def hash_data(self, data: str, algorithm: str = 'sha256') -> str:
        """Generate a hash of the data using specified algorithm."""
        data_bytes = data.encode('utf-8')
        
        if algorithm.lower() == 'sha256':
            digest = hashlib.sha256(data_bytes).hexdigest()
        elif algorithm.lower() == 'sha512':
            digest = hashlib.sha512(data_bytes).hexdigest()
        elif algorithm.lower() == 'sha1':
            digest = hashlib.sha1(data_bytes).hexdigest()
        elif algorithm.lower() == 'md5':
            # MD5 is included for compatibility but not recommended for security
            digest = hashlib.md5(data_bytes).hexdigest()
        else:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        return digest
    
    def hash_password(self, password: str, salt: Optional[bytes] = None) -> Tuple[str, str]:
        """Hash a password with salt for secure storage."""
        if salt is None:
            salt = self.generate_salt()
        
        # Use PBKDF2 for password hashing
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=self.backend
        )
        
        key = kdf.derive(password.encode('utf-8'))
        
        # Return base64 encoded hash and salt
        password_hash = base64.b64encode(key).decode('utf-8')
        salt_b64 = base64.b64encode(salt).decode('utf-8')
        
        return password_hash, salt_b64
    
    def verify_password(self, password: str, stored_hash: str, stored_salt: str) -> bool:
        """Verify a password against stored hash and salt."""
        try:
            # Decode salt and generate hash
            salt = base64.b64decode(stored_salt.encode('utf-8'))
            computed_hash, _ = self.hash_password(password, salt)
            
            # Compare hashes
            return computed_hash == stored_hash
        except Exception:
            return False
    
    def generate_hmac(self, data: str, key: str, algorithm: str = 'sha256') -> str:
        """Generate HMAC for message authentication."""
        import hmac
        
        key_bytes = key.encode('utf-8')
        data_bytes = data.encode('utf-8')
        
        if algorithm.lower() == 'sha256':
            mac = hmac.new(key_bytes, data_bytes, hashlib.sha256)
        elif algorithm.lower() == 'sha512':
            mac = hmac.new(key_bytes, data_bytes, hashlib.sha512)
        elif algorithm.lower() == 'sha1':
            mac = hmac.new(key_bytes, data_bytes, hashlib.sha1)
        else:
            raise ValueError(f"Unsupported HMAC algorithm: {algorithm}")
        
        return mac.hexdigest()
    
    def verify_hmac(self, data: str, key: str, expected_mac: str, algorithm: str = 'sha256') -> bool:
        """Verify HMAC for message authentication."""
        try:
            computed_mac = self.generate_hmac(data, key, algorithm)
            # Use constant-time comparison to prevent timing attacks
            import hmac
            return hmac.compare_digest(computed_mac, expected_mac)
        except Exception:
            return False

# What we accomplished in this step:
# - Added secure hash functions (SHA-256, SHA-512, SHA-1, MD5)
# - Implemented password hashing with PBKDF2 and salt
# - Added password verification functionality
# - Implemented HMAC for message authentication
# - Used constant-time comparison for security


# Step 6: Test the complete cryptography implementation
# ===============================================================================

# Explanation:
# Let's test all our cryptographic functions to ensure they work correctly
# and demonstrate best practices for secure data handling.

import os
import base64
import hashlib
from typing import Tuple, Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class CryptoManager:
    """Basic cryptography manager for secure operations."""
    
    def __init__(self):
        self.backend = default_backend()
        self.private_key = None
        self.public_key = None
    
    def generate_salt(self, length: int = 16) -> bytes:
        """Generate a random salt for key derivation."""
        return os.urandom(length)
    
    def derive_key_from_password(self, password: str, salt: bytes) -> bytes:
        """Derive a cryptographic key from a password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 256 bits for AES-256
            salt=salt,
            iterations=100000,  # Recommended minimum
            backend=self.backend
        )
        return kdf.derive(password.encode('utf-8'))
    
    def encrypt_symmetric(self, data: str, password: str) -> str:
        """Encrypt data using AES symmetric encryption."""
        # Generate random salt and IV
        salt = self.generate_salt()
        iv = os.urandom(16)  # 128-bit IV for AES
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and encrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        
        # Pad data to block size (16 bytes for AES)
        data_bytes = data.encode('utf-8')
        padding_length = 16 - (len(data_bytes) % 16)
        padded_data = data_bytes + bytes([padding_length] * padding_length)
        
        # Encrypt the data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Combine salt + iv + encrypted_data and encode as base64
        combined = salt + iv + encrypted_data
        return base64.b64encode(combined).decode('utf-8')
    
    def decrypt_symmetric(self, encrypted_data: str, password: str) -> str:
        """Decrypt data using AES symmetric encryption."""
        # Decode from base64
        combined = base64.b64decode(encrypted_data.encode('utf-8'))
        
        # Extract salt, IV, and encrypted data
        salt = combined[:16]
        iv = combined[16:32]
        ciphertext = combined[32:]
        
        # Derive key from password
        key = self.derive_key_from_password(password, salt)
        
        # Create cipher and decrypt
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        
        # Decrypt the data
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Remove padding
        padding_length = padded_data[-1]
        data = padded_data[:-padding_length]
        
        return data.decode('utf-8')
    
    def generate_rsa_keypair(self, key_size: int = 2048) -> Tuple[bytes, bytes]:
        """Generate RSA public/private key pair."""
        # Generate private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=self.backend
        )
        
        # Get public key
        self.public_key = self.private_key.public_key()
        
        # Serialize keys to PEM format
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
    
    def load_rsa_keys(self, private_pem: bytes, public_pem: bytes):
        """Load RSA keys from PEM format."""
        self.private_key = serialization.load_pem_private_key(
            private_pem, password=None, backend=self.backend
        )
        self.public_key = serialization.load_pem_public_key(
            public_pem, backend=self.backend
        )
    
    def encrypt_asymmetric(self, data: str, public_key_pem: Optional[bytes] = None) -> str:
        """Encrypt data using RSA public key."""
        # Use provided public key or instance public key
        if public_key_pem:
            public_key = serialization.load_pem_public_key(
                public_key_pem, backend=self.backend
            )
        else:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("No public key available for encryption")
        
        # Encrypt data
        encrypted = public_key.encrypt(
            data.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return base64.b64encode(encrypted).decode('utf-8')
    
    def decrypt_asymmetric(self, encrypted_data: str) -> str:
        """Decrypt data using RSA private key."""
        if not self.private_key:
            raise ValueError("No private key available for decryption")
        
        # Decode and decrypt
        encrypted_bytes = base64.b64decode(encrypted_data.encode('utf-8'))
        decrypted = self.private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode('utf-8')
    
    def sign_data(self, data: str) -> str:
        """Create a digital signature for the data."""
        if not self.private_key:
            raise ValueError("No private key available for signing")
        
        # Sign the data
        signature = self.private_key.sign(
            data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature).decode('utf-8')
    
    def verify_signature(self, data: str, signature: str, public_key_pem: Optional[bytes] = None) -> bool:
        """Verify a digital signature."""
        # Use provided public key or instance public key
        if public_key_pem:
            public_key = serialization.load_pem_public_key(
                public_key_pem, backend=self.backend
            )
        else:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("No public key available for verification")
        
        try:
            # Verify the signature
            signature_bytes = base64.b64decode(signature.encode('utf-8'))
            public_key.verify(
                signature_bytes,
                data.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    
    def hash_data(self, data: str, algorithm: str = 'sha256') -> str:
        """Generate a hash of the data using specified algorithm."""
        data_bytes = data.encode('utf-8')
        
        if algorithm.lower() == 'sha256':
            digest = hashlib.sha256(data_bytes).hexdigest()
        elif algorithm.lower() == 'sha512':
            digest = hashlib.sha512(data_bytes).hexdigest()
        elif algorithm.lower() == 'sha1':
            digest = hashlib.sha1(data_bytes).hexdigest()
        elif algorithm.lower() == 'md5':
            # MD5 is included for compatibility but not recommended for security
            digest = hashlib.md5(data_bytes).hexdigest()
        else:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
        return digest
    
    def hash_password(self, password: str, salt: Optional[bytes] = None) -> Tuple[str, str]:
        """Hash a password with salt for secure storage."""
        if salt is None:
            salt = self.generate_salt()
        
        # Use PBKDF2 for password hashing
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=self.backend
        )
        
        key = kdf.derive(password.encode('utf-8'))
        
        # Return base64 encoded hash and salt
        password_hash = base64.b64encode(key).decode('utf-8')
        salt_b64 = base64.b64encode(salt).decode('utf-8')
        
        return password_hash, salt_b64
    
    def verify_password(self, password: str, stored_hash: str, stored_salt: str) -> bool:
        """Verify a password against stored hash and salt."""
        try:
            # Decode salt and generate hash
            salt = base64.b64decode(stored_salt.encode('utf-8'))
            computed_hash, _ = self.hash_password(password, salt)
            
            # Compare hashes
            return computed_hash == stored_hash
        except Exception:
            return False
    
    def generate_hmac(self, data: str, key: str, algorithm: str = 'sha256') -> str:
        """Generate HMAC for message authentication."""
        import hmac
        
        key_bytes = key.encode('utf-8')
        data_bytes = data.encode('utf-8')
        
        if algorithm.lower() == 'sha256':
            mac = hmac.new(key_bytes, data_bytes, hashlib.sha256)
        elif algorithm.lower() == 'sha512':
            mac = hmac.new(key_bytes, data_bytes, hashlib.sha512)
        elif algorithm.lower() == 'sha1':
            mac = hmac.new(key_bytes, data_bytes, hashlib.sha1)
        else:
            raise ValueError(f"Unsupported HMAC algorithm: {algorithm}")
        
        return mac.hexdigest()
    
    def verify_hmac(self, data: str, key: str, expected_mac: str, algorithm: str = 'sha256') -> bool:
        """Verify HMAC for message authentication."""
        try:
            computed_mac = self.generate_hmac(data, key, algorithm)
            # Use constant-time comparison to prevent timing attacks
            import hmac
            return hmac.compare_digest(computed_mac, expected_mac)
        except Exception:
            return False

# Test the complete cryptography implementation
crypto = CryptoManager()

print("=== Testing Cryptography Basics ===\n")

# Test 1: Symmetric Encryption
print("1. Testing Symmetric Encryption (AES):")
secret_data = "This is highly confidential information!"
password = "my_secure_password_123"

encrypted = crypto.encrypt_symmetric(secret_data, password)
print(f"Original: {secret_data}")
print(f"Encrypted: {encrypted[:50]}...")

decrypted = crypto.decrypt_symmetric(encrypted, password)
print(f"Decrypted: {decrypted}")
print(f"Match: {secret_data == decrypted}\n")

# Test 2: Asymmetric Encryption
print("2. Testing Asymmetric Encryption (RSA):")
private_key, public_key = crypto.generate_rsa_keypair()
print("RSA key pair generated successfully")

message = "Secret message for RSA encryption"
rsa_encrypted = crypto.encrypt_asymmetric(message)
print(f"Original: {message}")
print(f"Encrypted: {rsa_encrypted[:50]}...")

rsa_decrypted = crypto.decrypt_asymmetric(rsa_encrypted)
print(f"Decrypted: {rsa_decrypted}")
print(f"Match: {message == rsa_decrypted}\n")

# Test 3: Digital Signatures
print("3. Testing Digital Signatures:")
document = "Important contract document"
signature = crypto.sign_data(document)
print(f"Document: {document}")
print(f"Signature: {signature[:50]}...")

is_valid = crypto.verify_signature(document, signature)
print(f"Signature valid: {is_valid}")

# Test with tampered document
tampered_doc = "Important contract document (modified)"
is_tampered_valid = crypto.verify_signature(tampered_doc, signature)
print(f"Tampered document signature valid: {is_tampered_valid}\n")

# Test 4: Secure Hashing
print("4. Testing Secure Hashing:")
data = "Data to be hashed"
sha256_hash = crypto.hash_data(data, 'sha256')
sha512_hash = crypto.hash_data(data, 'sha512')
print(f"Data: {data}")
print(f"SHA-256: {sha256_hash}")
print(f"SHA-512: {sha512_hash}\n")

# Test 5: Password Hashing
print("5. Testing Password Hashing:")
user_password = "user_password_123"
password_hash, salt = crypto.hash_password(user_password)
print(f"Password: {user_password}")
print(f"Hash: {password_hash}")
print(f"Salt: {salt}")

# Verify correct password
is_correct = crypto.verify_password(user_password, password_hash, salt)
print(f"Correct password verification: {is_correct}")

# Verify wrong password
wrong_password = "wrong_password"
is_wrong = crypto.verify_password(wrong_password, password_hash, salt)
print(f"Wrong password verification: {is_wrong}\n")

# Test 6: HMAC
print("6. Testing HMAC:")
message = "Message to authenticate"
hmac_key = "secret_hmac_key"
mac = crypto.generate_hmac(message, hmac_key)
print(f"Message: {message}")
print(f"HMAC: {mac}")

# Verify HMAC
is_authentic = crypto.verify_hmac(message, hmac_key, mac)
print(f"HMAC verification: {is_authentic}")

# Test with tampered message
tampered_message = "Message to authenticate (tampered)"
is_tampered_authentic = crypto.verify_hmac(tampered_message, hmac_key, mac)
print(f"Tampered message HMAC verification: {is_tampered_authentic}")

# What we accomplished in this step:
# - Tested all cryptographic functions comprehensively
# - Demonstrated symmetric and asymmetric encryption
# - Verified digital signature functionality
# - Tested secure hashing and password storage
# - Validated HMAC for message authentication
# - Showed proper error handling and security practices


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step cryptography solution!
#
# Key concepts learned:
# - Symmetric encryption with AES and proper key derivation
# - Asymmetric encryption with RSA and secure padding
# - Digital signatures for authentication and non-repudiation
# - Secure hashing for data integrity and password storage
# - HMAC for message authentication
# - Best practices for cryptographic security
#
# Security best practices demonstrated:
# - Use of cryptographically secure random number generation
# - Proper key derivation with PBKDF2 and salt
# - Secure padding schemes (OAEP for encryption, PSS for signatures)
# - Constant-time comparison for preventing timing attacks
# - High iteration counts for password hashing
# - Proper error handling without information leakage
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each security measure is necessary
# 4. Experiment with different algorithms and parameters
#
# Remember: Cryptography is complex - always use well-tested libraries!
# ===============================================================================