# Design Patterns in Python 🎨

Master the art of software design through proven patterns and elegant solutions. This comprehensive collection covers 23+ design patterns with practical Python implementations, real-world examples, and hands-on exercises.

## 🎯 Learning Objectives

By completing this section, you will:
- **Understand the Gang of Four (GoF)** design patterns and their applications
- **Master creational patterns** for flexible object creation
- **Implement structural patterns** for elegant object composition
- **Apply behavioral patterns** for effective object interaction
- **Recognize when and how** to use each pattern appropriately
- **Combine multiple patterns** to solve complex design problems
- **Write maintainable, extensible code** using proven design principles

## 📚 Pattern Categories

### 🏗️ Creational Patterns
**Purpose**: Deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

| Pattern | Purpose | When to Use | Implementation |
|---------|---------|-------------|----------------|
| **[Singleton](./singleton-pattern/)** | Ensure only one instance exists | Global access point needed | `01-basic-singleton-pattern.py` |
| **[Factory Method](./factory-method-pattern/)** | Create objects without specifying exact classes | Object creation logic varies | `01-factory-method-pattern.py` |
| **[Abstract Factory](./abstract-factory-pattern/)** | Create families of related objects | Multiple product families | `01-abstract-factory-pattern.py` |
| **[Builder](./builder-pattern/)** | Construct complex objects step by step | Complex object construction | `01-builder-pattern.py` |
| **[Prototype](./prototype-pattern/)** | Create objects by cloning existing instances | Object creation is expensive | `01-prototype-pattern.py` |

### 🏛️ Structural Patterns
**Purpose**: Deal with object composition and relationships between entities.

| Pattern | Purpose | When to Use | Implementation |
|---------|---------|-------------|----------------|
| **[Adapter](./adapter-pattern/)** | Make incompatible interfaces work together | Interface compatibility needed | `01-adapter-pattern.py` |
| **[Bridge](./bridge-pattern/)** | Separate abstraction from implementation | Avoid permanent binding | `01-bridge-pattern.py` |
| **[Composite](./composite-pattern/)** | Compose objects into tree structures | Part-whole hierarchies | `01-composite-pattern.py` |
| **[Decorator](./decorator-pattern/)** | Add behavior to objects dynamically | Extend functionality flexibly | `01-decorator-pattern.py` |
| **[Facade](./facade-pattern/)** | Provide simplified interface to complex subsystem | Simplify complex interfaces | `01-facade-pattern.py` |
| **[Flyweight](./flyweight-pattern/)** | Share common parts of state between objects | Memory optimization needed | `01-basic-flyweight-pattern.py` |
| **[Proxy](./proxy-pattern/)** | Provide placeholder/surrogate for another object | Control access to objects | `01-basic-proxy-pattern.py` |

### 🎭 Behavioral Patterns
**Purpose**: Focus on communication between objects and the assignment of responsibilities.

| Pattern | Purpose | When to Use | Implementation |
|---------|---------|-------------|----------------|
| **[Observer](./observer-pattern/)** | Define one-to-many dependency between objects | State change notifications | `01-event-observer-pattern.py` |
| **[Strategy](./strategy-pattern/)** | Define family of algorithms and make them interchangeable | Algorithm selection at runtime | `01-strategy-pattern.py` |
| **[Command](./command-pattern/)** | Encapsulate requests as objects | Undo/redo, queuing operations | `01-command-pattern.py` |
| **[State](./state-pattern/)** | Allow object to alter behavior when internal state changes | State-dependent behavior | `01-state-pattern.py` |
| **[Template Method](./template-method-pattern/)** | Define skeleton of algorithm, let subclasses override steps | Algorithm structure reuse | `01-template-method-pattern.py` |
| **[Chain of Responsibility](./chain-of-responsibility-pattern/)** | Pass requests along chain of handlers | Multiple processing options | `01-chain-of-responsibility-pattern.py` |
| **[Mediator](./mediator-pattern/)** | Define how objects interact with each other | Reduce coupling between objects | `01-mediator-pattern.py` |
| **[Memento](./memento-pattern/)** | Capture and restore object's internal state | Undo functionality needed | `01-memento-pattern.py` |
| **[Visitor](./visitor-pattern/)** | Define new operations without changing object structure | Operations on object structures | `01-visitor-pattern.py` |
| **[Iterator](./iterator-pattern/)** | Provide way to access elements sequentially | Traverse collections uniformly | `01-iterator-pattern.py` |
| **[Interpreter](./interpreter-pattern/)** | Define representation for grammar and interpreter | Language processing needed | `01-interpreter-pattern.py` |

