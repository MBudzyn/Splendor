
from button import Button
from point import Point
class Card:
    def __init__(self, coordinate_point: Point, graphics, alt_graphics, screen,
                 lvl, points, color):
        self.screen = screen
        self.card_button = Button(coordinate_point, graphics, alt_graphics, screen)
        self.lvl = lvl
        self.points = points
        self.cost = {"red": 0, "blue": 0, "black": 0, "white": 0, "green": 0}
        self.color = color
