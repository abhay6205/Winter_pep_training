year = int(input("Enter the year of birth: "))
age = 2021 - year
try:
    if age<=10 & age>=20:
        print("The age is valid")
    else:
        raise dobException
except dobException:
    print("The age is not within the range")