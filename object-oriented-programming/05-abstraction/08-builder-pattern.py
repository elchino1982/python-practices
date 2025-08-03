"""Question: Implement the Builder pattern to construct complex objects step by step.

Create a computer builder that can construct different types of computers
(gaming, office, server) with various components.

Requirements:
1. Create a Computer class with multiple components
2. Create an abstract ComputerBuilder
3. Create concrete builders for different computer types
4. Create a Director class to orchestrate the building process
5. Demonstrate building different computer configurations

Example usage:
    director = ComputerDirector()
    gaming_builder = GamingComputerBuilder()
    computer = director.build_computer(gaming_builder)
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
# - What is the complex object you're building?
# - What abstract builder interface do you need?
# - How do concrete builders implement the interface?
# - What role does the director play?
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


# Step 1: Import modules and create the complex product class
# ===============================================================================

# Explanation:
# The Builder pattern starts with a complex object that has many parts.
# We'll create a Computer class with multiple optional components.

from abc import ABC, abstractmethod
from typing import Optional

class Computer:
    """Complex object to be built."""
    
    def __init__(self):
        self.cpu: Optional[str] = None
        self.ram: Optional[str] = None
        self.storage: Optional[str] = None
        self.gpu: Optional[str] = None
        self.motherboard: Optional[str] = None
        self.power_supply: Optional[str] = None
        self.case: Optional[str] = None
        self.cooling: Optional[str] = None
        self.extras: list = []
    
    def __str__(self):
        """String representation of the computer."""
        specs = []
        specs.append(f"CPU: {self.cpu}")
        specs.append(f"RAM: {self.ram}")
        specs.append(f"Storage: {self.storage}")
        specs.append(f"GPU: {self.gpu}")
        specs.append(f"Motherboard: {self.motherboard}")
        specs.append(f"Power Supply: {self.power_supply}")
        specs.append(f"Case: {self.case}")
        specs.append(f"Cooling: {self.cooling}")
        
        if self.extras:
            specs.append(f"Extras: {', '.join(self.extras)}")
        
        return "Computer Specifications:\n" + "\n".join(f"  {spec}" for spec in specs)

# What we accomplished in this step:
# - Created the complex Computer class with multiple components
# - Added string representation for easy display


# Step 2: Create the abstract builder interface
# ===============================================================================

# Explanation:
# The abstract builder defines the interface for constructing parts of the product.
# Each method builds a specific part of the computer.

from abc import ABC, abstractmethod
from typing import Optional

class Computer:
    """Complex object to be built."""
    
    def __init__(self):
        self.cpu: Optional[str] = None
        self.ram: Optional[str] = None
        self.storage: Optional[str] = None
        self.gpu: Optional[str] = None
        self.motherboard: Optional[str] = None
        self.power_supply: Optional[str] = None
        self.case: Optional[str] = None
        self.cooling: Optional[str] = None
        self.extras: list = []
    
    def __str__(self):
        """String representation of the computer."""
        specs = []
        specs.append(f"CPU: {self.cpu}")
        specs.append(f"RAM: {self.ram}")
        specs.append(f"Storage: {self.storage}")
        specs.append(f"GPU: {self.gpu}")
        specs.append(f"Motherboard: {self.motherboard}")
        specs.append(f"Power Supply: {self.power_supply}")
        specs.append(f"Case: {self.case}")
        specs.append(f"Cooling: {self.cooling}")
        
        if self.extras:
            specs.append(f"Extras: {', '.join(self.extras)}")
        
        return "Computer Specifications:\n" + "\n".join(f"  {spec}" for spec in specs)

class ComputerBuilder(ABC):
    """Abstract builder for computers."""
    
    def __init__(self):
        self.computer = Computer()
    
    def reset(self):
        """Reset the builder to start building a new computer."""
        self.computer = Computer()
    
    @abstractmethod
    def build_cpu(self):
        """Build CPU component."""
        pass
    
    @abstractmethod
    def build_ram(self):
        """Build RAM component."""
        pass
    
    @abstractmethod
    def build_storage(self):
        """Build storage component."""
        pass
    
    @abstractmethod
    def build_gpu(self):
        """Build GPU component."""
        pass
    
    @abstractmethod
    def build_motherboard(self):
        """Build motherboard component."""
        pass
    
    @abstractmethod
    def build_power_supply(self):
        """Build power supply component."""
        pass
    
    @abstractmethod
    def build_case(self):
        """Build case component."""
        pass
    
    @abstractmethod
    def build_cooling(self):
        """Build cooling component."""
        pass
    
    def add_extra(self, extra: str):
        """Add extra component."""
        self.computer.extras.append(extra)
    
    def get_computer(self) -> Computer:
        """Get the built computer."""
        result = self.computer
        self.reset()
        return result

# What we accomplished in this step:
# - Created abstract builder interface with all necessary methods
# - Added reset functionality and computer retrieval


# Step 3: Create concrete builder for gaming computers
# ===============================================================================

# Explanation:
# Concrete builders implement the abstract interface and provide specific
# implementations for each component based on the computer type.

from abc import ABC, abstractmethod
from typing import Optional

class Computer:
    """Complex object to be built."""
    
    def __init__(self):
        self.cpu: Optional[str] = None
        self.ram: Optional[str] = None
        self.storage: Optional[str] = None
        self.gpu: Optional[str] = None
        self.motherboard: Optional[str] = None
        self.power_supply: Optional[str] = None
        self.case: Optional[str] = None
        self.cooling: Optional[str] = None
        self.extras: list = []
    
    def __str__(self):
        """String representation of the computer."""
        specs = []
        specs.append(f"CPU: {self.cpu}")
        specs.append(f"RAM: {self.ram}")
        specs.append(f"Storage: {self.storage}")
        specs.append(f"GPU: {self.gpu}")
        specs.append(f"Motherboard: {self.motherboard}")
        specs.append(f"Power Supply: {self.power_supply}")
        specs.append(f"Case: {self.case}")
        specs.append(f"Cooling: {self.cooling}")
        
        if self.extras:
            specs.append(f"Extras: {', '.join(self.extras)}")
        
        return "Computer Specifications:\n" + "\n".join(f"  {spec}" for spec in specs)

class ComputerBuilder(ABC):
    """Abstract builder for computers."""
    
    def __init__(self):
        self.computer = Computer()
    
    def reset(self):
        """Reset the builder to start building a new computer."""
        self.computer = Computer()
    
    @abstractmethod
    def build_cpu(self):
        """Build CPU component."""
        pass
    
    @abstractmethod
    def build_ram(self):
        """Build RAM component."""
        pass
    
    @abstractmethod
    def build_storage(self):
        """Build storage component."""
        pass
    
    @abstractmethod
    def build_gpu(self):
        """Build GPU component."""
        pass
    
    @abstractmethod
    def build_motherboard(self):
        """Build motherboard component."""
        pass
    
    @abstractmethod
    def build_power_supply(self):
        """Build power supply component."""
        pass
    
    @abstractmethod
    def build_case(self):
        """Build case component."""
        pass
    
    @abstractmethod
    def build_cooling(self):
        """Build cooling component."""
        pass
    
    def add_extra(self, extra: str):
        """Add extra component."""
        self.computer.extras.append(extra)
    
    def get_computer(self) -> Computer:
        """Get the built computer."""
        result = self.computer
        self.reset()
        return result

class GamingComputerBuilder(ComputerBuilder):
    """Builder for gaming computers."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i7-13700K"
    
    def build_ram(self):
        self.computer.ram = "32GB DDR5-5600"
    
    def build_storage(self):
        self.computer.storage = "1TB NVMe SSD + 2TB HDD"
    
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4080"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS ROG Strix Z790-E"
    
    def build_power_supply(self):
        self.computer.power_supply = "850W 80+ Gold Modular"
    
    def build_case(self):
        self.computer.case = "NZXT H7 Elite with RGB"
    
    def build_cooling(self):
        self.computer.cooling = "AIO Liquid Cooler 280mm"

