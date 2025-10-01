class Car:
    # class attributes
    wheels = 4
    doors = 2
    engine = True

    # default attributes at the end
    def __init__(self, model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year


car_one = Car("Model T", 1908)
car_two = Car("Phantom", 2020, "Rolls Royce")
print(car_one.make)  # Ford
print(car_two.make)  # Rolls Royce
# print(Car.make). # error, .make is an instance attribute, Car is
# not an instance

car_one.year = 2015
print(car_one.year)  # 2015
print(car_two.year)  # 2020
