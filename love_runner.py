import pygame
from pygame import *

from lib import *
from entities import constants
from levels import GameplayLevel
from levels.tutorial_levels import *
from levels.game_levels import *
from levels.test_levels import *

def main():
    pygame.mixer.pre_init(48000, -16, 2, 2048)
    pygame.init()
    screen = pygame.display.set_mode((constants.WIN_WIDTH, constants.WIN_HEIGHT))
    pygame.display.set_caption("Love Runner")
    clock = pygame.time.Clock()

    levels = [
        tutorial_01(),
        tutorial_02(),
        tutorial_03(),
        tutorial_04(),
        level_02_Patri(),
        level_03_Dani(),
        level_01()
    ]

    for i in range(1, len(levels)):
        level = levels[i-1]
        level.add_caption(create_caption("Level " + str(i).zfill(2), 5, 5, color_fg=(170, 170, 170)))

    done = False
    i = 0
    while i < len(levels) and not done:
        gameplay_level = GameplayLevel(levels[i])
        gameplay_level.play(screen, clock)
        i = i + 1


if __name__ == "__main__":
    main()
