# Day 3 - Data Structures and Collections

## Overview
Day 3 focuses on essential Python data structures that are the building blocks of most programs. This day covers lists, dictionaries, tuples, and sets with practical examples and comprehensive operations on these collections.

## Learning Objectives

- ✓ Understanding Python data structures
- ✓ Working with lists and operations
- ✓ Using dictionaries for key-value storage
- ✓ Iterating through collections
- ✓ Range and enumerate functions
- ✓ Dictionary methods and operations

## Project Files

### data_structure.py
Comprehensive exploration of Python's data structures:
- Lists: creation, modification, access
- Dictionaries: key-value pairs, access, iteration
- Tuples: immutable sequences
- Sets: unique elements
- Ranges and their usage
- Enumerate for indexed iteration

### practice.ipynb
Jupyter notebook with interactive examples and practice problems for data structures.

### swap.py
Practical example demonstrating variable swapping techniques.

## Key Concepts Covered

### 1. Lists
Ordered, mutable collections of items:
```python
# Creating lists
animals = ["cat", "dog", "bird"]

# Accessing elements
print(animals[0])  # 'cat'
print(animals[-1]) # 'bird'

# Modifying lists
animals.append("fish")
animals[0] = "tiger"
animals.remove("dog")

# List operations
print(len(animals))
print("cat" in animals)
```

### 2. Dictionaries
Key-value pair collections:
```python
# Creating dictionaries
person = {"name": "John", "age": 25, "city": "NYC"}

# Accessing values
print(person["name"])  # 'John'
print(person.get("age"))  # 25

# Modifying dictionaries
person["age"] = 26
person["email"] = "john@example.com"
person.pop("city")

# Iterating dictionaries
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")
```

### 3. Tuple
Immutable sequences:
```python
# Creating tuples
coordinates = (10, 20)
single_item = (5,)  # Note the comma

# Accessing elements
print(coordinates[0])  # 10

# Cannot modify - immutable
# coordinates[0] = 15  # This will cause an error

# Unpacking
x, y = coordinates
```

### 4. Sets
Unique, unordered collections:
```python
# Creating sets
numbers = {1, 2, 3, 3, 2, 1}  # Duplicates removed
print(numbers)  # {1, 2, 3}

# Set operations
numbers.add(4)
numbers.remove(2)

# Set operations (union, intersection, etc.)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # {3} - intersection
print(set1 | set2)  # {1, 2, 3, 4, 5} - union
```

### 5. Range Function
Generate sequences of numbers:
```python
# Range examples
range(5)        # 0, 1, 2, 3, 4
range(2, 5)     # 2, 3, 4
range(0, 10, 2) # 0, 2, 4, 6, 8

# Using in loops
for i in range(5):
    print(i)  # 0 to 4
```

### 6. Enumerate Function
Get both index and value during iteration:
```python
friends = ["Abhay", "Bipin", "Sunil"]

# Without enumerate
for index in range(len(friends)):
    print(f"Index {index}: {friends[index]}")

# With enumerate (cleaner)
for index, value in enumerate(friends):
    print(f"Index {index}: {value}")
```

## Topics Discussed

1. **Lists and List Operations**
   - Creating and modifying lists
   - Accessing elements by index
   - List methods (append, remove, insert, etc.)
   - List comprehension basics
   - Slicing lists

2. **Dictionaries**
   - Dictionary structure and syntax
   - Accessing values by key
   - Adding and removing keys
   - Dictionary methods (keys, values, items)
   - Nested dictionaries
   - Iterating through dictionaries

3. **Tuples**
   - Immutable sequences
   - When to use tuples
   - Tuple unpacking
   - Single-element tuples
   - Returning multiple values

4. **Sets**
   - Unique elements
   - Set operations (union, intersection, difference)
   - Set methods
   - Using sets to remove duplicates

5. **Iteration and Indexing**
   - Range function usage
   - Enumerate function
   - Index-based access
   - Iteration patterns
   - Half-open intervals

6. **Nested Structures**
   - Lists of dictionaries
   - Dictionaries of lists
   - Nested access patterns

## Activities

### Activity 1: List Operations
```python
# Create and modify lists
animals = ["cat", "dog", "bird"]
animals.append("fish")
animals[0] = "tiger"
print(animals)
```

### Activity 2: Dictionary Exploration
```python
# Create and access dictionary
my_dict = {"name": "Abhay", "cash": 5.5}

# Iterate through keys
for key in my_dict:
    print(key)

# Iterate through values
for value in my_dict.values():
    print(value)

# Iterate through both
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

### Activity 3: Range Usage
```python
# Different range patterns
print(list(range(3)))      # [0, 1, 2]
print(list(range(3, 9)))   # [3, 4, 5, 6, 7, 8]
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]

