from lib import *
from . import *


class DictionaryLevels:

    num_level = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_level(self, name):
        if name is None:
            raise Exception('Level chosen is None')

        elif name == "test_00":
            level = Level("levels/test_levels/test_00.txt", 60)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            return level
        elif name == "test_01":
            level = Level("levels/test_levels/test_01.txt", 32)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            return level
        elif name == "test_02":
            level = Level("levels/test_levels/test_02.txt", 16)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            return level

        elif name == "tutorial_00":
            level = Level("levels/tutorial_levels/tutorial_00.txt", 60)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            level.add_caption(create_caption("Movement Tutorial", self.width//2-400, 5))
            return level

        elif name == "level_00":
            level = Level("levels/game_levels/level_00.txt", 16)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            return level
        elif name == "level_01_Patri":
            level = Level("levels/game_levels/level_01_Patri.txt", 16)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            return level
        elif name == "level_02_Dani":
            level = Level("levels/game_levels/level_02_Dani.txt", 16)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            return level
        elif name == "level_03_Cor":
            level = Level("levels/game_levels/level_03_Cor.txt", 16)
            level.add_caption(create_caption("Level " + str(self.num_level).zfill(2), 5, 5, color_fg=(170, 170, 170)))
            self.num_level = self.num_level + 1
            return level

        else:
            raise Exception('Level ' + name + ' not configured yet in dict_levels.py')
