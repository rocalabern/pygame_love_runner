import pygame
from pygame import *

from lib import *
from entities import constants
from levels import GameplayLevel
from levels.tutorial_levels import *
from levels.game_levels import *
from screen_config.screen_config import ScreenConfig
from title.title import menu_title


def main():
    pygame.mixer.pre_init(48000, -16, 2, 2048)
    pygame.init()

    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((constants.WIN_WIDTH, constants.WIN_HEIGHT))
    pygame.display.set_caption("Love Runner")
    clock = pygame.time.Clock()

    info_display = pygame.display.Info()
    screen_config = ScreenConfig(info_display)
    constants.screen_config = screen_config

    levels = [
        tutorial_01(screen, screen_config, clock),
        tutorial_02(screen, screen_config, clock),
        tutorial_03(screen, screen_config, clock),
        tutorial_04(screen, screen_config, clock),
        tutorial_05(screen, screen_config, clock),
        tutorial_06(screen, screen_config, clock),
        tutorial_07(screen, screen_config, clock),
        tutorial_08(screen, screen_config, clock),
        tutorial_09(screen, screen_config, clock),
        tutorial_10(screen, screen_config, clock),
        tutorial_11(screen, screen_config, clock),
        level_02_Patri(screen, screen_config, clock),
        level_03_Dani(screen, screen_config, clock),
        level_04_Cor(screen, screen_config, clock)
    ]

    # for i in range(1, len(levels)):
    #     level = levels[i-1]
        # level.add_caption(create_caption("Level " + str(i).zfill(2), 5, 5, color_fg=(170, 170, 170)))

    menu_title(screen, screen_config, clock)

    done = False
    i = 0
    while i < len(levels) and not done:
        gameplay_level = GameplayLevel(levels[i])
        gameplay_level.play()
        i = i + 1


if __name__ == "__main__":
    main()
