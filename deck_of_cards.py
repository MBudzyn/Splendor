from card import Card
from point import Point
from button import Button
from action_field import ActionField


class DeckOfCards:
    def __init__(self, screen, lvl, graphics, coordinate_point: Point):
        self.cards: list[Card] = []
        self.number_of_cards = 0
        self.screen = screen
        self.lvl = lvl
        self.coordinate_point = coordinate_point
        self.deck_button = Button(self.coordinate_point, graphics, screen)
        self.load_cards_test(6,"red")


    def display(self):
        self.deck_button.display()

    def load_cards_test(self, number_of_cards, color):
        for i in range(1,number_of_cards + 1):
            self.add_card(Card(Point(0,0),f"graphics/card{i}.png", f"graphics/card{i}.png",self.screen, self.lvl,0,color))


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
