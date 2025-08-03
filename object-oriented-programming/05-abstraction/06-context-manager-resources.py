"""Question: Define a class Resource that uses the context management protocol
(__enter__ and __exit__ methods) to manage resources.
Ensure that resources are properly acquired and released.
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
# - What are the __enter__ and __exit__ methods used for?
# - When is __enter__ called and what should it return?
# - What parameters does __exit__ receive and what do they mean?
# - How do you use the 'with' statement to test context managers?
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


# Step 1: Define the Resource class
# ===============================================================================

# Explanation:
# Let's start by creating our Resource class. This class will implement the
# context management protocol, which allows it to be used with the 'with' statement.

class Resource:
    pass  # We'll add methods next

# What we accomplished in this step:
# - Created the basic Resource class structure


# Step 2: Add the __enter__ method
# ===============================================================================

# Explanation:
# The __enter__ method is called when entering the 'with' block. It should
# acquire the resource and return the object that will be assigned to the
# variable after 'as' in the with statement.

class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self  # Return self so it can be used in the with block

# What we accomplished in this step:
# - Added __enter__ method that simulates resource acquisition
# - Returns self to make the resource available in the with block


# Step 3: Add the __exit__ method
# ===============================================================================

# Explanation:
# The __exit__ method is called when exiting the 'with' block, whether normally
# or due to an exception. It receives information about any exception that occurred
# and should clean up the resource.

class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")
        # Return None (or False) to propagate any exceptions

# What we accomplished in this step:
# - Added __exit__ method that simulates resource cleanup
# - Accepts exception information parameters
# - Ensures resource is always released


# Step 4: Test our context manager
# ===============================================================================

# Explanation:
# Now let's test our Resource class using the 'with' statement. This will
# demonstrate how the context management protocol works in practice.

class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")

# Test our context manager:
print("=== Normal usage ===")
with Resource() as resource:
    print("Using resource")
    print(f"Resource object: {resource}")

print("\n=== Usage with exception ===")
try:
    with Resource() as resource:
        print("Using resource")
        raise ValueError("Something went wrong!")
        print("This won't be printed")
except ValueError as e:
    print(f"Caught exception: {e}")

# What we accomplished in this step:
# - Tested normal context manager usage
# - Tested behavior when exceptions occur
# - Verified that resources are always released


# Step 5: Enhanced version with resource name
# ===============================================================================

# Explanation:
# Let's create an enhanced version that can manage different types of resources
# and provides more detailed logging.

class Resource:
    def __init__(self, name="Generic Resource"):
        self.name = name
        self.is_acquired = False

    def __enter__(self):
        print(f"Acquiring {self.name}")
        self.is_acquired = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Releasing {self.name}")
        self.is_acquired = False
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        # Return False to propagate exceptions

    def do_work(self):
        if self.is_acquired:
            print(f"Working with {self.name}")
        else:
            print(f"Cannot work with {self.name} - not acquired")

# Test enhanced version:
print("\n=== Enhanced Resource Manager ===")
with Resource("Database Connection") as db:
    db.do_work()

with Resource("File Handle") as file:
    file.do_work()

# What we accomplished in this step:
# - Enhanced the Resource class with named resources
# - Added state tracking with is_acquired
# - Provided better exception information
# - Added a method to demonstrate resource usage


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Understanding the context management protocol (__enter__ and __exit__)
# - How the 'with' statement works with context managers
# - Proper resource acquisition and cleanup patterns
# - Exception handling in context managers
# - Creating reusable resource management classes
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try creating a FileResource that actually opens files!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
