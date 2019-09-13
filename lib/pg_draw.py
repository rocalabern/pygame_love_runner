import pygame
from pygame import *
from screen_config.screen_config import ScreenConfig


def create_block_bessel(tile_x, tile_y, color_dark, color_main, color_light, bessel_perc=8):
    offset_x = int(round(tile_x / bessel_perc))
    offset_y = int(round(tile_y / bessel_perc))

    temp = Surface((tile_x, tile_y))
    temp.convert()

    points = [
        (0, 0),
        (offset_x, offset_y),
        (offset_x, tile_y - offset_y),
        (tile_x - offset_x, tile_y - offset_y),
        (tile_x, tile_y),
        (0, tile_y)]
    pygame.draw.polygon(temp, Color(color_dark), points)

    points = [
        (0, 0),
        (tile_x, 0),
        (tile_x, tile_y),
        (tile_x - offset_x, tile_y - offset_y),
        (tile_x - offset_x, offset_y),
        (offset_x, offset_y),
    ]
    pygame.draw.polygon(temp, Color(color_light), points)

    temp.fill(Color(color_main), Rect(offset_x, offset_y, tile_x - 2 * offset_x, tile_y - 2 * offset_y))

    return temp


def create_block_bessel_left(tile_x, tile_y, color_dark, color_main, color_light, bessel_perc = 8):
    offset_x = int(round(tile_x / bessel_perc))
    offset_y = int(round(tile_y / bessel_perc))

    temp = Surface((tile_x, tile_y))
    temp.convert()

    points = [
        (0, 0),
        (offset_x, offset_y),
        (offset_x, tile_y - offset_y),
        (tile_x, tile_y - offset_y),
        (tile_x, tile_y),
        (0, tile_y)]
    pygame.draw.polygon(temp, Color(color_dark), points)

    points = [
        (0, 0),
        (tile_x, 0),
        (tile_x, offset_y),
        (offset_x, offset_y),
    ]
    pygame.draw.polygon(temp, Color(color_light), points)

    temp.fill(Color(color_main), Rect(offset_x, offset_y, tile_x, tile_y - 2 * offset_y))

    return temp


def create_block_bessel_right(tile_x, tile_y, color_dark, color_main, color_light, bessel_perc = 8):
    offset_x = int(round(tile_x / bessel_perc))
    offset_y = int(round(tile_y / bessel_perc))

    temp = Surface((tile_x, tile_y))
    temp.convert()

    points = [
        (0,tile_y - offset_y),
        (tile_x - offset_x, tile_y - offset_y),
        (tile_x, tile_y),
        (0, tile_y)]
    pygame.draw.polygon(temp, Color(color_dark), points)

    points = [
        (0, 0),
        (tile_x, 0),
        (tile_x, tile_y),
        (tile_x - offset_x, tile_y - offset_y),
        (tile_x - offset_x, offset_y),
        (0, offset_y),
    ]
    pygame.draw.polygon(temp, Color(color_light), points)

    temp.fill(Color(color_main), Rect(0, offset_y, tile_x - offset_x, tile_y - 2 * offset_y))

    return temp

