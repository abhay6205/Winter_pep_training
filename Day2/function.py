# simply defing functions
def first():
    print("First")

# defining function with argument
def second(y):
    print(y)

# with returning something from function
def third(x):
    return x*x

# with default argument
def fourth(x=10):
    return x 

# with n number of inputs
def multiadd(*args):
    result = 0
    for x in args:
        result = result + x
    return result


print(first())
print(second(10))
print(third(10))
print(fourth())
print(multiadd(5,6))
print(multiadd(5,6,7))
print(multiadd(10,20,30,40))