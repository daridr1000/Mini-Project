from character.hero import Hero
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
from character.creature.monster import Monster
from character.creature.goblin import Goblin
from character.creature import Creature
from getch1 import *
import sys, pickle, ctypes

#  enable ANSI escape sequence processing for the console window
#  https://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console?fbclid=IwAR2lfZ4Ygmhv7ymGaeNPyf6womENvcWFeDnkb8j6xs6cMqZmMayrUglKr4c
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Initialises the green and red colors in ANSI and the variable COLOR_END which sets back the default color
COLOR_END = "\033[0m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
# Initialises each element of the maze
WALL_CHAR = "#"
SPACE_CHAR = "-"
HERO_CHAR = "H"
MONSTER_CHAR = "M"
GOBLIN_CHAR = "G"


class _Environment:
    """Environment includes Maze+Monster+Goblin"""

    def __init__(self, maze):
        self._environment = deepcopy(maze)

    # Initialises a value on a certain position from the maze
    def set_coord(self, x, y, val):
        self._environment[x][y] = val

    # Returns an element from the maze with coordinates (x,y)
    def get_coord(self, x, y):
        return self._environment[x][y]

    # Returns the environment (the maze itself)
    def get_environment(self):
        return self._environment

    # Generates a monster and returns its coordinates
    def _get_monster(self):
        monster = Monster()
        while self.get_coord(monster.getcoordX(), monster.getcoordY()) != 0:
            # If the monster was not generated on a free position in the maze ( on the symbol '0'),
            # deletes the monster and
            # generates a new one
            Monster.hero_fight.remove(Monster.hero_fight[Monster.all_monsters.index(monster)])
            Monster.all_monsters.remove(monster)
            Monster.all_coordinates.remove([monster.getcoordX(), monster.getcoordY()])
            monster = Monster()
        # Sets the ability of the monster
        monster.set_ability()
        return [monster.getcoordX(), monster.getcoordY()]

    # Generates a goblin and returns its coordinates
    def _get_goblin(self):
        goblin = Goblin()
        while self.get_coord(goblin.getcoordX(), goblin.getcoordY()) != 0:
            # If the goblin was not generated on a free position in the maze ( on the symbol '0'),
            # deletes the goblin and
            # generates a new one
            Goblin.all_goblins.remove(goblin)
            Goblin.all_coordinates.remove([goblin.getcoordX(), goblin.getcoordY()])
            goblin = Goblin()
        # Sets the ability of the goblin
        goblin.set_ability()
        return [goblin.getcoordX(), goblin.getcoordY()]

    # Generates all the creatures and adds them in the maze ( monsters with symbol '3' and goblins with symbol '4')
    def set_creatures(self):
        for i in range(0, 5):
            monster = self._get_monster()
            XM = monster[0]
            YM = monster[1]
            self.set_coord(XM, YM, 3)
            goblin = self._get_goblin()
            XG = goblin[0]
            YG = goblin[1]
            self.set_coord(XG, YG, 4)

    def print_environment(self):
        """print out the environment in the terminal"""
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("1", WALL_CHAR)  # replace the wall character
            row_str = row_str.replace("0", SPACE_CHAR)  # replace the space character
            row_str = row_str.replace("2", HERO_CHAR)  # replace the hero character
            row_str = row_str.replace("3", RED + MONSTER_CHAR + COLOR_END)  # replace the monster character
            row_str = row_str.replace("4", GREEN + GOBLIN_CHAR + COLOR_END)  # replace the goblin character
            print("".join(row_str))


