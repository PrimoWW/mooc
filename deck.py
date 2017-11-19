"""
模拟洗扑克牌的过程
"""
from collections import namedtuple
from random import choice, shuffle

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck():
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'diamonds, spades, cubes, hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks
                                       for suit in self.suits]
    def __len__(self):
        return len(self.cards)

    def get_a_random_card(self):
        return choice(self.cards)

    def shuffle_cards(self):
        shuffle(self.cards)

c = FrenchDeck()
print(c.cards)
c.shuffle_cards()
print(c.cards)