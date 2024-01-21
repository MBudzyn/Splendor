from token import Token
class StackOfTokens:
    def __init__(self, color, amount, is_universal=False):
        self.color = color
        self.amount = amount
        self.is_universal = is_universal
        self.tokens = [Token(color, is_universal) for _ in range(amount)]
        self.max_amount = 7

    def is_empty(self):
        return self.amount == 0

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
