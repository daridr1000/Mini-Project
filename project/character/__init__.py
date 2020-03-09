import random


class Character:
    def __init__(self):
        # Randomly generates the coordinates of all characters of the game
        self._coordX = random.randint(1, 16)
        self._coordY = random.randint(1, 16)

    # returns the coordinates
    def getcoordX(self):
        return self._coordX

    def getcoordY(self):
        return self._coordY

    # Sets the coordinates ( method used when loading a game)
    def set_coords(self, x, y):
        self._coordX = x
        self._coordY = y
