import pygame


class Button:
    def __init__(self, coordinate_point, graphics, screen, alt_graphics = None):

        self.screen = screen
        self.coordinate_point = coordinate_point
        self.graphics = pygame.image.load(graphics)
        self.have_alt_graphic = alt_graphics is not None
        self.alt_graphics = alt_graphics
        self.button = self.graphics
        self.button_rect = self.button.get_rect(center=self.coordinate_point.get_coordinates())
        self.is_highlighted = False
        if self.have_alt_graphic:
            self.alt_graphics = pygame.image.load(self.alt_graphics)
            self.highlighted_button = self.alt_graphics
            self.highlighted_button_rect = self.highlighted_button.get_rect(center=self.coordinate_point.get_coordinates())

    def display(self):
        self.screen.blit(self.button, self.button_rect)
        if self.is_highlighted:
            self.screen.blit(self.highlighted_button, self.highlighted_button_rect)

    def is_colliding_with_mouse(self):
        return self.button_rect.collidepoint(pygame.mouse.get_pos())

    def highlight(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) and self.have_alt_graphic:
            self.is_highlighted = True
        else:
            self.is_highlighted = False

    def update(self):
        self.highlight()

    def set_coordinates_to_mouse(self):
        self.button_rect.center = pygame.mouse.get_pos()

    def set_coordinates(self, coordinate_point):
        self.button_rect = self.button.get_rect(center=coordinate_point.get_coordinates())
        if self.have_alt_graphic:
            self.highlighted_button_rect = self.highlighted_button.get_rect(center=coordinate_point.get_coordinates())


