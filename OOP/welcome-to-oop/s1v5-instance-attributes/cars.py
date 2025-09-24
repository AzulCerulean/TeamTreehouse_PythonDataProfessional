class Car:
  # class attributes
  wheels = 4
  doors = 2
  engine = True


car_one = Car()
car_two = Car()
print(car_one.doors)
print(car_two.doors)
print(Car.doors)

car_one.doors = 6
Car.doors = 3
print(f'Car One: {car_one.doors}')
print(id(car_one.doors))
print(f'Car Two: {car_two.doors}')
print(id(car_two.doors))
print(f'Class Car: {Car.doors}')
print(id(Car.doors))