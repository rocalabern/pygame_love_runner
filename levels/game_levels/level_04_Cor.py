import pygame
from pygame import *

from lib import *
from levels import *


def prepare_background(level, width, height):
    image_file = "images/wedding/bg/background_level_cor.png"
    image_background = pygame.image.load(image_file)
    x = image_background.get_rect().size[0]
    y = image_background.get_rect().size[1]
    diff = 0.05
    factor = (1.0-diff) * (width / x)
    image_background = pygame.transform.scale(image_background, (int(round(factor * x)), int(round(factor * y))))

    image_background_pos_x = 10+int(round((width-image_background.get_rect().size[0])/2))
    image_background_pos_y = 70
    level.image_background = image_background
    level.image_background_pos_x = image_background_pos_x
    level.image_background_pos_y = image_background_pos_y


def show_background(level, screen, width, height):
    screen.blit(level.image_background, (level.image_background_pos_x, level.image_background_pos_y))


def show_image(screen, width, height):
    image_file = "images/thumbs-up/noemi_y_roc_muy_bien.png"
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    diff = 0.0
    # factor = (1.0 - diff) * (height / y)
    factor = (1.0 - diff) * (width / x)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    y = temp.get_rect().size[1]
    screen.blit(temp, (int(round(0.0*width)), height-y))

    pg_print_message(
        screen,
        "Y finalmente, para nuestras lágrimas de alegría",
         int(round(width / 14))-20,
         int(round(1 * height / 12))-40,
         size=64
    )
    pg_print_message(
        screen,
        "por compartir este momento especial",
         int(round(width / 14))-20,
         int(round(2 * height / 12))-40,
         size=64
    )
    pg_print_message(
        screen,
        "en vuestras vidas.",
         int(round(width / 14))-20,
         int(round(3 * height / 12)-40),
         size=64
    )
    pg_print_message(
        screen,
        "¡¡¡Vivan las novios!!!",
         int(round(width / 14))+80,
         int(round(10 * height / 12)-40),
         size=128
    )

    pygame.display.update()
    pygame.time.wait(5000)


def level_04_Cor():
    level = Level("levels/game_levels/level_04_Cor.txt", 16)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.prepare_background = prepare_background
    level.print_background = show_background
    level.success_animation = show_image
    level.offset_width = 2
    return level



