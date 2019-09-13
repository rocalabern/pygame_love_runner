import pygame
from pygame import *

from lib import *
from levels import *


def prepare_background(level, width, height):
    image_file = "images/wedding/bg/background_level_patri.png"
    image_background = pygame.image.load(image_file)
    x = image_background.get_rect().size[0]
    y = image_background.get_rect().size[1]
    diff = 0.05
    factor = (1.0-diff) * (width / x)
    image_background = pygame.transform.scale(image_background, (int(round(factor * x)), int(round(factor * y))))

    image_background_pos_x = 10+int(round((width-image_background.get_rect().size[0])/2))
    image_background_pos_y = 100
    level.image_background = image_background
    level.image_background_pos_x = image_background_pos_x
    level.image_background_pos_y = image_background_pos_y


def show_background(level, screen, width, height):
    screen.blit(level.image_background, (level.image_background_pos_x, level.image_background_pos_y))


def show_image(screen, screen_config, width, height):
    image_file = "images/thumbs-up/carlos_y_tamara_muy_bien.png"
    temp = pygame.image.load(image_file)
    x = temp.get_rect().size[0]
    y = temp.get_rect().size[1]
    diff = 0.0
    factor = (1.0-diff) * (height / y)
    temp = pygame.transform.scale(temp, (int(round(factor * x)), int(round(factor * y))))
    screen.blit(temp, (int(round(0.0*width)), int(round(diff*height))))

    pg_print_message(screen, screen_config, "Un ramo de flores como", 20+int(round(1366 / 5)), int(round(3 * 768 / 4)), size=64)
    pg_print_message(screen, screen_config, "símbolo de nuestro afecto.", 20+int(round(1366 / 5)), int(round(5 * 768 / 6)), size=64)

    pygame.display.update()
    pygame.time.wait(5000)


def level_02_Patri(
        screen: pygame.Surface,
        screen_config: ScreenConfig,
        clock: pygame.time
):
    level = Level(
        "levels/game_levels/level_02_Patri.txt",
        screen,
        screen_config,
        clock
    )
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.prepare_background = prepare_background
    level.print_background = show_background
    level.success_animation = show_image
    return level



