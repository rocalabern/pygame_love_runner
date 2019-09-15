import pygame

from game_screen.game_screen import GameScreen
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
            game_screen: GameScreen,
            velocity_movement=6,
            velocity_jump=5.5,
            velocity_max_fall=30,
            num_players=0
    ):
        self.game_screen = game_screen
        self.clock = pygame.time.Clock()

        self.LEVEL_FILE = level_file
        self.level = read_level(self.LEVEL_FILE)
        self.TILE_Y_NUM = self.level.__len__()
        self.TILE_X_NUM = self.level[0].__len__()

        self.tile_x = int(game_screen.w / self.TILE_X_NUM)
        self.tile_y = int(game_screen.h / self.TILE_Y_NUM)

        self.VELOCITY_MOVEMENT = int(round(velocity_movement*(self.tile_y/40)))
        self.VELOCITY_JUMP = int(round(velocity_jump*(self.tile_y/40)))
        self.VELOCITY_MAX_FALL = int(round(velocity_max_fall*(self.tile_y/40)))

        self.prepare_background = None
        self.print_background = None
        self.captions = None
        self.success_animation = None

        self.num_players = num_players
        self.player_force_background = False

    def get_level(self):
        return self.level

    def add_caption(self, caption):
        if self.captions is None:
            self.captions = [caption]
        else:
            self.captions.append(caption)
