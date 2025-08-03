"""Question: Implement the Chain of Responsibility pattern to pass requests along a chain of handlers.

Create a customer support system where different types of issues (billing, technical, general)
are handled by different support levels (Level1, Level2, Manager) in a chain.

Requirements:
1. Create abstract Handler class with handle_request method
2. Implement concrete handlers for different support levels
3. Set up chain of handlers with next_handler references
4. Implement request passing mechanism
5. Demonstrate how requests flow through the chain
6. Show how handlers can be dynamically reconfigured

Example usage:
    level1 = Level1Support()
    level2 = Level2Support()
    manager = ManagerSupport()
    level1.set_next(level2).set_next(manager)
    level1.handle_request("billing_issue")
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
# - What is the abstract handler interface?
# - How do handlers link to the next handler?
# - How do requests flow through the chain?
# - What happens when a handler can't process a request?
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


# Step 1: Import modules and create the request class
# ===============================================================================

# Explanation:
# The Chain of Responsibility pattern starts with requests that need to be handled.
# We'll create a SupportRequest class to represent different types of issues.

from abc import ABC, abstractmethod
from typing import Optional

class SupportRequest:
    """Represents a customer support request."""
    
    def __init__(self, request_type: str, description: str, priority: str = "normal"):
        self.request_type = request_type  # billing, technical, general
        self.description = description
        self.priority = priority  # low, normal, high, urgent
        self.handled_by = None
    
    def __str__(self):
        """String representation of the request."""
        status = f"Handled by: {self.handled_by}" if self.handled_by else "Status: Unhandled"
        return f"Request Type: {self.request_type}\nDescription: {self.description}\nPriority: {self.priority}\n{status}"

# What we accomplished in this step:
# - Created the SupportRequest class to represent requests
# - Added attributes for type, description, priority, and handler tracking


# Step 2: Create the abstract handler interface
# ===============================================================================

# Explanation:
# The abstract handler defines the interface for handling requests and
# maintaining the chain. Each handler has a reference to the next handler.

from abc import ABC, abstractmethod
from typing import Optional

class SupportRequest:
    """Represents a customer support request."""
    
    def __init__(self, request_type: str, description: str, priority: str = "normal"):
        self.request_type = request_type  # billing, technical, general
        self.description = description
        self.priority = priority  # low, normal, high, urgent
        self.handled_by = None
    
    def __str__(self):
        """String representation of the request."""
        status = f"Handled by: {self.handled_by}" if self.handled_by else "Status: Unhandled"
        return f"Request Type: {self.request_type}\nDescription: {self.description}\nPriority: {self.priority}\n{status}"

class SupportHandler(ABC):
    """Abstract base class for support handlers."""
    
    def __init__(self):
        self._next_handler: Optional['SupportHandler'] = None
    
    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler  # Return handler for method chaining
    
    @abstractmethod
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle the request. Return True if handled, False otherwise."""
        pass
    
    def _pass_to_next(self, request: SupportRequest) -> bool:
        """Pass the request to the next handler in the chain."""
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return False

# What we accomplished in this step:
# - Created abstract SupportHandler with chain management
# - Added set_next method for building the chain
# - Added abstract handle_request method for processing
# - Added helper method to pass requests to next handler


# Step 3: Create concrete handler for Level 1 Support
# ===============================================================================

# Explanation:
# Level 1 Support handles basic general inquiries and simple technical issues.
# If they can't handle it, they pass it to the next level.

from abc import ABC, abstractmethod
from typing import Optional

class SupportRequest:
    """Represents a customer support request."""
    
    def __init__(self, request_type: str, description: str, priority: str = "normal"):
        self.request_type = request_type  # billing, technical, general
        self.description = description
        self.priority = priority  # low, normal, high, urgent
        self.handled_by = None
    
    def __str__(self):
        """String representation of the request."""
        status = f"Handled by: {self.handled_by}" if self.handled_by else "Status: Unhandled"
        return f"Request Type: {self.request_type}\nDescription: {self.description}\nPriority: {self.priority}\n{status}"

