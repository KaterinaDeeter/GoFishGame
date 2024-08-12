import random

from card import Card
from deck import Deck
from hand import Hand
from src import hand # added this so I can use the deck that I instantiated in hand

card_deck = hand.card_deck

testCard = Card('A', "\u2666")
print(testCard)
print(testCard.rank)
print(testCard.suit)



user_hand = Hand(7)
print(user_hand.hand)

user_hand.draw_card()
print(user_hand.hand)

print(user_hand.hand[1])
print(user_hand.hand[1].rank)

