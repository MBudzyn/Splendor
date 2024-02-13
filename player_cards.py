from card import Card
from point import Point
from action_field import ActionField
from Global import *


class PlayerCards:
    def __init__(self, action_field: ActionField):
        self.cards_container: dict[str, list[Card]] = {"red": [], "blue": [], "black": [], "white": [], "green": []}
        self.dict_with_x_coordinates = {"red": 1200, "blue": 450, "black": 600, "white": 750, "green": 900}
        self.points_sum = 0
        self.discount_dict = {"red": 0, "blue": 0, "black": 0, "white": 0, "green": 0}
        self.action_field = action_field

    def update_discount(self, card: Card):
        self.discount_dict[card.color] += 1

    def update_points_sum(self, card: Card):
        self.points_sum += card.points

    def buy_card_click_event(self):
        if self.action_field.buy_card_button.is_colliding_with_mouse():
            self.add_cart(self.action_field.remove_and_get_card())

    def add_cart(self, card: Card):
        if card is not None:
            self.update_discount(card)
            self.update_points_sum(card)
            card.set_coordinates(Point((self.dict_with_x_coordinates[card.color],
                                        PLAYER_CARDS_Y_COORDINATES[len(self.cards_container[card.color])])))
            self.cards_container[card.color].append(card)

    def get_sum_of_points(self):
        return self.points_sum

    def get_discount_dict(self):
        return self.discount_dict

    def display(self):
        for cards in self.cards_container.values():
            for card in cards:
                card.display()

    def click_events(self):
        self.buy_card_click_event()

    def update(self):
        for cards in self.cards_container.values():
            for card in cards:
                card.update()
