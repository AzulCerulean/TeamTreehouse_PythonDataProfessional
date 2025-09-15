course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

print(course.keys()) # dict_keys(['teacher', 'title', 'level'])
print(course.values()) # dict_values(['Ashley', 'Introducing Dictionaries', 'Beginner'])
print(course['teacher']) # Ashley

# sorting
print(sorted(course.keys())) # ['level', 'teacher', 'title']
print(sorted(course.values())) # ['level', 'teacher', 'title']
