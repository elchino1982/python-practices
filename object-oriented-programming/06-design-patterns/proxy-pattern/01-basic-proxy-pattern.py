"""Question: Implement the Proxy pattern to provide a placeholder/surrogate for another object.

Create an image viewer that uses proxy objects to control access to large images,
implementing lazy loading, caching, and access control.

Requirements:
1. Create Image interface with display() method
2. Implement RealImage class that loads actual image data
3. Create ProxyImage that controls access to RealImage
4. Implement lazy loading (load only when needed)
5. Add caching mechanism to avoid reloading
6. Demonstrate different proxy types (Virtual, Protection, Remote)

Example usage:
    image1 = ProxyImage("photo1.jpg")
    image1.display()  # Loads and displays
    image1.display()  # Uses cached version
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
# - How can you control access to an object?
# - What is lazy loading and when is it useful?
# - How can you cache expensive operations?
# - What are the different types of proxies?
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


# Step 1: Define the Subject Interface
# ===============================================================================

# Explanation:
# The Proxy pattern requires a common interface between the proxy and real object.
# This allows the proxy to be used wherever the real object would be used.

from abc import ABC, abstractmethod
import time

class Image(ABC):
    """Abstract interface for images."""
    
    @abstractmethod
    def display(self):
        """Display the image."""
        pass
    
    @abstractmethod
    def get_size(self):
        """Get image size."""
        pass

# What we accomplished in this step:
# - Created common interface for both proxy and real objects
# - Defined methods that both proxy and real object must implement


# Step 2: Implement the Real Subject
# ===============================================================================

# Explanation:
# The real subject contains the actual business logic and expensive operations.
# In our case, it simulates loading and displaying an image.

from abc import ABC, abstractmethod
import time

class Image(ABC):
    """Abstract interface for images."""
    
    @abstractmethod
    def display(self):
        """Display the image."""
        pass
    
    @abstractmethod
    def get_size(self):
        """Get image size."""
        pass

class RealImage(Image):
    """Real image that performs expensive loading operations."""
    
    def __init__(self, filename):
        self.filename = filename
        self.size = None
        self.data = None
        self._load_from_disk()
    
    def _load_from_disk(self):
        """Simulate expensive image loading operation."""
        print(f"Loading image '{self.filename}' from disk...")
        # Simulate time-consuming operation
        time.sleep(1)
        
        # Simulate loading image data
        self.data = f"Image data for {self.filename}"
        self.size = (800, 600)  # Simulated image dimensions
        print(f"Image '{self.filename}' loaded successfully!")
    
    def display(self):
        """Display the image."""
        print(f"Displaying image: {self.filename}")
        print(f"Image data: {self.data}")
    
    def get_size(self):
        """Get image size."""
        return self.size

# What we accomplished in this step:
# - Implemented real image class with expensive loading operation
# - Simulated time-consuming disk I/O operation
# - Created actual image functionality


# Step 3: Implement Virtual Proxy (Lazy Loading)
# ===============================================================================

# Explanation:
# Virtual proxy delays expensive operations until they're actually needed.
# This is useful for objects that are expensive to create or load.

from abc import ABC, abstractmethod
import time

class Image(ABC):
    """Abstract interface for images."""
    
    @abstractmethod
    def display(self):
        """Display the image."""
        pass
    
    @abstractmethod
    def get_size(self):
        """Get image size."""
        pass

class RealImage(Image):
    """Real image that performs expensive loading operations."""
    
    def __init__(self, filename):
        self.filename = filename
        self.size = None
        self.data = None
        self._load_from_disk()
    
    def _load_from_disk(self):
        """Simulate expensive image loading operation."""
        print(f"Loading image '{self.filename}' from disk...")
        # Simulate time-consuming operation
        time.sleep(1)
        
        # Simulate loading image data
        self.data = f"Image data for {self.filename}"
        self.size = (800, 600)  # Simulated image dimensions
        print(f"Image '{self.filename}' loaded successfully!")
    
    def display(self):
        """Display the image."""
        print(f"Displaying image: {self.filename}")
        print(f"Image data: {self.data}")
    
    def get_size(self):
        """Get image size."""
        return self.size

class VirtualImageProxy(Image):
    """Virtual proxy that implements lazy loading."""
    
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None
    
    def _get_real_image(self):
        """Get or create the real image (lazy loading)."""
        if self._real_image is None:
            print(f"Proxy: Creating real image for '{self.filename}'")
            self._real_image = RealImage(self.filename)
        return self._real_image
    
    def display(self):
        """Display the image through proxy."""
        print(f"Proxy: Requesting display for '{self.filename}'")
        real_image = self._get_real_image()
        real_image.display()
    
    def get_size(self):
        """Get image size through proxy."""
        print(f"Proxy: Requesting size for '{self.filename}'")
        real_image = self._get_real_image()
        return real_image.get_size()

# What we accomplished in this step:
# - Implemented virtual proxy with lazy loading
# - Delayed expensive object creation until needed
# - Maintained same interface as real object


# Step 4: Implement Caching Proxy
# ===============================================================================

# Explanation:
# Caching proxy stores results of expensive operations to avoid repeated work.
# This improves performance for frequently accessed resources.

from abc import ABC, abstractmethod
import time

class Image(ABC):
    """Abstract interface for images."""
    
    @abstractmethod
    def display(self):
        """Display the image."""
        pass
    
    @abstractmethod
    def get_size(self):
        """Get image size."""
        pass

class RealImage(Image):
    """Real image that performs expensive loading operations."""
    
    def __init__(self, filename):
        self.filename = filename
        self.size = None
        self.data = None
        self._load_from_disk()
    
    def _load_from_disk(self):
        """Simulate expensive image loading operation."""
        print(f"Loading image '{self.filename}' from disk...")
        # Simulate time-consuming operation
        time.sleep(1)
        
        # Simulate loading image data
        self.data = f"Image data for {self.filename}"
        self.size = (800, 600)  # Simulated image dimensions
        print(f"Image '{self.filename}' loaded successfully!")
    
    def display(self):
        """Display the image."""
        print(f"Displaying image: {self.filename}")
        print(f"Image data: {self.data}")
    
    def get_size(self):
        """Get image size."""
        return self.size

class VirtualImageProxy(Image):
    """Virtual proxy that implements lazy loading."""
    
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None
    
    def _get_real_image(self):
        """Get or create the real image (lazy loading)."""
        if self._real_image is None:
            print(f"Proxy: Creating real image for '{self.filename}'")
            self._real_image = RealImage(self.filename)
        return self._real_image
    
    def display(self):
        """Display the image through proxy."""
        print(f"Proxy: Requesting display for '{self.filename}'")
        real_image = self._get_real_image()
        real_image.display()
    
    def get_size(self):
        """Get image size through proxy."""
        print(f"Proxy: Requesting size for '{self.filename}'")
        real_image = self._get_real_image()
        return real_image.get_size()

class CachingImageProxy(Image):
    """Caching proxy that stores loaded images."""
    
    _cache = {}  # Class-level cache shared among all instances
    
    def __init__(self, filename):
        self.filename = filename
    
    def _get_cached_image(self):
        """Get image from cache or create new one."""
        if self.filename not in self._cache:
            print(f"Cache miss: Loading '{self.filename}' into cache")
            self._cache[self.filename] = RealImage(self.filename)
        else:
            print(f"Cache hit: Using cached '{self.filename}'")
        
        return self._cache[self.filename]
    
    def display(self):
        """Display cached image."""
        cached_image = self._get_cached_image()
        cached_image.display()
    
    def get_size(self):
        """Get size from cached image."""
        cached_image = self._get_cached_image()
        return cached_image.get_size()
    
    @classmethod
    def clear_cache(cls):
        """Clear the image cache."""
        cls._cache.clear()
        print("Image cache cleared")
    
    @classmethod
    def get_cache_size(cls):
        """Get number of cached images."""
        return len(cls._cache)

# What we accomplished in this step:
# - Implemented caching proxy to store loaded images
# - Added cache management methods
# - Demonstrated performance improvement through caching


# Step 5: Implement Protection Proxy
# ===============================================================================

# Explanation:
# Protection proxy controls access based on permissions or authentication.
# This is useful for implementing security and access control.

from abc import ABC, abstractmethod
import time

class Image(ABC):
    """Abstract interface for images."""
    
    @abstractmethod
    def display(self):
        """Display the image."""
        pass
    
    @abstractmethod
    def get_size(self):
        """Get image size."""
        pass

class RealImage(Image):
    """Real image that performs expensive loading operations."""
    
    def __init__(self, filename):
        self.filename = filename
        self.size = None
        self.data = None
        self._load_from_disk()
    
    def _load_from_disk(self):
        """Simulate expensive image loading operation."""
        print(f"Loading image '{self.filename}' from disk...")
        # Simulate time-consuming operation
        time.sleep(1)
        
        # Simulate loading image data
        self.data = f"Image data for {self.filename}"
        self.size = (800, 600)  # Simulated image dimensions
        print(f"Image '{self.filename}' loaded successfully!")
    
    def display(self):
        """Display the image."""
        print(f"Displaying image: {self.filename}")
        print(f"Image data: {self.data}")
    
    def get_size(self):
        """Get image size."""
        return self.size

class VirtualImageProxy(Image):
    """Virtual proxy that implements lazy loading."""
    
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None
    
    def _get_real_image(self):
        """Get or create the real image (lazy loading)."""
        if self._real_image is None:
            print(f"Proxy: Creating real image for '{self.filename}'")
            self._real_image = RealImage(self.filename)
        return self._real_image
    
    def display(self):
        """Display the image through proxy."""
        print(f"Proxy: Requesting display for '{self.filename}'")
        real_image = self._get_real_image()
        real_image.display()
    
    def get_size(self):
        """Get image size through proxy."""
        print(f"Proxy: Requesting size for '{self.filename}'")
        real_image = self._get_real_image()
        return real_image.get_size()

class CachingImageProxy(Image):
    """Caching proxy that stores loaded images."""
    
    _cache = {}  # Class-level cache shared among all instances
    
    def __init__(self, filename):
        self.filename = filename
    
    def _get_cached_image(self):
        """Get image from cache or create new one."""
        if self.filename not in self._cache:
            print(f"Cache miss: Loading '{self.filename}' into cache")
            self._cache[self.filename] = RealImage(self.filename)
        else:
            print(f"Cache hit: Using cached '{self.filename}'")
        
        return self._cache[self.filename]
    
    def display(self):
        """Display cached image."""
        cached_image = self._get_cached_image()
        cached_image.display()
    
    def get_size(self):
        """Get size from cached image."""
        cached_image = self._get_cached_image()
        return cached_image.get_size()
    
    @classmethod
    def clear_cache(cls):
        """Clear the image cache."""
        cls._cache.clear()
        print("Image cache cleared")
    
    @classmethod
    def get_cache_size(cls):
        """Get number of cached images."""
        return len(cls._cache)

class User:
    """User class for authentication."""
    
    def __init__(self, username, role):
        self.username = username
        self.role = role

class ProtectionImageProxy(Image):
    """Protection proxy that controls access based on user permissions."""
    
    def __init__(self, filename, required_role="user"):
        self.filename = filename
        self.required_role = required_role
        self._real_image = None
        self.current_user = None
    
    def authenticate(self, user):
        """Authenticate user for access."""
        self.current_user = user
        print(f"User '{user.username}' authenticated with role '{user.role}'")
    
    def _check_access(self):
        """Check if current user has required permissions."""
        if self.current_user is None:
            raise PermissionError("No user authenticated")
        
        # Simple role-based access control
        role_hierarchy = {"guest": 0, "user": 1, "admin": 2}
        user_level = role_hierarchy.get(self.current_user.role, 0)
        required_level = role_hierarchy.get(self.required_role, 1)
        
        if user_level < required_level:
            raise PermissionError(f"Access denied. Required role: {self.required_role}, User role: {self.current_user.role}")
        
        return True
    
    def _get_real_image(self):
        """Get real image after access check."""
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        return self._real_image
    
    def display(self):
        """Display image if user has permission."""
        try:
            self._check_access()
            print(f"Access granted for '{self.current_user.username}' to view '{self.filename}'")
            real_image = self._get_real_image()
            real_image.display()
        except PermissionError as e:
            print(f"Access denied: {e}")
    
    def get_size(self):
        """Get image size if user has permission."""
        try:
            self._check_access()
            real_image = self._get_real_image()
            return real_image.get_size()
        except PermissionError as e:
            print(f"Access denied: {e}")
            return None

# What we accomplished in this step:
# - Implemented protection proxy with role-based access control
# - Added user authentication and authorization
# - Demonstrated security through proxy pattern


# Step 6: Testing and Demonstration
# ===============================================================================

# Explanation:
# Let's test all our proxy implementations and demonstrate their different
# behaviors and use cases.

print("=== Testing Proxy Pattern ===\n")

# Test 1: Virtual Proxy (Lazy Loading)
print("--- Test 1: Virtual Proxy (Lazy Loading) ---")
print("Creating virtual proxy (no loading yet)...")
virtual_proxy = VirtualImageProxy("vacation_photo.jpg")
print("Proxy created, real image not loaded yet\n")

print("First access - triggers loading:")
virtual_proxy.display()
print()

print("Second access - uses already loaded image:")
virtual_proxy.display()
print()

# Test 2: Caching Proxy
print("--- Test 2: Caching Proxy ---")
print("First image access:")
cache_proxy1 = CachingImageProxy("document.pdf")
cache_proxy1.display()
print()

print("Second image access (different proxy, same file):")
cache_proxy2 = CachingImageProxy("document.pdf")
cache_proxy2.display()
print()

print("Different image:")
cache_proxy3 = CachingImageProxy("presentation.ppt")
cache_proxy3.display()
print(f"Cache size: {CachingImageProxy.get_cache_size()}")
print()

# Test 3: Protection Proxy
print("--- Test 3: Protection Proxy ---")

# Create users with different roles
guest_user = User("guest_user", "guest")
regular_user = User("john_doe", "user")
admin_user = User("admin", "admin")

# Create protected image requiring admin access
protected_proxy = ProtectionImageProxy("confidential_report.pdf", "admin")

print("Attempting access without authentication:")
protected_proxy.display()
print()

print("Guest user attempting access:")
protected_proxy.authenticate(guest_user)
protected_proxy.display()
print()

print("Regular user attempting access:")
protected_proxy.authenticate(regular_user)
protected_proxy.display()
print()

print("Admin user accessing:")
protected_proxy.authenticate(admin_user)
protected_proxy.display()
print()

# Test 4: Combined Proxy Features
print("--- Test 4: Combined Proxy Features ---")

class SmartImageProxy(Image):
    """Smart proxy combining multiple proxy features."""
    
    _cache = {}
    
    def __init__(self, filename, required_role="user"):
        self.filename = filename
        self.required_role = required_role
        self.current_user = None
        self._real_image = None
    
    def authenticate(self, user):
        """Authenticate user."""
        self.current_user = user
    
    def _check_access(self):
        """Check access permissions."""
        if self.current_user is None:
            raise PermissionError("Authentication required")
        
        role_hierarchy = {"guest": 0, "user": 1, "admin": 2}
        user_level = role_hierarchy.get(self.current_user.role, 0)
        required_level = role_hierarchy.get(self.required_role, 1)
        
        if user_level < required_level:
            raise PermissionError(f"Insufficient permissions")
        
        return True
    
    def _get_image(self):
        """Get image with caching and lazy loading."""
        # Check cache first
        if self.filename in self._cache:
            print(f"Smart Proxy: Using cached '{self.filename}'")
            return self._cache[self.filename]
        
        # Lazy loading
        if self._real_image is None:
            print(f"Smart Proxy: Lazy loading '{self.filename}'")
            self._real_image = RealImage(self.filename)
            self._cache[self.filename] = self._real_image
        
        return self._real_image
    
    def display(self):
        """Display with all proxy features."""
        try:
            self._check_access()
            image = self._get_image()
            image.display()
        except PermissionError as e:
            print(f"Smart Proxy: Access denied - {e}")
    
    def get_size(self):
        """Get size with all proxy features."""
        try:
            self._check_access()
            image = self._get_image()
            return image.get_size()
        except PermissionError as e:
            print(f"Smart Proxy: Access denied - {e}")
            return None

# Test smart proxy
smart_proxy = SmartImageProxy("smart_document.pdf", "user")
smart_proxy.authenticate(regular_user)
smart_proxy.display()

# What we accomplished in this step:
# - Tested all proxy types with different scenarios
# - Demonstrated lazy loading, caching, and access control
# - Showed how proxies can be combined for multiple features
# - Verified that proxies maintain the same interface as real objects


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Proxy pattern structure and implementation
# - Virtual proxy for lazy loading and performance
# - Caching proxy for avoiding repeated expensive operations
# - Protection proxy for access control and security
# - Smart proxy combining multiple proxy features
# - Transparent interface between proxy and real object
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHEN to use each type of proxy
# 4. Experiment with combining different proxy features
#
# Remember: The best way to learn is by doing!
# ===============================================================================