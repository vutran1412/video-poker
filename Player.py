class Player(object):
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips


# Get the number of players playing the game
def get_num_of_players():
    while True:
        try:
            num_of_players = int(input("How many players are playing?\n"))
            if num_of_players < 2 or num_of_players > 10:
                raise Exception("Invalid number of players, must be at least 2 or more players and up to 10 players")
            return num_of_players
        except ValueError:
            print("Number of players must be numerals")
        except Exception as e:
            print(e)


# Get all the player names
def add_players(num_of_players):
    players = []
    for i in range(num_of_players):
        if i == 0:
            name = input("What is the name of the " + str(i + 1) + "st player?\n")
        elif i == 1:
            name = input("What is the name of the " + str(i + 1) + "nd player?\n")
        elif i == 2:
            name = input("What is the name of the " + str(i + 1) + "rd player?\n")
        elif i == 3:
            name = input("What is the name of the " + str(i + 1) + "rd player?\n")
        else:
            name = input("What is the name of the " + str(i) + "th player?\n")
        players.append(name)
    return players


def set_money():
    return 2000


def add_chips(players):
    money = set_money()
    players_with_money = {}
    for player in players:
        players_with_money[player] = money
    return players_with_money
