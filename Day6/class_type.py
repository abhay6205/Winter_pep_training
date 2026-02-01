### all the class variables are public
class Car():
    def __init__(self, window, doors, engine_type):
        self.window = window
        self.doors = doors
        self.engine_type = engine_type
        
audi1 = Car(6,4,'Diesel')
# print(audi1.window)

audi1.window = 7
# print(audi1.window)

### all the class variables are protected
class Car():
    def __init__(self, window, doors, engine_type):
        self._window = window
        self._doors = doors
        self._engine_type = engine_type
        
class Truck(Car):
    def __init__(self, window, doors, engine_type, horsepower):
        super().__init__(window, doors, engine_type)
        self.horsepower = horsepower
        print(self._Car__window)  # accessing protected variable using name mangling
        
truck1 = Truck(8,2,'Diesel',500)
# print(dir(truck1))
truck1._doors = 3  # this will create a new variable __doors in truck1 object
print(truck1._doors)


### all the class variables are private
class Car():
    def __init__(self, window, doors, engine_type):
        self.__window = window
        self.__doors = doors
        self.__engine_type = engine_type
        
audi = Car(6,4,'Diesel')

audi._Car__doors = 5  # this will create a new variable __doors in audi object