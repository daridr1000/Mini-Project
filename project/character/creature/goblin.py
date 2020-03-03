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
        Goblin.all_coordinates.append([self.getcoordX(), self.getcoordY()])
        self._ability = None

    def set_ability(self):
        self._ability = Goblin.abilities[Goblin.all_goblins.index(self)]

    def get_ability(self):
        return self._ability

    @classmethod
    def reset_goblins(cls):
        cls.all_goblins = []
        cls.all_coordinates = []

    @classmethod
    def load_goblins(cls, coordinates, abilities):
        for i in range(0, 5):
            goblin = Goblin()
        cls.all_coordinates = coordinates
        cls.abilities = abilities
        for i in range(0, 5):
            for j in range(0, 5):
                cls.all_goblins[i].set_coords(coordinates[i][0], coordinates[i][1])
        for i in range(0, 5):
            cls.all_goblins[i].set_ability()

    def wealth_goblin(self):
        coins = 0
        r = random.random()
        if r <= 0.7 - self.get_difficulty() / 10:
            coins = 400 - 100 * self.get_difficulty()
        return coins

    def health_goblin(self):
        health = 0
        r = random.random()
        if r <= 0.7 - self.get_difficulty() / 10:
            health = 70 - 10 * self.get_difficulty()
        return health

    @staticmethod
    def goblins_details():
        print("GOBLINS:")
        goblins = Goblin.all_goblins
        for i in range(0, 5):
            if goblins[i].get_ability() == 1:
                type = "Wealth Goblin"
            elif goblins[i].get_ability() == 2:
                type = "Health Goblin"
            else:
                type = "Gamer Goblin"
            print(type, goblins[i].getcoordX(), goblins[i].getcoordY())



