from card import Card
from point import Point


class PlayerCards:
    def __init__(self):
        self.cards_container: dict[str, list[Card]] = {"red": [], "blue": [], "black": [], "white": [], "green": []}
        self.dict_with_x_coordinates = {"red": 300, "blue": 450, "black": 600, "white": 750, "green": 900}
        self.points_sum = 0
        self.discount_dict = {"red": 0, "blue": 0, "black": 0, "white": 0, "green": 0}

    def update_discount(self, card: Card):
        self.discount_dict[card.color] += 1

    def update_points_sum(self, card: Card):
        self.points_sum += card.points

    def add_cart(self, card: Card):
        self.update_discount(card)
        self.update_points_sum(card)
        card.set_coordinates(Point(self.dict_with_x_coordinates[card.color],
                                   len(self.cards_container[card.color] * 100)))
        self.cards_container[card.color].append(card)

    def get_sum_of_points(self):
        return self.points_sum

    def get_discount_dict(self):
        return self.discount_dict
