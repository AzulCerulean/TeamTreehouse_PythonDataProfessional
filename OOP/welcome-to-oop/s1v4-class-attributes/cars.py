class Car:
  pass


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