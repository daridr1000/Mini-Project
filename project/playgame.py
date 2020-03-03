from character.hero import Hero
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
from character.creature.monster import Monster
from character.creature.goblin import Goblin
from character.creature import Creature
from getch1 import *
import sys,math

WALL_CHAR = "#"
SPACE_CHAR = "-"
HERO_CHAR = "H"
MONSTER_CHAR = "M"
GOBLIN_CHAR = "G"


class _Environment:
    """Environment includes Maze+Monster+Goblin"""

    def __init__(self, maze):
        self._environment = deepcopy(maze)

    def set_coord(self, x, y, val):
        self._environment[x][y] = val

    def get_coord(self, x, y):
        return self._environment[x][y]

    def get_environment(self):
        return self._environment

    def print_environment(self):
        """print out the environment in the terminal"""
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("1", WALL_CHAR)  # replace the wall character
            row_str = row_str.replace("0", SPACE_CHAR)  # replace the space character
            row_str = row_str.replace("2", HERO_CHAR )  # replace the hero character
            row_str = row_str.replace("3", MONSTER_CHAR)  # replace the monster character
            row_str = row_str.replace("4", GOBLIN_CHAR)  # replace the goblin character
            print("".join(row_str))


class Game:
    _count = 0
    _users = []
    _coins = []
    _files = [["leaguetable_easy.txt", "EASY"], ["leaguetable_medium.txt", "MEDIUM"],
              ["leaguetable_hard.txt", "HARD"], ["leaguetable_very_hard.txt", "VERY HARD"]]

    def __init__(self):
        self.myHero = Hero()
        self.maze = make_maze_recursion(17, 17)
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself
        self._count = 0

    def _get_hero(self):
        environment = self.MyEnvironment.get_environment()
        while environment[self.myHero.getcoordX()][self.myHero.getcoordY()] != 0:
            self.myHero = Hero()
        return [self.myHero.getcoordX(), self.myHero.getcoordY()]

    def _get_monster(self):
        environment = self.MyEnvironment.get_environment()
        monster = Monster()
        while environment[monster.getcoordX()][monster.getcoordY()] != 0:
            Monster.hero_fight.remove(Monster.hero_fight[Monster.all_monsters.index(monster)])
            Monster.all_monsters.remove(monster)
            Monster.all_coordinates.remove([monster.getcoordX(), monster.getcoordY()])
            monster = Monster()
        monster.set_ability()
        return [monster.getcoordX(), monster.getcoordY()]

    def _get_goblin(self):
        environment = self.MyEnvironment.get_environment()
        goblin = Goblin()
        while environment[goblin.getcoordX()][goblin.getcoordY()] != 0:
            Goblin.all_goblins.remove(goblin)
            Goblin.all_coordinates.remove([goblin.getcoordX(), goblin.getcoordY()])
            goblin = Goblin()
        goblin.set_ability()
        return [goblin.getcoordX(), goblin.getcoordY()]

    @staticmethod
    def menu():
        print("MENU: START GAME (press ENTER ) | LOAD GAME (press L) | HELP (press H)  | LEAGUE TABLE (press T)| "
              "EXIT (press E)")

    @staticmethod
    def instructions():
        print("INSTRUCTIONS:")
        print("press up key, right key, left key or down key for moving in the maze")
        print("press E for exiting the game")
        print("press S for saving the game ")

    def _load_abilities(self, lines):
        self._count = int(lines[0].rstrip('\n'))
        self.myHero.load_hero_abilities(int(lines[1].rstrip('\n')), int(lines[2].rstrip('\n')),
                                        int(lines[3].rstrip('\n')),int(lines[9].rstrip('\n')),int(lines[10].rstrip('\n')))
        for i in list(range(4, 8)) + [11,13]:
            lines[i] = lines[i].rstrip('\n')
            lines[i]=lines[i].strip('][').split(', ')
        coord_m = []
        coord_g = []
        for i in range(0,10,2):
            coord_m.append(lines[4][i:(i+2)])
            coord_g.append(lines[6][i:(i+2)])
        for i in range(0,4):
            coord_m[i][1] = coord_m[i][1].replace(']','')
            coord_g[i][1] = coord_g[i][1].replace(']','')
        for i in range(1, 5):
            coord_m[i][0] = coord_m[i][0].replace('[','')
            coord_g[i][0] = coord_g[i][0].replace('[','')
        for i in range(0,5):
            for j in range(0,2):
                coord_m[i][j] = int(coord_m[i][j])
                coord_g[i][j] = int(coord_g[i][j])
        for i in range(0,len(lines[5])):
            lines[5][i] = int(lines[5][i])
        for i in range(0,len(lines[11])):
            lines[11][i] = int(lines[11][i])
        for i in range(0,len(lines[12])):
            lines[12][i] = int(lines[12][i])
        Monster.load_monsters(coord_m, lines[5],lines[11])
        Goblin.load_goblins(coord_g,lines[12])
        maze = []
        for i in range(0,len(lines[7]),int(math.sqrt(len(lines[7])))):
            maze.append(lines[7][i:(i+int(math.sqrt(len(lines[7]))))])
        for i in range(0,len(maze)):
            maze[i][16] = maze[i][0] = 1
        for i in range(0,len(maze)):
            for j in range(0,len(maze)):
                maze[i][j] = int(maze[i][j])
        self.MyEnvironment = _Environment(maze)
        Creature.set_difficulty(int(lines[8].rstrip('\n')))

    def load(self):
        f = open("load_game.txt", "r")
        fl = f.readlines()
        self._load_abilities(fl)
        f.close()

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

    @classmethod
    def update_league_table(cls, file):
        league_table = []
        f = open(file, "r")
        fl = f.readlines()
        n = len(fl)
        if n > 20:
            n = 20
        for i in range(0, n, 2):
            league_table.append([fl[i].rstrip('\n'), int(fl[i + 1].rstrip('\n'))])
        f.close()
        league_table.sort(key=lambda x: x[1], reverse=True)
        cls._users = []
        cls._coins = []
        for i in range(0, len(league_table)):
            cls._users.append(league_table[i][0])
            cls._coins.append(league_table[i][1])
        f = open(file, "w")
        for i in range(0, len(cls._users)):
            f.write(cls._users[i] + '\n' + str(cls._coins[i]) + '\n')
        f.close()

    def type_user(self):
        user = input("Type a user name: ")
        Game._users.append(user)
        Game._coins.append(self.myHero.getcoins())

    @classmethod
    def save_user(cls, file):
        f = open(file, "a+")
        f.write(cls._users[-1] + '\n' + str(cls._coins[-1]) + '\n')
        f.close()

    def _set_hero(self, environment):
        XH = self._get_hero()[0]
        YH = self._get_hero()[1]
        environment[XH][YH] = 2

    def _set_creatures(self, environment):
        for i in range(0, 5):
            monster = self._get_monster()
            XM = monster[0]
            YM = monster[1]
            environment[XM][YM] = 3
            goblin = self._get_goblin()
            XG = goblin[0]
            YG = goblin[1]
            environment[XG][YG] = 4

    @staticmethod
    def choose_option():
        print("Choose an option ! ")
        ch = getch()
        return ch

    def reset(self):
        self._count = 0
        self.myHero.reset_hero_abilities()
        Monster.reset_monsters()
        Goblin.reset_goblins()
        self.MyEnvironment = _Environment(self.maze)

    @staticmethod
    def choose_difficulty():
        print("Choose a difficulty! ")
        difficulty = getch()
        while not (48 <= ord(difficulty) <= 51):
            print("Wrong input!")
            print("Choose a difficulty! ")
            difficulty = getch()
        Creature.set_difficulty(int(difficulty))

    @staticmethod
    def difficulties():
        print("EASY (PRESS 0) | MEDIUM (PRESS 1) | HARD (PRESS 2) | VERY HARD (PRESS 3)")

    def play(self):
        Game.menu()
        option = Game.choose_option()
        while ord(option) != 13 and ord(option) != 76:
            if ord(option) == 72:
                Game.instructions()
            elif ord(option) == 84:
                for i in range(0, 4):
                    print(Game._files[i][1])
                    Game.league_table(Game._files[i][0])
            elif ord(option) == 69:
                sys.exit()
            else:
                print("Wrong input")
            Game.menu()
            option = Game.choose_option()
        if ord(option) == 13:
            Game.difficulties()
            Game.choose_difficulty()
            print("============================")
            environment = self.MyEnvironment.get_environment()
            self._set_hero(environment)
            self._set_creatures(environment)
        if ord(option) == 76:
            self.load()
            print("Game loaded!")
        self.MyEnvironment.print_environment()
        self.myHero.hero_details()
        Monster.monsters_details()
        Goblin.goblins_details()
        while True:
            if self.myHero.move(self.MyEnvironment.get_environment()):
                # if self.myHero.move_debug(environment):  #this works in debug mode
                print("============================")
                self.MyEnvironment.print_environment()
                self._count += 1
                self.myHero.increase_gem()
                print("============================", self._count)
                XH = self.myHero.getcoordX()
                YH = self.myHero.getcoordY()
                print("Hero new position: ", XH, YH)
                print("Monsters abilities: ",Monster.abilities)
                print("Goblins abilities: ",Goblin.abilities)
                if self.myHero.gethealth() > 0:
                    print("Health", self.myHero.gethealth())
                else:
                    print("Health 0")
                print("Coins", self.myHero.getcoins())
                print("Monsters visited:", sum(Monster.hero_fight))
                if self.myHero.lose_game():
                    print("Hero lost!")
                    break
                else:
                    if self.myHero.win_game():
                        print("Hero wins!")
                        self.type_user()
                        Game.save_user(Game._files[Creature.get_difficulty()][0])
                        Game.update_league_table(Game._files[Creature.get_difficulty()][0])
                        break
                print("Press M for seeing the current map with the type of creatures and their positions in the maze")
                print("Press H for seeing the game available operations")
                ch = getch()
                if ch == b'M':
                    print("============================")
                    self.MyEnvironment.print_environment()
                    print("============================")
                    self.myHero.hero_details()
                    Monster.monsters_details()
                    Goblin.goblins_details()
                elif ch == b'H':
                    Game.instructions()




if __name__ == "__main__":

    myGame = Game()
    while True:
        myGame.play()
        myGame.reset()
