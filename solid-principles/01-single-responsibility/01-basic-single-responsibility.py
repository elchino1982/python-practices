"""Question: Define a class User that has methods to get and set user information.
Refactor the class to adhere to the Single Responsibility Principle
by separating user information management from user authentication.
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
# - What is the Single Responsibility Principle (SRP)?
# - What are the different responsibilities in the User class?
# - How can you separate user information management from authentication?
# - What are the benefits of having classes with single responsibilities?
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


# Step 1: Identify the SRP violation in the original class
# ===============================================================================

# Explanation:
# Let's first look at the original User class that violates SRP by having
# multiple responsibilities: managing user information AND handling authentication.

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user_info(self):
        return {"username": self.username, "password": self.password}

    def authenticate(self, password):
        return self.password == password

# What we can observe:
# - The User class has TWO responsibilities:
#   1. Managing user information (username, password, get_user_info)
#   2. Handling authentication (authenticate method)
# - This violates SRP because the class has more than one reason to change

print("=== Original User Class (SRP Violation) ===")
user = User("john_doe", "securepassword")
print(f"User info: {user.get_user_info()}")
print(f"Authentication result: {user.authenticate('securepassword')}")


# Step 2: Refactor to separate user information management
# ===============================================================================

# Explanation:
# Let's create a UserInfo class that only handles user information,
# removing the authentication responsibility.

class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user_info(self):
        return {"username": self.username, "password": self.password}

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

# What we accomplished in this step:
# - UserInfo class now only manages user data
# - Added setter methods for better encapsulation
# - Removed authentication logic


# Step 3: Create separate UserAuth class for authentication
# ===============================================================================

# Explanation:
# Now let's create a separate class that handles user authentication,
# following the SRP by giving it a single responsibility.

class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user_info(self):
        return {"username": self.username, "password": self.password}

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

class UserAuth:
    def __init__(self, user_info):
        self.user_info = user_info

    def authenticate(self, password):
        return self.user_info.password == password

# What we accomplished in this step:
# - Created UserAuth class with single responsibility: authentication
# - Separated concerns: UserInfo handles data, UserAuth handles authentication
# - Each class now has only one reason to change


# Step 4: Test our SRP-compliant design
# ===============================================================================

# Explanation:
# Let's test our refactored design to ensure it works correctly and
# demonstrates the benefits of following SRP.

class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user_info(self):
        return {"username": self.username, "password": self.password}

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

class UserAuth:
    def __init__(self, user_info):
        self.user_info = user_info

    def authenticate(self, password):
        return self.user_info.password == password

# Test our SRP-compliant design:
print("\n=== SRP-Compliant Design ===")

user_info = UserInfo("john_doe", "securepassword")
user_auth = UserAuth(user_info)

print("Testing authentication:")
print(f"Correct password: {user_auth.authenticate('securepassword')}")
print(f"Wrong password: {user_auth.authenticate('wrongpassword')}")

print("\nTesting user info management:")
print(f"Original info: {user_info.get_user_info()}")
user_info.set_username("jane_doe")
user_info.set_password("newpassword")
print(f"Updated info: {user_info.get_user_info()}")

print("\nTesting authentication with updated info:")
print(f"Old password: {user_auth.authenticate('securepassword')}")
print(f"New password: {user_auth.authenticate('newpassword')}")

# What we accomplished in this step:
# - Demonstrated that our refactored design works correctly
# - Showed how UserInfo and UserAuth can be used independently
# - Verified that changes to user info automatically affect authentication


# Step 5: Enhanced example with advanced authentication features
# ===============================================================================

# Explanation:
# Let's create a more comprehensive example that shows the benefits of SRP
# by adding advanced authentication features without changing the UserInfo class.

class UserInfo:
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email
        self.created_at = self._get_current_time()

    def get_user_info(self):
        info = {"username": self.username, "email": self.email, "created_at": self.created_at}
        return info

    def get_secure_info(self):
        # Don't include password in secure info
        return self.get_user_info()

    def set_username(self, username):
        if username and len(username.strip()) >= 3:
            self.username = username.strip()
        else:
            raise ValueError("Username must be at least 3 characters")

    def set_password(self, password):
        if len(password) >= 6:
            self.password = password
        else:
            raise ValueError("Password must be at least 6 characters")

    def set_email(self, email):
        if "@" in email:
            self.email = email
        else:
            raise ValueError("Invalid email format")

    def _get_current_time(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class AdvancedUserAuth:
    def __init__(self, user_info):
        self.user_info = user_info
        self.failed_attempts = 0
        self.max_attempts = 3
        self.locked = False
        self.last_login = None

    def authenticate(self, password):
        if self.locked:
            return {"success": False, "message": "Account locked due to too many failed attempts"}

        if self.user_info.password == password:
            self.failed_attempts = 0
            self.last_login = self._get_current_time()
            return {"success": True, "message": "Authentication successful", "last_login": self.last_login}
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= self.max_attempts:
                self.locked = True
                return {"success": False, "message": "Account locked due to too many failed attempts"}
            else:
                remaining = self.max_attempts - self.failed_attempts
                return {"success": False, "message": f"Authentication failed. {remaining} attempts remaining"}

    def unlock_account(self):
        self.locked = False
        self.failed_attempts = 0
        return "Account unlocked"

    def get_auth_status(self):
        return {
            "locked": self.locked,
            "failed_attempts": self.failed_attempts,
            "last_login": self.last_login
        }

    def _get_current_time(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password, email=None):
        if username in self.users:
            raise ValueError("Username already exists")
        
        user_info = UserInfo(username, password, email)
        user_auth = AdvancedUserAuth(user_info)
        self.users[username] = {"info": user_info, "auth": user_auth}
        return f"User {username} created successfully"

    def login(self, username, password):
        if username not in self.users:
            return {"success": False, "message": "User not found"}
        
        user_auth = self.users[username]["auth"]
        return user_auth.authenticate(password)

    def get_user_info(self, username):
        if username in self.users:
            return self.users[username]["info"].get_secure_info()
        return None

# Test enhanced SRP design:
print("\n=== Enhanced SRP Design with Advanced Features ===")

user_service = UserService()

# Create users
print("Creating users:")
print(user_service.create_user("alice", "password123", "alice@example.com"))
print(user_service.create_user("bob", "securepass", "bob@example.com"))

# Test authentication
print("\nTesting authentication:")
result1 = user_service.login("alice", "password123")
print(f"Alice login (correct): {result1}")

result2 = user_service.login("alice", "wrongpass")
print(f"Alice login (wrong): {result2}")

result3 = user_service.login("alice", "wrongpass")
print(f"Alice login (wrong again): {result3}")

result4 = user_service.login("alice", "wrongpass")
print(f"Alice login (locked): {result4}")

# Test user info
print("\nTesting user info:")
alice_info = user_service.get_user_info("alice")
print(f"Alice info: {alice_info}")

# What we accomplished in this step:
# - Demonstrated how SRP enables easy extension with advanced features
# - UserInfo class remains unchanged when adding authentication features
# - Authentication logic can be enhanced without affecting user data management
# - System is more flexible and maintainable


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the Single Responsibility Principle solution!
#
# Key concepts learned:
# - Understanding the Single Responsibility Principle (SRP)
# - Identifying classes with multiple responsibilities
# - Separating concerns into different classes
# - Benefits of SRP: easier maintenance, testing, and extension
# - How SRP enables flexible system design
# - Creating authentication systems with proper separation of concerns
#
# SRP Benefits demonstrated:
# - UserInfo class can change without affecting authentication logic
# - Authentication logic can change without affecting UserInfo class
# - Easy to add new authentication features (account locking, login tracking)
# - Each class is easier to test in isolation
# - Code is more readable and maintainable
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each separation improves the design
# 4. Experiment with adding new authentication features or user properties
#
# Remember: The best way to learn is by doing!
# ===============================================================================
