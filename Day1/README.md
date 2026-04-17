# Day 1 - Python Basics and Introduction

## Overview
Day 1 is the introduction to Python programming fundamentals. This day focuses on basic print statements, understanding the Python environment, assessing prior knowledge, and establishing foundational programming concepts that will be built upon in subsequent days.

## Learning Objectives

- ✓ Understanding Python basics and setup
- ✓ Writing and executing Python programs
- ✓ Using print statements for output
- ✓ Understanding Python syntax
- ✓ Learning about data types
- ✓ Writing first Python programs

## Project Files

### main.py
Main entry point for the day's exercises with basic Python programs.

### hello_world.py
Classic Hello World program to demonstrate basic print functionality:
```python
print("Hello World!")
```

**Purpose**: Verify Python installation and understand basic print syntax.

### conditional.py
Demonstrates conditional statements (if/else) for decision-making:
- Using if statements
- Boolean conditions
- Comparison operators
- Logical operators

## Key Concepts Covered

### 1. Print Statement
The most basic output function in Python:
```python
print("Hello World!")
print("Welcome to Python")
```

### 2. Data Types (Introduction)
- **Strings**: Text enclosed in quotes
- **Numbers**: Integers and floats
- **Booleans**: True or False

### 3. Variables
- Variable assignment
- Naming conventions
- Variable types

### 4. Basic Operators
- Arithmetic operators (+, -, *, /)
- Comparison operators (==, !=, <, >)
- Assignment operators (=)

### 5. Comments
Using # for single-line comments

## Topics Discussed

1. **Python Introduction**
   - What is Python
   - Why learn Python
   - Python applications and use cases
   - Python community and resources

2. **Development Environment**
   - Installing Python
   - Using command line/terminal
   - Running Python scripts
   - Using IDE or text editor

3. **First Program**
   - Writing hello_world.py
   - Executing programs
   - Understanding output
   - Debugging basics

4. **Basic Syntax**
   - Print statements
   - Data types
   - Variables
   - Comments

5. **Conditional Logic** (Introduction)
   - If statements
   - Boolean values
   - Simple conditions

## Activities

### Activity 1: Print Hello World
Write and execute a program that prints "Hello World!"

### Activity 2: Print Multi-line Output
Use multiple print statements to output information:
```python
print("Name: John Doe")
print("Age: 25")
print("City: New York")
```

### Activity 3: Variables and Output
Create variables and print them:
```python
name = "John"
age = 25
print(name)
print(age)
```

### Activity 4: Basic Calculations
Perform simple arithmetic:
```python
a = 10
b = 20
print(a + b)
print(a * b)
```

### Activity 5: Conditional Statements
Write simple if/else statements:
```python
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

## Setup and Execution

1. Ensure Python 3.x is installed
2. Navigate to Day1 folder:
   ```bash
   cd Day1
   ```

3. Run hello_world.py:
   ```bash
   python hello_world.py
   ```

4. Run main.py:
   ```bash
   python main.py
   ```

5. Run conditional.py:
   ```bash
   python conditional.py
   ```

## Code Examples

### Basic Print
```python
# Output text
print("Hello, World!")

# Output multiple values
print("Welcome", "to", "Python")

# Print with variables
message = "Learning Python"
print(message)
```

### Variables and Types
```python
# String variable
name = "John Doe"

# Integer variable
age = 25

# Float variable
height = 5.9

# Boolean variable
is_student = True

# Print all
print(name, age, height, is_student)
```

### Conditional Statements
```python
# Simple if-else
score = 75
if score >= 60:
    print("Pass")
else:
    print("Fail")

# If-elif-else
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
```

## Common Mistakes to Avoid

1. **Syntax Errors**: Missing colons or incorrect indentation
   ```python
   # Wrong - no colon
   if x > 5
       print("Greater")
   
   # Correct
   if x > 5:
       print("Greater")
   ```

2. **Undefined Variables**: Using variable before assignment
   ```python
   # Wrong
   print(undefined_var)
   
   # Correct
   my_var = 10
   print(my_var)
   ```

3. **Incorrect Data Types**: Mixing types incorrectly
   ```python
   # Be careful with type operations
   age = "25"  # This is a string
   print(age + 5)  # This will cause an error
   ```

## Troubleshooting

### "Python not recognized"
- Add Python to system PATH
- Use full path to Python executable

### "SyntaxError: unexpected indent"
- Check indentation consistency
- Don't mix tabs and spaces

### "NameError: name 'variable' is not defined"
- Define variable before using it
- Check variable spelling

## Next Steps

After Day 1, you should:
- Understand Python basics
- Be comfortable with print statements
- Know how to run Python programs
- Understand variables and data types
- Be ready for loops and iterations (Day 2)

## Concepts to Review

- Python syntax
- Print statement usage
- Variable assignment
- Data types
- Conditional statements
- How to run Python files

## Key Takeaways

1. Python is a simple, readable language
2. Print statements display output
3. Variables store data
4. Conditionals control program flow
5. Comments explain code
6. Practice is essential

## Additional Practice

Try these exercises:
1. Write a program that prints your name and age
2. Create variables and swap their values
3. Write a program using at least 3 conditional statements
4. Create a simple quiz with if/else statements
5. Experiment with different data types

## Technologies

- **Python 3.x**: Programming language
- **Text Editor**: Code writing tool (VS Code, Notepad++, etc.)
- **Terminal/Command Prompt**: Code execution

## Resources

- Python Official Documentation: https://docs.python.org/3/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Interactive Python Learning: https://www.codecademy.com/learn/learn-python-3

## Notes

This is the foundation for all subsequent Python learning. Mastering the basics here means easier learning in the days ahead. Don't rush—ensure you understand each concept before moving forward.