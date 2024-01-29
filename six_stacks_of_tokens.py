from stack_of_tokens import StackOfTokens
from token import Token
from action_field import ActionField



class SixStackOfTokens:
    def __init__(self,
                 blue_stack: StackOfTokens,
                 green_stack: StackOfTokens,
                 red_stack: StackOfTokens,
                 white_stack: StackOfTokens,
                 black_stack: StackOfTokens,
                 special_stack: StackOfTokens,
                 screen,
                 action_field: ActionField):
        self.action_field = action_field
        self.screen = screen
        self.stacks: dict[str, StackOfTokens] = {"blue": blue_stack,
                                                 "green": green_stack,
                                                 "red": red_stack,
                                                 "white": white_stack,
                                                 "black": black_stack,
                                                 "special": special_stack}

    def add_token_to_correct_stack(self, token: Token):
        if token is not None:
            self.stacks[token.color].add_token()

    def display(self):
        for stack in self.stacks.values():
            stack.display()

    def click_events_on_action_field(self):
        if self.action_field.back_button.is_colliding_with_mouse():
            for token in self.action_field.remove_and_return_all_tokens():
                self.add_token_to_correct_stack(token)

    def update(self):
        for stack in self.stacks.values():
            stack.update()

    def click_events(self):
        self.click_events_on_action_field()
        for stack in self.stacks.values():
            stack.click_events()
