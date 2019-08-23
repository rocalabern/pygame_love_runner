def read_level(str_file):
    with open(str_file) as f:
        line_list = f.readlines()

    line_list = [line.rstrip('\n') for line in open(str_file)]
    return line_list


class Level:

    LEVEL_FILE = None
    level = None

    VELOCITY_MOVEMENT = 4
    VELOCITY_JUMP = 4
    VELOCITY_MAX_FALL = 15

    TILE = 32
    TILE_X = TILE
    TILE_Y = TILE
    TILE_X_NUM = 0
    TILE_Y_NUM = 0

    def __init__(self, level_file):
        self.LEVEL_FILE = level_file
        self.level = read_level(self.LEVEL_FILE)
        self.TILE_Y_NUM = self.level.__len__()
        self.TILE_X_NUM = self.level[0].__len__()

    def __init__(self, level_file, tile):
        self.LEVEL_FILE = level_file
        self.level = read_level(self.LEVEL_FILE)
        self.set_tile(tile)
        self.TILE_Y_NUM = self.level.__len__()
        self.TILE_X_NUM = self.level[0].__len__()

    def set_tile(self, tile):
        self.TILE = tile
        self.TILE_X = self.TILE
        self.TILE_Y = self.TILE
        self.TILE_X_NUM = 1312 // self.TILE_X
        self.TILE_Y_NUM = 704 // self.TILE_Y

    def get_level(self):
        return self.level


