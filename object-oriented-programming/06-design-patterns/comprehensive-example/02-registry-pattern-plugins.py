"""Question: Create a class Plugin with a class attribute registry to keep
track of all plugin instances.
Use a class method to register a new plugin and
a static method to list all registered plugins.
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
# - What is a plugin registry? (central place to track all plugins)
# - How do you automatically register plugins? (in __init__)
# - What's the difference between class method and static method here?
# - How do you prevent duplicate registrations?
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


# Step 1: Define the Plugin class with registry
# ===============================================================================

# Explanation:
# Let's start by creating our Plugin class with a class attribute to serve as a registry.
# This registry will keep track of all plugin instances.

class Plugin:
    registry = []

# What we accomplished in this step:
# - Created Plugin class with class attribute registry


# Step 2: Add constructor with automatic registration
# ===============================================================================

# Explanation:
# The constructor should automatically register each new plugin instance.
# This ensures that all plugins are tracked without manual registration.

class Plugin:
    registry = []

    def __init__(self, name):
        self.name = name
        Plugin.registry.append(self)

# What we accomplished in this step:
# - Added constructor that automatically registers plugins
# - Each plugin has a name for identification


# Step 3: Add class method for manual registration
# ===============================================================================

# Explanation:
# Sometimes we might want to register plugins manually or register plugins
# created elsewhere. A class method provides this functionality.

class Plugin:
    registry = []

    def __init__(self, name):
        self.name = name
        Plugin.registry.append(self)

    @classmethod
    def register_plugin(cls, plugin):
        if plugin not in cls.registry:
            cls.registry.append(plugin)

# What we accomplished in this step:
# - Added class method for manual plugin registration
# - Added duplicate prevention


# Step 4: Add static method to list plugins
# ===============================================================================

# Explanation:
# A static method to list all registered plugins provides a clean interface
# for accessing plugin information without needing an instance.

class Plugin:
    registry = []

    def __init__(self, name):
        self.name = name
        Plugin.registry.append(self)

    @classmethod
    def register_plugin(cls, plugin):
        if plugin not in cls.registry:
            cls.registry.append(plugin)

    @staticmethod
    def list_plugins():
        return [plugin.name for plugin in Plugin.registry]

# What we accomplished in this step:
# - Added static method to list all plugin names


# Step 5: Add additional registry management methods
# ===============================================================================

# Explanation:
# Let's add more functionality to make our plugin registry more complete,
# including methods to find, remove, and get detailed information about plugins.

class Plugin:
    registry = []

    def __init__(self, name, version="1.0", description=""):
        self.name = name
        self.version = version
        self.description = description
        Plugin.registry.append(self)

    @classmethod
    def register_plugin(cls, plugin):
        if plugin not in cls.registry:
            cls.registry.append(plugin)

    @classmethod
    def unregister_plugin(cls, plugin):
        if plugin in cls.registry:
            cls.registry.remove(plugin)

    @classmethod
    def find_plugin(cls, name):
        for plugin in cls.registry:
            if plugin.name == name:
                return plugin
        return None

    @staticmethod
    def list_plugins():
        return [plugin.name for plugin in Plugin.registry]

    @staticmethod
    def get_plugin_count():
        return len(Plugin.registry)

    @classmethod
    def clear_registry(cls):
        cls.registry.clear()

# What we accomplished in this step:
# - Enhanced constructor with version and description
# - Added unregister_plugin method
# - Added find_plugin method
# - Added get_plugin_count static method
# - Added clear_registry for testing


# Step 6: Add string representation and plugin information
# ===============================================================================

# Explanation:
# Let's add methods to make our plugins more informative and easier to work with.

class Plugin:
    registry = []

    def __init__(self, name, version="1.0", description=""):
        self.name = name
        self.version = version
        self.description = description
        self.enabled = True
        Plugin.registry.append(self)

    @classmethod
    def register_plugin(cls, plugin):
        if plugin not in cls.registry:
            cls.registry.append(plugin)

    @classmethod
    def unregister_plugin(cls, plugin):
        if plugin in cls.registry:
            cls.registry.remove(plugin)

    @classmethod
    def find_plugin(cls, name):
        for plugin in cls.registry:
            if plugin.name == name:
                return plugin
        return None

    @staticmethod
    def list_plugins():
        return [plugin.name for plugin in Plugin.registry]

    @staticmethod
    def get_plugin_count():
        return len(Plugin.registry)

    @staticmethod
    def list_enabled_plugins():
        return [plugin.name for plugin in Plugin.registry if plugin.enabled]

    @classmethod
    def clear_registry(cls):
        cls.registry.clear()

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_info(self):
        return {
            'name': self.name,
            'version': self.version,
            'description': self.description,
            'enabled': self.enabled
        }

    def __str__(self):
        status = "Enabled" if self.enabled else "Disabled"
        return f"Plugin(name='{self.name}', version='{self.version}', {status})"

    def __repr__(self):
        return f"Plugin('{self.name}', '{self.version}', '{self.description}')"

# What we accomplished in this step:
# - Added enabled/disabled functionality
# - Added get_info method for detailed information
# - Added string representations
# - Added list_enabled_plugins static method


# Step 7: Test the plugin registry system
# ===============================================================================

# Explanation:
# Finally, let's test our complete plugin registry system to make sure
# all functionality works correctly.

class Plugin:
    registry = []

    def __init__(self, name, version="1.0", description=""):
        self.name = name
        self.version = version
        self.description = description
        self.enabled = True
        Plugin.registry.append(self)

    @classmethod
    def register_plugin(cls, plugin):
        if plugin not in cls.registry:
            cls.registry.append(plugin)

    @classmethod
    def unregister_plugin(cls, plugin):
        if plugin in cls.registry:
            cls.registry.remove(plugin)

    @classmethod
    def find_plugin(cls, name):
        for plugin in cls.registry:
            if plugin.name == name:
                return plugin
        return None

    @staticmethod
    def list_plugins():
        return [plugin.name for plugin in Plugin.registry]

    @staticmethod
    def get_plugin_count():
        return len(Plugin.registry)

    @staticmethod
    def list_enabled_plugins():
        return [plugin.name for plugin in Plugin.registry if plugin.enabled]

    @classmethod
    def clear_registry(cls):
        cls.registry.clear()

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_info(self):
        return {
            'name': self.name,
            'version': self.version,
            'description': self.description,
            'enabled': self.enabled
        }

    def __str__(self):
        status = "Enabled" if self.enabled else "Disabled"
        return f"Plugin(name='{self.name}', version='{self.version}', {status})"

    def __repr__(self):
        return f"Plugin('{self.name}', '{self.version}', '{self.description}')"

# Test our plugin registry system:
print("Testing Plugin Registry System:")

print(f"Initial plugin count: {Plugin.get_plugin_count()}")

# Create plugins automatically registered
plugin1 = Plugin("Database Connector", "2.1", "Connects to various databases")
plugin2 = Plugin("Authentication", "1.5", "Handles user authentication")
plugin3 = Plugin("Logging", "3.0", "Advanced logging capabilities")

print(f"After creating 3 plugins: {Plugin.get_plugin_count()}")
print(f"All plugins: {Plugin.list_plugins()}")

# Test manual registration
plugin4 = Plugin("Cache Manager", "1.2", "Manages application cache")
Plugin.register_plugin(plugin4)  # Already registered, should not duplicate

print(f"After manual registration: {Plugin.get_plugin_count()}")

# Test plugin information
print(f"\nPlugin details:")
for name in Plugin.list_plugins():
    plugin = Plugin.find_plugin(name)
    print(f"  {plugin}")

# Test enable/disable functionality
plugin2.disable()
print(f"\nEnabled plugins: {Plugin.list_enabled_plugins()}")
print(f"All plugins: {Plugin.list_plugins()}")

# Test finding plugins
found_plugin = Plugin.find_plugin("Database Connector")
if found_plugin:
    print(f"\nFound plugin: {found_plugin.get_info()}")

# Test unregistration
Plugin.unregister_plugin(plugin3)
print(f"\nAfter unregistering Logging plugin: {Plugin.list_plugins()}")

print(f"Final plugin count: {Plugin.get_plugin_count()}")

# What we accomplished in this step:
# - Created and tested our complete plugin registry system
# - Demonstrated automatic and manual registration
# - Showed plugin management functionality


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Plugin architecture and registry patterns
# - Class attributes for shared state management
# - Automatic registration in constructors
# - Class methods vs static methods usage
# - Plugin lifecycle management (enable/disable)
# - Information retrieval and plugin discovery
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding plugin dependencies or loading order!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================