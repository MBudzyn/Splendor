
from player_cards import PlayerCards
from player_tokens import PlayerTokens
class Player:
    def __init__(self, nick_name, screen):
        self.nick_name = nick_name
        self.screen = screen
        self.player_cards = PlayerCards()
        self.player_tokens = PlayerTokens(screen)

    def display(self):
        self.player_cards.display()
        self.player_tokens.display()

    def update(self):
        self.player_cards.update()
        self.player_tokens.update()

    def click_events(self):
        self.player_tokens.click_events()
