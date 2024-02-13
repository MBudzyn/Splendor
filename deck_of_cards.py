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
        self.load_cards_test(8, "red")

    def display(self):
        self.deck_button.display()

    def load_cards_test(self, number_of_cards, color):
        for i in range(1, number_of_cards + 1):
            self.add_card(
                Card(Point((200, 200)), f"graphics/card{i % 6 + 1}.png", f"graphics/card_frame.png", self.screen,
                     self.lvl, 0, color))
        self.add_card(
            Card(Point((200, 200)), f"graphics/blue_card1.png", f"graphics/card_frame.png", self.screen,
                 self.lvl, 0, "blue"))
        self.add_card(
            Card(Point((200, 200)), f"graphics/green_card1.png", f"graphics/card_frame.png", self.screen,
                 self.lvl, 0, "green"))
        self.add_card(
            Card(Point((200, 200)), f"graphics/white_card1.png", f"graphics/card_frame.png", self.screen,
                 self.lvl, 0, "white"))
        self.add_card(
            Card(Point((200, 200)), f"graphics/red_card1.png", f"graphics/card_frame.png", self.screen,
                 self.lvl, 0, "red"))
        



    def is_colliding_with_mouse(self) -> bool:
        return self.deck_button.is_colliding_with_mouse()

    def delete_from_top(self):
        self.cards = self.cards[:-1]
        self.number_of_cards -= 1

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.number_of_cards += 1

    def is_possible_to_remove_card(self) -> bool:
        return self.number_of_cards > 0

    def get_card_from_top(self) -> Card:
        return self.cards[-1]

    def remove_card_from_top(self) -> Card:
        if self.is_possible_to_remove_card():
            card = self.get_card_from_top()
            self.delete_from_top()
            return card

