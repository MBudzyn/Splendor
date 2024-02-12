from token import Token
from color_dict import ColorDict
from button import Button
from point import Point
from Global import *
from action_field import ActionField


class GameTokens:
    def __init__(self, screen, action_field: ActionField):
        self.action_field = action_field
        self.screen = screen
        self.tokens: ColorDict = ColorDict()
        self.tokens_graphics = {"red": [f"graphics/red_token{i}.png" for i in range(8)],
                                "blue": [f"graphics/blue_token{i}.png" for i in range(8)],
                                "green": [f"graphics/green_token{i}.png" for i in range(8)],
                                "black": [f"graphics/black_token{i}.png" for i in range(8)],
                                "white": [f"graphics/white_token{i}.png" for i in range(8)],
                                "special": [f"graphics/special_token{i}.png" for i in range(8)]}

        self.stacks_buttons = {
            "red": Button(Point(GAME_RED_STACK_COORDINATES), f"graphics/red_token0.png",
                          screen, "graphics/token_highlight.png"),
            "blue": Button(Point(GAME_BLUE_STACK_COORDINATES), f"graphics/blue_token0.png",
                           screen, "graphics/token_highlight.png"),
            "green": Button(Point(GAME_GREEN_STACK_COORDINATES), f"graphics/green_token0.png",
                            screen, "graphics/token_highlight.png"),
            "black": Button(Point(GAME_WHITE_STACK_COORDINATES), f"graphics/black_token0.png",
                            screen, "graphics/token_highlight.png"),
            "white": Button(Point(GAME_BLACK_STACK_COORDINATES), f"graphics/white_token0.png",
                            screen, "graphics/token_highlight.png"),
            "special": Button(Point(GAME_SPECIAL_STACK_COORDINATES), f"graphics/special_token0.png",
                              screen, "graphics/token_highlight.png")}

    def display(self):
        for stack_button in self.stacks_buttons.values():
            stack_button.display()

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
        self.action_field.add_color_to_game_tokens(color)

    def if_possible_place_in_action_field(self, color):
        if self.is_possible_to_remove_token(color) and self.action_field.game_token_can_be_added(color):
            self.add_token_to_action_field(color)
            self.remove_token(color)

    def remove_token(self, color):
        if self.is_possible_to_remove_token(color):
            self.tokens.increase_color_value(color, -1)

    def click_events(self):
        self.click_events_on_action_field()
        for color, stack_button in self.stacks_buttons.items():
            if stack_button.is_colliding_with_mouse():
                self.if_possible_place_in_action_field(color)

    def click_events_on_action_field(self):
        if self.action_field.back_button.is_colliding_with_mouse():
            for color in self.action_field.remove_and_return_all_game_tokens():
                self.add_token(color)
