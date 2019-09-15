import pygame
from pygame import *
from game_screen.game_screen import GameScreen


def pg_print_message(
        screen: pygame.Surface,
        game_screen: GameScreen,
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
    size = int(round((game_screen.w / 1366) * (size / 32) * 32))
    x = game_screen.x_offset + int(round((game_screen.w / 1366)*x))
    y = game_screen.y_offset + int(round((game_screen.w / 1366)*y))

    my_font = pygame.font.SysFont(sys_font, size)
    my_font.set_bold(bold)
    text = my_font.render(message, alias, color_bg)
    game_screen.screen_desktop.blit(text, (x + offset, y + offset))
    game_screen.screen_desktop.blit(text, (x - offset, y - offset))
    game_screen.screen_desktop.blit(text, (x + offset, y - offset))
    game_screen.screen_desktop.blit(text, (x - offset, y + offset))
    text = my_font.render(message, alias, color_fg)
    game_screen.screen_desktop.blit(text, (x, y))


def create_caption(
        message,
        x,
        y,
        sys_font="TO DEFINE A FONT",
        bold=True,
        size=32,
        color_fg=(237, 210, 36),
        color_bg=(0, 0, 0),
        alias=8,
        offset=2
):
    def new_caption(game_screen):
        pg_print_message(
            None,
            game_screen,
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

