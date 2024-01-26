from stack_of_tokens import StackOfTokens
from token import Token

class SixStackOfTokens:
    def __init__(self,blue_stack, green_stack, red_stack, white_stack, black_stack, special_stack, screen):
        self.screen = screen
        self.stacks: dict[str, StackOfTokens] = {"blue" : blue_stack,
                                                 "green" : green_stack,
                                                 "red" : red_stack,
                                                 "white" : white_stack,
                                                 "black" : black_stack,
                                                 "special" : special_stack}

    def add_token_to_correct_stack(self, token):
        self.stacks[token.color].add_token()

    def display(self):
        for stack in self.stacks.values():
            stack.display(self.screen)

    def update(self):
        for stack in self.stacks.values():
            stack.update()

    def click_events(self):
        for stack in self.stacks.values():
            stack.click_events()

