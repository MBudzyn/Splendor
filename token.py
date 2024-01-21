


class Token:
    def __init__(self, color, screen, is_universal=False, coordinates=None):
        import pygame
        self.color = color
        self.is_universal = is_universal
        self.coordinates = coordinates
        self.screen = screen
        self.graphics = f"graphics/{color}_token3.png"
        self.actual_image = pygame.image.load(self.graphics)
        self.actual_image_rect = self.actual_image.get_rect(center=(600, 600))

    def set_image_to_actual(self):
        import pygame
        self.actual_image_rect = self.actual_image.get_rect(center=pygame.mouse.get_pos())

    def move_token(self):
        import pygame
        if pygame.MOUSEBUTTONDOWN:
            self.set_image_to_actual()

    def update(self):
        self.move_token()


    def display(self, screen):
        screen.blit(self.actual_image, self.actual_image_rect)
