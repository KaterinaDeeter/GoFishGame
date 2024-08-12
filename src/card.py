class Card:
    # Creates Card with a Rank and Suit
    def __init__(self, card_rank, card_suit):
        self.rank = card_rank
        self.suit = card_suit

    # Compares the rank of one card to another -- is this useful?
    def compare_ranks(self, other):
        return self.rank == other.rank

    # is one card equal to another (not sure why I have this currently TODO is this necessary?)
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.__str__()
