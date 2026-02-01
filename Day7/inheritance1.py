class Car:
    def __init__(self,windows,doors,engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type
        
    def driving(self):
        print("The car is driving")
        
#Audi class is inheriting the Car class    
class Audi(Car):
    def __init__(self,windows,doors,engine_type,horsepower):
        super().__init__(windows,doors,engine_type)
        self.horsepower = horsepower
        
    def driving(self):
        print("It is self driving car")
        
audi1 = Audi(6,4,'Diesel',400)
print(audi1.windows)
audi1.driving()
print(audi1.horsepower)
audi1.driving()

car1 = Car(4,4,'Petrol')
print(car1)
print(audi1)
print(dir(car1))
print(dir(audi1))