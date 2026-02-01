"""
in python, the database decorator is a feature introduced in python 3.7 that provides a concise way 
to define classes primarily intended to store data. it automatically generates special methods like __init__(),
repr (), and __eq__() based on the class attributes, reducing boilerplate code and enhancing readability.
this simplifies the process of creating and working with data-focused classes
"""
from attr import dataclass


@dataclass
class person:   
    name: str
    age: int
    city: str
"""
the @database decorator automatically generates the following methods for you:
1. __init__(): this method is automatically created to initialize the attributes of the class based on the defined fields.
2. __repr__(): this method provides a string representation of the class instance, making it easier to debug and log.
3. __eq__(): this method allows for easy comparison between instances of the class based on their attribute values.
"""

person1 = person('kirish',17,'SE')
# print(person1.age)

@dataclass
class Rectangle:
    length: int
    width: int
    color: str='blue'

rectangle1 = Rectangle(12, 7)
rectangle2 = Rectangle(10, 5, 'red')
    
# print(rectangle1.width)
# print(rectangle2.color)  


@dataclass
class Point:
    x: int
    y: int
    
point1 = Point(3, 4)
# print(point1.x, point1.y) 



#if we we declare any value with frozen = True, then we cannot change the value of that attribute
@dataclass(frozen=True)
class Point2:
    x: int
    y: int
    
point3 = Point2(5, 6)
# point3.x = 10   # this will raise an error because the dataclass is frozen
# print(point3.x, point3.y)


# Inheritance with Dataclasses
@dataclass
class Person:
    name: str
    age: int
@dataclass
class Employee(Person):
    employee_id: int
    position: str


person1 = Person('Bob', 25)
# print(person1.name, person1.age)
employee1 = Employee('Alice', 30, 101, 'Engineer')
# print(employee1.name, employee1.position, employee1.age, employee1.employee_id)



#Nested Dataclasses
@dataclass
class Address:
    street: str
    city: str
    zip_code: str
@dataclass
class Person:
    name: str
    age: str
    address: Address
    
address1 = Address('123 Main St', 'New York', '10001')
person1 = Person('John', 28, address1)
# print(person1.name, person1.address.city)



@dataclass   #@ keyword is known as decorator, in this case it is dataclass decorator
class Student:
    name: str
    roll_number: int
    reg_no: int

@dataclass
class Interview_score:
    communication: int
    tech_skills: int
    resume: int
    
@dataclass    
class Marks:
    class_test: int
    mid_term: int
    end_term: Interview_score
    
student1 = Student('Abhay', 101, 2024)
marks1 = Marks(85, 90, Interview_score(8, 9, 7))
print(student1.name)
print(marks1.end_term.tech_skills)