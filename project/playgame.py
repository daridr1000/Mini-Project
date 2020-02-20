from hero import Hero
from maze_gen_recursive import make_maze_recursion
from copy import deepcopy
from monster import Monster
from goblin import Goblin
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
            row_str = row_str.replace("3", MONSTER_CHAR) # replace the monster character
            row_str = row_str.replace("4", GOBLIN_CHAR) # replace the hero character
            print("".join(row_str))


class Game:

    _count = 0

    def __init__(self):
        self.myHero = Hero()
        self.maze = make_maze_recursion(17, 17)
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself
        self._count = 0


    def _get_monster(self):
        environment = self.MyEnvironment.get_environment()
        monster = Monster()
        while environment[monster.getcoordX()][monster.getcoordY()]!=0:
            monster = Monster()
        return [monster.getcoordX(),monster.getcoordY()]


    def _get_goblin(self):
        environment = self.MyEnvironment.get_environment()
        goblin = Goblin()
        while environment[goblin.getcoordX()][goblin.getcoordY()] != 0:
            goblin = Goblin()
        return [goblin.getcoordX(), goblin.getcoordY()]

    def play(self):
        environment=self.MyEnvironment.get_environment()
        XH =self.myHero.getcoordX()
        YH =self.myHero.getcoordY()
        environment[XH][YH]=2
        for i in range(0,5):
            monster=self._get_monster()
            XM = monster[0]
            YM = monster[1]
            environment[XM][YM] = 3
            goblin=self._get_goblin()
            XG = goblin[0]
            YG = goblin[1]
            environment[XG][YG] = 4

        self.MyEnvironment.print_environment()
        print("Hero position: ",XH,YH)
        print("Health", self.myHero.gethealth())
        while True:
            #if self.myHero.move(self.MyEnvironment):
            if self.myHero.move_debug(environment):  #this works in debug mode
                self.MyEnvironment.print_environment()
                self._count += 1
                print("============================", self._count)
                XH = self.myHero.getcoordX()
                YH = self.myHero.getcoordY()
                print("Hero new position: ",XH,YH)
                print("Health",self.myHero.gethealth())
                if self.myHero.gethealth()==0:
                    break


if __name__ == "__main__":

    myGame = Game()
    myGame.play()
    