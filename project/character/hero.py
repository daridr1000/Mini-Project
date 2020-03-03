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
        self._gem = 0
        self._visited_monsters = 0

    def increase_gem(self):
        self._gem += 1

    def gethealth(self):
        return self._health

    def getcoins(self):
        return self._coins

    def hero_details(self):
        print("Hero position: ", self.getcoordX(), self.getcoordY())
        print("Health", self.gethealth())
        print("Coins", self.getcoins())

    def reset_hero_abilities(self):
        self._gem = 0
        self._health = 100
        self._coins = 1000
        self._visited_monsters = 0

    def load_hero_abilities(self, health, coins, visited_monsters,x,y):
        self._health = health
        self._coins = coins
        self._visited_monsters = visited_monsters
        self.set_coords(x,y)

    def win_game(self):
        if self._visited_monsters == 5:
            return True
        return False

    def lose_game(self):
        if self.gethealth() <= 0:
            return True
        return False

    def load_game(self, environment):
        f = open("load_game.txt", "w")
        load = str(self._gem) + '\n' + str(self.gethealth()) + '\n' + str(self.getcoins()) + \
               '\n'+ str(self._visited_monsters) +  \
               '\n' + str(Monster.all_coordinates) + '\n' + str(Monster.hero_fight) + \
               '\n' + str(Goblin.all_coordinates) + '\n' + str(environment) + \
               '\n' + str(Creature.get_difficulty()) + \
                '\n' + str(self.getcoordX()) + '\n' + str(self.getcoordY()) + \
                '\n' +str(Monster.abilities) + '\n' + str(Goblin.abilities)

        f.write(load)
        f.close()

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
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX - 1, self._coordY])]
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
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX + 1, self._coordY])]
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
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX, self._coordY - 1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY -= 1
            elif environment[self._coordX][self._coordY - 1] == 4:
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX, self._coordY - 1])]
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
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX, self._coordY + 1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            elif environment[self._coordX][self._coordY + 1] == 4:
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX, self._coordY + 1])]
                self.meet(goblin)
                environment[self._coordX][self._coordY + 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            return True
        elif ch2 == b'S':
            self.load_game(environment)
        elif ch2 == b'E':
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
        while ch!='R' and ch!='P' and ch != 'S':
            print("Wrong input!")
            ch = input("Choose rock(R), paper(P) or scissor(S) : ")
        creature_choice = Creature.gamer()
        choices = ["P", "R", "S", ""]
        print("Creature picked:", choices[creature_choice])
        while choices.index(ch) == creature_choice:
            ch = input("Draw! Choose again! ")
            creature_choice = Creature.gamer()
            print("Creature picked:", choices[creature_choice])
        if choices.index(ch) - creature_choice == -1 or choices.index(ch) - creature_choice == 2:
            return True
        elif choices.index(ch) - creature_choice == 1 or choices.index(ch) - creature_choice == -2:
            return False

    def fight(self, monster):
        """fight with monsters"""
        if Monster.hero_fight[Monster.all_monsters.index(monster)] == 0:
            self._visited_monsters += 1
            Monster.hero_fight[Monster.all_monsters.index(monster)] = 1

        if monster.get_ability() == 1:
            coins_stolen = monster.thief_monster()
            print("The hero meets a thief monster with the ability of ({}, {}%) at coordinate ({},{}). "
                  "There is a {}% probability that the monster will steal {} coins from the hero.".format(
                50 + 50 * Creature.get_difficulty(), 30 + 10 * Creature.get_difficulty(),
                monster.getcoordX(), monster.getcoordY(),
                30 + 10 * Creature.get_difficulty(), 50 + 50 * Creature.get_difficulty()))
            print("Press ENTER to see the outcome")
            ch = getch()
            while ord(ch) != 13:
                ch = getch()

            if coins_stolen == 0:
                print("The hero fought with the thief monster at coordinate ({},{}) and "
                      "won the fight, no coins were lost".format(
                    monster.getcoordX(), monster.getcoordY()))
            else:
                print("The hero fought with the thief monster at coordinate ({},{}) and "
                      "lost the fight, {} coins were lost".format(
                    monster.getcoordX(), monster.getcoordY(), coins_stolen))
            self._coins -= coins_stolen
        elif monster.get_ability() == 2:
            health_taken = monster.fighter_monster()
            print("The hero meets a fighter monster with the ability of ({}, {}%) at coordinate ({},{}). "
                  "There is a {}% probability that the monster will steal "
                  "{} health points from the hero.".format(
                10 + 10 * Creature.get_difficulty(), 30 + 10 * Creature.get_difficulty(),
                monster.getcoordX(), monster.getcoordY(),
                30 + 10 * Creature.get_difficulty(), 10 + 10 * Creature.get_difficulty()))
            print("Press ENTER to see the outcome")
            ch = getch()
            while ord(ch) != 13:
                ch = getch()

            if health_taken == 0:
                print("The hero fought with the fighter monster at coordinate ({},{}) and "
                      "won the fight, no health points were lost".format(
                    monster.getcoordX(), monster.getcoordY()))
            else:
                print("The hero fought with the thief monster at coordinate ({},{}) and "
                      "lost the fight, {} health points were lost".format(
                    monster.getcoordX(), monster.getcoordY(), health_taken))
            self._health -= health_taken
        else:
            print("The hero meets a gamer monster with the ability of ({},{}) at coordinate ({},{}). "
                  "A game will be played and if the monster "
                  "wins the game, it will steal"
                  " {} coins and {} health points from the hero.".format(
                50 + 100 * Creature.get_difficulty(), 10 + 10 * Creature.get_difficulty(),
                monster.getcoordX(), monster.getcoordY(),
                50 + 100 * Creature.get_difficulty(), 10 + 10 * Creature.get_difficulty()))

            print("Press ENTER to see the outcome")
            ch = getch()
            while ord(ch) != 13:
                ch = getch()
            game = Hero.rock_paper_scissors()
            if not game:
                print("Monster wins the game, {} coins and {} health points were lost".format(
                    50 + 100 * Creature.get_difficulty(), 10 + 10 * Creature.get_difficulty()))
                self._coins -= (50 + 100 * Creature.get_difficulty())
                self._health -= (10 + 10 * Creature.get_difficulty())
            else:
                print("Hero wins the game, no coins or health points were lost")

    def meet(self, goblin):
        """meet with goblins"""
        if goblin.get_ability() == 1:
            print("The hero meets a wealth goblin with the ability of ({}, {}%) at coordinate ({},{}). "
                  "There is a {}% probability that the hero will get {} coins from the goblin.".format(
                400 - 100 * Creature.get_difficulty(), 70 - 10 * Creature.get_difficulty(),
                goblin.getcoordX(), goblin.getcoordY(),
                70 - 10 * Creature.get_difficulty(), 400 - 100 * Creature.get_difficulty()))
            print("Press ENTER to see the outcome")
            ch = getch()
            while ord(ch) != 13:
                ch = getch()
            coins_given = goblin.wealth_goblin()
            if coins_given != 0:
                print("The hero met a wealth goblin at coordinate ({},{}) and "
                      "won the challenge. The hero gets {} coins".format(
                    goblin.getcoordX(), goblin.getcoordY(), coins_given))
            else:
                print("The hero met a wealth goblin at coordinate ({},{}) and "
                      "failed the challenge.The hero does not get any coins".format(
                    goblin.getcoordX(), goblin.getcoordY()))
            self._coins += coins_given
        elif goblin.get_ability() == 2:
            print("The hero meets a health goblin with the ability of ({}, {}%) at coordinate ({},{}). "
                  "There is a {}% probability that the hero will get {} health points from the goblin.".format(
                70 - 10 * Creature.get_difficulty(), 70 - 10 * Creature.get_difficulty(),
                goblin.getcoordX(), goblin.getcoordY(),
                70 - 10 * Creature.get_difficulty(), 70 - 10 * Creature.get_difficulty()))
            print("Press ENTER to see the outcome")
            ch = getch()
            while ord(ch) != 13:
                ch = getch()
            health_given = goblin.health_goblin()
            if health_given != 0:
                print("The hero met a wealth goblin at coordinate ({},{}) and "
                      "won the challenge. The hero gets {} health points".format(
                    goblin.getcoordX(), goblin.getcoordY(), health_given))
            else:
                print("The hero met a health goblin at coordinate ({},{}) and "
                      "failed the challenge.The hero does not get any health points".format(
                    goblin.getcoordX(), goblin.getcoordY()))
            self._health += health_given
        else:
            print("The hero meets a gamer goblin with the ability of ({},{}) at coordinate ({},{}). "
                  "A game will be played and if the hero "
                  "wins the game, he will get "
                  " {} coins and {} health points from the hero.".format(
                50 + 100 * Creature.get_difficulty(), 10 + 10 * Creature.get_difficulty(),
                goblin.getcoordX(), goblin.getcoordY(),
                50 + 100 * Creature.get_difficulty(), 10 + 10 * Creature.get_difficulty()))
            print("Press ENTER to see the outcome")
            ch = getch()
            while ord(ch) != 13:
                ch = getch()
            game = Hero.rock_paper_scissors()
            if game:
                print("Hero wins the game! He got {} coins and {} health points".format(
                    50 + 100 * Creature.get_difficulty(), 10 + 10 * Creature.get_difficulty()))
                self._coins += 50 + 100 * Creature.get_difficulty()
                self._health += 10 + 10 * Creature.get_difficulty()
            else:
                print("Goblin wins the game! The hero does not get any coins or health points")
