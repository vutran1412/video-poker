class Player(object):
    def __init__(self):
        self.name = self.get_player_name()
        self.credits = self.add_chips()
        self.hand = []

    def get_player_name(self):
        self.name = input("What is your name?\n")
        return self.name

    def add_chips(self):
        self.credits = int(input("How much money would you like to play with?\n"))
        return self.credits

    def __str__(self):
        return "Player: " + self.name + "\tCredits: " + str(self.credits)

    def place_bet(self):
        bet = int(input("How much would you like to bet?\n"))
        return self.credits - bet

    def winnings(self, winnings):
        return self.credits + winnings