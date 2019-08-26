import pygame
from pygame import *

from lib import *
from entities import constants
from .platformblock import PlatformBlock


class GoalBlockLeft(PlatformBlock):

    image_empty = "images/sprites/HUD/hudHeart_empty.png"
    image_full = "images/sprites/HUD/hudHeart_full.png"

    collides = True
    has_grip = False

    def __init__(self, x, y):
        PlatformBlock.__init__(self, x, y)
        self.set_draw_procedural(constants.TILE_X, constants.TILE_Y, self.image_empty)
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)

    def set_draw_procedural(self, tile_x, tile_y, image_file):
        bessel_perc = 8
        color_dark = "#b3b300"
        color_light = "#e6e600"
        color_main = "#ffff99"

        temp = create_block_bessel_left(
            constants.TILE_X,
            constants.TILE_Y,
            color_dark, color_light, color_main,
            bessel_perc)

        flip = False
        temp_image = pygame.image.load(image_file)
        if flip:
            temp_image = pygame.transform.flip(temp_image, True, False)
        temp_image = pygame.transform.scale(temp_image, (constants.TILE_X, constants.TILE_Y))
        temp.blit(temp_image, [constants.TILE_X//2, 0])

        self.image = temp