class Game:
    # Initialises a class variable, an array which contains each user of the game
    _users = []
    # Initialises a class variable, an array which contains the number of coins of each user
    _coins = []
    # Initialises a class variable, a 2-dimensional array which contains the four league tables
    # and each difficulty of the game
    _files = [["leaguetable_easy.txt", "EASY"], ["leaguetable_medium.txt", "MEDIUM"],
              ["leaguetable_hard.txt", "HARD"], ["leaguetable_very_hard.txt", "VERY HARD"]]

    def __init__(self):
        self.myHero = Hero()
        self.maze = make_maze_recursion(17, 17)
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself

    # Generates the hero ( the character the users will be able to control) and returns his coordinates
    def _get_hero(self):
        environment = self.MyEnvironment.get_environment()
        # Tries to generate the hero as many times as his position in the maze corresponds to the symbol '0'
        while environment[self.myHero.getcoordX()][self.myHero.getcoordY()] != 0:
            self.myHero = Hero()
        return [self.myHero.getcoordX(), self.myHero.getcoordY()]

    # Adds the hero in the maze
    def set_hero(self):
        XH = self._get_hero()[0]
        YH = self._get_hero()[1]
        self.MyEnvironment.set_coord(XH, YH, 2)

    # Resets all of the characters at their initial abilities and the environment at its initial state
    def reset(self):
        self.myHero.reset_hero_abilities()
        Monster.reset_monsters()
        Goblin.reset_goblins()
        self.MyEnvironment = _Environment(self.maze)

    # Loads all the variables that have been saved in the backup file by using the pickle method
    def load(self):
        f = open("backup", "rb")
        self.myHero.set_moves(pickle.load(f))
        health = pickle.load(f)
        coins = pickle.load(f)
        monsters_visited = pickle.load(f)
        coord_X = pickle.load(f)
        coord_Y = pickle.load(f)
        self.myHero.load_hero_abilities(health, coins, monsters_visited, coord_X, coord_Y)
        Monster.all_monsters = pickle.load(f)
        Monster.all_coordinates = pickle.load(f)
        Monster.hero_fight = pickle.load(f)
        Goblin.all_goblins = pickle.load(f)
        Goblin.all_coordinates = pickle.load(f)
        maze = pickle.load(f)
        self.MyEnvironment = _Environment(maze)
        difficulty = pickle.load(f)
        Creature.set_difficulty(difficulty)
        Monster.abilities = pickle.load(f)
        Goblin.abilities = pickle.load(f)
        f.close()

    # Prints a league table which has been saved in a file with the first 10 players ordered by the number of the coins
    @staticmethod
    def league_table(file):
        f = open(file, "r")
        fl = f.readlines()
        if fl != " ":
            n = len(fl)
            if n > 20:
                n = 20
            line = 1
            for i in range(0, n, 2):
                print(line, str(fl[i].rstrip('\n')) + " " + str(fl[i + 1].rstrip('\n')))
                line += 1
        f.close()

    # Updates one of the league tables accordingly
    @classmethod
    def update_league_table(cls, file):
        league_table = []
        f = open(file, "r")
        fl = f.readlines()
        n = len(fl)
        for i in range(0, n, 2):
            # Takes the names and the coins of the users and adds them to a 2-dimensional array
            league_table.append([fl[i].rstrip('\n'), int(fl[i + 1].rstrip('\n'))])
        f.close()
        # Sorts the array by the number of the coins
        league_table.sort(key=lambda x: x[1], reverse=True)
        # Resets the arrays of users and coins
        cls._users = []
        cls._coins = []
        # Adds the new sorted league table array to the users and coins array
        # (users names to array "users" and coins to array "coins")
        for i in range(0, len(league_table)):
            cls._users.append(league_table[i][0])
            cls._coins.append(league_table[i][1])
        # Opens a file and updates it with the new league table
        f = open(file, "w")
        for i in range(0, len(cls._users)):
            f.write(cls._users[i] + '\n' + str(cls._coins[i]) + '\n')
        f.close()

    # After winning the game, the player must type a name of their choice
    # which will be saved along with the number of coins
    #  they managed to win
    def type_user(self):
        user = input("Type a user name: ")
        Game._users.append(user)
        Game._coins.append(self.myHero.getcoins())

    # Saves the user and the coins in a file
    @classmethod
    def save_user(cls, file):
        f = open(file, "a+")
        f.write(cls._users[-1] + '\n' + str(cls._coins[-1]) + '\n')
        f.close()

    # Prints the menu of the game
    @staticmethod
    def menu():
        print("MENU: START GAME (press ENTER ) | LOAD GAME (press L) | HELP (press H)  | LEAGUE TABLE (press T)| "
              "EXIT (press E)")

    # Prints the instructions of the game
    @staticmethod
    def instructions():
        print("INSTRUCTIONS:")
        print("press up key, right key, left key or down key for moving in the maze")
        print("press E for exiting the game")
        print("press S for saving the game ")

    # Gives the player the opportunity to choose from the options from the menu
    @staticmethod
    def choose_option():
        print("Choose an option ! ")
        ch = getch()
        return ch

    # Prints the 4 difficulties the player has to choose from
    @staticmethod
    def difficulties():
        print("EASY (PRESS 0) | MEDIUM (PRESS 1) | HARD (PRESS 2) | VERY HARD (PRESS 3)")

    # The player is required to choose the difficulty for the game before starting it
    @staticmethod
    def choose_difficulty():
        print("Choose a difficulty! ")
        difficulty = getch()
        while not (48 <= ord(difficulty) <= 51):
            print("Wrong input!")
            print("Choose a difficulty! ")
            difficulty = getch()
        Creature.set_difficulty(int(difficulty))

    # The player starts playing the game
    def play(self):
        Game.menu()
        # The player must choose an option
        option = Game.choose_option()
        while ord(option) != 13 and ord(option) != 76:  # While the player does not choose to press ENTER
            # (starting the game) or L ( loading a game) ,
            # the program will keep showing the menu and the options again after the player chooses from
            # the other options
            if ord(option) == 72:  # player presses H and the instructions are printed
                Game.instructions()
            elif ord(option) == 84:  # player presses T and the league table is printed
                for i in range(0, 4):
                    print(Game._files[i][1])
                    Game.league_table(Game._files[i][0])
            elif ord(option) == 69:  # the player presses E and the program stops working
                sys.exit()
            else:  # if the player chooses another option, the " wrong input" message will be displayed
                print("Wrong input")
            Game.menu()
            option = Game.choose_option()
        if ord(option) == 13:  # if the player presses ENTER, they will be asked to choose a difficulty
            # and the game starts
            Game.difficulties()
            Game.choose_difficulty()
            # Initialises the hero and the creatures in the maze
            self.set_hero()
            self.MyEnvironment.set_creatures()
        if ord(option) == 76:  # if the player presses L, the program will display the game that has been
            # saved by the player
            self.load()
            print("Game loaded!")

        # The program prints the maze , the hero's and the creatures' details
        print("============================ Difficulty: ", Game._files[Creature.get_difficulty()][1])
        self.MyEnvironment.print_environment()
        self.myHero.hero_details()
        Monster.monsters_details()
        Goblin.goblins_details()
        while True:  # the game starts in an infinite loop which stops only when the player wins or loses
            if self.myHero.move(self.MyEnvironment.get_environment()):  # Checks if the player made a correct move
                # if self.myHero.move_debug(environment):  #this works in debug mode
                print("============================ Difficulty: ",Game._files[Creature.get_difficulty()][1])
                # Prints the maze and increases the moves the hero has made
                self.MyEnvironment.print_environment()
                self.myHero.increase_moves()
                print("============================", self.myHero.get_moves())
                XH = self.myHero.getcoordX()
                YH = self.myHero.getcoordY()
                print("Hero new position: ", XH, YH)  # Prints the new position of the hero
                if self.myHero.gethealth() > 0:
                    print("Health", self.myHero.gethealth())  # Prints the hero's health
                else:
                    print("Health 0")
                print("Coins", self.myHero.getcoins())  # Prints the hero's coins
                print("Monsters visited:", sum(Monster.hero_fight))  # Prints how many monsters
                # the hero has visited so far
                if self.myHero.lose_game():  # if the hero lost the game, prints an appropiate message
                    # and ends the game
                    print("Hero lost!")
                    break
                else:
                    # If the hero won the game, prints an appropiate message and allows the player to write their name
                    if self.myHero.win_game():
                        print("Hero wins!")
                        self.type_user()
                        # Saves the user in the one of the league table and updates the league table
                        Game.save_user(Game._files[Creature.get_difficulty()][0])
                        Game.update_league_table(Game._files[Creature.get_difficulty()][0])
                        break
                # While playing the game, the player will be able to see the current map with
                # all the creatures and their
                # positions in the maze and abilities or
                # by pressing H they will see the game instructions
                print("Press M for seeing the current map with the type of creatures and their positions in the maze")
                print("Press H for seeing the game available operations")
                ch = getch()
                if ch == b'M': # The player pressed M
                    print("============================ Difficulty: " , Game._files[Creature.get_difficulty()][1])
                    self.MyEnvironment.print_environment()
                    print("============================")
                    self.myHero.hero_details()
                    Monster.monsters_details()
                    Goblin.goblins_details()
                elif ch == b'H': # The player pressed H
                    Game.instructions()
                elif ch == b'E': # If the player presses E, the game will stop
                    sys.exit()
                elif ch == b'S': # If the player presses S, the game will be saved and they will be able
                    # to replay it later
                    self.myHero.save_game(self.MyEnvironment.get_environment())


if __name__ == "__main__":
    myGame = Game() # Creates the game instance
    while True:
        # The game will run infinitely many times and it will reset as well, unless the player ends the
        # program by pressing E
        myGame.play()
        myGame.reset()

