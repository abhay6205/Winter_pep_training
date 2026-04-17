# Day 7 - Class Methods and Advanced Inheritance

## Overview
Day 7 deepens knowledge of OOP with class methods, static methods, and advanced inheritance patterns. This day explores how to use class-level operations and create more sophisticated class hierarchies.

## Learning Objectives

- ✓ Understanding class methods (@classmethod)
- ✓ Understanding static methods (@staticmethod)
- ✓ Advanced inheritance patterns
- ✓ Method resolution order (MRO)
- ✓ Class hierarchies
- ✓ Polymorphism through inheritance

## Project Files

### class_methods.py
Demonstrates class methods and their usage:
- @classmethod decorator
- Modifying class variables
- Alternative constructors
- Class-level operations

### inheritance.py
Shows single inheritance patterns.

### inheritance1.py
Demonstrates more advanced inheritance concepts.

## Key Concepts Covered

### 1. Class Methods
Methods that operate on class data, not instance data:
```python
class Car:
    base_price = 100000  # Class variable
    
    def __init__(self, model):
        self.model = model
    
    def get_base_price(self):
        # Instance method
        print(f"Base price: {self.base_price}")
    
    @classmethod  # Decorator indicates class method
    def revise_base_price(cls, inflation_rate):
        # cls refers to the class, not instance
        cls.base_price = cls.base_price + (cls.base_price * inflation_rate)

# Usage
print(Car.base_price)  # 100000
Car.revise_base_price(0.10)  # 10% inflation
print(Car.base_price)  # 110000
```

### 2. Static Methods
Methods that don't interact with instance or class data:
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# No need for instance
result = MathUtils.add(5, 3)  # 8
result = MathUtils.multiply(5, 3)  # 15
```

### 3. Decorators
Functions that modify other functions/methods:
```python
class Car:
    base_price = 100000
    
    # @ symbol indicates a decorator
    @classmethod  # This is a decorator
    def revise_base_price(cls, inflation_rate):
        cls.base_price = cls.base_price + (cls.base_price * inflation_rate)

    @staticmethod
    def is_valid_year(year):
        return 1886 <= year <= 2100
```

### 4. Alternative Constructors with Class Methods
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_str):
        # Alternative way to create object
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)

# Normal constructor
date1 = Date(2024, 1, 15)

# Using class method constructor
date2 = Date.from_string("2024-01-15")
```

### 5. Inheritance Continued
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")  # Override

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")  # Override

# Polymorphism - same interface, different behavior
animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    animal.speak()  # Different behavior per type
```

## Topics Discussed

1. **Class vs Instance Methods**
   - Instance methods: operate on self
   - Class methods: operate on cls
   - When to use each
   - Method calls

2. **Static Methods**
   - No access to self or cls
   - Utility functions
   - When to use static methods
   - Calling static methods

3. **Decorators**
   - What are decorators
   - @classmethod decorator
   - @staticmethod decorator
   - Creating custom decorators (intro)

4. **Alternative Constructors**
   - Using class methods as constructors
   - Different initialization patterns
   - Flexible object creation
   - Factory pattern

5. **Inheritance Patterns**
   - Single inheritance
   - Multi-level inheritance
   - Multiple inheritance (intro)
   - Method resolution order

6. **Method Overriding**
   - Extending parent methods
   - Replacing parent methods
   - super() calls
   - Polymorphism

7. **Polymorphism**
   - Different types, same interface
   - Type flexibility
   - Designing extensible code

## Activities

### Activity 1: Class Methods
```python
class Car:
    base_price = 100000
    
    def __init__(self, model):
        self.model = model
    
    @classmethod
    def set_base_price(cls, new_price):
        cls.base_price = new_price

Car.set_base_price(120000)
print(Car.base_price)  # 120000
```

### Activity 2: Static Methods
```python
class Help:
    @staticmethod
    def greet(name):
        return f"Hello, {name}!"
    
    @staticmethod
    def farewell(name):
        return f"Goodbye, {name}!"