class SupportHandler(ABC):
    """Abstract base class for support handlers."""
    
    def __init__(self):
        self._next_handler: Optional['SupportHandler'] = None
    
    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler  # Return handler for method chaining
    
    @abstractmethod
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle the request. Return True if handled, False otherwise."""
        pass
    
    def _pass_to_next(self, request: SupportRequest) -> bool:
        """Pass the request to the next handler in the chain."""
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return False

class Level1Support(SupportHandler):
    """Level 1 Support - handles basic general inquiries."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle basic general requests and simple technical issues."""
        print(f"Level 1 Support received: {request.request_type} - {request.description}")
        
        # Level 1 can handle basic general requests
        if (request.request_type == "general" and 
            request.priority in ["low", "normal"]):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the issue")
            return True
        
        # Level 1 can handle simple technical issues
        if (request.request_type == "technical" and 
            request.priority == "low" and 
            "password" in request.description.lower()):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the password issue")
            return True
        
        # Can't handle this request, pass to next level
        print("→ Level 1 Support escalating to next level")
        return self._pass_to_next(request)

# What we accomplished in this step:
# - Created Level1Support concrete handler
# - Implemented logic for handling basic requests
# - Added escalation to next handler when needed


# Step 4: Create concrete handler for Level 2 Support
# ===============================================================================

# Explanation:
# Level 2 Support handles more complex technical issues and billing problems.
# They have more expertise and authority than Level 1.

from abc import ABC, abstractmethod
from typing import Optional

class SupportRequest:
    """Represents a customer support request."""
    
    def __init__(self, request_type: str, description: str, priority: str = "normal"):
        self.request_type = request_type  # billing, technical, general
        self.description = description
        self.priority = priority  # low, normal, high, urgent
        self.handled_by = None
    
    def __str__(self):
        """String representation of the request."""
        status = f"Handled by: {self.handled_by}" if self.handled_by else "Status: Unhandled"
        return f"Request Type: {self.request_type}\nDescription: {self.description}\nPriority: {self.priority}\n{status}"

class SupportHandler(ABC):
    """Abstract base class for support handlers."""
    
    def __init__(self):
        self._next_handler: Optional['SupportHandler'] = None
    
    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler  # Return handler for method chaining
    
    @abstractmethod
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle the request. Return True if handled, False otherwise."""
        pass
    
    def _pass_to_next(self, request: SupportRequest) -> bool:
        """Pass the request to the next handler in the chain."""
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return False

class Level1Support(SupportHandler):
    """Level 1 Support - handles basic general inquiries."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle basic general requests and simple technical issues."""
        print(f"Level 1 Support received: {request.request_type} - {request.description}")
        
        # Level 1 can handle basic general requests
        if (request.request_type == "general" and 
            request.priority in ["low", "normal"]):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the issue")
            return True
        
        # Level 1 can handle simple technical issues
        if (request.request_type == "technical" and 
            request.priority == "low" and 
            "password" in request.description.lower()):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the password issue")
            return True
        
        # Can't handle this request, pass to next level
        print("→ Level 1 Support escalating to next level")
        return self._pass_to_next(request)

class Level2Support(SupportHandler):
    """Level 2 Support - handles complex technical and billing issues."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle complex technical issues and billing problems."""
        print(f"Level 2 Support received: {request.request_type} - {request.description}")
        
        # Level 2 can handle most technical issues
        if (request.request_type == "technical" and 
            request.priority in ["low", "normal", "high"]):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support resolved the technical issue")
            return True
        
        # Level 2 can handle billing issues
        if (request.request_type == "billing" and 
            request.priority in ["low", "normal"]):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support resolved the billing issue")
            return True
        
        # Level 2 can handle high priority general requests
        if (request.request_type == "general" and 
            request.priority == "high"):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support handled the high priority request")
            return True
        
        # Can't handle this request, escalate to manager
        print("→ Level 2 Support escalating to manager")
        return self._pass_to_next(request)

