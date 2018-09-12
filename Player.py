from Deck import *


# Player class, holds player name, chips and hand
class Player(object):
    def __init__(self):
        self.name = self.get_player_name()
        self.credits = self.add_chips()
        self.hand = []

    # Function to store player name
    def get_player_name(self):
        self.name = input("What is your name?\n")
        return self.name

    # Function to store player chips
    def add_chips(self):
        self.credits = int(input("How much money would you like to play with?\n"))
        return self.credits

    # Function to store player information
    def __str__(self):
        return "Player: " + self.name + "\tCredits: " + str(self.credits)

    # Show player hand
    def show_hand(self):
        for i in self.hand:
            print(i, end=" ")

    # Add cards to hand
    def add_cards(self, cards):
        return self.hand.append(cards)

    # Places a bet
    def place_bet(self):
        bet = 5
        return self.credits - bet

    # Adds winnings to current player's chips
    def winnings(self, winnings):
        return self.credits + winnings

    # Count all the cards in player's hands
    def card_count(self):
        return len(self.hand)



