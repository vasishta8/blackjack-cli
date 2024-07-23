import random

def deck_generation():
    deck = []
    suits = ['♣', '♥', '♠', '♦']
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]
    for suit in suits:
        for value in values:
            deck.append(value+suit)
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

