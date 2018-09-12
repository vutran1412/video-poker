# Preliminary Card class, not used

class Card:
    # Card ranks
    RANKS = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
    ]
    # Suits are in Unicode:
    SUITS = [
                u"\N{BLACK SPADE SUIT}",
                u"\N{BLACK HEART SUIT}",
                u"\N{BLACK DIAMOND SUIT}",
                u"\N{BLACK CLUB SUIT}",
    ]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "|{} {}|".format(Card.RANKS[self.rank], Card.SUITS[self.suit])


print(Card(1, 2))
