import pygame
from pygame import *

from lib import *
from levels import *


def show_background(screen, width, height):
    image_background = None
    # image_file = "images/sprites/background/blue_land.png"
    image_file = "images/wedding/level_Patri/background_level_patri_03.png"
    image_background = pygame.image.load(image_file)
    image_background = pygame.transform.scale(image_background, (width, int(0.5*height)))
    # image_background = pygame.transform.scale(image_background, (int(round(0.5*width)), int(round(0.5*height))))
    # image_background_pos_x = int(round(width*0.25))
    image_background_pos_x = 10
    image_background_pos_y = 10
    screen.blit(image_background, (image_background_pos_x, image_background_pos_y))


def show_image(screen, width, height):
    image_file = "images/thumbs-up/hugo_muy_bien.jpg"
    temp = pygame.image.load(image_file)
    temp = pygame.transform.scale(temp, (width, height))
    screen.blit(temp, (0, 0))
    pg_print_message(screen, "MUY BIEN", int(round(width / 4)), int(round(height / 4)), size=128)
    pygame.display.update()
    pygame.time.wait(5000)


def level_02_Patri():
    level = Level("levels/game_levels/level_02_Patri.txt", 16)
    # level.add_caption(create_caption("Movement Tutorial", level.width//2-400, 5))
    level.print_background = show_background
    level.success_animation = show_image
    return level



