import pygame
from pygame import *

from lib import *
from entities import constants
from .entity import Entity


def draw_sprite():
    image_file = "images/sprites/ground/stoneCenter.png"
    # image_file = "images/sprites/items/boxCrate.png"
    temp = pygame.image.load(image_file)
    temp = pygame.transform.scale(temp, (constants.TILE_X, constants.TILE_Y))
    return temp


def draw_procedural_simple():
    temp = Surface((constants.TILE_X, constants.TILE_Y))
    temp.convert()
    temp.fill(Color("#392613"))
    return temp


def draw_procedural(tile_x, tile_y):
    bessel_perc = 8
    color_dark = "#a3a375"
    color_light = "#ebebe0"
    color_main = "#ccccb3"

    temp = create_block_bessel(
        constants.TILE_X,
        constants.TILE_Y,
        color_dark, color_light, color_main,
        bessel_perc)

    return temp

class PlatformBlock(Entity):

    collides = True
    has_grip = False

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = draw_procedural(constants.TILE_X, constants.TILE_Y)
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)
