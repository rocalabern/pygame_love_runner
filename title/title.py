import pygame
from pygame import *

from lib import *
from game_screen.game_screen import GameScreen


def menu_title(game_screen: GameScreen):
    # music_file = 'music/8-bit-mario-theme.mp3'
    # pygame.mixer.music.load(music_file)
    # pygame.mixer.music.play(-1)
    failure_sound = pygame.mixer.Sound("sounds/sad_trombone.wav")
    success_sound = pygame.mixer.Sound("sounds/applause2.wav")

    image_file_lode = 'images/titles/LodeRunner_bg.png'
    image_file_love = 'images/titles/LodeRunner_love.png'
    image_file_ball = 'images/titles/LodeRunner_ball_25px.png'

    image_lode_raw = pygame.image.load(image_file_lode)
    image_love_raw = pygame.image.load(image_file_love)
    (image_lode, image_lode_x, image_lode_y) = pg_rescale_image_full_screen(game_screen, image_lode_raw, perc=1.0)
    (image_love, image_love_x, image_love_y) = pg_rescale_image_full_screen(game_screen, image_love_raw, perc=1.0)
    image_ball_raw = pygame.image.load(image_file_ball)
    image_ball = pg_rescale_image_factor_bg(image_ball_raw, image_lode_raw, image_lode)

    clock = pygame.time.Clock()
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
                image_title = image_love
                image_title_x = image_love_x
                image_title_y = image_love_y
                success_sound.play()
                done = True

                # draw background
                game_screen.screen_desktop.blit(
                    image_title,
                    (
                        game_screen.x_offset + image_title_x,
                        game_screen.y_offset + image_title_y
                    )
                )

                (pos_x, pos_y) = game_screen.position_desktop(0.385, 0.465+(state - 1)*0.07)
                game_screen.screen_desktop.blit(image_ball, (pos_x, pos_y))

                pygame.display.update()
                clock.tick(100)
                pygame.time.wait(3000)
            else:
                image_title = image_lode
                image_title_x = image_lode_x
                image_title_y = image_lode_y

            # draw background
            game_screen.screen_desktop.blit(image_title, (game_screen.x_offset + image_title_x, game_screen.y_offset + image_title_y))
            (pos_x, pos_y) = game_screen.position_desktop(0.385, 0.465+(state - 1)*0.07)
            game_screen.screen_desktop.blit(image_ball, (pos_x, pos_y))
            pygame.display.update()
            clock.tick(100)
