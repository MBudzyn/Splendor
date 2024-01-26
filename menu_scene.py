
from scene import *
import sys
from stack_of_tokens import StackOfTokens
from action_field import ActionField
from point import Point
from deck_of_cards import DeckOfCards
from row_of_cards_in_ply import RowOfCards
from button import Button
from three_rows import ThreeRows


class MenuScene(Scene):
    def __init__(self, screen, scene_man):
        super().__init__(screen)
        self.scene_man = scene_man
        self.action_field = ActionField(screen)
        self.stack_of_red_tokens = StackOfTokens("red", 7, screen, self.action_field, Point(400,50))
        self.stack_of_blue_tokens = StackOfTokens("blue", 7, screen, self.action_field, Point(500,50))
        self.stack_of_green_tokens = StackOfTokens("green", 7, screen, self.action_field, Point(600, 50))
        self.stack_of_special_tokens = StackOfTokens("special", 5, screen, self.action_field, Point(300, 50))
        self.deck_of_cards = DeckOfCards(screen, 1, "graphics/deck_of_cards.png", Point(1300, 200))
        self.mata = Button(Point(0,0), "graphics/mata.png", screen)
        self.three_rows_of_cards = ThreeRows(RowOfCards(1, screen, self.action_field, self.deck_of_cards),
                                             RowOfCards(2, screen, self.action_field, self.deck_of_cards),
                                             RowOfCards(3, screen, self.action_field, self.deck_of_cards))
        self.action_field.row_of_cards = self.three_rows_of_cards.first_row


    def handle_events(self):
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.stack_of_red_tokens.click_events()
                self.stack_of_blue_tokens.click_events()
                self.stack_of_green_tokens.click_events()
                self.stack_of_special_tokens.click_events()
                self.action_field.click_events()
                self.three_rows_of_cards.click_events()



    def update(self):
        self.stack_of_red_tokens.update()
        self.stack_of_blue_tokens.update()
        self.stack_of_special_tokens.update()
        self.stack_of_green_tokens.update()
        self.three_rows_of_cards.update()
        self.action_field.update()

    def display(self):
        self.mata.display()
        self.stack_of_red_tokens.display(self.screen)
        self.stack_of_blue_tokens.display(self.screen)
        self.stack_of_green_tokens.display(self.screen)
        self.stack_of_special_tokens.display(self.screen)
        self.action_field.display()
        self.three_rows_of_cards.display()

