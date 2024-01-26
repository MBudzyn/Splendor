from row_of_cards_in_ply import RowOfCards
from card import Card
class ThreeRows:
    def __init__(self, first_row, second_row, third_row):
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row
        self.rows: dict[int, RowOfCards] = {self.first_row.lvl: self.first_row,
                                            self.second_row.lvl: self.second_row,
                                            self.third_row.lvl: self.third_row}

    def add_card_to_correct_row(self, card: Card):
        self.rows[card.lvl].add_card(card)

    def display(self):
        for row in self.rows.values():
            row.display()
    def update(self):
        for row in self.rows.values():
            row.update()

    def click_events(self):
        for row in self.rows.values():
            row.click_events()
