from row_of_cards_in_ply import RowOfCards
from card import Card
from action_field import ActionField
class ThreeRows:
    def __init__(self, first_row, second_row, third_row, action_field: ActionField):
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row
        self.action_field = action_field
        self.rows: dict[int, RowOfCards] = {self.first_row.lvl: self.first_row,
                                            self.second_row.lvl: self.second_row,
                                            self.third_row.lvl: self.third_row}


    def add_card_to_correct_row(self, card):
        if card is not None:
            self.rows[card.lvl].add_card(card)
            self.change_cards_coordinates_to_correct()

    def clean_field_click_event(self):
        if self.action_field.clean_field_button.is_colliding_with_mouse():
            card = self.action_field.get_card()
            if card is not None and not card.get_reserved():
                self.add_card_to_correct_row(self.action_field.remove_and_get_card())


    def click_events_on_action_field(self):
        self.clean_field_click_event()
        if self.action_field.destroy_player_tokens_button.is_colliding_with_mouse():
            self.add_card_to_correct_row(self.action_field.remove_and_get_card())







    def change_cards_coordinates_to_correct(self):
        for row in self.rows.values():
            row.change_cards_coordinates_to_correct()

    def display(self):
        for row in self.rows.values():
            row.display()

    def update(self):
        for row in self.rows.values():
            row.update()
        if not self.action_field.cards_on_action_field:
            self.fill_from_decks()

    def click_events(self):
        self.click_events_on_action_field()
        for row in self.rows.values():
            row.click_events()


    def fill_from_decks(self):
        for row in self.rows.values():
            row.fill_from_deck()
            row.change_cards_coordinates_to_correct()
