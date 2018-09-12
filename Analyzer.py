from Deck import *

""" This class will analyze player's hands and determine what type of hand the player has based on the card 
combinations in the player's hands """


class Analyzer(object):
    # Constructor, the only arguments need is the cards in the player's hand
    def __init__(self, cards):
        self.cards = cards

    # Function to look for the highest card in the player's hand
    def high_card(self):
        # List comprehension to get all the cards in the player's hands and store in a list
        ranks = [card.rank for card in self.cards]
        # The high card is initialized as None
        high_card = None
        # Loop through the current hand
        for card in self.cards:
            # If high_card is empty, assign it the value of card
            if high_card is None:
                high_card = card
            # If the current high_card is less than the card in the iteration, assign it the new value
            elif high_card.rank < card.rank:
                high_card = card
        # return the high_card
        return high_card

    # Counts the number of cards in the hand, this function will be used to determine three of a kinds
    def highest_card_count(self):
        # Initialize the counter at 0
        count = 0
        # List comprehension to get all the card ranks in the hand and save it in a list
        ranks = [card.rank for card in self.cards]
        # Iterate through the list
        for rank in ranks:
            # if we see more cards of the same rank, assign that value to counter
            if ranks.count(rank) > count:
                count = ranks.count(rank)
        # return the count
        return count

    # Function to determine if the hand contains pairs
    def pairs(self):
        # Initialize an empty list
        pairs =[]
        # List comprehension to save all the ranks in the hand to a list
        ranks = [card.rank for card in self.cards]
        # Loops through the ranks
        for rank in ranks:
            # if we have two cards of the same rank and not currently in the list, append them to the list
            if ranks.count(rank) == 2 and rank not in pairs:
                pairs.append(rank)
        # return the pairs
        return pairs

    # Function to determine if the cards in hand are a flush
    def flush(self):
        # List comprehension to save all the suits in current hand
        suits = [card.suit for card in self.cards]
        # Return true if all the suits are the same
        if len(set(suits)) == 1:
            return True
        else:
            return False

    # Function to determine if the cards in hand form a straight
    def straight(self):
        # Get all the ranks in a list through list comprehension
        ranks = [card.rank for card in self.cards]
        # Sort all the ranks
        ranks.sort()
        # Length of the collection must be 5
        if not len(set(ranks)) == 5:
            return False
        else:
            # check if the number is a straight, since the collection is now ordered, the next index should
            # equal the current index plus one.
            if not ranks[0] + 1 == ranks[1]:
                return False
            elif not ranks[1] + 1 == ranks[2]:
                return False
            elif not ranks[2] + 1 == ranks[3]:
                return False
            elif not ranks[3] + 1 == ranks[4]:
                return False
        return ranks[4]

    # Function to check if the player has a four of a kind
    def four_of_a_kind(self):
        # Save all the ranks from hand
        ranks = [card.rank for card in self.cards]
        # Loop through the ranks
        for rank in ranks:
            # Return true if there are four cards of the same rank
            if ranks.count(rank) == 4:
                return True

    # Function to check if the player has a full house
    def full_house(self):
        # Initialize the two and three cards booleans, this will be used to check to see if the hand has two
        # and three cards of the same rank
        two_cards = False
        three_cards = False
        # All the ranks in the player's hand
        ranks = [card.rank for card in self.cards]
        # If there are two cards of the same rank two cards will be set to true
        if ranks.count(ranks) == 2:
            two_cards = True
        # If there are three cards of the same rank three cards will be set to true
        elif ranks.count(ranks) == 3:
            three_cards = True
        # If both conditions are true, then the player has a full house
        if two_cards and three_cards:
            return True
        else:
            return False
