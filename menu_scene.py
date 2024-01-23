
from scene import *
import sys
from stack_of_tokens import StackOfTokens
from action_field import ActionField
from point import Point


class MenuScene(Scene):
    def __init__(self, screen, scene_man):
        super().__init__(screen)
        self.scene_man = scene_man
        self.action_field = ActionField(screen)
        self.stack_of_red_tokens = StackOfTokens("red", 7, screen, self.action_field, Point(400,400))
        self.stack_of_blue_tokens = StackOfTokens("blue", 7, screen, self.action_field, Point(500,400))


    def handle_events(self):
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stack_of_red_tokens.click_events()
                self.stack_of_blue_tokens.click_events()
                self.action_field.click_events()


    def update(self):
        self.stack_of_red_tokens.update()
        self.stack_of_blue_tokens.update()

    def display(self):
        self.stack_of_red_tokens.display(self.screen)
        self.stack_of_blue_tokens.display(self.screen)
        self.action_field.display()
