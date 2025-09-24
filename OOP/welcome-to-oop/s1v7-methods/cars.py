class Car:
    # Class Attributes
    wheels = 4
    doors = 2
    engine = True

    # The Initializer
    def __init__(self, model, year, make="ford"):
        # Instance attributes
        self.make = make
        self.model = model
        self.year =year


car_one = Car('Model T', 1908)
car_two = Car('Phantom', 2020, 'Rolls Royce')

print(car_one.make)
print(car_two.make)