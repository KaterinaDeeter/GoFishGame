import random

from card import Card

# Provides list of suits and ranks to fill deck with
def suits():
    return ["\u2663", "\u2665", "\u2666", "\u2660"]

def ranks():
    return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self):
        self.contents = [Card(rank, suit) for rank in ranks() for suit in suits()]

    # Grabs random card from deck, this can be used for drawing a card
    def random_card(self):
        card = random.choice(self.contents)
        return card

    # Removes card from deck
    def removeCard(self, card):
        if card in self.contents:
            self.contents.remove(card)

    # Self-explanatory, will be used to check for end game conditions
    def is_empty(self):
        deck_empty = False
        if not self.contents:
            deck_empty = True
        return deck_empty

    # This would output the same thing as deck.contents when called in main, but makes it less verbose, more readable
    def __str__(self):
        return str(self.contents)