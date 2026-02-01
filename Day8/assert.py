"""Python provides the asserts statement to check if a given expression is true or false
Program execution proceeds only if the expression is true and raises the AeertionError
when it is false."""

try:
    x = int(input("Enter the number: "))
    assert x>=0, "The number is negative"
    print(f"The number is {x}")
except AssertionError:
    print("The number is negative, please enter a positive number")
    
    
try:
    num=int(input("Enter the number: "))
    assert num%2==0
    print(f"The number is even: {num}")
except AssertionError:
    print("Please enter an even number")