# for loop - Capitalize all names in the nametags list
# old_nametags = ['laura', 'dustin', 'rachel']
# new_nametags = []
# for nametag in old_nametags:
#     new_nametags.append(nametag.capitalize())

# list comprehension syntax template
new_nametags = [nametag.capitalize() for nametag in
                ['laura', 'dustin', 'rachel']]

########

# for loop - make the 'welcome' string all caps
# old_banner = "welcome"
# new_banner = ""
# for letter in old_banner:
#     new_banner += letter.upper()

# list comprehension syntax template
new_banner = "".join([letter.upper() for letter in "welcome"])

########

# print statements
print(new_nametags)  # ['Laura', 'Dustin', 'Rachel']
print(new_banner)  # WELCOME