# What we accomplished in this step:
# - Created Level2Support concrete handler
# - Implemented logic for handling technical and billing issues
# - Added capability to handle higher priority requests


# Step 5: Create concrete handler for Manager Support
# ===============================================================================

# Explanation:
# Manager Support is the final handler in the chain. They can handle
# urgent issues, complex billing problems, and escalations.

from abc import ABC, abstractmethod
from typing import Optional

class SupportRequest:
    """Represents a customer support request."""
    
    def __init__(self, request_type: str, description: str, priority: str = "normal"):
        self.request_type = request_type  # billing, technical, general
        self.description = description
        self.priority = priority  # low, normal, high, urgent
        self.handled_by = None
    
    def __str__(self):
        """String representation of the request."""
        status = f"Handled by: {self.handled_by}" if self.handled_by else "Status: Unhandled"
        return f"Request Type: {self.request_type}\nDescription: {self.description}\nPriority: {self.priority}\n{status}"

class SupportHandler(ABC):
    """Abstract base class for support handlers."""
    
    def __init__(self):
        self._next_handler: Optional['SupportHandler'] = None
    
    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler  # Return handler for method chaining
    
    @abstractmethod
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle the request. Return True if handled, False otherwise."""
        pass
    
    def _pass_to_next(self, request: SupportRequest) -> bool:
        """Pass the request to the next handler in the chain."""
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return False

class Level1Support(SupportHandler):
    """Level 1 Support - handles basic general inquiries."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle basic general requests and simple technical issues."""
        print(f"Level 1 Support received: {request.request_type} - {request.description}")
        
        # Level 1 can handle basic general requests
        if (request.request_type == "general" and 
            request.priority in ["low", "normal"]):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the issue")
            return True
        
        # Level 1 can handle simple technical issues
        if (request.request_type == "technical" and 
            request.priority == "low" and 
            "password" in request.description.lower()):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the password issue")
            return True
        
        # Can't handle this request, pass to next level
        print("→ Level 1 Support escalating to next level")
        return self._pass_to_next(request)

class Level2Support(SupportHandler):
    """Level 2 Support - handles complex technical and billing issues."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle complex technical issues and billing problems."""
        print(f"Level 2 Support received: {request.request_type} - {request.description}")
        
        # Level 2 can handle most technical issues
        if (request.request_type == "technical" and 
            request.priority in ["low", "normal", "high"]):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support resolved the technical issue")
            return True
        
        # Level 2 can handle billing issues
        if (request.request_type == "billing" and 
            request.priority in ["low", "normal"]):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support resolved the billing issue")
            return True
        
        # Level 2 can handle high priority general requests
        if (request.request_type == "general" and 
            request.priority == "high"):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support handled the high priority request")
            return True
        
        # Can't handle this request, escalate to manager
        print("→ Level 2 Support escalating to manager")
        return self._pass_to_next(request)

class ManagerSupport(SupportHandler):
    """Manager Support - handles urgent issues and final escalations."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle urgent issues and complex problems."""
        print(f"Manager Support received: {request.request_type} - {request.description}")
        
        # Manager can handle urgent requests of any type
        if request.priority == "urgent":
            request.handled_by = "Manager Support"
            print("✓ Manager Support handled the urgent request")
            return True
        
        # Manager can handle complex billing issues
        if (request.request_type == "billing" and 
            request.priority == "high"):
            request.handled_by = "Manager Support"
            print("✓ Manager Support resolved the complex billing issue")
            return True
        
        # Manager can handle urgent technical issues
        if (request.request_type == "technical" and 
            request.priority == "urgent"):
            request.handled_by = "Manager Support"
            print("✓ Manager Support handled the critical technical issue")
            return True
        
        # If even the manager can't handle it, escalate externally
        print("⚠ Manager Support: Request requires external escalation")
        request.handled_by = "External Escalation Required"
        return False

