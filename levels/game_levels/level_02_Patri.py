import pygame
from pygame import *

from lib import *
from levels import *


def level_02_Patri():
    level = Level("levels/game_levels/level_02_Patri.txt", 16)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    return level



