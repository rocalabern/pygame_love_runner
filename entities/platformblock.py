import pygame
from pygame import *

from entities import constants
from .entity import Entity


class PlatformBlock(Entity):

    collides = True
    has_grip = False

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((constants.TILE_X, constants.TILE_Y))
        self.image.convert()
        self.image.fill(Color("#392613"))
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)
