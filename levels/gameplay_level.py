import pygame
from pygame import *

from lib import *
from entities import *


def get_background_tile(tile_x, tile_y):
    bg = Surface((tile_x, tile_y))
    bg.convert()
    bg.fill(Color(constants.COLOR_BCKGRND_BOLD))
    bg.fill(Color(constants.COLOR_BCKGRND), Rect(2, 2, tile_x-2, tile_y-2))
    return bg


def load_level(level):
    constants.VELOCITY_MOVEMENT = level.VELOCITY_MOVEMENT
    constants.VELOCITY_JUMP = level.VELOCITY_JUMP
    constants.VELOCITY_MAX_FALL = level.VELOCITY_MAX_FALL
    constants.TILE_X = level.TILE_X
    constants.TILE_Y = level.TILE_Y
    constants.TILE_X_NUM = level.TILE_X_NUM
    constants.TILE_Y_NUM = level.TILE_Y_NUM

    entities = pygame.sprite.Group()
    platforms = []

    # build the level
    x = y = 0
    for level_row in level.get_level():
        for level_block in level_row:
            if level_block == "P":
                e = PlatformBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if level_block == "E":
                e = StairsBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if level_block == "B":
                e = BarBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if level_block == "G":
                e = GoalBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if level_block == "Y":
                player_p1 = Player(x, y, constants.COLOR_PLAYER_P2, constants.IMAGE_X, flip=True)
            if level_block == "X":
                player_p2 = Player(x, y, constants.COLOR_PLAYER_P1, constants.IMAGE_Y, flip=True)
            x += constants.TILE_X
        y += constants.TILE_Y
        x = 0
    platforms.append(player_p1)
    entities.add(player_p1)
    entities.add(player_p2)
    platforms.append(player_p2)
    return (entities, platforms, player_p1, player_p2)


class GameplayLevel:

    def __init__(self, level):
        self.level = level

    def play(self, screen, clock):
        (entities, platforms, player_p1, player_p2) = load_level(self.level)

        bg = get_background_tile(constants.TILE_X, constants.TILE_Y)

        up_p1 = down_p1 = left_p1 = right_p1 = False
        up_p2 = down_p2 = left_p2 = right_p2 = False

        done = False
        skip = False
        while not done:

            e: event
            for e in pygame.event.get():
                if e.type == QUIT:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    raise SystemExit("ESCAPE")
                if e.type == KEYDOWN and e.key == K_F2:
                    done = True
                if e.type == KEYDOWN and e.key == K_F3:
                    done = True
                    skip = True

                if e.type == KEYDOWN or e.type == KEYUP:

                    if e.key == K_UP:
                        up_p1 = e.type == KEYDOWN
                    if e.key == K_DOWN:
                        down_p1 = e.type == KEYDOWN
                    if e.key == K_LEFT:
                        left_p1 = e.type == KEYDOWN
                    if e.key == K_RIGHT:
                        right_p1 = e.type == KEYDOWN

                    if e.key == K_w:
                        up_p2 = e.type == KEYDOWN
                    if e.key == K_s:
                        down_p2 = e.type == KEYDOWN
                    if e.key == K_a:
                        left_p2 = e.type == KEYDOWN
                    if e.key == K_d:
                        right_p2 = e.type == KEYDOWN

            # update player, draw everything else
            player_p1.update(up_p1, down_p1, left_p1, right_p1, platforms)
            player_p2.update(up_p2, down_p2, left_p2, right_p2, platforms)
            if player_p1.on_goal and player_p2.on_goal:
                done = True

            # draw background
            for y in range(constants.TILE_Y_NUM):
                for x in range(constants.TILE_X_NUM):
                    screen.blit(bg, (x * constants.TILE_X, y * constants.TILE_Y))
            # image_file = "images/sprites/background/blue_land.png"
            # temp = pygame.image.load(image_file)
            # temp = pygame.transform.scale(temp, (constants.WIN_WIDTH, constants.WIN_HEIGHT))
            # screen.blit(temp, (0, 0))
            entities.draw(screen)

            if self.level.captions is not None:
                for caption in self.level.captions:
                    caption(screen)

            pygame.display.update()
            clock.tick(60)

        print("Level finished")
        if not skip:
            print("Level finished : not skipped")
            pygame.time.wait(1000)
            if self.level.end_level is not None:
                print("Level finished : Doing final animation")
                self.level.end_level(screen, constants.WIN_WIDTH, constants.WIN_HEIGHT)
                pygame.display.update()
                pygame.time.wait(2000)
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == KEYDOWN:
                            return
                    clock.tick(60)
