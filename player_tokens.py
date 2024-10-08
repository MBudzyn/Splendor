from token import Token
from color_dict import ColorDict
from button import Button
from point import Point
from Global import *
from action_field import ActionField


class PlayerTokens:
    def __init__(self, screen, action_field: ActionField):
        self.action_field = action_field
        self.screen = screen
        self.tokens: ColorDict = ColorDict(True)
        self.tokens_graphics = {"red": [f"graphics/red_token{i}.png" for i in range(8)],
                                "blue": [f"graphics/blue_token{i}.png" for i in range(8)],
                                "green": [f"graphics/green_token{i}.png" for i in range(8)],
                                "black": [f"graphics/black_token{i}.png" for i in range(8)],
                                "white": [f"graphics/white_token{i}.png" for i in range(8)],
                                "special": [f"graphics/special_token{i}.png" for i in range(8)]}

        self.stacks_buttons = {
            "red": Button(Point(PLAYER_RED_STACK_COORDINATES), f"graphics/red_token0.png",
                          screen, "graphics/token_highlight.png"),
            "blue": Button(Point(PLAYER_BLUE_STACK_COORDINATES), f"graphics/blue_token0.png",
                           screen, "graphics/token_highlight.png"),
            "green": Button(Point(PLAYER_GREEN_STACK_COORDINATES),f"graphics/green_token0.png",
                            screen, "graphics/token_highlight.png"),
            "black": Button(Point(PLAYER_BLACK_STACK_COORDINATES), f"graphics/black_token0.png",
                            screen, "graphics/token_highlight.png"),
            "white": Button(Point(PLAYER_WHITE_STACK_COORDINATES), f"graphics/white_token0.png",
                            screen, "graphics/token_highlight.png"),
            "special": Button(Point(PLAYER_SPECIAL_STACK_COORDINATES), f"graphics/special_token0.png",
                              screen, "graphics/token_highlight.png")}

    def display(self):
        for stack_button in self.stacks_buttons.values():
            stack_button.display()

    def get_sum_of_tokens(self):
        return self.tokens.get_sum_of_tokens()

    def clean_field_click_event(self):
        if self.action_field.clean_field_button.is_colliding_with_mouse():
            tokens = self.action_field.remove_and_return_all_player_tokens()
            for color in tokens:
                self.add_token(color)

    def update(self):
        self.set_correct_image_to_stacks()
        for stack_button in self.stacks_buttons.values():
            stack_button.update()

    def set_correct_image_to_stacks(self):
        for color, stack in self.stacks_buttons.items():
            stack.set_graphic(self.tokens_graphics[color][self.tokens.get_dict()[color]])

    def add_token(self, color):
        self.tokens.increase_color_value(color, 1)

    def is_possible_to_remove_token(self, color):
        if self.tokens.get_dict()[color] > 0:
            return True
        return False

    def add_token_to_action_field(self, color):
        self.action_field.add_color_to_player_tokens(color)

    def if_possible_place_in_action_field(self, color):
        if self.is_possible_to_remove_token(color) and self.action_field.player_token_can_be_added():
            self.add_token_to_action_field(color)
            self.remove_token(color)
            
    def remove_token(self, color):
        if self.is_possible_to_remove_token(color):
            self.tokens.increase_color_value(color, -1)

    def take_tokens_click_event(self):
        if self.action_field.take_tokens_button.is_colliding_with_mouse() and self.action_field.cards_on_action_field == []:
            if self.get_sum_of_tokens() + self.action_field.get_sum_of_tokens() <= 10 and self.action_field.game_tokens_can_be_get():
                for color in self.action_field.remove_and_return_all_game_tokens():
                    self.add_token(color)
                self.action_field.next_turn()



    def reserve_card_click_event(self):
        if self.action_field.reserve_card_button.is_colliding_with_mouse():
            if self.get_sum_of_tokens() + self.action_field.get_sum_of_tokens() <= 10:
                for color in self.action_field.remove_and_return_all_game_tokens():
                    self.add_token(color)


    def click_events(self):
        self.reserve_card_click_event()
        self.take_tokens_click_event()
        self.clean_field_click_event()
        for color, stack_button in self.stacks_buttons.items():
            if stack_button.is_colliding_with_mouse():
                self.if_possible_place_in_action_field(color)


