"""Question: Implement the Factory Method pattern to create objects without specifying exact classes.

Create a document processing system where different document types (PDF, Word, Text)
can be created through a factory method without the client knowing the specific classes.

Requirements:
1. Create abstract Document and DocumentFactory classes
2. Implement concrete document types (PDF, Word, Text)
3. Implement concrete factory classes for each document type
4. Demonstrate creation of documents through factories
5. Show how new document types can be added easily

Example usage:
    pdf_factory = PDFDocumentFactory()
    pdf_doc = pdf_factory.create_document("report.pdf")
    pdf_doc.open()
"""

# LEARNING CHALLENGE
#
# Before looking at any solution below, please try to solve this yourself first!

# Try to implement your solution here:
# (Write your code below this line)


















































# HINT SECTION (Only look if you're really stuck!)
#
# Think about:
# - What is the product you're creating?
# - What abstract factory interface do you need?
# - How do concrete factories implement the interface?
# - What role does the creator play?
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


# Step 1: Import modules and create the abstract product class
# ===============================================================================

# Explanation:
# The Factory Method pattern starts with an abstract product that defines
# the interface for objects the factory method creates.

from abc import ABC, abstractmethod
from typing import Optional

class Document(ABC):
    """Abstract document class that defines the interface for all documents."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content: str = ""
        self.is_open: bool = False
    
    @abstractmethod
    def open(self):
        """Open the document."""
        pass
    
    @abstractmethod
    def save(self):
        """Save the document."""
        pass
    
    @abstractmethod
    def close(self):
        """Close the document."""
        pass
    
    @abstractmethod
    def get_file_info(self) -> str:
        """Get file information."""
        pass

# What we accomplished in this step:
# - Created abstract Document class with common interface
# - Defined abstract methods that all document types must implement


# Step 2: Create concrete document classes
# ===============================================================================

# Explanation:
# Concrete products implement the abstract product interface.
# Each document type has its own specific behavior.

from abc import ABC, abstractmethod
from typing import Optional

class Document(ABC):
    """Abstract document class that defines the interface for all documents."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content: str = ""
        self.is_open: bool = False
    
    @abstractmethod
    def open(self):
        """Open the document."""
        pass
    
    @abstractmethod
    def save(self):
        """Save the document."""
        pass
    
    @abstractmethod
    def close(self):
        """Close the document."""
        pass
    
    @abstractmethod
    def get_file_info(self) -> str:
        """Get file information."""
        pass

