
from buttons import Buttons

class Card:
    def __init__(self, center_coordinates, graphics, alt_graphics, screen,
                 lvl, points, color):
        self.screen = screen
        self.card_button = Buttons(center_coordinates, graphics, alt_graphics, screen)
        self.lvl = lvl
        self.points = points
        self.cost = {"red": 0, "blue": 0, "black": 0, "white": 0, "green": 0}
        self.color = color