# What we accomplished in this step:
# - Created gaming computer builder with high-performance components
# - Each method sets appropriate gaming-focused specifications


# Step 4: Create concrete builder for office computers
# ===============================================================================

# Explanation:
# Office computers need different specifications - more budget-friendly
# and focused on productivity rather than performance.

from abc import ABC, abstractmethod
from typing import Optional

class Computer:
    """Complex object to be built."""
    
    def __init__(self):
        self.cpu: Optional[str] = None
        self.ram: Optional[str] = None
        self.storage: Optional[str] = None
        self.gpu: Optional[str] = None
        self.motherboard: Optional[str] = None
        self.power_supply: Optional[str] = None
        self.case: Optional[str] = None
        self.cooling: Optional[str] = None
        self.extras: list = []
    
    def __str__(self):
        """String representation of the computer."""
        specs = []
        specs.append(f"CPU: {self.cpu}")
        specs.append(f"RAM: {self.ram}")
        specs.append(f"Storage: {self.storage}")
        specs.append(f"GPU: {self.gpu}")
        specs.append(f"Motherboard: {self.motherboard}")
        specs.append(f"Power Supply: {self.power_supply}")
        specs.append(f"Case: {self.case}")
        specs.append(f"Cooling: {self.cooling}")
        
        if self.extras:
            specs.append(f"Extras: {', '.join(self.extras)}")
        
        return "Computer Specifications:\n" + "\n".join(f"  {spec}" for spec in specs)