# What we accomplished in this step:
# - Created ManagerSupport concrete handler
# - Implemented logic for handling urgent and complex issues
# - Added final escalation handling for unresolvable requests


# Step 6: Test the complete chain implementation
# ===============================================================================

# Explanation:
# Let's test our Chain of Responsibility pattern with various request types
# and see how they flow through the chain.

from abc import ABC, abstractmethod
from typing import Optional

class SupportRequest:
    """Represents a customer support request."""
    
    def __init__(self, request_type: str, description: str, priority: str = "normal"):
        self.request_type = request_type  # billing, technical, general
        self.description = description
        self.priority = priority  # low, normal, high, urgent
        self.handled_by = None
    
    def __str__(self):
        """String representation of the request."""
        status = f"Handled by: {self.handled_by}" if self.handled_by else "Status: Unhandled"
        return f"Request Type: {self.request_type}\nDescription: {self.description}\nPriority: {self.priority}\n{status}"

class SupportHandler(ABC):
    """Abstract base class for support handlers."""
    
    def __init__(self):
        self._next_handler: Optional['SupportHandler'] = None
    
    def set_next(self, handler: 'SupportHandler') -> 'SupportHandler':
        """Set the next handler in the chain."""
        self._next_handler = handler
        return handler  # Return handler for method chaining
    
    @abstractmethod
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle the request. Return True if handled, False otherwise."""
        pass
    
    def _pass_to_next(self, request: SupportRequest) -> bool:
        """Pass the request to the next handler in the chain."""
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return False

class Level1Support(SupportHandler):
    """Level 1 Support - handles basic general inquiries."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle basic general requests and simple technical issues."""
        print(f"Level 1 Support received: {request.request_type} - {request.description}")
        
        # Level 1 can handle basic general requests
        if (request.request_type == "general" and 
            request.priority in ["low", "normal"]):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the issue")
            return True
        
        # Level 1 can handle simple technical issues
        if (request.request_type == "technical" and 
            request.priority == "low" and 
            "password" in request.description.lower()):
            request.handled_by = "Level 1 Support"
            print("✓ Level 1 Support resolved the password issue")
            return True
        
        # Can't handle this request, pass to next level
        print("→ Level 1 Support escalating to next level")
        return self._pass_to_next(request)

class Level2Support(SupportHandler):
    """Level 2 Support - handles complex technical and billing issues."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle complex technical issues and billing problems."""
        print(f"Level 2 Support received: {request.request_type} - {request.description}")
        
        # Level 2 can handle most technical issues
        if (request.request_type == "technical" and 
            request.priority in ["low", "normal", "high"]):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support resolved the technical issue")
            return True
        
        # Level 2 can handle billing issues
        if (request.request_type == "billing" and 
            request.priority in ["low", "normal"]):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support resolved the billing issue")
            return True
        
        # Level 2 can handle high priority general requests
        if (request.request_type == "general" and 
            request.priority == "high"):
            request.handled_by = "Level 2 Support"
            print("✓ Level 2 Support handled the high priority request")
            return True
        
        # Can't handle this request, escalate to manager
        print("→ Level 2 Support escalating to manager")
        return self._pass_to_next(request)

class ManagerSupport(SupportHandler):
    """Manager Support - handles urgent issues and final escalations."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle urgent issues and complex problems."""
        print(f"Manager Support received: {request.request_type} - {request.description}")
        
        # Manager can handle urgent requests of any type
        if request.priority == "urgent":
            request.handled_by = "Manager Support"
            print("✓ Manager Support handled the urgent request")
            return True
        
        # Manager can handle complex billing issues
        if (request.request_type == "billing" and 
            request.priority == "high"):
            request.handled_by = "Manager Support"
            print("✓ Manager Support resolved the complex billing issue")
            return True
        
        # Manager can handle urgent technical issues
        if (request.request_type == "technical" and 
            request.priority == "urgent"):
            request.handled_by = "Manager Support"
            print("✓ Manager Support handled the critical technical issue")
            return True
        
        # If even the manager can't handle it, escalate externally
        print("⚠ Manager Support: Request requires external escalation")
        request.handled_by = "External Escalation Required"
        return False

