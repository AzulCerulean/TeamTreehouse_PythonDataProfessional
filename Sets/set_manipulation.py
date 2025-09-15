### Complete the exercises below by:
### 1. uncommenting the line with the underscores
### 2. replacing the underscores with the proper method
### 3. run the script in the console and to see if your code matches the test message!


vowels = set()

#vowels.___ # Add A, E, I, O, and U into the vowels set

print(vowels, 'should include A, E, I, O, and U', ':', vowels == {'A', 'E', 'I', 'O', 'U'})


#example_0 = vowels.___ # copy the vowels set

try:
    print(example_0, 'should be equal to', vowels, ':', example_0 == vowels)
except NameError:
    print('Complete example_0 to run test')


example_1 = vowels.copy()

#example_1.___ # remove all elements from the example

print(example_1, 'should be an empty set', ':', example_1 == set())


example_2 = vowels.copy()

#example_2.___ # remove A from the example 

try:
    print(example_2, 'should not include A', ':', example_2 == {'E', 'I', 'O', 'U'})
except NameError:
    print('Complete example_2 to run test')


example_3 = vowels.copy()

#example_3.___ # remove O from the example

#example_3.___ # remove O again, with no key error

try:
    print(example_3, 'should not include O', ':', example_3 == {'A', 'E', 'I', 'U'})
except NameError:
    print('Complete example_3 to run test')


example_4 = vowels.copy()

#random_vowel = example_4.___ # remove and return a random element from the example

print(len(example_4), 'should be 4', ':', len(example_4) == 4)

try:
    print(random_vowel, 'should be removed from', example_4, ':', random_vowel not in example_4)
except NameError:
    print('Complete example_4 to run test')