## 🚀 Quick Start Guide

### 1. **Beginner Path** 🌱
Start with fundamental patterns that are commonly used:

```bash
# Essential patterns for beginners
1. Singleton Pattern          # Global access and single instance
2. Factory Method Pattern     # Object creation flexibility
3. Observer Pattern          # Event-driven programming
4. Strategy Pattern          # Algorithm selection
5. Decorator Pattern         # Extending functionality
```

### 2. **Intermediate Path** 🌿
Build upon basics with more complex patterns:

```bash
# Intermediate patterns for growing developers
1. Abstract Factory Pattern   # Family of related objects
2. Builder Pattern           # Complex object construction
3. Adapter Pattern           # Interface compatibility
4. Facade Pattern            # Simplified interfaces
5. Command Pattern           # Request encapsulation
```

### 3. **Advanced Path** 🌳
Master sophisticated patterns for complex systems:

```bash
# Advanced patterns for experienced developers
1. Composite Pattern         # Tree structures
2. Proxy Pattern            # Access control
3. State Pattern            # State-dependent behavior
4. Mediator Pattern         # Object interaction management
5. Visitor Pattern          # Operations on object structures
```

## 📁 Directory Structure

```
06-design-patterns/
├── README.md                           # This comprehensive guide
├── tutorial/                           # In-depth tutorial and theory
│   └── README.md                      # Complete design patterns tutorial
├── comprehensive-example/              # Advanced combined examples
│   ├── 01-comprehensive-design-patterns-example.py
│   ├── 02-registry-pattern-plugins.py
│   ├── 03-thread-safe-counter.py
│   ├── 04-immutable-set-collections.py
│   └── 05-comprehensive-oop-system.py
│
├── singleton-pattern/                  # Creational Pattern
│   ├── 01-basic-singleton-pattern.py
│   ├── 02-singleton-pattern-logger.py
│   ├── 03-thread-safe-singleton.py
│   └── 04-borg-pattern-configuration.py
│
├── factory-method-pattern/             # Creational Pattern
│   └── 01-factory-method-pattern.py
│
├── abstract-factory-pattern/           # Creational Pattern
│   └── 01-abstract-factory-pattern.py
│
├── builder-pattern/                    # Creational Pattern
│   └── 01-builder-pattern.py
│
├── prototype-pattern/                  # Creational Pattern
│   └── 01-prototype-pattern.py
│
├── adapter-pattern/                    # Structural Pattern
│   └── 01-adapter-pattern.py
│
├── bridge-pattern/                     # Structural Pattern
│   └── 01-bridge-pattern.py
│
├── composite-pattern/                  # Structural Pattern
│   └── 01-composite-pattern.py
│
├── decorator-pattern/                  # Structural Pattern
│   └── 01-decorator-pattern.py
│
├── facade-pattern/                     # Structural Pattern
│   └── 01-facade-pattern.py
│
├── flyweight-pattern/                  # Structural Pattern
│   ├── 01-basic-flyweight-pattern.py
│   └── 02-advanced-flyweight-pattern.py
│
├── proxy-pattern/                      # Structural Pattern
│   ├── 01-basic-proxy-pattern.py
│   └── 02-advanced-proxy-pattern.py
│
├── observer-pattern/                   # Behavioral Pattern
│   ├── 01-event-observer-pattern.py
│   ├── 02-observer-pattern-observable.py
│   ├── 03-observer-pattern-publisher.py
│   └── 04-advanced-observer-pattern.py
│
├── strategy-pattern/                   # Behavioral Pattern
│   └── 01-strategy-pattern.py
│
├── command-pattern/                    # Behavioral Pattern
│   └── 01-command-pattern.py
│
├── state-pattern/                      # Behavioral Pattern
│   ├── 01-state-management-pattern.py
│   └── 02-state-pattern.py
│
├── template-method-pattern/            # Behavioral Pattern
│   └── 01-template-method-pattern.py
│
├── chain-of-responsibility-pattern/    # Behavioral Pattern
│   └── 01-chain-of-responsibility-pattern.py
│
├── mediator-pattern/                   # Behavioral Pattern
│   └── 01-mediator-pattern.py
│
├── memento-pattern/                    # Behavioral Pattern
│   └── 01-memento-pattern.py
│
├── visitor-pattern/                    # Behavioral Pattern
│   └── 01-visitor-pattern.py
│
├── iterator-pattern/                   # Behavioral Pattern
│   └── 01-iterator-pattern.py
│
└── interpreter-pattern/                # Behavioral Pattern
    └── 01-interpreter-pattern.py
```

