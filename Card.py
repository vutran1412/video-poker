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

    def __init__(self, rank=0, suit=0):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "|{} {}|".format(Card.RANKS[self.rank], Card.SUITS[self.suit])



