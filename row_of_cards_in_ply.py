from card import Card
from action_field import ActionField
from deck_of_cards import DeckOfCards
from point import Point


class RowOfCards:
    def __init__(self, lvl, screen, action_field: ActionField, deck_of_cards: DeckOfCards):
        self.lvl = lvl
        self.screen = screen
        self.action_field = action_field
        self.cards: list[Card] = []
        self.deck_of_cards = deck_of_cards
        self.fill_from_deck()
        self.change_cards_coordinates()

    def display(self):
        for _card in self.cards:
            _card.disply()

    def fill_from_deck(self):
        for i in range(4):
            self.add_from_top_of_deck()

    def change_cards_coordinates(self):
        for i in range(len(self.cards)):
            self.cards[i].card_button.set_coordinates(Point(100 + i * 150, self.lvl * 200 +75))

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def add_card(self, card: Card):
        self.cards.append(card)

    def is_possible_to_add_card(self):
        return len(self.cards) <= 3

    def is_full(self):
        return len(self.cards) == 4

    def is_possible_to_remove_card(self):
        return len(self.cards) > 0

    def add_from_top_of_deck(self):
        if self.deck_of_cards.is_possible_to_remove_card() and self.is_possible_to_add_card():
            self.add_card(self.deck_of_cards.get_card_from_top())
