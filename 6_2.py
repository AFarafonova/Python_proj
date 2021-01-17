class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

class MassCount(Road):
    def __init__(self, _length, _width, volume, santemeter):
        super().__init__(_length, _width)
        self.volume = volume
        self.santemeter = santemeter

    def mass(self):
        return self._length * self._width * self.volume * self.santemeter

r = MassCount(20, 5000, 25, 5)
print(r.mass())