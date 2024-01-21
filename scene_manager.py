
from menu_scene import MenuScene
class SceneManager:
    def __init__(self):
        import pygame
        pygame.init()
        self.screen = pygame.display.set_mode((1500, 800))
        self.clock = pygame.time.Clock()
        self.menu_scene = MenuScene(self.screen, self)

        self.current_scene = self.menu_scene

    def handle_events(self):
        self.current_scene.handle_events()

    def update(self):
        self.current_scene.update()

    def render(self):
        import pygame
        self.current_scene.render()

        pygame.display.flip()
        self.clock.tick(60)
