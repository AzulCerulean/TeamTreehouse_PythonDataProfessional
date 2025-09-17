# Fill in your name and pronouns

student = {
    'name': 'Azul',
    'pronouns': ['She', 'They']
}

workshop = {
    'title': 'Python Sets',
    'objective': 'Learn a new data structure!'
}

# Complete the key-value pairs below

python_set = {
    'definition': 'An unordered collection of unique elements.',
    'properties': 'No order & no duplicate values.',
    'membership': 'An element of a set is called a member.',
}

my_first_set = {'Hello Sets!'}
# print(my_first_set) # {'Hello Sets!'}
# print(type(my_first_set)) # <class 'set'>
# print(len(my_first_set)) # 1

# Sets - order does not matter
# print({1, 2, 3} == {3, 2, 1}) # True

# Lists - order DOES matter
# print([1, 2, 3] == [3, 2, 1]) # False

# print({1, 2, 3, 4, 1, 2, 3, 4,1, 2}) #{1, 2, 3, 4}
# print(len({1, 2, 3, 4, 1, 2, 3, 4,1, 2})) # 4

fours = {4, 4.0}
# print(fours) # {4}
# print(4 == 4.0) # True
# print({4.0, 4}) # 4.0
# they are both 4 and it will display the first one, left to right
challenge = {4.0, 4, 5.0, 5}
# print(challenge) # {4.0, 5.0}

twos = {'two', 2, 2.22, ('dos', 'Spanish')}
# print(twos) # {2, 2.22, ('dos', 'Spanish'), 'two'}
booleans = {True, False}
# print(booleans) # {False, True}
none_set = {None}
# print(none_set) # {None}
# print({[1,2,3]}) # TypeError: unhashable type: 'list'
# print({{'hello': 'world!'}}) # TypeError: unhashable type: 'dict'
# print({{'hello sets!'}}) # TypeError: unhashable type: 'set'
