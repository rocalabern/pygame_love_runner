import sys
import mutagen.mp3
import pygame
from pygame import *

from lib import *
from entities import *


def get_background_tile_simple(tile_x, tile_y):
    bg = Surface((tile_x, tile_y))
    bg.convert()

    bg.fill(Color(constants.COLOR_BCKGRND_BOLD))
    bg.fill(Color("#ffe6e6"))
    bg.fill(Color("#ffffff"), Rect(2, 2, tile_x-2, tile_y-2))

    return bg


def get_background_tile(tile_x, tile_y):
    # bessel_perc = 16
    # # color_dark = "#330033"
    # # color_light = "#990099"
    # # color_main = "#4d004d"
    # color_dark = "#1a1a1a"
    # color_light = "#404040"
    # color_main = "#595959"
    #
    # temp = create_block_bessel(
    #     constants.TILE_X,
    #     constants.TILE_Y,
    #     color_light, color_dark, color_main,
    #     bessel_perc)

    temp = Surface((tile_x, tile_y))
    temp.convert()
    temp.fill(Color(constants.COLOR_BAR_BCKGRND))

    return temp


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
    player_p1 = Player(0, 0, "dummy")
    player_p2 = Player(0, 0, "dummy")
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
            if level_block == "L":
                e = GoalBlockLeft(x, y)
                platforms.append(e)
                entities.add(e)
            if level_block == "R":
                e = GoalBlockRight(x, y)
                platforms.append(e)
                entities.add(e)
            if level_block == "Y":
                player_p1 = Player(
                    x, y, "Y",
                    constants.COLOR_PLAYER_P2, constants.IMAGE_X,
                    flip=True, force_background=level.player_force_background)
                level.num_players = level.num_players + 1
            if level_block == "X":
                player_p2 = Player(
                    x, y, "X",
                    constants.COLOR_PLAYER_P1, constants.IMAGE_Y,
                    flip=True, force_background=level.player_force_background)
                level.num_players = level.num_players + 1
            x += constants.TILE_X
        y += constants.TILE_Y
        x = 0
    if player_p1.name is not "Dummy":
        platforms.append(player_p1)
        entities.add(player_p1)
    if player_p2.name is not "Dummy":
        entities.add(player_p2)
        platforms.append(player_p2)
    return (entities, platforms, player_p1, player_p2)


class GameplayLevel:

    def __init__(self, level):
        self.level = level

    def play(self, screen, clock):
        (entities, platforms, player_p1, player_p2) = load_level(self.level)

        music_file = 'music/8-bit-mario-theme.mp3'
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)

        bg = get_background_tile(constants.TILE_X, constants.TILE_Y)
        if self.level.prepare_background is not None:
            self.level.prepare_background(self.level, constants.WIN_WIDTH, constants.WIN_HEIGHT)

        up_p1 = down_p1 = left_p1 = right_p1 = False
        up_p2 = down_p2 = left_p2 = right_p2 = False

        done = False
        skip = False
        while not done:

            # e: event
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
            if self.level.num_players == 1:
                if player_p1.on_goal or player_p2.on_goal:
                    done = True
                    for p in platforms:
                        if isinstance(p, GoalBlockLeft) or isinstance(p, GoalBlockRight):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_full)
                else:
                    for p in platforms:
                        if isinstance(p, GoalBlockLeft) or isinstance(p, GoalBlockRight):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_empty)

            else:
                if player_p1.on_goal and player_p2.on_goal:
                    done = True
                    for p in platforms:
                        if isinstance(p, GoalBlockLeft) or isinstance(p, GoalBlockRight):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_full)
                elif player_p1.on_goal and not player_p2.on_goal:
                    for p in platforms:
                        if isinstance(p, GoalBlockLeft):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_empty)
                        if isinstance(p, GoalBlockRight):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_full)
                elif not player_p1.on_goal and player_p2.on_goal:
                    for p in platforms:
                        if isinstance(p, GoalBlockLeft):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_full)
                        if isinstance(p, GoalBlockRight):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_empty)
                else:
                    for p in platforms:
                        if isinstance(p, GoalBlockLeft) or isinstance(p, GoalBlockRight):
                            p.set_draw_procedural(constants.TILE_X, constants.TILE_Y, p.image_empty)

            # draw background
            for y in range(constants.TILE_Y_NUM):
                for x in range(constants.TILE_X_NUM):
                    screen.blit(bg, (x * constants.TILE_X, y * constants.TILE_Y))

            if self.level.print_background is not None:
                self.level.print_background(self.level, screen, constants.WIN_WIDTH, constants.WIN_HEIGHT)

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
            if self.level.success_animation is not None:
                print("Level finished : Doing final animation")
                self.level.success_animation(screen, constants.WIN_WIDTH, constants.WIN_HEIGHT)

                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == KEYDOWN and event.key == K_F10:
                            return
                    clock.tick(60)
