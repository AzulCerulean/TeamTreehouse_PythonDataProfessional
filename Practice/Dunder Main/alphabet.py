## Challenge ##
# Write code to find the word in a 
# list that would come first alphabetically

## Example: When given the list below
# word_list = ["hamster", "turtle", "cat", "bird"]
# The code should find "bird" as the word that 
# would come first alphabetically
def sort_list(list):
    return print(sorted(list)[0])
# can also use return min(list) to return the smallest character (num and/or letter)

# can place testing withing the dunder main to hide it when the main file runs
if __name__ == "__main__":
    word_list = ["hamster", "turtle", "cat", "bird"]
    print(sorted(word_list)[0])