## 🎯 Pattern Selection Guide

### When to Use Each Pattern

#### 🏗️ **Creational Patterns**

**Use Singleton when:**
- ✅ Need exactly one instance (database connection, logger)
- ✅ Global access point required
- ✅ Instance creation is expensive

**Use Factory Method when:**
- ✅ Object creation logic is complex
- ✅ Need to decouple object creation from usage
- ✅ Want to centralize object creation

**Use Builder when:**
- ✅ Object construction is complex with many parameters
- ✅ Want to create different representations of the same object
- ✅ Construction process must allow different representations

#### 🏛️ **Structural Patterns**

**Use Adapter when:**
- ✅ Need to use existing class with incompatible interface
- ✅ Want to create reusable class that cooperates with unrelated classes
- ✅ Need to use several existing subclasses but impractical to adapt their interface

**Use Decorator when:**
- ✅ Want to add responsibilities to objects dynamically
- ✅ Extension by subclassing is impractical
- ✅ Need to add functionality that can be withdrawn

#### 🎭 **Behavioral Patterns**

**Use Observer when:**
- ✅ Change to one object requires changing many others
- ✅ Object should notify other objects without making assumptions about who they are
- ✅ Need loose coupling between interacting objects

**Use Strategy when:**
- ✅ Many related classes differ only in their behavior
- ✅ Need different variants of an algorithm
- ✅ Algorithm uses data that clients shouldn't know about

## 💡 Best Practices

### ✅ **Do's**
- **Start Simple**: Begin with basic patterns before combining them
- **Understand Intent**: Know why a pattern exists before using it
- **Consider Context**: Evaluate if the pattern fits your specific problem
- **Document Usage**: Clearly document which patterns you're using and why
- **Test Thoroughly**: Patterns can add complexity, so test carefully

### ❌ **Don'ts**
- **Don't Over-Engineer**: Don't use patterns just because you can
- **Don't Force Patterns**: If a simple solution works, use it
- **Don't Mix Too Many**: Combining too many patterns can create confusion
- **Don't Ignore Performance**: Some patterns have performance implications
- **Don't Skip Documentation**: Pattern usage should be well-documented

## 🔍 Real-World Applications

### **E-commerce System Example**
```python
# Combining multiple patterns in a real system
class ECommerceSystem:
    def __init__(self):
        self.logger = Logger.get_instance()          # Singleton
        self.payment_factory = PaymentFactory()     # Factory Method
        self.order_builder = OrderBuilder()         # Builder
        self.observers = []                          # Observer
        self.pricing_strategy = None                 # Strategy
```

