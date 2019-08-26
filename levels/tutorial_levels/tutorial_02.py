import pygame
from pygame import *

from lib import *
from levels import *


def set_end_level(level):
    def show_image(screen, width, height):
        # image_file = "images/face_mar.png"
        image_file = "images/julia_muy_bien.png"
        temp = pygame.image.load(image_file)
        temp = pygame.transform.scale(temp, (width, height))
        screen.blit(temp, (0, 0))
        pg_print_message(screen, "MUY BIEN", int(round(width / 4)), int(round(height / 4)), size=128)

    level.end_level = show_image


def tutorial_02():
    level = Level("levels/tutorial_levels/tutorial_02.txt", 60, velocity_jump=6)
    level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    set_end_level(level)
    return level



