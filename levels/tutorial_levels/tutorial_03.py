import pygame
from pygame import *

from game_screen.game_screen import GameScreen
from lib import *
from levels import *


def show_image(screen, screen_config, width, height):
    # screen.fill(Color("#FFFFFF"))
    screen.fill(Color("#000000"))

    diff = 0.4
    temp = rescale_image_height_pixels(
        "images/wedding/rewards/end_level_animation_tutorial_01.png",
        height,
        margin=diff
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

    temp = rescale_image_height_pixels(
        "images/wedding/carlos_ruiz_pozo/carlos_ruiz_pozo_01.png",
        height,
        margin=0.3
    )
    screen.blit(
        temp,
        (
            screen_config.x_offset+width-temp.get_rect().size[0],
            screen_config.y_offset+height-temp.get_rect().size[1]
        )
    )

    pg_print_message(screen, screen_config, "Primera barra conseguida!", int(round(1366 / 5)), int(round(768 / 6)), size=64)

    pygame.display.update()
    pygame.time.wait(5000)


def tutorial_03(
        game_screen: GameScreen
):
    level = Level(
        "levels/tutorial_levels/tutorial_03.txt",
        game_screen
    )
    level.add_caption(create_caption("La cita! dos mitades de un corazón", 176, 120))
    level.add_caption(create_caption("PISTA: Debéis reuniros", 176, 600, color_fg=(150, 150, 150)))

    level.success_animation = show_image
    level.offset_width = 10
    return level



