from token import Token
import pygame
class StackOfTokens:
    def __init__(self, color, amount, screen, is_universal=False):
        self.color = color
        self.amount = amount
        self.is_universal = is_universal
        self.tokens = [Token(color, is_universal) for _ in range(amount)]
        self.graphics_links = [f"graphics/{color}_token{i}.png" for i in range(8)]
        self.max_amount = 7
        self.set_image_to_actual()
        self.screen = screen

    def is_empty(self):
        return self.amount == 0

    def set_image_to_actual(self):
        self.actual_stack_image = pygame.image.load(self.graphics_links[self.amount])
        self.actual_stack_image_rect = self.actual_stack_image.get_rect(center=(400, 400))

    def display(self, screen):
        screen.blit(self.actual_stack_image, self.actual_stack_image_rect)

    def is_possible_to_take_token(self):
        return not self.is_empty()

    def is_possible_to_take_two_tokens(self):
        return self.amount >= 4

    def is_possible_to_add_token(self):
        return self.amount < self.max_amount

    def delete_token(self):
        if self.is_possible_to_take_token():
            self.tokens.pop()
            self.amount -= 1

    def get_token(self):
        if self.is_possible_to_take_token():
            token = self.tokens[-1]
            self.delete_token()
            return token

    def add_token(self):
        if self.is_possible_to_add_token():
            self.tokens.append(Token(self.color, self.is_universal))
            self.amount += 1
