import pygame.image
from token import Token
from point import Point
from button import Button

class ActionField():
    def __init__(self, screen):
        self.screen = screen
        self.tokens_on_action_field: list[Token] = []
        self.actual_token_position = Point(750, 500)
        self.action_field_button = Button(Point(800, 500), "graphics/action_field.png", screen)
        self.clear_field_button = Button(Point(800, 420), "graphics/clear_button.png", screen)


    def display(self):
        self.action_field_button.display()
        self.clear_field_button.display()
        for _token in self.tokens_on_action_field:
            _token.display(self.screen)

    def click_events(self):
        if self.clear_field_button.is_colliding_with_mouse():
            self.clear_tokens_on_action_field()

    def clear_tokens_on_action_field(self):
        self.tokens_on_action_field = []
        self.actual_token_position.set_coordinates(750, 500)

    def can_be_added(self, token):
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


    def add_token(self, _token):
        if type(_token) == Token and self.can_be_added(_token):
            self.tokens_on_action_field.append(_token)
            _token.actual_image_rect.center = self.actual_token_position.get_coordinates()
            self.actual_token_position.increase_coordinates(50,0)

