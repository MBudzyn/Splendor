from scene import *
import pygame
import sys
from stack_of_tokens import *

class MenuScene(Scene):
    def __init__(self, screen, scene_man):
        super().__init__(screen)
        self.scene_man = scene_man
        self.stack_of_tokens = StackOfTokens("red", 7, screen)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def render(self):
        self.stack_of_tokens.display(self.screen)
