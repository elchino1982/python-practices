"""Question: Implement a class Proxy that uses the Proxy pattern to control
access to another object.
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
# - What is the Proxy pattern and when is it useful?
# - How do you create a proxy that controls access to another object?
# - What methods should both the proxy and real subject implement?
# - How do you add access control, logging, or caching to the proxy?
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


# Step 1: Define the RealSubject class
# ===============================================================================

# Explanation:
# Let's start by creating the RealSubject class. This is the actual object
# that does the real work. The proxy will control access to this object.

class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

# What we accomplished in this step:
# - Created the RealSubject class that performs the actual work
# - Added a request method that represents the core functionality


# Step 2: Define the Proxy class
# ===============================================================================

# Explanation:
# Now let's create the Proxy class. The proxy will hold a reference to the
# RealSubject and control access to it.

class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

# What we accomplished in this step:
# - Created Proxy class that holds a reference to RealSubject
# - Added constructor to initialize the proxy with a real subject


# Step 3: Add the request method to the Proxy
# ===============================================================================

# Explanation:
# The proxy should implement the same interface as the RealSubject.
# We'll add a request method that can control access to the real subject.

class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # We'll add access control logic next
        return self._real_subject.request()

# What we accomplished in this step:
# - Added request method to proxy that delegates to real subject
# - Proxy now implements the same interface as RealSubject


# Step 4: Add access control logic
# ===============================================================================

# Explanation:
# Now let's add access control to the proxy. We'll create a method to check
# access and only allow the request if access is granted.

class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            return self._real_subject.request()
        else:
            return "Proxy: Access denied."

    def check_access(self):
        # Simulate access control
        return True

# What we accomplished in this step:
# - Added check_access method to control access
# - Proxy now only delegates to real subject if access is allowed
# - Returns access denied message when access is not granted


# Step 5: Test our basic Proxy implementation
# ===============================================================================

# Explanation:
# Let's test our basic proxy implementation to see how it controls access
# to the real subject.

class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            return self._real_subject.request()
        else:
            return "Proxy: Access denied."

    def check_access(self):
        # Simulate access control
        return True

# Test our basic proxy:
print("=== Testing Basic Proxy Pattern ===")

real_subject = RealSubject()
proxy = Proxy(real_subject)

print("Testing proxy with access allowed:")
result = proxy.request()
print(f"Result: {result}")

print("\nTesting direct access to real subject:")
direct_result = real_subject.request()
print(f"Direct result: {direct_result}")

# What we accomplished in this step:
# - Created instances of RealSubject and Proxy
# - Tested proxy delegation to real subject
# - Verified that proxy controls access while maintaining same interface


# Step 6: Enhanced Proxy with dynamic access control
# ===============================================================================

# Explanation:
# Let's create an enhanced version that includes more sophisticated access
# control, logging, and additional proxy features.

class EnhancedRealSubject:
    def __init__(self, name):
        self.name = name

    def request(self, data):
        return f"RealSubject '{self.name}': Processing request with data: {data}"

    def sensitive_operation(self, secret_data):
        return f"RealSubject '{self.name}': Performed sensitive operation with: {secret_data}"

class EnhancedProxy:
    def __init__(self, real_subject, user_role="guest"):
        self._real_subject = real_subject
        self.user_role = user_role
        self.access_log = []

    def request(self, data):
        self._log_access("request", data)
        if self._check_access("request"):
            result = self._real_subject.request(data)
            self._log_access("request_success", data)
            return result
        else:
            self._log_access("request_denied", data)
            return "Proxy: Access denied for request operation."

    def sensitive_operation(self, secret_data):
        self._log_access("sensitive_operation", "***REDACTED***")
        if self._check_access("sensitive_operation"):
            result = self._real_subject.sensitive_operation(secret_data)
            self._log_access("sensitive_operation_success", "***REDACTED***")
            return result
        else:
            self._log_access("sensitive_operation_denied", "***REDACTED***")
            return "Proxy: Access denied for sensitive operation."

    def _check_access(self, operation):
        """Check if current user has access to the operation"""
        if operation == "request":
            return True  # All users can make basic requests
        elif operation == "sensitive_operation":
            return self.user_role in ["admin", "manager"]  # Only privileged users
        return False

    def _log_access(self, action, data):
        """Log access attempts"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.access_log.append(f"[{timestamp}] {self.user_role}: {action} - {data}")

    def get_access_log(self):
        """Get the access log"""
        return self.access_log

    def set_user_role(self, role):
        """Change user role (for testing)"""
        self.user_role = role
        self._log_access("role_changed", role)

# Test enhanced proxy:
print("\n=== Enhanced Proxy with Access Control and Logging ===")

real_subject = EnhancedRealSubject("DatabaseService")

# Test with guest user
guest_proxy = EnhancedProxy(real_subject, "guest")
print("Testing with guest user:")
print(guest_proxy.request("user_data"))
print(guest_proxy.sensitive_operation("secret_key"))

# Test with admin user
admin_proxy = EnhancedProxy(real_subject, "admin")
print("\nTesting with admin user:")
print(admin_proxy.request("admin_data"))
print(admin_proxy.sensitive_operation("secret_key"))

