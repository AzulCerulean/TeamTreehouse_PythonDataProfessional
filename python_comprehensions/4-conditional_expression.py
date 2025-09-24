# for loop - Return a list with 6+ lettered names capitialized
# old_nametags = ['laura', 'dustin', 'rachel']
# new_nametags = []
# for nametag in old_nametags:
#     if len(nametag) >= 6:
#         new_nametags.append(nametag.capitalize())
#     else:
#         new_nametags.append(nametag)

# conditional expression syntax template
new_nametags = [nametag.capitalize() if len(nametag) >= 6 else nametag
                for nametag in ['laura', 'dustin', 'rachel']]

# for loop - make only the vowels uppercase
# old_banner = "welcome"
# new_banner = ""
# for letter in old_banner:
#     if letter in 'aeiou':
#         new_banner += letter.upper()
#     else:
#         new_banner += letter

# conditional expression syntax template
new_banner = "".join([letter.upper() if letter in 'aeiou' else letter
                      for letter in "welcome"])


# print statements
print(new_nametags)  # ['laura', 'Dustin', 'Rachel']
print(new_banner)  # wElcOmE
