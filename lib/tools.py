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
