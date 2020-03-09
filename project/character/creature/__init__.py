import random

from character import Character


class Creature(Character):
    _difficulty = None # initialises the difficulty of the game

    def __init__(self):
        super().__init__()

    @staticmethod # determines the choice of the creature for the rock-paper-scissors game
    def gamer():
        i = random.randint(0, 2)
        return i

    @classmethod # sets the difficulty of the game
    def set_difficulty(cls, difficulty):
        cls._difficulty = difficulty

    @classmethod # returns the difficulty of the game
    def get_difficulty(cls):
        return cls._difficulty
