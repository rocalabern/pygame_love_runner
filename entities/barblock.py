import pygame
from pygame import *

from entities import constants
from .entity import Entity


def draw_procedural():
    temp = Surface((constants.TILE_X, constants.TILE_Y))
    temp.convert()
    temp.fill(Color(constants.COLOR_BAR_BCKGRND), Rect(0, 0, constants.TILE_X, constants.TILE_Y))
    # temp.fill(Color(constants.COLOR_BAR), Rect(0, 0, constants.TILE_X, 2))
    COLOR_BAR_LIGHT = "#f5f5f0"
    COLOR_BAR = "#adad85"
    COLOR_BAR_DARK = "#5c5c3d"
    temp.fill(Color(COLOR_BAR_LIGHT), Rect(0, 0, constants.TILE_X, 1))
    temp.fill(Color(COLOR_BAR_DARK), Rect(0, 2, constants.TILE_X, 3))
    temp.fill(Color(COLOR_BAR), Rect(0, 1, constants.TILE_X, 2))

    return temp


class BarBlock(Entity):

    collides = False
    has_grip = True

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = draw_procedural()
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)