# Show access logs
print("\nGuest access log:")
for log_entry in guest_proxy.get_access_log():
    print(f"  {log_entry}")

print("\nAdmin access log:")
for log_entry in admin_proxy.get_access_log():
    print(f"  {log_entry}")

# What we accomplished in this step:
# - Enhanced proxy with role-based access control
# - Added logging functionality to track access attempts
# - Demonstrated different access levels for different operations
# - Showed how proxy can add security without changing real subject


# Step 7: Caching Proxy for performance optimization
# ===============================================================================

# Explanation:
# Let's create a caching proxy that stores results to improve performance
# for expensive operations.

class ExpensiveService:
    def __init__(self):
        self.call_count = 0

    def expensive_calculation(self, n):
        self.call_count += 1
        print(f"  ExpensiveService: Performing calculation #{self.call_count} for n={n}")
        # Simulate expensive calculation
        import time
        time.sleep(0.1)  # Simulate delay
        return n * n * n  # Cube calculation

class CachingProxy:
    def __init__(self, service):
        self._service = service
        self._cache = {}
        self.cache_hits = 0
        self.cache_misses = 0

    def expensive_calculation(self, n):
        if n in self._cache:
            self.cache_hits += 1
            print(f"  CachingProxy: Cache HIT for n={n}")
            return self._cache[n]
        else:
            self.cache_misses += 1
            print(f"  CachingProxy: Cache MISS for n={n}")
            result = self._service.expensive_calculation(n)
            self._cache[n] = result
            return result

    def get_cache_stats(self):
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0
        return {
            'cache_hits': self.cache_hits,
            'cache_misses': self.cache_misses,
            'hit_rate': f"{hit_rate:.1f}%",
            'cached_values': dict(self._cache)
        }

    def clear_cache(self):
        self._cache.clear()
        print("  CachingProxy: Cache cleared")

# Test caching proxy:
print("\n=== Caching Proxy for Performance Optimization ===")

service = ExpensiveService()
caching_proxy = CachingProxy(service)

print("Making requests through caching proxy:")
test_values = [5, 3, 5, 7, 3, 5, 10, 7]

for value in test_values:
    result = caching_proxy.expensive_calculation(value)
    print(f"  Result for {value}: {result}")

print(f"\nCache statistics:")
stats = caching_proxy.get_cache_stats()
for key, value in stats.items():
    print(f"  {key}: {value}")

print(f"\nService was called {service.call_count} times (instead of {len(test_values)} without caching)")

# What we accomplished in this step:
# - Created caching proxy that stores expensive calculation results
# - Demonstrated performance benefits of caching
# - Added cache statistics to monitor effectiveness
# - Showed how proxy can add functionality without changing service


# Step 8: Virtual Proxy for lazy initialization
# ===============================================================================

# Explanation:
# Let's create a virtual proxy that delays the creation of expensive objects
# until they are actually needed.

class HeavyResource:
    def __init__(self, resource_id):
        print(f"  HeavyResource: Creating expensive resource {resource_id}...")
        import time
        time.sleep(0.2)  # Simulate expensive initialization
        self.resource_id = resource_id
        self.data = f"Heavy data for resource {resource_id}"
        print(f"  HeavyResource: Resource {resource_id} created successfully")

    def get_data(self):
        return f"HeavyResource {self.resource_id}: {self.data}"

    def process(self, input_data):
        return f"HeavyResource {self.resource_id}: Processed '{input_data}'"

class VirtualProxy:
    def __init__(self, resource_id):
        self.resource_id = resource_id
        self._real_resource = None

    def _get_real_resource(self):
        """Lazy initialization of the real resource"""
        if self._real_resource is None:
            print(f"  VirtualProxy: Initializing real resource {self.resource_id}")
            self._real_resource = HeavyResource(self.resource_id)
        return self._real_resource

    def get_data(self):
        return self._get_real_resource().get_data()

    def process(self, input_data):
        return self._get_real_resource().process(input_data)

# Test virtual proxy:
print("\n=== Virtual Proxy for Lazy Initialization ===")

print("Creating virtual proxies (should be fast):")
proxy1 = VirtualProxy("DB_CONNECTION_1")
proxy2 = VirtualProxy("DB_CONNECTION_2")
proxy3 = VirtualProxy("DB_CONNECTION_3")
print("All proxies created instantly!")

print("\nUsing proxy1 (will trigger real resource creation):")
result1 = proxy1.get_data()
print(f"Result: {result1}")

print("\nUsing proxy1 again (real resource already exists):")
result2 = proxy1.process("test_data")
print(f"Result: {result2}")

print("\nUsing proxy2 (will trigger another real resource creation):")
result3 = proxy2.get_data()
print(f"Result: {result3}")

print("\nproxy3 was never used, so its real resource was never created!")

# What we accomplished in this step:
# - Created virtual proxy that delays expensive object creation
# - Demonstrated lazy initialization benefits
# - Showed how proxy can improve application startup time
# - Illustrated that unused proxies don't create expensive resources


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Proxy pattern and its various types
# - Implementing access control and security through proxies
# - Adding logging and monitoring capabilities
# - Creating caching proxies for performance optimization
# - Using virtual proxies for lazy initialization
# - Understanding when and why to use different proxy types
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a remote proxy for network services!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
