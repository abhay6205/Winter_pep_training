# Day 4 - String Methods and Text Processing

## Overview
Day 4 focuses on advanced string manipulation techniques. This day explores string methods, text processing, and practical applications of string operations that are essential for handling text data in real-world programming scenarios.

## Learning Objectives

- ✓ Mastering string methods
- ✓ String splitting and joining
- ✓ Character replacement and substitution
- ✓ Text parsing and analysis
- ✓ Whitespace handling
- ✓ Format strings effectively

## Project Files

### split_and_join.py
Demonstrates string splitting and joining operations:
- Breaking strings into words/parts
- Joining sequences back into strings
- Processing sentences and text
- Handling whitespace

### requirement.txt
Lists project dependencies and required packages.

## Key Concepts Covered

### 1. String Split
Break strings into parts:
```python
sentence = "Hello World Python Programming"

# Split by space (default)
words = sentence.split()
# ['Hello', 'World', 'Python', 'Programming']

# Split by specific delimiter
csv = "apple,banana,orange"
fruits = csv.split(",")
# ['apple', 'banana', 'orange']

# Split with limit
text = "one-two-three-four"
parts = text.split("-", 2)
# ['one', 'two', 'three-four']
```

### 2. String Join
Combine sequences into strings:
```python
words = ['Hello', 'World', 'Python']

# Join with space
result = " ".join(words)
# 'Hello World Python'

# Join with different separator
items = ['apple', 'banana', 'orange']
csv = ",".join(items)
# 'apple,banana,orange'

# Join with no separator
letters = ['P', 'y', 't', 'h', 'o', 'n']
word = "".join(letters)
# 'Python'
```

### 3. String Replacement
Replace parts of strings:
```python
text = "Hello World"

# Replace single occurrence
new_text = text.replace("World", "Python")
# 'Hello Python'

# Replace all occurrences
text_with_spaces = "a b a d a"
replaced = text_with_spaces.replace("a", "x")
# 'x b x d x'

# Replace with limit
text = "banana"
replaced = text.replace("a", "o", 2)
# 'bonona' (only first 2 replaced)
```

### 4. String Methods
Common string operations:
```python
text = "Hello World Python"

# Case conversion
print(text.upper())        # 'HELLO WORLD PYTHON'
print(text.lower())        # 'hello world python'
print(text.title())        # 'Hello World Python'
print(text.capitalize())   # 'Hello world python'
print(text.swapcase())     # 'hELLO wORLD pYTHON'

# Searching
print(text.find("World"))     # 6
print(text.index("World"))    # 6
print(text.count("o"))        # 2
print(text.startswith("Hello")) # True
print(text.endswith("Python"))  # True

# Whitespace handling
text_with_spaces = "  Hello World  "
print(text_with_spaces.strip())   # 'Hello World'
print(text_with_spaces.lstrip())  # 'Hello World  '
print(text_with_spaces.rstrip())  # '  Hello World'

# Checking
print("123".isdigit())       # True
print("abc".isalpha())       # True
print("abc123".isalnum())    # True
print("   ".isspace())       # True
```

### 5. String Formatting
Create formatted strings:
```python
# Old style (%)
name = "John"
age = 25
print("Name: %s, Age: %d" % (name, age))

# str.format()
print("Name: {}, Age: {}".format(name, age))
print("Name: {name}, Age: {age}".format(name="John", age=25))

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Next year: {name} will be {age + 1}")

# Number formatting
pi = 3.14159
print(f"Pi: {pi:.2f}")  # Pi: 3.14
print(f"Large number: {10000:,}")  # Large number: 10,000
```

## Topics Discussed

1. **String Splitting**
   - Split by default whitespace
   - Split by custom delimiter
   - Limiting split results
   - Removing empty strings

2. **String Joining**
   - Joining lists to strings
   - Custom separators
   - Different use cases
   - Performance considerations

3. **String Replacement**
   - Replacing single occurrence
   - Replacing all occurrences
   - Conditional replacement
   - Using regular expressions (intro)

4. **Case Conversion**
   - Upper and lower case
   - Title and capitalize
   - Case-insensitive comparisons

5. **String Searching**
   - Finding substrings
   - Counting occurrences
   - Starting/ending checks
   - Case sensitivity

6. **Whitespace Management**
   - Removing leading/trailing spaces
   - Handling internal whitespace
   - Normalizing whitespace

7. **Text Processing Applications**
   - Parsing CSV data
   - Processing user input
   - Cleaning text data
   - Building formatted output

