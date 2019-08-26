import pygame
from pygame import *

from lib import *
from levels import *


def level_01():
    level = Level("levels/game_levels/level_01.txt", 16)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    return level



