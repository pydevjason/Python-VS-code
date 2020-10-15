import random
# using the len() function as an example for polymorphism

class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __len__(self):
        return self.height

values = [
    "Jason",
    [1,2,3],
    (4,5,6,7),
    {"a": 1, "b": 2},
    Person(name = "Jason", height = 68)
]

for v in values:
    print(len(v))

print("\n")
# as long as the __len__ method is present for all these different data types this is an an example of polymorphism as the __len__ method is present for each object in values

# the following will demonstrate how polymorphism works with a subclass hierarchy 

class Player():
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.games_played

class HumanPlayer(Player):
    def make_move(self):
        print("Let player make the decision!")

class ComputerPlayer(Player):
    def make_move(self):
        print("Run advanced algorithm to calc best move!")

human_player = HumanPlayer(games_played = 30, victories = 15)
computer_player = ComputerPlayer(games_played = 1000, victories = 999)

print(human_player.win_ratio)
print(computer_player.win_ratio)

game_players = [human_player, computer_player]
starting_player = random.choice(game_players)

starting_player.make_move()
