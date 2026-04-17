# Day 5 - Exception Handling and Error Management

## Overview
Day 5 focuses on handling errors gracefully in Python programs. This day covers exception handling using try-except blocks, raising custom exceptions, and implementing robust error management strategies that make programs more reliable and user-friendly.

## Learning Objectives

- ✓ Understanding exception types
- ✓ Using try-except blocks
- ✓ Handling multiple exceptions
- ✓ Raising custom exceptions
- ✓ Using finally blocks
- ✓ Writing error-resistant code

## Project Files

### exception.py
Demonstrates exception handling patterns:
- Try-except blocks
- Multiple exception handling
- Raising exceptions
- Finally blocks
- Custom exception classes

### practice.py
Practice exercises for exception handling:
- Common exception scenarios
- Error handling strategies
- Building robust functions

## Key Concepts Covered

### 1. Try-Except Blocks
Handle errors gracefully:
```python
try:
    # Code that might raise an exception
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"You are {age} years old")
except ValueError:
    print("Invalid age entered")
except TypeError:
    print("Wrong data type")
```

### 2. Multiple Exception Handling
Catch different exception types:
```python
try:
    value = int("abc")  # ValueError
    result = 10 / 0     # ZeroDivisionError
except ValueError as ve:
    print(f"Value Error: {ve}")
except ZeroDivisionError as zde:
    print(f"Cannot divide by zero")
except Exception as e:
    print(f"Unknown error: {e}")
```

### 3. Finally Block
Code that always executes:
```python
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if 'file' in locals():
        file.close()  # Always close file
```

### 4. Raising Exceptions
Create custom errors:
```python
def validate_age(age):
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation Error: {e}")
```

### 5. Custom Exceptions
Define your own exception classes:
```python
class DobException(Exception):
    """Custom exception for date of birth validation"""
    pass

def check_dob(age):
    if age <= 10 or age >= 20:  # Custom validation
        raise DobException("Age is outside valid range")
    return True

try:
    check_dob(25)
except DobException as e:
    print(f"DOB Exception: {e}")
```

### 6. Common Exceptions
Types of errors you'll encounter:
```python
# ZeroDivisionError
result = 10 / 0  # Error

# ValueError
age = int("not a number")  # Error

# TypeError
result = "hello" + 5  # Error

# IndexError
my_list = [1, 2, 3]
print(my_list[10])  # Error

# KeyError
my_dict = {"name": "John"}
print(my_dict["age"])  # Error

# FileNotFoundError
file = open("nonexistent.txt")  # Error

# AttributeError
text = "hello"
text.unknown_method()  # Error
```

## Topics Discussed

1. **Exception Handling Basics**
   - What are exceptions
   - Try-except structure
   - Exception objects
   - Catching specific exceptions

2. **Multiple Exception Handling**
   - Different exception types
   - Exception hierarchy
   - Catching parent class
   - Exception as clause

3. **Finally Blocks**
   - Code that always runs
   - Resource cleanup
   - File handling
   - Connection closing

4. **Raising Exceptions**
   - Raising built-in exceptions
   - Custom exception messages
   - When to raise exceptions
   - Exception propagation

5. **Custom Exceptions**
   - Creating exception classes
   - Inheritance from Exception
   - Adding custom methods
   - Documentation

6. **Error-Resistant Programming**
   - Input validation
   - Graceful degradation
   - User-friendly messages
   - Logging errors

## Activities

### Activity 1: Basic Exception Handling
```python
try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 150:
        raise ValueError("Invalid age")
    print(f"Valid age: {age}")
except ValueError:
    print("Please enter a valid age")
```

### Activity 2: Multiple Exceptions
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Activity 3: Finally Block
```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup completed")
```

### Activity 4: Custom Exception
```python
class DobException(Exception):
    pass

def check_dob(age):
    if age <= 10 | age >= 20:
        raise DobException("Age not in valid range")
    return True

try:
    check_dob(5)
except DobException:
    print("The age is not within the range")
```

### Activity 5: Input Validation
```python
def get_valid_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

number = get_valid_number()
print(f"You entered: {number}")
```

## Code Examples

### File Handling with Exception Management
```python
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except IOError:
        print(f"Error: Cannot read file '{filename}'")
        return None

content = read_file("data.txt")
```

### Robust Calculator
```python
def divide(a, b):
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be a number")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be a number")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None

result = divide(10, 2)      # 5.0
result = divide(10, 0)      # Error message
result = divide("10", 2)    # Error message
```

### Custom Exception Example
```python
class InsufficientFunds(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds. Balance: {balance}, Requested: {amount}"
        super().__init__(message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFunds as e:
    print(f"Withdrawal error: {e}")
```

## Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── AttributeError
    ├── IOError
    │   └── FileNotFoundError
    └── ... (many more)
```

## Common Mistakes to Avoid

1. **Catching Too Broad**
   ```python
   # Too broad - catches all exceptions
   try:
       age = int(input("Enter age: "))
   except:  # AVOID THIS
       print("Error")
   
   # Better - catch specific exception
   try:
       age = int(input("Enter age: "))
   except ValueError:
       print("Invalid number")
   ```

2. **Not Using Finally**
   ```python
   # Resource might not be released
   file = open("data.txt")
   data = file.read()
   file.close()  # What if read() fails?
   
   # Better - use finally
   try:
       file = open("data.txt")
       data = file.read()
   finally:
       file.close()
   ```

3. **Ignoring Exceptions**
   ```python
   # Silent failure - bad practice
   try:
       result = dangerous_function()
   except:
       pass  # AVOID - ignores all errors
   ```

4. **Wrong Exception Type**
   ```python
   # Catching wrong exception type
   try:
       age = int("abc")  # Raises ValueError
   except KeyError:  # Won't catch ValueError
       print("Error")
   ```

## Practical Applications

### Real-world scenarios:
- User input validation
- File handling
- Network operations
- Database queries
- API calls
- Resource management
- Error logging

## Setup and Execution

1. Navigate to Day5 folder:
   ```bash
   cd Day5
   ```

2. Run examples:
   ```bash
   python exception.py
   python practice.py
   ```

## Next Steps

After Day 5, you should:
- Handle exceptions properly
- Write error-resistant code
- Understand exception hierarchy
- Be ready for OOP (Day 6)

## Concepts to Review

- Try-except blocks
- Multiple exception handling
- Finally blocks
- Raising exceptions
- Custom exceptions
- Exception best practices

## Key Takeaways

1. Exceptions are errors that can be handled
2. Try-except prevents program crashes
3. Finally block ensures cleanup
4. Catch specific exceptions, not all
5. Raise exceptions for invalid conditions
6. Log and handle errors gracefully

## Additional Practice

Try these exercises:
1. Create a function with full exception handling
2. Build a simple calculator with error handling
3. Write a file reader with error handling
4. Create custom exceptions for business logic
5. Add logging to your exception handlers
6. Build a user input validator with exceptions

## Technologies

- **Python 3.x**: Programming language
- **Text Editor**: Code writing tool
- **Terminal**: Code execution

## Notes

Exception handling is crucial for writing professional, robust applications. Every function should handle potential errors appropriately. Practice different exception scenarios to build this important skill.