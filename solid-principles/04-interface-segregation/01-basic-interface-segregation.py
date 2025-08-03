"""Question: Define an interface Printer with methods print_document and scan_document.
Create classes BasicPrinter and AllInOnePrinter that implement the interface.
Refactor the interface to adhere to the Interface Segregation Principle.
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
# - What is the Interface Segregation Principle (ISP)?
# - How does the original Printer interface violate ISP?
# - What happens when BasicPrinter is forced to implement scan_document()?
# - How can you create smaller, more focused interfaces?
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


# Step 1: Identify the ISP violation in the original design
# ===============================================================================

# Explanation:
# Let's examine the original Printer interface that violates ISP by forcing
# all printers to implement both printing and scanning functionality.

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

class BasicPrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"

    def scan_document(self, document):
        raise NotImplementedError("BasicPrinter cannot scan documents")

class AllInOnePrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"

    def scan_document(self, document):
        return f"Scanning: {document}"

# What we can observe:
# - The Printer interface forces ALL printers to implement both print and scan
# - AllInOnePrinter can implement both methods naturally
# - BasicPrinter violates ISP by being forced to implement scan_document()
# - Clients depending on Printer interface may get unexpected exceptions

print("=== Original Design (ISP Violation) ===")
printers = [BasicPrinter(), AllInOnePrinter()]

print("Testing all printer functionalities:")
for i, printer in enumerate(printers, 1):
    printer_type = printer.__class__.__name__
    print(f"\nPrinter {i} ({printer_type}):")
    print(f"  Print: {printer.print_document('Document.pdf')}")
    
    try:
        print(f"  Scan: {printer.scan_document('Document.pdf')}")
    except Exception as e:
        print(f"  Scan: ERROR - {e}")

print("\nISP Violation: BasicPrinter is forced to implement scan_document() it cannot use!")


# Step 2: Design focused interfaces following ISP
# ===============================================================================

# Explanation:
# Let's create smaller, more focused interfaces that follow ISP by
# separating printing and scanning concerns.

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

# What we accomplished in this step:
# - Created two focused interfaces, each with a single responsibility
# - Printable: for devices that can print documents
# - Scannable: for devices that can scan documents
# - Each interface is cohesive and focused


# Step 3: Implement BasicPrinter with only printing capability
# ===============================================================================

# Explanation:
# Now let's implement BasicPrinter by inheriting only from the Printable
# interface, since it can only print documents.

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class BasicPrinter(Printable):
    def print_document(self, document):
        return f"BasicPrinter printing: {document}"

# What we accomplished in this step:
# - BasicPrinter only implements Printable interface
# - No forced implementation of scan_document() method
# - Follows ISP: only implements methods it can actually use


# Step 4: Implement AllInOnePrinter with both capabilities
# ===============================================================================

# Explanation:
# Let's implement AllInOnePrinter by inheriting from both interfaces,
# since it can both print and scan documents.

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class BasicPrinter(Printable):
    def print_document(self, document):
        return f"BasicPrinter printing: {document}"

class AllInOnePrinter(Printable, Scannable):
    def print_document(self, document):
        return f"AllInOnePrinter printing: {document}"

    def scan_document(self, document):
        return f"AllInOnePrinter scanning: {document}"

# What we accomplished in this step:
# - AllInOnePrinter implements both Printable and Scannable interfaces
# - Each method has a clear purpose and implementation
# - Follows ISP: implements all interfaces it can actually use


# Step 5: Test our ISP-compliant design
# ===============================================================================

# Explanation:
# Let's test our redesigned interfaces to verify that they follow ISP
# and provide appropriate functionality for different client needs.

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class BasicPrinter(Printable):
    def print_document(self, document):
        return f"BasicPrinter printing: {document}"

class AllInOnePrinter(Printable, Scannable):
    def print_document(self, document):
        return f"AllInOnePrinter printing: {document}"

    def scan_document(self, document):
        return f"AllInOnePrinter scanning: {document}"

# Test our ISP-compliant design:
print("\n=== ISP-Compliant Design ===")

basic_printer = BasicPrinter()
all_in_one_printer = AllInOnePrinter()

# Test printing functionality (both can print)
printable_devices = [basic_printer, all_in_one_printer]
print("Testing Printable interface:")
for device in printable_devices:
    device_type = device.__class__.__name__
    print(f"  {device_type}: {device.print_document('Document.pdf')}")

# Test scanning functionality (only all-in-one can scan)
scannable_devices = [device for device in [basic_printer, all_in_one_printer] 
                    if isinstance(device, Scannable)]
print(f"\nTesting Scannable interface ({len(scannable_devices)} devices):")
for device in scannable_devices:
    device_type = device.__class__.__name__
    print(f"  {device_type}: {device.scan_document('Document.pdf')}")

print("\nISP Success: Each device only implements interfaces it can actually use!")

# What we accomplished in this step:
# - Verified that all devices can print through Printable interface
# - Demonstrated that only appropriate devices implement Scannable
# - Confirmed that no exceptions are thrown due to inappropriate method calls


# Step 6: Enhanced example with more device types and client code
# ===============================================================================

# Explanation:
# Let's create a more comprehensive example that shows how ISP enables
# flexible client code that depends only on the interfaces it needs.

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax_document(self, document, number):
        pass

class Copyable(ABC):
    @abstractmethod
    def copy_document(self, document, copies):
        pass

# Different types of office devices
class BasicPrinter(Printable):
    def __init__(self, model):
        self.model = model

    def print_document(self, document):
        return f"{self.model} printing: {document}"

class Scanner(Scannable):
    def __init__(self, model):
        self.model = model

    def scan_document(self, document):
        return f"{self.model} scanning: {document}"

class AllInOnePrinter(Printable, Scannable, Copyable):
    def __init__(self, model):
        self.model = model

    def print_document(self, document):
        return f"{self.model} printing: {document}"

    def scan_document(self, document):
        return f"{self.model} scanning: {document}"

    def copy_document(self, document, copies):
        return f"{self.model} copying {document} ({copies} copies)"

class OfficeCenter(Printable, Scannable, Faxable, Copyable):
    def __init__(self, model):
        self.model = model

    def print_document(self, document):
        return f"{self.model} printing: {document}"

    def scan_document(self, document):
        return f"{self.model} scanning: {document}"

    def fax_document(self, document, number):
        return f"{self.model} faxing {document} to {number}"

    def copy_document(self, document, copies):
        return f"{self.model} copying {document} ({copies} copies)"

# Client code that depends only on specific interfaces
class PrintManager:
    def __init__(self):
        self.printers = []

    def add_printer(self, printer):
        if isinstance(printer, Printable):
            self.printers.append(printer)
        else:
            raise TypeError("Device must implement Printable interface")

    def print_documents(self, documents):
        """Client code that only depends on Printable interface"""
        results = []
        for printer in self.printers:
            for document in documents:
                result = printer.print_document(document)
                results.append(result)
        return results

class ScanManager:
    def scan_documents(self, devices, documents):
        """Client code that only depends on Scannable interface"""
        results = []
        scannable_devices = [d for d in devices if isinstance(d, Scannable)]
        
        if not scannable_devices:
            return ["No scannable devices available"]
        
        for device in scannable_devices:
            for document in documents:
                result = device.scan_document(document)
                results.append(result)
        return results

class CopyManager:
    def copy_documents(self, devices, documents, copies=1):
        """Client code that only depends on Copyable interface"""
        results = []
        copyable_devices = [d for d in devices if isinstance(d, Copyable)]
        
        if not copyable_devices:
            return ["No copyable devices available"]
        
        for device in copyable_devices:
            for document in documents:
                result = device.copy_document(document, copies)
                results.append(result)
        return results

class FaxManager:
    def fax_documents(self, devices, documents, fax_number):
        """Client code that only depends on Faxable interface"""
        results = []
        faxable_devices = [d for d in devices if isinstance(d, Faxable)]
        
        if not faxable_devices:
            return ["No fax-capable devices available"]
        
        for device in faxable_devices:
            for document in documents:
                result = device.fax_document(document, fax_number)
                results.append(result)
        return results

# Test enhanced ISP design:
print("\n=== Enhanced ISP Design with Multiple Device Types ===")

# Create different types of devices
devices = [
    BasicPrinter("HP LaserJet"),
    Scanner("Canon Scanner"),
    AllInOnePrinter("Epson WorkForce"),
    OfficeCenter("Xerox WorkCentre")
]

# Create managers
print_manager = PrintManager()
scan_manager = ScanManager()
copy_manager = CopyManager()
fax_manager = FaxManager()

# Add printable devices to print manager
for device in devices:
    if isinstance(device, Printable):
        print_manager.add_printer(device)

documents = ["Report.pdf", "Invoice.docx"]

print("Print operations:")
print_results = print_manager.print_documents(documents)
for result in print_results:
    print(f"  {result}")

print("\nScan operations:")
scan_results = scan_manager.scan_documents(devices, documents)
for result in scan_results:
    print(f"  {result}")

print("\nCopy operations:")
copy_results = copy_manager.copy_documents(devices, documents, copies=3)
for result in copy_results:
    print(f"  {result}")

print("\nFax operations:")
fax_results = fax_manager.fax_documents(devices, documents, "555-1234")
for result in fax_results:
    print(f"  {result}")

# Demonstrate interface segregation benefits
print(f"\n=== ISP Benefits Demonstrated ===")
print(f"- PrintManager only depends on Printable interface")
print(f"- ScanManager only depends on Scannable interface")
print(f"- CopyManager only depends on Copyable interface")
print(f"- FaxManager only depends on Faxable interface")
print(f"- Each client is isolated from changes in unrelated interfaces")
print(f"- No client is forced to depend on methods it doesn't use")

# What we accomplished in this step:
# - Created multiple device types with different capabilities
# - Demonstrated client code that depends only on specific interfaces
# - Showed how ISP enables flexible and maintainable system design
# - Illustrated that changes to one interface don't affect unrelated clients


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the Interface Segregation Principle solution!
#
# Key concepts learned:
# - Understanding the Interface Segregation Principle (ISP)
# - Identifying fat interfaces that violate ISP
# - Creating focused, cohesive interfaces with single responsibilities
# - Benefits of multiple inheritance with focused interfaces
# - How ISP enables flexible client code design
# - Avoiding forced implementation of inappropriate methods
#
# ISP Benefits demonstrated:
# - Clients depend only on interfaces they actually use
# - No forced implementation of methods that don't make sense
# - Changes to one interface don't affect unrelated clients
# - System is more flexible and maintainable
# - Easy to add new device types without breaking existing code
# - Clear separation of concerns and responsibilities
#
# Real-world applications:
# - Office equipment management systems
# - Plugin architectures with specific capability interfaces
# - Device driver systems with focused operation interfaces
# - GUI component libraries with role-specific interfaces
# - Database access layers with specialized query interfaces
# - Web service APIs with resource-specific endpoints
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY the original design violates ISP
# 4. Experiment with adding new device types (PhotoPrinter, NetworkScanner, etc.)
#
# Remember: The best way to learn is by doing!
# ===============================================================================
