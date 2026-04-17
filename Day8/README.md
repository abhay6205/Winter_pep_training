# Day 8 - Advanced Classes and Design Patterns

## Overview
Day 8 covers advanced class concepts and introduces important design patterns in Python. This day explores assertion-based programming, advanced encapsulation, and patterns for writing robust, maintainable object-oriented code.

## Learning Objectives

- ✓ Using assertions for debugging and testing
- ✓ Advanced encapsulation techniques
- ✓ Property decorators
- ✓ Special methods (__str__, __repr__, etc.)
- ✓ Iterators and generators (intro)
- ✓ Writing robust classes

## Project Files

### class.py
Demonstrates advanced class features and design patterns:
- Class definition and structure
- Methods and attributes
- Special methods
- Property decorators

### assert.py
Shows assertion-based programming:
- Assert statements for testing
- Assertions in development
- Contract-based programming

## Key Concepts Covered

### 1. Assertions
Test conditions during development:
```python
# Assert statement
assert condition, "Error message"

# Examples
age = 25
assert age > 0, "Age must be positive"
assert age < 150, "Age seems unrealistic"

# In functions
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

# With classes
class Person:
    def __init__(self, age):
        assert age >= 0, "Age cannot be negative"
        self.age = age
```

### 2. Special Methods
Methods with double underscores that Python uses internally:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        # User-friendly string representation
        return f"Person: {self.name} ({self.age} years old)"
    
    def __repr__(self):
        # Developer-friendly representation
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        # Return length (for len() function)
        return self.age
    
    def __eq__(self, other):
        # Equality comparison (==)
        return self.age == other.age
    
    def __lt__(self, other):
        # Less than comparison (<)
        return self.age < other.age

# Usage
p1 = Person("John", 25)
print(str(p1))     # __str__
print(repr(p1))    # __repr__
print(len(p1))     # __len__
print(p1 == Person("Jane", 25))  # __eq__
```

### 3. Property Decorators
Create getter/setter methods that look like attributes:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Protected attribute
    
    @property
    def radius(self):
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter with validation"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        """Computed property"""
        return 3.14159 * self._radius ** 2

# Usage
circle = Circle(5)
print(circle.radius)   # Uses getter
circle.radius = 10     # Uses setter
print(circle.area)     # Computed property
```

### 4. Duck Typing
If it walks like a duck and quacks like a duck, it's a duck:
```python
class Duck:
    def quack(self):
        print("Quack quack")
    
    def move(self):
        print("Walks like a duck")

class Person:
    def quack(self):
        print("I'm imitating a duck")
    
    def move(self):
        print("I'm walking")

def make_it_quack_and_move(creature):
    # Doesn't care about type, only that methods exist
    creature.quack()
    creature.move()

duck = Duck()
person = Person()

make_it_quack_and_move(duck)
make_it_quack_and_move(person)  # Works even if not a Duck!
```

### 5. Abstract Base Classes
Define interfaces that subclasses must implement:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
    def move(self):
        return "Runs on four legs"

# This works
dog = Dog()

# This would fail
# animal = Animal()  # TypeError: Can't instantiate abstract class
```

## Topics Discussed

1. **Assertions in Development**
   - Testing conditions
   - Debugging aids
   - Contract programming
   - When assertions fail

2. **Special Methods (Dunder Methods)**
   - __init__ constructor
   - __str__ and __repr__
   - __len__, __getitem__, __setitem__
   - __add__, __sub__ (operator overloading)
   - __eq__, __lt__, __gt__ (comparisons)

3. **Property Decorators**
   - Creating properties
   - Getters and setters
   - Validation in setters
   - Computed properties
   - Read-only properties

4. **Operator Overloading**
   - Defining custom behavior for operators
   - Mathematical operations
   - Comparison operations

5. **Duck Typing**
   - Pythonic approach
   - Interface-based programming
   - Flexibility in design

6. **Abstract Base Classes**
   - Defining interfaces
   - Enforcing implementation
   - Multiple inheritance with ABC

## Activities

### Activity 1: Using Assertions
```python
def validate_age(age):
    assert age > 0, "Age must be positive"
    assert age < 150, "Age seems unrealistic"
    return True

validate_age(25)  # OK
validate_age(-5)  # AssertionError
validate_age(200)  # AssertionError
```

### Activity 2: Special Methods
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return self.title == other.title

book1 = Book("Python 101", "John", 300)
print(str(book1))
print(len(book1))
```

### Activity 3: Property Decorators
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(0)
print(temp.celsius)     # 0
print(temp.fahrenheit)  # 32
```

### Activity 4: Duck Typing
```python
class Guitar:
    def play(self):
        print("Plays guitar music")

class Violin:
    def play(self):
        print("Plays violin music")

def perform_concert(instrument):
    instrument.play()

guitar = Guitar()
violin = Violin()
perform_concert(guitar)
perform_concert(violin)  # Works even though different type
```

## Code Examples

### Complete Class with Special Methods
```python
class Vector:
    def __init__(self, x, y):
        assert isinstance(x, (int, float)), "x must be a number"
        assert isinstance(y, (int, float)), "y must be a number"
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2
print(v3)  # Vector(4, 6)
print(len(v3))  # 7 (distance from origin)
```

### Using Properties
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
    
    @property
    def is_rich(self):
        return self._balance > 1000000

# Usage
account = BankAccount(500000)
print(account.balance)  # 500000
account.balance = 600000  # Uses setter
print(account.is_rich)  # False
```

## Common Mistakes to Avoid

1. **Abusing Assertions**
   ```python
   # Wrong - assertions can be disabled with -O flag
   assert user_input > 0, "Invalid input"  # Not for production validation
   
   # Better - use if statement for validation
   if user_input <= 0:
       raise ValueError("Invalid input")
   ```

2. **Not Using Property Decorators**
   ```python
   # Old way
   def get_radius(self):
       return self._radius
   
   # Better - use @property
   @property
   def radius(self):
       return self._radius
   ```

3. **Forgetting __repr__**
   ```python
   # __repr__ helps with debugging
   def __repr__(self):
       return f"{self.__class__.__name__}({self.x}, {self.y})"
   ```

## Real-World Applications

### When to use different concepts:
- **Assertions**: Development and debugging
- **Special Methods**: Making classes behave like built-in types
- **Properties**: Controlling access to attributes
- **Duck Typing**: Writing flexible, reusable code
- **Abstract Classes**: Defining interfaces

## Setup and Execution

1. Navigate to Day8 folder:
   ```bash
   cd Day8
   ```

2. Run examples:
   ```bash
   python class.py
   python assert.py
   ```

## Next Steps

After Day 8, you should:
- Understand advanced class features
- Use assertions effectively
- Design robust classes
- Be ready for Django basics (Day 9)

## Concepts to Review

- Assertions and testing
- Special methods/dunder methods
- Property decorators
- Operator overloading
- Duck typing
- Abstract base classes

## Key Takeaways

1. Assertions help find bugs early
2. Special methods customize class behavior
3. Properties look like attributes
4. Duck typing favors flexibility
5. Abstract classes define interfaces
6. Write robust, defensive code

## Additional Practice

Try these exercises:
1. Create a class with all special methods
2. Implement property decorators with validation
3. Overload operators for a custom class
4. Create an abstract base class and implement it
5. Design a flexible system using duck typing
6. Add assertions to your existing classes

## Technologies

- **Python 3.x**: Programming language
- **abc module**: Abstract base classes
- **Text Editor**: Code writing tool

## Notes

These advanced class features bridge the gap between basic OOP and professional Python development. They're essential for writing maintainable, robust code that integrates well with Python's design philosophy.