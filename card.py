from button import Button
from point import Point


class Card:
    def __init__(self, coordinate_point: Point, graphics, alt_graphics, screen,
                 lvl, points, color, cost=None):
        self.screen = screen
        self.card_button = Button(coordinate_point, graphics, screen, alt_graphics)
        self.lvl = lvl
        self.points = points
        self.cost = cost
        self.color = color
        self.is_reserved = False
        if self.cost is None:
            self.cost = {"red": 0, "blue": 0, "black": 0, "white": 0, "green": 0}

    def display(self):
        self.card_button.display()

    def set_reserved(self, boolean):
        self.is_reserved = boolean

    def get_reserved(self):
        return self.is_reserved

    def update(self):
        self.card_button.update()

    def set_coordinates(self, coordinate_point: Point):
        self.card_button.set_coordinates(coordinate_point)
