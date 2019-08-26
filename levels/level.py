import pygame
from lib import *


def read_level(str_file):
    with open(str_file) as f:
        line_list = f.readlines()

    line_list = [line.rstrip('\n') for line in open(str_file)]
    return line_list


class Level:

    def __init__(
            self,
            level_file,
            tile_x,
            tile_y: int = None,
            width=1312,
            height=704,
            velocity_movement=4,
            velocity_jump=4,
            num_players=0
    ):
        self.LEVEL_FILE = level_file
        self.level = read_level(self.LEVEL_FILE)
        self.width = width
        self.height = height
        self.TILE_X = tile_x
        if tile_y is None:
            self.TILE_Y = tile_x
        else:
            self.TILE_Y = tile_y
        self.TILE_Y_NUM = self.level.__len__()
        self.TILE_X_NUM = self.level[0].__len__()
        self.VELOCITY_MOVEMENT = velocity_movement
        self.VELOCITY_JUMP = velocity_jump
        self.VELOCITY_MAX_FALL = 15
        self.captions = None
        self.end_level = None
        self.num_players = num_players

    def get_level(self):
        return self.level

    def add_caption(self, caption):
        if self.captions is None:
            self.captions = [caption]
        else:
            self.captions.append(caption)

    def set_end_level(self, end_level=None):
        def show_image(screen, width, height):
            # image_file = "images/face_mar.png"
            image_file = "images/julia_muy_bien.png"
            temp = pygame.image.load(image_file)
            temp = pygame.transform.scale(temp, (width, height))
            screen.blit(temp, (0, 0))
            pg_print_message(screen, "MUY BIEN", int(round(width/4)), int(round(height/4)), size=128)
        self.end_level = show_image
