import random

from card import Card
from deck import Deck

testCard = Card('K', 'Clubs')
print(testCard)
print(testCard.rank)
print(testCard.suit)

testDeck = Deck()
print(testDeck)
print(testDeck.contents[1])
