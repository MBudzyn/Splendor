from stack_of_tokens import StackOfTokens
from token import Token



class SixStackOfTokens:
    def __init__(self,
                 blue_stack: StackOfTokens,
                 green_stack: StackOfTokens,
                 red_stack: StackOfTokens,
                 white_stack: StackOfTokens,
                 black_stack: StackOfTokens,
                 special_stack: StackOfTokens,
                 screen):

        self.screen = screen
        self.stacks: dict[str, StackOfTokens] = {"blue": blue_stack,
                                                 "green": green_stack,
                                                 "red": red_stack,
                                                 "white": white_stack,
                                                 "black": black_stack,
                                                 "special": special_stack}

    def add_token_to_correct_stack(self, token: Token):
        self.stacks[token.color].add_token()

    def display(self):
        for stack in self.stacks.values():
            stack.display()



    def update(self):
        for stack in self.stacks.values():
            stack.update()

    def click_events(self):
        for stack in self.stacks.values():
            stack.click_events()
