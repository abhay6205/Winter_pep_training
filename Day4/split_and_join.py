# Below is the wrong logic
"""
line = str(input("Enter the sentence"))
for ch in line:
    if ch.isspace():
        line[ch] = ch
    else:
        line[ch] = '-'
print(line)
"""

# with correct logic, means string is immutable so we cannot directly change
# for that we have initialize new empty variable that will store word
"""
line = input("Enter the sentence: ")
result = ""

for ch in line:
    if ch == " ":
        result += "-"
    else:
        result += ch

print(result)
"""

# Using function
# it will print the as many number of hyphen that are present blank space in sentence
"""
def split_and_join(line):
    result = ""
    
    for ch in line:
        if ch == " ":
            result += "-"
        else:
            result += ch
            
    print(result)

if __name__ == "__main__":
    line = input("Enter the sentence: ")
    split_and_join(line)
"""    
    
# it will print single hyphen only if or not more than one blank spaces are present  
def split_and_join(line):
    result = ""
    prev_space = False

    for ch in line:
        if ch == " ":
            if not prev_space:
                result += "-"
                prev_space = True
        else:
            result += ch
            prev_space = False

    print(result)

if __name__ == "__main__":
    line = input("Enter the sentence: ")
    split_and_join(line)


# for checking the new line, if we have new line then we have to simply replace with hyphen
# python has not its array data structure, so that we use external library for using array which is numpy