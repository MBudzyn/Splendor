from card import Card
from point import Point
from action_field import ActionField
from Global import *


class PlayerReservedCards:
    def __init__(self, action_field: ActionField):
        self.cards: list[Card] = []
        self.action_field = action_field

    def is_full(self):
        return len(self.cards) == 3

    def reserve_card_click_event(self):
        if self.action_field.reserve_card_button.is_colliding_with_mouse():
            if self.can_be_added():
                self.add_card(self.action_field.remove_and_get_card())
                self.action_field.next_turn()


    def add_card(self, card: Card):
        if card is not None and self.can_be_added():
            card.set_reserved(True)
            self.cards.append(card)

    def clean_field_click_event(self):
        if self.action_field.clean_field_button.is_colliding_with_mouse():
            card = self.action_field.get_card()
            if card is not None and card.get_reserved():
                self.add_card(self.action_field.remove_and_get_card())





    def display(self):
        for i in range(len(self.cards)):
            self.cards[i].set_coordinates(Point(PLAYER_RESERVED_CARDS_COORDINATES[i]))
        for card in self.cards:
            card.display()

    def can_be_added(self):
        return not self.is_full()

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def is_possible_to_place_in_action_field(self):
        return self.action_field.card_can_be_added()

    def place_in_action_field(self, card: Card):
        if self.is_possible_to_place_in_action_field():
            self.action_field.add_card(card)
            self.remove_card(card)

    def click_events(self):
        self.clean_field_click_event()
        self.reserve_card_click_event()
        for card in self.cards:
            if card.card_button.is_colliding_with_mouse():
                self.place_in_action_field(card)

    def update(self):
        for card in self.cards:
            card.update()
