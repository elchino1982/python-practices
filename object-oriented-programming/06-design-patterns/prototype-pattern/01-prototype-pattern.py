"""Question: Implement the Prototype pattern to create objects by cloning existing instances.

Create a document template system where complex document objects can be cloned
to create new instances without going through expensive initialization.

Requirements:
1. Create abstract Prototype interface with clone method
2. Implement concrete prototypes (Report, Invoice, Letter templates)
3. Create PrototypeManager to manage and clone prototypes
4. Demonstrate deep vs shallow cloning
5. Show performance benefits of cloning vs creation
6. Handle complex nested objects properly

Example usage:
    manager = PrototypeManager()
    report_template = manager.get_prototype("report")
    new_report = report_template.clone()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!

# Try to implement your solution here:
# (Write your code below this line)


















































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What is the abstract Prototype interface?
# - How do you implement deep vs shallow cloning?
# - What complex objects need to be cloned?
# - How does the PrototypeManager work?
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


# Step 1: Import modules and create the abstract Prototype interface
# ===============================================================================

# Explanation:
# The Prototype pattern starts with an abstract interface that defines
# the clone method. This allows objects to create copies of themselves.

from abc import ABC, abstractmethod
import copy
from typing import Dict, Any, List
from datetime import datetime

class Prototype(ABC):
    """Abstract prototype interface."""
    
    @abstractmethod
    def clone(self):
        """Create a copy of this object."""
        pass
    
    @abstractmethod
    def __str__(self):
        """String representation of the object."""
        pass

# What we accomplished in this step:
# - Created the abstract Prototype interface with clone method
# - Added string representation for easy display


# Step 2: Create complex document classes with nested objects
# ===============================================================================

# Explanation:
# We'll create complex document classes that have nested objects to demonstrate
# deep vs shallow cloning. Each document has metadata, content, and formatting.

class DocumentMetadata:
    """Metadata for documents - demonstrates nested objects."""
    
    def __init__(self, title: str = "", author: str = "", created: datetime = None):
        self.title = title
        self.author = author
        self.created = created or datetime.now()
        self.tags: List[str] = []
        self.properties: Dict[str, Any] = {}
    
    def __str__(self):
        return f"Metadata(title='{self.title}', author='{self.author}', tags={self.tags})"

class DocumentContent:
    """Content structure for documents."""
    
    def __init__(self):
        self.sections: List[str] = []
        self.images: List[str] = []
        self.tables: List[Dict[str, Any]] = []
    
    def add_section(self, section: str):
        self.sections.append(section)
    
    def add_image(self, image_path: str):
        self.images.append(image_path)
    
    def add_table(self, table_data: Dict[str, Any]):
        self.tables.append(table_data)
    
    def __str__(self):
        return f"Content(sections={len(self.sections)}, images={len(self.images)}, tables={len(self.tables)})"

class DocumentFormatting:
    """Formatting settings for documents."""
    
    def __init__(self):
        self.font_family: str = "Arial"
        self.font_size: int = 12
        self.margins: Dict[str, float] = {"top": 1.0, "bottom": 1.0, "left": 1.0, "right": 1.0}
        self.colors: Dict[str, str] = {"text": "#000000", "background": "#FFFFFF"}
    
    def __str__(self):
        return f"Formatting(font='{self.font_family}', size={self.font_size})"

# What we accomplished in this step:
# - Created complex nested objects (DocumentMetadata, DocumentContent, DocumentFormatting)
# - These will demonstrate the importance of deep vs shallow cloning


# Step 3: Create concrete prototype classes (Report, Invoice, Letter)
# ===============================================================================

# Explanation:
# Now we'll create concrete document classes that implement the Prototype interface.
# Each class will have different default configurations and cloning behavior.

from abc import ABC, abstractmethod
import copy
from typing import Dict, Any, List
from datetime import datetime

class Prototype(ABC):
    """Abstract prototype interface."""
    
    @abstractmethod
    def clone(self):
        """Create a copy of this object."""
        pass
    
    @abstractmethod
    def __str__(self):
        """String representation of the object."""
        pass

class DocumentMetadata:
    """Metadata for documents - demonstrates nested objects."""
    
    def __init__(self, title: str = "", author: str = "", created: datetime = None):
        self.title = title
        self.author = author
        self.created = created or datetime.now()
        self.tags: List[str] = []
        self.properties: Dict[str, Any] = {}
    
    def __str__(self):
        return f"Metadata(title='{self.title}', author='{self.author}', tags={self.tags})"

class DocumentContent:
    """Content structure for documents."""
    
    def __init__(self):
        self.sections: List[str] = []
        self.images: List[str] = []
        self.tables: List[Dict[str, Any]] = []
    
    def add_section(self, section: str):
        self.sections.append(section)
    
    def add_image(self, image_path: str):
        self.images.append(image_path)
    
    def add_table(self, table_data: Dict[str, Any]):
        self.tables.append(table_data)
    
    def __str__(self):
        return f"Content(sections={len(self.sections)}, images={len(self.images)}, tables={len(self.tables)})"

class DocumentFormatting:
    """Formatting settings for documents."""
    
    def __init__(self):
        self.font_family: str = "Arial"
        self.font_size: int = 12
        self.margins: Dict[str, float] = {"top": 1.0, "bottom": 1.0, "left": 1.0, "right": 1.0}
        self.colors: Dict[str, str] = {"text": "#000000", "background": "#FFFFFF"}
    
    def __str__(self):
        return f"Formatting(font='{self.font_family}', size={self.font_size})"

class ReportDocument(Prototype):
    """Concrete prototype for business reports."""
    
    def __init__(self):
        self.metadata = DocumentMetadata("Business Report Template", "System")
        self.metadata.tags = ["business", "report", "template"]
        
        self.content = DocumentContent()
        self.content.add_section("Executive Summary")
        self.content.add_section("Introduction")
        self.content.add_section("Analysis")
        self.content.add_section("Conclusions")
        self.content.add_section("Recommendations")
        
        self.formatting = DocumentFormatting()
        self.formatting.font_family = "Times New Roman"
        self.formatting.font_size = 11
        self.formatting.margins = {"top": 1.5, "bottom": 1.0, "left": 1.25, "right": 1.0}
        
        self.report_type = "business"
        self.charts_enabled = True
        self.confidentiality_level = "internal"
    
    def clone(self):
        """Create a deep copy of this report."""
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"ReportDocument(type='{self.report_type}', {self.metadata}, {self.content}, {self.formatting})"

class InvoiceDocument(Prototype):
    """Concrete prototype for invoices."""
    
    def __init__(self):
        self.metadata = DocumentMetadata("Invoice Template", "Billing System")
        self.metadata.tags = ["invoice", "billing", "template"]
        
        self.content = DocumentContent()
        self.content.add_section("Company Header")
        self.content.add_section("Bill To")
        self.content.add_section("Invoice Details")
        self.content.add_section("Line Items")
        self.content.add_section("Totals")
        self.content.add_section("Payment Terms")
        
        self.formatting = DocumentFormatting()
        self.formatting.font_family = "Arial"
        self.formatting.font_size = 10
        self.formatting.colors = {"text": "#000000", "background": "#FFFFFF", "header": "#0066CC"}
        
        self.invoice_number = ""
        self.tax_rate = 0.0
        self.currency = "USD"
        self.payment_terms = "Net 30"
    
    def clone(self):
        """Create a deep copy of this invoice."""
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"InvoiceDocument(currency='{self.currency}', {self.metadata}, {self.content}, {self.formatting})"

class LetterDocument(Prototype):
    """Concrete prototype for formal letters."""
    
    def __init__(self):
        self.metadata = DocumentMetadata("Formal Letter Template", "Office System")
        self.metadata.tags = ["letter", "formal", "template"]
        
        self.content = DocumentContent()
        self.content.add_section("Sender Address")
        self.content.add_section("Date")
        self.content.add_section("Recipient Address")
        self.content.add_section("Salutation")
        self.content.add_section("Body")
        self.content.add_section("Closing")
        self.content.add_section("Signature")
        
        self.formatting = DocumentFormatting()
        self.formatting.font_family = "Calibri"
        self.formatting.font_size = 12
        self.formatting.margins = {"top": 1.0, "bottom": 1.0, "left": 1.0, "right": 1.0}
        
        self.letter_type = "formal"
        self.letterhead_enabled = True
        self.signature_required = True
    
    def clone(self):
        """Create a deep copy of this letter."""
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"LetterDocument(type='{self.letter_type}', {self.metadata}, {self.content}, {self.formatting})"

# What we accomplished in this step:
# - Created three concrete prototype classes with complex nested objects
# - Each class has different default configurations and uses deep copying
# - Demonstrated how prototypes encapsulate creation logic


# Step 4: Create the PrototypeManager class
# ===============================================================================

# Explanation:
# The PrototypeManager stores prototype instances and provides a way to clone them.
# This centralizes prototype management and provides a clean interface for clients.

class PrototypeManager:
    """Manages prototype instances and provides cloning interface."""
    
    def __init__(self):
        self._prototypes: Dict[str, Prototype] = {}
        self._initialize_prototypes()
    
    def _initialize_prototypes(self):
        """Initialize default prototypes."""
        self._prototypes["report"] = ReportDocument()
        self._prototypes["invoice"] = InvoiceDocument()
        self._prototypes["letter"] = LetterDocument()
    
    def register_prototype(self, name: str, prototype: Prototype):
        """Register a new prototype."""
        self._prototypes[name] = prototype
    
    def unregister_prototype(self, name: str):
        """Remove a prototype."""
        if name in self._prototypes:
            del self._prototypes[name]
    
    def get_prototype(self, name: str) -> Prototype:
        """Get a clone of the specified prototype."""
        if name not in self._prototypes:
            raise ValueError(f"Prototype '{name}' not found")
        return self._prototypes[name].clone()
    
    def list_prototypes(self) -> List[str]:
        """List all available prototype names."""
        return list(self._prototypes.keys())
    
    def get_prototype_info(self, name: str) -> str:
        """Get information about a prototype without cloning it."""
        if name not in self._prototypes:
            raise ValueError(f"Prototype '{name}' not found")
        return str(self._prototypes[name])
    
    def __str__(self):
        return f"PrototypeManager(prototypes={list(self._prototypes.keys())})"

# What we accomplished in this step:
# - Created PrototypeManager to centralize prototype management
# - Provided methods to register, unregister, and clone prototypes
# - Added utility methods for listing and inspecting prototypes


# Step 5: Demonstrate deep vs shallow cloning
# ===============================================================================

# Explanation:
# Let's create classes that demonstrate the difference between deep and shallow cloning.
# This is crucial for understanding when to use each approach.

class ShallowCloneDocument(Prototype):
    """Document that uses shallow cloning - demonstrates potential issues."""
    
    def __init__(self):
        self.metadata = DocumentMetadata("Shallow Clone Template", "Test System")
        self.metadata.tags = ["shallow", "test"]
        
        self.content = DocumentContent()
        self.content.add_section("Shared Section")
        
        self.formatting = DocumentFormatting()
        self.shared_data = {"shared_list": [1, 2, 3], "shared_dict": {"key": "value"}}
    
    def clone(self):
        """Create a shallow copy - nested objects are shared!"""
        return copy.copy(self)  # Shallow copy instead of deepcopy
    
    def __str__(self):
        return f"ShallowCloneDocument(shared_data={self.shared_data})"

class DeepCloneDocument(Prototype):
    """Document that uses deep cloning - safe for independent modifications."""
    
    def __init__(self):
        self.metadata = DocumentMetadata("Deep Clone Template", "Test System")
        self.metadata.tags = ["deep", "test"]
        
        self.content = DocumentContent()
        self.content.add_section("Independent Section")
        
        self.formatting = DocumentFormatting()
        self.independent_data = {"independent_list": [1, 2, 3], "independent_dict": {"key": "value"}}
    
    def clone(self):
        """Create a deep copy - all nested objects are independent."""
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"DeepCloneDocument(independent_data={self.independent_data})"

def demonstrate_cloning_differences():
    """Demonstrate the difference between shallow and deep cloning."""
    print("=== Cloning Demonstration ===")
    
    # Shallow cloning demonstration
    print("\n1. Shallow Cloning Issues:")
    shallow_original = ShallowCloneDocument()
    shallow_clone = shallow_original.clone()
    
    print(f"Original: {shallow_original}")
    print(f"Clone: {shallow_clone}")
    print(f"Are they the same object? {shallow_original is shallow_clone}")
    print(f"Do they share nested objects? {shallow_original.shared_data is shallow_clone.shared_data}")
    
    # Modify the clone's shared data
    shallow_clone.shared_data["shared_list"].append(4)
    shallow_clone.shared_data["new_key"] = "new_value"
    
    print(f"\nAfter modifying clone:")
    print(f"Original: {shallow_original}")
    print(f"Clone: {shallow_clone}")
    print("Notice: Both objects were affected!")
    
    # Deep cloning demonstration
    print("\n2. Deep Cloning Safety:")
    deep_original = DeepCloneDocument()
    deep_clone = deep_original.clone()
    
    print(f"Original: {deep_original}")
    print(f"Clone: {deep_clone}")
    print(f"Are they the same object? {deep_original is deep_clone}")
    print(f"Do they share nested objects? {deep_original.independent_data is deep_clone.independent_data}")
    
    # Modify the clone's independent data
    deep_clone.independent_data["independent_list"].append(4)
    deep_clone.independent_data["new_key"] = "new_value"
    
    print(f"\nAfter modifying clone:")
    print(f"Original: {deep_original}")
    print(f"Clone: {deep_clone}")
    print("Notice: Only the clone was affected!")

# What we accomplished in this step:
# - Demonstrated shallow vs deep cloning with practical examples
# - Showed the risks of shallow cloning with shared mutable objects
# - Illustrated the safety of deep cloning for independent modifications


# Step 6: Performance comparison - cloning vs creation
# ===============================================================================

# Explanation:
# One of the main benefits of the Prototype pattern is performance.
# Let's measure the difference between cloning and creating from scratch.

import time

def measure_performance():
    """Compare performance of cloning vs creating new objects."""
    print("\n=== Performance Comparison ===")
    
    # Setup
    manager = PrototypeManager()
    iterations = 1000
    
    # Measure creation from scratch
    start_time = time.time()
    created_objects = []
    for _ in range(iterations):
        # Creating new objects requires full initialization
        report = ReportDocument()
        invoice = InvoiceDocument()
        letter = LetterDocument()
        created_objects.extend([report, invoice, letter])
    creation_time = time.time() - start_time
    
    # Measure cloning
    start_time = time.time()
    cloned_objects = []
    for _ in range(iterations):
        # Cloning reuses existing initialized objects
        report = manager.get_prototype("report")
        invoice = manager.get_prototype("invoice")
        letter = manager.get_prototype("letter")
        cloned_objects.extend([report, invoice, letter])
    cloning_time = time.time() - start_time
    
    print(f"Creating {iterations * 3} objects from scratch: {creation_time:.4f} seconds")
    print(f"Cloning {iterations * 3} objects: {cloning_time:.4f} seconds")
    print(f"Performance improvement: {creation_time / cloning_time:.2f}x faster")
    print(f"Time saved: {((creation_time - cloning_time) / creation_time) * 100:.1f}%")


# Step 7: Practical usage examples and demonstrations
# ===============================================================================

# Explanation:
# Let's create practical examples showing how to use the Prototype pattern
# in real-world scenarios.

def demonstrate_basic_usage():
    """Demonstrate basic prototype pattern usage."""
    print("\n=== Basic Usage Example ===")
    
    # Create prototype manager
    manager = PrototypeManager()
    
    # List available prototypes
    print(f"Available prototypes: {manager.list_prototypes()}")
    
    # Clone different document types
    print("\n1. Creating documents from prototypes:")
    
    # Create a business report
    report = manager.get_prototype("report")
    report.metadata.title = "Q4 Sales Report"
    report.metadata.author = "Sales Team"
    report.confidentiality_level = "confidential"
    print(f"Created: {report}")
    
    # Create an invoice
    invoice = manager.get_prototype("invoice")
    invoice.metadata.title = "Invoice #INV-2025-001"
    invoice.invoice_number = "INV-2025-001"
    invoice.currency = "EUR"
    invoice.tax_rate = 0.21
    print(f"Created: {invoice}")
    
    # Create a formal letter
    letter = manager.get_prototype("letter")
    letter.metadata.title = "Job Offer Letter"
    letter.metadata.author = "HR Department"
    letter.letter_type = "job_offer"
    print(f"Created: {letter}")

def demonstrate_custom_prototypes():
    """Demonstrate registering and using custom prototypes."""
    print("\n=== Custom Prototypes Example ===")
    
    # Create a custom document type
    class ContractDocument(Prototype):
        def __init__(self):
            self.metadata = DocumentMetadata("Contract Template", "Legal Department")
            self.metadata.tags = ["contract", "legal", "template"]
            
            self.content = DocumentContent()
            self.content.add_section("Parties")
            self.content.add_section("Terms and Conditions")
            self.content.add_section("Payment Terms")
            self.content.add_section("Termination Clause")
            self.content.add_section("Signatures")
            
            self.formatting = DocumentFormatting()
            self.formatting.font_family = "Times New Roman"
            self.formatting.font_size = 11
            
            self.contract_type = "service"
            self.duration_months = 12
            self.auto_renewal = False
        
        def clone(self):
            return copy.deepcopy(self)
        
        def __str__(self):
            return f"ContractDocument(type='{self.contract_type}', duration={self.duration_months})"
    
    # Register custom prototype
    manager = PrototypeManager()
    manager.register_prototype("contract", ContractDocument())
    
    print(f"Available prototypes: {manager.list_prototypes()}")
    
    # Use custom prototype
    contract = manager.get_prototype("contract")
    contract.metadata.title = "Software Development Contract"
    contract.contract_type = "development"
    contract.duration_months = 6
    print(f"Created custom document: {contract}")

def demonstrate_advanced_cloning():
    """Demonstrate advanced cloning scenarios."""
    print("\n=== Advanced Cloning Example ===")
    
    # Create a complex document with nested data
    original_report = ReportDocument()
    original_report.metadata.title = "Master Report Template"
    original_report.metadata.tags.extend(["master", "template", "complex"])
    original_report.content.add_table({"name": "Sales Data", "rows": 100, "columns": 5})
    original_report.content.add_image("chart1.png")
    
    print(f"Original: {original_report}")
    print(f"Original tags: {original_report.metadata.tags}")
    print(f"Original tables: {len(original_report.content.tables)}")
    
    # Clone and modify
    cloned_report = original_report.clone()
    cloned_report.metadata.title = "Q1 Sales Report"
    cloned_report.metadata.tags.append("q1")
    cloned_report.content.add_table({"name": "Q1 Specific Data", "rows": 50, "columns": 3})
    
    print(f"\nCloned: {cloned_report}")
    print(f"Cloned tags: {cloned_report.metadata.tags}")
    print(f"Cloned tables: {len(cloned_report.content.tables)}")
    
    # Verify independence
    print(f"\nOriginal after clone modification:")
    print(f"Original tags: {original_report.metadata.tags}")
    print(f"Original tables: {len(original_report.content.tables)}")
    print("Notice: Original remains unchanged (deep cloning works!)")

def main():
    """Main demonstration function."""
    print("PROTOTYPE PATTERN DEMONSTRATION")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_cloning_differences()
    measure_performance()
    demonstrate_basic_usage()
    demonstrate_custom_prototypes()
    demonstrate_advanced_cloning()
    
    print("\n" + "=" * 50)
    print("PROTOTYPE PATTERN BENEFITS:")
    print("1. Performance: Faster than creating objects from scratch")
    print("2. Flexibility: Easy to create variations of complex objects")
    print("3. Encapsulation: Creation logic is encapsulated in prototypes")
    print("4. Runtime Configuration: Can register new prototypes at runtime")
    print("5. Reduced Subclassing: Avoid creating many subclasses for variations")

if __name__ == "__main__":
    main()

