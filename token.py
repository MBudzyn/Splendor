


class Token:
    def __init__(self, color, screen, is_universal=False, coordinates=None):
        import pygame
        self.color = color
        self.is_universal = is_universal
        self.coordinates = coordinates
        self.screen = screen
        self.graphics = f"graphics/{color}_token.png"
        self.actual_image = pygame.image.load(self.graphics)
        self.actual_image_rect = self.actual_image.get_rect(center=(600, 600))


    def display(self, screen):
        screen.blit(self.actual_image, self.actual_image_rect)
