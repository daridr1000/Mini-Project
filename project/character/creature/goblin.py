#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0


import random
from character.creature import Creature


class Goblin(Creature):
    """define your goblin class here"""
    all_goblins = []
    all_coordinates = []
    abilities = [1, 2, 3, random.randrange(1, 4), random.randrange(1, 4)]
    random.shuffle(abilities)

    def __init__(self):
        super().__init__()
        Goblin.all_goblins.append(self)
        Goblin.all_coordinates.append([self.getcoordX() , self.getcoordY()])
        self._ability = None

    def set_ability(self):
        self._ability = Goblin.abilities[Goblin.all_goblins.index(self)]

    def get_ability(self):
        return self._ability

    @staticmethod
    def wealth_goblin():
        coins = 0
        r = random.random()
        if r <= 0.5:
            coins = 100
        return coins

    @staticmethod
    def health_goblin():
        health = 0
        r = random.random()
        if r <= 0.7:
            health = 50
        return health
