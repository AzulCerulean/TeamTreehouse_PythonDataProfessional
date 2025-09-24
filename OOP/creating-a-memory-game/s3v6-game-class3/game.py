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

  def create_row(self, num):
    row = []
    for column in self.columns:
      for card in self.cards:
        if card.location == f'{column}{num}':
          if card.matched:
            row.append(str(card))
          else:
            row.append('   ')
    return row

  def create_grid(self):
    header = ' |  ' + '  |  '.join(self.columns) + '  |'
    print(header)
    for row in range(1, (self.size + 1)):
      print_row = f'{row}| '
      get_row = self.create_row(row)
      print_row += ' | '.join(get_row) + ' |'
      print(print_row)

        # check for matches
        # check for a win
        # make sure the player’s location input is a real 
        # run the game


# dunder main
    # create an instance
    # call start game