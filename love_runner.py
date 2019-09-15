import pygame
from pygame import *

from lib import *
from entities import constants
from levels import GameplayLevel
from levels.tutorial_levels import *
from levels.game_levels import *
from game_screen.game_screen import GameScreen
from title.title import menu_title

# SCREEN_WIDTH = 1366
# SCREEN_HEIGHT = 768
# SCREEN_WIDTH = 1280
# SCREEN_HEIGHT = 1024
# WIN_WIDTH = 1245
# WIN_HEIGHT = 700
# WIN_WIDTH = 875
# WIN_HEIGHT = 700


def main(win_width: int=875, win_height: int=700):
    pygame.mixer.pre_init(48000, -16, 2, 2048)
    pygame.init()
    if win_width is None or win_height is None:
        screen_window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen_window = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Love Runner")

    game_screen = GameScreen(screen_window)
    constants.game_screen = game_screen

    levels = [
        # tutorial_01(game_screen),
        # tutorial_02(game_screen),
        tutorial_03(game_screen),
        # tutorial_04(game_screen),
        # tutorial_05(game_screen),
        # tutorial_06(game_screen),
        # tutorial_07(game_screen),
        # tutorial_08(game_screen),
        # tutorial_09(game_screen),
        # tutorial_10(game_screen),
        tutorial_11(game_screen),
        level_02_Patri(game_screen),
        level_03_Dani(game_screen),
        level_04_Cor(game_screen)
    ]

    # for i in range(1, len(levels)):
    #     level = levels[i-1]
        # level.add_caption(create_caption("Level " + str(i).zfill(2), 5, 5, color_fg=(170, 170, 170)))

    menu_title(game_screen)

    done = False
    i = 0
    while i < len(levels) and not done:
        gameplay_level = GameplayLevel(levels[i])
        gameplay_level.play()
        i = i + 1


if __name__ == "__main__":
    main()
