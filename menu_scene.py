
from scene import *
import sys
from stack_of_tokens import StackOfTokens


class MenuScene(Scene):
    def __init__(self, screen, scene_man):
        super().__init__(screen)
        self.scene_man = scene_man
        self.stack_of_tokens = StackOfTokens("red", 7, screen)


    def handle_events(self):
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stack_of_tokens.click_events()


    def update(self):
        self.stack_of_tokens.update()

    def render(self):
        self.stack_of_tokens.display(self.screen)
