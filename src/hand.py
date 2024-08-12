import random

from card import Card
from deck import Deck

card_deck = Deck()
class Hand:
    def __init__(self, hand_size):
        self.hand = []
        for ii in range(hand_size):
            self.draw_card()

    def draw_card(self):
        card = card_deck.random_card()
        self.hand.append(card)
        card_deck.removeCard(card)