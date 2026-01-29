"""
Range
python tends to follow half-open interval ([start, end]) with range and slices:
end - start = length
easy to concat ranges w/o overlap(i.e list(range(3)) + list(range(3,9)))
"""

#LIST
"""
animals = ["cat","dog","bird"]
for index in range(len(animals)):
    print("index",index,"has value", animals[index])
    
    

friends = ["Abhay","Sunil","Bipin","Sheelendra","Himanshu","Anish"]
for index, value in enumerate(friends):  #enumerate is used for getting exact length of that variable
    print("index",index,"has value", value) #enumerate contain both index and value but range does not
"""    

#DICTIONARIES
"""
my_dict = {"name":"Abhay","cash":5.5}
for key in my_dict:  #loop over keys
    print(key)
for value in my_dict.values():
    print(value)


my_dict1 = {"name":["Abhay","Bipin","Sunil","Anish"],
           "Roll no":[12,13,14,15]  # multiple values in dictionaries will be stored as list
           }
for key in my_dict1:
    print(key)
for value in my_dict1.values():
    print(value)
    
for key,value in my_dict1.items():
    print(key,":",value)
"""

# Methods of list

frnd = ["Abhay","Bipin","Sunil","Anish","Himanshu"]
frnd.append("Sheelendra")  # adding element at last using append method in list
print(frnd)

print(frnd.index("Himanshu")) #all these are method for getting the value or index number of any specified value
print(frnd[4])
print(frnd.__getitem__(4))

frnd[4] = "Gupta"  # method for replacing any value at the specified index
print(frnd)    # if this makes changes then it proved that list is mutable data structure in python  

print('Abhay' in frnd)   # method for finding that any elements are present inside list or not
print(frnd.__contains__('Abhay'))

enumerate(frnd)   # this method is used for getting index along with value of any list
print(list(enumerate(frnd)))

list((i-len(frnd),n)
    for i, n in enumerate(frnd))  # method for getting negative indexes with value


#SLICING
""" 
includes start index but not neccessarily end
length = end-start
"""