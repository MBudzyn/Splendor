
class Button:
    def __init__(self, coordinate_point, graphics, screen, alt_graphics = None):
        import pygame
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

    def set_graphic(self, graphic):
        import pygame
        self.graphics = pygame.image.load(graphic)
        self.button = self.graphics
        self.button_rect = self.button.get_rect(center=self.coordinate_point.get_coordinates())

    def is_colliding_with_mouse(self):
        import pygame
        return self.button_rect.collidepoint(pygame.mouse.get_pos())

    def highlight(self):
        import pygame
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) and self.have_alt_graphic:
            self.is_highlighted = True
        else:
            self.is_highlighted = False

    def update(self):
        self.highlight()

    def set_coordinates_to_mouse(self):
        import pygame
        self.button_rect.center = pygame.mouse.get_pos()

    def set_coordinates(self, coordinate_point):
        self.button_rect = self.button.get_rect(center=coordinate_point.get_coordinates())
        if self.have_alt_graphic:
            self.highlighted_button_rect = self.highlighted_button.get_rect(center=coordinate_point.get_coordinates())