class PDFDocument(Document):
    """Concrete PDF document implementation."""
    
    def open(self):
        """Open PDF document."""
        if not self.is_open:
            print(f"Opening PDF document: {self.filename}")
            print("Loading PDF viewer...")
            self.is_open = True
            self.content = "PDF content loaded"
        else:
            print(f"PDF document {self.filename} is already open")
    
    def save(self):
        """Save PDF document."""
        if self.is_open:
            print(f"Saving PDF document: {self.filename}")
            print("Compressing PDF content...")
        else:
            print("Cannot save: PDF document is not open")
    
    def close(self):
        """Close PDF document."""
        if self.is_open:
            print(f"Closing PDF document: {self.filename}")
            print("Releasing PDF viewer resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"PDF document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get PDF file information."""
        return f"PDF Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class WordDocument(Document):
    """Concrete Word document implementation."""
    
    def open(self):
        """Open Word document."""
        if not self.is_open:
            print(f"Opening Word document: {self.filename}")
            print("Loading Microsoft Word...")
            self.is_open = True
            self.content = "Word content loaded"
        else:
            print(f"Word document {self.filename} is already open")
    
    def save(self):
        """Save Word document."""
        if self.is_open:
            print(f"Saving Word document: {self.filename}")
            print("Applying Word formatting...")
        else:
            print("Cannot save: Word document is not open")
    
    def close(self):
        """Close Word document."""
        if self.is_open:
            print(f"Closing Word document: {self.filename}")
            print("Releasing Word application resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Word document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get Word file information."""
        return f"Word Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class TextDocument(Document):
    """Concrete text document implementation."""
    
    def open(self):
        """Open text document."""
        if not self.is_open:
            print(f"Opening text document: {self.filename}")
            print("Loading text editor...")
            self.is_open = True
            self.content = "Text content loaded"
        else:
            print(f"Text document {self.filename} is already open")
    
    def save(self):
        """Save text document."""
        if self.is_open:
            print(f"Saving text document: {self.filename}")
            print("Writing plain text...")
        else:
            print("Cannot save: Text document is not open")
    
    def close(self):
        """Close text document."""
        if self.is_open:
            print(f"Closing text document: {self.filename}")
            print("Releasing text editor resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Text document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get text file information."""
        return f"Text Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

# What we accomplished in this step:
# - Created concrete document classes for PDF, Word, and Text
# - Each class implements the abstract interface with specific behavior
# - Added realistic document operations and status tracking


# Step 3: Create the abstract factory class
# ===============================================================================

# Explanation:
# The abstract factory defines the factory method interface.
# This is the core of the Factory Method pattern.

from abc import ABC, abstractmethod
from typing import Optional

class Document(ABC):
    """Abstract document class that defines the interface for all documents."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content: str = ""
        self.is_open: bool = False
    
    @abstractmethod
    def open(self):
        """Open the document."""
        pass
    
    @abstractmethod
    def save(self):
        """Save the document."""
        pass
    
    @abstractmethod
    def close(self):
        """Close the document."""
        pass
    
    @abstractmethod
    def get_file_info(self) -> str:
        """Get file information."""
        pass

class PDFDocument(Document):
    """Concrete PDF document implementation."""
    
    def open(self):
        """Open PDF document."""
        if not self.is_open:
            print(f"Opening PDF document: {self.filename}")
            print("Loading PDF viewer...")
            self.is_open = True
            self.content = "PDF content loaded"
        else:
            print(f"PDF document {self.filename} is already open")
    
    def save(self):
        """Save PDF document."""
        if self.is_open:
            print(f"Saving PDF document: {self.filename}")
            print("Compressing PDF content...")
        else:
            print("Cannot save: PDF document is not open")
    
    def close(self):
        """Close PDF document."""
        if self.is_open:
            print(f"Closing PDF document: {self.filename}")
            print("Releasing PDF viewer resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"PDF document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get PDF file information."""
        return f"PDF Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class WordDocument(Document):
    """Concrete Word document implementation."""
    
    def open(self):
        """Open Word document."""
        if not self.is_open:
            print(f"Opening Word document: {self.filename}")
            print("Loading Microsoft Word...")
            self.is_open = True
            self.content = "Word content loaded"
        else:
            print(f"Word document {self.filename} is already open")
    
    def save(self):
        """Save Word document."""
        if self.is_open:
            print(f"Saving Word document: {self.filename}")
            print("Applying Word formatting...")
        else:
            print("Cannot save: Word document is not open")
    
    def close(self):
        """Close Word document."""
        if self.is_open:
            print(f"Closing Word document: {self.filename}")
            print("Releasing Word application resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Word document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get Word file information."""
        return f"Word Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class TextDocument(Document):
    """Concrete text document implementation."""
    
    def open(self):
        """Open text document."""
        if not self.is_open:
            print(f"Opening text document: {self.filename}")
            print("Loading text editor...")
            self.is_open = True
            self.content = "Text content loaded"
        else:
            print(f"Text document {self.filename} is already open")
    
    def save(self):
        """Save text document."""
        if self.is_open:
            print(f"Saving text document: {self.filename}")
            print("Writing plain text...")
        else:
            print("Cannot save: Text document is not open")
    
    def close(self):
        """Close text document."""
        if self.is_open:
            print(f"Closing text document: {self.filename}")
            print("Releasing text editor resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Text document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get text file information."""
        return f"Text Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class DocumentFactory(ABC):
    """Abstract factory for creating documents."""
    
    @abstractmethod
    def create_document(self, filename: str) -> Document:
        """Factory method to create a document."""
        pass
    
    def process_document(self, filename: str) -> Document:
        """Template method that uses the factory method."""
        print(f"Processing document creation for: {filename}")
        
        # Create document using factory method
        document = self.create_document(filename)
        
        # Common processing steps
        print(f"Document created: {document.get_file_info()}")
        
        return document

# What we accomplished in this step:
# - Created abstract DocumentFactory with factory method
# - Added template method that uses the factory method
# - Defined the interface that concrete factories must implement


# Step 4: Create concrete factory classes
# ===============================================================================

# Explanation:
# Concrete factories implement the factory method to create specific document types.
# Each factory knows how to create one type of document.

from abc import ABC, abstractmethod
from typing import Optional

class Document(ABC):
    """Abstract document class that defines the interface for all documents."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content: str = ""
        self.is_open: bool = False
    
    @abstractmethod
    def open(self):
        """Open the document."""
        pass
    
    @abstractmethod
    def save(self):
        """Save the document."""
        pass
    
    @abstractmethod
    def close(self):
        """Close the document."""
        pass
    
    @abstractmethod
    def get_file_info(self) -> str:
        """Get file information."""
        pass

class PDFDocument(Document):
    """Concrete PDF document implementation."""
    
    def open(self):
        """Open PDF document."""
        if not self.is_open:
            print(f"Opening PDF document: {self.filename}")
            print("Loading PDF viewer...")
            self.is_open = True
            self.content = "PDF content loaded"
        else:
            print(f"PDF document {self.filename} is already open")
    
    def save(self):
        """Save PDF document."""
        if self.is_open:
            print(f"Saving PDF document: {self.filename}")
            print("Compressing PDF content...")
        else:
            print("Cannot save: PDF document is not open")
    
    def close(self):
        """Close PDF document."""
        if self.is_open:
            print(f"Closing PDF document: {self.filename}")
            print("Releasing PDF viewer resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"PDF document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get PDF file information."""
        return f"PDF Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class WordDocument(Document):
    """Concrete Word document implementation."""
    
    def open(self):
        """Open Word document."""
        if not self.is_open:
            print(f"Opening Word document: {self.filename}")
            print("Loading Microsoft Word...")
            self.is_open = True
            self.content = "Word content loaded"
        else:
            print(f"Word document {self.filename} is already open")
    
    def save(self):
        """Save Word document."""
        if self.is_open:
            print(f"Saving Word document: {self.filename}")
            print("Applying Word formatting...")
        else:
            print("Cannot save: Word document is not open")
    
    def close(self):
        """Close Word document."""
        if self.is_open:
            print(f"Closing Word document: {self.filename}")
            print("Releasing Word application resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Word document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get Word file information."""
        return f"Word Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class TextDocument(Document):
    """Concrete text document implementation."""
    
    def open(self):
        """Open text document."""
        if not self.is_open:
            print(f"Opening text document: {self.filename}")
            print("Loading text editor...")
            self.is_open = True
            self.content = "Text content loaded"
        else:
            print(f"Text document {self.filename} is already open")
    
    def save(self):
        """Save text document."""
        if self.is_open:
            print(f"Saving text document: {self.filename}")
            print("Writing plain text...")
        else:
            print("Cannot save: Text document is not open")
    
    def close(self):
        """Close text document."""
        if self.is_open:
            print(f"Closing text document: {self.filename}")
            print("Releasing text editor resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Text document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get text file information."""
        return f"Text Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class DocumentFactory(ABC):
    """Abstract factory for creating documents."""
    
    @abstractmethod
    def create_document(self, filename: str) -> Document:
        """Factory method to create a document."""
        pass
    
    def process_document(self, filename: str) -> Document:
        """Template method that uses the factory method."""
        print(f"Processing document creation for: {filename}")
        
        # Create document using factory method
        document = self.create_document(filename)
        
        # Common processing steps
        print(f"Document created: {document.get_file_info()}")
        
        return document

class PDFDocumentFactory(DocumentFactory):
    """Concrete factory for creating PDF documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a PDF document."""
        print("Initializing PDF document factory...")
        print("Setting up PDF-specific configurations...")
        return PDFDocument(filename)

class WordDocumentFactory(DocumentFactory):
    """Concrete factory for creating Word documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a Word document."""
        print("Initializing Word document factory...")
        print("Setting up Microsoft Word configurations...")
        return WordDocument(filename)

class TextDocumentFactory(DocumentFactory):
    """Concrete factory for creating text documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a text document."""
        print("Initializing text document factory...")
        print("Setting up plain text configurations...")
        return TextDocument(filename)

# What we accomplished in this step:
# - Created concrete factories for each document type
# - Each factory implements the factory method with specific logic
# - Added factory-specific initialization and configuration


# Step 5: Demonstrate the Factory Method pattern
# ===============================================================================

# Explanation:
# Let's test our Factory Method pattern implementation with different document types.

from abc import ABC, abstractmethod
from typing import Optional

class Document(ABC):
    """Abstract document class that defines the interface for all documents."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content: str = ""
        self.is_open: bool = False
    
    @abstractmethod
    def open(self):
        """Open the document."""
        pass
    
    @abstractmethod
    def save(self):
        """Save the document."""
        pass
    
    @abstractmethod
    def close(self):
        """Close the document."""
        pass
    
    @abstractmethod
    def get_file_info(self) -> str:
        """Get file information."""
        pass

class PDFDocument(Document):
    """Concrete PDF document implementation."""
    
    def open(self):
        """Open PDF document."""
        if not self.is_open:
            print(f"Opening PDF document: {self.filename}")
            print("Loading PDF viewer...")
            self.is_open = True
            self.content = "PDF content loaded"
        else:
            print(f"PDF document {self.filename} is already open")
    
    def save(self):
        """Save PDF document."""
        if self.is_open:
            print(f"Saving PDF document: {self.filename}")
            print("Compressing PDF content...")
        else:
            print("Cannot save: PDF document is not open")
    
    def close(self):
        """Close PDF document."""
        if self.is_open:
            print(f"Closing PDF document: {self.filename}")
            print("Releasing PDF viewer resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"PDF document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get PDF file information."""
        return f"PDF Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class WordDocument(Document):
    """Concrete Word document implementation."""
    
    def open(self):
        """Open Word document."""
        if not self.is_open:
            print(f"Opening Word document: {self.filename}")
            print("Loading Microsoft Word...")
            self.is_open = True
            self.content = "Word content loaded"
        else:
            print(f"Word document {self.filename} is already open")
    
    def save(self):
        """Save Word document."""
        if self.is_open:
            print(f"Saving Word document: {self.filename}")
            print("Applying Word formatting...")
        else:
            print("Cannot save: Word document is not open")
    
    def close(self):
        """Close Word document."""
        if self.is_open:
            print(f"Closing Word document: {self.filename}")
            print("Releasing Word application resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Word document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get Word file information."""
        return f"Word Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class TextDocument(Document):
    """Concrete text document implementation."""
    
    def open(self):
        """Open text document."""
        if not self.is_open:
            print(f"Opening text document: {self.filename}")
            print("Loading text editor...")
            self.is_open = True
            self.content = "Text content loaded"
        else:
            print(f"Text document {self.filename} is already open")
    
    def save(self):
        """Save text document."""
        if self.is_open:
            print(f"Saving text document: {self.filename}")
            print("Writing plain text...")
        else:
            print("Cannot save: Text document is not open")
    
    def close(self):
        """Close text document."""
        if self.is_open:
            print(f"Closing text document: {self.filename}")
            print("Releasing text editor resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Text document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get text file information."""
        return f"Text Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class DocumentFactory(ABC):
    """Abstract factory for creating documents."""
    
    @abstractmethod
    def create_document(self, filename: str) -> Document:
        """Factory method to create a document."""
        pass
    
    def process_document(self, filename: str) -> Document:
        """Template method that uses the factory method."""
        print(f"Processing document creation for: {filename}")
        
        # Create document using factory method
        document = self.create_document(filename)
        
        # Common processing steps
        print(f"Document created: {document.get_file_info()}")
        
        return document

class PDFDocumentFactory(DocumentFactory):
    """Concrete factory for creating PDF documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a PDF document."""
        print("Initializing PDF document factory...")
        print("Setting up PDF-specific configurations...")
        return PDFDocument(filename)

class WordDocumentFactory(DocumentFactory):
    """Concrete factory for creating Word documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a Word document."""
        print("Initializing Word document factory...")
        print("Setting up Microsoft Word configurations...")
        return WordDocument(filename)

class TextDocumentFactory(DocumentFactory):
    """Concrete factory for creating text documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a text document."""
        print("Initializing text document factory...")
        print("Setting up plain text configurations...")
        return TextDocument(filename)

print("=== Testing Factory Method Pattern ===\n")

# Test 1: Create PDF document
print("1. Creating PDF Document:")
pdf_factory = PDFDocumentFactory()
pdf_doc = pdf_factory.process_document("report.pdf")
pdf_doc.open()
pdf_doc.save()
pdf_doc.close()
print()

# Test 2: Create Word document
print("2. Creating Word Document:")
word_factory = WordDocumentFactory()
word_doc = word_factory.process_document("letter.docx")
word_doc.open()
word_doc.save()
word_doc.close()
print()

# Test 3: Create Text document
print("3. Creating Text Document:")
text_factory = TextDocumentFactory()
text_doc = text_factory.process_document("notes.txt")
text_doc.open()
text_doc.save()
text_doc.close()
print()

# What we accomplished in this step:
# - Demonstrated the Factory Method pattern in action
# - Showed how different factories create different document types
# - Tested the complete document lifecycle (create, open, save, close)


# Step 6: Demonstrate extensibility - Adding new document types
# ===============================================================================

# Explanation:
# One of the key benefits of the Factory Method pattern is easy extensibility.
# Let's add a new document type without modifying existing code.

from abc import ABC, abstractmethod
from typing import Optional

class Document(ABC):
    """Abstract document class that defines the interface for all documents."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.content: str = ""
        self.is_open: bool = False
    
    @abstractmethod
    def open(self):
        """Open the document."""
        pass
    
    @abstractmethod
    def save(self):
        """Save the document."""
        pass
    
    @abstractmethod
    def close(self):
        """Close the document."""
        pass
    
    @abstractmethod
    def get_file_info(self) -> str:
        """Get file information."""
        pass

class PDFDocument(Document):
    """Concrete PDF document implementation."""
    
    def open(self):
        """Open PDF document."""
        if not self.is_open:
            print(f"Opening PDF document: {self.filename}")
            print("Loading PDF viewer...")
            self.is_open = True
            self.content = "PDF content loaded"
        else:
            print(f"PDF document {self.filename} is already open")
    
    def save(self):
        """Save PDF document."""
        if self.is_open:
            print(f"Saving PDF document: {self.filename}")
            print("Compressing PDF content...")
        else:
            print("Cannot save: PDF document is not open")
    
    def close(self):
        """Close PDF document."""
        if self.is_open:
            print(f"Closing PDF document: {self.filename}")
            print("Releasing PDF viewer resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"PDF document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get PDF file information."""
        return f"PDF Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class WordDocument(Document):
    """Concrete Word document implementation."""
    
    def open(self):
        """Open Word document."""
        if not self.is_open:
            print(f"Opening Word document: {self.filename}")
            print("Loading Microsoft Word...")
            self.is_open = True
            self.content = "Word content loaded"
        else:
            print(f"Word document {self.filename} is already open")
    
    def save(self):
        """Save Word document."""
        if self.is_open:
            print(f"Saving Word document: {self.filename}")
            print("Applying Word formatting...")
        else:
            print("Cannot save: Word document is not open")
    
    def close(self):
        """Close Word document."""
        if self.is_open:
            print(f"Closing Word document: {self.filename}")
            print("Releasing Word application resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Word document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get Word file information."""
        return f"Word Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class TextDocument(Document):
    """Concrete text document implementation."""
    
    def open(self):
        """Open text document."""
        if not self.is_open:
            print(f"Opening text document: {self.filename}")
            print("Loading text editor...")
            self.is_open = True
            self.content = "Text content loaded"
        else:
            print(f"Text document {self.filename} is already open")
    
    def save(self):
        """Save text document."""
        if self.is_open:
            print(f"Saving text document: {self.filename}")
            print("Writing plain text...")
        else:
            print("Cannot save: Text document is not open")
    
    def close(self):
        """Close text document."""
        if self.is_open:
            print(f"Closing text document: {self.filename}")
            print("Releasing text editor resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Text document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get text file information."""
        return f"Text Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

# NEW: Adding Excel document type without modifying existing code
class ExcelDocument(Document):
    """Concrete Excel document implementation."""
    
    def open(self):
        """Open Excel document."""
        if not self.is_open:
            print(f"Opening Excel document: {self.filename}")
            print("Loading Microsoft Excel...")
            print("Initializing spreadsheet engine...")
            self.is_open = True
            self.content = "Excel spreadsheet loaded"
        else:
            print(f"Excel document {self.filename} is already open")
    
    def save(self):
        """Save Excel document."""
        if self.is_open:
            print(f"Saving Excel document: {self.filename}")
            print("Calculating formulas...")
            print("Compressing spreadsheet data...")
        else:
            print("Cannot save: Excel document is not open")
    
    def close(self):
        """Close Excel document."""
        if self.is_open:
            print(f"Closing Excel document: {self.filename}")
            print("Releasing Excel application resources...")
            self.is_open = False
            self.content = ""
        else:
            print(f"Excel document {self.filename} is already closed")
    
    def get_file_info(self) -> str:
        """Get Excel file information."""
        return f"Excel Document: {self.filename} (Status: {'Open' if self.is_open else 'Closed'})"

class DocumentFactory(ABC):
    """Abstract factory for creating documents."""
    
    @abstractmethod
    def create_document(self, filename: str) -> Document:
        """Factory method to create a document."""
        pass
    
    def process_document(self, filename: str) -> Document:
        """Template method that uses the factory method."""
        print(f"Processing document creation for: {filename}")
        
        # Create document using factory method
        document = self.create_document(filename)
        
        # Common processing steps
        print(f"Document created: {document.get_file_info()}")
        
        return document

class PDFDocumentFactory(DocumentFactory):
    """Concrete factory for creating PDF documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a PDF document."""
        print("Initializing PDF document factory...")
        print("Setting up PDF-specific configurations...")
        return PDFDocument(filename)

class WordDocumentFactory(DocumentFactory):
    """Concrete factory for creating Word documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a Word document."""
        print("Initializing Word document factory...")
        print("Setting up Microsoft Word configurations...")
        return WordDocument(filename)

class TextDocumentFactory(DocumentFactory):
    """Concrete factory for creating text documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create a text document."""
        print("Initializing text document factory...")
        print("Setting up plain text configurations...")
        return TextDocument(filename)

# NEW: Adding Excel factory without modifying existing code
class ExcelDocumentFactory(DocumentFactory):
    """Concrete factory for creating Excel documents."""
    
    def create_document(self, filename: str) -> Document:
        """Create an Excel document."""
        print("Initializing Excel document factory...")
        print("Setting up Microsoft Excel configurations...")
        print("Loading spreadsheet templates...")
        return ExcelDocument(filename)

print("=== Testing Factory Method Pattern ===\n")

# Test 1: Create PDF document
print("1. Creating PDF Document:")
pdf_factory = PDFDocumentFactory()
pdf_doc = pdf_factory.process_document("report.pdf")
pdf_doc.open()
pdf_doc.save()
pdf_doc.close()
print()

# Test 2: Create Word document
print("2. Creating Word Document:")
word_factory = WordDocumentFactory()
word_doc = word_factory.process_document("letter.docx")
word_doc.open()
word_doc.save()
word_doc.close()
print()

# Test 3: Create Text document
print("3. Creating Text Document:")
text_factory = TextDocumentFactory()
text_doc = text_factory.process_document("notes.txt")
text_doc.open()
text_doc.save()
text_doc.close()
print()

# Test 4: Create Excel document (NEW)
print("4. Creating Excel Document:")
excel_factory = ExcelDocumentFactory()
excel_doc = excel_factory.process_document("budget.xlsx")
excel_doc.open()
excel_doc.save()
excel_doc.close()
print()

# Demonstrate polymorphism with factory method
print("5. Demonstrating Polymorphism:")
factories = [
    PDFDocumentFactory(),
    WordDocumentFactory(),
    TextDocumentFactory(),
    ExcelDocumentFactory()
]

filenames = ["report.pdf", "memo.docx", "readme.txt", "data.xlsx"]

for factory, filename in zip(factories, filenames):
    print(f"Using factory: {factory.__class__.__name__}")
    doc = factory.process_document(filename)
    print(f"Created: {doc.get_file_info()}")
    print()

# What we accomplished in this step:
# - Added new Excel document type without modifying existing code
# - Demonstrated the Open/Closed Principle (open for extension, closed for modification)
# - Showed polymorphism with different factories
# - Proved the extensibility of the Factory Method pattern


# ===============================================================================
# CONGRATULATIONS!
#
# You've successfully completed the step-by-step Factory Method pattern solution!
#
# Key concepts learned:
# - Factory Method pattern structure and purpose
# - Abstract product and concrete product implementations
# - Abstract factory and concrete factory implementations
# - Template method pattern integration
# - Extensibility without modifying existing code
# - Polymorphism and the Open/Closed Principle
#
# Benefits of Factory Method pattern:
# 1. Decouples object creation from object usage
# 2. Makes code more flexible and extensible
# 3. Follows the Open/Closed Principle
# 4. Enables polymorphic object creation
# 5. Centralizes object creation logic
#
# Try it yourself:
# 1. Start with Step 1 and code along
# 2. Test each step before moving to the next
# 3. Understand WHY each step is necessary
# 4. Experiment with modifications (try adding PowerPoint documents!)
#
# Remember: The best way to learn is by doing!
# ===============================================================================

