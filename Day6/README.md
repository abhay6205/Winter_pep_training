# Day 6 - Classes and Object-Oriented Programming

## Overview
Day 6 introduces Object-Oriented Programming (OOP) in Python. This day covers classes, objects, instance variables, class variables, and the fundamental concepts of OOP that enable writing modular, reusable, and maintainable code.

## Learning Objectives

- ✓ Understanding classes and objects
- ✓ Creating instance variables and methods
- ✓ Understanding class variables
- ✓ Access modifiers (public, protected)
- ✓ Encapsulation principles
- ✓ Introduction to inheritance

## Project Files

### class_type.py
Explores different access levels and encapsulation:
- Public class variables (no prefix)
- Protected variables (single underscore _)
- Name mangling for private variables (double underscore __)
- Inheritance with protected variables

### dataclass.py
Working with classes and their structure.

### methods.py
Demonstrates different types of methods in classes.

## Key Concepts Covered

### 1. Basic Class Definition
```python
class Car:
    def __init__(self, window, doors, engine_type):
        self.window = window      # Instance variable
        self.doors = doors        # Instance variable
        self.engine_type = engine_type  # Instance variable
    
    def display_info(self):
        print(f"Car: {self.doors} doors, {self.engine_type}")

# Creating object
audi1 = Car(6, 4, 'Diesel')
audi1.display_info()
```

### 2. Access Modifiers

#### Public Variables (No Prefix)
```python
class Car:
    def __init__(self, window, doors, engine_type):
        self.window = window      # Public
        self.doors = doors        # Public
        self.engine_type = engine_type  # Public

audi1 = Car(6, 4, 'Diesel')
audi1.window = 7  # Can be modified from outside
print(audi1.window)  # 7
```

#### Protected Variables (Single Underscore)
```python
class Car:
    def __init__(self, window, doors, engine_type):
        self._window = window     # Protected
        self._doors = doors       # Protected
        self._engine_type = engine_type  # Protected

# Still accessible but indicates "internal use"
car = Car(6, 4, 'Diesel')
car._window = 7  # Works but not recommended
```

#### Private Variables (Double Underscore - Name Mangling)
```python
class Car:
    def __init__(self, window):
        self.__window = window    # Private

car = Car(6)
# car.__window = 7  # ERROR - not accessible directly
# Access through name mangling:
car._Car__window = 7  # Works but very bad practice
```

### 3. Instance vs Class Variables
```python
class Car:
    base_price = 100000  # Class variable (shared by all instances)
    
    def __init__(self, windows, doors):
        self.windows = windows   # Instance variable (unique per object)
        self.doors = doors       # Instance variable (unique per object)

# Class variable is shared
print(Car.base_price)  # 100000
car1 = Car(4, 5)
car2 = Car(2, 3)
print(car1.base_price)  # 100000
print(car2.base_price)  # 100000
```

### 4. Methods and Self
```python
class Car:
    def __init__(self, model):
        self.model = model
    
    # Instance method - takes self
    def display_model(self):
        print(f"Car model: {self.model}")
    
    # Another instance method
    def modify_model(self, new_model):
        self.model = new_model

car = Car("Audi")
car.display_model()  # Car model: Audi
car.modify_model("BMW")
car.display_model()  # Car model: BMW
```

### 5. Inheritance Basics
```python
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Vehicle: {self.name}")

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, name, doors):
        super().__init__(name)  # Call parent __init__
        self.doors = doors
    
    def display(self):
        super().display()  # Call parent method
        print(f"Doors: {self.doors}")

car = Car("Audi", 4)
car.display()  # Calls overridden method
```

## Topics Discussed

1. **Classes and Objects**
   - Class definition
   - Creating objects
   - __init__ constructor
   - Instance creation

2. **Instance Variables**
   - Variables unique to each object
   - Defined in __init__
   - Accessing via self
   - Modifying instance variables

3. **Methods**
   - Instance methods
   - Method parameters
   - Return values
   - Calling other methods

4. **Class Variables**
   - Variables shared by all instances
   - Accessing via class or instance
   - Modifying class variables
   - When to use class variables

5. **Access Modifiers**
   - Public (no prefix)
   - Protected (_ prefix)
   - Private (__ prefix - name mangling)
   - Conventions vs enforcement

6. **Encapsulation**
   - Data hiding
   - Getter and setter methods
   - Property decorators
   - Interface design

7. **Inheritance**
   - Extending classes
   - super() function
   - Method overriding
   - Parent-child relationships

## Activities

