#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

import random
from character.creature import Creature


class Monster(Creature):
    """define your monster class here"""
    all_monsters = []
    all_coordinates = []
    hero_fight = []
    abilities = [1, 2, 3, random.randrange(1,4),random.randrange(1,4)]
    random.shuffle(abilities)

    def __init__(self):
        super().__init__()
        Monster.all_monsters.append(self)
        Monster.all_coordinates.append([self.getcoordX() , self.getcoordY()])
        Monster.hero_fight.append(0)
        self._ability = None

    def set_ability(self):
        self._ability = Monster.abilities[Monster.all_monsters.index(self)]

    def get_ability(self):
        return self._ability

    @staticmethod
    def reset_monsters():
        Monster.all_monsters = []
        Monster.all_coordinates = []
        Monster.hero_fight = []

    @staticmethod
    def thief_monster():
        coins = 0
        r = random.random()
        if r <= 0.9:
            coins = 10
        return coins

    @staticmethod
    def fighter_monster():
        health = 0
        r = random.random()
        if r <= 0.4:
            health = 30
        return health


