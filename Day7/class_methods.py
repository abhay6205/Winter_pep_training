class Car:
    base_price = 100000  # Class variable
    def __init__(self, windows, doors, power):
        self.windows = windows      # Instance variable
        self.doors = doors          # Instance variable
        self.power = power  # Instance variable
        
    def what_base_price(self):
        print("The base price of the car is {}".format(self.base_price))
    @classmethod         # '@' keyword is known as decorator, in this case it is classmethod decorator
    def revise_base_price(cls, inflation_rate):
        cls.base_price = cls.base_price + (cls.base_price * inflation_rate)
        
        
        
Car.revise_base_price(0.10)
print("Revised base price is {}".format(Car.base_price))

# car1 = Car(4, 5, 2000)
# print("Car1 base price is {}".format(car1.base_price))

Car.revise_base_price(0.07)
print("Revised base price is {}".format(Car.base_price))

