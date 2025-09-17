# Set Operations: Union & Intersection
# There are four main set operations that allow you to compare and contrast collections like a Venn Diagram. Union and Intersection are two methods for comparing shared membership between sets.

# Main Set Operations
# The following methods and operations return a new set.

# s.intersection(t) / s & t - Return the intersection of two sets as a new set. (i.e. all elements that are in both sets.)

# s.union(t) / s | t - Return the union of sets as a new set. (i.e. all elements that are in either set.)

turkey = {'turkey', 'cheese', 'eggs', 'onion', 'spinach', 'mushrooms'}

vegetarian = {'tomato', 'onion', 'cheese', 'mushrooms', 'avocado', 'eggs', 'black olives'}

denver = {'tomato',  'eggs', 'green pepper', 'onion', 'cheese', 'ham'}

bacon = {'mushrooms', 'eggs', 'cheese', 'avocado', 'bacon', 'onion'}

smothered = {'onion', 'cheese', 'avocado', 'turkey', 'green chile', 'eggs'}

print(turkey.union(vegetarian)) # {'spinach', 'cheese', 'eggs', 'avocado', 'black olives', 'turkey', 'onion', 'mushrooms', 'tomato'}
print(turkey.union(vegetarian, denver)) # {'mushrooms', 'tomato', 'black olives', 'ham', 'green pepper', 'cheese', 'avocado', 'onion', 'eggs', 'spinach', 'turkey'}

all_ingredients = turkey | vegetarian | denver | bacon | smothered
print(all_ingredients) # {'green pepper', 'ham', 'onion', 'eggs', 'mushrooms', 'green chile', 'tomato', 'bacon', 'avocado', 'cheese', 'black olives', 'spinach', 'turkey'}

print(vegetarian.intersection(bacon)) # {'cheese', 'avocado', 'eggs', 'onion', 'mushrooms'}
shared_ingredients = turkey & vegetarian & denver & bacon & smothered
print(shared_ingredients) # {'onion', 'eggs', 'cheese'}

# Set Operations: Symmetric Difference & Difference
# The other two main set operations are Symmetric Difference and Difference. These methods allow you to contrast the membership of collections.

# Main Set Operations

# The following methods and operations return a new set.

# s.difference(t) / s - t - Return the difference of two or more sets as a new set. (i.e. all elements that are in this set but not the others.)

# s.symmetric_difference(t) / s ^ t - Return the symmetric difference of two sets as a new set. (i.e. all elements that are in exactly one of the sets.)

# Additional Notes

# The symmetric difference can also be found with the union minus the intersection: (s | t) - (s & t)

print(vegetarian.symmetric_difference(bacon)) # {'bacon', 'tomato', 'black olives'}
# print(vegetarian.symmetric_difference(bacon, denver)) # TypeError: set.symmetric_difference() takes exactly one argument (2 given)
# print(vegetarian.symmetric_difference(bacon).symmetric_difference(denver)) # {'bacon', 'onion', 'black olives', 'ham', 'cheese', 'eggs', 'green pepper'}
# printed the common items, eggs, onion, cheese, we want only other items

different_ingredients = vegetarian ^ bacon
print(different_ingredients) # {'bacon', 'black olives', 'tomato'}

custom_ingredients = all_ingredients.difference(shared_ingredients)
print(custom_ingredients) # {'bacon', 'green chile', 'mushrooms', 'tomato', 'spinach', 'ham', 'avocado', 'turkey', 'green pepper', 'black olives'}
custom_ingredients2 = all_ingredients - shared_ingredients
print(custom_ingredients2) # {'ham', 'mushrooms', 'turkey', 'black olives', 'spinach', 'green pepper', 'bacon', 'avocado', 'green chile', 'tomato'}
