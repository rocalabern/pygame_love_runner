

class ScreenConfig:

    def __init__(self, info_display, aspect_ratio=16/9, debug=True):
        self.aspect_ratio = aspect_ratio
        self.info_display = info_display
        if self.aspect_ratio * self.info_display.current_h < self.info_display.current_w:
            self.w = int(round(self.aspect_ratio * self.info_display.current_h))
            self.h = int(round(self.info_display.current_h))
            self.x_offset = int((self.info_display.current_w - self.w) / 2)
            self.y_offset = 0
            if debug:
                print("Max axis : height")
        else:
            self.w = int(round(self.info_display.current_w))
            self.h = int(round(self.info_display.current_w / self.aspect_ratio))
            self.x_offset = 0
            self.y_offset = int((self.info_display.current_h - self.h) / 2)
            if debug:
                print("Max axis : with")
        if debug:
            print("aspect_ratio : " + str(self.aspect_ratio))
            print("screen : " + str(self.w) + " x " + str(self.h))
            print("offset : " + str(self.x_offset) + " , " + str(self.y_offset))

    def position(self, x=0.5, y=0.5):
        factor_x = x * self.w
        factor_y = y * self.h
        pos_x = int(round(self.x_offset + factor_x))
        pos_y = int(round(self.y_offset + factor_y))
        return pos_x, pos_y