print(Help.greet("John"))
print(Help.farewell("John"))
```

### Activity 3: Inheritance with Override
```python
class Bird:
    def sound(self):
        return "Generic bird sound"

class Parrot(Bird):
    def sound(self):
        return "Squawk!"

class Sparrow(Bird):
    def sound(self):
        return "Tweet!"

for bird in [Parrot(), Sparrow()]:
    print(bird.sound())
```

### Activity 4: Class Method Constructor
```python
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    @classmethod
    def from_seconds(cls, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return cls(hours, minutes)

t1 = Time(2, 30)
t2 = Time.from_seconds(9000)  # 2.5 hours
```

## Code Examples

### Car with Class Methods
```python
class Car:
    base_price = 100000  # Class variable
    
    def __init__(self, model):
        self.model = model
    
    def what_base_price(self):
        print(f"The base price of the car is {self.base_price}")
    
    @classmethod
    def revise_base_price(cls, inflation_rate):
        cls.base_price = cls.base_price + (cls.base_price * inflation_rate)

# Usage
Car.revise_base_price(0.10)  # Increase by 10%
print(f"Revised base price is {Car.base_price}")

Car.revise_base_price(0.07)  # Increase by 7%
print(f"Revised base price is {Car.base_price}")
```

### Animal Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks: Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: Meow!")

# Create instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Buddy barks: Woof! Woof!
cat.speak()  # Whiskers meows: Meow!
```

### Multi-Level Inheritance
```python
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def start(self):
        print(f"{self.name} is starting")

class Car(Vehicle):
    def __init__(self, name, doors):
        super().__init__(name)
        self.doors = doors

class ElectricCar(Car):
    def __init__(self, name, doors, battery_capacity):
        super().__init__(name, doors)
        self.battery = battery_capacity

# Usage
tesla = ElectricCar("Tesla", 4, 100)
tesla.start()  # Inherited from Vehicle
```

## Method Resolution Order (MRO)

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Check MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

## Common Mistakes to Avoid

1. **Missing @ Symbol in Decorators**
   ```python
   # Wrong - forgot @
   classmethod
   def revise_price(cls):
       pass
   
   # Correct
   @classmethod
   def revise_price(cls):
       pass
   ```

2. **Using self in Class Methods**
   ```python
   # Wrong - cls not self
   @classmethod
   def revise(self):
       self.base_price = 100  # ERROR
   
   # Correct - use cls
   @classmethod
   def revise(cls):
       cls.base_price = 100
   ```

3. **Not Respecting Polymorphism**
   ```python
   # Poor design - type checking
   if type(animal) == Dog:
       animal.bark()
   
   # Better - polymorphism
   animal.speak()  # Works for all types
   ```

## Setup and Execution

1. Navigate to Day7 folder:
   ```bash
   cd Day7
   ```

2. Run examples:
   ```bash
   python class_methods.py
   python inheritance.py
   python inheritance1.py
   ```

## Next Steps

After Day 7, you should:
- Understand class and static methods
- Master inheritance patterns
- Understand polymorphism
- Be ready for advanced Python (Day 8)

## Concepts to Review

- Class methods and @classmethod
- Static methods and @staticmethod
- Method overriding
- Inheritance hierarchies
- Polymorphism principles
- MRO (Method Resolution Order)

## Key Takeaways

1. Class methods operate on class data
2. Static methods are utilities
3. Decorators modify method behavior
4. Polymorphism enables flexibility
5. Inheritance creates hierarchies
6. MRO determines method lookup order

## Additional Practice

Try these exercises:
1. Create a calculator with static methods
2. Create a class hierarchy for shapes
3. Implement polymorphic behavior
4. Create alternative constructors with class methods
5. Design a game with inheritance
6. Implement a factory pattern with class methods

## Technologies

- **Python 3.x**: Programming language
- **Text Editor**: Code writing tool
- **Terminal**: Code execution

## Notes

Class methods and decorators are powerful tools that enable writing clean, professional Python code. They're used extensively in frameworks like Django. Master these concepts for advanced Python development.