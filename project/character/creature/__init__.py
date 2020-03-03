import random

from character import Character


class Creature(Character):
    _difficulty = None

    def __init__(self):
        super().__init__()

    @staticmethod
    def gamer():
        i = random.randint(0, 2)
        return i

    @classmethod
    def set_difficulty(cls, difficulty):
        cls._difficulty = difficulty

    @classmethod
    def get_difficulty(cls):
        return cls._difficulty
