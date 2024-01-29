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
            "blue": Button(Point(750, 700), f"graphics/blue_token0.png",
                           screen, "graphics/token_highlight.png"),
            "green": Button(Point(800, 700),f"graphics/green_token0.png",
                            screen, "graphics/token_highlight.png"),
            "black": Button(Point(850, 700), f"graphics/black_token0.png",
                            screen, "graphics/token_highlight.png"),
            "white": Button(Point(900, 700), f"graphics/white_token0.png",
                            screen, "graphics/token_highlight.png"),
            "special": Button(Point(950, 700), f"graphics/special_token0.png",
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

    def is_possible_to_remove_token(self, token: Token):
        if self.tokens.get_dict()[token.color] > 0:
            return True
        return False

    def remove_token(self, token: Token):
        self.tokens.increase_color_value(token.color, -1)
