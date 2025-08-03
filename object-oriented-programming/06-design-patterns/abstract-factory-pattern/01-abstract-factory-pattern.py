"""Question: Implement the Abstract Factory pattern to create families of related objects.

Create a GUI framework that can produce different UI components (buttons, text fields)
for different operating systems (Windows, Mac, Linux) without specifying concrete classes.

Requirements:
1. Create abstract factory for UI components
2. Implement concrete factories for each OS
3. Create abstract and concrete UI components
4. Demonstrate creation of complete UI sets
5. Show how the pattern ensures compatibility within families

Example usage:
    windows_factory = WindowsUIFactory()
    button = windows_factory.create_button()
    textfield = windows_factory.create_textfield()
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
# - What is an Abstract Factory? (creates families of related objects)
# - How do you define abstract classes? (ABC and abstractmethod)
# - What are the product families? (UI components for different OS)
# - How do concrete factories differ? (they create OS-specific components)
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


# Step 1: Understanding the Abstract Factory Pattern
# ===============================================================================

# Explanation:
# The Abstract Factory pattern provides an interface for creating families of related
# or dependent objects without specifying their concrete classes. It's useful when
# you need to create objects that work together and belong to the same family.

from abc import ABC, abstractmethod

print("Step 1: Understanding Abstract Factory Pattern")
print("Abstract Factory creates families of related objects")
print("Example: UI components for different operating systems")

# What we accomplished in this step:
# - Imported ABC for creating abstract classes
# - Understood the purpose of Abstract Factory pattern


# Step 2: Define abstract product interfaces
# ===============================================================================

# Explanation:
# First, we need to define the abstract interfaces for our products.
# In our GUI example, we'll have Button and TextField components.

from abc import ABC, abstractmethod

print("\nStep 2: Defining abstract product interfaces")

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

print("Abstract Button and TextField interfaces defined")

# What we accomplished in this step:
# - Created abstract base classes for our UI components
# - Defined the interface that all concrete products must implement


# Step 3: Create concrete product implementations for Windows
# ===============================================================================

# Explanation:
# Now we'll create concrete implementations of our products for Windows OS.
# Each concrete product implements the abstract interface.

from abc import ABC, abstractmethod

print("\nStep 3: Creating Windows-specific UI components")

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button with rounded corners"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(TextField):
    def render(self):
        return "Rendering Windows-style text field with blue border"
    
    def type_text(self, text):
        return f"Typing '{text}' in Windows text field with spell check"

print("Windows UI components created")

# What we accomplished in this step:
# - Created concrete Windows implementations of Button and TextField
# - Each implementation has Windows-specific behavior and styling


# Step 4: Create concrete product implementations for Mac and Linux
# ===============================================================================

# Explanation:
# Let's add concrete implementations for Mac and Linux to complete our product families.
# Each OS will have its own distinctive look and behavior.

from abc import ABC, abstractmethod

print("\nStep 4: Creating Mac and Linux UI components")

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button with rounded corners"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(TextField):
    def render(self):
        return "Rendering Windows-style text field with blue border"
    
    def type_text(self, text):
        return f"Typing '{text}' in Windows text field with spell check"

class MacButton(Button):
    def render(self):
        return "Rendering Mac-style button with gradient and shadow"
    
    def click(self):
        return "Mac button clicked with elegant animation"

class MacTextField(TextField):
    def render(self):
        return "Rendering Mac-style text field with clean design"
    
    def type_text(self, text):
        return f"Typing '{text}' in Mac text field with auto-complete"

class LinuxButton(Button):
    def render(self):
        return "Rendering Linux-style button with flat design"
    
    def click(self):
        return "Linux button clicked with minimal feedback"

class LinuxTextField(TextField):
    def render(self):
        return "Rendering Linux-style text field with dark theme"
    
    def type_text(self, text):
        return f"Typing '{text}' in Linux text field with vim shortcuts"

print("Mac and Linux UI components created")

# What we accomplished in this step:
# - Created complete product families for all three operating systems
# - Each OS has its own distinctive implementation style


# Step 5: Define the abstract factory interface
# ===============================================================================

# Explanation:
# Now we need to create the abstract factory that defines the interface
# for creating families of related products.

from abc import ABC, abstractmethod

print("\nStep 5: Defining abstract factory interface")

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button with rounded corners"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(TextField):
    def render(self):
        return "Rendering Windows-style text field with blue border"
    
    def type_text(self, text):
        return f"Typing '{text}' in Windows text field with spell check"

class MacButton(Button):
    def render(self):
        return "Rendering Mac-style button with gradient and shadow"
    
    def click(self):
        return "Mac button clicked with elegant animation"

class MacTextField(TextField):
    def render(self):
        return "Rendering Mac-style text field with clean design"
    
    def type_text(self, text):
        return f"Typing '{text}' in Mac text field with auto-complete"

class LinuxButton(Button):
    def render(self):
        return "Rendering Linux-style button with flat design"
    
    def click(self):
        return "Linux button clicked with minimal feedback"

class LinuxTextField(TextField):
    def render(self):
        return "Rendering Linux-style text field with dark theme"
    
    def type_text(self, text):
        return f"Typing '{text}' in Linux text field with vim shortcuts"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_textfield(self):
        pass

print("Abstract UIFactory interface defined")

# What we accomplished in this step:
# - Created the abstract factory interface
# - Defined methods for creating each type of UI component


# Step 6: Implement concrete factories for each operating system
# ===============================================================================

# Explanation:
# Now we'll create concrete factory implementations for each OS.
# Each factory knows how to create the appropriate family of products.

from abc import ABC, abstractmethod

print("\nStep 6: Creating concrete factories for each OS")

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button with rounded corners"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(TextField):
    def render(self):
        return "Rendering Windows-style text field with blue border"
    
    def type_text(self, text):
        return f"Typing '{text}' in Windows text field with spell check"

class MacButton(Button):
    def render(self):
        return "Rendering Mac-style button with gradient and shadow"
    
    def click(self):
        return "Mac button clicked with elegant animation"

class MacTextField(TextField):
    def render(self):
        return "Rendering Mac-style text field with clean design"
    
    def type_text(self, text):
        return f"Typing '{text}' in Mac text field with auto-complete"

class LinuxButton(Button):
    def render(self):
        return "Rendering Linux-style button with flat design"
    
    def click(self):
        return "Linux button clicked with minimal feedback"

class LinuxTextField(TextField):
    def render(self):
        return "Rendering Linux-style text field with dark theme"
    
    def type_text(self, text):
        return f"Typing '{text}' in Linux text field with vim shortcuts"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_textfield(self):
        pass

class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_textfield(self):
        return WindowsTextField()

class MacUIFactory(UIFactory):
    def create_button(self):
        return MacButton()
    
    def create_textfield(self):
        return MacTextField()

class LinuxUIFactory(UIFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_textfield(self):
        return LinuxTextField()

print("Concrete factories for Windows, Mac, and Linux created")

# What we accomplished in this step:
# - Created concrete factory implementations for each OS
# - Each factory creates the appropriate family of UI components


# Step 7: Create a client class that uses the factory
# ===============================================================================

# Explanation:
# Let's create a client class that uses the abstract factory to create UI components.
# The client doesn't need to know which specific factory it's using.

from abc import ABC, abstractmethod

print("\nStep 7: Creating client class that uses the factory")

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button with rounded corners"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(TextField):
    def render(self):
        return "Rendering Windows-style text field with blue border"
    
    def type_text(self, text):
        return f"Typing '{text}' in Windows text field with spell check"

class MacButton(Button):
    def render(self):
        return "Rendering Mac-style button with gradient and shadow"
    
    def click(self):
        return "Mac button clicked with elegant animation"

class MacTextField(TextField):
    def render(self):
        return "Rendering Mac-style text field with clean design"
    
    def type_text(self, text):
        return f"Typing '{text}' in Mac text field with auto-complete"

class LinuxButton(Button):
    def render(self):
        return "Rendering Linux-style button with flat design"
    
    def click(self):
        return "Linux button clicked with minimal feedback"

class LinuxTextField(TextField):
    def render(self):
        return "Rendering Linux-style text field with dark theme"
    
    def type_text(self, text):
        return f"Typing '{text}' in Linux text field with vim shortcuts"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_textfield(self):
        pass

class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_textfield(self):
        return WindowsTextField()

class MacUIFactory(UIFactory):
    def create_button(self):
        return MacButton()
    
    def create_textfield(self):
        return MacTextField()

class LinuxUIFactory(UIFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_textfield(self):
        return LinuxTextField()

class Application:
    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.button = None
        self.textfield = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.textfield = self.factory.create_textfield()
        return "UI components created successfully"
    
    def render_ui(self):
        if not self.button or not self.textfield:
            return "UI not created yet. Call create_ui() first."
        
        button_render = self.button.render()
        textfield_render = self.textfield.render()
        return f"UI Rendered:\n- {button_render}\n- {textfield_render}"
    
    def interact_with_ui(self, text_input="Hello World"):
        if not self.button or not self.textfield:
            return "UI not created yet. Call create_ui() first."
        
        click_result = self.button.click()
        type_result = self.textfield.type_text(text_input)
        return f"UI Interaction:\n- {click_result}\n- {type_result}"

print("Application client class created")

# What we accomplished in this step:
# - Created a client class that works with any UI factory
# - The client is decoupled from specific implementations
# - Added methods to create, render, and interact with UI components


# Step 8: Add factory selection logic
# ===============================================================================

# Explanation:
# Let's add a factory selector that can choose the appropriate factory
# based on the operating system or user preference.

from abc import ABC, abstractmethod
import platform

print("\nStep 8: Adding factory selection logic")

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button with rounded corners"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(TextField):
    def render(self):
        return "Rendering Windows-style text field with blue border"
    
    def type_text(self, text):
        return f"Typing '{text}' in Windows text field with spell check"

class MacButton(Button):
    def render(self):
        return "Rendering Mac-style button with gradient and shadow"
    
    def click(self):
        return "Mac button clicked with elegant animation"

class MacTextField(TextField):
    def render(self):
        return "Rendering Mac-style text field with clean design"
    
    def type_text(self, text):
        return f"Typing '{text}' in Mac text field with auto-complete"

class LinuxButton(Button):
    def render(self):
        return "Rendering Linux-style button with flat design"
    
    def click(self):
        return "Linux button clicked with minimal feedback"

class LinuxTextField(TextField):
    def render(self):
        return "Rendering Linux-style text field with dark theme"
    
    def type_text(self, text):
        return f"Typing '{text}' in Linux text field with vim shortcuts"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_textfield(self):
        pass

class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_textfield(self):
        return WindowsTextField()

class MacUIFactory(UIFactory):
    def create_button(self):
        return MacButton()
    
    def create_textfield(self):
        return MacTextField()

class LinuxUIFactory(UIFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_textfield(self):
        return LinuxTextField()

class Application:
    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.button = None
        self.textfield = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.textfield = self.factory.create_textfield()
        return "UI components created successfully"
    
    def render_ui(self):
        if not self.button or not self.textfield:
            return "UI not created yet. Call create_ui() first."
        
        button_render = self.button.render()
        textfield_render = self.textfield.render()
        return f"UI Rendered:\n- {button_render}\n- {textfield_render}"
    
    def interact_with_ui(self, text_input="Hello World"):
        if not self.button or not self.textfield:
            return "UI not created yet. Call create_ui() first."
        
        click_result = self.button.click()
        type_result = self.textfield.type_text(text_input)
        return f"UI Interaction:\n- {click_result}\n- {type_result}"

class UIFactorySelector:
    @staticmethod
    def get_factory(os_type=None):
        if os_type is None:
            # Auto-detect OS
            system = platform.system().lower()
            if 'windows' in system:
                os_type = 'windows'
            elif 'darwin' in system:  # macOS
                os_type = 'mac'
            else:
                os_type = 'linux'
        
        factories = {
            'windows': WindowsUIFactory(),
            'mac': MacUIFactory(),
            'linux': LinuxUIFactory()
        }
        
        return factories.get(os_type.lower(), LinuxUIFactory())
    
    @staticmethod
    def get_available_factories():
        return ['windows', 'mac', 'linux']

print("Factory selector with auto-detection created")

# What we accomplished in this step:
# - Added automatic OS detection
# - Created a factory selector for easy factory creation
# - Made the system more flexible and user-friendly


# Step 9: Test the complete Abstract Factory implementation
# ===============================================================================

# Explanation:
# Finally, let's test our complete Abstract Factory implementation
# and demonstrate how it ensures compatibility within product families.

from abc import ABC, abstractmethod
import platform

class Button(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def type_text(self, text):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows-style button with rounded corners"
    
    def click(self):
        return "Windows button clicked with system sound"

class WindowsTextField(TextField):
    def render(self):
        return "Rendering Windows-style text field with blue border"
    
    def type_text(self, text):
        return f"Typing '{text}' in Windows text field with spell check"

class MacButton(Button):
    def render(self):
        return "Rendering Mac-style button with gradient and shadow"
    
    def click(self):
        return "Mac button clicked with elegant animation"

class MacTextField(TextField):
    def render(self):
        return "Rendering Mac-style text field with clean design"
    
    def type_text(self, text):
        return f"Typing '{text}' in Mac text field with auto-complete"

class LinuxButton(Button):
    def render(self):
        return "Rendering Linux-style button with flat design"
    
    def click(self):
        return "Linux button clicked with minimal feedback"

class LinuxTextField(TextField):
    def render(self):
        return "Rendering Linux-style text field with dark theme"
    
    def type_text(self, text):
        return f"Typing '{text}' in Linux text field with vim shortcuts"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    
    @abstractmethod
    def create_textfield(self):
        pass

class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_textfield(self):
        return WindowsTextField()

class MacUIFactory(UIFactory):
    def create_button(self):
        return MacButton()
    
    def create_textfield(self):
        return MacTextField()

class LinuxUIFactory(UIFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_textfield(self):
        return LinuxTextField()

class Application:
    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.button = None
        self.textfield = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.textfield = self.factory.create_textfield()
        return "UI components created successfully"
    
    def render_ui(self):
        if not self.button or not self.textfield:
            return "UI not created yet. Call create_ui() first."
        
        button_render = self.button.render()
        textfield_render = self.textfield.render()
        return f"UI Rendered:\n- {button_render}\n- {textfield_render}"
    
    def interact_with_ui(self, text_input="Hello World"):
        if not self.button or not self.textfield:
            return "UI not created yet. Call create_ui() first."
        
        click_result = self.button.click()
        type_result = self.textfield.type_text(text_input)
        return f"UI Interaction:\n- {click_result}\n- {type_result}"

class UIFactorySelector:
    @staticmethod
    def get_factory(os_type=None):
        if os_type is None:
            # Auto-detect OS
            system = platform.system().lower()
            if 'windows' in system:
                os_type = 'windows'
            elif 'darwin' in system:  # macOS
                os_type = 'mac'
            else:
                os_type = 'linux'
        
        factories = {
            'windows': WindowsUIFactory(),
            'mac': MacUIFactory(),
            'linux': LinuxUIFactory()
        }
        
        return factories.get(os_type.lower(), LinuxUIFactory())
    
    @staticmethod
    def get_available_factories():
        return ['windows', 'mac', 'linux']

# Test our complete Abstract Factory implementation:
print("\nTesting Abstract Factory implementation:")

print("\n1. Testing with different OS factories:")
for os_name in ['windows', 'mac', 'linux']:
    print(f"\n--- Testing {os_name.upper()} UI ---")
    factory = UIFactorySelector.get_factory(os_name)
    app = Application(factory)
    
    print(app.create_ui())
    print(app.render_ui())
    print(app.interact_with_ui(f"Hello from {os_name}!"))

print("\n2. Testing auto-detection:")
auto_factory = UIFactorySelector.get_factory()
auto_app = Application(auto_factory)
auto_app.create_ui()
print("Auto-detected factory created and tested successfully")

print("\n3. Testing family compatibility:")
print("All components from the same factory work together seamlessly")
print("Each factory ensures consistent look and feel across all components")

print("\n4. Available factory types:")
print(f"Supported OS types: {UIFactorySelector.get_available_factories()}")

# Demonstrate the key benefits:
print("\nKey Benefits Demonstrated:")
print("✓ Family consistency: All components from same factory match")
print("✓ Easy switching: Change factory to change entire UI family")
print("✓ Extensibility: Easy to add new OS support")
print("✓ Decoupling: Client code doesn't depend on concrete classes")

# What we accomplished in this step:
# - Tested the complete Abstract Factory implementation
# - Demonstrated family consistency and compatibility
# - Showed how easy it is to switch between different product families
# - Verified that the pattern works as intended


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step Abstract Factory pattern solution!
#
# Key concepts learned:
# - Abstract Factory pattern for creating families of related objects
# - Abstract base classes and interfaces
# - Concrete product implementations for different families
# - Factory selection and auto-detection
# - Client-factory decoupling
# - Family consistency and compatibility
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding new UI components or OS support!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================

