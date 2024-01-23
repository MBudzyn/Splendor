from card import Card
from point import Point
from button import Button
class DeckOfCards:
    def __init__(self, screen, lvl, graphics, coordinate_point: Point):
        self.cards: list[Card] = []
        self.number_of_cards = 0
        self.screen = screen
        self.lvl = lvl
        self.coordinate_point = coordinate_point
        self.deck_button = Button(self.coordinate_point, graphics, screen)

    def display(self):
        self.deck_button.display()


