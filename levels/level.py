
def read_level(str_file):
    with open(str_file) as f:
        line_list = f.readlines()

    line_list = [line.rstrip('\n') for line in open(str_file)]
    return line_list


class Level:

    def __init__(self, level_file, tile_x, tile_y: int = None):
        self.LEVEL_FILE = level_file
        self.level = read_level(self.LEVEL_FILE)
        self.TILE_X = tile_x
        if tile_y is None:
            self.TILE_Y = tile_x
        else:
            self.TILE_Y = tile_y
        self.TILE_Y_NUM = self.level.__len__()
        self.TILE_X_NUM = self.level[0].__len__()
        self.VELOCITY_MOVEMENT = 4
        self.VELOCITY_JUMP = 4
        self.VELOCITY_MAX_FALL = 15
        self.captions = None

    def get_level(self):
        return self.level

    def add_caption(self, caption):
        if self.captions is None:
            self.captions = [caption]
        else:
            self.captions.append(caption)