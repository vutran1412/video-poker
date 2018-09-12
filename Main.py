from Player import *


def main():
    num_of_players = get_num_of_players()
    players = add_players(num_of_players)
    players_with_money = add_chips(players)
    print(players_with_money)



main()
