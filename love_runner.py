import pygame
from pygame import *

from lib import *
from entities import constants
from levels import GameplayLevel
from levels import DictionaryLevels


def main():
    pygame.mixer.pre_init(48000, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((constants.WIN_WIDTH, constants.WIN_HEIGHT))
    pygame.display.set_caption("Love Runner")
    clock = pygame.time.Clock()

    dict_levels = DictionaryLevels(constants.WIN_WIDTH, constants.WIN_HEIGHT)
    levels = [
        dict_levels.get_level("tutorial_00"),
        dict_levels.get_level("level_01_Patri"),
        dict_levels.get_level("level_02_Dani"),
        dict_levels.get_level("level_00")
    ]

    # levels = [
    #     dict_levels.get_level("test_00"),
    #     dict_levels.get_level("test_01"),
    #     dict_levels.get_level("test_02")
    # ]
    #
    # levels = [
    #     dict_levels.get_level("level_01_Patri")
    # ]

    done = False
    i = 0
    while i < len(levels) and not done:
        gameplay_level = GameplayLevel(levels[i])
        gameplay_level.play(screen, clock)
        i = i + 1


if __name__ == "__main__":
    main()
