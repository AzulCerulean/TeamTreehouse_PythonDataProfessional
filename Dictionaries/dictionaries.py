course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

print(course.keys()) # dict_keys(['teacher', 'title', 'level'])
print(course.values()) # dict_values(['Ashley', 'Introducing Dictionaries', 'Beginner'])
print(course['teacher']) # Ashley

# sorting
print(sorted(course.keys())) # ['level', 'teacher', 'title']
print(sorted(course.values())) # ['level', 'teacher', 'title']

# updating and mutating
course['teacher'] = 'Treasure'
course['level'] = 'Intermediate'
course['stages'] = 2
print(course) # {'teacher': 'Treasure', 'title': 'Introducing Dictionaries', 'level': 'Intermediate', 'stages': 2}
del(course['stages'])
print(course) # {'teacher': 'Treasure', 'title': 'Introducing Dictionaries', 'level': 'Intermediate'}

# iterating over dictionaries
print(course.items()) # dict_items([('teacher', 'Ashley'), ('title', 'Introducing Dictionaries'), ('level', 'Beginner')])
for item in course.items():
    print(item)
# ('teacher', 'Ashley')                                                                 
# ('title', 'Introducing Dictionaries')                                                 
# ('level', 'Beginner')
for key, value in course.items():
    print(key)
    print(value)
# teacher                                                                               
# Ashley                                                                                
# title                                                                                 
# Introducing Dictionaries                                                              
# level                                                                                 
# Beginner

# packing with dictionaries
def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
print_teacher(name='Ashley', job='Instructor', topic='Python', second_topic='JavaScript')
# name: Ashley                                                                          
# job: Instructor                                                                       
# topic: Python
# second_topic: JavaScript

# unpacking dictionairies
teacher = {'name':'Ashley', 'job':'Instructor', 'topic':'Python'}
def print_teacher2(name, job, topic):
    print(name)
    print(job)
    print(topic)
# **teacher feeds the dictionary teacher into the function
print_teacher2(**teacher)
# Ashley                                                                                
# Instructor                                                                            
# Python
