from button import Button
from point import Point


class Token:
    def __init__(self, color, screen, is_universal=False, coordinates=None):
        self.color = color
        self.is_universal = is_universal
        self.coordinates = coordinates
        if self.coordinates is None:
            self.coordinates = Point(600,600)
        self.button = Button(self.coordinates, f"graphics/{color}_token.png", screen)

    def display(self):
        self.button.display()
