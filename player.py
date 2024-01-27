
from player_cards import PlayerCards
class Player:
    def __init__(self, nick_name, screen):
        self.nick_name = nick_name
        self.screen = screen
        self.player_cards = PlayerCards()
