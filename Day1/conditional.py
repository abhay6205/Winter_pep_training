
# By procedural method

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))

# if(a > b and a > c):
#     print("First Number is greater: ",a)
# elif(c > a and c > b):
#     print("Third Number is greater: ",c)
# else:
#     print("Second Number is greater: ",b)

# by functional method
def main():
    x,y = 10, 100
    
    if(x<y):
        print("X is less than y")
    elif(x==y):
        print("X is equal to y")
    else:
        print("Y is greater than x")
    
   
if __name__ == "__main__":
    main()
    
    
x,y=5,6   
st = "X is less than y" if(x < y) else "Y is greater or equal to Y"
print(st)