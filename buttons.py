import pygame


class Buttons:
    def __init__(self, coordinate_point, graphics, screen, alt_graphics = None):

        self.screen = screen
        self.coordinate_point = coordinate_point
        self.graphics = pygame.image.load(graphics)
        if alt_graphics is not None:
            self.alt_graphics = pygame.image.load(alt_graphics)
        self.button = self.graphics
        self.button_rect = self.button.get_rect(center=self.coordinate_point.get_coordinates())

    def display(self):
        self.screen.blit(self.button, self.button_rect)

    def is_colliding_with_mouse(self):
        return self.button_rect.collidepoint(pygame.mouse.get_pos())

    def highlight(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.change_to_alt()
        else:
            self.change_to_normal()

    def update(self):
        self.highlight()

    def set_coordinates_to_mouse(self):
        self.button_rect.center = pygame.mouse.get_pos()

    def change_to_alt(self):
        self.button = self.alt_graphics

    def change_to_normal(self):
        self.button = self.graphics
