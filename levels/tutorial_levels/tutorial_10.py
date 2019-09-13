import pygame
from pygame import *

from lib import *
from levels import *


def show_image(screen, screen_config, width, height):
    # screen.fill(Color("#FFFFFF"))
    screen.fill(Color("#000000"))

    diff = 0.4
    temp = rescale_image_height(
        "images/wedding/rewards/end_level_animation_tutorial_08.png",
        height,
        diff=diff
    )
    pygame.draw.rect(
        screen,
        Color("#FFFFFF"),
        (
            screen_config.x_offset+int(round(0.50 * width - temp.get_rect().size[0]/2)),
            screen_config.y_offset+int(round(diff * height-(diff*height)/4)),
            temp.get_rect().size[0],
            temp.get_rect().size[1]
        )
    )
    screen.blit(
        temp,
        (
            screen_config.x_offset+int(round(0.50 * width - temp.get_rect().size[0]/2)),
            screen_config.y_offset+int(round(diff * height-(diff*height)/4))
        )
    )

    temp = rescale_image_height(
        "images/wedding/carlos_ruiz_pozo/carlos_ruiz_pozo_08.png",
        height,
        diff=0.3
    )
    screen.blit(
        temp,
        (
            screen_config.x_offset+width-temp.get_rect().size[0],
            screen_config.y_offset+height-temp.get_rect().size[1]
        )
    )

    pg_print_message(screen, screen_config, "Hay más refranes que...", int(round(1366 / 5)), int(round(768 / 6)), size=64)

    pygame.display.update()
    pygame.time.wait(5000)


def tutorial_10(
        screen: pygame.Surface,
        screen_config: ScreenConfig,
        clock: pygame.time
):
    level = Level(
        "levels/tutorial_levels/tutorial_10.txt",
        screen,
        screen_config,
        clock,
        velocity_jump=6
    )
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.success_animation = show_image
    level.player_force_background = True
    level.offset_width = 10
    return level