class ComputerBuilder(ABC):
    """Abstract builder for computers."""
    
    def __init__(self):
        self.computer = Computer()
    
    def reset(self):
        """Reset the builder to start building a new computer."""
        self.computer = Computer()
    
    @abstractmethod
    def build_cpu(self):
        """Build CPU component."""
        pass
    
    @abstractmethod
    def build_ram(self):
        """Build RAM component."""
        pass
    
    @abstractmethod
    def build_storage(self):
        """Build storage component."""
        pass
    
    @abstractmethod
    def build_gpu(self):
        """Build GPU component."""
        pass
    
    @abstractmethod
    def build_motherboard(self):
        """Build motherboard component."""
        pass
    
    @abstractmethod
    def build_power_supply(self):
        """Build power supply component."""
        pass
    
    @abstractmethod
    def build_case(self):
        """Build case component."""
        pass
    
    @abstractmethod
    def build_cooling(self):
        """Build cooling component."""
        pass
    
    def add_extra(self, extra: str):
        """Add extra component."""
        self.computer.extras.append(extra)
    
    def get_computer(self) -> Computer:
        """Get the built computer."""
        result = self.computer
        self.reset()
        return result

class GamingComputerBuilder(ComputerBuilder):
    """Builder for gaming computers."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i7-13700K"
    
    def build_ram(self):
        self.computer.ram = "32GB DDR5-5600"
    
    def build_storage(self):
        self.computer.storage = "1TB NVMe SSD + 2TB HDD"
    
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4080"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS ROG Strix Z790-E"
    
    def build_power_supply(self):
        self.computer.power_supply = "850W 80+ Gold Modular"
    
    def build_case(self):
        self.computer.case = "NZXT H7 Elite with RGB"
    
    def build_cooling(self):
        self.computer.cooling = "AIO Liquid Cooler 280mm"

class OfficeComputerBuilder(ComputerBuilder):
    """Builder for office computers."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5-13400"
    
    def build_ram(self):
        self.computer.ram = "16GB DDR4-3200"
    
    def build_storage(self):
        self.computer.storage = "512GB NVMe SSD"
    
    def build_gpu(self):
        self.computer.gpu = "Integrated Graphics"
    
    def build_motherboard(self):
        self.computer.motherboard = "MSI Pro B660M-A"
    
    def build_power_supply(self):
        self.computer.power_supply = "500W 80+ Bronze"
    
    def build_case(self):
        self.computer.case = "Compact Mini-ITX Case"
    
    def build_cooling(self):
        self.computer.cooling = "Stock CPU Cooler"

# What we accomplished in this step:
# - Created office computer builder with budget-friendly components
# - Focused on efficiency and cost-effectiveness


# Step 5: Create the director class
# ===============================================================================

# Explanation:
# The director orchestrates the building process. It knows the order
# in which to call builder methods to construct the product.

from abc import ABC, abstractmethod
from typing import Optional

class Computer:
    """Complex object to be built."""
    
    def __init__(self):
        self.cpu: Optional[str] = None
        self.ram: Optional[str] = None
        self.storage: Optional[str] = None
        self.gpu: Optional[str] = None
        self.motherboard: Optional[str] = None
        self.power_supply: Optional[str] = None
        self.case: Optional[str] = None
        self.cooling: Optional[str] = None
        self.extras: list = []
    
    def __str__(self):
        """String representation of the computer."""
        specs = []
        specs.append(f"CPU: {self.cpu}")
        specs.append(f"RAM: {self.ram}")
        specs.append(f"Storage: {self.storage}")
        specs.append(f"GPU: {self.gpu}")
        specs.append(f"Motherboard: {self.motherboard}")
        specs.append(f"Power Supply: {self.power_supply}")
        specs.append(f"Case: {self.case}")
        specs.append(f"Cooling: {self.cooling}")
        
        if self.extras:
            specs.append(f"Extras: {', '.join(self.extras)}")
        
        return "Computer Specifications:\n" + "\n".join(f"  {spec}" for spec in specs)