## Activities

### Activity 1: String Splitting
```python
# Split sentence into words
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
print(f"Number of words: {len(words)}")
print(f"Words: {words}")
```

### Activity 2: String Joining
```python
# Join with different separators
fruits = ["apple", "banana", "orange", "mango"]

# With space
print(" ".join(fruits))

# With comma
print(", ".join(fruits))

# With newline
print("\n".join(fruits))
```

### Activity 3: Replacing Characters
```python
# Replace blank spaces with hyphens
sentence = "The quick brown fox"
result = sentence.replace(" ", "-")
print(result)  # The-quick-brown-fox
```

### Activity 4: String Methods
```python
text = "learning python is fun"

# Various operations
print(text.upper())
print(text.title())
print(text.replace("python", "PYTHON"))
print(text.count("n"))
```

### Activity 5: Whitespace Handling
```python
# Remove leading and trailing spaces
user_input = "  hello world  "
cleaned = user_input.strip()
print(f"'{cleaned}'")  # 'hello world'
```

## Code Examples

### Split and Join Example
```python
line = "apple,banana,orange,mango"

# Split by comma
fruits = line.split(",")
# ['apple', 'banana', 'orange', 'mango']

# Process each fruit
fruits = [fruit.strip().upper() for fruit in fruits]
# ['APPLE', 'BANANA', 'ORANGE', 'MANGO']

# Join back with different separator
result = " | ".join(fruits)
print(result)
# APPLE | BANANA | ORANGE | MANGO
```

### Text Cleaning
```python
def clean_text(text):
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Convert to lowercase
    text = text.lower()
    
    # Replace punctuation with space
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    
    # Split into words
    words = text.split()
    
    # Remove duplicates and rejoin
    unique_words = list(set(words))
    return " ".join(unique_words)

sample = "Hello, world. Hello, python."
print(clean_text(sample))
```

### String Formatting
```python
# Create formatted report
name = "Alice"
score = 95.7
percentage = 85

report = f"""
Student Report
==============
Name: {name}
Score: {score:.1f}
Percentage: {percentage}%
Grade: {'A' if percentage >= 90 else 'B'}
"""
print(report)
```

## Common Mistakes to Avoid

1. **Forgetting String Immutability**
   ```python
   # Strings don't change in place
   text = "hello"
   text.upper()  # Returns new string, doesn't modify
   new_text = text.upper()  # Correct way
   ```

2. **Index Errors in Replacing**
   ```python
   # Index works differently than replace
   text = "hello"
   text[0] = 'H'  # ERROR - strings are immutable
   text = 'H' + text[1:]  # Correct
   ```

3. **Split Edge Cases**
   ```python
   text = "a  b  c"  # Multiple spaces
   parts = text.split()  # Handles automatically [' a', 'b', 'c']
   parts = text.split(" ")  # May include empty strings ['a', '', 'b', '', 'c']
   ```

4. **Join Type Errors**
   ```python
   numbers = [1, 2, 3]
   result = " ".join(numbers)  # ERROR - join needs strings
   result = " ".join(map(str, numbers))  # Correct
   ```

## Practical Applications

### Real-world scenarios:
- Parsing CSV data
- Processing log files
- Text cleaning and normalization
- Building formatted reports
- Data extraction from text
- User input validation

## Setup and Execution

1. Navigate to Day4 folder:
   ```bash
   cd Day4
   ```

2. Run Python example:
   ```bash
   python split_and_join.py
   ```

3. Install requirements (if needed):
   ```bash
   pip install -r requirement.txt
   ```

## Next Steps

After Day 4, you should:
- Master string methods and operations
- Understand string immutability
- Process text data effectively
- Be ready for exception handling (Day 5)

## Concepts to Review

- String split and join
- String replacement
- Case conversion methods
- String searching methods
- Whitespace handling
- String formatting

## Key Takeaways

1. Strings are immutable in Python
2. Split breaks strings into parts
3. Join combines sequences
4. Many built-in string methods available
5. Format strings for output
6. String operations are fundamental

## Additional Practice

Try these exercises:
1. Parse a CSV line into data
2. Clean and normalize text
3. Count word frequencies in text
4. Create formatted reports
5. Extract specific information from strings
6. Build a simple text processor

## Technologies

- **Python 3.x**: Programming language
- **Text Editor**: Code writing tool
- **Terminal**: Code execution

## Notes

String manipulation is central to most programming tasks. The methods covered here are used constantly in real-world development, especially when processing user input, files, and data.