#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

import random
from character import Character

class Monster(Character):
    """define your monster class here"""
    def __init__(self):
        super().__init__()
        self._ability = random.randint(1, 4)