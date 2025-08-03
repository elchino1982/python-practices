"""Question: Create comprehensive README files for Python projects.

Learn how to write effective README files that serve as the entry point
for your project documentation.

Requirements:
1. Create a basic README structure
2. Add project description and features
3. Include installation instructions
4. Add usage examples and API documentation
5. Include contribution guidelines and licensing

Example usage:
    readme = ReadmeBuilder()
    readme.add_title("My Python Project")
    readme.add_description("A comprehensive Python library")
    content = readme.build()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!
#
# Tips for success:
# - Read the question carefully
# - Think about what sections a good README needs
# - Start with a simple structure
# - Build up complexity step by step
# - Don't worry if it's not perfect - learning is a process!
#
# Remember: The best way to learn documentation is by writing, not by reading examples!
#
# Take your time, experiment, and enjoy the learning process!

# Try to implement your solution here:
# (Write your code below this line)


























# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What are the essential sections of a README?
# - How can you structure content in a readable way?
# - What information do users need first?
# - How can you make installation and usage clear?
#
# Remember: Start with basic structure and add details gradually!


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


# Step 1: Create basic README structure and builder class
# ===============================================================================

# Explanation:
# A good README starts with a clear structure. We'll create a builder class
# that helps construct README content systematically.

from typing import List, Optional
from datetime import datetime

class ReadmeBuilder:
    """Builder class for creating comprehensive README files."""
    
    def __init__(self):
        self.sections: List[str] = []
        self.title: str = ""
        self.description: str = ""
    
    def add_title(self, title: str) -> 'ReadmeBuilder':
        """Add project title."""
        self.title = title
        return self
    
    def add_description(self, description: str) -> 'ReadmeBuilder':
        """Add project description."""
        self.description = description
        return self
    
    def build(self) -> str:
        """Build the complete README content."""
        content = []
        
        if self.title:
            content.append(f"# {self.title}")
            content.append("")
        
        if self.description:
            content.append(self.description)
            content.append("")
        
        content.extend(self.sections)
        return "\n".join(content)

# Test Step 1
print("=== Step 1: Basic README Structure ===")
readme = ReadmeBuilder()
readme.add_title("My Python Project").add_description("A simple Python library for demonstration.")
print(readme.build())
print()


# Step 2: Add badges and features section (includes all code from Step 1)
# ===============================================================================

# Explanation:
# Badges provide quick visual information about project status, version, etc.
# Features section highlights what the project can do.

from typing import List, Optional, Dict
from datetime import datetime

class ReadmeBuilder:
    """Builder class for creating comprehensive README files."""
    
    def __init__(self):
        self.sections: List[str] = []
        self.title: str = ""
        self.description: str = ""
        self.badges: List[str] = []
        self.features: List[str] = []
    
    def add_title(self, title: str) -> 'ReadmeBuilder':
        """Add project title."""
        self.title = title
        return self
    
    def add_description(self, description: str) -> 'ReadmeBuilder':
        """Add project description."""
        self.description = description
        return self
    
    def add_badge(self, name: str, url: str, shield_url: str) -> 'ReadmeBuilder':
        """Add a badge to the README."""
        badge = f"[![{name}]({shield_url})]({url})"
        self.badges.append(badge)
        return self
    
    def add_feature(self, feature: str) -> 'ReadmeBuilder':
        """Add a feature to the features list."""
        self.features.append(f"- {feature}")
        return self
    
    def build(self) -> str:
        """Build the complete README content."""
        content = []
        
        if self.title:
            content.append(f"# {self.title}")
            content.append("")
        
        if self.badges:
            content.extend(self.badges)
            content.append("")
        
        if self.description:
            content.append(self.description)
            content.append("")
        
        if self.features:
            content.append("## Features")
            content.append("")
            content.extend(self.features)
            content.append("")
        
        content.extend(self.sections)
        return "\n".join(content)

# Test Step 2
print("=== Step 2: Badges and Features ===")
readme = ReadmeBuilder()
readme.add_title("My Python Project") \
      .add_description("A comprehensive Python library for demonstration.") \
      .add_badge("Version", "https://pypi.org/project/myproject/", "https://img.shields.io/pypi/v/myproject") \
      .add_badge("License", "https://github.com/user/myproject/blob/main/LICENSE", "https://img.shields.io/github/license/user/myproject") \
      .add_feature("Easy to use API") \
      .add_feature("Comprehensive documentation") \
      .add_feature("Cross-platform compatibility")
print(readme.build())
print()


# Step 3: Add installation instructions (includes all code from Steps 1-2)
# ===============================================================================

# Explanation:
# Installation section is crucial - users need to know how to get started.
# We'll support multiple installation methods and requirements.

from typing import List, Optional, Dict
from datetime import datetime

class ReadmeBuilder:
    """Builder class for creating comprehensive README files."""
    
    def __init__(self):
        self.sections: List[str] = []
        self.title: str = ""
        self.description: str = ""
        self.badges: List[str] = []
        self.features: List[str] = []
        self.installation_methods: Dict[str, List[str]] = {}
        self.requirements: List[str] = []
    
    def add_title(self, title: str) -> 'ReadmeBuilder':
        """Add project title."""
        self.title = title
        return self
    
    def add_description(self, description: str) -> 'ReadmeBuilder':
        """Add project description."""
        self.description = description
        return self
    
    def add_badge(self, name: str, url: str, shield_url: str) -> 'ReadmeBuilder':
        """Add a badge to the README."""
        badge = f"[![{name}]({shield_url})]({url})"
        self.badges.append(badge)
        return self
    
    def add_feature(self, feature: str) -> 'ReadmeBuilder':
        """Add a feature to the features list."""
        self.features.append(f"- {feature}")
        return self
    
    def add_installation_method(self, method: str, commands: List[str]) -> 'ReadmeBuilder':
        """Add an installation method with commands."""
        self.installation_methods[method] = commands
        return self
    
    def add_requirement(self, requirement: str) -> 'ReadmeBuilder':
        """Add a system requirement."""
        self.requirements.append(f"- {requirement}")
        return self
    
    def build(self) -> str:
        """Build the complete README content."""
        content = []
        
        if self.title:
            content.append(f"# {self.title}")
            content.append("")
        
        if self.badges:
            content.extend(self.badges)
            content.append("")
        
        if self.description:
            content.append(self.description)
            content.append("")
        
        if self.features:
            content.append("## Features")
            content.append("")
            content.extend(self.features)
            content.append("")
        
        if self.requirements or self.installation_methods:
            content.append("## Installation")
            content.append("")
            
            if self.requirements:
                content.append("### Requirements")
                content.append("")
                content.extend(self.requirements)
                content.append("")
            
            for method, commands in self.installation_methods.items():
                content.append(f"### {method}")
                content.append("")
                content.append("```bash")
                content.extend(commands)
                content.append("```")
                content.append("")
        
        content.extend(self.sections)
        return "\n".join(content)

# Test Step 3
print("=== Step 3: Installation Instructions ===")
readme = ReadmeBuilder()
readme.add_title("My Python Project") \
      .add_description("A comprehensive Python library for demonstration.") \
      .add_badge("Version", "https://pypi.org/project/myproject/", "https://img.shields.io/pypi/v/myproject") \
      .add_badge("License", "https://github.com/user/myproject/blob/main/LICENSE", "https://img.shields.io/github/license/user/myproject") \
      .add_feature("Easy to use API") \
      .add_feature("Comprehensive documentation") \
      .add_feature("Cross-platform compatibility") \
      .add_requirement("Python 3.8 or higher") \
      .add_requirement("pip package manager") \
      .add_installation_method("Using pip", ["pip install myproject"]) \
      .add_installation_method("From source", [
          "git clone https://github.com/user/myproject.git",
          "cd myproject",
          "pip install -e ."
      ])
print(readme.build())
print()


# Step 4: Add usage examples and API documentation (includes all code from Steps 1-3)
# ===============================================================================

# Explanation:
# Usage examples show users how to actually use the project.
# API documentation provides quick reference for key functions.

from typing import List, Optional, Dict
from datetime import datetime

class ReadmeBuilder:
    """Builder class for creating comprehensive README files."""
    
    def __init__(self):
        self.sections: List[str] = []
        self.title: str = ""
        self.description: str = ""
        self.badges: List[str] = []
        self.features: List[str] = []
        self.installation_methods: Dict[str, List[str]] = {}
        self.requirements: List[str] = []
        self.usage_examples: List[Dict[str, str]] = []
        self.api_methods: List[Dict[str, str]] = []
    
    def add_title(self, title: str) -> 'ReadmeBuilder':
        """Add project title."""
        self.title = title
        return self
    
    def add_description(self, description: str) -> 'ReadmeBuilder':
        """Add project description."""
        self.description = description
        return self
    
    def add_badge(self, name: str, url: str, shield_url: str) -> 'ReadmeBuilder':
        """Add a badge to the README."""
        badge = f"[![{name}]({shield_url})]({url})"
        self.badges.append(badge)
        return self
    
    def add_feature(self, feature: str) -> 'ReadmeBuilder':
        """Add a feature to the features list."""
        self.features.append(f"- {feature}")
        return self
    
    def add_installation_method(self, method: str, commands: List[str]) -> 'ReadmeBuilder':
        """Add an installation method with commands."""
        self.installation_methods[method] = commands
        return self
    
    def add_requirement(self, requirement: str) -> 'ReadmeBuilder':
        """Add a system requirement."""
        self.requirements.append(f"- {requirement}")
        return self
    
    def add_usage_example(self, title: str, description: str, code: str) -> 'ReadmeBuilder':
        """Add a usage example with code."""
        self.usage_examples.append({
            'title': title,
            'description': description,
            'code': code
        })
        return self
    
    def add_api_method(self, method: str, description: str, example: str) -> 'ReadmeBuilder':
        """Add an API method documentation."""
        self.api_methods.append({
            'method': method,
            'description': description,
            'example': example
        })
        return self
    
    def build(self) -> str:
        """Build the complete README content."""
        content = []
        
        if self.title:
            content.append(f"# {self.title}")
            content.append("")
        
        if self.badges:
            content.extend(self.badges)
            content.append("")
        
        if self.description:
            content.append(self.description)
            content.append("")
        
        if self.features:
            content.append("## Features")
            content.append("")
            content.extend(self.features)
            content.append("")
        
        if self.requirements or self.installation_methods:
            content.append("## Installation")
            content.append("")
            
            if self.requirements:
                content.append("### Requirements")
                content.append("")
                content.extend(self.requirements)
                content.append("")
            
            for method, commands in self.installation_methods.items():
                content.append(f"### {method}")
                content.append("")
                content.append("```bash")
                content.extend(commands)
                content.append("```")
                content.append("")
        
        if self.usage_examples:
            content.append("## Usage")
            content.append("")
            
            for example in self.usage_examples:
                content.append(f"### {example['title']}")
                content.append("")
                content.append(example['description'])
                content.append("")
                content.append("```python")
                content.append(example['code'])
                content.append("```")
                content.append("")
        
        if self.api_methods:
            content.append("## API Reference")
            content.append("")
            
            for method in self.api_methods:
                content.append(f"### `{method['method']}`")
                content.append("")
                content.append(method['description'])
                content.append("")
                content.append("```python")
                content.append(method['example'])
                content.append("```")
                content.append("")
        
        content.extend(self.sections)
        return "\n".join(content)

# Test Step 4
print("=== Step 4: Usage Examples and API Documentation ===")
readme = ReadmeBuilder()
readme.add_title("My Python Project") \
      .add_description("A comprehensive Python library for demonstration.") \
      .add_badge("Version", "https://pypi.org/project/myproject/", "https://img.shields.io/pypi/v/myproject") \
      .add_badge("License", "https://github.com/user/myproject/blob/main/LICENSE", "https://img.shields.io/github/license/user/myproject") \
      .add_feature("Easy to use API") \
      .add_feature("Comprehensive documentation") \
      .add_feature("Cross-platform compatibility") \
      .add_requirement("Python 3.8 or higher") \
      .add_requirement("pip package manager") \
      .add_installation_method("Using pip", ["pip install myproject"]) \
      .add_installation_method("From source", [
          "git clone https://github.com/user/myproject.git",
          "cd myproject",
          "pip install -e ."
      ]) \
      .add_usage_example(
          "Basic Usage",
          "Here's how to get started with the basic functionality:",
          "from myproject import MyClass\n\n# Create an instance\nobj = MyClass()\nresult = obj.process_data('hello world')\nprint(result)"
      ) \
      .add_usage_example(
          "Advanced Usage",
          "For more complex scenarios:",
          "from myproject import AdvancedProcessor\n\nprocessor = AdvancedProcessor(config={'verbose': True})\nwith processor.batch_mode():\n    results = processor.process_multiple(['data1', 'data2'])"
      ) \
      .add_api_method(
          "MyClass.process_data(data: str) -> str",
          "Processes input data and returns the result.",
          "obj = MyClass()\nresult = obj.process_data('input')"
      ) \
      .add_api_method(
          "AdvancedProcessor.batch_mode()",
          "Context manager for batch processing operations.",
          "with processor.batch_mode():\n    # batch operations here\n    pass"
      )
print(readme.build())
print()


# Step 5: Add contribution guidelines and licensing (includes all code from Steps 1-4)
# ===============================================================================

# Explanation:
# Contribution guidelines help others contribute to your project.
# Licensing and contact information provide legal clarity and ways to reach you.

from typing import List, Optional, Dict
from datetime import datetime

class ReadmeBuilder:
    """Builder class for creating comprehensive README files."""
    
    def __init__(self):
        self.sections: List[str] = []
        self.title: str = ""
        self.description: str = ""
        self.badges: List[str] = []
        self.features: List[str] = []
        self.installation_methods: Dict[str, List[str]] = {}
        self.requirements: List[str] = []
        self.usage_examples: List[Dict[str, str]] = []
        self.api_methods: List[Dict[str, str]] = []
        self.contribution_steps: List[str] = []
        self.license_info: Dict[str, str] = {}
        self.contact_info: Dict[str, str] = {}
        self.acknowledgments: List[str] = []
    
    def add_title(self, title: str) -> 'ReadmeBuilder':
        """Add project title."""
        self.title = title
        return self
    
    def add_description(self, description: str) -> 'ReadmeBuilder':
        """Add project description."""
        self.description = description
        return self
    
    def add_badge(self, name: str, url: str, shield_url: str) -> 'ReadmeBuilder':
        """Add a badge to the README."""
        badge = f"[![{name}]({shield_url})]({url})"
        self.badges.append(badge)
        return self
    
    def add_feature(self, feature: str) -> 'ReadmeBuilder':
        """Add a feature to the features list."""
        self.features.append(f"- {feature}")
        return self
    
    def add_installation_method(self, method: str, commands: List[str]) -> 'ReadmeBuilder':
        """Add an installation method with commands."""
        self.installation_methods[method] = commands
        return self
    
    def add_requirement(self, requirement: str) -> 'ReadmeBuilder':
        """Add a system requirement."""
        self.requirements.append(f"- {requirement}")
        return self
    
    def add_usage_example(self, title: str, description: str, code: str) -> 'ReadmeBuilder':
        """Add a usage example with code."""
        self.usage_examples.append({
            'title': title,
            'description': description,
            'code': code
        })
        return self
    
    def add_api_method(self, method: str, description: str, example: str) -> 'ReadmeBuilder':
        """Add an API method documentation."""
        self.api_methods.append({
            'method': method,
            'description': description,
            'example': example
        })
        return self
    
    def add_contribution_step(self, step: str) -> 'ReadmeBuilder':
        """Add a contribution step."""
        self.contribution_steps.append(f"1. {step}")
        return self
    
    def set_license(self, license_name: str, license_url: str = "") -> 'ReadmeBuilder':
        """Set license information."""
        self.license_info = {
            'name': license_name,
            'url': license_url
        }
        return self
    
    def add_contact(self, method: str, value: str) -> 'ReadmeBuilder':
        """Add contact information."""
        self.contact_info[method] = value
        return self
    
    def add_acknowledgment(self, acknowledgment: str) -> 'ReadmeBuilder':
        """Add an acknowledgment."""
        self.acknowledgments.append(f"- {acknowledgment}")
        return self
    
    def build(self) -> str:
        """Build the complete README content."""
        content = []
        
        if self.title:
            content.append(f"# {self.title}")
            content.append("")
        
        if self.badges:
            content.extend(self.badges)
            content.append("")
        
        if self.description:
            content.append(self.description)
            content.append("")
        
        if self.features:
            content.append("## Features")
            content.append("")
            content.extend(self.features)
            content.append("")
        
        if self.requirements or self.installation_methods:
            content.append("## Installation")
            content.append("")
            
            if self.requirements:
                content.append("### Requirements")
                content.append("")
                content.extend(self.requirements)
                content.append("")
            
            for method, commands in self.installation_methods.items():
                content.append(f"### {method}")
                content.append("")
                content.append("```bash")
                content.extend(commands)
                content.append("```")
                content.append("")
        
        if self.usage_examples:
            content.append("## Usage")
            content.append("")
            
            for example in self.usage_examples:
                content.append(f"### {example['title']}")
                content.append("")
                content.append(example['description'])
                content.append("")
                content.append("```python")
                content.append(example['code'])
                content.append("```")
                content.append("")
        
        if self.api_methods:
            content.append("## API Reference")
            content.append("")
            
            for method in self.api_methods:
                content.append(f"### `{method['method']}`")
                content.append("")
                content.append(method['description'])
                content.append("")
                content.append("```python")
                content.append(method['example'])
                content.append("```")
                content.append("")
        
        if self.contribution_steps:
            content.append("## Contributing")
            content.append("")
            content.append("We welcome contributions! Please follow these steps:")
            content.append("")
            content.extend(self.contribution_steps)
            content.append("")
        
        if self.license_info:
            content.append("## License")
            content.append("")
            if self.license_info.get('url'):
                content.append(f"This project is licensed under the [{self.license_info['name']}]({self.license_info['url']}) License.")
            else:
                content.append(f"This project is licensed under the {self.license_info['name']} License.")
            content.append("")
        
        if self.contact_info:
            content.append("## Contact")
            content.append("")
            for method, value in self.contact_info.items():
                content.append(f"- **{method}**: {value}")
            content.append("")
        
        if self.acknowledgments:
            content.append("## Acknowledgments")
            content.append("")
            content.extend(self.acknowledgments)
            content.append("")
        
        content.extend(self.sections)
        return "\n".join(content)

# Test Step 5 - Complete README
print("=== Step 5: Complete README with Contribution Guidelines and Licensing ===")
readme = ReadmeBuilder()
readme.add_title("My Python Project") \
      .add_description("A comprehensive Python library for demonstration purposes. This project showcases best practices in Python development and documentation.") \
      .add_badge("Version", "https://pypi.org/project/myproject/", "https://img.shields.io/pypi/v/myproject") \
      .add_badge("License", "https://github.com/user/myproject/blob/main/LICENSE", "https://img.shields.io/github/license/user/myproject") \
      .add_badge("Tests", "https://github.com/user/myproject/actions", "https://img.shields.io/github/workflow/status/user/myproject/tests") \
      .add_feature("Easy to use API with intuitive design") \
      .add_feature("Comprehensive documentation and examples") \
      .add_feature("Cross-platform compatibility (Windows, macOS, Linux)") \
      .add_feature("Extensive test coverage") \
      .add_requirement("Python 3.8 or higher") \
      .add_requirement("pip package manager") \
      .add_installation_method("Using pip", ["pip install myproject"]) \
      .add_installation_method("From source", [
          "git clone https://github.com/user/myproject.git",
          "cd myproject",
          "pip install -e ."
      ]) \
      .add_usage_example(
          "Basic Usage",
          "Here's how to get started with the basic functionality:",
          "from myproject import MyClass\n\n# Create an instance\nobj = MyClass()\nresult = obj.process_data('hello world')\nprint(result)  # Output: processed data"
      ) \
      .add_usage_example(
          "Advanced Usage",
          "For more complex scenarios with configuration:",
          "from myproject import AdvancedProcessor\n\nprocessor = AdvancedProcessor(config={'verbose': True})\nwith processor.batch_mode():\n    results = processor.process_multiple(['data1', 'data2'])\n    print(f'Processed {len(results)} items')"
      ) \
      .add_api_method(
          "MyClass.process_data(data: str) -> str",
          "Processes input data and returns the result.",
          "obj = MyClass()\nresult = obj.process_data('input')"
      ) \
      .add_api_method(
          "AdvancedProcessor.batch_mode()",
          "Context manager for batch processing operations.",
          "with processor.batch_mode():\n    # batch operations here\n    pass"
      ) \
      .add_contribution_step("Fork the repository") \
      .add_contribution_step("Create a feature branch (`git checkout -b feature/amazing-feature`)") \
      .add_contribution_step("Make your changes and add tests") \
      .add_contribution_step("Run the test suite (`python -m pytest`)") \
      .add_contribution_step("Commit your changes (`git commit -m 'Add amazing feature'`)") \
      .add_contribution_step("Push to the branch (`git push origin feature/amazing-feature`)") \
      .add_contribution_step("Open a Pull Request") \
      .set_license("MIT", "https://opensource.org/licenses/MIT") \
      .add_contact("Email", "developer@example.com") \
      .add_contact("GitHub", "https://github.com/user") \
      .add_contact("Twitter", "@developer") \
      .add_acknowledgment("Thanks to all contributors who have helped improve this project") \
      .add_acknowledgment("Inspired by best practices from the Python community") \
      .add_acknowledgment("Special thanks to the open source community")

print(readme.build())
print()

# Demonstration of README file generation
print("=== README File Generation Complete ===")
print("This comprehensive README builder demonstrates:")
print("✓ Professional project structure")
print("✓ Clear installation instructions")
print("✓ Practical usage examples")
print("✓ API documentation")
print("✓ Contribution guidelines")
print("✓ Proper licensing information")
print("✓ Contact and acknowledgment sections")
print("\nYou can now generate professional README files for any Python project!")