# Set up the chain of responsibility
level1 = Level1Support()
level2 = Level2Support()
manager = ManagerSupport()

# Chain the handlers together
level1.set_next(level2).set_next(manager)

print("=== Testing Chain of Responsibility Pattern ===\n")

# Test different types of requests
test_requests = [
    SupportRequest("general", "How do I reset my password?", "low"),
    SupportRequest("technical", "Password reset not working", "low"),
    SupportRequest("technical", "Server is down", "high"),
    SupportRequest("billing", "Wrong charge on my account", "normal"),
    SupportRequest("billing", "Refund request for overcharge", "high"),
    SupportRequest("general", "VIP customer complaint", "urgent"),
    SupportRequest("technical", "Critical system failure", "urgent")
]

for i, request in enumerate(test_requests, 1):
    print(f"{i}. Processing Request:")
    print(f"   {request.request_type.title()} - {request.description} (Priority: {request.priority})")
    print()
    
    level1.handle_request(request)
    print(f"   Final Status: {request.handled_by}")
    print("-" * 60)

# What we accomplished in this step:
# - Set up the complete chain of handlers
# - Tested various request types and priorities
# - Demonstrated how requests flow through the chain
# - Showed different handling outcomes


# Step 7: Demonstrate dynamic chain reconfiguration
# ===============================================================================

# Explanation:
# One of the key benefits of the Chain of Responsibility pattern is the ability
# to dynamically reconfigure the chain at runtime.

print("\n=== Dynamic Chain Reconfiguration ===\n")

# Create a specialized handler for VIP customers
class VIPSupport(SupportHandler):
    """VIP Support - handles all VIP customer requests immediately."""
    
    def handle_request(self, request: SupportRequest) -> bool:
        """Handle VIP customer requests with priority."""
        print(f"VIP Support received: {request.request_type} - {request.description}")
        
        # VIP support handles everything for VIP customers
        if "VIP" in request.description:
            request.handled_by = "VIP Support"
            print("✓ VIP Support provided premium service")
            return True
        
        # Not a VIP request, pass to regular chain
        print("→ VIP Support passing to regular chain")
        return self._pass_to_next(request)

# Reconfigure chain with VIP support at the front
vip_support = VIPSupport()
level1_new = Level1Support()
level2_new = Level2Support()
manager_new = ManagerSupport()

# New chain: VIP -> Level1 -> Level2 -> Manager
vip_support.set_next(level1_new).set_next(level2_new).set_next(manager_new)

print("Testing with VIP Support chain:")
vip_request = SupportRequest("general", "VIP customer needs immediate assistance", "high")
print(f"Request: {vip_request.description}")
print()
vip_support.handle_request(vip_request)
print(f"Final Status: {vip_request.handled_by}")
print()

# Test bypassing certain levels
print("=== Bypassing Levels Example ===\n")
print("Direct Level2 -> Manager chain (bypassing Level1):")
direct_chain = Level2Support()
direct_manager = ManagerSupport()
direct_chain.set_next(direct_manager)

bypass_request = SupportRequest("technical", "Complex server configuration", "high")
print(f"Request: {bypass_request.description}")
print()
direct_chain.handle_request(bypass_request)
print(f"Final Status: {bypass_request.handled_by}")


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Chain of Responsibility pattern structure and purpose
# - Abstract handler interface and concrete implementations
# - Request passing mechanism through the chain
# - Dynamic chain configuration and reconfiguration
# - Flexible request handling with different priorities
# - Separation of request sender and receiver
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a security handler!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================