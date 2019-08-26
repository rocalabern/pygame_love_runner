import pygame
from pygame import *

from lib import *
from levels import *


def test_03():
    level = Level("levels/test_levels/test_03.txt", 16, velocity_jump=4)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    return level



