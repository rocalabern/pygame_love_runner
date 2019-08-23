import pygame
from pygame import *

from entities import constants
from .entity import Entity


class StairsBlock(Entity):

    collides = False
    has_grip = True

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((constants.TILE_X, constants.TILE_Y))
        self.image.convert()
        self.image.fill(Color(constants.COLOR_STAIRS_BCKGRND))
        for i_step in range(constants.TILE_Y // 4):
            print(x)
            self.image.fill(Color(constants.COLOR_STAIRS), Rect(0, 8*i_step, constants.TILE_X, 1))
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)

0