import pygame
from pygame import *

from lib import *
from levels import *


def show_image(screen, width, height):
    image_file = "images/thumbs-up/hugo_muy_bien.jpg"
    temp = pygame.image.load(image_file)
    temp = pygame.transform.scale(temp, (width, height))
    screen.blit(temp, (0, 0))
    pg_print_message(screen, "MUY BIEN", int(round(width / 4)), int(round(height / 4)), size=128)
    pygame.display.update()
    pygame.time.wait(5000)


def level_04_Cor():
    level = Level("levels/game_levels/level_04_Cor.txt", 16)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.success_animation = show_image
    return level



