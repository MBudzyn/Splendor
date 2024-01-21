class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)
