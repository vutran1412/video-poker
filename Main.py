from Player import *


def main():
    player_1 = Player()
    print(player_1)
    player_1.credits = player_1.place_bet()
    print(player_1)

main()
