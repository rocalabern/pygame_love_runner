import pygame
from pygame import *

from lib import tools
from entities import constants
from entities import Entity
from entities import PlatformBlock
from entities import StairsBlock
from entities import BarBlock
from entities import GoalBlock
from entities import Player
from levels import Level


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
                player_p1 = Player(x, y, constants.COLOR_PLAYER_P1)
            if level_block == "X":
                player_p2 = Player(x, y, constants.COLOR_PLAYER_P2)
            x += constants.TILE_X
        y += constants.TILE_Y
        x = 0
    platforms.append(player_p1)
    entities.add(player_p1)
    entities.add(player_p2)
    platforms.append(player_p2)
    return (entities, platforms, player_p1, player_p2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.WIN_WIDTH, constants.WIN_HEIGHT))
    pygame.display.set_caption("Love Runner")
    clock = pygame.time.Clock()

    levels = [
        Level("levels/00_level.txt", 32),
        Level("levels/01_level.txt", 32),
        Level("levels/02_level.txt", 16),
        Level("levels/03_level.txt", 16),
        Level("levels/04_level.txt", 16)
    ]

    (entities, platforms, player_p1, player_p2) = load_level(levels[4])

    bg = get_background_tile(constants.TILE_X, constants.TILE_Y)

    up_p1 = down_p1 = left_p1 = right_p1 = False
    up_p2 = down_p2 = left_p2 = right_p2 = False

    done = False
    while not done:

        e: event
        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                done = True

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
        entities.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
