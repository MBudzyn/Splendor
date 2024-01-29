from token import Token
from color_dict import ColorDict
from button import Button
from point import Point


class PlayerTokens:
    def __init__(self, screen):
        self.screen = screen
        self.tokens: ColorDict = ColorDict()
        self.tokens_graphics = {"red": [f"graphics/red_token{i}.png" for i in range(8)],
                                "blue": [f"graphics/blue_token{i}.png" for i in range(8)],
                                "green": [f"graphics/green_token{i}.png" for i in range(8)],
                                "black": [f"graphics/black_token{i}.png" for i in range(8)],
                                "white": [f"graphics/white_token{i}.png" for i in range(8)],
                                "special": [f"graphics/special_token{i}.png" for i in range(8)]}

        self.stacks_buttons = {
            "red": Button(Point(700, 700), f"graphics/red_token0.png",
                          screen, "graphics/token_highlight.png"),
            "blue": Button(Point(775, 700), f"graphics/blue_token0.png",
                           screen, "graphics/token_highlight.png"),
            "green": Button(Point(850, 700),f"graphics/green_token0.png",
                            screen, "graphics/token_highlight.png"),
            "black": Button(Point(925, 700), f"graphics/black_token0.png",
                            screen, "graphics/token_highlight.png"),
            "white": Button(Point(1000, 700), f"graphics/white_token0.png",
                            screen, "graphics/token_highlight.png"),
            "special": Button(Point(1075, 700), f"graphics/special_token0.png",
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

    def add_token(self, token: Token):
        self.tokens.increase_color_value(token.color, 1)

    def is_possible_to_remove_token(self, color):
        if self.tokens.get_dict()[color] > 0:
            return True
        return False

    def remove_token(self, color):
        if self.is_possible_to_remove_token(color):
            self.tokens.increase_color_value(color, -1)

    def click_events(self):
        for color, stack_button in self.stacks_buttons.items():
            if stack_button.is_colliding_with_mouse():
                self.remove_token(color)


