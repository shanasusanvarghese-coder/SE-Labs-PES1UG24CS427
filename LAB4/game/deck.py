import random
from game.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        self.cards = [Card(rank, suit) for suit in suits for rank in range(2, 15)]
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.shuffle()
        return self.cards.pop()

    @property
    def remaining(self):
        return len(self.cards)
