"""Question: Implement the Abstract Factory pattern to create families of related objects.

Create an abstract factory for creating different types of UI components (buttons, text fields)
for different operating systems (Windows, Mac, Linux).

Requirements:
1. Create abstract base classes for UI components
2. Create concrete implementations for each OS
3. Create abstract factory and concrete factories
4. Demonstrate the pattern usage

Example usage:
    factory = WindowsUIFactory()
    button = factory.create_button()
    text_field = factory.create_text_field()
    button.render()
    text_field.render()
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
# - What abstract classes do you need for UI components?
# - How do you create an abstract factory interface?
# - What concrete implementations are needed for each OS?
# - How does the client code use the factory?
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


# Step 1: Import necessary modules and create abstract UI components
# ===============================================================================

# Explanation:
# The Abstract Factory pattern starts with abstract product interfaces.
# We need abstract classes for each type of UI component we want to create.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

# What we accomplished in this step:
# - Created abstract interfaces for UI components
# - Defined the contract that all concrete implementations must follow


# Step 2: Create concrete Windows UI components
# ===============================================================================

# Explanation:
# Now we implement concrete versions of our abstract components for Windows.
# Each concrete class provides specific implementations for the abstract methods.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

class WindowsButton(AbstractButton):
    """Windows-style button implementation."""
    
    def render(self):
        return "Rendering Windows button with native styling"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(AbstractTextField):
    """Windows-style text field implementation."""
    
    def render(self):
        return "Rendering Windows text field with border styling"
    
    def get_text(self):
        return "Getting text from Windows text field"

# What we accomplished in this step:
# - Implemented Windows-specific UI components
# - Each component has its own Windows-style behavior


# Step 3: Create concrete Mac UI components
# ===============================================================================

# Explanation:
# Similar to Windows components, but with Mac-specific styling and behavior.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

class WindowsButton(AbstractButton):
    """Windows-style button implementation."""
    
    def render(self):
        return "Rendering Windows button with native styling"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(AbstractTextField):
    """Windows-style text field implementation."""
    
    def render(self):
        return "Rendering Windows text field with border styling"
    
    def get_text(self):
        return "Getting text from Windows text field"

class MacButton(AbstractButton):
    """Mac-style button implementation."""
    
    def render(self):
        return "Rendering Mac button with rounded corners"
    
    def click(self):
        return "Mac button clicked with subtle animation"

class MacTextField(AbstractTextField):
    """Mac-style text field implementation."""
    
    def render(self):
        return "Rendering Mac text field with clean design"
    
    def get_text(self):
        return "Getting text from Mac text field"

# What we accomplished in this step:
# - Implemented Mac-specific UI components
# - Demonstrated how different platforms can have different implementations


# Step 4: Create concrete Linux UI components
# ===============================================================================

# Explanation:
# Linux components complete our family of UI implementations.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

class WindowsButton(AbstractButton):
    """Windows-style button implementation."""
    
    def render(self):
        return "Rendering Windows button with native styling"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(AbstractTextField):
    """Windows-style text field implementation."""
    
    def render(self):
        return "Rendering Windows text field with border styling"
    
    def get_text(self):
        return "Getting text from Windows text field"

class MacButton(AbstractButton):
    """Mac-style button implementation."""
    
    def render(self):
        return "Rendering Mac button with rounded corners"
    
    def click(self):
        return "Mac button clicked with subtle animation"

class MacTextField(AbstractTextField):
    """Mac-style text field implementation."""
    
    def render(self):
        return "Rendering Mac text field with clean design"
    
    def get_text(self):
        return "Getting text from Mac text field"

class LinuxButton(AbstractButton):
    """Linux-style button implementation."""
    
    def render(self):
        return "Rendering Linux button with GTK styling"
    
    def click(self):
        return "Linux button clicked"

class LinuxTextField(AbstractTextField):
    """Linux-style text field implementation."""
    
    def render(self):
        return "Rendering Linux text field with theme styling"
    
    def get_text(self):
        return "Getting text from Linux text field"

# What we accomplished in this step:
# - Completed our family of platform-specific UI components
# - Now we have three complete sets of related objects


# Step 5: Create the abstract factory interface
# ===============================================================================

# Explanation:
# The abstract factory defines the interface for creating families of related objects.
# It declares methods for creating each type of product.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

class WindowsButton(AbstractButton):
    """Windows-style button implementation."""
    
    def render(self):
        return "Rendering Windows button with native styling"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(AbstractTextField):
    """Windows-style text field implementation."""
    
    def render(self):
        return "Rendering Windows text field with border styling"
    
    def get_text(self):
        return "Getting text from Windows text field"

class MacButton(AbstractButton):
    """Mac-style button implementation."""
    
    def render(self):
        return "Rendering Mac button with rounded corners"
    
    def click(self):
        return "Mac button clicked with subtle animation"

class MacTextField(AbstractTextField):
    """Mac-style text field implementation."""
    
    def render(self):
        return "Rendering Mac text field with clean design"
    
    def get_text(self):
        return "Getting text from Mac text field"

class LinuxButton(AbstractButton):
    """Linux-style button implementation."""
    
    def render(self):
        return "Rendering Linux button with GTK styling"
    
    def click(self):
        return "Linux button clicked"

class LinuxTextField(AbstractTextField):
    """Linux-style text field implementation."""
    
    def render(self):
        return "Rendering Linux text field with theme styling"
    
    def get_text(self):
        return "Getting text from Linux text field"

class AbstractUIFactory(ABC):
    """Abstract factory for creating UI components."""
    
    @abstractmethod
    def create_button(self) -> AbstractButton:
        """Create a button component."""
        pass
    
    @abstractmethod
    def create_text_field(self) -> AbstractTextField:
        """Create a text field component."""
        pass

# What we accomplished in this step:
# - Created the abstract factory interface
# - Defined methods for creating each type of UI component


# Step 6: Create concrete factories for each platform
# ===============================================================================

# Explanation:
# Each concrete factory implements the abstract factory interface and creates
# components for a specific platform.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

class WindowsButton(AbstractButton):
    """Windows-style button implementation."""
    
    def render(self):
        return "Rendering Windows button with native styling"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(AbstractTextField):
    """Windows-style text field implementation."""
    
    def render(self):
        return "Rendering Windows text field with border styling"
    
    def get_text(self):
        return "Getting text from Windows text field"

class MacButton(AbstractButton):
    """Mac-style button implementation."""
    
    def render(self):
        return "Rendering Mac button with rounded corners"
    
    def click(self):
        return "Mac button clicked with subtle animation"

class MacTextField(AbstractTextField):
    """Mac-style text field implementation."""
    
    def render(self):
        return "Rendering Mac text field with clean design"
    
    def get_text(self):
        return "Getting text from Mac text field"

class LinuxButton(AbstractButton):
    """Linux-style button implementation."""
    
    def render(self):
        return "Rendering Linux button with GTK styling"
    
    def click(self):
        return "Linux button clicked"

class LinuxTextField(AbstractTextField):
    """Linux-style text field implementation."""
    
    def render(self):
        return "Rendering Linux text field with theme styling"
    
    def get_text(self):
        return "Getting text from Linux text field"

class AbstractUIFactory(ABC):
    """Abstract factory for creating UI components."""
    
    @abstractmethod
    def create_button(self) -> AbstractButton:
        """Create a button component."""
        pass
    
    @abstractmethod
    def create_text_field(self) -> AbstractTextField:
        """Create a text field component."""
        pass

class WindowsUIFactory(AbstractUIFactory):
    """Factory for creating Windows UI components."""
    
    def create_button(self) -> AbstractButton:
        return WindowsButton()
    
    def create_text_field(self) -> AbstractTextField:
        return WindowsTextField()

class MacUIFactory(AbstractUIFactory):
    """Factory for creating Mac UI components."""
    
    def create_button(self) -> AbstractButton:
        return MacButton()
    
    def create_text_field(self) -> AbstractTextField:
        return MacTextField()

class LinuxUIFactory(AbstractUIFactory):
    """Factory for creating Linux UI components."""
    
    def create_button(self) -> AbstractButton:
        return LinuxButton()
    
    def create_text_field(self) -> AbstractTextField:
        return LinuxTextField()

# What we accomplished in this step:
# - Created concrete factories for each platform
# - Each factory creates components specific to its platform


# Step 7: Create client code that uses the factory
# ===============================================================================

# Explanation:
# The client code works with the abstract factory interface, not concrete classes.
# This allows it to work with any platform without knowing the specifics.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

class WindowsButton(AbstractButton):
    """Windows-style button implementation."""
    
    def render(self):
        return "Rendering Windows button with native styling"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(AbstractTextField):
    """Windows-style text field implementation."""
    
    def render(self):
        return "Rendering Windows text field with border styling"
    
    def get_text(self):
        return "Getting text from Windows text field"

class MacButton(AbstractButton):
    """Mac-style button implementation."""
    
    def render(self):
        return "Rendering Mac button with rounded corners"
    
    def click(self):
        return "Mac button clicked with subtle animation"

class MacTextField(AbstractTextField):
    """Mac-style text field implementation."""
    
    def render(self):
        return "Rendering Mac text field with clean design"
    
    def get_text(self):
        return "Getting text from Mac text field"

class LinuxButton(AbstractButton):
    """Linux-style button implementation."""
    
    def render(self):
        return "Rendering Linux button with GTK styling"
    
    def click(self):
        return "Linux button clicked"

class LinuxTextField(AbstractTextField):
    """Linux-style text field implementation."""
    
    def render(self):
        return "Rendering Linux text field with theme styling"
    
    def get_text(self):
        return "Getting text from Linux text field"

class AbstractUIFactory(ABC):
    """Abstract factory for creating UI components."""
    
    @abstractmethod
    def create_button(self) -> AbstractButton:
        """Create a button component."""
        pass
    
    @abstractmethod
    def create_text_field(self) -> AbstractTextField:
        """Create a text field component."""
        pass

class WindowsUIFactory(AbstractUIFactory):
    """Factory for creating Windows UI components."""
    
    def create_button(self) -> AbstractButton:
        return WindowsButton()
    
    def create_text_field(self) -> AbstractTextField:
        return WindowsTextField()

class MacUIFactory(AbstractUIFactory):
    """Factory for creating Mac UI components."""
    
    def create_button(self) -> AbstractButton:
        return MacButton()
    
    def create_text_field(self) -> AbstractTextField:
        return MacTextField()

class LinuxUIFactory(AbstractUIFactory):
    """Factory for creating Linux UI components."""
    
    def create_button(self) -> AbstractButton:
        return LinuxButton()
    
    def create_text_field(self) -> AbstractTextField:
        return LinuxTextField()

class Application:
    """Application that uses the abstract factory."""
    
    def __init__(self, factory: AbstractUIFactory):
        self.factory = factory
        self.button = None
        self.text_field = None
    
    def create_ui(self):
        """Create UI components using the factory."""
        self.button = self.factory.create_button()
        self.text_field = self.factory.create_text_field()
    
    def render_ui(self):
        """Render all UI components."""
        if self.button and self.text_field:
            return f"{self.button.render()}\n{self.text_field.render()}"
        return "UI not created yet"

# What we accomplished in this step:
# - Created client code that works with any factory
# - Demonstrated how the pattern isolates client from concrete classes


# Step 8: Test the complete implementation
# ===============================================================================

# Explanation:
# Let's test our Abstract Factory implementation with different platforms.

from abc import ABC, abstractmethod

class AbstractButton(ABC):
    """Abstract base class for buttons."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass
    
    @abstractmethod
    def click(self):
        """Handle button click."""
        pass

