from Analyzer import *
from Deck import *

# This class is used to test out the card hand analyzer

# straight_flush = [Card(1, 2), Card(1, 3), Card(1, 4), Card(1, 5), Card(1, 6)]
# analyzer = Analyzer(straight_flush)

# four_of_a_kind = [Card(1, 2), Card(2, 2), Card(3, 2), Card(4, 2), Card(1, 6)]
# analyzer = Analyzer(four_of_a_kind)

# flush_test = [Card(1, 5), Card(1, 8), Card(1, 9), Card(1, 2), Card(1, 14)]
# analyzer = Analyzer(flush_test)

# three_of_a_kind_test = [Card(1, 5), Card(2, 5), Card(3, 5), Card(1, 2), Card(1, 14)]
# analyzer = Analyzer(three_of_a_kind_test)

# pairs_test = [Card(1, 5), Card(2, 5), Card(3, 4), Card(4, 4), Card(1, 14)]
# analyzer = Analyzer(pairs_test)

pair_test = [Card(1, 11), Card(2, 11), Card(1, 9), Card(1, 2), Card(1, 14)]
analyzer = Analyzer(pair_test)

straight = analyzer.straight()
flush = analyzer.flush()
highest_count = analyzer.highest_card_count()
pairs = analyzer.pairs()
# Royal flush
if straight and flush and straight == 14:
    print("Royal Flush!!!")
    print("+2000")
# Straight flush
elif straight and flush:
    print("Straight Flush!")
    print("+250")
# 4 of a kind
elif analyzer.four_of_a_kind():
    print("Four of a kind!")
    print("+125")
# Full House
elif analyzer.full_house():
    print("Full House!")
    print("+40")
# Flush
elif flush:
    print("Flush!")
    print("+25")
# Straight
elif straight:
    print("Straight!")
    print("+20")
# 3 of a kind
elif highest_count == 3:
    print("Three of a Kind!")
    print("+15")
# 2 pair
elif len(pairs) == 2:
    print("Two Pairs!")
    print("+10")
# Jacks or better
elif pairs and pairs[0] > 10:
    print("Jacks or Better!")
    print("+5")

