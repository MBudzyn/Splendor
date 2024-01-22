import pygame.image
from token import Token

class ActionField():
    def __init__(self, screen):
        self.screen = screen
        self.action_field = pygame.image.load("graphics/action_field.png")
        self.action_field_rect = self.action_field.get_rect(center=(800,500))
        self.tokens_on_action_field: list[Token] = []

    def display(self):
        self.screen.blit(self.action_field, self.action_field_rect)
        for _token in self.tokens_on_action_field:
            _token.display(self.screen)

    def add_token(self, _token):
        self.tokens_on_action_field.append(_token)
        _token.actual_image_rect.center = self.action_field_rect.center

