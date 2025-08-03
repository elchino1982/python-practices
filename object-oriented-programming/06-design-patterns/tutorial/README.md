# Design Patterns in Python - Comprehensive Tutorial

## Table of Contents
1. [Introduction to Design Patterns](#introduction)
2. [Understanding Pattern Categories](#pattern-categories)
3. [Creational Patterns](#creational-patterns)
4. [Structural Patterns](#structural-patterns)
5. [Behavioral Patterns](#behavioral-patterns)
6. [Advanced Pattern Combinations](#advanced-combinations)
7. [Real-World Applications](#real-world-applications)
8. [Best Practices](#best-practices)
9. [Common Pitfalls](#common-pitfalls)
10. [Exercises and Practice](#exercises)

---

## Introduction to Design Patterns {#introduction}

**Design Patterns** are proven solutions to recurring problems in software design. They represent best practices evolved over time by experienced developers and provide a common vocabulary for discussing design solutions.

### Why Design Patterns Matter

🎯 **Key Benefits:**
- **Proven Solutions**: Time-tested approaches to common problems
- **Communication**: Common vocabulary for developers
- **Reusability**: Solutions that can be applied across different contexts
- **Maintainability**: Well-structured, understandable code
- **Flexibility**: Designs that can adapt to changing requirements

### Real-World Analogy

Think of design patterns like **architectural blueprints**:
- **Blueprints** provide proven solutions for building structures
- **Patterns** provide proven solutions for software structures
- Both can be **adapted** to specific needs
- Both promote **consistency** and **quality**
- Both help **communicate** complex ideas simply

### The Gang of Four (GoF)

The most famous design patterns come from the book "Design Patterns: Elements of Reusable Object-Oriented Software" by the Gang of Four (Gamma, Helm, Johnson, and Vlissides). They identified 23 fundamental patterns.

---

## Understanding Pattern Categories {#pattern-categories}

Design patterns are typically organized into three main categories:

### 1. Creational Patterns 🏗️
**Purpose**: Deal with object creation mechanisms
**Focus**: How objects are created, composed, and represented
**Examples**: Singleton, Factory, Builder, Prototype

```python
# Example: Factory Pattern
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")
```

### 2. Structural Patterns 🏛️
**Purpose**: Deal with object composition and relationships
**Focus**: How classes and objects are composed to form larger structures
**Examples**: Adapter, Decorator, Facade, Proxy

```python
# Example: Decorator Pattern
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2
```

### 3. Behavioral Patterns 🎭
**Purpose**: Deal with communication between objects and assignment of responsibilities
**Focus**: How objects interact and distribute responsibilities
**Examples**: Observer, Strategy, Command, State

```python
# Example: Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
```

### Pattern Comparison Table

| Category | Purpose | When to Use | Common Examples |
|----------|---------|-------------|-----------------|
| **Creational** | Object creation | Need flexible object creation | Singleton, Factory |
| **Structural** | Object composition | Need to organize classes/objects | Adapter, Decorator |
| **Behavioral** | Object interaction | Need to define communication | Observer, Strategy |

---

## Creational Patterns {#creational-patterns}

Creational patterns abstract the instantiation process and help make systems independent of how objects are created, composed, and represented.

### 1. Singleton Pattern

**Intent**: Ensure a class has only one instance and provide global access to it.

**When to Use**:
- Need exactly one instance (database connection, logger)
- Global access point required
- Instance creation is expensive

```python
class Singleton:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.value = 0
            self._initialized = True
    
    def increment(self):
        self.value += 1
        return self.value

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - same instance

s1.increment()
print(s2.value)  # 1 - shared state
```

### 2. Factory Pattern

**Intent**: Create objects without specifying their exact classes.

**When to Use**:
- Object creation logic is complex
- Need to decouple object creation from usage
- Want to centralize object creation

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animals = {
            'dog': Dog,
            'cat': Cat,
            'bird': Bird
        }
        
        animal_class = animals.get(animal_type.lower())
        if animal_class:
            return animal_class()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.make_sound())  # Woof!
print(cat.make_sound())  # Meow!
```

### 3. Builder Pattern

**Intent**: Construct complex objects step by step.

**When to Use**:
- Object construction is complex
- Want to create different representations
- Need to construct objects with many optional parameters

```python
class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.graphics = None
    
    def __str__(self):
        return f"Computer(CPU: {self.cpu}, Memory: {self.memory}, Storage: {self.storage}, Graphics: {self.graphics})"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self  # Return self for method chaining
    
    def set_memory(self, memory):
        self.computer.memory = memory
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def set_graphics(self, graphics):
        self.computer.graphics = graphics
        return self
    
    def build(self):
        return self.computer

class ComputerDirector:
    @staticmethod
    def build_gaming_computer():
        return (ComputerBuilder()
                .set_cpu("Intel i9")
                .set_memory("32GB DDR4")
                .set_storage("1TB NVMe SSD")
                .set_graphics("RTX 4080")
                .build())
    
    @staticmethod
    def build_office_computer():
        return (ComputerBuilder()
                .set_cpu("Intel i5")
                .set_memory("16GB DDR4")
                .set_storage("512GB SSD")
                .set_graphics("Integrated")
                .build())

# Usage
gaming_pc = ComputerDirector.build_gaming_computer()
office_pc = ComputerDirector.build_office_computer()

print(gaming_pc)
print(office_pc)
```

### 4. Prototype Pattern

**Intent**: Create objects by cloning existing instances.

**When to Use**:
- Object creation is expensive
- Need to create objects similar to existing ones
- Want to avoid subclasses of creator

```python
import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Document(Prototype):
    def __init__(self, title, content, formatting):
        self.title = title
        self.content = content
        self.formatting = formatting
    
    def clone(self):
        # Deep copy to ensure complete independence
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Document(title='{self.title}', content='{self.content[:20]}...', formatting={self.formatting})"

class DocumentManager:
    def __init__(self):
        self._prototypes = {}
    
    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype
    
    def create_document(self, prototype_name, title, content):
        if prototype_name in self._prototypes:
            # Clone the prototype and customize
            document = self._prototypes[prototype_name].clone()
            document.title = title
            document.content = content
            return document
        else:
            raise ValueError(f"Unknown prototype: {prototype_name}")

# Usage
manager = DocumentManager()

# Register prototypes
report_template = Document("Template", "", {"font": "Arial", "size": 12, "margins": "1in"})
letter_template = Document("Template", "", {"font": "Times", "size": 11, "margins": "1.5in"})

manager.register_prototype("report", report_template)
manager.register_prototype("letter", letter_template)

# Create documents from prototypes
quarterly_report = manager.create_document("report", "Q1 Report", "Sales increased by 15%...")
cover_letter = manager.create_document("letter", "Cover Letter", "Dear Hiring Manager...")

print(quarterly_report)
print(cover_letter)
```

---

## Structural Patterns {#structural-patterns}

Structural patterns deal with object composition, helping to ensure that if one part changes, the entire structure doesn't need to change.

### 1. Adapter Pattern

**Intent**: Allow incompatible interfaces to work together.

**When to Use**:
- Need to use existing class with incompatible interface
- Want to create reusable class that cooperates with unrelated classes
- Need to use several existing subclasses but can't adapt their interface

```python
# Target interface that client expects
class MediaPlayer:
    def play(self, audio_type, filename):
        pass

# Existing classes with different interfaces
class Mp3Player:
    def play_mp3(self, filename):
        print(f"Playing MP3 file: {filename}")

class Mp4Player:
    def play_mp4(self, filename):
        print(f"Playing MP4 file: {filename}")

class VlcPlayer:
    def play_vlc(self, filename):
        print(f"Playing VLC file: {filename}")

# Adapter to make incompatible interfaces work
class MediaAdapter:
    def __init__(self, audio_type):
        if audio_type == "mp4":
            self.player = Mp4Player()
        elif audio_type == "vlc":
            self.player = VlcPlayer()
    
    def play(self, audio_type, filename):
        if audio_type == "mp4":
            self.player.play_mp4(filename)
        elif audio_type == "vlc":
            self.player.play_vlc(filename)

# Client class that uses the adapter
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            # Built-in support for MP3
            mp3_player = Mp3Player()
            mp3_player.play_mp3(filename)
        elif audio_type in ["mp4", "vlc"]:
            # Use adapter for other formats
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")

# Usage
player = AudioPlayer()
player.play("mp3", "song.mp3")
player.play("mp4", "video.mp4")
player.play("vlc", "movie.vlc")
player.play("avi", "video.avi")  # Not supported
```

### 2. Decorator Pattern

**Intent**: Add new functionality to objects dynamically without altering their structure.

**When to Use**:
- Want to add responsibilities to objects dynamically
- Extension by subclassing is impractical
- Need to add functionality that can be withdrawn

```python
from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def description(self):
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5.0
    
    def description(self):
        return "Simple coffee"

# Base decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2.0
    
    def description(self):
        return self._coffee.description() + ", milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.0
    
    def description(self):
        return self._coffee.description() + ", sugar"

class WhipDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3.0
    
    def description(self):
        return self._coffee.description() + ", whipped cream"

class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.5
    
    def description(self):
        return self._coffee.description() + ", vanilla"

# Usage
coffee = SimpleCoffee()
print(f"{coffee.description()}: ${coffee.cost()}")

# Add milk
coffee = MilkDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")

# Add sugar
coffee = SugarDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")

# Add whipped cream
coffee = WhipDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")

# Create a complex coffee in one go
fancy_coffee = VanillaDecorator(
    WhipDecorator(
        SugarDecorator(
            MilkDecorator(
                SimpleCoffee()
            )
        )
    )
)
print(f"{fancy_coffee.description()}: ${fancy_coffee.cost()}")
```

### 3. Facade Pattern

**Intent**: Provide a unified interface to a set of interfaces in a subsystem.

**When to Use**:
- Want to provide simple interface to complex subsystem
- Need to decouple clients from subsystem components
- Want to layer your subsystems

```python
# Complex subsystem classes
class CPU:
    def freeze(self):
        print("CPU: Freezing processor")
    
    def jump(self, position):
        print(f"CPU: Jumping to position {position}")
    
    def execute(self):
        print("CPU: Executing instructions")

class Memory:
    def load(self, position, data):
        print(f"Memory: Loading data '{data}' at position {position}")

class HardDrive:
    def read(self, lba, size):
        print(f"HardDrive: Reading {size} bytes from LBA {lba}")
        return f"Boot data from sector {lba}"

class GPU:
    def render(self):
        print("GPU: Rendering graphics")

class SoundCard:
    def play_sound(self, sound):
        print(f"SoundCard: Playing {sound}")

# Facade class
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
        self.gpu = GPU()
        self.sound_card = SoundCard()
    
    def start_computer(self):
        print("=== Starting Computer ===")
        self.cpu.freeze()
        boot_data = self.hard_drive.read(0, 1024)
        self.memory.load(0, boot_data)
        self.cpu.jump(0)
        self.cpu.execute()
        self.gpu.render()
        self.sound_card.play_sound("startup.wav")
        print("=== Computer Started Successfully ===")
    
    def shutdown_computer(self):
        print("=== Shutting Down Computer ===")
        self.sound_card.play_sound("shutdown.wav")
        print("=== Computer Shut Down ===")
    
    def restart_computer(self):
        print("=== Restarting Computer ===")
        self.shutdown_computer()
        self.start_computer()

# Usage
computer = ComputerFacade()
computer.start_computer()
print()
computer.restart_computer()
print()
computer.shutdown_computer()
```

### 4. Proxy Pattern

**Intent**: Provide a placeholder or surrogate for another object to control access to it.

**When to Use**:
- Need lazy initialization (virtual proxy)
- Need access control (protection proxy)
- Need local representation of remote object (remote proxy)
- Need to add functionality when accessing object

```python
from abc import ABC, abstractmethod
import time

# Subject interface
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Real subject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self._load_from_disk()
    
    def _load_from_disk(self):
        print(f"Loading image from disk: {self.filename}")
        # Simulate expensive loading operation
        time.sleep(1)
    
    def display(self):
        print(f"Displaying image: {self.filename}")

# Proxy
class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None
    
    def display(self):
        if self._real_image is None:
            # Lazy loading - create real object only when needed
            self._real_image = RealImage(self.filename)
        self._real_image.display()

# Protection Proxy
class ProtectedImageProxy(Image):
    def __init__(self, filename, user_role):
        self.filename = filename
        self.user_role = user_role
        self._real_image = None
    
    def display(self):
        if self._has_access():
            if self._real_image is None:
                self._real_image = RealImage(self.filename)
            self._real_image.display()
        else:
            print(f"Access denied: {self.user_role} cannot view {self.filename}")
    
    def _has_access(self):
        # Simple access control logic
        restricted_files = ["classified.jpg", "secret.png"]
        if self.filename in restricted_files:
            return self.user_role == "admin"
        return True

# Caching Proxy
class CachingImageProxy(Image):
    _cache = {}
    
    def __init__(self, filename):
        self.filename = filename
    
    def display(self):
        if self.filename not in self._cache:
            print(f"Cache miss for {self.filename}")
            self._cache[self.filename] = RealImage(self.filename)
        else:
            print(f"Cache hit for {self.filename}")
        
        self._cache[self.filename].display()

# Usage
print("=== Virtual Proxy (Lazy Loading) ===")
proxy_image = ImageProxy("photo.jpg")
print("Proxy created, but image not loaded yet")
proxy_image.display()  # Now image is loaded
proxy_image.display()  # Uses already loaded image

print("\n=== Protection Proxy ===")
admin_image = ProtectedImageProxy("classified.jpg", "admin")
user_image = ProtectedImageProxy("classified.jpg", "user")

admin_image.display()  # Access granted
user_image.display()   # Access denied

print("\n=== Caching Proxy ===")
cache_proxy1 = CachingImageProxy("cached_photo.jpg")
cache_proxy2 = CachingImageProxy("cached_photo.jpg")

cache_proxy1.display()  # Cache miss - loads image
cache_proxy2.display()  # Cache hit - uses cached image
```

---

## Behavioral Patterns {#behavioral-patterns}

Behavioral patterns focus on communication between objects and the assignment of responsibilities.

### 1. Observer Pattern

**Intent**: Define a one-to-many dependency between objects so that when one object changes state, all dependents are notified.

**When to Use**:
- Need to notify multiple objects about state changes
- Want loose coupling between subject and observers
- Need to add/remove observers dynamically

```python
from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

# Concrete subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0
    
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer {observer.__class__.__name__} attached")
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer {observer.__class__.__name__} detached")
    
    def notify(self):
        print("Notifying all observers...")
        for observer in self._observers:
            observer.update(self)
    
    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()
    
    @property
    def temperature(self):
        return self._temperature
    
    @property
    def humidity(self):
        return self._humidity
    
    @property
    def pressure(self):
        return self._pressure

# Concrete observers
class CurrentConditionsDisplay(Observer):
    def update(self, subject: WeatherStation):
        print(f"Current Conditions: {subject.temperature}°F, {subject.humidity}% humidity")

class StatisticsDisplay(Observer):
    def __init__(self):
        self._temperatures = []
    
    def update(self, subject: WeatherStation):
        self._temperatures.append(subject.temperature)
        avg_temp = sum(self._temperatures) / len(self._temperatures)
        print(f"Statistics: Avg temp: {avg_temp:.1f}°F, Min: {min(self._temperatures)}°F, Max: {max(self._temperatures)}°F")

class ForecastDisplay(Observer):
    def update(self, subject: WeatherStation):
        if subject.pressure > 30.20:
            forecast = "Improving weather on the way!"
        elif subject.pressure < 29.20:
            forecast = "Watch out for cooler, rainy weather"
        else:
            forecast = "More of the same"
        print(f"Forecast: {forecast}")

# Usage
weather_station = WeatherStation()

# Create and attach observers
current_display = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()
forecast_display = ForecastDisplay()

weather_station.attach(current_display)
weather_station.attach(statistics_display)
weather_station.attach(forecast_display)

# Update weather data
print("=== Weather Update 1 ===")
weather_station.set_measurements(80, 65, 30.4)

print("\n=== Weather Update 2 ===")
weather_station.set_measurements(82, 70, 29.2)

print("\n=== Detaching Statistics Display ===")
weather_station.detach(statistics_display)

print("\n=== Weather Update 3 ===")
weather_station.set_measurements(78, 90, 29.2)
```

### 2. Strategy Pattern

**Intent**: Define a family of algorithms, encapsulate each one, and make them interchangeable.

**When to Use**:
- Have multiple ways to perform a task
- Want to switch algorithms at runtime
- Need to eliminate conditional statements

```python
from abc import ABC, abstractmethod

# Strategy interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass
    
    @abstractmethod
    def get_name(self):
        pass

# Concrete strategies
class BubbleSort(SortingStrategy):
    def sort(self, data):
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def get_name(self):
        return "Bubble Sort"

class QuickSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        return self.sort(left) + middle + self.sort(right)
    
    def get_name(self):
        return "Quick Sort"

class MergeSort(SortingStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def get_name(self):
        return "Merge Sort"

# Context class
class Sorter:
    def __init__(self, strategy: SortingStrategy = None):
        self._strategy = strategy
    
    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy
    
    def sort_data(self, data):
        if self._strategy is None:
            raise ValueError("No sorting strategy set")
        
        print(f"Using {self._strategy.get_name()}")
        return self._strategy.sort(data)

# Usage
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original data: {data}")

sorter = Sorter()

# Use different strategies
strategies = [BubbleSort(), QuickSort(), MergeSort()]

for strategy in strategies:
    sorter.set_strategy(strategy)
    sorted_data = sorter.sort_data(data)
    print(f"Sorted with {strategy.get_name()}: {sorted_data}")
    print()
```

### 3. Command Pattern

**Intent**: Encapsulate a request as an object, allowing you to parameterize clients with different requests, queue operations, and support undo.

**When to Use**:
- Need to parameterize objects with operations
- Want to queue, log, or support undo operations
- Need to support macro recording

```python
from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

# Receiver classes
class Light:
    def __init__(self, location):
        self.location = location
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.location} light is ON")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.location} light is OFF")

class Fan:
    def __init__(self, location):
        self.location = location
        self.speed = 0  # 0=off, 1=low, 2=medium, 3=high
    
    def turn_on(self, speed=1):
        self.speed = speed
        speeds = ["OFF", "LOW", "MEDIUM", "HIGH"]
        print(f"{self.location} fan is {speeds[speed]}")
    
    def turn_off(self):
        self.speed = 0
        print(f"{self.location} fan is OFF")

# Concrete commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
    
    def undo(self):
        self.light.turn_on()

class FanOnCommand(Command):
    def __init__(self, fan, speed=1):
        self.fan = fan
        self.speed = speed
        self.previous_speed = 0
    
    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.turn_on(self.speed)
    
    def undo(self):
        if self.previous_speed == 0:
            self.fan.turn_off()
        else:
            self.fan.turn_on(self.previous_speed)

class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan
        self.previous_speed = 0
    
    def execute(self):
        self.previous_speed = self.fan.speed
        self.fan.turn_off()
    
    def undo(self):
        if self.previous_speed > 0:
            self.fan.turn_on(self.previous_speed)

# Null Object pattern for empty slots
class NoCommand(Command):
    def execute(self):
        pass
    
    def undo(self):
        pass

# Macro command
class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands
    
    def execute(self):
        for command in self.commands:
            command.execute()
    
    def undo(self):
        # Undo in reverse order
        for command in reversed(self.commands):
            command.undo()

# Invoker
class RemoteControl:
    def __init__(self):
        self.on_commands = [NoCommand()] * 7
        self.off_commands = [NoCommand()] * 7
        self.undo_command = NoCommand()
    
    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command
    
    def on_button_pressed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]
    
    def off_button_pressed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]
    
    def undo_button_pressed(self):
        self.undo_command.undo()

# Usage
remote = RemoteControl()

# Create devices
living_room_light = Light("Living Room")
kitchen_light = Light("Kitchen")
bedroom_fan = Fan("Bedroom")

# Create commands
living_room_light_on = LightOnCommand(living_room_light)
living_room_light_off = LightOffCommand(living_room_light)
kitchen_light_on = LightOnCommand(kitchen_light)
kitchen_light_off = LightOffCommand(kitchen_light)
bedroom_fan_on = FanOnCommand(bedroom_fan, 2)
bedroom_fan_off = FanOffCommand(bedroom_fan)

# Set up remote
remote.set_command(0, living_room_light_on, living_room_light_off)
remote.set_command(1, kitchen_light_on, kitchen_light_off)
remote.set_command(2, bedroom_fan_on, bedroom_fan_off)

# Create macro command for "party mode"
party_on = MacroCommand([living_room_light_on, kitchen_light_on, bedroom_fan_on])
party_off = MacroCommand([living_room_light_off, kitchen_light_off, bedroom_fan_off])
remote.set_command(6, party_on, party_off)

# Test the remote
print("=== Testing Remote Control ===")
remote.on_button_pressed(0)   # Living room light on
remote.off_button_pressed(0)  # Living room light off
remote.undo_button_pressed()  # Undo (light back on)

print("\n=== Party Mode ===")
remote.on_button_pressed(6)   # Party mode on
remote.undo_button_pressed()  # Undo party mode
```

---

## Advanced Pattern Combinations {#advanced-combinations}

Real-world applications often combine multiple design patterns to solve complex problems.

### 1. MVC (Model-View-Controller) Pattern

Combines Observer, Strategy, and Composite patterns:

```python
from abc import ABC, abstractmethod
from typing import List

# Model (Subject in Observer pattern)
class Model:
    def __init__(self):
        self._observers: List['Observer'] = []
        self._data = {}
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def set_data(self, key, value):
        self._data[key] = value
        self.notify()
    
    def get_data(self, key):
        return self._data.get(key)
    
    def get_all_data(self):
        return self._data.copy()

# View (Observer pattern)
class View(ABC):
    @abstractmethod
    def update(self, model):
        pass
    
    @abstractmethod
    def render(self):
        pass

class ConsoleView(View):
    def __init__(self, name):
        self.name = name
        self.model_data = {}
    
    def update(self, model):
        self.model_data = model.get_all_data()
        self.render()
    
    def render(self):
        print(f"=== {self.name} View ===")
        for key, value in self.model_data.items():
            print(f"{key}: {value}")
        print()

class WebView(View):
    def __init__(self):
        self.model_data = {}
    
    def update(self, model):
        self.model_data = model.get_all_data()
        self.render()
    
    def render(self):
        print("=== Web View (HTML) ===")
        print("<html><body>")
        for key, value in self.model_data.items():
            print(f"<p><strong>{key}:</strong> {value}</p>")
        print("</body></html>")
        print()

# Controller (Strategy pattern for different actions)
class Controller:
    def __init__(self, model):
        self.model = model
    
    def update_user_name(self, name):
        self.model.set_data("user_name", name)
    
    def update_user_email(self, email):
        self.model.set_data("user_email", email)
    
    def update_user_age(self, age):
        self.model.set_data("user_age", age)

# Usage
model = Model()
console_view = ConsoleView("Console")
web_view = WebView()

model.attach(console_view)
model.attach(web_view)

controller = Controller(model)

# Update data through controller
controller.update_user_name("Alice")
controller.update_user_email("alice@example.com")
controller.update_user_age(30)
```

### 2. Plugin Architecture with Multiple Patterns

Combines Factory, Strategy, Observer, and Registry patterns:

```python
from abc import ABC, abstractmethod
from typing import Dict, List, Any

# Plugin interface (Strategy pattern)
class Plugin(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    def execute(self, data: Any) -> Any:
        pass

# Plugin Registry (Registry pattern)
class PluginRegistry:
    _plugins: Dict[str, type] = {}
    
    @classmethod
    def register(cls, plugin_class):
        """Decorator to register plugins"""
        cls._plugins[plugin_class.__name__] = plugin_class
        return plugin_class
    
    @classmethod
    def get_plugin(cls, name: str):
        return cls._plugins.get(name)
    
    @classmethod
    def list_plugins(cls):
        return list(cls._plugins.keys())

# Plugin Factory (Factory pattern)
class PluginFactory:
    @staticmethod
    def create_plugin(plugin_name: str, **kwargs):
        plugin_class = PluginRegistry.get_plugin(plugin_name)
        if plugin_class:
            return plugin_class(**kwargs)
        raise ValueError(f"Unknown plugin: {plugin_name}")

# Event system (Observer pattern)
class EventManager:
    def __init__(self):
        self._listeners: Dict[str, List[callable]] = {}
    
    def subscribe(self, event_name: str, callback: callable):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(callback)
    
    def emit(self, event_name: str, data: Any = None):
        if event_name in self._listeners:
            for callback in self._listeners[event_name]:
                callback(data)

# Plugin Manager (Facade pattern)
class PluginManager:
    def __init__(self):
        self.event_manager = EventManager()
        self.loaded_plugins: Dict[str, Plugin] = {}
    
    def load_plugin(self, plugin_name: str, **kwargs):
        try:
            plugin = PluginFactory.create_plugin(plugin_name, **kwargs)
            self.loaded_plugins[plugin.name] = plugin
            self.event_manager.emit("plugin_loaded", plugin.name)
            return plugin
        except ValueError as e:
            self.event_manager.emit("plugin_error", str(e))
            raise
    
    def execute_plugin(self, plugin_name: str, data: Any):
        if plugin_name in self.loaded_plugins:
            result = self.loaded_plugins[plugin_name].execute(data)
            self.event_manager.emit("plugin_executed", {
                "plugin": plugin_name,
                "result": result
            })
            return result
        raise ValueError(f"Plugin {plugin_name} not loaded")

# Concrete plugins
@PluginRegistry.register
class DataValidatorPlugin(Plugin):
    def __init__(self, rules=None):
        self.rules = rules or []
    
    @property
    def name(self):
        return "DataValidator"
    
    def execute(self, data):
        print(f"Validating data with {len(self.rules)} rules")
        # Simulate validation
        return {"valid": True, "data": data}

@PluginRegistry.register
class DataTransformerPlugin(Plugin):
    def __init__(self, transformation_type="uppercase"):
        self.transformation_type = transformation_type
    
    @property
    def name(self):
        return "DataTransformer"
    
    def execute(self, data):
        if self.transformation_type == "uppercase" and isinstance(data, str):
            return data.upper()
        return data

@PluginRegistry.register
class DataLoggerPlugin(Plugin):
    @property
    def name(self):
        return "DataLogger"
    
    def execute(self, data):
        print(f"Logging data: {data}")
        return data

# Usage
manager = PluginManager()

# Subscribe to events
manager.event_manager.subscribe("plugin_loaded", 
    lambda name: print(f"Plugin loaded: {name}"))
manager.event_manager.subscribe("plugin_executed", 
    lambda data: print(f"Plugin executed: {data['plugin']} -> {data['result']}"))

# Load and use plugins
print("Available plugins:", PluginRegistry.list_plugins())

validator = manager.load_plugin("DataValidatorPlugin", rules=["required", "email"])
transformer = manager.load_plugin("DataTransformerPlugin", transformation_type="uppercase")
logger = manager.load_plugin("DataLoggerPlugin")

# Execute plugins
test_data = "hello world"
result1 = manager.execute_plugin("DataValidator", test_data)
result2 = manager.execute_plugin("DataTransformer", test_data)
result3 = manager.execute_plugin("DataLogger", result2)
```

---

## Real-World Applications {#real-world-applications}

### 1. E-commerce System

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict

# State pattern for order states
class OrderState(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.state = OrderState.PENDING
        self.items = []
        self.total = 0.0
    
    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})
        self.total += item.price * quantity
    
    def confirm(self):
        if self.state == OrderState.PENDING:
            self.state = OrderState.CONFIRMED
            return True
        return False
    
    def ship(self):
        if self.state == OrderState.CONFIRMED:
            self.state = OrderState.SHIPPED
            return True
        return False
    
    def deliver(self):
        if self.state == OrderState.SHIPPED:
            self.state = OrderState.DELIVERED
            return True
        return False

# Strategy pattern for payment methods
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    def pay(self, amount: float) -> bool:
        print(f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}")
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> bool:
        print(f"Paid ${amount} using PayPal account {self.email}")
        return True

class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number: str):
        self.account_number = account_number
    
    def pay(self, amount: float) -> bool:
        print(f"Paid ${amount} using Bank Transfer from account {self.account_number}")
        return True

# Observer pattern for notifications
class OrderObserver(ABC):
    @abstractmethod
    def notify(self, order: Order, event: str):
        pass

class EmailNotification(OrderObserver):
    def notify(self, order: Order, event: str):
        print(f"Email: Order {order.order_id} has been {event}")

class SMSNotification(OrderObserver):
    def notify(self, order: Order, event: str):
        print(f"SMS: Order {order.order_id} status: {event}")

class PushNotification(OrderObserver):
    def notify(self, order: Order, event: str):
        print(f"Push: Your order {order.order_id} is now {event}")

# Factory pattern for creating different product types
class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

class ProductFactory:
    @staticmethod
    def create_product(product_type: str, name: str, price: float, **kwargs):
        if product_type == "electronics":
            return Product(name, price, "Electronics")
        elif product_type == "clothing":
            return Product(name, price, "Clothing")
        elif product_type == "books":
            return Product(name, price, "Books")
        else:
            return Product(name, price, "General")

# Main e-commerce system (Facade pattern)
class ECommerceSystem:
    def __init__(self):
        self.orders: Dict[str, Order] = {}
        self.observers: List[OrderObserver] = []
        self.payment_strategy: PaymentStrategy = None
    
    def add_observer(self, observer: OrderObserver):
        self.observers.append(observer)
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy
    
    def create_order(self, order_id: str) -> Order:
        order = Order(order_id)
        self.orders[order_id] = order
        self._notify_observers(order, "created")
        return order
    
    def process_payment(self, order_id: str) -> bool:
        order = self.orders.get(order_id)
        if order and self.payment_strategy:
            if self.payment_strategy.pay(order.total):
                order.confirm()
                self._notify_observers(order, "confirmed")
                return True
        return False
    
    def ship_order(self, order_id: str):
        order = self.orders.get(order_id)
        if order and order.ship():
            self._notify_observers(order, "shipped")
    
    def deliver_order(self, order_id: str):
        order = self.orders.get(order_id)
        if order and order.deliver():
            self._notify_observers(order, "delivered")
    
    def _notify_observers(self, order: Order, event: str):
        for observer in self.observers:
            observer.notify(order, event)

# Usage
ecommerce = ECommerceSystem()

# Add notification observers
ecommerce.add_observer(EmailNotification())
ecommerce.add_observer(SMSNotification())
ecommerce.add_observer(PushNotification())

# Create products
laptop = ProductFactory.create_product("electronics", "Gaming Laptop", 1200.0)
shirt = ProductFactory.create_product("clothing", "Cotton Shirt", 25.0)

# Create and process order
order = ecommerce.create_order("ORD-001")
order.add_item(laptop, 1)
order.add_item(shirt, 2)

print(f"Order total: ${order.total}")

# Set payment method and process payment
ecommerce.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456"))
ecommerce.process_payment("ORD-001")

# Ship and deliver
ecommerce.ship_order("ORD-001")
ecommerce.deliver_order("ORD-001")
```

---

## Best Practices {#best-practices}

### 1. Choose the Right Pattern

✅ **Good Pattern Selection:**
```python
# Use Observer when you need to notify multiple objects
class EventManager:
    def __init__(self):
        self._listeners = []
    
    def subscribe(self, listener):
        self._listeners.append(listener)
    
    def notify(self, event):
        for listener in self._listeners:
            listener.handle(event)

# Use Strategy when you have multiple algorithms
class DataProcessor:
    def __init__(self, strategy):
        self._strategy = strategy
    
    def process(self, data):
        return self._strategy.process(data)
```

❌ **Poor Pattern Selection:**
```python
# Don't use Singleton for everything
class DatabaseSingleton:  # Overkill for simple config
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Don't use Observer for simple callbacks
class SimpleCalculator:  # Observer is overkill here
    def __init__(self):
        self._observers = []
    
    def add(self, a, b):
        result = a + b
        self._notify_observers(result)  # Unnecessary complexity
        return result
```

### 2. Keep Patterns Simple

✅ **Simple Implementation:**
```python
class Command:
    def __init__(self, action, *args):
        self.action = action
        self.args = args
    
    def execute(self):
        return self.action(*self.args)

# Usage
def print_message(msg):
    print(msg)

command = Command(print_message, "Hello, World!")
command.execute()
```

❌ **Over-engineered Implementation:**
```python
class AbstractCommandFactoryBuilder:  # Too many patterns
    def create_command_factory(self):
        return CommandFactory()

class CommandFactory:
    def create_command(self, command_type):
        if command_type == "print":
            return PrintCommandBuilder().build()
        # ... more complexity
```

### 3. Document Pattern Usage

```python
class WeatherStation:
    """
    Weather monitoring system using Observer pattern.
    
    This class implements the Subject role in the Observer pattern,
    allowing multiple display elements to be notified when weather
    measurements change.
    
    Design Patterns Used:
    - Observer: For notifying displays of weather changes
    - Strategy: For different measurement algorithms (future)
    """
    
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
    
    def attach(self, observer):
        """Add an observer (Display element)"""
        self._observers.append(observer)
    
    def notify(self):
        """Notify all observers of state change"""
        for observer in self._observers:
            observer.update(self)
```

---

## Common Pitfalls {#common-pitfalls}

### 1. Pattern Overuse

❌ **Bad:**
```python
# Using patterns where simple solutions would work
class SingletonFactoryObserverCommand:  # Too many patterns!
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def create_observer_command(self, observer_type):
        # Unnecessary complexity for simple task
        pass
```

✅ **Good:**
```python
# Simple solution for simple problem
class MessageSender:
    def send(self, message, recipients):
        for recipient in recipients:
            print(f"Sending '{message}' to {recipient}")
```

### 2. Wrong Pattern Choice

❌ **Bad:**
```python
# Using Singleton for stateless utility class
class MathUtilsSingleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def add(self, a, b):
        return a + b  # No state needed!
```

✅ **Good:**
```python
# Simple static methods or functions
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Or even simpler
def add(a, b):
    return a + b
```

### 3. Ignoring Python Idioms

❌ **Bad:**
```python
# Java-style Observer in Python
class Observer:
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
```

✅ **Good:**
```python
# Pythonic approach with callbacks
class EventEmitter:
    def __init__(self):
        self._callbacks = []
    
    def on(self, callback):
        self._callbacks.append(callback)
    
    def emit(self, *args, **kwargs):
        for callback in self._callbacks:
            callback(*args, **kwargs)

# Usage
emitter = EventEmitter()
emitter.on(lambda data: print(f"Received: {data}"))
emitter.emit("Hello!")
```

---

## Exercises and Practice {#exercises}

### Beginner Level

1. **Observer Weather Station**
   - Create a weather station that notifies multiple displays
   - Implement temperature, humidity, and pressure sensors
   - Add different display types (current conditions, statistics, forecast)

2. **Strategy Calculator**
   - Create a calculator that can switch between different operation strategies
   - Implement addition, subtraction, multiplication, division strategies
   - Allow runtime strategy switching

### Intermediate Level

3. **Command Text Editor**
   - Build a simple text editor with undo/redo functionality
   - Implement commands for insert, delete, replace operations
   - Add macro recording capabilities

4. **Decorator Coffee Shop**
   - Create a coffee ordering system using decorator pattern
   - Base coffee types with various add-ons (milk, sugar, whip, etc.)
   - Calculate total cost with all decorations

### Advanced Level

5. **Factory Game Characters**
   - Design a game character creation system
   - Different character types (warrior, mage, archer) with unique abilities
   - Use abstract factory for different character families

6. **Proxy Image Gallery**
   - Build an image gallery with lazy loading
   - Implement virtual proxy for expensive image loading
   - Add caching and access control proxies

### Expert Level

7. **MVC Web Framework**
   - Create a mini web framework using MVC pattern
   - Combine Observer, Strategy, and Template Method patterns
   - Support multiple view formats (HTML, JSON, XML)

8. **Plugin Architecture**
   - Design an extensible plugin system
   - Combine Factory, Registry, Observer, and Strategy patterns
   - Support dynamic plugin loading and configuration

---

## Summary

Design patterns are powerful tools that help you:

- **Solve common problems** with proven solutions
- **Communicate effectively** with other developers
- **Write maintainable code** that's easy to understand and modify
- **Create flexible designs** that can adapt to changing requirements
- **Avoid reinventing the wheel** by using established best practices

### Key Takeaways

1. **Understand the problem first**: Choose patterns based on actual needs, not trends
2. **Start simple**: Don't over-engineer solutions with unnecessary patterns
3. **Learn the intent**: Understand why patterns exist, not just how to implement them
4. **Practice regularly**: Apply patterns in real projects to gain experience
5. **Combine wisely**: Real applications often use multiple patterns together

### Pattern Selection Guide

| Problem Type | Recommended Patterns | When to Use |
|-------------|---------------------|-------------|
| **Object Creation** | Singleton, Factory, Builder | Complex creation logic |
| **Object Structure** | Adapter, Decorator, Facade | Interface compatibility |
| **Object Behavior** | Observer, Strategy, Command | Dynamic behavior changes |
| **System Architecture** | MVC, Plugin, Layered | Large, complex systems |

### Next Steps

- Practice implementing patterns from scratch
- Study real-world frameworks to see patterns in action
- Experiment with pattern combinations
- Focus on solving real problems, not just learning patterns

Remember: Patterns are tools, not goals. Use them when they solve real problems and make your code better, not just because you can.

---