### **Game Development Example**
```python
# Game engine using multiple design patterns
class GameEngine:
    def __init__(self):
        self.entity_factory = EntityFactory()       # Abstract Factory
        self.command_manager = CommandManager()     # Command
        self.state_machine = GameStateMachine()     # State
        self.event_system = EventSystem()           # Observer
```

## 📚 Learning Resources

### **In This Repository**
- 📖 **[Complete Tutorial](./tutorial/README.md)** - Comprehensive theory and examples
- 🔧 **Individual Pattern Implementations** - Hands-on code examples
- 🎯 **[Comprehensive Examples](./comprehensive-example/)** - Real-world applications
- 💼 **Advanced Combinations** - Multiple patterns working together

### **Recommended Reading Order**
1. **Start with [Tutorial](./tutorial/README.md)** for theoretical foundation
2. **Practice with Basic Patterns**: Singleton, Factory, Observer
3. **Move to Structural Patterns**: Adapter, Decorator, Facade
4. **Master Behavioral Patterns**: Strategy, Command, State
5. **Explore Advanced Combinations** in comprehensive examples

## 🎮 Practice Exercises

### **Beginner Exercises**
1. **Logger System**: Implement Singleton pattern for application logging
2. **Shape Factory**: Create Factory Method for different geometric shapes
3. **Event System**: Build Observer pattern for game events

### **Intermediate Exercises**
1. **Plugin System**: Combine Factory and Strategy patterns
2. **UI Components**: Use Decorator pattern for component enhancement
3. **Workflow Engine**: Implement Chain of Responsibility for request processing

### **Advanced Exercises**
1. **Game Engine**: Combine multiple patterns in a game architecture
2. **Web Framework**: Build MVC framework using various patterns
3. **Distributed System**: Design microservices using appropriate patterns

## 🚀 Getting Started

1. **Read the [Tutorial](./tutorial/README.md)** for comprehensive understanding
2. **Choose your learning path** based on your experience level
3. **Start with basic patterns** and gradually move to complex ones
4. **Practice with real examples** in each pattern directory
5. **Experiment with combinations** in comprehensive examples

## 🤝 Contributing

We welcome contributions to improve this design patterns collection:

- 🐛 **Bug fixes** in existing implementations
- 📚 **Additional examples** and use cases
- 🔧 **New pattern variations** and implementations
- 📖 **Documentation improvements** and clarifications
- 🎯 **Real-world case studies** and applications

## 📞 Support

- 🐛 **Found an issue?** Check existing implementations and documentation
- 💡 **Need clarification?** Review the comprehensive tutorial
- 🤔 **Want to discuss?** Consider the pattern's intent and applicability
- 📧 **Still stuck?** Open an issue with specific questions

---

## 🎯 Quick Pattern Reference

| Need | Pattern | Category | Complexity |
|------|---------|----------|------------|
| Single instance | Singleton | Creational | ⭐ |
| Object creation | Factory Method | Creational | ⭐⭐ |
| Interface compatibility | Adapter | Structural | ⭐⭐ |
| Add functionality | Decorator | Structural | ⭐⭐ |
| Event notifications | Observer | Behavioral | ⭐⭐ |
| Algorithm selection | Strategy | Behavioral | ⭐⭐ |
| Complex construction | Builder | Creational | ⭐⭐⭐ |
| Access control | Proxy | Structural | ⭐⭐⭐ |
| State-dependent behavior | State | Behavioral | ⭐⭐⭐ |
| Object interaction | Mediator | Behavioral | ⭐⭐⭐⭐ |

**Legend**: ⭐ = Basic, ⭐⭐ = Intermediate, ⭐⭐⭐ = Advanced, ⭐⭐⭐⭐ = Expert

---

🎨 **Master the art of software design with proven patterns!** Start your journey today and build more maintainable, flexible, and elegant code. 🚀