# Keep in mind: end - start = length
print(list(range(3)) + list(range(3, 9)))  # No overlap
```

### Activity 4: Enumerate
```python
friends = ["Abhay", "Sunil", "Bipin"]
for index, value in enumerate(friends):
    print(f"index {index} has value {value}")
```

### Activity 5: Nested Structures
```python
# List of dictionaries
students = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 21},
    {"name": "Bob", "age": 20}
]

# Accessing nested data
print(students[0]["name"])  # 'John'

# Iterating through nested structure
for student in students:
    print(f"{student['name']} is {student['age']} years old")
```

## Code Examples

### Working with Lists
```python
# List creation and modification
numbers = [10, 20, 30, 40]
numbers.append(50)           # Add at end
numbers.insert(0, 5)         # Add at specific index
numbers.remove(20)           # Remove specific value
popped = numbers.pop()       # Remove and return last

print(numbers)     # [5, 10, 30, 40]
print(popped)      # 50
```

### Working with Dictionaries
```python
# Dictionary with various types
person = {
    "name": "John",
    "age": 25,
    "hobbies": ["reading", "coding"],
    "address": {"city": "NYC", "zip": "10001"}
}

# Access values
print(person["name"])
print(person.get("age", "N/A"))

# Update dictionary
person["age"] = 26
person["email"] = "john@example.com"

# Remove items
if "address" in person:
    del person["address"]
```

### Iterating with Enumerate
```python
items = ["apple", "banana", "cherry"]

# Using enumerate
for idx, item in enumerate(items):
    print(f"{idx}. {item}")

# Output:
# 0. apple
# 1. banana
# 2. cherry
```

## Common Mistakes to Avoid

1. **Confusing List and Dictionary Access**
   ```python
   # List uses index
   my_list = [10, 20, 30]
   print(my_list[0])  # 10 - CORRECT
   
   # Dictionary uses key
   my_dict = {"a": 10, "b": 20}
   print(my_dict["a"])  # 10 - CORRECT
   ```

2. **Mutating While Iterating**
   ```python
   # Risky - modifying while iterating
   for item in my_list:
       if item == 2:
           my_list.remove(item)  # Can cause issues
   
   # Better approach
   my_list = [x for x in my_list if x != 2]
   ```

3. **Forgetting Immutability of Tuples**
   ```python
   # Tuples cannot be modified
   my_tuple = (1, 2, 3)
   # my_tuple[0] = 10  # ERROR - immutable
   ```

4. **Half-Open Interval Confusion**
   ```python
   # range(3, 9) gives 3 to 8, not including 9
   list(range(3, 9))  # [3, 4, 5, 6, 7, 8]
   ```

## Practical Applications

### When to use each data structure:
- **Lists**: When order matters, need modification
- **Tuples**: When immutability is important, returning multiple values
- **Dictionaries**: When mapping keys to values, structured data
- **Sets**: When uniqueness is important, fast lookup

## Setup and Execution

1. Navigate to Day3 folder:
   ```bash
   cd Day3
   ```

2. Run Python examples:
   ```bash
   python data_structure.py
   python swap.py
   ```

3. Open Jupyter notebook:
   ```bash
   jupyter notebook practice.ipynb
   ```

## Next Steps

After Day 3, you should:
- Understand all basic data structures
- Know when to use each structure
- Be comfortable iterating through collections
- Be ready for exception handling (Day 5)

## Concepts to Review

- Lists and list methods
- Dictionaries and key-value access
- Tuples and immutability
- Sets and set operations
- Range and enumerate
- Nested structures

## Key Takeaways

1. Lists are mutable, ordered sequences
2. Dictionaries map keys to values
3. Tuples are immutable sequences
4. Sets contain unique elements
5. Enumerate provides indexed iteration
6. Choose right structure for your use case

## Additional Practice

Try these exercises:
1. Create a list of students and modify it
2. Build a dictionary representing a person
3. Find duplicates using sets
4. Combine range and loops to generate patterns
5. Create nested structures for complex data
6. Write functions using different data structures

## Technologies

- **Python 3.x**: Programming language
- **Jupyter Notebook**: Interactive coding environment
- **Text Editor**: Code writing tool

## Notes

Data structures are fundamental to programming. Mastering them now will make subsequent programming much easier. Spend time practicing different operations and nested combinations.