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
    abilities = [1, 2, 3, random.randrange(1, 4), random.randrange(1, 4)]
    random.shuffle(abilities)

    def __init__(self):
        super().__init__()
        Monster.all_monsters.append(self)
        Monster.all_coordinates.append([self.getcoordX(), self.getcoordY()])
        Monster.hero_fight.append(0)
        self._ability = None

    def set_ability(self):
        self._ability = Monster.abilities[Monster.all_monsters.index(self)]

    def get_ability(self):
        return self._ability

    @classmethod
    def reset_monsters(cls):
        cls.all_monsters = []
        cls.all_coordinates = []
        cls.hero_fight = []

    @classmethod
    def load_monsters(cls, coordinates, hero_fight, abilities):
        cls.all_coordinates = coordinates
        cls.hero_fight = hero_fight
        for i in range(0,5):
            for j in range(0,5):
                cls.all_monsters[i].set_coords(coordinates[i][0],coordinates[i][1])
        cls.abilities = abilities
        for i in range(0,5):
            cls.all_monsters[i].set_ability()

    def thief_monster(self):
        coins = 0
        r = random.random()
        if r <= 0.3 + self.get_difficulty() / 10:
            coins = 50 + 50 * self.get_difficulty()
        return coins

    def fighter_monster(self):
        health = 0
        r = random.random()
        if r <= 0.3 + self.get_difficulty() / 10:
            health = 10 + 10 * self.get_difficulty()
        return health

    @staticmethod
    def monsters_details():
        print("MONSTERS:")
        monsters = Monster.all_monsters
        for i in range(0, 5):
            if monsters[i].get_ability() == 1:
                type = "Thief Monster"
            elif monsters[i].get_ability() == 2:
                type = "Fighter Monster"
            else:
                type = "Gamer Monster"
            print(type, monsters[i].getcoordX(), monsters[i].getcoordY())
