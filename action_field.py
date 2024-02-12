
from token import Token
from point import Point
from button import Button
from card import Card
from Global import *


class ActionField:
    def __init__(self, screen):
        self.screen = screen
        self.tokens_on_action_field: list[Token] = []
        self.game_tokens_on_action_field: list[str] = []
        self.player_tokens_on_action_field: list[Token] = []
        self.action_field_button = Button(Point((1000, 500)), "graphics/action_field.png", screen)
        self.buy_card_button = Button(Point(BUY_CARD_BUTTON_COORDINATES), "graphics/buy_card.png", screen,
                                         "graphics/clear_alt_button.png")
        self.take_tokens_button = Button(Point(TAKE_TOKENS_BUTTON_COORDINATES), "graphics/take_tokens.png", screen,
                               "graphics/clear_alt_button.png")
        self.reserve_card_button = Button(Point(RESERVE_CARD_BUTTON_COORDINATES), "graphics/reserve_card.png", screen, "graphics/clear_alt_button.png")
        self.destroy_player_tokens_button = Button(Point(DESTROY_PLAYER_TOKENS_BUTTON_COORDINATES), "graphics/destroy_tokens.png", screen, "graphics/clear_alt_button.png")
        self.cards_on_action_field: list[Card] = []
        self.fill_rows_button = Button(Point(FILL_ROWS_BUTTON_COORDINATES),"graphics/fill_rows.png", screen,"graphics/clear_alt_button.png")

    def update(self):
        self.action_field_button.update()
        self.take_tokens_button.update()
        self.buy_card_button.update()
        self.reserve_card_button.update()
        self.fill_rows_button.update()
        self.destroy_player_tokens_button.update()

    def display_player_tokens(self):
        table = []
        i = 0
        for color in self.player_tokens_on_action_field:
            table.append(Token(color, self.screen, False, Point(ALL_PLAYER_TOKENS_ON_ACTION_FIELD_COORDINATES[i])))
            i += 1
        for token in table:
            token.display()

    def display_game_tokens(self):
        table = []
        i = 0
        for color in self.game_tokens_on_action_field:
            table.append(Token(color, self.screen, False, Point(ALL_GAME_TOKENS_ON_ACTION_FIELD_COORDINATES[i])))
            i += 1
        for token in table:
            token.display()


    def display(self):
        self.action_field_button.display()
        self.buy_card_button.display()
        self.reserve_card_button.display()
        self.take_tokens_button.display()
        self.fill_rows_button.display()
        self.destroy_player_tokens_button.display()
        self.display_player_tokens()
        self.display_game_tokens()
        for card in self.cards_on_action_field:
            card.display()


    def clear_player_tokens_on_action_field(self):
        self.player_tokens_on_action_field = []


    def click_events(self):
        pass


    def add_color_to_player_tokens(self,color):
        self.player_tokens_on_action_field.append(color)
    def add_color_to_game_tokens(self,color):
        self.game_tokens_on_action_field.append(color)


    def remove_and_get_card(self):
        if self.cards_on_action_field:
            return self.cards_on_action_field.pop()

    def remove_and_return_all_game_tokens(self):
        tokens = self.game_tokens_on_action_field
        self.game_tokens_on_action_field = []
        return tokens
    def remove_and_return_all_player_tokens(self):
        tokens = self.player_tokens_on_action_field
        self.player_tokens_on_action_field = []
        return tokens

    def clear_tokens_on_action_field(self):
        self.tokens_on_action_field = []

    def clear_action_field(self):
        self.clear_tokens_on_action_field()
        self.clear_cards_on_action_field()

    def clear_cards_on_action_field(self):
        self.cards_on_action_field = []

    def get_sum_of_tokens(self):
        return len(self.game_tokens_on_action_field)


    def game_token_can_be_added(self, color):
        if len(self.game_tokens_on_action_field) > 2:
            return False
        if len(self.game_tokens_on_action_field) == 2:
            if self.game_tokens_on_action_field[0] == self.game_tokens_on_action_field[1]:
                return False
            if self.game_tokens_on_action_field[0] == color or self.game_tokens_on_action_field[1] == color:
                return False
        if len(self.game_tokens_on_action_field) > 0 and color == "special":
            return False
        if len(self.game_tokens_on_action_field) > 0 and self.game_tokens_on_action_field[0] == "special":
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
            _card.card_button.set_coordinates(Point(CARD_ON_ACTION_FIELD_COORDINATES))
