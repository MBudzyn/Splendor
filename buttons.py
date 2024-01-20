import pygame


class Buttons:
    def __init__(self, center_coordinates, graphics, alt_graphics, screen):

        self.screen = screen
        self.center_coordinates = center_coordinates
        self.graphics = pygame.image.load(graphics)
        self.alt_graphics = pygame.image.load(alt_graphics)
        self.button = self.graphics
        self.button_rect = self.button.get_rect(center=self.center_coordinates)

    def display(self):
        self.screen.blit(self.button, self.button_rect)

    def highlight(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.change_to_alt()
        else:
            self.change_to_normal()

    def change_to_alt(self):
        self.button = self.alt_graphics

    def change_to_normal(self):
        self.button = self.graphics
