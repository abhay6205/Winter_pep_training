"""
given the participants's score sheet for your university sports day, you are required to 
find the runner-up score. You re given scores. store them in a list and find the score of the runner-up

Input format:
Thr first line contains total number of contenstants a.
the second line contains an array of integer each separated by a space.
Constraints 2<=a<=100

Output format:
Print the runner-up score

Sample input:
5
2 3 6 6 5
Sample output
5
"""

# a = int(input("Enter the number of contenstants: "))
# arr = []
# for i in range(a):
#     b = int(input("Enter the score: "))
#     arr.append(b)
    
# c = sorted(arr)
# arr1 = []
# d = c[0]
# for i in range(1,a):
#     if d == c[i]:
#         d = c[i]
#     elif d != c[i]:
        
#         arr1.append(d)
    
        
# print(arr1)



""" 
i have a list of dictionaries which consist data with key 'name' and 'age',
i have to sort this list on the basis of age value in descending order
"""

# my_dict = {'name': ['Abhay','Bipin','Sunil','Himanshu','Sheelendra','Pallavi'],
#            'age': [21, 20, 22, 23, 19, 21]}

# c = sorted(my_dict, key=lambda x: x['age'], reverse=True)
# print(c)



# my_dict1 = {'name': 'Abhay', 'age': 21,
#             'name': 'Bipin', 'age': 20,
#             'Name': 'Sunil', 'age': 22}

# d = sorted(my_dict1, value=lambda x: x['age'], reverse=True)
# print(d)


# in above 2 solutions, i was trying to sort on a dictionary which is wrong process, i have to perform operation on list


# my_dict3 = [
#     {'name': 'Abhay', 'age': 21},
#     {'name': 'Bipin', 'age': 20},
#     {'name': 'Sunil', 'age': 22},
#     {'name': 'Himanshu', 'age': 23},
#     {'name': 'Sheelendra', 'age': 19},
#     {'name': 'Pallavi', 'age': 21}
# ]

# e = sorted(my_dict3, key=lambda x: x['age'], reverse=True)
# print(e)



""" 
take input from user as string. we have replace a character with some other
"""

# a = input("Enter the word: ")
# b = input("Enter the character which have to replace: ")
# # a=list(a)   #string is immutable for converting into list
# # for i in range(len(a)):
# #     if b in a[i]:
# #         a[i] = '#'
# # a=''.join(a)       
# # print(a)
# a=a.replace(b,'#')
# print(a)

"""Take input from user as string and print the repeated character"""

# a = input("Enter the Word: ")
# s = set(a)
# b = []
# for c in s:
#     if a.count(c) > 1:
#         b.append(c)
        
# print(b)


""" i have a string stored, i have to find a character but within sub-string which should be 
taken as input from user. is that character is matched then return true otherwise false"""

# a = input("Enter the Sentence: ")
# ch = input("Enter the character to search: ")
# b = int(input("Enter the length of string within you want to search: "))

# if ch in a[:b]:
#     print("True")
# else:
#     print("False")


"""try-else except"""

# try:
#     a = int(input("Enter the number 1: "))
#     b = int(input("Enter the number 2: "))
#     c=a/b
#     d=a*b
#     e=a+b
# except NameError:
#     print("The user has not define the variable")
# except ZeroDivisionError:
#     print("please provide the number greater than 0")
# except TypeError:
#     print("Try to make the datatype similar")
# except Exception as ex:
#     print(ex)
# else:
#     print(c)
#     print(d)
#     print(e)
    
    
    
    
""" 
Given a string, which is the company name in lowercase letters, your task is to find the 
top three most common characters in the string.
print the three most comon characters along with their occuerence count.
sort in descending order of occurenec count.
if the occurence count is the same, sort the characters in alphabetical order.

input format
aabcdcbebf

output format
b 3
a 2
c 2
"""

# s = input()

# count = {}

# for ch in s:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1
# print(count)
# items = list(count.items())
# items1 = sorted(items, key=lambda x: (-x[1], x[0]))
# print(items1)
# for i in range(3):
#     print(items1[i][0], items1[i][1])


"""
all the information related to a student has stored across multiple classes
after creating classes, store some value. now i have to compare the marks, 
if student gets more than 70 marks, then he is pass,
if student get between 2=30 and 70, then he is in average category, 
if below 30 then he is fail, if marks is 0 then absent, 
but using exeption handling, if some student are absent then it should come inside exception block
"""

class Student:
    name = str
    roll_number = int

class Marks(Student):
    marks = int
    
class result(Marks):
    def check_result(self):
        try:
            if self.marks > 70:
                print(f"{self.name} has passed the exam")
            elif 30 <= self.marks <= 70:
                print(f"{self.name} is in average category")
            elif 0 < self.marks < 30:
                print(f"{self.name} has failed the exam")
            elif self.marks == 0:
                raise ValueError
        except ValueError:
            print("Student is absent")
            
            
student1 = result()
student1.name = "Abhay"
student1.roll_number = 1
student1.marks = 0
# print(student1.check_result())

"""leap year or not"""

year = int(input("Enter the year between 1900 and 2100: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("True")
# else:
#     print("False")
    
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    return leap
print(is_leap(year))



