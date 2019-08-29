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

        self.image_background = None
        self.image_background_pos_x = None
        self.image_background_pos_y = None

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
