# Polymorphism 🎭

Master polymorphism in Python - the ability for objects of different types to be treated as instances of the same type through a common interface.

## 🎯 Learning Objectives

- Understand polymorphism and operator overloading
- Master magic methods (`__add__`, `__sub__`, `__mul__`, etc.)
- Implement mathematical operations for custom classes
- Learn method overriding for different behaviors
- Apply polymorphism in real-world mathematical scenarios
- Work with callable objects using `__call__`

## 📚 Exercises

### Intermediate Level (🟡)

1. **[Employee Polymorphism](./01-employee-polymorphism.py)** - Basic Method Implementation
   - Simple class design with salary calculations
   - Percentage-based operations
   - Method implementation for state modification
   - Testing with multiple operations

2. **[Vector Operator Overloading](./02-vector-operator-overloading.py)** - Mathematical Operations
   - Implementing `__add__`, `__sub__`, and `__mul__` magic methods
   - Vector addition and subtraction operations
   - Dot product calculations
   - String representation with `__str__`
   - Mathematical accuracy in programming

3. **[Matrix Operator Overloading](./03-matrix-operator-overloading.py)** - Advanced Mathematics
   - Matrix addition with corresponding elements
   - Matrix multiplication algorithms
   - Working with 2D data structures
   - Using `zip()` for element-wise operations
   - Matrix transposition techniques

4. **[Polynomial Operator Overloading](./04-polynomial-operator-overloading.py)** - Callable Objects
   - Polynomial addition and subtraction
   - Implementing `__call__` for function-like behavior
   - Coefficient-based mathematical operations
   - Polynomial evaluation at specific values
   - Mathematical notation in string representation

### Advanced Level (🟠)

5. **[Advanced Vector Operations](./05-advanced-vector-operations.py)** - Robust Implementation
   - Enhanced vector operations with validation
   - Error handling for incompatible operations
   - Encapsulation with length checking
   - Comprehensive operator overloading
   - Professional-grade mathematical library design

## 🔑 Key Concepts

### Basic Operator Overloading
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):  # Dot product
        return self.x * other.x + self.y * other.y
```

### String Representation
```python
class Vector:
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

### Callable Objects
```python
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

# Usage: p = Polynomial([1, 2, 3])  # 1 + 2x + 3x²
# result = p(2)  # Evaluate at x=2
```

### Matrix Operations
```python
class Matrix:
    def __add__(self, other):
        result = []
        for row1, row2 in zip(self.data, other.data):
            result.append([x + y for x, y in zip(row1, row2)])
        return Matrix(result)
    
    def __mul__(self, other):  # Matrix multiplication
        result = []
        for row in self.data:
            new_row = []
            for col in zip(*other.data):  # Transpose columns
                new_row.append(sum(x * y for x, y in zip(row, col)))
            result.append(new_row)
        return Matrix(result)
```

## 🎓 Progressive Learning Path

### Start Here (Foundation)
1. **Employee Polymorphism** - Learn basic method implementation and state modification
2. **Vector Operator Overloading** - Understand magic methods and mathematical operations

### Build Mathematical Understanding
3. **Matrix Operator Overloading** - Master 2D data operations and complex algorithms
4. **Polynomial Operator Overloading** - Learn callable objects and mathematical evaluation

### Advanced Implementation
5. **Advanced Vector Operations** - Implement robust, production-ready mathematical classes

## 🧮 Magic Methods Reference

### Arithmetic Operations
- `__add__(self, other)` - Addition (`+`)
- `__sub__(self, other)` - Subtraction (`-`)
- `__mul__(self, other)` - Multiplication (`*`)
- `__truediv__(self, other)` - Division (`/`)
- `__pow__(self, other)` - Exponentiation (`**`)

### Comparison Operations
- `__eq__(self, other)` - Equal (`==`)
- `__lt__(self, other)` - Less than (`<`)
- `__gt__(self, other)` - Greater than (`>`)

### String Representation
- `__str__(self)` - Human-readable string
- `__repr__(self)` - Developer-friendly representation

### Special Methods
- `__call__(self, *args)` - Make object callable like a function
- `__len__(self)` - Length (`len()`)
- `__getitem__(self, key)` - Indexing (`obj[key]`)

## 💡 Best Practices

### ✅ Do This
- **Return new objects** from arithmetic operations (immutability)
- **Implement `__str__` and `__repr__`** for debugging and display
- **Use meaningful variable names** in mathematical operations
- **Validate inputs** in advanced implementations
- **Follow mathematical conventions** (e.g., dot product returns scalar)

### ❌ Avoid This
- **Don't modify self** in arithmetic operations - return new objects
- **Don't implement operations that don't make sense** mathematically
- **Don't forget error handling** for incompatible operations
- **Don't mix up `__mul__` meanings** (scalar vs. dot product vs. matrix multiplication)

## 🔍 Common Patterns

### Immutable Mathematical Objects
```python
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)  # New object
```

### Validation in Operations
```python
class Vector:
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have same length")
        return Vector([a + b for a, b in zip(self.components, other.components)])
```

### Fluent Interface
```python
class Calculator:
    def __init__(self, value=0):
        self.value = value
    
    def add(self, x):
        return Calculator(self.value + x)
    
    def multiply(self, x):
        return Calculator(self.value * x)

# Usage: result = Calculator(5).add(3).multiply(2)  # Chaining
```

## 🚀 Getting Started

1. **Start with [Employee Polymorphism](./01-employee-polymorphism.py)** - Master basic method implementation
2. **Progress through mathematical examples** - Build understanding gradually
3. **Experiment with modifications** - Try implementing additional operations
4. **Focus on mathematical accuracy** - Understand the math behind the code

## 🎯 Learning Tips

- **Understand the mathematics first** - Know how operations work before coding
- **Test with simple examples** - Use easy numbers to verify correctness
- **Draw diagrams** - Visualize vectors, matrices, and polynomials
- **Use interactive Python** - Test operations step by step
- **Read error messages carefully** - They often indicate mathematical issues

## 🧪 Practice Challenges

After completing the exercises, try these extensions:

1. **Add more vector operations** - Cross product, magnitude, normalization
2. **Implement complex numbers** - With real and imaginary parts
3. **Create a fraction class** - With proper arithmetic operations
4. **Build a polynomial calculator** - With derivative and integral operations
5. **Design a matrix library** - With determinant, inverse, and eigenvalues

---

Ready to master polymorphism? Start with [Employee Polymorphism](./01-employee-polymorphism.py)! 🎯