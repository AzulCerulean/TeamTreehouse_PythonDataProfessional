class Car:
    # class attributes
    wheels = 4
    doors = 2
    engine = True


car_one = Car()
car_two = Car()
# print(car_one.doors)  # 2
# print(car_two.doors)  # 2
# print(Car.doors)  # 2

# car_one.doors = 4
# print(car_one.doors)  # 4
# print(car_two.doors)  # 2
# print(Car.doors)  # 2

# Car.doors = 4
# print(car_one.doors)  # 4
# print(car_two.doors)  # 4
# print(Car.doors)  # 4

car_one.doors = 6
Car.doors = 3
print(f'car_one {car_one.doors}')  # car_one 6
print(id(car_one.doors))  # without changes: 4580616024, with: 4429297624
print(f'car_two {car_two.doors}')  # car_two 3
print(id(car_two.doors))  # without changes: 4580616024, with: 4429297528
print(f'Car() {Car.doors}')  # Car() 3
print(id(Car.doors))  # without changes: 4580616024, with: 4429297528

# Car.doors = 5
# car_one.doors = 7
# print(f'car_one {car_one.doors}')  # car_one 7
# print(f'car_two {car_two.doors}')  # car_two 5
# print(f'Car() {Car.doors}')  # Car() 5

# an instance of class Car
Car()
# an instance saved to a variable
my_car = Car()

# print an instance
print(Car())
# or
print(my_car)

# print the type
print(type(Car()))
# or
print(type(my_car))

# Check if it's an instance
print(isinstance(Car(), Car))
