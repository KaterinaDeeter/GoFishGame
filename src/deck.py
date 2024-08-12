from card import Card

# Provides list of suits and ranks to
def suits():
    return ["\u2663", "\u2665", "\u2666", "\u2660"]

def ranks():
    return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self):
        self.contents = [Card(rank, suit) for rank in ranks() for suit in suits()]

    def __str__(self):
        return str(self.contents)