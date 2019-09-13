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
            screen: pygame.Surface,
            screen_config: ScreenConfig,
            clock: pygame.time,
            velocity_movement=4,
            velocity_jump=4,
            velocity_max_fall=15,
            num_players=0
    ):
        self.screen = screen
        self.screen_config = screen_config
        self.clock = clock

        self.LEVEL_FILE = level_file
        self.level = read_level(self.LEVEL_FILE)
        self.TILE_Y_NUM = self.level.__len__()
        self.TILE_X_NUM = self.level[0].__len__()

        self.VELOCITY_MOVEMENT = int(round(velocity_movement*(screen_config.w / 1366)))
        self.VELOCITY_JUMP = int(round(velocity_jump*(screen_config.w / 1366)))
        self.VELOCITY_MAX_FALL = int(round(velocity_max_fall*(screen_config.w / 1366)))

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
