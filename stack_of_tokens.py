from token import Token
from point import Point
from action_field import ActionField
from button import Button



class StackOfTokens:
    def __init__(self, color: str, amount: int, screen, action_field: ActionField,
                 coordinate_point: Point, is_universal=False):

        self.color = color
        self.amount = amount
        self.is_universal = is_universal
        self.tokens = [Token(color, is_universal) for _ in range(amount)]
        self.graphics_links = [f"graphics/{color}_token{i}.png" for i in range(8)]
        self.max_amount = 7
        self.coordinate_point = coordinate_point
        self.stack_button = Button(self.coordinate_point, f"graphics/{color}_token0.png",
                                   screen, "graphics/token_highlight.png")
        self.set_image_to_actual()
        self.screen = screen
        self.action_field = action_field

    def is_empty(self):
        return self.amount == 0

    def set_image_to_actual(self):
        self.stack_button.set_graphic(self.graphics_links[self.amount])

    def update(self):
        self.set_image_to_actual()
        self.stack_button.update()

    def click_events(self):
        if self.stack_button.is_colliding_with_mouse():
            self.action_field.add_token(self.get_token())
            self.update()

    def display(self):
        self.stack_button.display()

    def is_possible_to_add_token_to_action_field(self):
        if len(self.action_field.tokens_on_action_field) == 1 and \
                self.action_field.tokens_on_action_field[0].color == self.color and \
                self.is_not_possible_to_take_second():
            return False
        if self.action_field.cards_on_action_field:
            return False
        return not self.is_empty() and self.action_field.token_can_be_added(self.tokens[-1])

    def is_not_possible_to_take_second(self):
        return self.amount < 3

    def is_possible_to_add_token(self):
        return self.amount < self.max_amount

    def delete_token(self):
        if self.is_possible_to_add_token_to_action_field():
            self.tokens.pop()
            self.amount -= 1

    def get_token(self):
        if self.is_possible_to_add_token_to_action_field():
            token = self.tokens[-1]
            self.delete_token()
            return token

    def add_token(self):
        if self.is_possible_to_add_token():
            self.tokens.append(Token(self.color, self.is_universal))
            self.amount += 1
