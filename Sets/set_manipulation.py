# Set Mutability: Adding Elements
# Sets are mutable containers. If an element is not already in a set, it can be added to the set at any time.

# Use .add() to add single items to a set.
# Use .update() to add many items from an iterable into a set.
secondary_colors = set()
secondary_colors.add('orange')
secondary_colors.add('purple')
secondary_colors.add('green')
secondary_colors.add('green')
secondary_colors.add('green')
# print(secondary_colors) # {'green', 'orange', 'purple'}
fancy_colors = set()
fancy_colors.update(['aquamarine', 'emerald green', 'tiffany blue'])
fancy_colors.update(['tiffany blue', 'bacon red'])
# print(fancy_colors) # {'bacon red', 'tiffany blue', 'aquamarine', 'emerald green'}

# Set Mutability: Deleting Elements
# There are four methods to remove an element from a set: clear, remove, discard, pop.

# The .remove() and .discard() methods remove a specific item from a set.
# If an element is not a member of the set, .remove() will throw a KeyError, while .discard() will have no effect.

# The .clear() method removes all elements from a set.

# These three methods return None so be careful not to assign them to a variable!

fancy_colors = set()
fancy_colors.update(['aquamarine', 'emerald green', 'tiffany blue'])
fancy_colors.update(['tiffany blue', 'bacon red'])
fancy_colors.remove('tiffany blue')
# fancy_colors.remove('tiffany blue') # KeyError: 'tiffany blue'
# print(fancy_colors) # {'emerald green', 'bacon red', 'aquamarine'}
fancy_colors.discard('aquamarine')
fancy_colors.discard('aquamarine') # no effect
# print(fancy_colors) # {'emerald green', 'bacon red'}
fancy_colors.clear()
# print(fancy_colors) # set()

# Watch out!
nothing = fancy_colors.clear() # None
# print(nothing) # None

# The .pop() method removes and returns a random member of a set. It will throw a KeyError when called on an empty set.

lucky_numbers = {1, 2, 7, 13, 26, 52}
random_number = lucky_numbers.pop()
# print(random_number) # 1
# print(lucky_numbers) # {2, 52, 7, 26, 13}

### Complete the exercises below by:
### 1. uncommenting the line with the underscores
### 2. replacing the underscores with the proper method
### 3. run the script in the console and to see if your code matches the test message!


vowels = set()

#vowels.___ # Add A, E, I, O, and U into the vowels set
vowels.update('AEIOU')
print(vowels, 'should include A, E, I, O, and U', ':', vowels == {'A', 'E', 'I', 'O', 'U'})


#example_0 = vowels.___ # copy the vowels set
example_0 = vowels.copy()

try:
    print(example_0, 'should be equal to', vowels, ':', example_0 == vowels)
except NameError:
    print('Complete example_0 to run test')


example_1 = vowels.copy()
#example_1.___ # remove all elements from the example
example_1.clear()

print(example_1, 'should be an empty set', ':', example_1 == set())


example_2 = vowels.copy()
#example_2.___ # remove A from the example 
example_2.discard('A')

try:
    print(example_2, 'should not include A', ':', example_2 == {'E', 'I', 'O', 'U'})
except NameError:
    print('Complete example_2 to run test')


example_3 = vowels.copy()
#example_3.___ # remove O from the example
example_3.discard('O')
#example_3.___ # remove O again, with no key error
example_3.discard('O')
try:
    print(example_3, 'should not include O', ':', example_3 == {'A', 'E', 'I', 'U'})
except NameError:
    print('Complete example_3 to run test')


example_4 = vowels.copy()
#random_vowel = example_4.___ # remove and return a random element from the example
random_vowel = example_4.pop()
print(len(example_4), 'should be 4', ':', len(example_4) == 4)

try:
    print(random_vowel, 'should be removed from', example_4, ':', random_vowel not in example_4)
except NameError:
    print('Complete example_4 to run test')

