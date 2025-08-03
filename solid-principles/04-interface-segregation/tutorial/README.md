# Interface Segregation Principle (ISP) - Complete Tutorial

## Table of Contents
1. [Introduction](#introduction)
2. [What is the Interface Segregation Principle?](#what-is-the-interface-segregation-principle)
3. [Why ISP Matters](#why-isp-matters)
4. [Beginner Level: Understanding the Basics](#beginner-level-understanding-the-basics)
5. [Intermediate Level: Practical Applications](#intermediate-level-practical-applications)
6. [Advanced Level: Complex Systems](#advanced-level-complex-systems)
7. [Expert Level: Design Patterns and Architecture](#expert-level-design-patterns-and-architecture)
8. [Common Pitfalls and How to Avoid Them](#common-pitfalls-and-how-to-avoid-them)
9. [Best Practices](#best-practices)
10. [Real-World Examples](#real-world-examples)
11. [Testing ISP-Compliant Code](#testing-isp-compliant-code)
12. [Conclusion](#conclusion)

---

## Introduction

Welcome to the comprehensive tutorial on the Interface Segregation Principle (ISP), the fourth principle of SOLID design principles. This tutorial is designed to take you from a complete beginner to an expert level understanding of ISP, with practical examples and real-world applications.

### Who This Tutorial Is For
- **Beginners**: New to programming or SOLID principles
- **Intermediate**: Familiar with basic OOP concepts
- **Advanced**: Experienced developers looking to deepen their understanding
- **Experts**: Architects and senior developers seeking advanced patterns

### Prerequisites
- Basic understanding of Python
- Familiarity with classes and objects
- Basic knowledge of inheritance (helpful but not required)

---

## What is the Interface Segregation Principle?

> **"Clients should not be forced to depend upon interfaces that they do not use."**
> 
> *- Robert C. Martin*

The Interface Segregation Principle states that:

1. **No client should be forced to depend on methods it does not use**
2. **Interfaces should be small and focused**
3. **It's better to have many specific interfaces than one general-purpose interface**
4. **Classes should only implement interfaces they can fully support**

### Key Concepts

- **Interface**: A contract that defines what methods a class must implement
- **Client**: Code that uses an interface or class
- **Segregation**: Separating concerns into focused, specific interfaces
- **Dependency**: When one piece of code relies on another

---

## Why ISP Matters

### Problems ISP Solves

1. **Fat Interfaces**: Large interfaces with many unrelated methods
2. **Forced Implementation**: Classes implementing methods they can't use
3. **Tight Coupling**: Changes in one part affecting unrelated parts
4. **Violation of Single Responsibility**: Interfaces doing too many things

### Benefits of Following ISP

1. **Flexibility**: Easy to add new implementations
2. **Maintainability**: Changes don't ripple through unrelated code
3. **Testability**: Easier to mock and test specific behaviors
4. **Clarity**: Clear separation of concerns
5. **Reusability**: Focused interfaces can be reused in different contexts

---

## Beginner Level: Understanding the Basics

### 🎯 Learning Objectives
By the end of this section, you will:
- Understand what makes an interface "fat" or bloated
- Recognize ISP violations in simple code
- Know how to split interfaces appropriately
- Write your first ISP-compliant code

### Example 1: The Classic Printer Problem

Let's start with a simple example that every beginner can understand.

#### ❌ Bad Example (ISP Violation)

```python
from abc import ABC, abstractmethod

# This is a "fat" interface - it tries to do too much
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass
    
    @abstractmethod
    def scan_document(self, document):
        pass
    
    @abstractmethod
    def fax_document(self, document, number):
        pass

# This class can do everything - no problem here
class AllInOnePrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"
    
    def scan_document(self, document):
        return f"Scanning: {document}"
    
    def fax_document(self, document, number):
        return f"Faxing {document} to {number}"

# This class has a problem - it's forced to implement methods it can't use!
class BasicPrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"
    
    def scan_document(self, document):
        # This is bad! We're forced to implement something we can't do
        raise NotImplementedError("This printer cannot scan!")
    
    def fax_document(self, document, number):
        # This is bad! We're forced to implement something we can't do
        raise NotImplementedError("This printer cannot fax!")
```

**What's wrong here?**
- BasicPrinter is forced to implement methods it can't use
- Clients using the Printer interface might get unexpected exceptions
- The interface is doing too many things (printing, scanning, faxing)

#### ✅ Good Example (ISP Compliant)

```python
from abc import ABC, abstractmethod

# Split the fat interface into focused, specific interfaces
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

# Now each class only implements what it can actually do
class BasicPrinter(Printable):
    def print_document(self, document):
        return f"Basic printer printing: {document}"

class AllInOnePrinter(Printable, Scannable, Faxable):
    def print_document(self, document):
        return f"All-in-one printing: {document}"
    
    def scan_document(self, document):
        return f"All-in-one scanning: {document}"
    
    def fax_document(self, document, number):
        return f"All-in-one faxing {document} to {number}"

# Client code that only needs printing
def print_documents(printer: Printable, documents):
    results = []
    for doc in documents:
        results.append(printer.print_document(doc))
    return results

# Client code that only needs scanning
def scan_documents(scanner: Scannable, documents):
    results = []
    for doc in documents:
        results.append(scanner.scan_document(doc))
    return results
```

**What's better now?**
- Each class only implements methods it can actually use
- No forced implementation of inappropriate methods
- Client code depends only on the specific functionality it needs
- Easy to add new printer types without breaking existing code

### 🧪 Try It Yourself: Simple Exercise

Create interfaces and classes for different types of vehicles:

```python
# Your task: Create appropriate interfaces for these vehicle types
# - Car: can drive, has engine
# - Bicycle: can drive, no engine
# - Boat: can sail, has engine
# - Sailboat: can sail, no engine

# Hint: Think about what interfaces you need:
# - Drivable? Sailable? HasEngine?
```

### Key Takeaways for Beginners

1. **One Interface, One Purpose**: Each interface should have a single, clear responsibility
2. **Implement Only What You Can**: Classes should only implement interfaces they can fully support
3. **Think About Clients**: Consider who will use your interfaces and what they actually need
4. **Start Small**: It's easier to combine small interfaces than to split large ones

---

## Intermediate Level: Practical Applications

### 🎯 Learning Objectives
By the end of this section, you will:
- Apply ISP to more complex scenarios
- Understand role-based interface design
- Learn about interface composition patterns
- Handle multiple client requirements effectively

### Example 2: Employee Management System

Let's look at a more complex example that demonstrates ISP in a business context.

#### ❌ Bad Example (Fat Interface)

```python
from abc import ABC, abstractmethod

# This interface tries to handle all employee operations
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def get_salary(self):
        pass
    
    @abstractmethod
    def manage_team(self):
        pass
    
    @abstractmethod
    def approve_expenses(self):
        pass
    
    @abstractmethod
    def conduct_interviews(self):
        pass
    
    @abstractmethod
    def access_confidential_data(self):
        pass

# Problems arise when implementing this interface
class Intern(Employee):
    def work(self):
        return "Intern working on assigned tasks"
    
    def get_salary(self):
        return "Intern receives stipend"
    
    def manage_team(self):
        # Interns don't manage teams!
        raise NotImplementedError("Interns cannot manage teams")
    
    def approve_expenses(self):
        # Interns can't approve expenses!
        raise NotImplementedError("Interns cannot approve expenses")
    
    def conduct_interviews(self):
        # Interns don't conduct interviews!
        raise NotImplementedError("Interns cannot conduct interviews")
    
    def access_confidential_data(self):
        # Interns shouldn't access confidential data!
        raise NotImplementedError("Interns cannot access confidential data")
```

#### ✅ Good Example (ISP Compliant)

```python
from abc import ABC, abstractmethod

# Split into role-based interfaces
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Payable(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class Manager(ABC):
    @abstractmethod
    def manage_team(self):
        pass

class ExpenseApprover(ABC):
    @abstractmethod
    def approve_expenses(self):
        pass

class Interviewer(ABC):
    @abstractmethod
    def conduct_interviews(self):
        pass

class ConfidentialDataAccess(ABC):
    @abstractmethod
    def access_confidential_data(self):
        pass

# Now each employee type implements only appropriate interfaces
class Intern(Worker, Payable):
    def __init__(self, name):
        self.name = name
    
    def work(self):
        return f"Intern {self.name} working on assigned tasks"
    
    def get_salary(self):
        return f"Intern {self.name} receives $1000 stipend"

class Developer(Worker, Payable):
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def work(self):
        return f"{self.level} Developer {self.name} writing code"
    
    def get_salary(self):
        salary_map = {"Junior": 60000, "Senior": 90000}
        return f"Developer {self.name} earns ${salary_map.get(self.level, 75000)}"

class TeamLead(Worker, Payable, Manager, Interviewer):
    def __init__(self, name):
        self.name = name
    
    def work(self):
        return f"Team Lead {self.name} coordinating development work"
    
    def get_salary(self):
        return f"Team Lead {self.name} earns $100000"
    
    def manage_team(self):
        return f"Team Lead {self.name} managing development team"
    
    def conduct_interviews(self):
        return f"Team Lead {self.name} interviewing candidates"

class Director(Worker, Payable, Manager, ExpenseApprover, Interviewer, ConfidentialDataAccess):
    def __init__(self, name):
        self.name = name
    
    def work(self):
        return f"Director {self.name} setting strategic direction"
    
    def get_salary(self):
        return f"Director {self.name} earns $150000"
    
    def manage_team(self):
        return f"Director {self.name} managing multiple teams"
    
    def approve_expenses(self):
        return f"Director {self.name} approving department expenses"
    
    def conduct_interviews(self):
        return f"Director {self.name} interviewing senior candidates"
    
    def access_confidential_data(self):
        return f"Director {self.name} accessing strategic data"

# Client code for different management needs
class PayrollSystem:
    def process_payroll(self, employees):
        """Only depends on Payable interface"""
        results = []
        for employee in employees:
            if isinstance(employee, Payable):
                results.append(employee.get_salary())
        return results

class ProjectManager:
    def assign_work(self, workers):
        """Only depends on Worker interface"""
        results = []
        for worker in workers:
            if isinstance(worker, Worker):
                results.append(worker.work())
        return results

class HRDepartment:
    def schedule_interviews(self, interviewers):
        """Only depends on Interviewer interface"""
        results = []
        for interviewer in interviewers:
            if isinstance(interviewer, Interviewer):
                results.append(interviewer.conduct_interviews())
        return results

# Example usage
employees = [
    Intern("Alice"),
    Developer("Bob", "Senior"),
    TeamLead("Carol"),
    Director("David")
]

payroll = PayrollSystem()
pm = ProjectManager()
hr = HRDepartment()

print("=== Payroll Processing ===")
for result in payroll.process_payroll(employees):
    print(f"  {result}")

print("\n=== Work Assignment ===")
for result in pm.assign_work(employees):
    print(f"  {result}")

print("\n=== Interview Scheduling ===")
for result in hr.schedule_interviews(employees):
    print(f"  {result}")
```

### Example 3: Media Player System

Let's explore another practical example with media handling.

#### The Problem
We need to build a media player system that can handle different types of media files and different types of players.

#### ✅ ISP Solution

```python
from abc import ABC, abstractmethod

# Focused interfaces for different media capabilities
class AudioPlayable(ABC):
    @abstractmethod
    def play_audio(self, audio_file):
        pass

class VideoPlayable(ABC):
    @abstractmethod
    def play_video(self, video_file):
        pass

class Recordable(ABC):
    @abstractmethod
    def record(self, duration):
        pass

class Streamable(ABC):
    @abstractmethod
    def stream(self, url):
        pass

class VolumeControllable(ABC):
    @abstractmethod
    def set_volume(self, level):
        pass

class PlaylistManageable(ABC):
    @abstractmethod
    def create_playlist(self, name):
        pass
    
    @abstractmethod
    def add_to_playlist(self, playlist, media):
        pass

# Different types of media players
class BasicAudioPlayer(AudioPlayable, VolumeControllable):
    def __init__(self):
        self.volume = 50
    
    def play_audio(self, audio_file):
        return f"Playing audio: {audio_file} at volume {self.volume}"
    
    def set_volume(self, level):
        self.volume = max(0, min(100, level))
        return f"Volume set to {self.volume}"

class SmartPhone(AudioPlayable, VideoPlayable, Recordable, VolumeControllable, PlaylistManageable):
    def __init__(self):
        self.volume = 70
        self.playlists = {}
    
    def play_audio(self, audio_file):
        return f"Smartphone playing audio: {audio_file}"
    
    def play_video(self, video_file):
        return f"Smartphone playing video: {video_file}"
    
    def record(self, duration):
        return f"Smartphone recording for {duration} seconds"
    
    def set_volume(self, level):
        self.volume = max(0, min(100, level))
        return f"Smartphone volume set to {self.volume}"
    
    def create_playlist(self, name):
        self.playlists[name] = []
        return f"Created playlist: {name}"
    
    def add_to_playlist(self, playlist, media):
        if playlist in self.playlists:
            self.playlists[playlist].append(media)
            return f"Added {media} to {playlist}"
        return f"Playlist {playlist} not found"

class StreamingDevice(AudioPlayable, VideoPlayable, Streamable, VolumeControllable):
    def __init__(self):
        self.volume = 80
    
    def play_audio(self, audio_file):
        return f"Streaming device playing audio: {audio_file}"
    
    def play_video(self, video_file):
        return f"Streaming device playing video: {video_file}"
    
    def stream(self, url):
        return f"Streaming from: {url}"
    
    def set_volume(self, level):
        self.volume = max(0, min(100, level))
        return f"Streaming device volume set to {self.volume}"

# Specialized client code
class AudioManager:
    def play_audio_files(self, players, files):
        """Only depends on AudioPlayable interface"""
        results = []
        for player in players:
            if isinstance(player, AudioPlayable):
                for file in files:
                    results.append(player.play_audio(file))
        return results

class VolumeController:
    def adjust_volume(self, devices, level):
        """Only depends on VolumeControllable interface"""
        results = []
        for device in devices:
            if isinstance(device, VolumeControllable):
                results.append(device.set_volume(level))
        return results

class PlaylistManager:
    def setup_playlists(self, devices):
        """Only depends on PlaylistManageable interface"""
        results = []
        for device in devices:
            if isinstance(device, PlaylistManageable):
                results.append(device.create_playlist("Favorites"))
                results.append(device.add_to_playlist("Favorites", "song1.mp3"))
        return results
```

### 🧪 Intermediate Exercise

Design an ISP-compliant system for a smart home:

```python
# Your task: Create interfaces for smart home devices
# Devices to consider:
# - Smart Light: can turn on/off, dim, change color
# - Smart Thermostat: can heat, cool, set temperature, schedule
# - Smart Speaker: can play music, respond to voice, control other devices
# - Smart Camera: can record, stream, detect motion, send alerts
# - Smart Lock: can lock/unlock, log access, send notifications

# Think about:
# 1. What interfaces do you need?
# 2. Which devices implement which interfaces?
# 3. What client code would use these interfaces?
```

### Key Takeaways for Intermediate Level

1. **Role-Based Design**: Think about the different roles or capabilities your objects need
2. **Client-Driven Interfaces**: Design interfaces based on what clients actually need
3. **Composition Over Inheritance**: Use multiple small interfaces rather than large hierarchies
4. **Interface Cohesion**: Keep related methods together, separate unrelated ones
5. **Flexibility Through Segregation**: Small interfaces make the system more flexible and extensible

---

## Advanced Level: Complex Systems

### 🎯 Learning Objectives
By the end of this section, you will:
- Design ISP-compliant architectures for complex systems
- Understand interface hierarchies and composition
- Learn advanced patterns like adapters and facades with ISP
- Handle cross-cutting concerns while maintaining ISP

### Example 4: Enterprise Document Management System

Let's build a sophisticated document management system that demonstrates advanced ISP concepts.

#### The Challenge
We need to build a system that handles various document types, processing workflows, security levels, and integration with external systems.

#### ✅ Advanced ISP Solution

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from enum import Enum

# Core document interfaces
class Readable(ABC):
    @abstractmethod
    def read_content(self) -> str:
        pass

class Writable(ABC):
    @abstractmethod
    def write_content(self, content: str) -> bool:
        pass

class Searchable(ABC):
    @abstractmethod
    def search(self, query: str) -> List[str]:
        pass

class Versionable(ABC):
    @abstractmethod
    def create_version(self) -> str:
        pass
    
    @abstractmethod
    def get_version_history(self) -> List[str]:
        pass

# Security interfaces
class Encryptable(ABC):
    @abstractmethod
    def encrypt(self, key: str) -> bool:
        pass
    
    @abstractmethod
    def decrypt(self, key: str) -> bool:
        pass

class AccessControlled(ABC):
    @abstractmethod
    def set_permissions(self, user: str, permissions: List[str]) -> bool:
        pass
    
    @abstractmethod
    def check_permission(self, user: str, action: str) -> bool:
        pass

class Auditable(ABC):
    @abstractmethod
    def log_access(self, user: str, action: str) -> None:
        pass
    
    @abstractmethod
    def get_audit_trail(self) -> List[Dict[str, Any]]:
        pass

# Processing interfaces
class Convertible(ABC):
    @abstractmethod
    def convert_to(self, format: str) -> 'Document':
        pass

class Compressible(ABC):
    @abstractmethod
    def compress(self) -> bool:
        pass
    
    @abstractmethod
    def decompress(self) -> bool:
        pass

class Signable(ABC):
    @abstractmethod
    def add_digital_signature(self, signature: str) -> bool:
        pass
    
    @abstractmethod
    def verify_signature(self) -> bool:
        pass

# Workflow interfaces
class Approvable(ABC):
    @abstractmethod
    def submit_for_approval(self, approver: str) -> bool:
        pass
    
    @abstractmethod
    def approve(self, approver: str) -> bool:
        pass
    
    @abstractmethod
    def reject(self, approver: str, reason: str) -> bool:
        pass

class Publishable(ABC):
    @abstractmethod
    def publish(self, channel: str) -> bool:
        pass
    
    @abstractmethod
    def unpublish(self) -> bool:
        pass

# Integration interfaces
class Syncable(ABC):
    @abstractmethod
    def sync_to_cloud(self, provider: str) -> bool:
        pass
    
    @abstractmethod
    def sync_from_cloud(self, provider: str) -> bool:
        pass

class Exportable(ABC):
    @abstractmethod
    def export_to_system(self, system: str, format: str) -> bool:
        pass

# Document implementations
class BasicDocument(Readable, Writable, Searchable):
    def __init__(self, title: str, content: str = ""):
        self.title = title
        self.content = content
    
    def read_content(self) -> str:
        return self.content
    
    def write_content(self, content: str) -> bool:
        self.content = content
        return True
    
    def search(self, query: str) -> List[str]:
        lines = self.content.split('\n')
        return [line for line in lines if query.lower() in line.lower()]

class SecureDocument(Readable, Writable, Searchable, Encryptable, AccessControlled, Auditable):
    def __init__(self, title: str, content: str = ""):
        self.title = title
        self.content = content
        self.encrypted = False
        self.permissions = {}
        self.audit_log = []
    
    def read_content(self) -> str:
        if self.encrypted:
            return "[ENCRYPTED CONTENT]"
        return self.content
    
    def write_content(self, content: str) -> bool:
        if not self.encrypted:
            self.content = content
            return True
        return False
    
    def search(self, query: str) -> List[str]:
        if self.encrypted:
            return ["Cannot search encrypted content"]
        lines = self.content.split('\n')
        return [line for line in lines if query.lower() in line.lower()]
    
    def encrypt(self, key: str) -> bool:
        if not self.encrypted:
            self.encrypted = True
            self.log_access("system", "encrypt")
            return True
        return False
    
    def decrypt(self, key: str) -> bool:
        if self.encrypted:
            self.encrypted = False
            self.log_access("system", "decrypt")
            return True
        return False
    
    def set_permissions(self, user: str, permissions: List[str]) -> bool:
        self.permissions[user] = permissions
        self.log_access("admin", f"set_permissions for {user}")
        return True
    
    def check_permission(self, user: str, action: str) -> bool:
        return action in self.permissions.get(user, [])
    
    def log_access(self, user: str, action: str) -> None:
        import datetime
        self.audit_log.append({
            "user": user,
            "action": action,
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    def get_audit_trail(self) -> List[Dict[str, Any]]:
        return self.audit_log.copy()

class EnterpriseDocument(Readable, Writable, Searchable, Versionable, 
                        Encryptable, AccessControlled, Auditable,
                        Convertible, Compressible, Signable,
                        Approvable, Publishable, Syncable, Exportable):
    def __init__(self, title: str, content: str = ""):
        self.title = title
        self.content = content
        self.versions = [content]
        self.encrypted = False
        self.compressed = False
        self.permissions = {}
        self.audit_log = []
        self.signatures = []
        self.approval_status = "draft"
        self.published = False
    
    # Implement all interface methods (abbreviated for space)
    def read_content(self) -> str:
        if self.encrypted:
            return "[ENCRYPTED CONTENT]"
        return self.content
    
    def write_content(self, content: str) -> bool:
        if not self.encrypted and self.approval_status == "draft":
            self.content = content
            return True
        return False
    
    def search(self, query: str) -> List[str]:
        if self.encrypted:
            return ["Cannot search encrypted content"]
        lines = self.content.split('\n')
        return [line for line in lines if query.lower() in line.lower()]
    
    def create_version(self) -> str:
        version_id = f"v{len(self.versions)}"
        self.versions.append(self.content)
        self.log_access("system", f"created version {version_id}")
        return version_id
    
    def get_version_history(self) -> List[str]:
        return [f"v{i}" for i in range(len(self.versions))]
    
    # ... (implement remaining methods)
    
    def submit_for_approval(self, approver: str) -> bool:
        if self.approval_status == "draft":
            self.approval_status = "pending"
            self.log_access(approver, "submitted_for_approval")
            return True
        return False
    
    def approve(self, approver: str) -> bool:
        if self.approval_status == "pending":
            self.approval_status = "approved"
            self.log_access(approver, "approved")
            return True
        return False
    
    def publish(self, channel: str) -> bool:
        if self.approval_status == "approved":
            self.published = True
            self.log_access("system", f"published to {channel}")
            return True
        return False
    
    # Additional method implementations...
    def encrypt(self, key: str) -> bool:
        self.encrypted = True
        return True
    
    def decrypt(self, key: str) -> bool:
        self.encrypted = False
        return True
    
    def set_permissions(self, user: str, permissions: List[str]) -> bool:
        self.permissions[user] = permissions
        return True
    
    def check_permission(self, user: str, action: str) -> bool:
        return action in self.permissions.get(user, [])
    
    def log_access(self, user: str, action: str) -> None:
        import datetime
        self.audit_log.append({
            "user": user,
            "action": action,
            "timestamp": datetime.datetime.now().isoformat()
        })
    
    def get_audit_trail(self) -> List[Dict[str, Any]]:
        return self.audit_log.copy()

# Specialized service classes that depend only on specific interfaces
class DocumentReader:
    def read_documents(self, documents: List[Readable]) -> List[str]:
        """Service that only needs to read documents"""
        return [doc.read_content() for doc in documents]

class SecurityManager:
    def secure_documents(self, documents: List[Encryptable], key: str) -> List[bool]:
        """Service that only handles encryption"""
        return [doc.encrypt(key) for doc in documents]
    
    def audit_access(self, documents: List[Auditable]) -> Dict[str, List[Dict]]:
        """Service that only handles auditing"""
        return {f"doc_{i}": doc.get_audit_trail() 
                for i, doc in enumerate(documents)}

class WorkflowManager:
    def process_approvals(self, documents: List[Approvable], approver: str) -> List[bool]:
        """Service that only handles approval workflow"""
        results = []
        for doc in documents:
            doc.submit_for_approval(approver)
            results.append(doc.approve(approver))
        return results

class PublishingService:
    def publish_documents(self, documents: List[Publishable], channel: str) -> List[bool]:
        """Service that only handles publishing"""
        return [doc.publish(channel) for doc in documents]

class VersionControl:
    def create_snapshots(self, documents: List[Versionable]) -> List[str]:
        """Service that only handles versioning"""
        return [doc.create_version() for doc in documents]

class IntegrationService:
    def sync_to_cloud(self, documents: List[Syncable], provider: str) -> List[bool]:
        """Service that only handles cloud synchronization"""
        return [doc.sync_to_cloud(provider) for doc in documents]
    
    def export_documents(self, documents: List[Exportable], system: str) -> List[bool]:
        """Service that only handles exports"""
        return [doc.export_to_system(system, "pdf") for doc in documents]

# Document management facade that coordinates services
class DocumentManagementSystem:
    def __init__(self):
        self.reader = DocumentReader()
        self.security = SecurityManager()
        self.workflow = WorkflowManager()
        self.publisher = PublishingService()
        self.version_control = VersionControl()
        self.integration = IntegrationService()
    
    def process_document_lifecycle(self, document: EnterpriseDocument, approver: str):
        """Demonstrate full document lifecycle using ISP-compliant services"""
        print(f"Processing document: {document.title}")
        
        # Version control
        if isinstance(document, Versionable):
            version = self.version_control.create_snapshots([document])[0]
            print(f"  Created version: {version}")
        
        # Security
        if isinstance(document, Encryptable):
            encrypted = self.security.secure_documents([document], "secret_key")[0]
            print(f"  Encrypted: {encrypted}")
        
        # Workflow
        if isinstance(document, Approvable):
            approved = self.workflow.process_approvals([document], approver)[0]
            print(f"  Approved: {approved}")
        
        # Publishing
        if isinstance(document, Publishable):
            published = self.publisher.publish_documents([document], "web")[0]
            print(f"  Published: {published}")
        
        # Integration
        if isinstance(document, Syncable):
            synced = self.integration.sync_to_cloud([document], "aws")[0]
            print(f"  Synced to cloud: {synced}")

# Example usage
print("=== Advanced Document Management System ===")

# Create different types of documents
basic_doc = BasicDocument("Basic Report", "This is a basic document.")
secure_doc = SecureDocument("Confidential Report", "This is confidential.")
enterprise_doc = EnterpriseDocument("Strategic Plan", "This is our strategy.")

# Set up permissions for secure document
secure_doc.set_permissions("user1", ["read", "write"])
secure_doc.set_permissions("admin", ["read", "write", "encrypt", "decrypt"])

# Create document management system
dms = DocumentManagementSystem()

# Process enterprise document through full lifecycle
dms.process_document_lifecycle(enterprise_doc, "manager")

# Demonstrate service segregation
print("\n=== Service Segregation Demo ===")

# Each service only works with documents that support its interface
documents = [basic_doc, secure_doc, enterprise_doc]

# Reading service works with all documents (all implement Readable)
readable_docs = [doc for doc in documents if isinstance(doc, Readable)]
print(f"Documents that can be read: {len(readable_docs)}")

# Security service only works with documents that support encryption
encryptable_docs = [doc for doc in documents if isinstance(doc, Encryptable)]
print(f"Documents that can be encrypted: {len(encryptable_docs)}")

# Workflow service only works with documents that support approval
approvable_docs = [doc for doc in documents if isinstance(doc, Approvable)]
print(f"Documents that support approval workflow: {len(approvable_docs)}")
```

### Example 5: Plugin Architecture with ISP

Let's explore how ISP enables flexible plugin architectures.

```python
from abc import ABC, abstractmethod
from typing import Dict, List, Any

# Core plugin interfaces
class Plugin(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def get_version(self) -> str:
        pass

class Initializable(ABC):
    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    def shutdown(self) -> bool:
        pass

class Configurable(ABC):
    @abstractmethod
    def configure(self, settings: Dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    def get_configuration(self) -> Dict[str, Any]:
        pass

# Capability-specific interfaces
class DataProcessor(ABC):
    @abstractmethod
    def process_data(self, data: Any) -> Any:
        pass

class EventListener(ABC):
    @abstractmethod
    def handle_event(self, event: str, data: Any) -> None:
        pass

class UIProvider(ABC):
    @abstractmethod
    def render_ui(self) -> str:
        pass
    
    @abstractmethod
    def handle_user_input(self, input_data: str) -> Any:
        pass

class NetworkCapable(ABC):
    @abstractmethod
    def send_request(self, url: str, data: Any) -> Any:
        pass
    
    @abstractmethod
    def receive_data(self) -> Any:
        pass

class Cacheable(ABC):
    @abstractmethod
    def cache_data(self, key: str, data: Any) -> bool:
        pass
    
    @abstractmethod
    def get_cached_data(self, key: str) -> Any:
        pass

# Plugin implementations
class DataAnalyticsPlugin(Plugin, Initializable, Configurable, DataProcessor, Cacheable):
    def __init__(self):
        self.config = {}
        self.cache = {}
        self.initialized = False
    
    def get_name(self) -> str:
        return "Data Analytics Plugin"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.config = config
        self.initialized = True
        return True
    
    def shutdown(self) -> bool:
        self.cache.clear()
        self.initialized = False
        return True
    
    def configure(self, settings: Dict[str, Any]) -> bool:
        self.config.update(settings)
        return True
    
    def get_configuration(self) -> Dict[str, Any]:
        return self.config.copy()
    
    def process_data(self, data: Any) -> Any:
        # Simulate data processing
        processed = f"Analyzed: {data}"
        self.cache_data(f"processed_{hash(str(data))}", processed)
        return processed
    
    def cache_data(self, key: str, data: Any) -> bool:
        self.cache[key] = data
        return True
    
    def get_cached_data(self, key: str) -> Any:
        return self.cache.get(key)

class NotificationPlugin(Plugin, Initializable, EventListener, NetworkCapable):
    def __init__(self):
        self.initialized = False
        self.subscribers = []
    
    def get_name(self) -> str:
        return "Notification Plugin"
    
    def get_version(self) -> str:
        return "2.1.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.initialized = True
        return True
    
    def shutdown(self) -> bool:
        self.subscribers.clear()
        self.initialized = False
        return True
    
    def handle_event(self, event: str, data: Any) -> None:
        notification = f"Event '{event}' occurred with data: {data}"
        self.send_request("notification-service", notification)
    
    def send_request(self, url: str, data: Any) -> Any:
        return f"Sent to {url}: {data}"
    
    def receive_data(self) -> Any:
        return "Notification acknowledgment received"

class UIPlugin(Plugin, Initializable, Configurable, UIProvider, EventListener):
    def __init__(self):
        self.config = {}
        self.initialized = False
    
    def get_name(self) -> str:
        return "UI Plugin"
    
    def get_version(self) -> str:
        return "3.0.0"
    
    def initialize(self, config: Dict[str, Any]) -> bool:
        self.config = config
        self.initialized = True
        return True
    
    def shutdown(self) -> bool:
        self.initialized = False
        return True
    
    def configure(self, settings: Dict[str, Any]) -> bool:
        self.config.update(settings)
        return True
    
    def get_configuration(self) -> Dict[str, Any]:
        return self.config.copy()
    
    def render_ui(self) -> str:
        theme = self.config.get("theme", "default")
        return f"Rendering UI with {theme} theme"
    
    def handle_user_input(self, input_data: str) -> Any:
        return f"Processing user input: {input_data}"
    
    def handle_event(self, event: str, data: Any) -> None:
        if event == "ui_update":
            print(f"UI updated with: {data}")

# Plugin management system
class PluginManager:
    def __init__(self):
        self.plugins: List[Plugin] = []
        self.initialized_plugins: List[Initializable] = []
        self.event_listeners: List[EventListener] = []
        self.data_processors: List[DataProcessor] = []
        self.ui_providers: List[UIProvider] = []
    
    def register_plugin(self, plugin: Plugin) -> bool:
        """Register a plugin and categorize it by capabilities"""
        self.plugins.append(plugin)
        
        if isinstance(plugin, Initializable):
            self.initialized_plugins.append(plugin)
        
        if isinstance(plugin, EventListener):
            self.event_listeners.append(plugin)
        
        if isinstance(plugin, DataProcessor):
            self.data_processors.append(plugin)
        
        if isinstance(plugin, UIProvider):
            self.ui_providers.append(plugin)
        
        return True
    
    def initialize_all_plugins(self, config: Dict[str, Any]) -> List[bool]:
        """Initialize only plugins that support initialization"""
        results = []
        for plugin in self.initialized_plugins:
            result = plugin.initialize(config)
            results.append(result)
            print(f"Initialized {plugin.get_name()}: {result}")
        return results
    
    def process_data_with_all_processors(self, data: Any) -> List[Any]:
        """Process data with all data processing plugins"""
        results = []
        for processor in self.data_processors:
            result = processor.process_data(data)
            results.append(result)
        return results
    
    def broadcast_event(self, event: str, data: Any) -> None:
        """Send event to all event listener plugins"""
        for listener in self.event_listeners:
            listener.handle_event(event, data)
    
    def render_all_uis(self) -> List[str]:
        """Render UI from all UI provider plugins"""
        return [ui.render_ui() for ui in self.ui_providers]
    
    def get_plugin_info(self) -> List[Dict[str, str]]:
        """Get information about all registered plugins"""
        return [
            {"name": plugin.get_name(), "version": plugin.get_version()}
            for plugin in self.plugins
        ]

# Example usage
print("\n=== Plugin Architecture Demo ===")

# Create plugin manager
manager = PluginManager()

# Register plugins
plugins = [
    DataAnalyticsPlugin(),
    NotificationPlugin(),
    UIPlugin()
]

for plugin in plugins:
    manager.register_plugin(plugin)
    print(f"Registered: {plugin.get_name()}")

# Initialize plugins
print("\n--- Plugin Initialization ---")
manager.initialize_all_plugins({"debug": True, "theme": "dark"})

# Process data with available processors
print("\n--- Data Processing ---")
sample_data = "user_activity_log.csv"
results = manager.process_data_with_all_processors(sample_data)
for result in results:
    print(f"Processed result: {result}")

# Broadcast events to listeners
print("\n--- Event Broadcasting ---")
manager.broadcast_event("user_login", {"user": "alice", "timestamp": "2025-01-01"})

# Render UIs
print("\n--- UI Rendering ---")
ui_outputs = manager.render_all_uis()
for output in ui_outputs:
    print(f"UI Output: {output}")

# Show plugin information
print("\n--- Plugin Information ---")
for info in manager.get_plugin_info():
    print(f"Plugin: {info['name']} v{info['version']}")
```

### Key Takeaways for Advanced Level

1. **Interface Composition**: Combine multiple focused interfaces to create complex behaviors
2. **Service Segregation**: Each service depends only on the interfaces it actually needs
3. **Plugin Architecture**: ISP enables flexible plugin systems where plugins implement only needed capabilities
4. **Facade Pattern**: Use facades to coordinate multiple ISP-compliant services
5. **Capability-Based Design**: Design around what objects can do, not what they are
6. **Cross-Cutting Concerns**: Handle concerns like security and auditing through separate interfaces

---

## Expert Level: Design Patterns and Architecture

### 🎯 Learning Objectives
By the end of this section, you will:
- Master advanced architectural patterns with ISP
- Design microservices with ISP principles
- Understand ISP in distributed systems
- Create domain-driven designs using ISP

### Example 6: Microservices Architecture with ISP

Let's design a comprehensive e-commerce system using microservices and ISP principles.

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

# Domain events and data structures
@dataclass
class Product:
    id: str
    name: str
    price: float
    category: str

@dataclass
class Order:
    id: str
    customer_id: str
    items: List[Dict[str, Any]]
    total: float
    status: str

@dataclass
class Customer:
    id: str
    name: str
    email: str
    tier: str

# Core business capability interfaces
class ProductCatalog(ABC):
    @abstractmethod
    def get_product(self, product_id: str) -> Optional[Product]:
        pass
    
    @abstractmethod
    def search_products(self, query: str) -> List[Product]:
        pass
    
    @abstractmethod
    def get_products_by_category(self, category: str) -> List[Product]:
        pass

class InventoryManagement(ABC):
    @abstractmethod
    def check_availability(self, product_id: str, quantity: int) -> bool:
        pass
    
    @abstractmethod
    def reserve_inventory(self, product_id: str, quantity: int) -> bool:
        pass
    
    @abstractmethod
    def release_inventory(self, product_id: str, quantity: int) -> bool:
        pass

class PricingEngine(ABC):
    @abstractmethod
    def calculate_price(self, product_id: str, customer_id: str, quantity: int) -> float:
        pass
    
    @abstractmethod
    def apply_discount(self, customer_id: str, amount: float) -> float:
        pass

class OrderManagement(ABC):
    @abstractmethod
    def create_order(self, customer_id: str, items: List[Dict]) -> Order:
        pass
    
    @abstractmethod
    def update_order_status(self, order_id: str, status: str) -> bool:
        pass
    
    @abstractmethod
    def get_order(self, order_id: str) -> Optional[Order]:
        pass

class PaymentProcessing(ABC):
    @abstractmethod
    def process_payment(self, order_id: str, amount: float, method: str) -> bool:
        pass
    
    @abstractmethod
    def refund_payment(self, order_id: str, amount: float) -> bool:
        pass

class ShippingService(ABC):
    @abstractmethod
    def calculate_shipping(self, order: Order, address: str) -> float:
        pass
    
    @abstractmethod
    def create_shipment(self, order: Order, address: str) -> str:
        pass
    
    @abstractmethod
    def track_shipment(self, shipment_id: str) -> Dict[str, Any]:
        pass

# Cross-cutting concern interfaces
class EventPublisher(ABC):
    @abstractmethod
    def publish_event(self, event_type: str, data: Dict[str, Any]) -> None:
        pass

class CacheManager(ABC):
    @abstractmethod
    def get(self, key: str) -> Any:
        pass
    
    @abstractmethod
    def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        pass
    
    @abstractmethod
    def invalidate(self, key: str) -> None:
        pass

class MetricsCollector(ABC):
    @abstractmethod
    def increment_counter(self, metric: str, tags: Dict[str, str] = None) -> None:
        pass
    
    @abstractmethod
    def record_timing(self, metric: str, duration: float, tags: Dict[str, str] = None) -> None:
        pass

class AuditLogger(ABC):
    @abstractmethod
    def log_action(self, user_id: str, action: str, resource: str, details: Dict = None) -> None:
        pass

# Microservice implementations
class ProductService(ProductCatalog, CacheManager, MetricsCollector):
    def __init__(self):
        self.products = {}
        self.cache = {}
    
    def get_product(self, product_id: str) -> Optional[Product]:
        self.increment_counter("product.get_requests")
        
        # Check cache first
        cached = self.get(f"product:{product_id}")
        if cached:
            return cached
        
        # Simulate database lookup
        product = self.products.get(product_id)
        if product:
            self.set(f"product:{product_id}", product)
        
        return product
    
    def search_products(self, query: str) -> List[Product]:
        self.increment_counter("product.search_requests")
        # Simulate search logic
        return [p for p in self.products.values() if query.lower() in p.name.lower()]
    
    def get_products_by_category(self, category: str) -> List[Product]:
        self.increment_counter("product.category_requests")
        return [p for p in self.products.values() if p.category == category]
    
    def get(self, key: str) -> Any:
        return self.cache.get(key)
    
    def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        self.cache[key] = value
    
    def invalidate(self, key: str) -> None:
        self.cache.pop(key, None)
    
    def increment_counter(self, metric: str, tags: Dict[str, str] = None) -> None:
        print(f"Metric: {metric} incremented")
    
    def record_timing(self, metric: str, duration: float, tags: Dict[str, str] = None) -> None:
        print(f"Metric: {metric} recorded {duration}ms")

class OrderService(OrderManagement, EventPublisher, AuditLogger, MetricsCollector):
    def __init__(self):
        self.orders = {}
        self.order_counter = 0
    
    def create_order(self, customer_id: str, items: List[Dict]) -> Order:
        self.increment_counter("order.created")
        
        self.order_counter += 1
        order_id = f"ORD-{self.order_counter:06d}"
        
        total = sum(item['price'] * item['quantity'] for item in items)
        
        order = Order(
            id=order_id,
            customer_id=customer_id,
            items=items,
            total=total,
            status="created"
        )
        
        self.orders[order_id] = order
        
        # Publish event
        self.publish_event("order.created", {
            "order_id": order_id,
            "customer_id": customer_id,
            "total": total
        })
        
        # Log action
        self.log_action(customer_id, "create_order", order_id, {"total": total})
        
        return order
    
    def update_order_status(self, order_id: str, status: str) -> bool:
        if order_id in self.orders:
            old_status = self.orders[order_id].status
            self.orders[order_id].status = status
            
            self.publish_event("order.status_changed", {
                "order_id": order_id,
                "old_status": old_status,
                "new_status": status
            })
            
            return True
        return False
    
    def get_order(self, order_id: str) -> Optional[Order]:
        return self.orders.get(order_id)
    
    def publish_event(self, event_type: str, data: Dict[str, Any]) -> None:
        print(f"Event published: {event_type} - {data}")
    
    def log_action(self, user_id: str, action: str, resource: str, details: Dict = None) -> None:
        print(f"Audit: User {user_id} performed {action} on {resource}")
    
    def increment_counter(self, metric: str, tags: Dict[str, str] = None) -> None:
        print(f"Metric: {metric} incremented")
    
    def record_timing(self, metric: str, duration: float, tags: Dict[str, str] = None) -> None:
        print(f"Metric: {metric} recorded {duration}ms")

class PaymentService(PaymentProcessing, EventPublisher, AuditLogger, MetricsCollector):
    def __init__(self):
        self.payments = {}
    
    def process_payment(self, order_id: str, amount: float, method: str) -> bool:
        self.increment_counter("payment.processed")
        
        # Simulate payment processing
        success = amount > 0  # Simple validation
        
        self.payments[order_id] = {
            "amount": amount,
            "method": method,
            "status": "success" if success else "failed"
        }
        
        self.publish_event("payment.processed", {
            "order_id": order_id,
            "amount": amount,
            "method": method,
            "success": success
        })
        
        self.log_action("system", "process_payment", order_id, {
            "amount": amount,
            "method": method,
            "success": success
        })
        
        return success
    
    def refund_payment(self, order_id: str, amount: float) -> bool:
        if order_id in self.payments:
            self.publish_event("payment.refunded", {
                "order_id": order_id,
                "amount": amount
            })
            return True
        return False
    
    def publish_event(self, event_type: str, data: Dict[str, Any]) -> None:
        print(f"Event published: {event_type} - {data}")
    
    def log_action(self, user_id: str, action: str, resource: str, details: Dict = None) -> None:
        print(f"Audit: User {user_id} performed {action} on {resource}")
    
    def increment_counter(self, metric: str, tags: Dict[str, str] = None) -> None:
        print(f"Metric: {metric} incremented")
    
    def record_timing(self, metric: str, duration: float, tags: Dict[str, str] = None) -> None:
        print(f"Metric: {metric} recorded {duration}ms")

# Orchestration layer that coordinates microservices
class ECommerceOrchestrator:
    def __init__(self, product_service: ProductCatalog, 
                 inventory_service: InventoryManagement,
                 pricing_service: PricingEngine,
                 order_service: OrderManagement,
                 payment_service: PaymentProcessing,
                 shipping_service: ShippingService):
        self.product_service = product_service
        self.inventory_service = inventory_service
        self.pricing_service = pricing_service
        self.order_service = order_service
        self.payment_service = payment_service
        self.shipping_service = shipping_service
    
    def process_customer_order(self, customer_id: str, cart_items: List[Dict], 
                             payment_method: str, shipping_address: str) -> Dict[str, Any]:
        """
        Orchestrate a complete order processing workflow using ISP-compliant services
        """
        try:
            # Step 1: Validate products and check inventory
            validated_items = []
            for item in cart_items:
                product = self.product_service.get_product(item['product_id'])
                if not product:
                    return {"success": False, "error": f"Product {item['product_id']} not found"}
                
                if not self.inventory_service.check_availability(item['product_id'], item['quantity']):
                    return {"success": False, "error": f"Insufficient inventory for {product.name}"}
                
                # Calculate pricing
                price = self.pricing_service.calculate_price(
                    item['product_id'], customer_id, item['quantity']
                )
                
                validated_items.append({
                    'product_id': item['product_id'],
                    'quantity': item['quantity'],
                    'price': price,
                    'name': product.name
                })
            
            # Step 2: Reserve inventory
            for item in validated_items:
                self.inventory_service.reserve_inventory(item['product_id'], item['quantity'])
            
            # Step 3: Create order
            order = self.order_service.create_order(customer_id, validated_items)
            
            # Step 4: Calculate shipping
            shipping_cost = self.shipping_service.calculate_shipping(order, shipping_address)
            total_amount = order.total + shipping_cost
            
            # Step 5: Process payment
            payment_success = self.payment_service.process_payment(
                order.id, total_amount, payment_method
            )
            
            if not payment_success:
                # Rollback inventory reservations
                for item in validated_items:
                    self.inventory_service.release_inventory(item['product_id'], item['quantity'])
                return {"success": False, "error": "Payment processing failed"}
            
            # Step 6: Update order status and create shipment
            self.order_service.update_order_status(order.id, "paid")
            shipment_id = self.shipping_service.create_shipment(order, shipping_address)
            self.order_service.update_order_status(order.id, "shipped")
            
            return {
                "success": True,
                "order_id": order.id,
                "shipment_id": shipment_id,
                "total_amount": total_amount
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}

# Mock implementations for demonstration
class MockInventoryService(InventoryManagement):
    def check_availability(self, product_id: str, quantity: int) -> bool:
        return True  # Always available for demo
    
    def reserve_inventory(self, product_id: str, quantity: int) -> bool:
        print(f"Reserved {quantity} units of {product_id}")
        return True
    
    def release_inventory(self, product_id: str, quantity: int) -> bool:
        print(f"Released {quantity} units of {product_id}")
        return True

class MockPricingService(PricingEngine):
    def calculate_price(self, product_id: str, customer_id: str, quantity: int) -> float:
        base_price = 10.0  # Mock base price
        return base_price * quantity
    
    def apply_discount(self, customer_id: str, amount: float) -> float:
        return amount * 0.9  # 10% discount

class MockShippingService(ShippingService):
    def calculate_shipping(self, order: Order, address: str) -> float:
        return 5.99  # Flat shipping rate
    
    def create_shipment(self, order: Order, address: str) -> str:
        shipment_id = f"SHIP-{order.id}"
        print(f"Created shipment {shipment_id} for order {order.id}")
        return shipment_id
    
    def track_shipment(self, shipment_id: str) -> Dict[str, Any]:
        return {"status": "in_transit", "estimated_delivery": "2025-01-15"}

# Example usage
print("=== Expert Level: Microservices with ISP ===")

# Initialize services
product_service = ProductService()
inventory_service = MockInventoryService()
pricing_service = MockPricingService()
order_service = OrderService()
payment_service = PaymentService()
shipping_service = MockShippingService()

# Add some sample products
product_service.products["PROD-001"] = Product("PROD-001", "Laptop", 999.99, "Electronics")
product_service.products["PROD-002"] = Product("PROD-002", "Mouse", 29.99, "Electronics")

# Create orchestrator
orchestrator = ECommerceOrchestrator(
    product_service, inventory_service, pricing_service,
    order_service, payment_service, shipping_service
)

# Process a customer order
cart_items = [
    {"product_id": "PROD-001", "quantity": 1},
    {"product_id": "PROD-002", "quantity": 2}
]

result = orchestrator.process_customer_order(
    customer_id="CUST-001",
    cart_items=cart_items,
    payment_method="credit_card",
    shipping_address="123 Main St, City, State"
)

print(f"Order processing result: {result}")
```

### Example 7: Domain-Driven Design with ISP

```python
from abc import ABC, abstractmethod
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

# Domain entities and value objects
@dataclass
class UserId:
    value: str

@dataclass
class Email:
    value: str

@dataclass
class Money:
    amount: float
    currency: str

# Domain interfaces segregated by business capabilities
class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: UserId) -> Optional['User']:
        pass
    
    @abstractmethod
    def find_by_email(self, email: Email) -> Optional['User']:
        pass
    
    @abstractmethod
    def save(self, user: 'User') -> None:
        pass

class AccountRepository(ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: UserId) -> Optional['Account']:
        pass
    
    @abstractmethod
    def save(self, account: 'Account') -> None:
        pass

class TransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: 'Transaction') -> None:
        pass
    
    @abstractmethod
    def find_by_account_id(self, account_id: str) -> List['Transaction']:
        pass

# Domain services interfaces
class EmailService(ABC):
    @abstractmethod
    def send_notification(self, email: Email, subject: str, body: str) -> bool:
        pass

class FraudDetectionService(ABC):
    @abstractmethod
    def is_suspicious_transaction(self, transaction: 'Transaction') -> bool:
        pass

class ExchangeRateService(ABC):
    @abstractmethod
    def convert(self, amount: Money, target_currency: str) -> Money:
        pass

# Application service interfaces
class UserRegistrationService(ABC):
    @abstractmethod
    def register_user(self, email: Email, password: str) -> UserId:
        pass

class AccountManagementService(ABC):
    @abstractmethod
    def create_account(self, user_id: UserId, initial_balance: Money) -> str:
        pass
    
    @abstractmethod
    def get_balance(self, account_id: str) -> Money:
        pass

class TransferService(ABC):
    @abstractmethod
    def transfer_money(self, from_account: str, to_account: str, amount: Money) -> bool:
        pass

# Domain entities
class User:
    def __init__(self, user_id: UserId, email: Email, password_hash: str):
        self.id = user_id
        self.email = email
        self.password_hash = password_hash
        self.created_at = datetime.now()

class Account:
    def __init__(self, account_id: str, user_id: UserId, balance: Money):
        self.id = account_id
        self.user_id = user_id
        self.balance = balance
        self.created_at = datetime.now()
    
    def debit(self, amount: Money) -> bool:
        if self.balance.amount >= amount.amount and self.balance.currency == amount.currency:
            self.balance.amount -= amount.amount
            return True
        return False
    
    def credit(self, amount: Money) -> None:
        if self.balance.currency == amount.currency:
            self.balance.amount += amount.amount

class Transaction:
    def __init__(self, from_account: str, to_account: str, amount: Money):
        self.id = f"TXN-{datetime.now().timestamp()}"
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.timestamp = datetime.now()
        self.status = "pending"

# Implementation of application services using ISP
class BankingApplicationService(UserRegistrationService, AccountManagementService, TransferService):
    def __init__(self, 
                 user_repo: UserRepository,
                 account_repo: AccountRepository,
                 transaction_repo: TransactionRepository,
                 email_service: EmailService,
                 fraud_service: FraudDetectionService,
                 exchange_service: ExchangeRateService):
        self.user_repo = user_repo
        self.account_repo = account_repo
        self.transaction_repo = transaction_repo
        self.email_service = email_service
        self.fraud_service = fraud_service
        self.exchange_service = exchange_service
    
    def register_user(self, email: Email, password: str) -> UserId:
        # Check if user already exists
        existing_user = self.user_repo.find_by_email(email)
        if existing_user:
            raise ValueError("User already exists")
        
        # Create new user
        user_id = UserId(f"USER-{datetime.now().timestamp()}")
        user = User(user_id, email, self._hash_password(password))
        
        self.user_repo.save(user)
        
        # Send welcome email
        self.email_service.send_notification(
            email, 
            "Welcome to Our Bank", 
            "Your account has been created successfully"
        )
        
        return user_id
    
    def create_account(self, user_id: UserId, initial_balance: Money) -> str:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        account_id = f"ACC-{datetime.now().timestamp()}"
        account = Account(account_id, user_id, initial_balance)
        
        self.account_repo.save(account)
        
        return account_id
    
    def get_balance(self, account_id: str) -> Money:
        # This method would need account_id to UserId mapping in real implementation
        # Simplified for demonstration
        accounts = []  # Would query by account_id
        if accounts:
            return accounts[0].balance
        raise ValueError("Account not found")
    
    def transfer_money(self, from_account: str, to_account: str, amount: Money) -> bool:
        # Create transaction
        transaction = Transaction(from_account, to_account, amount)
        
        # Check for fraud
        if self.fraud_service.is_suspicious_transaction(transaction):
            transaction.status = "blocked"
            self.transaction_repo.save(transaction)
            return False
        
        # Get accounts (simplified - would use proper queries)
        from_acc = Account(from_account, UserId("user1"), Money(1000.0, "USD"))
        to_acc = Account(to_account, UserId("user2"), Money(500.0, "USD"))
        
        # Perform transfer
        if from_acc.debit(amount):
            to_acc.credit(amount)
            transaction.status = "completed"
            
            # Save changes
            self.account_repo.save(from_acc)
            self.account_repo.save(to_acc)
            self.transaction_repo.save(transaction)
            
            return True
        else:
            transaction.status = "failed"
            self.transaction_repo.save(transaction)
            return False
    
    def _hash_password(self, password: str) -> str:
        return f"hashed_{password}"  # Simplified for demo

# Client code that depends only on specific interfaces
class UserOnboardingWorkflow:
    def __init__(self, registration_service: UserRegistrationService, 
                 account_service: AccountManagementService):
        self.registration_service = registration_service
        self.account_service = account_service
    
    def onboard_new_user(self, email_str: str, password: str, initial_deposit: float):
        """Complete user onboarding workflow"""
        email = Email(email_str)
        
        # Register user
        user_id = self.registration_service.register_user(email, password)
        print(f"User registered with ID: {user_id.value}")
        
        # Create account with initial deposit
        initial_balance = Money(initial_deposit, "USD")
        account_id = self.account_service.create_account(user_id, initial_balance)
        print(f"Account created with ID: {account_id}")
        
        return {"user_id": user_id.value, "account_id": account_id}

class TransferWorkflow:
    def __init__(self, transfer_service: TransferService):
        self.transfer_service = transfer_service
    
    def process_transfer(self, from_account: str, to_account: str, amount: float, currency: str):
        """Process money transfer"""
        money = Money(amount, currency)
        success = self.transfer_service.transfer_money(from_account, to_account, money)
        
        if success:
            print(f"Transfer of {amount} {currency} completed successfully")
        else:
            print("Transfer failed")
        
        return success

print("\n=== Domain-Driven Design with ISP ===")

# Mock implementations for demonstration
class MockUserRepository(UserRepository):
    def __init__(self):
        self.users = {}
    
    def find_by_id(self, user_id: UserId) -> Optional[User]:
        return self.users.get(user_id.value)
    
    def find_by_email(self, email: Email) -> Optional[User]:
        for user in self.users.values():
            if user.email.value == email.value:
                return user
        return None
    
    def save(self, user: User) -> None:
        self.users[user.id.value] = user

# Create mock services and repositories
user_repo = MockUserRepository()
# ... other mock implementations would go here

# Demonstrate ISP benefits in domain-driven design
print("ISP enables clean separation of domain concerns")
print("Each service interface represents a specific business capability")
print("Clients depend only on the interfaces they actually need")
```

### Key Takeaways for Expert Level

1. **Microservices Design**: ISP enables clean service boundaries and loose coupling
2. **Domain-Driven Design**: Business capabilities map naturally to focused interfaces
3. **Orchestration Patterns**: Coordinate multiple ISP-compliant services without tight coupling
4. **Cross-Cutting Concerns**: Handle infrastructure concerns through separate interfaces
5. **Evolutionary Architecture**: ISP makes systems more adaptable to changing requirements
6. **Testing Strategy**: Focused interfaces enable precise mocking and testing

---

## Common Pitfalls and How to Avoid Them

### ❌ Pitfall 1: Over-Segregation
**Problem**: Creating too many tiny interfaces with single methods.

```python
# Too granular - over-segregation
class Readable(ABC):
    @abstractmethod
    def read(self):
        pass

class Openable(ABC):
    @abstractmethod
    def open(self):
        pass

class Closeable(ABC):
    @abstractmethod
    def close(self):
        pass

# Better - cohesive grouping
class FileOperations(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
```

**Solution**: Group related methods that are typically used together.

### ❌ Pitfall 2: Interface Pollution
**Problem**: Adding methods to interfaces just because some implementations can support them.

```python
# Bad - polluted interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def record(self):  # Not all players can record!
        pass

# Good - segregated interfaces
class Playable(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass

class Recordable(ABC):
    @abstractmethod
    def record(self):
        pass
```

### ❌ Pitfall 3: Ignoring Client Needs
**Problem**: Designing interfaces based on implementation rather than client requirements.

```python
# Bad - implementation-driven
class DatabaseConnection(ABC):
    @abstractmethod
    def connect_to_mysql(self):
        pass
    
    @abstractmethod
    def connect_to_postgresql(self):
        pass

# Good - client-driven
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self, connection_string: str):
        pass

class QueryExecutor(ABC):
    @abstractmethod
    def execute_query(self, query: str):
        pass
```

---

## Best Practices

### 1. **Start with Client Requirements**
- Identify what clients actually need
- Design interfaces based on use cases
- Avoid anticipating future requirements

### 2. **Keep Interfaces Cohesive**
- Group related methods together
- Ensure methods in an interface work toward the same goal
- Avoid mixing unrelated concerns

### 3. **Use Composition Over Large Interfaces**
```python
# Good practice - compose multiple focused interfaces
class SmartDevice(Controllable, Monitorable, Configurable):
    pass
```

### 4. **Apply the "Role Interface" Pattern**
```python
# Design interfaces around roles/capabilities
class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, credentials):
        pass

class Authorizer(ABC):
    @abstractmethod
    def authorize(self, user, resource):
        pass
```

### 5. **Consider Interface Evolution**
- Design for backward compatibility
- Use versioning when breaking changes are needed
- Prefer adding new interfaces over modifying existing ones

---

## Real-World Examples

### 1. **Web Framework Design**
```python
# Request handling interfaces
class RequestHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

class Middleware(ABC):
    @abstractmethod
    def process_request(self, request):
        pass
    
    @abstractmethod
    def process_response(self, response):
        pass

class TemplateRenderer(ABC):
    @abstractmethod
    def render_template(self, template_name, context):
        pass

class SessionManager(ABC):
    @abstractmethod
    def get_session(self, session_id):
        pass
    
    @abstractmethod
    def save_session(self, session):
        pass
```

### 2. **Database ORM Design**
```python
# ORM interfaces following ISP
class Queryable(ABC):
    @abstractmethod
    def filter(self, **kwargs):
        pass
    
    @abstractmethod
    def order_by(self, field):
        pass

class Executable(ABC):
    @abstractmethod
    def execute(self):
        pass

class Cacheable(ABC):
    @abstractmethod
    def cache_result(self, key, ttl):
        pass

class Model(Queryable, Executable):
    pass
```

### 3. **Cloud Service Integration**
```python
# Cloud service interfaces
class StorageService(ABC):
    @abstractmethod
    def upload_file(self, file_path, content):
        pass
    
    @abstractmethod
    def download_file(self, file_path):
        pass

class ComputeService(ABC):
    @abstractmethod
    def create_instance(self, config):
        pass
    
    @abstractmethod
    def terminate_instance(self, instance_id):
        pass

class MonitoringService(ABC):
    @abstractmethod
    def log_metric(self, metric_name, value):
        pass
    
    @abstractmethod
    def create_alert(self, condition):
        pass
```

---

## Testing ISP-Compliant Code

### 1. **Interface-Based Testing**
```python
import unittest
from unittest.mock import Mock

class TestDocumentProcessor(unittest.TestCase):
    def test_process_readable_documents(self):
        # Mock only the interface we need
        mock_readable = Mock(spec=Readable)
        mock_readable.read_content.return_value = "test content"
        
        processor = DocumentProcessor()
        result = processor.process_document(mock_readable)
        
        mock_readable.read_content.assert_called_once()
        self.assertEqual(result, "processed: test content")
    
    def test_secure_encryptable_documents(self):
        # Mock only the encryption interface
        mock_encryptable = Mock(spec=Encryptable)
        mock_encryptable.encrypt.return_value = True
        
        security_manager = SecurityManager()
        result = security_manager.secure_document(mock_encryptable, "key")
        
        mock_encryptable.encrypt.assert_called_once_with("key")
        self.assertTrue(result)
```

### 2. **Focused Test Doubles**
```python
class MockPrintable(Printable):
    def __init__(self):
        self.printed_documents = []
    
    def print_document(self, document):
        self.printed_documents.append(document)
        return f"Mock printed: {document}"

class MockScannable(Scannable):
    def __init__(self):
        self.scanned_documents = []
    
    def scan_document(self, document):
        self.scanned_documents.append(document)
        return f"Mock scanned: {document}"
```

### 3. **Contract Testing**
```python
class PrintableContractTest:
    """Base test class to verify Printable interface contract"""
    
    def create_printable(self) -> Printable:
        """Override in subclasses to provide implementation"""
        raise NotImplementedError
    
    def test_print_document_returns_string(self):
        printable = self.create_printable()
        result = printable.print_document("test.pdf")
        self.assertIsInstance(result, str)
    
    def test_print_document_handles_empty_input(self):
        printable = self.create_printable()
        result = printable.print_document("")
        self.assertIsInstance(result, str)

class BasicPrinterTest(PrintableContractTest, unittest.TestCase):
    def create_printable(self) -> Printable:
        return BasicPrinter()
```

---

## Conclusion

### 🎉 Congratulations!

You've completed the comprehensive Interface Segregation Principle tutorial! You now understand:

#### **Core Concepts**
- What ISP is and why it matters
- How to identify and fix ISP violations
- The difference between fat and focused interfaces

#### **Practical Skills**
- Designing role-based interfaces
- Implementing ISP in real-world scenarios
- Balancing interface granularity

#### **Advanced Techniques**
- Microservices architecture with ISP
- Domain-driven design patterns
- Plugin architectures and extensibility

#### **Professional Practices**
- Testing ISP-compliant code
- Avoiding common pitfalls
- Evolutionary interface design

### 🚀 Next Steps

1. **Practice**: Apply ISP to your current projects
2. **Refactor**: Identify fat interfaces in existing code and segregate them
3. **Design**: Use ISP principles in new system designs
4. **Share**: Teach others about ISP benefits

### 📚 Further Reading

- **Books**: "Clean Architecture" by Robert C. Martin
- **Patterns**: Study the Strategy, Observer, and Adapter patterns
- **Frameworks**: Examine how popular frameworks apply ISP
- **Code Reviews**: Look for ISP violations in code reviews

### 💡 Remember

> **"The Interface Segregation Principle is about designing for your clients, not your implementations. Focus on what clients need, and your interfaces will naturally become more focused, flexible, and maintainable."**

### 🎯 Final Challenge

Design an ISP-compliant system for a domain you're familiar with. Consider:
- What are the different client needs?
- How can you segregate interfaces by responsibility?
- What cross-cutting concerns need separate interfaces?
- How will you test your design?

**Happy coding, and may your interfaces be forever focused!** 🎊

---

*This tutorial is part of the SOLID Principles series. Continue your journey with the Dependency Inversion Principle to complete your understanding of SOLID design principles.*
