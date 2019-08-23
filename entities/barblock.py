import pygame
from pygame import *

from entities import constants
from .entity import Entity


class BarBlock(Entity):

    collides = False
    has_grip = True

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((constants.TILE_X, constants.TILE_Y))
        self.image.convert()
        self.image.fill(Color(constants.COLOR_BAR_BCKGRND), Rect(2, 2, constants.TILE_X - 2, constants.TILE_Y - 2))
        self.image.fill(Color(constants.COLOR_BAR), Rect(0, 0, constants.TILE_X, 2))
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)