class AbstractTextField(ABC):
    """Abstract base class for text fields."""
    
    @abstractmethod
    def render(self):
        """Render the text field."""
        pass
    
    @abstractmethod
    def get_text(self):
        """Get text from the field."""
        pass

class WindowsButton(AbstractButton):
    """Windows-style button implementation."""
    
    def render(self):
        return "Rendering Windows button with native styling"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(AbstractTextField):
    """Windows-style text field implementation."""
    
    def render(self):
        return "Rendering Windows text field with border styling"
    
    def get_text(self):
        return "Getting text from Windows text field"

class MacButton(AbstractButton):
    """Mac-style button implementation."""
    
    def render(self):
        return "Rendering Mac button with rounded corners"
    
    def click(self):
        return "Mac button clicked with subtle animation"

class MacTextField(AbstractTextField):
    """Mac-style text field implementation."""
    
    def render(self):
        return "Rendering Mac text field with clean design"
    
    def get_text(self):
        return "Getting text from Mac text field"

class LinuxButton(AbstractButton):
    """Linux-style button implementation."""
    
    def render(self):
        return "Rendering Linux button with GTK styling"
    
    def click(self):
        return "Linux button clicked"

class LinuxTextField(AbstractTextField):
    """Linux-style text field implementation."""
    
    def render(self):
        return "Rendering Linux text field with theme styling"
    
    def get_text(self):
        return "Getting text from Linux text field"

