import pygame
from pygame import *

from lib import *
from levels import *


def show_image(screen, width, height):
    image_file = "images/thumbs-up/julia_muy_bien_01.png"
    temp = pygame.image.load(image_file)
    temp = pygame.transform.scale(temp, (width, height))
    screen.blit(temp, (0, 0))

    pg_print_message(screen, "MUY BIEN", int(round(1366 / 4)), int(round(768 / 4)), size=128)

    pygame.display.update()
    pygame.time.wait(5000)


def level_01(
        screen: pygame.Surface,
        screen_config: ScreenConfig,
        clock: pygame.time
):
    level = Level(
        "levels/game_levels/level_01.txt",
        screen,
        screen_config,
        clock
    )
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.success_animation = show_image
    return level



