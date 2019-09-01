import pygame
from pygame import *

from lib import *
from levels import *


def show_image(screen, width, height):
    image_file = "images/wedding/rewards/end_level_animation_tutorial_01.png"
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    diff = 0.4
    factor = (1.0-diff) * (height / y)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))

    # screen.fill(Color("#FFFFFF"))
    screen.fill(Color("#000000"))
    pygame.draw.rect(screen, Color("#FFFFFF"), (int(round(0.50 * width - temp.get_rect().size[0]/2)), int(round(diff * height-(diff*height)/4)), temp.get_rect().size[0], temp.get_rect().size[1]))
    screen.blit(temp, (int(round(0.50 * width - temp.get_rect().size[0]/2)), int(round(diff * height-(diff*height)/4))))

    pg_print_message(screen, "Primera barra conseguida!", int(round(width / 5)), int(round(height / 6)), size=64)

    pygame.display.update()
    pygame.time.wait(5000)


def tutorial_03():
    level = Level("levels/tutorial_levels/tutorial_03.txt", 64, velocity_jump=6)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.success_animation = show_image
    level.offset_width = 10
    return level



