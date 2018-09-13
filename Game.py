# Video Poker
# Author: Dreyeke Boone and Vu Tran
""" This is a basic commandline video poker game, based off of 5 card draw rules, player selects the cards they want
to discard, player is dealt new cards to replace discarded cards. There is a payout system in place for
different hands"""

from Player import *
from Deck import *
from Analyzer import *
# 3rd party Library to render fancy logo
from pyfiglet import Figlet


def main():
    # Renders any text into an nice looking logo
    # learned about this on
    # https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
    # Figlet documentation: http://www.figlet.org/
    f = Figlet(font='slant')
    print(f.renderText('Video Poker'))
    # Prompts the user to start game
    input("Hit enter to start game\n")
    print()
    print("It costs 5 credits per play\n")
    print()
    # Get all the user inputs and create the player object
    player_1 = Player()
    player_1.add_chips()
    # Loop condition
    quit_game = False
    while not quit_game:
        # Create the deck object and shuffle the cards
        deck = Deck()
        deck.shuffle()
        # Deal the player 5 cards
        for i in range(5):
            player_1.add_cards(deck.draw())

        # Display player information and current hand
        print(player_1)
        player_1.show_hand()
        print()
        # Place bet
        player_1.credits = player_1.place_bet()

        # Loop condition
        valid_input = False
        while not valid_input:
            print("Select cards to discard (using 1,2,3)")
            print("Left through right, separated by a comma")
            print("Hit return to hold all, type Q to quit game")
            # Take user input, user selects the cards to discard
            user_choice = input()
            # If user wants to quit, the quit condition is case insensitive
            if user_choice == "Q" or user_choice == "q":
                quit_game = True
                break
            else:
                try:
                    # Split the user input and save in a list
                    user_input_list = [int(user_input.strip()) for user_input in user_choice.split(",") if user_input]

                    # If user selects a number lower than 1 or greater than 6 run the loop
                    for user_input in user_input_list:
                        if user_input > 6 or user_input < 1:
                            continue

                    # Draw a card to replace discarded cards
                    for user_input in user_input_list:
                        player_1.hand[user_input - 1] = deck.draw()
                    # End the loop if everything checks out
                    valid_input = True
                except ValueError:
                    print("Card selections must be in numerals")
                except Exception as e:
                    print(e)
        print("\n\n")
        player_1.show_hand()
        print("\n\n")
        # Checks the player's hand against every possible hand
        # These functions were tested in test.py
        player_hand = Analyzer(player_1.hand)
        straight = player_hand.straight()
        flush = player_hand.flush()
        highest_count = player_hand.highest_card_count()
        pairs = player_hand.pairs()
        # Player payouts
        # Royal Flush
        winnings = 0
        if straight and flush and straight == 14:
            print("Royal Flush!!!")
            print("+2000")
            winnings = 2000
        # Straight flush
        elif straight and flush:
            print("Straight Flush!")
            print("+250")
            winnings = 250
        # 4 of a kind
        elif player_hand.four_of_a_kind():
            print("Four of a kind!")
            print("+125")
            winnings = 125
        # Full House
        elif player_hand.full_house():
            print("Full House!")
            print("+40")
            winnings = 40
        # Flush
        elif flush:
            print("Flush!")
            print("+25")
            winnings = 25
        # Straight
        elif straight:
            print("Straight!")
            print("+20")
            winnings = 20
        # 3 of a kind
        elif highest_count == 3:
            print("Three of a Kind!")
            print("+15")
            winnings = 15
        # 2 pair
        elif len(pairs) == 2:
            print("Two Pairs!")
            print("+10")
            winnings = 10
        # Jacks or better
        elif pairs and pairs[0] > 10:
            print("Jacks or Better!")
            print("+5")
            winnings = 5
        # Pay the player
        player_1.credits = player_1.winnings(winnings)
        # empty hand
        player_1.hand = []
    print("\n\n\n\n\n\n")

main()
