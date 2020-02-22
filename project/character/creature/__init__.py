import random

from character import Character


class Creature(Character):
    def __init__(self):
        super().__init__()

    @staticmethod
    def gamer():
        i = random.randint(0, 2)
        return i