class AbstractUIFactory(ABC):
    """Abstract factory for creating UI components."""
    
    @abstractmethod
    def create_button(self) -> AbstractButton:
        """Create a button component."""
        pass
    
    @abstractmethod
    def create_text_field(self) -> AbstractTextField:
        """Create a text field component."""
        pass

class WindowsUIFactory(AbstractUIFactory):
    """Factory for creating Windows UI components."""
    
    def create_button(self) -> AbstractButton:
        return WindowsButton()
    
    def create_text_field(self) -> AbstractTextField:
        return WindowsTextField()

class MacUIFactory(AbstractUIFactory):
    """Factory for creating Mac UI components."""
    
    def create_button(self) -> AbstractButton:
        return MacButton()
    
    def create_text_field(self) -> AbstractTextField:
        return MacTextField()

class LinuxUIFactory(AbstractUIFactory):
    """Factory for creating Linux UI components."""
    
    def create_button(self) -> AbstractButton:
        return LinuxButton()
    
    def create_text_field(self) -> AbstractTextField:
        return LinuxTextField()

class Application:
    """Application that uses the abstract factory."""
    
    def __init__(self, factory: AbstractUIFactory):
        self.factory = factory
        self.button = None
        self.text_field = None
    
    def create_ui(self):
        """Create UI components using the factory."""
        self.button = self.factory.create_button()
        self.text_field = self.factory.create_text_field()
    
    def render_ui(self):
        """Render all UI components."""
        if self.button and self.text_field:
            return f"{self.button.render()}\n{self.text_field.render()}"
        return "UI not created yet"

# Test different OS factories
operating_systems = ['windows', 'mac', 'linux']
factories = {
    'windows': WindowsUIFactory(),
    'mac': MacUIFactory(),
    'linux': LinuxUIFactory()
}

print("=== Testing Abstract Factory Pattern ===\n")

for os_name in operating_systems:
    print(f"--- Testing {os_name.upper()} UI Factory ---")
    
    # Get factory for OS
    factory = factories[os_name]
    
    # Create application with factory
    app = Application(factory)
    app.create_ui()
    
    # Render UI
    print(app.render_ui())
    
    # Test component interactions
    print(app.button.click())
    print(app.text_field.get_text())
    print()

# What we accomplished in this step:
# - Tested the complete Abstract Factory implementation
# - Demonstrated how different factories create different component families
# - Showed polymorphism in action


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Abstract Factory pattern structure and purpose
# - Creating families of related objects
# - Abstract product interfaces and concrete implementations
# - Abstract factory interface and concrete factories
# - Client code that works with any factory
# - Platform-specific object creation
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding mobile platforms!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================