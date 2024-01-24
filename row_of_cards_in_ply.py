from card import Card
from action_field import ActionField
from deck_of_cards import DeckOfCards


class RowOfCards:
    def __init__(self, lvl, screen, action_field: ActionField, deck_of_cards: DeckOfCards):
        self.lvl = lvl
        self.screen = screen
        self.action_field = action_field
        self.cards: list[Card] = []
        self.deck_of_cards = deck_of_cards

    def display(self):
        for _card in self.cards:
            _card.disply()
