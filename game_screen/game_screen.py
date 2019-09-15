import pygame


class GameScreen:
    def __init__(self, screen_desktop: pygame.Surface, game_w: int = 1280, game_h: int = 720, debug=True):
        self.screen_desktop = screen_desktop
        # self.info_display = pygame.display.Info()
        # self.desktop_w = self.info_display.current_w
        # self.desktop_h = self.info_display.current_h
        self.screen_desktop_rect = self.screen_desktop.get_rect()
        self.desktop_w = self.screen_desktop_rect.width
        self.desktop_h = self.screen_desktop_rect.height

        self.game_aspect_ratio = game_w / game_h

        if self.game_aspect_ratio < self.desktop_w / self.desktop_h:
            self.w = int(round(self.game_aspect_ratio * self.desktop_h))
            self.h = int(round(self.window_h))
            self.x_offset = int((self.desktop_w - self.w) / 2)
            self.y_offset = 0
            if debug:
                print("Max axis : height")
        else:
            self.w = int(round(self.desktop_w))
            self.h = int(round(self.desktop_w / self.game_aspect_ratio))
            self.x_offset = 0
            self.y_offset = int((self.desktop_h - self.h) / 2)
            if debug:
                print("Max axis : with")
        if debug:
            print("aspect_ratio : " + str(self.game_aspect_ratio))
            print("screen : " + str(self.w) + " x " + str(self.h))
            print("offset : " + str(self.x_offset) + " , " + str(self.y_offset))

        self.screen_game = pygame.Surface((game_w, game_h))
        self.screen_game_rect = self.screen_game.get_rect()
        self.game_w = game_w
        self.game_h = game_h

        self.ratio_x = (self.screen_desktop_rect.width / self.screen_game_rect.width)
        self.ratio_y = (self.screen_desktop_rect.height / self.screen_game_rect.height)

    def position_desktop(self, x=0.5, y=0.5):
        factor_x = x * self.w
        factor_y = y * self.h
        pos_x = int(round(self.x_offset + factor_x))
        pos_y = int(round(self.y_offset + factor_y))
        return pos_x, pos_y

    def update(self):
        scaled_screen = pygame.transform.scale(self.screen_game, self.screen_desktop_rect.size)
        self.screen_desktop.blit(scaled_screen, (0, 0))
        pygame.display.update()
