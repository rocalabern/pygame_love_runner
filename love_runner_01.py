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

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.WIN_WIDTH, constants.WIN_HEIGHT))
    pygame.display.set_caption("Love Runner")
    timer = pygame.time.Clock()

    tile = 16
    constants.VELOCITY_MOVEMENT = 4
    constants.VELOCITY_JUMP = 4
    constants.VELOCITY_MAX_FALL = 15
    constants.TILE_X = tile
    constants.TILE_Y = tile
    constants.TILE_X_NUM = 1312 // tile
    constants.TILE_Y_NUM = 704 // tile
    level = tools.read_level("levels/01_level.txt")
    # level = tools.read_level("levels/02_level.txt")
    
    bg = Surface((constants.TILE_X, constants.TILE_Y))
    bg.convert()
    # bg.fill(Color(constants.COLOR_BCKGRND))
    bg.fill(Color(constants.COLOR_BCKGRND), Rect(2, 2, constants.TILE_X-2, constants.TILE_Y-2))

    entities = pygame.sprite.Group()
    player_p1 = Player(constants.TILE_X, constants.TILE_Y, "#4da6ff")
    player_p2 = Player(constants.TILE_X*2, constants.TILE_Y, "#ff80bf")
    platforms = []

    # build the level
    x = y = 0
    for row in level:
        for col in row:
            if col == "P":
                e = PlatformBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "E":
                e = StairsBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "B":
                e = BarBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "G":
                e = GoalBlock(x, y)
                platforms.append(e)
                entities.add(e)
            x += constants.TILE_X
        y += constants.TILE_Y
        x = 0

    entities.add(player_p1)
    entities.add(player_p2)
    platforms.append(player_p1)
    platforms.append(player_p2)

    up_p1 = down_p1 = left_p1 = right_p1 = False
    up_p2 = down_p2 = left_p2 = right_p2 = False

    done = False
    while not done:
        timer.tick(60)

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

        # draw background
        for y in range(constants.TILE_Y_NUM):
            for x in range(constants.TILE_X_NUM):
                screen.blit(bg, (x * constants.TILE_X, y * constants.TILE_Y))

        # update player, draw everything else
        player_p1.update(up_p1, down_p1, left_p1, right_p1, platforms)
        player_p2.update(up_p2, down_p2, left_p2, right_p2, platforms)
        entities.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
