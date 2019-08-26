import pygame
from pygame import *

from entities import constants
from .entity import Entity


def draw_sprite():
    image_file = "images/sprites/items/ladderMid.png"
    temp = pygame.image.load(image_file)
    temp = pygame.transform.scale(temp, (constants.TILE_X, constants.TILE_Y))
    return temp


def draw_procedural():
    temp = Surface((constants.TILE_X, constants.TILE_Y))
    temp.convert()
    temp.fill(Color(constants.COLOR_STAIRS_BCKGRND))
    for i_step in range(constants.TILE_Y // 4):
        temp.fill(Color(constants.COLOR_STAIRS), Rect(0, 8 * i_step, constants.TILE_X, 1))
    return temp


class StairsBlock(Entity):

    collides = False
    has_grip = True

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = draw_procedural()
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)