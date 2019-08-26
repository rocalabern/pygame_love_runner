import pygame
from pygame import *

from lib import *
from levels import *


def test_01():
    level = Level("levels/test_levels/test_01.txt", 60, velocity_jump=6)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    return level



