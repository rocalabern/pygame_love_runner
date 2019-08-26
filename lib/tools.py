import pygame
from pygame import *


def read_level(str_file):
    with open(str_file) as f:
        line_list = f.readlines()

    line_list = [line.rstrip('\n') for line in open(str_file)]
    return line_list


def pg_print_message(
        screen,
        message,
        x,
        y,
        sys_font="suruma",
        bold=True,
        size=32,
        color_fg=(237, 210, 36),
        color_bg=(0, 0, 0),
        alias=8,
        offset=2
):
    my_font = pygame.font.SysFont(sys_font, size)
    my_font.set_bold(bold)
    text = my_font.render(message, alias, color_bg)
    screen.blit(text, (x+offset, y+offset))
    text = my_font.render(message, alias, color_fg)
    screen.blit(text, (x, y))


def create_caption(
        message,
        x,
        y,
        sys_font="suruma",
        bold=True,
        size=32,
        color_fg=(237, 210, 36),
        color_bg=(0, 0, 0),
        alias=8,
        offset=2
):
    def new_caption(screen):
        pg_print_message(
            screen,
            message,
            x,
            y,
            sys_font,
            bold,
            size,
            color_fg,
            color_bg,
            alias,
            offset
        )

    return new_caption


def create_block_bessel(tile_x, tile_y, color_dark, color_main, color_light, bessel_perc = 8):
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