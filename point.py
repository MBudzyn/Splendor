class Point:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.coordinates = coordinates



    def get_coordinates(self) -> tuple[int, int]:
        return self.coordinates

    def set_coordinates(self, x: int, y: int):
        self.x = x
        self.y = y
        self.coordinates = (x, y)

    def increase_coordinates(self, x: int, y: int):
        self.x += x
        self.y += y
        self.coordinates = (self.x, self.y)