from cards import Card
import random


class Game:
  def __init__(self):
    self.size = 4
    self.card_options = ['Add', 'Boo', 'Cat', 'Dev',  'Egg', 'Far', 'Gum', 'Hut']
    self.columns = ['A', 'B', 'C', 'D']
    self.cards = []
    self.locations = []
    for column in self.columns:
      for num in range(1, self.size + 1):
        location = f'{column}{num}'
        self.locations.append(location)
    # Methods

  def set_cards(self):
    used_locations = []
    for card in self.card_options:
      for i in range(2):
        random_location = random.choice(list(set(self.locations) - set(used_locations)))
        used_locations.append(random_location)
        game_card = Card(card, random_location)
        self.cards.append(game_card)

        # check for matches
        # check for a win
        # make sure the player’s location input is a real 
        # run the game


# dunder main
    # create an instance
    # call start game