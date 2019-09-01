import pygame
from pygame import *

from entities import constants
from .entity import Entity
from .barblock import BarBlock


def draw_procedural():
    temp = Surface((constants.TILE_X, constants.TILE_Y))
    temp.convert()
    temp.fill(Color(constants.COLOR_BAR_BCKGRND), Rect(0, 0, constants.TILE_X, constants.TILE_Y))
    # temp.fill(Color(constants.COLOR_BAR), Rect(0, 0, constants.TILE_X, 2))
    COLOR_BAR_LIGHT = "#f5f5f0"
    COLOR_BAR = "#adad85"
    COLOR_BAR_DARK = "#5c5c3d"
    if (constants.TILE_Y < 32):
        temp.fill(Color(COLOR_BAR_LIGHT), Rect(0, 2, constants.TILE_X, 1))
        temp.fill(Color(COLOR_BAR), Rect(0, 3, constants.TILE_X, 2))
        temp.fill(Color(COLOR_BAR_DARK), Rect(0, 4, constants.TILE_X, 1))
    else:
        temp.fill(Color(COLOR_BAR_LIGHT), Rect(0, 4, constants.TILE_X, 2))
        temp.fill(Color(COLOR_BAR), Rect(0, 6, constants.TILE_X, 2))
        temp.fill(Color(COLOR_BAR_DARK), Rect(0, 8, constants.TILE_X, 2))

    return temp


class BarHBlock(BarBlock):

    collides = False
    has_grip = True

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = draw_procedural()
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)
