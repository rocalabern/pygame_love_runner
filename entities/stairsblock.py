import pygame
from pygame import *

from entities import constants
from .entity import Entity


def draw_sprite():
    image_file = "images/sprites/items/ladderMid.png"
    temp = pygame.image.load(image_file)
    temp = pygame.transform.scale(temp, (constants.TILE_X, constants.TILE_Y))
    return temp


def draw_procedural_simple():
    temp = Surface((constants.TILE_X, constants.TILE_Y))
    temp.convert()
    temp.fill(Color(constants.COLOR_STAIRS_BCKGRND))
    for i_step in range(constants.TILE_Y // 4):
        temp.fill(Color(constants.COLOR_STAIRS), Rect(0, 8 * i_step, constants.TILE_X, 1))
    return temp


def draw_procedural():
    COLOR_BAR_LIGHT = "#ffe699"
    COLOR_BAR = "#ffbf00"
    COLOR_BAR_DARK = "#b38600"
    temp = Surface((constants.TILE_X, constants.TILE_Y))
    temp.convert()
    temp.fill(Color(constants.COLOR_STAIRS_BCKGRND))
    i_step = 0
    while i_step <= constants.TILE_Y:
        if (constants.TILE_Y<32):
            temp.fill(Color(COLOR_BAR_LIGHT), Rect(0, i_step, constants.TILE_X, 1))
            temp.fill(Color(COLOR_BAR), Rect(0, i_step+1, constants.TILE_X, 1))
            temp.fill(Color(COLOR_BAR_DARK), Rect(0, i_step+2, constants.TILE_X, 1))
            i_step = i_step + 8
        else:
            temp.fill(Color(COLOR_BAR_LIGHT), Rect(0, i_step, constants.TILE_X, 1))
            temp.fill(Color(COLOR_BAR), Rect(0, i_step+1, constants.TILE_X, 2))
            temp.fill(Color(COLOR_BAR_DARK), Rect(0, i_step+3, constants.TILE_X, 1))
            i_step = i_step + 8
    return temp

class StairsBlock(Entity):

    collides = False
    has_grip = True

    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = draw_procedural()
        self.rect = Rect(x, y, constants.TILE_X, constants.TILE_Y)