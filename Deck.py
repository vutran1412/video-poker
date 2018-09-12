import random


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        if self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        elif self.rank == 14:
            rank = "Ace"
        else:
            rank = self.rank

        print("|{} {}|".format(rank, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # generate 52 cards
    def build(self):
        for suit in [  u"\N{BLACK SPADE SUIT}",
                    u"\N{BLACK HEART SUIT}",
                    u"\N{BLACK DIAMOND SUIT}",
                    u"\N{BLACK CLUB SUIT}",
                    ]:
                    for rank in range(1, 14):
                        self.cards.append(Card(suit, rank))

    # display all cards in the deck
    def show(self):
        for c in self.cards:
            c.show()

    # shuffle the deck
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        return self.cards.pop()


deck = Deck()
deck.shuffle()
card = deck.draw()
card.show()