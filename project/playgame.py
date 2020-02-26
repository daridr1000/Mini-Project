from character.hero import Hero
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
from character.creature.monster import Monster
from character.creature.goblin import Goblin
import sys

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
            row_str = row_str.replace("2", HERO_CHAR)  # replace the hero character
            row_str = row_str.replace("3", MONSTER_CHAR)  # replace the monster character
            row_str = row_str.replace("4", GOBLIN_CHAR)  # replace the hero character
            print("".join(row_str))


class Game:
    _count = 0
    _users = []
    _coins = []

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
    def save():
        pass

    @staticmethod
    def instructions():
        pass

    @staticmethod
    def league_table():
        f = open("leaguetable.txt", "r")
        fl = f.readlines()
        if fl != " ":
            line = 1
            for i in range(0, len(fl) - 1, 2):
                print(line, str(fl[i].rstrip('\n')) + " " + str(fl[i + 1].rstrip('\n')))
                line += 1
        f.close()

    @classmethod
    def update_league_table(cls):
        league_table = []
        f = open("leaguetable.txt", "r")
        fl = f.readlines()
        for i in range(0, len(fl) - 1, 2):
            league_table.append([fl[i].rstrip('\n'), int(fl[i + 1])])
        f.close()
        league_table.sort(key=lambda x: x[1], reverse=True)
        cls._users = []
        cls._coins = []
        for i in range(0, len(league_table)):
            cls._users.append(league_table[i][0])
            cls._coins.append(league_table[i][1])
        f = open("leaguetable.txt", "w")
        for i in range(0, len(cls._users)):
            f.write(cls._users[i] + '\n' + str(cls._coins[i]) + '\n')
        f.close()

    def type_user(self):
        user = input("Type a user name: ")
        Game._users.append(user)
        Game._coins.append(self.myHero.getcoins())

    @classmethod
    def save_user(cls):
        f = open("leaguetable.txt", "a+")
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

    def _hero_details(self):
        print("Hero position: ", self.myHero.getcoordX(), self.myHero.getcoordY())
        print("Health", self.myHero.gethealth())
        print("Coins", self.myHero.getcoins())

    @staticmethod
    def _monsters_details():
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

    @staticmethod
    def _goblins_details():
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

    @staticmethod
    def choose_option():
        ch = sys.stdin.read(1)
        if ch == 'L':
            Game.save()
            return False
        elif ch == 'H':
            Game.instructions()
            return False
        elif ch == 'T':
            Game.league_table()
            return False
        elif ch == 'E':
            sys.exit()
        elif ch == '\n':
            return True
        else:
            return False

    def reset(self):
        self._count = 0
        self.myHero.reset_hero_abilities()
        Monster.reset_monsters()
        Goblin.reset_goblins()
        self.MyEnvironment = _Environment(self.maze)

    def play(self):
        Game.menu()
        while not Game.choose_option():
            Game.choose_option()
            Game.menu()
        environment = self.MyEnvironment.get_environment()
        self._set_hero(environment)
        self._set_creatures(environment)
        self.MyEnvironment.print_environment()
        self._hero_details()
        Game._monsters_details()
        Game._goblins_details()
        while True:
            if self.myHero.move(self.MyEnvironment.get_environment()):
                # if self.myHero.move_debug(environment):  #this works in debug mode
                self.MyEnvironment.print_environment()
                self._count += 1
                print("============================", self._count)
                XH = self.myHero.getcoordX()
                YH = self.myHero.getcoordY()
                print("Hero new position: ", XH, YH)
                if self.myHero.gethealth() > 0:
                    print("Health", self.myHero.gethealth())
                else:
                    print("Health 0")
                print("Coins", self.myHero.getcoins())
                print("Monsters visited:", Monster.hero_fight)
                if self.myHero.lose_game():
                    print("Hero lost!")

                    break
                else:
                    if self.myHero.win_game():
                        print("Hero wins!")
                        self.type_user()
                        Game.save_user()
                        Game.update_league_table()
                        """ADD LEAGUE TABLE , INSTRUCTIONS AND DIFFICULTIES! """
                        break


if __name__ == "__main__":

    myGame = Game()
    while True:
        myGame.play()
        myGame.reset()
