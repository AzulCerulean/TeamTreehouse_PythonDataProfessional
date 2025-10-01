# class Game
from cards import Card
import random


class Game:
    def __init__(self):
        # grid size
        self.size = 4
        # card options - words to use in the game
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev',
                             'Egg', 'Far', 'Gum', 'Hut']
        # columns - rows can be generated
        self.columns = ['A', 'B', 'C', 'D']
        self.cards = []
        # list of locations in the grid
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f'{column}{num}')

    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)
    # Methods
        # create a list of card instances
        # create a grid
        # check for matches
        # check for a win
        # make sure the player’s location input is a real
        # run the game


# dunder main
if __name__ == '__main__':
    # create an instance
    # call start game
    game = Game()
    game.set_cards()
    for card in game.cards:
        print(card)
