import random


class Character:
    def __init__(self):
        self._coordX = random.randint(1, 16)
        self._coordY = random.randint(1, 16)

    def getcoordX(self):
        return self._coordX

    def getcoordY(self):
        return self._coordY

    def set_coords(self, x, y):
        self._coordX = x
        self._coordY = y
