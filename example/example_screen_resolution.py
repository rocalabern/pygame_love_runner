"""
http://stackoverflow.com/a/15459868/190597 (unutbu)
Based on http://www.pygame.org/docs/tut/intro/intro.html
Draws a red ball bouncing around in the window.
Pressing the arrow keys moves the ball
"""

import sys
import pygame
import os


image_file = os.path.expanduser('../images/titles/LodeRunner_ball_25px.png')

delta = {
    pygame.K_LEFT: (-8, 0),
    pygame.K_RIGHT: (+8, 0),
    pygame.K_UP: (0, -8),
    pygame.K_DOWN: (0, +8),
    }

gravity = +0.5


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_game_rect: pygame.Rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.speed = [0, 0]
        self.width, self.height = screen_game_rect.width, screen_game_rect.height

    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.height:
            self.speed[1] = -self.speed[1]
        if self.rect.bottom > self.height and abs(self.speed[1]) < 2.5:
            self.speed[1] = 0
        self.rect.left = clip(self.rect.left, 0, self.width)
        self.rect.right = clip(self.rect.right, 0, self.width)
        self.rect.top = clip(self.rect.top, 0, self.height)
        self.rect.bottom = clip(self.rect.bottom, 0, self.height)


def clip(val, minval, maxval):
    return min(max(val, minval), maxval)


class Main(object):
    def __init__(self, width: int, height: int):
        pygame.init()

        # self.screen_desktop = pygame.display.set_mode((1280, 720), 0, 32)
        # self.screen_desktop = pygame.display.set_mode((640, 360), 0, 32)
        # self.screen_desktop = pygame.display.set_mode((320, 180), 0, 32)
        self.screen_desktop = pygame.display.set_mode((width, height), 0, 32)
        self.screen_desktop_rect = self.screen_desktop.get_rect()

        self.screen_game = pygame.Surface((640, 360))
        self.screen_game_rect = self.screen_game.get_rect()
        self.width = self.screen_game_rect.width
        self.height = self.screen_game_rect.height

        self.ratio_x = (self.screen_desktop_rect.width / self.screen_game_rect.width)
        self.ratio_y = (self.screen_desktop_rect.height / self.screen_game_rect.height)

        self.ball = Ball(self.screen_game_rect)

        self.background = pygame.Surface(self.screen_game.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.screen_game.blit(self.background, (0, 0))
        pygame.display.flip()

    def draw(self):
        self.screen_game.blit(self.background, (0, 0))
        self.screen_game.blit(self.ball.image, self.ball.rect)
        pygame.display.flip()

    def event_loop(self):
        ball = self.ball
        friction = 0.99
        while True:
            for event in pygame.event.get():
                if ((event.type == pygame.QUIT) or
                    (event.type == pygame.KEYDOWN and
                     event.key == pygame.K_ESCAPE)):
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    deltax, deltay = delta.get(event.key, (0, 0))
                    ball.speed[0] += deltax
                    ball.speed[1] += deltay

            ball.speed = [friction*s for s in ball.speed]
            ball.speed[1] += gravity
            ball.update()

            scaled_screen = pygame.transform.scale(self.screen_game, self.screen_desktop_rect.size)
            self.screen_desktop.blit(scaled_screen, (0, 0))
            self.draw()
            pygame.time.delay(15)


if __name__ == '__main__':
    # app = Main(1280, 720)
    # app.event_loop()

    app = Main(640, 360)
    app.event_loop()

    # app = Main(320, 180)
    # app.event_loop()
