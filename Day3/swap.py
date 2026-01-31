"""
st = 'hello'
print(st.islower())
"""

"""
st1 = 'HELLO'
print(st1.islower())
print(st1.isupper())
"""
"""
st = 'Abhay'
n= len(st)
for i in range(n):
    if st[i].islower() == st[i]:
        print(st[i]) 
    else:
        print(False)
"""       
        
"""     
st = 'Abhay'

for ch in st:
    if ch.islower():
        print(ch, "is lowercase")
        print(ch.upper())
    elif ch.isupper():
        print(ch, "is uppercase")
        print(ch.lower())
"""

# using function
def swap_case(s):
    for ch in s:
        if ch.islower():
            a = print(ch, "is lowercase")
            b = print(ch.upper())
        elif ch.isupper():
            a=print(ch, "is uppercase")
            b=print(ch.lower())
        else:
            c=print(ch, "it is not string")
    return a,b,c


if __name__ == "__main__":
    ch=input("Enter the word: ")
    swap_case(ch)