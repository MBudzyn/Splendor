
from scene import *
import sys
from action_field import ActionField
from point import Point
from deck_of_cards import DeckOfCards
from row_of_cards_in_ply import RowOfCards
from button import Button
from three_rows import ThreeRows
from player import Player
from game_tokens import GameTokens


class MenuScene(Scene):
    def __init__(self, screen, scene_man):
        super().__init__(screen)
        self.screen = screen
        self.scene_man = scene_man
        self.action_field = ActionField(screen)
        self.player_one = Player("Player One", screen, self.action_field)
        self.player_two = Player("Player Two", screen, self.action_field)
        self.player_three = Player("Player Three", screen, self.action_field)
        self.player_four = Player("Player Four", screen, self.action_field)
        self.playing_player = self.player_one
        self.first_deck_of_cards = DeckOfCards(screen, 1, "graphics/deck_of_cards.png", Point((1300, 200)))
        self.second_deck_of_cards = DeckOfCards(screen, 2, "graphics/deck_of_cards.png", Point((1300, 200)))
        self.third_deck_of_cards = DeckOfCards(screen, 3, "graphics/deck_of_cards.png", Point((1300, 200)))
        self.mata = Button(Point((0,0)), "graphics/mata.png", screen)
        self.game_field = Button(Point((350,425)), "graphics/game_field.png", screen)
        self.player_field = Button(Point((1150, 625)), "graphics/player_field.png", screen)
        self.action_field_d = Button(Point((1150, 250)), "graphics/action_field.png", screen)
        self.buy_card_field = Button(Point((950, 250)), "graphics/buy_card_field.png", screen)
        self.three_rows_of_cards = ThreeRows(RowOfCards(1, screen, self.action_field, self.first_deck_of_cards),
                                             RowOfCards(2, screen, self.action_field, self.second_deck_of_cards),
                                             RowOfCards(3, screen, self.action_field, self.third_deck_of_cards),self.action_field)
        self.six_stacks_of_tokens = GameTokens(screen, self.action_field)

    def set_playing_player(self):
        if self.action_field.get_actual_turn() % 4 == 1:
            self.playing_player = self.player_one
        if self.action_field.get_actual_turn() % 4 == 2:
            self.playing_player = self.player_two
        if self.action_field.get_actual_turn() % 4 == 3:
            self.playing_player = self.player_three
        if self.action_field.get_actual_turn() % 4 == 0:
            self.playing_player = self.player_four

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
                self.playing_player.click_events()
    def update(self):
        self.set_playing_player()
        self.three_rows_of_cards.update()
        self.action_field.update()
        self.six_stacks_of_tokens.update()
        self.playing_player.update()
    def display(self):
        self.mata.display()
        self.game_field.display()
        self.player_field.display()
        self.action_field_d.display()
        self.buy_card_field.display()
        self.action_field.display()
        self.three_rows_of_cards.display()
        self.six_stacks_of_tokens.display()
        self.playing_player.display()

