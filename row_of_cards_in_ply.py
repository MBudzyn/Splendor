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
        self.change_cards_coordinates_to_correct()

    def display(self):
        for _card in self.cards:
            _card.display()

    def fill_from_deck(self):
        for i in range(4):
            self.add_from_top_of_deck()

    def change_cards_coordinates_to_correct(self):
        for i in range(len(self.cards)):
            self.cards[i].card_button.set_coordinates(Point(100 + i * 150, self.lvl * 200 + 75))

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def is_possible_to_place_in_action_field(self):
        return self.action_field.card_can_be_added()

    def add_card(self, card: Card):
        self.cards.append(card)

    def place_in_action_field(self, card: Card):
        if self.is_possible_to_place_in_action_field():
            self.action_field.add_card(card)
            self.remove_card(card)

    def is_possible_to_add_card(self):
        return not self.is_full()

    def is_full(self):
        return len(self.cards) == 4

    def update(self):
        for _card in self.cards:
            _card.update()

    def is_possible_to_remove_card(self):
        return len(self.cards) > 0

    def click_events(self):
        for card in self.cards:
            if card.card_button.is_colliding_with_mouse():
                self.place_in_action_field(card)

    def add_from_top_of_deck(self):
        if self.deck_of_cards.is_possible_to_remove_card() and self.is_possible_to_add_card():
            self.add_card(self.deck_of_cards.remove_card_from_top())
