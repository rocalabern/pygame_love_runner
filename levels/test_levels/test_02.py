import pygame
from pygame import *

from lib import *
from levels import *


def test_02():
    level = Level("levels/test_levels/test_02.txt", 32, velocity_jump=5)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    return level



