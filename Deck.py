import random

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank

        print("{} {}".format(rank, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # generate 52 cards
    def build(self):
        for s in [  u"\N{BLACK SPADE SUIT}",
                    u"\N{BLACK HEART SUIT}",
                    u"\N{BLACK DIAMOND SUIT}",
                    u"\N{BLACK CLUB SUIT}",
                    ]:
                    for r in range(1, 14):
                        self.cards.append(Card(s, r))

    # display all cards in the deck
    def show(self):
        for c in self.cards:
            c.show()

    # shuffle the deck
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()



#class Player(object)
deck = Deck()
#deck.show()
deck.shuffle()
deck.show()
