# class Card
class Card:
    # hold a card
    # hold the card's location
    # know whether it's been matched or not
    def __init__(self, word, location):
        self.word = word
        self.location = location
        self.matched = False

    # know if two cards are equal or not
    def __eq__(self, other):
        return self.word == other.word

    # be able to print out the card
    def __str__(self):
        return self.word


if __name__ == '__main__':
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('hut', 'D4')

    print(card1 == card2)  # True
    print(card1 == card3)  # False
    print(card1)  # egg
