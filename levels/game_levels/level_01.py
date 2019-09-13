import pygame
from pygame import *

from lib import *
from levels import *


def show_image(screen, screen_config, width, height):
    image_file = "images/thumbs-up/julia_y_mar_muy_bien.png"
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    diff = 0.0
    factor = (1.0-diff) * (height / y)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    screen.blit(temp, (screen_config.x_offset+int(round(0.20*width)), screen_config.y_offset+int(round(diff*height))))

    pg_print_message(screen, screen_config, "MUY BIEN", int(round(1366 / 4)), int(round(768 / 4)), size=128)

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
        clock,
        velocity_jump=6
    )
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.success_animation = show_image
    return level



