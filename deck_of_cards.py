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

    def is_colliding_with_mouse(self) -> bool:
        return self.deck_button.is_colliding_with_mouse()

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.number_of_cards += 1

    def is_possible_to_remove_card(self) -> bool:
        return self.number_of_cards > 0

    def get_card_from_top(self):
        if self.is_possible_to_remove_card():
            self.number_of_cards -= 1
            return self.cards.pop()
