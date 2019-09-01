import pygame
from pygame import *

from lib import *
from entities import constants
from levels import GameplayLevel
from levels.tutorial_levels import *
from levels.game_levels import *
from levels.test_levels import *


def main():
    pygame.mixer.pre_init(48000, -16, 2, 2048)
    pygame.init()
    # 1366 x 768
    # (1366-1312)/2 = 54/2 = 27
    # (768-704)/2 = 64/2 = 32
    offset_width = 27
    offset_height = 32

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((constants.WIN_WIDTH, constants.WIN_HEIGHT))
    pygame.display.set_caption("Love Runner")
    clock = pygame.time.Clock()

    info_display = pygame.display.Info()
    constants.current_w = info_display.current_w
    constants.current_h = info_display.current_h
    # constants.WIN_WIDTH = constants.current_w
    # constants.WIN_HEIGHT = constants.current_h

    levels = [
        tutorial_01(),
        tutorial_02(),
        tutorial_03(),
        tutorial_04(),
        tutorial_05(),
        tutorial_06(),
        tutorial_07(),
        tutorial_08(),
        tutorial_09(),
        tutorial_10(),
        tutorial_11(),
        level_02_Patri(),
        level_03_Dani(),
        level_04_Cor()
    ]

    # for i in range(1, len(levels)):
    #     level = levels[i-1]
        # level.add_caption(create_caption("Level " + str(i).zfill(2), 5, 5, color_fg=(170, 170, 170)))

    # music_file = 'music/8-bit-mario-theme.mp3'
    # pygame.mixer.music.load(music_file)
    # pygame.mixer.music.play(-1)
    failure_sound = pygame.mixer.Sound("sounds/sad_trombone.wav")
    success_sound = pygame.mixer.Sound("sounds/applause2.wav")

    image_file_lode = 'images/titles/LodeRunner_bg.png'
    image_file_love = 'images/titles/LodeRunner_love.png'
    image_file_ball = 'images/titles/LodeRunner_ball_25px.png'

    up = down = False
    failed = False
    success = False
    state = 1
    press_enter = 0
    done = False
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

            if e.type == KEYDOWN or e.type == KEYUP:

                if e.key == K_UP:
                    up = e.type == KEYDOWN
                if e.key == K_DOWN:
                    down = e.type == KEYDOWN

            if e.type == KEYDOWN:
                if e.key == K_RETURN or e.key == K_SPACE:
                    press_enter = 1

            if down:
                state = state + 1
                state = min(state, 3)

            if up:
                state = state - 1
                state = max(state, 1)

            if state == 1 and press_enter == 1:
                press_enter = 0
                failure_sound.play()
                failed = True

            if state == 2 and failed and press_enter == 1:
                press_enter = 0
                success = True

            if success:
                image_file = image_file_love
                success_sound.play()
                done = True

                image_title = pygame.image.load(image_file)
                image_ball = pygame.image.load(image_file_ball)
                screen.blit(image_title, (offset_width, offset_height))
                screen.blit(image_ball, (offset_width+516, offset_height+321 + (state - 1) * 52))
                pygame.display.update()
                clock.tick(600)
                pygame.time.wait(3000)
            else:
                image_file = image_file_lode

            # draw background
            image_title = pygame.image.load(image_file)
            image_ball = pygame.image.load(image_file_ball)
            screen.blit(image_title, (offset_width, offset_height))
            screen.blit(image_ball, (offset_width+516, offset_height+321+(state-1)*52))
            pygame.display.update()
            clock.tick(600)

    done = False
    i = 0
    while i < len(levels) and not done:
        # gameplay_level = GameplayLevel(levels[i], offset_width, offset_height)
        gameplay_level = GameplayLevel(levels[i])
        gameplay_level.play(screen, clock)
        i = i + 1


if __name__ == "__main__":
    main()
