# import pdb

my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

# pdb.set_trace()
# can also  use it in one line and the only time a semi-colon is ok
# import pdb; pdb.set_trace()
# you usually remove it one debugged
del my_list[3]  # [5, 2, 1, "abcdefg", 3, False, 4]
del my_list[3]  # [5, 2, 1, 3, False, 4]
del my_list[4]  # [5, 2, 1, 3, False, 4]
print(my_list)
