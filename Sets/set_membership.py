import string

# Code along to my video below!
# Set Membership & Relationship
# Membership testing is a distinguishing feature of sets. Testing for membership means asking if an element is present in a set. Sets can have relationships with each other based on their mutual membership.

# These operations return a boolean value.

# Testing for Membership
# x in set True if set contains element.
# x not in set True if set does not contain element.
vowels = { 'A', 'E', 'I', 'O', 'U' }
print('A' in vowels) # True
print('B' in vowels) # False
print('C' not in vowels) # True
alphabet = set(string.ascii_lowercase) # 'abcdefghijklmnopqrstuvwxyz'
print(alphabet) # {'q', 'v', 'u', 'w', 'c', 'b', 'm', 'x', 't', 'o', 'r', 'y', 'e', 'j', 'f', 'a', 'd', 'l', 'k', 'i', 'g', 'n', 'p', 'z', 'h', 's'}
alphabet = set(string.ascii_uppercase)
is_related = None
for letter in vowels:
    if letter in alphabet:
        is_related = True
    else:
        is_related = False
        break
if is_related is True:
    print("It's related!") # It's related!

# Testing for Equality
# == "equal to" - True if two sets are equal length and contain the exact same members
# != "not equal to" - Opposite of "equal to"

# Testing for Relationship
# isdisjoint() - True if two sets have a null intersection (ie. no members in common).
digits = set(string.digits)
print(digits.isdisjoint(alphabet)) # True

# issubset() / <= - True if another set contains this set.
# issuperset() / >= True if this set contains another set.
# An empty set is both a disjointed set and a subset of all sets.
# A set is both a subset and a superset of itself.
print(vowels.issubset(alphabet)) # True
print(alphabet.issuperset(vowels)) # True
print(vowels <= alphabet) # True
print(alphabet >= vowels) # True
