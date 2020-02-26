#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

from getch1 import *
from character import Character
from character.creature.monster import Monster
from character.creature.goblin import Goblin
from character.creature import Creature
import sys


class Hero(Character):
    """this is the hero class, further define it please"""

    def __init__(self):
        """set the coordinate of the hero in the maze"""
        super().__init__()
        self._health = 100
        self._coins = 1000  # gold coins the hero have.
        self._gem = 3
        self._visited_monsters = 0

    def gethealth(self):
        return self._health

    def getcoins(self):
        return self._coins

    def reset_hero_abilities(self):
        self._health = 100
        self._coins = 1000
        self._visited_monsters = 0

    def win_game(self):
        if self._visited_monsters == 5:
            return True
        return False

    def lose_game(self):
        if self.gethealth() <= 0:
            return True
        return False

    def move(self, environment):
        """move in the maze, it is noted this function may not work in the debug mode"""

        ch2 = getch()

        if ch2 == b'H' or ch2 == "A":
            # the up arrow key was pressed
            print("up key pressed")

            if environment[self._coordX - 1][self._coordY] == 0:
                environment[self._coordX - 1][self._coordY] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 3:
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX - 1,self._coordY])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 4:
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX - 1, self._coordY])]
                self.meet(goblin)
                environment[self._coordX - 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX -= 1

            return True


        elif ch2 == b'P' or ch2 == "B":
            print("down key pressed")
            if environment[self._coordX + 1][self._coordY] == 0:
                environment[self._coordX + 1][self._coordY] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordX += 1
            elif environment[self._coordX + 1][self._coordY] == 3:
                monster =Monster.all_monsters[Monster.all_coordinates.index([self._coordX + 1,self._coordY])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX += 1
            elif environment[self._coordX + 1][self._coordY] == 4:
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX + 1, self._coordY])]
                self.meet(goblin)
                environment[self._coordX + 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX += 1
            return True


        elif ch2 == b'K' or ch2 == "D":
            # the left arrow key was pressed
            print("left key pressed")
            if environment[self._coordX][self._coordY - 1] == 0:
                environment[self._coordX][self._coordY - 1] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordY -= 1
            elif environment[self._coordX][self._coordY - 1] == 3:
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX ,self._coordY-1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY -= 1
            elif environment[self._coordX][self._coordY - 1] == 4:
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX , self._coordY-1])]
                self.meet(goblin)
                environment[self._coordX][self._coordY - 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY -= 1
            return True

        elif ch2 == b'M' or ch2 == "C":
            # the right arrow key was pressed
            print("right key pressed")
            if environment[self._coordX][self._coordY + 1] == 0:
                environment[self._coordX][self._coordY + 1] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordY += 1
            elif environment[self._coordX][self._coordY + 1] == 3:
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX ,self._coordY+1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            elif environment[self._coordX][self._coordY + 1] == 4:
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX , self._coordY+1])]
                self.meet(goblin)
                environment[self._coordX][self._coordY + 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            return True
        elif ord(ch2) == 77:
            print(environment)
        elif ord(ch2) == 69:
            sys.exit()
        return False

    def move_debug(self, environment):
        """move in the maze, you need to press the enter key after keying in
        direction, and this works in the debug mode"""

        ch2 = sys.stdin.read(1)
        if ch2 == "w":
            # the up arrow key was pressed
            print("up key pressed")
            if environment[self._coordX - 1][self._coordY] == 0:
                environment[self._coordX - 1][self._coordY] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 3:
                self.fight()
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 4:
                self.meet()
                environment[self._coordX - 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX -= 1

            return True

        elif ch2 == "s":
            # the down arrow key was pressed
            print("down key pressed")
            if environment[self._coordX + 1][self._coordY] == 0:
                environment[self._coordX + 1][self._coordY] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordX += 1
            elif environment[self._coordX + 1][self._coordY] == 3:
                self.fight()
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX += 1
            elif environment[self._coordX + 1][self._coordY] == 4:
                self.meet()
                environment[self._coordX + 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX += 1
            return True

        elif ch2 == "a":
            # the left arrow key was pressed
            print("left key pressed")

            if environment[self._coordX][self._coordY - 1] == 0:
                environment[self._coordX][self._coordY - 1] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordY -= 1
            elif environment[self._coordX][self._coordY - 1] == 3:
                self.fight()
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY -= 1
            elif environment[self._coordX][self._coordY - 1] == 4:
                self.meet()
                environment[self._coordX][self._coordY - 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY -= 1
            return True

        elif ch2 == "d":
            # the right arrow key was pressed
            print("right key pressed")

            if environment[self._coordX][self._coordY + 1] == 0:
                environment[self._coordX][self._coordY + 1] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordY += 1
            elif environment[self._coordX][self._coordY + 1] == 3:
                self.fight()
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            elif environment[self._coordX][self._coordY + 1] == 4:
                self.meet()
                environment[self._coordX][self._coordY + 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            return True

        return False

    @staticmethod
    def rock_paper_scissors():
        ch = input("Choose rock(R), paper(P) or scissor(S) : ")
        creature_choice = Creature.gamer()
        choices = ["P", "R", "S", ""]
        while choices.index(ch) == creature_choice:
            ch = input("Draw! Choose again! ")
            creature_choice = Creature.gamer()
            print("Creature picked : ", creature_choice)
            """ADD MESSAGES AND DIFFICULTIES"""
        if choices.index(ch) - creature_choice == -1 or choices.index(ch) - creature_choice == 2:
            return True
        elif choices.index(ch) - creature_choice == 1 or choices.index(ch) - creature_choice == -2:
            return False

    def fight(self,monster):
        """fight with monsters"""
        if Monster.hero_fight[Monster.all_monsters.index(monster)] == 0:
            self._visited_monsters += 1
            Monster.hero_fight[Monster.all_monsters.index(monster)] = 1
        if monster.get_ability() == 1:
            coins_stolen = Monster.thief_monster()
            self._coins -= coins_stolen
        elif monster.get_ability() == 2:
            health_taken = Monster.fighter_monster()
            self._health -= health_taken
        else:
            game = Hero.rock_paper_scissors()
            if not game:
                print("Monster wins!")
                self._coins -= 100
                self._health -= 50
            else:
                print("Hero wins!")

    def meet(self,goblin):
        """meet with goblins"""
        if goblin.get_ability() == 1:
            coins_given = Goblin.wealth_goblin()
            self._coins += coins_given
        elif goblin.get_ability() == 2:
            health_given = Goblin.health_goblin()
            self._health += health_given
        else:
            game = Hero.rock_paper_scissors()
            if game:
                self._coins += 100
                self._health += 50
                print("Hero wins!")
            else:
                print("Goblin wins!")