from Player import *
from Deck import *


def main():
    player_1 = Player()
    deck = Deck()
    deck.shuffle()
    for i in range(5):
        player_1.add_cards(deck.draw())
    print(player_1)
    player_1.show_hand()


main()