class ComputerBuilder(ABC):
    """Abstract builder for computers."""
    
    def __init__(self):
        self.computer = Computer()
    
    def reset(self):
        """Reset the builder to start building a new computer."""
        self.computer = Computer()
    
    @abstractmethod
    def build_cpu(self):
        """Build CPU component."""
        pass
    
    @abstractmethod
    def build_ram(self):
        """Build RAM component."""
        pass
    
    @abstractmethod
    def build_storage(self):
        """Build storage component."""
        pass
    
    @abstractmethod
    def build_gpu(self):
        """Build GPU component."""
        pass
    
    @abstractmethod
    def build_motherboard(self):
        """Build motherboard component."""
        pass
    
    @abstractmethod
    def build_power_supply(self):
        """Build power supply component."""
        pass
    
    @abstractmethod
    def build_case(self):
        """Build case component."""
        pass
    
    @abstractmethod
    def build_cooling(self):
        """Build cooling component."""
        pass
    
    def add_extra(self, extra: str):
        """Add extra component."""
        self.computer.extras.append(extra)
    
    def get_computer(self) -> Computer:
        """Get the built computer."""
        result = self.computer
        self.reset()
        return result

class GamingComputerBuilder(ComputerBuilder):
    """Builder for gaming computers."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i7-13700K"
    
    def build_ram(self):
        self.computer.ram = "32GB DDR5-5600"
    
    def build_storage(self):
        self.computer.storage = "1TB NVMe SSD + 2TB HDD"
    
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4080"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS ROG Strix Z790-E"
    
    def build_power_supply(self):
        self.computer.power_supply = "850W 80+ Gold Modular"
    
    def build_case(self):
        self.computer.case = "NZXT H7 Elite with RGB"
    
    def build_cooling(self):
        self.computer.cooling = "AIO Liquid Cooler 280mm"

class OfficeComputerBuilder(ComputerBuilder):
    """Builder for office computers."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5-13400"
    
    def build_ram(self):
        self.computer.ram = "16GB DDR4-3200"
    
    def build_storage(self):
        self.computer.storage = "512GB NVMe SSD"
    
    def build_gpu(self):
        self.computer.gpu = "Integrated Graphics"
    
    def build_motherboard(self):
        self.computer.motherboard = "MSI Pro B660M-A"
    
    def build_power_supply(self):
        self.computer.power_supply = "500W 80+ Bronze"
    
    def build_case(self):
        self.computer.case = "Compact Mini-ITX Case"
    
    def build_cooling(self):
        self.computer.cooling = "Stock CPU Cooler"

class ComputerDirector:
    """Director that orchestrates the building process."""
    
    def build_computer(self, builder: ComputerBuilder) -> Computer:
        """Build a complete computer using the provided builder."""
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()
        builder.build_gpu()
        builder.build_motherboard()
        builder.build_power_supply()
        builder.build_case()
        builder.build_cooling()
        
        return builder.get_computer()
    
    def build_basic_computer(self, builder: ComputerBuilder) -> Computer:
        """Build a basic computer with minimal components."""
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()
        builder.build_motherboard()
        builder.build_power_supply()
        
        return builder.get_computer()

# What we accomplished in this step:
# - Created director to orchestrate the building process
# - Added different building strategies (complete, basic)


# Step 6: Test the complete implementation
# ===============================================================================

# Explanation:
# Let's test our Builder pattern implementation with different computer types.

from abc import ABC, abstractmethod
from typing import Optional

class Computer:
    """Complex object to be built."""
    
    def __init__(self):
        self.cpu: Optional[str] = None
        self.ram: Optional[str] = None
        self.storage: Optional[str] = None
        self.gpu: Optional[str] = None
        self.motherboard: Optional[str] = None
        self.power_supply: Optional[str] = None
        self.case: Optional[str] = None
        self.cooling: Optional[str] = None
        self.extras: list = []
    
    def __str__(self):
        """String representation of the computer."""
        specs = []
        specs.append(f"CPU: {self.cpu}")
        specs.append(f"RAM: {self.ram}")
        specs.append(f"Storage: {self.storage}")
        specs.append(f"GPU: {self.gpu}")
        specs.append(f"Motherboard: {self.motherboard}")
        specs.append(f"Power Supply: {self.power_supply}")
        specs.append(f"Case: {self.case}")
        specs.append(f"Cooling: {self.cooling}")
        
        if self.extras:
            specs.append(f"Extras: {', '.join(self.extras)}")
        
        return "Computer Specifications:\n" + "\n".join(f"  {spec}" for spec in specs)

