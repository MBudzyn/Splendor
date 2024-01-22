import pygame.image


class ActionField():
    def __init__(self, screen):
        self.screen = screen
        self.action_field = pygame.image.load("graphics/action_field.png")
        self.action_field_rect = self.action_field.get_rect(center=(800,500))

    def display(self):
        self.screen.blit(self.action_field, self.action_field_rect)