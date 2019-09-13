import pygame
from pygame import *
from screen_config.screen_config import ScreenConfig


def pg_print_message(
        screen,
        screen_config: ScreenConfig,
        message,
        x,
        y,
        sys_font="TO DEFINE A FONT",
        bold=True,
        size=32,
        color_fg=(237, 210, 36),
        color_bg=(0, 0, 0),
        alias=8,
        offset=4
):
    size = int(round((screen_config.w / 1366) * (size / 32) * 32))
    x = screen_config.x_offset + int(round((screen_config.w / 1366)*x))
    y = screen_config.y_offset + int(round((screen_config.w / 1366)*y))

    my_font = pygame.font.SysFont(sys_font, size)
    my_font.set_bold(bold)
    text = my_font.render(message, alias, color_bg)
    screen.blit(text, (x + offset, y + offset))
    screen.blit(text, (x - offset, y - offset))
    screen.blit(text, (x + offset, y - offset))
    screen.blit(text, (x - offset, y + offset))
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
    def new_caption(screen, screen_config):
        pg_print_message(
            screen,
            screen_config,
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

