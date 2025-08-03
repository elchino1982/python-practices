"""Question: Create a class Database with methods connect and disconnect.
Implement a class Application that depends on Database.
Refactor the classes to adhere to
the Dependency Inversion Principle by introducing an interface DatabaseConnection.
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
# - What is the Dependency Inversion Principle (DIP)?
# - How does the original Application class violate DIP?
# - What is the difference between depending on abstractions vs. concrete classes?
# - How can you create an interface that both Application and Database can depend on?
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


# Step 1: Identify the DIP violation in the original design
# ===============================================================================

# Explanation:
# Let's examine the original Application and Database classes that violate DIP by
# having Application directly depend on the concrete Database class.

class Database:
    def connect(self):
        return "Database connected"

    def disconnect(self):
        return "Database disconnected"

class Application:
    def __init__(self, database):
        self.database = database  # Direct dependency on concrete Database class

    def start(self):
        return self.database.connect()

    def stop(self):
        return self.database.disconnect()

# What we can observe:
# - Application directly depends on Database (concrete class)
# - This violates DIP: high-level module (Application) depends on low-level module (Database)
# - Application is tightly coupled to Database
# - Hard to test Application with different database types
# - Difficult to add new database implementations

print("=== Original Design (DIP Violation) ===")
database = Database()
app = Application(database)
start_result = app.start()
stop_result = app.stop()
print(f"Start: {start_result}")
print(f"Stop: {stop_result}")
print("DIP Violation: Application directly depends on concrete Database class!")


# Step 2: Create an abstraction for database connections
# ===============================================================================

# Explanation:
# Let's create an abstract interface that defines the contract for database
# connections, following DIP by depending on abstractions.

from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

# What we accomplished in this step:
# - Created DatabaseConnection abstraction that defines the interface
# - This abstraction will be the dependency for high-level modules
# - Concrete implementations will depend on this abstraction


# Step 3: Implement Database as a concrete database connection
# ===============================================================================

# Explanation:
# Now let's implement Database as a concrete implementation of the
# DatabaseConnection abstraction.

from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Database(DatabaseConnection):
    def connect(self):
        return "Database connected"

    def disconnect(self):
        return "Database disconnected"

# What we accomplished in this step:
# - Database now implements DatabaseConnection abstraction
# - Low-level module (Database) depends on abstraction (DatabaseConnection)
# - Follows DIP: concrete implementation depends on abstraction


# Step 4: Refactor Application to depend on abstraction
# ===============================================================================

# Explanation:
# Let's refactor Application to depend on the DatabaseConnection abstraction
# instead of the concrete Database implementation.

from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Database(DatabaseConnection):
    def connect(self):
        return "Database connected"

    def disconnect(self):
        return "Database disconnected"

class Application:
    def __init__(self, database: DatabaseConnection):
        self.database = database  # Depends on abstraction

    def start(self):
        return self.database.connect()

    def stop(self):
        return self.database.disconnect()

# What we accomplished in this step:
# - Application now depends on DatabaseConnection abstraction
# - Uses dependency injection to receive the database connection
# - High-level module (Application) depends on abstraction (DatabaseConnection)
# - Follows DIP: both modules depend on abstraction


# Step 5: Test our DIP-compliant design
# ===============================================================================

# Explanation:
# Let's test our refactored design to verify that it follows DIP
# and provides the same functionality with better flexibility.

from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Database(DatabaseConnection):
    def connect(self):
        return "Database connected"

    def disconnect(self):
        return "Database disconnected"

class Application:
    def __init__(self, database: DatabaseConnection):
        self.database = database

    def start(self):
        return self.database.connect()

    def stop(self):
        return self.database.disconnect()

# Test our DIP-compliant design:
print("\n=== DIP-Compliant Design ===")

database = Database()
app = Application(database)
start_result = app.start()
stop_result = app.stop()
print(f"Start: {start_result}")
print(f"Stop: {stop_result}")
print("DIP Success: Application depends on DatabaseConnection abstraction!")

# What we accomplished in this step:
# - Verified that our refactored design works correctly
# - Application now depends on abstraction instead of concrete implementation
# - System is more flexible and follows DIP


# Step 6: Demonstrate DIP benefits by adding new database types
# ===============================================================================

# Explanation:
# Let's prove that our DIP-compliant design is flexible by adding new
# database types without modifying existing code.

from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Database(DatabaseConnection):
    def connect(self):
        return "MySQL Database connected"

    def disconnect(self):
        return "MySQL Database disconnected"

# Adding new database types without modifying existing code (DIP benefit!)
class PostgreSQLDatabase(DatabaseConnection):
    def connect(self):
        return "PostgreSQL Database connected"

    def disconnect(self):
        return "PostgreSQL Database disconnected"

class MongoDatabase(DatabaseConnection):
    def connect(self):
        return "MongoDB connected"

    def disconnect(self):
        return "MongoDB disconnected"

class RedisDatabase(DatabaseConnection):
    def connect(self):
        return "Redis Cache connected"

    def disconnect(self):
        return "Redis Cache disconnected"

class Application:
    def __init__(self, database: DatabaseConnection):
        self.database = database

    def start(self):
        return self.database.connect()

    def stop(self):
        return self.database.disconnect()

print("\n=== Demonstrating DIP Benefits (Multiple Database Types) ===")

# Test with different database types
databases = [
    Database(),
    PostgreSQLDatabase(),
    MongoDatabase(),
    RedisDatabase()
]

for database in databases:
    app = Application(database)
    db_name = database.__class__.__name__
    start_result = app.start()
    stop_result = app.stop()
    print(f"{db_name}:")
    print(f"  Start: {start_result}")
    print(f"  Stop: {stop_result}")

print("\nDIP Benefits: Easy to add new database types without modifying Application!")

# What we accomplished in this step:
# - Added multiple database types without modifying Application
# - Demonstrated flexibility and extensibility of DIP-compliant design
# - Showed how abstraction enables easy database switching


# Step 7: Enhanced example with enterprise application architecture
# ===============================================================================

# Explanation:
# Let's create a more comprehensive example that shows advanced DIP
# applications with an enterprise application architecture.

from abc import ABC, abstractmethod
import json

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    @abstractmethod
    def get_connection_info(self):
        pass

class CacheConnection(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def set(self, key, value):
        pass

class MessageQueueConnection(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def send_message(self, queue, message):
        pass
    
    @abstractmethod
    def receive_message(self, queue):
        pass

# Enhanced database implementations
class MySQLDatabase(DatabaseConnection):
    def __init__(self, host, port, username, database_name):
        self.host = host
        self.port = port
        self.username = username
        self.database_name = database_name
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        return f"MySQL connected to {self.host}:{self.port}/{self.database_name}"

    def disconnect(self):
        self.is_connected = False
        return f"MySQL disconnected from {self.database_name}"

    def execute_query(self, query):
        if not self.is_connected:
            return "Error: Database not connected"
        return f"MySQL executed: {query[:50]}..."

    def get_connection_info(self):
        return {
            "type": "MySQL",
            "host": self.host,
            "port": self.port,
            "database": self.database_name,
            "connected": self.is_connected
        }

class PostgreSQLDatabase(DatabaseConnection):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        return f"PostgreSQL connected using connection string"

    def disconnect(self):
        self.is_connected = False
        return "PostgreSQL disconnected"

    def execute_query(self, query):
        if not self.is_connected:
            return "Error: Database not connected"
        return f"PostgreSQL executed: {query[:50]}..."

    def get_connection_info(self):
        return {
            "type": "PostgreSQL",
            "connection_string": self.connection_string[:20] + "...",
            "connected": self.is_connected
        }

class MongoDatabase(DatabaseConnection):
    def __init__(self, cluster_url, database_name):
        self.cluster_url = cluster_url
        self.database_name = database_name
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        return f"MongoDB connected to cluster {self.database_name}"

    def disconnect(self):
        self.is_connected = False
        return f"MongoDB disconnected from {self.database_name}"

    def execute_query(self, query):
        if not self.is_connected:
            return "Error: Database not connected"
        return f"MongoDB executed: {query[:50]}..."

    def get_connection_info(self):
        return {
            "type": "MongoDB",
            "cluster": self.cluster_url,
            "database": self.database_name,
            "connected": self.is_connected
        }

# Cache implementations
class RedisCache(CacheConnection):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.is_connected = False
        self.cache_data = {}

    def connect(self):
        self.is_connected = True
        return f"Redis connected to {self.host}:{self.port}"

    def disconnect(self):
        self.is_connected = False
        return f"Redis disconnected from {self.host}:{self.port}"

    def get(self, key):
        if not self.is_connected:
            return None
        return self.cache_data.get(key)

    def set(self, key, value):
        if not self.is_connected:
            return False
        self.cache_data[key] = value
        return True

class MemcachedCache(CacheConnection):
    def __init__(self, servers):
        self.servers = servers
        self.is_connected = False
        self.cache_data = {}

    def connect(self):
        self.is_connected = True
        return f"Memcached connected to {len(self.servers)} servers"

    def disconnect(self):
        self.is_connected = False
        return f"Memcached disconnected from all servers"

    def get(self, key):
        if not self.is_connected:
            return None
        return self.cache_data.get(key)

    def set(self, key, value):
        if not self.is_connected:
            return False
        self.cache_data[key] = value
        return True

# Message queue implementations
class RabbitMQQueue(MessageQueueConnection):
    def __init__(self, host, virtual_host):
        self.host = host
        self.virtual_host = virtual_host
        self.is_connected = False
        self.queues = {}

    def connect(self):
        self.is_connected = True
        return f"RabbitMQ connected to {self.host}/{self.virtual_host}"

    def disconnect(self):
        self.is_connected = False
        return f"RabbitMQ disconnected from {self.host}"

    def send_message(self, queue, message):
        if not self.is_connected:
            return False
        if queue not in self.queues:
            self.queues[queue] = []
        self.queues[queue].append(message)
        return True

    def receive_message(self, queue):
        if not self.is_connected or queue not in self.queues:
            return None
        return self.queues[queue].pop(0) if self.queues[queue] else None

# Enterprise application components that depend on abstractions
class DataAccessLayer:
    def __init__(self, database: DatabaseConnection):
        self.database = database

    def initialize(self):
        return self.database.connect()

    def shutdown(self):
        return self.database.disconnect()

    def get_user(self, user_id):
        query = f"SELECT * FROM users WHERE id = {user_id}"
        return self.database.execute_query(query)

    def create_user(self, user_data):
        query = f"INSERT INTO users (name, email) VALUES ('{user_data['name']}', '{user_data['email']}')"
        return self.database.execute_query(query)

    def get_database_info(self):
        return self.database.get_connection_info()

class CacheLayer:
    def __init__(self, cache: CacheConnection):
        self.cache = cache

    def initialize(self):
        return self.cache.connect()

    def shutdown(self):
        return self.cache.disconnect()

    def get_cached_data(self, key):
        return self.cache.get(key)

    def cache_data(self, key, data):
        return self.cache.set(key, json.dumps(data))

class MessagingLayer:
    def __init__(self, message_queue: MessageQueueConnection):
        self.message_queue = message_queue

    def initialize(self):
        return self.message_queue.connect()

    def shutdown(self):
        return self.message_queue.disconnect()

    def publish_event(self, event_type, event_data):
        message = {"type": event_type, "data": event_data, "timestamp": "2025-01-01T00:00:00Z"}
        return self.message_queue.send_message("events", json.dumps(message))

    def consume_event(self):
        message = self.message_queue.receive_message("events")
        return json.loads(message) if message else None

class EnterpriseApplication:
    def __init__(self, database: DatabaseConnection, cache: CacheConnection, message_queue: MessageQueueConnection):
        self.data_layer = DataAccessLayer(database)
        self.cache_layer = CacheLayer(cache)
        self.messaging_layer = MessagingLayer(message_queue)
        self.is_running = False

    def startup(self):
        """Initialize all application layers"""
        results = []
        
        # Initialize database
        db_result = self.data_layer.initialize()
        results.append(f"Database: {db_result}")
        
        # Initialize cache
        cache_result = self.cache_layer.initialize()
        results.append(f"Cache: {cache_result}")
        
        # Initialize messaging
        msg_result = self.messaging_layer.initialize()
        results.append(f"Messaging: {msg_result}")
        
        self.is_running = True
        results.append("Application startup completed successfully")
        return results

    def shutdown(self):
        """Shutdown all application layers"""
        results = []
        
        # Shutdown messaging
        msg_result = self.messaging_layer.shutdown()
        results.append(f"Messaging: {msg_result}")
        
        # Shutdown cache
        cache_result = self.cache_layer.shutdown()
        results.append(f"Cache: {cache_result}")
        
        # Shutdown database
        db_result = self.data_layer.shutdown()
        results.append(f"Database: {db_result}")
        
        self.is_running = False
        results.append("Application shutdown completed successfully")
        return results

    def create_user_with_caching(self, user_data):
        """Business operation that uses multiple layers"""
        if not self.is_running:
            return "Application not running"
        
        # Create user in database
        db_result = self.data_layer.create_user(user_data)
        
        # Cache user data
        cache_key = f"user_{user_data.get('email', 'unknown')}"
        self.cache_layer.cache_data(cache_key, user_data)
        
        # Publish user creation event
        self.messaging_layer.publish_event("user_created", user_data)
        
        return f"User created: {db_result}"

    def get_user_with_caching(self, user_id):
        """Business operation with cache-first strategy"""
        if not self.is_running:
            return "Application not running"
        
        # Try cache first
        cache_key = f"user_{user_id}"
        cached_data = self.cache_layer.get_cached_data(cache_key)
        
        if cached_data:
            return f"User from cache: {cached_data}"
        
        # Fallback to database
        db_result = self.data_layer.get_user(user_id)
        return f"User from database: {db_result}"

    def get_system_status(self):
        """Get status of all system components"""
        return {
            "application_running": self.is_running,
            "database_info": self.data_layer.get_database_info(),
            "cache_connected": True,  # Simplified for demo
            "messaging_connected": True  # Simplified for demo
        }

class ApplicationFactory:
    """Factory that creates applications with different infrastructure configurations"""
    
    @staticmethod
    def create_development_app():
        """Create app with lightweight development infrastructure"""
        database = MySQLDatabase("localhost", 3306, "dev_user", "dev_db")
        cache = RedisCache("localhost", 6379)
        message_queue = RabbitMQQueue("localhost", "dev_vhost")
        return EnterpriseApplication(database, cache, message_queue)
    
    @staticmethod
    def create_production_app():
        """Create app with production infrastructure"""
        database = PostgreSQLDatabase("postgresql://prod_user:password@prod-cluster/prod_db")
        cache = MemcachedCache(["cache1.prod.com", "cache2.prod.com"])
        message_queue = RabbitMQQueue("mq.prod.com", "prod_vhost")
        return EnterpriseApplication(database, cache, message_queue)
    
    @staticmethod
    def create_cloud_app():
        """Create app with cloud infrastructure"""
        database = MongoDatabase("mongodb+srv://cluster.cloud.com", "cloud_db")
        cache = RedisCache("redis.cloud.com", 6380)
        message_queue = RabbitMQQueue("mq.cloud.com", "cloud_vhost")
        return EnterpriseApplication(database, cache, message_queue)

# Test enhanced DIP design:
print("\n=== Enhanced DIP Design with Enterprise Architecture ===")

# Create different application configurations
print("Creating different application environments:")

environments = [
    ("Development", ApplicationFactory.create_development_app()),
    ("Production", ApplicationFactory.create_production_app()),
    ("Cloud", ApplicationFactory.create_cloud_app())
]

for env_name, app in environments:
    print(f"\n=== {env_name} Environment ===")
    
    # Startup application
    print("Starting up application:")
    startup_results = app.startup()
    for result in startup_results:
        print(f"  {result}")
    
    # Perform business operations
    print("\nPerforming business operations:")
    user_data = {"name": f"{env_name} User", "email": f"user@{env_name.lower()}.com"}
    create_result = app.create_user_with_caching(user_data)
    print(f"  {create_result}")
    
    get_result = app.get_user_with_caching(123)
    print(f"  {get_result}")
    
    # Get system status
    print("\nSystem status:")
    status = app.get_system_status()
    print(f"  Application running: {status['application_running']}")
    print(f"  Database type: {status['database_info']['type']}")
    print(f"  Database connected: {status['database_info']['connected']}")
    
    # Shutdown application
    print("\nShutting down application:")
    shutdown_results = app.shutdown()
    for result in shutdown_results:
        print(f"  {result}")

# What we accomplished in this step:
# - Created comprehensive enterprise architecture using DIP
# - Demonstrated multiple abstractions (Database, Cache, MessageQueue)
# - Showed how DIP enables flexible infrastructure configuration
# - Illustrated real-world application of dependency injection in enterprise systems


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the advanced Dependency Inversion Principle solution!
#
# Key concepts learned:
# - Advanced application of DIP in enterprise architecture
# - Creating flexible systems that support multiple infrastructure providers
# - Separating high-level business logic from low-level infrastructure concerns
# - Using dependency injection to configure different environments
# - Benefits of DIP in complex, real-world enterprise systems
# - How DIP enables easy switching between different technology stacks
#
# Advanced DIP Benefits demonstrated:
# - Application logic is completely independent of infrastructure choices
# - Easy to switch between MySQL, PostgreSQL, MongoDB without code changes
# - Different cache providers (Redis, Memcached) can be used interchangeably
# - Message queue implementations can be swapped without affecting business logic
# - Environment-specific configurations (dev, prod, cloud) are easily managed
# - Testing becomes easier with mock implementations of abstractions
# - Infrastructure changes don't cascade to business logic
#
# Real-world applications:
# - Microservices architecture with pluggable infrastructure components
# - Multi-tenant applications with different database configurations per tenant
# - Cloud-native applications that can run on different cloud providers
# - Enterprise applications with environment-specific infrastructure
# - Integration platforms that support multiple third-party services
# - A/B testing different infrastructure providers for performance optimization
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY depending on abstractions enables infrastructure flexibility
# 4. Experiment with adding new database types or infrastructure components
#
# Remember: The best way to learn is by doing!
# ===============================================================================
