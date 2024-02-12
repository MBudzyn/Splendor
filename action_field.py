
from token import Token
from point import Point
from button import Button
from card import Card


class ActionField:
    def __init__(self, screen):
        self.screen = screen
        self.tokens_on_action_field: list[Token] = []
        self.player_tokens_on_action_field: list[Token] = []
        self.actual_token_position = Point((750, 500))
        self.actual_card_position = Point((750, 600))
        self.action_field_button = Button(Point((1000, 500)), "graphics/action_field.png", screen)
        self.clear_field_button = Button(Point((1000, 420)), "graphics/clear_button.png", screen,
                                         "graphics/clear_alt_button.png")
        self.back_button = Button(Point((1000, 600)), "graphics/back.png", screen, "graphics/clear_alt_button.png")
        self.destroy_player_tokens_button = Button(Point((1250, 500)), "graphics/back.png", screen, "graphics/clear_alt_button.png")
        self.cards_on_action_field: list[Card] = []
        self.fill_rows_button = Button(Point((1000, 300)),"graphics/fill_rows.png", screen,"graphics/clear_alt_button.png")

    def update(self):
        self.action_field_button.update()
        self.clear_field_button.update()
        self.back_button.update()
        self.fill_rows_button.update()
        self.destroy_player_tokens_button.update()

    def display_player_tokens_by_colors(self):
        iterator = 0
        table = []
        for color in self.player_tokens_on_action_field:
            table.append(Token(color, self.screen, False, Point((1200,100 + iterator))))
            iterator += 50
        for token in table:
            token.display()


    def display(self):
        self.action_field_button.display()
        self.clear_field_button.display()
        self.back_button.display()
        self.fill_rows_button.display()
        self.destroy_player_tokens_button.display()
        self.display_player_tokens_by_colors()
        for _token in self.tokens_on_action_field:
            _token.display()
        for _card in self.cards_on_action_field:
            _card.display()

    def clear_player_tokens_on_action_field(self):
        self.player_tokens_on_action_field = []


    def click_events(self):
        if self.clear_field_button.is_colliding_with_mouse():
            self.clear_action_field()
        if self.destroy_player_tokens_button.is_colliding_with_mouse():
            self.clear_player_tokens_on_action_field()

    def add_color_to_player_tokens(self,color):
        self.player_tokens_on_action_field.append(color)

    def remove_and_get_card(self):
        if self.cards_on_action_field:
            return self.cards_on_action_field.pop()

    def remove_and_return_all_tokens(self):
        tokens = self.tokens_on_action_field
        self.clear_tokens_on_action_field()
        return tokens
    def clear_tokens_on_action_field(self):
        self.tokens_on_action_field = []
        self.actual_token_position.set_coordinates(750, 500)

    def clear_action_field(self):
        self.clear_tokens_on_action_field()
        self.clear_cards_on_action_field()

    def clear_cards_on_action_field(self):
        self.cards_on_action_field = []
        self.actual_card_position.set_coordinates(750, 600)

    def token_can_be_added(self, token: Token):
        if token.color == "special" and len(self.tokens_on_action_field) != 0:
            return False
        if not len(self.tokens_on_action_field) < 3:
            return False
        if len(self.tokens_on_action_field) == 1 and self.tokens_on_action_field[0].color == token.color:
            return True
        if len(self.tokens_on_action_field) == 1 and self.tokens_on_action_field[0].color == "special":
            return False
        if len(self.tokens_on_action_field) == 2:
            if self.tokens_on_action_field[0].color == self.tokens_on_action_field[1].color:
                return False
        for _token in self.tokens_on_action_field:
            if _token.color == token.color:
                return False
        return True

    def card_can_be_added(self):
        if not self.cards_on_action_field:
            if self.tokens_on_action_field == [] or self.tokens_on_action_field[0].color == "special":
                return True
        return False



    def add_card(self, _card: Card):
        if self.card_can_be_added():
            self.cards_on_action_field.append(_card)
            _card.card_button.set_coordinates(self.actual_token_position)

    def add_token(self, _token):
        if type(_token) == Token and self.token_can_be_added(_token):
            self.tokens_on_action_field.append(_token)
            _token.button.set_coordinates(self.actual_token_position)
            self.actual_token_position.increase_coordinates(50, 0)
