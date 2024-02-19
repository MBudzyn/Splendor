from player_cards import PlayerCards
from player_tokens import PlayerTokens
from player_reserved_cards import PlayerReservedCards


class Player:
    def __init__(self, nick_name, screen, action_field):
        self.nick_name = nick_name
        self.screen = screen
        self.player_cards = PlayerCards(action_field)
        self.player_tokens = PlayerTokens(screen, action_field)
        self.player_reserved_cards = PlayerReservedCards(action_field)
        self.is_turn = False
        import pygame
        self.font = pygame.font.SysFont("Comic Sans MS", 70)
        self.text = self.font.render(nick_name, False, [255, 255, 255])

    def display(self):
        self.player_cards.display()
        self.player_tokens.display()
        self.player_reserved_cards.display()
        self.screen.blit(self.text, (900,550))

    def set_turn(self, is_turn):
        self.is_turn = is_turn

    def get_turn(self):
        return self.is_turn

    def update(self):
        self.player_cards.update()
        self.player_tokens.update()
        self.player_reserved_cards.update()

    def click_events(self):
        self.player_tokens.click_events()
        self.player_cards.click_events()
        self.player_reserved_cards.click_events()