class ComputerBuilder(ABC):
    """Abstract builder for computers."""
    
    def __init__(self):
        self.computer = Computer()
    
    def reset(self):
        """Reset the builder to start building a new computer."""
        self.computer = Computer()
    
    @abstractmethod
    def build_cpu(self):
        """Build CPU component."""
        pass
    
    @abstractmethod
    def build_ram(self):
        """Build RAM component."""
        pass
    
    @abstractmethod
    def build_storage(self):
        """Build storage component."""
        pass
    
    @abstractmethod
    def build_gpu(self):
        """Build GPU component."""
        pass
    
    @abstractmethod
    def build_motherboard(self):
        """Build motherboard component."""
        pass
    
    @abstractmethod
    def build_power_supply(self):
        """Build power supply component."""
        pass
    
    @abstractmethod
    def build_case(self):
        """Build case component."""
        pass
    
    @abstractmethod
    def build_cooling(self):
        """Build cooling component."""
        pass
    
    def add_extra(self, extra: str):
        """Add extra component."""
        self.computer.extras.append(extra)
    
    def get_computer(self) -> Computer:
        """Get the built computer."""
        result = self.computer
        self.reset()
        return result

class GamingComputerBuilder(ComputerBuilder):
    """Builder for gaming computers."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i7-13700K"
    
    def build_ram(self):
        self.computer.ram = "32GB DDR5-5600"
    
    def build_storage(self):
        self.computer.storage = "1TB NVMe SSD + 2TB HDD"
    
    def build_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4080"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS ROG Strix Z790-E"
    
    def build_power_supply(self):
        self.computer.power_supply = "850W 80+ Gold Modular"
    
    def build_case(self):
        self.computer.case = "NZXT H7 Elite with RGB"
    
    def build_cooling(self):
        self.computer.cooling = "AIO Liquid Cooler 280mm"

class OfficeComputerBuilder(ComputerBuilder):
    """Builder for office computers."""
    
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5-13400"
    
    def build_ram(self):
        self.computer.ram = "16GB DDR4-3200"
    
    def build_storage(self):
        self.computer.storage = "512GB NVMe SSD"
    
    def build_gpu(self):
        self.computer.gpu = "Integrated Graphics"
    
    def build_motherboard(self):
        self.computer.motherboard = "MSI Pro B660M-A"
    
    def build_power_supply(self):
        self.computer.power_supply = "500W 80+ Bronze"
    
    def build_case(self):
        self.computer.case = "Compact Mini-ITX Case"
    
    def build_cooling(self):
        self.computer.cooling = "Stock CPU Cooler"

class ComputerDirector:
    """Director that orchestrates the building process."""
    
    def build_computer(self, builder: ComputerBuilder) -> Computer:
        """Build a complete computer using the provided builder."""
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()
        builder.build_gpu()
        builder.build_motherboard()
        builder.build_power_supply()
        builder.build_case()
        builder.build_cooling()
        
        return builder.get_computer()
    
    def build_basic_computer(self, builder: ComputerBuilder) -> Computer:
        """Build a basic computer with minimal components."""
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()
        builder.build_motherboard()
        builder.build_power_supply()
        
        return builder.get_computer()

director = ComputerDirector()

print("=== Testing Builder Pattern ===\n")

# Build gaming computer
print("1. Gaming Computer:")
gaming_builder = GamingComputerBuilder()
gaming_computer = director.build_computer(gaming_builder)
print(gaming_computer)
print()

# Build office computer
print("2. Office Computer:")
office_builder = OfficeComputerBuilder()
office_computer = director.build_computer(office_builder)
print(office_computer)
print()

# Build basic computer
print("3. Basic Office Computer:")
basic_builder = OfficeComputerBuilder()
basic_computer = director.build_basic_computer(basic_builder)
print(basic_computer)

# What we accomplished in this step:
# - Tested all builder types with the director
# - Demonstrated different building strategies
# - Showed how the same process creates different products


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step solution!
#
# Key concepts learned:
# - Builder pattern structure and purpose
# - Complex object construction step by step
# - Abstract builder interface and concrete implementations
# - Director class for orchestrating construction
# - Different building strategies for flexibility
# - Separation of construction and representation
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding a workstation builder!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================