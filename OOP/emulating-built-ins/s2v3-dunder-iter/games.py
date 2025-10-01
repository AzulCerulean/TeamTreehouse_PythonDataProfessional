class Games:
    def __init__(self, name, loc_player_num):
        self.name = name
        self.loc_player_num = loc_player_num

    def __str__(self):
        return f'{self.name}, local up to: {self.loc_player_num}'


class GameLibrary:
    def __init__(self):
        self.games = []

    def __iter__(self):
        yield from self.games

    def add_game(self, game):
        self.games.append(game)


game_one = Games('Dragon Age: Origins', 1)
game_two = Games('Baldur\'s Gate 3', 2)

my_game_library = GameLibrary()

my_game_library.add_game(game_one)
my_game_library.add_game(game_two)

for game in my_game_library:
    print(game)
    # Dragon Age: Origins, local up to: 1
    # Baldur's Gate 3, local up to: 2
