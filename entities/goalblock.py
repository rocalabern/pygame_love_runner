import pygame
from pygame import *

from lib import *
from entities import constants
from .platformblock import PlatformBlock


def draw_procedural_simple():
    temp = Surface((constants.TILE_X, constants.TILE_Y))
    temp.convert()
    temp.fill(Color("#99ff99"))
    return temp


def draw_procedural(tile_x, tile_y):
    bessel_perc = 8
    color_dark = "#b3b300"
    color_light = "#e6e600"
    color_main = "#ffff99"

    temp = create_block_bessel(
        constants.TILE_X,
        constants.TILE_Y,
        color_dark, color_light, color_main,
        bessel_perc)

    return temp

class GoalBlock(PlatformBlock):

    collides = True
    has_grip = False

    def __init__(self, x, y):
        PlatformBlock.__init__(self, x, y)
        self.image = draw_procedural(constants.TILE_X, constants.TILE_Y)
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)
