import pygame
from pygame import *

from lib import *
from levels import *


def show_image(screen, width, height):
    # screen.fill(Color("#FFFFFF"))
    screen.fill(Color("#000000"))

    diff = 0.4
    temp = rescale_image_height(
        "images/wedding/rewards/end_level_animation_tutorial_09.png",
        height,
        diff=diff
    )
    pygame.draw.rect(screen, Color("#FFFFFF"), (int(round(0.50 * width - temp.get_rect().size[0]/2)), int(round(diff * height-(diff*height)/4)), temp.get_rect().size[0], temp.get_rect().size[1]))
    screen.blit(temp, (int(round(0.50 * width - temp.get_rect().size[0]/2)), int(round(diff * height-(diff*height)/4))))

    temp = rescale_image_height(
        "images/wedding/carlos_ruiz_pozo/carlos_ruiz_pozo_09.png",
        height,
        diff=0.3
    )
    screen.blit(
        temp,
        (
            width-temp.get_rect().size[0],
            height-temp.get_rect().size[1]
        )
    )

    pygame.display.update()
    pygame.time.wait(5000)


def tutorial_11():
    level = Level("levels/tutorial_levels/tutorial_11.txt", 64, velocity_jump=6)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.success_animation = show_image
    level.player_force_background = True
    level.offset_width = 10
    return level