### Activity 1: Creating a Simple Class
```python
class Car:
    def __init__(self, window, doors, engine_type):
        self.window = window
        self.doors = doors
        self.engine_type = engine_type

audi1 = Car(6, 4, 'Diesel')
print(audi1.doors)  # 4
audi1.window = 7
print(audi1.window)  # 7
```

### Activity 2: Protected Variables
```python
class Car:
    def __init__(self, window, doors, engine_type):
        self._window = window
        self._doors = doors
        self._engine_type = engine_type

class Truck(Car):
    def __init__(self, window, doors, engine_type, horsepower):
        super().__init__(window, doors, engine_type)
        self.horsepower = horsepower
        print(self._Car__window)  # Name mangling access

truck1 = Truck(8, 2, 'Diesel', 500)
```

### Activity 3: Methods and Self
```python
class Car:
    def __init__(self, model):
        self.model = model
    
    def get_model(self):
        return self.model
    
    def set_model(self, new_model):
        self.model = new_model

car = Car("Audi")
print(car.get_model())
car.set_model("BMW")
print(car.get_model())
```

### Activity 4: Class Variables
```python
class Car:
    base_price = 100000
    
    def __init__(self, model):
        self.model = model

car1 = Car("Audi")
print(Car.base_price)
print(car1.base_price)
```

## Code Examples

### Complete Car Class
```python
class Car:
    # Class variable
    total_cars_made = 0
    
    def __init__(self, model, price):
        # Instance variables
        self.model = model
        self.price = price
        Car.total_cars_made += 1
    
    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        if new_price > 0:
            self.price = new_price
    
    def display_info(self):
        print(f"{self.model}: ${self.price}")

# Usage
audi = Car("Audi A4", 50000)
bmw = Car("BMW 3 Series", 55000)

audi.display_info()
bmw.display_info()
print(f"Total cars: {Car.total_cars_made}")
```

### Inheritance Example
```python
class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def display(self):
        print(f"{self.name}: {self.color}")

class Car(Vehicle):
    def __init__(self, name, color, doors):
        super().__init__(name, color)
        self.doors = doors
    
    def display(self):
        super().display()
        print(f"Doors: {self.doors}")

car = Car("Audi", "Red", 4)
car.display()
```

## Common Mistakes to Avoid

1. **Forgetting self Parameter**
   ```python
   # Wrong
   class Car:
       def display(self):  # Missing self
           print(self.model)
   
   # Correct
   class Car:
       def display(self):
           print(self.model)
   ```

2. **Accessing Class Variable Incorrectly**
   ```python
   # Can be confusing
   class Circle:
       pi = 3.14
       
       def __init__(self, radius):
           self.radius = radius
   
   circle = Circle(5)
   print(circle.pi)  # Works but unusual
   print(Circle.pi)  # Better - more explicit
   ```

3. **Not Calling super().__init__()**
   ```python
   # Incomplete initialization
   class Car(Vehicle):
       def __init__(self, name):
           # Missing super().__init__()
           self.name = name
   ```

## OOP Principles

### Encapsulation
Hide internal details, expose necessary interface:
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Protected
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
```

## Setup and Execution

1. Navigate to Day6 folder:
   ```bash
   cd Day6
   ```

2. Run examples:
   ```bash
   python class_type.py
   python dataclass.py
   python methods.py
   ```

## Next Steps

After Day 6, you should:
- Understand OOP fundamentals
- Create and use classes
- Understand inheritance basics
- Be ready for more advanced OOP (Day 7)

## Concepts to Review

- Classes and objects
- Instance variables and methods
- Class variables
- Access modifiers
- Inheritance
- Encapsulation

## Key Takeaways

1. Classes group data and behavior together
2. Objects are instances of classes
3. Instance variables are unique per object
4. Class variables are shared by all objects
5. Methods operate on instance data
6. Inheritance allows code reuse
7. Encapsulation hides internal details

## Additional Practice

Try these exercises:
1. Create a Student class with attributes and methods
2. Create a BankAccount class with deposit/withdraw
3. Create an Animal parent class and extend it
4. Create a Book class with validation
5. Implement getters and setters
6. Create a Rectangle class with area calculation

## Technologies

- **Python 3.x**: Programming language
- **Text Editor**: Code writing tool
- **Terminal**: Code execution

## Notes

Object-Oriented Programming is a paradigm shift in thinking about code. Don't worry if it takes time to fully grasp. The more you practice creating classes, the more natural it becomes. OOP is essential for professional software development.