"""Question: Create a class Config that uses the Borg pattern to ensure
all instances share the same state.
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
# - What is the Borg pattern and how does it differ from Singleton?
# - How can you make all instances share the same __dict__?
# - What is the role of _shared_state in the pattern?
# - How do you ensure state is shared across all instances?
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


# Step 1: Define the Borg base class
# ===============================================================================

# Explanation:
# Let's start by creating our Borg base class. The Borg pattern ensures that
# all instances of a class share the same state, even though they are different objects.

class Borg:
    pass  # We'll add the shared state mechanism next

# What we accomplished in this step:
# - Created the basic Borg class structure


# Step 2: Add shared state mechanism
# ===============================================================================

# Explanation:
# The key to the Borg pattern is having a class variable that stores the shared state.
# All instances will point their __dict__ to this shared state.

class Borg:
    _shared_state = {}

# What we accomplished in this step:
# - Added class variable to store shared state
# - This dictionary will be shared across all instances


# Step 3: Implement the constructor
# ===============================================================================

# Explanation:
# In the constructor, we assign the shared state dictionary to the instance's __dict__.
# This makes all instances share the same attribute storage.

class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

# What we accomplished in this step:
# - Added constructor that assigns shared state to instance __dict__
# - All instances will now share the same attribute storage


# Step 4: Create the Config class that inherits from Borg
# ===============================================================================

# Explanation:
# Now let's create our Config class that inherits from Borg and adds
# configuration-specific functionality.

class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Config(Borg):
    def __init__(self, **kwargs):
        super().__init__()
        # We'll add configuration update logic next

# What we accomplished in this step:
# - Created Config class that inherits from Borg
# - Added constructor that accepts keyword arguments for configuration


# Step 5: Add configuration update logic
# ===============================================================================

# Explanation:
# The Config constructor should update the shared state with any new
# configuration values passed as keyword arguments.

class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Config(Borg):
    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(kwargs)

# What we accomplished in this step:
# - Added logic to update shared state with new configuration values
# - All instances will see these updates immediately


# Step 6: Test our Borg pattern implementation
# ===============================================================================

# Explanation:
# Let's test our Borg pattern by creating multiple instances and verifying
# that they all share the same state.

class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Config(Borg):
    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(kwargs)

# Test our Borg pattern:
print("=== Testing Borg Pattern ===")

print("Creating first config instance:")
config1 = Config(database_url="localhost", debug=True)
print(f"config1.__dict__: {config1.__dict__}")
print(f"config1 id: {id(config1)}")

print("\nCreating second config instance:")
config2 = Config(port=8080, timeout=30)
print(f"config2.__dict__: {config2.__dict__}")
print(f"config2 id: {id(config2)}")

print("\nCreating third config instance:")
config3 = Config(api_key="secret123")
print(f"config3.__dict__: {config3.__dict__}")
print(f"config3 id: {id(config3)}")

print(f"\nAll instances share the same state:")
print(f"config1 == config2 (objects): {config1 is config2}")
print(f"config1.__dict__ is config2.__dict__ (state): {config1.__dict__ is config2.__dict__}")

# What we accomplished in this step:
# - Created multiple Config instances with different parameters
# - Verified that all instances share the same state
# - Demonstrated that objects are different but state is shared


# Step 7: Enhanced version with additional features
# ===============================================================================

# Explanation:
# Let's create an enhanced version that includes methods for managing
# configuration and demonstrates more advanced Borg pattern usage.

class EnhancedBorg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

    def get_state_info(self):
        return {
            'state_id': id(self.__dict__),
            'instance_id': id(self),
            'attributes': dict(self.__dict__)
        }

class EnhancedConfig(EnhancedBorg):
    def __init__(self, **kwargs):
        super().__init__()
        self.update_config(**kwargs)

    def update_config(self, **kwargs):
        """Update configuration with new values"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_config(self, key, default=None):
        """Get a configuration value"""
        return getattr(self, key, default)

    def remove_config(self, key):
        """Remove a configuration key"""
        if hasattr(self, key):
            delattr(self, key)

    def get_all_config(self):
        """Get all configuration as a dictionary"""
        return dict(self.__dict__)

    def clear_config(self):
        """Clear all configuration"""
        self.__dict__.clear()

# Test enhanced version:
print("\n=== Enhanced Borg Pattern with Configuration Management ===")

# Create instances
app_config = EnhancedConfig(app_name="MyApp", version="1.0")
db_config = EnhancedConfig(host="localhost", port=5432)
api_config = EnhancedConfig(endpoint="/api/v1", rate_limit=1000)

print("Configuration after creating all instances:")
print(f"app_config: {app_config.get_all_config()}")
print(f"db_config: {db_config.get_all_config()}")
print(f"api_config: {api_config.get_all_config()}")

print("\nTesting configuration methods:")
print(f"Get app_name: {app_config.get_config('app_name')}")
print(f"Get non-existent key: {db_config.get_config('missing_key', 'default_value')}")

print("\nUpdating configuration from one instance:")
app_config.update_config(debug=True, log_level="INFO")
print(f"All instances see the update: {api_config.get_all_config()}")

print("\nState information:")
for i, config in enumerate([app_config, db_config, api_config], 1):
    info = config.get_state_info()
    print(f"Instance {i}: state_id={info['state_id']}, instance_id={info['instance_id']}")

# What we accomplished in this step:
# - Enhanced the Borg pattern with configuration management methods
# - Added methods to get, set, and remove configuration values
# - Demonstrated that all instances share updates immediately
# - Provided state information for debugging


# Step 8: Comparison with Singleton pattern
# ===============================================================================

# Explanation:
# Let's compare the Borg pattern with the Singleton pattern to understand
# the differences and benefits of each approach.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = {}

class SingletonConfig(Singleton):
    def set_config(self, key, value):
        self.data[key] = value

    def get_config(self, key):
        return self.data.get(key)

# Compare patterns:
print("\n=== Comparing Borg vs Singleton ===")

print("Singleton pattern:")
singleton1 = SingletonConfig()
singleton2 = SingletonConfig()
singleton1.set_config("test", "value1")

print(f"singleton1 is singleton2: {singleton1 is singleton2}")
print(f"singleton1 id: {id(singleton1)}")
print(f"singleton2 id: {id(singleton2)}")
print(f"Both see the same data: {singleton2.get_config('test')}")

print("\nBorg pattern:")
borg1 = Config(test="value1")
borg2 = Config()

print(f"borg1 is borg2: {borg1 is borg2}")
print(f"borg1 id: {id(borg1)}")
print(f"borg2 id: {id(borg2)}")
print(f"Both see the same state: {borg2.test}")

print("\nKey differences:")
print("- Singleton: Same object instance, same identity")
print("- Borg: Different object instances, shared state")
print("- Borg allows normal inheritance and polymorphism")
print("- Singleton ensures only one instance exists")

# What we accomplished in this step:
# - Implemented a Singleton pattern for comparison
# - Demonstrated the key differences between Borg and Singleton
# - Showed that Borg allows multiple instances with shared state
# - Highlighted the benefits of each pattern


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the Borg pattern and its purpose
# - Implementing shared state across multiple instances
# - Using __dict__ assignment for state sharing
# - Comparing Borg pattern with Singleton pattern
# - Creating configuration management systems
# - Understanding when to use Borg vs Singleton
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a Borg-based cache system!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
