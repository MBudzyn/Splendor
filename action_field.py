import pygame.image
from token import Token

class ActionField():
    def __init__(self, screen):
        self.screen = screen
        self.action_field = pygame.image.load("graphics/action_field.png")
        self.action_field_rect = self.action_field.get_rect(center=(800,500))
        self.tokens_on_action_field: list[Token] = []
        self.actual_token_position = [750,500]

    def display(self):
        self.screen.blit(self.action_field, self.action_field_rect)
        for _token in self.tokens_on_action_field:
            _token.display(self.screen)

    def can_be_added(self, token):
        if not len(self.tokens_on_action_field) < 3:
            return False
        if len(self.tokens_on_action_field) == 1 and self.tokens_on_action_field[0].color == token.color:
            return True
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
            _token.actual_image_rect.center = self.actual_token_position
            self.actual_token_position[0] += 50

