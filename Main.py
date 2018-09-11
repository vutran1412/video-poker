from Player import *


def main():
    num_of_players = get_num_of_players()
    players = add_players(num_of_players)
    for player in players:
        print(player)


main()
