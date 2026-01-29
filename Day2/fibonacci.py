# using function or loops, we have to define a function which take input as a number and
# print the fibonnacci series till that number
# for example, if input is 5 then we have print first five fibonnacci number


# Below is wrong logic code(First Try)
"""
previous = 0
x = int(input("Enter a number"))
for i in range(x):
    current = i + previous
    previous = i
    print(previous)
"""

# Below is the corrected logic code
"""
a = 0
b = 1
n = int(input("Enter a number: "))

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
"""
# using function for printing fibonacci series(Chat GPT)
"""
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    return 0

if __name__ == "__main__":   #i made a mistake here for writing fibonacci instead of main
    fibonacci(5)   
"""  
    
# using recursive formula
  
def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci(n-1, b, a+b)

if __name__ == "__main__":
    v=int(input("Enter the number: "))
    fibonacci(v)
