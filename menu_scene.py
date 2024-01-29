
from scene import *
import sys
from stack_of_tokens import StackOfTokens
from action_field import ActionField
from point import Point
from deck_of_cards import DeckOfCards
from row_of_cards_in_ply import RowOfCards
from button import Button
from three_rows import ThreeRows
from six_stacks_of_tokens import SixStackOfTokens
from player import Player


class MenuScene(Scene):
    def __init__(self, screen, scene_man):
        super().__init__(screen)
        self.screen = screen
        self.scene_man = scene_man
        self.player_one = Player("Player One", screen)
        self.action_field = ActionField(screen)
        self.first_deck_of_cards = DeckOfCards(screen, 1, "graphics/deck_of_cards.png", Point(1300, 200))
        self.second_deck_of_cards = DeckOfCards(screen, 2, "graphics/deck_of_cards.png", Point(1300, 200))
        self.third_deck_of_cards = DeckOfCards(screen, 3, "graphics/deck_of_cards.png", Point(1300, 200))
        self.mata = Button(Point(0,0), "graphics/mata.png", screen)
        self.three_rows_of_cards = ThreeRows(RowOfCards(1, screen, self.action_field, self.first_deck_of_cards),
                                             RowOfCards(2, screen, self.action_field, self.second_deck_of_cards),
                                             RowOfCards(3, screen, self.action_field, self.third_deck_of_cards),self.action_field)

        self.six_stacks_of_tokens = SixStackOfTokens(StackOfTokens("blue", 7, screen, self.action_field, Point(500,50)),
                                                     StackOfTokens("green", 7, screen, self.action_field,Point(600, 50)),
                                                     StackOfTokens("red", 7, screen, self.action_field, Point(400, 50)),
                                                     StackOfTokens("white", 7, screen, self.action_field,Point(800, 50)),
                                                     StackOfTokens("black", 7, screen, self.action_field, Point(700, 50)),
                                                     StackOfTokens("special", 5, screen, self.action_field, Point(900, 50)),
                                                     self.screen,self.action_field)

    def handle_events(self):
        import pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.action_field.click_events()
                self.six_stacks_of_tokens.click_events()
                self.three_rows_of_cards.click_events()
                self.player_one.click_events()
    def update(self):
        self.three_rows_of_cards.update()
        self.action_field.update()
        self.six_stacks_of_tokens.update()
        self.player_one.update()
    def display(self):
        self.mata.display()
        self.action_field.display()
        self.three_rows_of_cards.display()
        self.six_stacks_of_tokens.display()
        self.player_one.display()

