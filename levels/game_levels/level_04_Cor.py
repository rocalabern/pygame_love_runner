import pygame
from pygame import *

from lib import *
from levels import *


def prepare_background(level, width, height):
    image_file = "images/wedding/bg/background_level_cor.png"
    image_background = pygame.image.load(image_file)
    image_background = pygame.transform.scale(image_background, (width, int(0.5 * height)))
    # image_background = pygame.transform.scale(image_background, (int(round(0.5*width)), int(round(0.5*height))))
    # image_background_pos_x = int(round(width*0.25))
    image_background_pos_x = 10
    image_background_pos_y = 10
    level.image_background = image_background
    level.image_background_pos_x = image_background_pos_x
    level.image_background_pos_y = image_background_pos_y


def show_background(level, screen, width, height):
    screen.blit(level.image_background, (level.image_background_pos_x, level.image_background_pos_y))


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
    level.prepare_background = prepare_background
    level.print_background = show_background
    level.success_animation = show_image
    return level



