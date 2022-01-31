class Road:
    _length = float
    _width = float

    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width
        self.mass = round(((_length * _width * 25 * 0.05) / 1000), 4)

    def mass_road(self):
        return f'Необходимо {self.mass} т асфальта'


road = Road(20.1, 5000.589)
print(road.mass_road())
