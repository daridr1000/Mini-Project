#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

from getch1 import *
from character import Character
from character.creature.monster import Monster
from character.creature.goblin import Goblin
from character.creature import Creature
import sys
import pickle


class Hero(Character):
    """this is the hero class, further define it please"""

    def __init__(self):
        super().__init__()
        # Initialising the main attributes
        self._health = 100
        self._coins = 1000
        self._moves = 0
        self._visited_monsters = 0

    # Sets the moves hero has made so far inside the maze
    def set_moves(self,moves):
        self._moves = moves

    # Increases the moves hero has mad inside the maze
    def increase_moves(self):
        self._moves += 1

    # Returns the number of moves
    def get_moves(self):
        return self._moves

    # Returns the number of health points
    def gethealth(self):
        return self._health

    # Returns the number of coins
    def getcoins(self):
        return self._coins

    # Prints the details of the hero
    def hero_details(self):
        print("Hero position: ", self.getcoordX(), self.getcoordY())
        print("Health", self.gethealth())
        print("Coins", self.getcoins())

    # Resets all the hero's abilities
    def reset_hero_abilities(self):
        self._moves = 0
        self._health = 100
        self._coins = 1000
        self._visited_monsters = 0

    # Loads all the hero abilities with the ones that have been saved by using pickle
    def load_hero_abilities(self, health, coins, visited_monsters, x, y):
        self._health = health
        self._coins = coins
        self._visited_monsters = visited_monsters
        self.set_coords(x, y)

    # Determines whether the hero won the game or not
    def win_game(self):
        if self._visited_monsters == 5:
            return True
        return False

    # Determines whether the hero lost the game or not
    def lose_game(self):
        if self.gethealth() <= 0:
            return True
        return False

    # Saves all the necessary elements of the game in order to allow the player replay it after exiting and
    # loading the game
    def save_game(self, environment):
        f = open("backup", "wb")
        pickle.dump(self._moves, f)
        pickle.dump(self.gethealth(), f)
        pickle.dump(self.getcoins(), f)
        pickle.dump(self._visited_monsters, f)
        pickle.dump(self.getcoordX(), f)
        pickle.dump(self.getcoordY(), f)
        pickle.dump(Monster.all_monsters, f)
        pickle.dump(Monster.all_coordinates, f)
        pickle.dump(Monster.hero_fight, f)
        pickle.dump(Goblin.all_goblins, f)
        pickle.dump(Goblin.all_coordinates, f)
        pickle.dump(environment, f)
        pickle.dump(Creature.get_difficulty(), f)
        pickle.dump(Monster.abilities, f)
        pickle.dump(Goblin.abilities, f)
        f.close()

    def move(self, environment):
        """move in the maze, it is noted this function may not work in the debug mode"""

        ch2 = getch()

        if ch2 == b'H' or ch2 == "A":
            # the up arrow key was pressed
            print("up key pressed")
            if environment[self._coordX - 1][self._coordY] == 0: # moves inside the maze only on the 0's
                environment[self._coordX - 1][self._coordY] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 3:
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX - 1, self._coordY])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX - 1, self._coordY])]
                self.meet(goblin)
                environment[self._coordX - 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
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
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX + 1, self._coordY])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX += 1
            elif environment[self._coordX + 1][self._coordY] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX + 1, self._coordY])]
                self.meet(goblin)
                environment[self._coordX + 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
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
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX, self._coordY - 1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY -= 1
            elif environment[self._coordX][self._coordY - 1] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX, self._coordY - 1])]
                self.meet(goblin)
                environment[self._coordX][self._coordY - 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
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
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX, self._coordY + 1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            elif environment[self._coordX][self._coordY + 1] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX, self._coordY + 1])]
                self.meet(goblin)
                environment[self._coordX][self._coordY + 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
                self._coordY += 1
            return True
        elif ch2 == b'S':
            # Saves the game as the player pressed S
            self.save_game(environment)
        elif ch2 == b'E':
            # Exits the game
            sys.exit()
        return False

    def move_debug(self, environment):
        """move in the maze, you need to press the enter key after keying in
        direction, and this works in the debug mode"""

        ch2 = sys.stdin.read(1)
        if ch2 == "w":
            # the up arrow key was pressed
            print("up key pressed")
            if environment[self._coordX - 1][self._coordY] == 0:  # moves inside the maze only on the 0's
                environment[self._coordX - 1][self._coordY] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 3:
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX - 1, self._coordY])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX -= 1
            elif environment[self._coordX - 1][self._coordY] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX - 1, self._coordY])]
                self.meet(goblin)
                environment[self._coordX - 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
                self._coordX -= 1

            return True

        elif ch2 == "s":
            print("down key pressed")
            if environment[self._coordX + 1][self._coordY] == 0:
                environment[self._coordX + 1][self._coordY] = 2
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._health -= 1
                self._coordX += 1
            elif environment[self._coordX + 1][self._coordY] == 3:
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX + 1, self._coordY])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordX += 1
            elif environment[self._coordX + 1][self._coordY] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX + 1, self._coordY])]
                self.meet(goblin)
                environment[self._coordX + 1][self._coordY] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
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
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX, self._coordY - 1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY -= 1
            elif environment[self._coordX][self._coordY - 1] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX, self._coordY - 1])]
                self.meet(goblin)
                environment[self._coordX][self._coordY - 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
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
                # Takes the monster from that position and makes the hero fight with it
                monster = Monster.all_monsters[Monster.all_coordinates.index([self._coordX, self._coordY + 1])]
                self.fight(monster)
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0
                self._coordY += 1
            elif environment[self._coordX][self._coordY + 1] == 4:
                # Takes the goblin from that position and makes the hero meet it
                goblin = Goblin.all_goblins[Goblin.all_coordinates.index([self._coordX, self._coordY + 1])]
                self.meet(goblin)
                environment[self._coordX][self._coordY + 1] = 2
                self._health -= 1
                if environment[self._coordX][self._coordY] != 3:
                    environment[self._coordX][self._coordY] = 0  # makes the goblin disappear
                self._coordY += 1
            return True
        elif ch2 == "S":
            # Saves the game as the player pressed S
            self.save_game(environment)
        elif ch2 == "E":
            # Exits the game
            sys.exit()
        return False

    @staticmethod
    def rock_paper_scissors():
        # User chooses rock, paper or scissors
        ch = input("Choose rock(R), paper(P) or scissor(S) : ")
        while ch != 'R' and ch != 'P' and ch != 'S':
            print("Wrong input!")
            ch = input("Choose rock(R), paper(P) or scissor(S) : ")
        # The input of the creature is taken
        creature_choice = Creature.gamer()
        choices = ["P", "R", "S"]
        print("Creature picked:", choices[creature_choice])
        while choices.index(ch) == creature_choice: # Repeats the game if the creature and the hero choose the same
            ch = input("Draw! Choose again! ")
            while ch != 'R' and ch != 'P' and ch != 'S':
                print("Wrong input!")
                ch = input("Choose rock(R), paper(P) or scissor(S) : ")
            creature_choice = Creature.gamer()
            print("Creature picked:", choices[creature_choice])
        if choices.index(ch) - creature_choice == -1 or choices.index(ch) - creature_choice == 2:
            return True # returns true if the hero won
        elif choices.index(ch) - creature_choice == 1 or choices.index(ch) - creature_choice == -2:
            return False # returns false if the hero loses

    def fight(self, monster):
        """fight with monsters"""
        if Monster.hero_fight[Monster.all_monsters.index(monster)] == 0: # if the monster has not been visited before,
            # increase the number of monsters visited by the hero
            self._visited_monsters += 1
            # marks the monster as visited
            Monster.hero_fight[Monster.all_monsters.index(monster)] = 1
        if monster.get_ability() == 1: # if the monster is a thief monster
            coins_stolen = monster.thief_monster()
            # Prints appropiate messages if the hero lost or won the challenge
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
        elif monster.get_ability() == 2: # if the monster is a fighter monster
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
                print("The hero fought with the fighter monster at coordinate ({},{}) and "
                      "lost the fight, {} health points were lost".format(
                    monster.getcoordX(), monster.getcoordY(), health_taken))
            self._health -= health_taken
        else: # if the monster is a gamer monster
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
