# The Set Constructor Function
# The Set Constructor function can convert iterable data types into a set. Iterables include strings, lists, tuples, and ranges

empty_set = {}
print(empty_set) # {}
print(type(empty_set)) # <class 'dict'>

empty_set = set()
print(empty_set) # set()
print(type(empty_set)) # <class 'set'>

sentence = 'My favorite data type is the string!'
letters = set(sentence)
print(letters) # {'i', 'a', 'o', ' ', 'y', 'v', 'r', 't', 'd', 'p', 'g', 'h', '!', 'f', 'n', 's', 'e', 'M'}
# went through the set, removed the duplicates
print(len(letters) < len(sentence)) # True

primary_colors = ['red', 'yellow', 'blue']
primary_colors = set(primary_colors)
print(primary_colors) # {'yellow', 'blue', 'red'}

secondary_colors = ('orange', 'purple', 'green')
secondary_colors = set(secondary_colors)
print(secondary_colors) # {'purple', 'orange', 'green'}

odds = set(range(1,11,2))
evens = set(range(2,11,2))
print(odds) # {1, 3, 5, 7, 9}
print(evens) # {2, 4, 6, 8, 10}

groceries = {'milk': 1, 'bread': 2}
print(set(groceries)) # {'bread', 'milk'}
# dictionaries will only provide the keys

# Sets Simplify Data Processing
# Sets can be useful when trying to remove duplicates from a list.

# Sort and Deduplicate a list (not using sets)

numbers = [3,1,2,2,1,3,3,1,2]
unique_numbers = []

for index, number in enumerate(sorted(numbers)):
    if index == 0:
        unique_numbers.append(number)
    elif number == unique_numbers[-1]:
        pass
    else:
        unique_numbers.append(number)

print(unique_numbers) # [1, 2, 3]

# # Sort and Deduplicate a list (using sets)
numbers = [3,1,2,2,1,3,3,1,2]
unique_numbers = sorted(set(numbers))
print(unique_numbers) # [1, 2, 3]
