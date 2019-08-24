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

        # image_file = "images/sprites/ground/stoneCenter.png"
        # image_file = "images/sprites/items/boxCrate.png"
        # temp = pygame.image.load(image_file)
        # temp = pygame.transform.scale(temp, (constants.TILE_X, constants.TILE_Y))
        # self.image = temp
