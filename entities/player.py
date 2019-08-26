import pygame
from pygame import *

from entities import constants
from entities import Entity
from entities import PlatformBlock
from entities import StairsBlock
from entities import BarBlock
from entities import GoalBlock
from entities import GoalBlockLeft
from entities import GoalBlockRight

def draw_player(color, image_file=None, flip=False):
    temp_image = Surface((constants.TILE_X, constants.TILE_Y))
    temp_image.fill(Color(color))
    if image_file is not None:
        temp = pygame.image.load(image_file)
        if flip:
            temp = pygame.transform.flip(temp, True, False)
        temp = pygame.transform.scale(temp, (constants.TILE_X, constants.TILE_Y))
        temp_image.blit(temp, [0, 0])
        if constants.TILE_X > 16:
            temp_image = temp   # without background
    temp_image.convert()
    return temp_image


class Player(Entity):

    collides = True
    has_grip = False

    def __init__(self, x, y, name, color, image_file=None, flip=False):
        Entity.__init__(self)
        self.name = name
        self.color = color
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.onStairs = False
        self.onBar = False
        self.on_goal = False
        self.image = draw_player(self.color, image_file, flip)
        self.rect = Rect(x, y, constants.TILE_X-2, constants.TILE_Y)

    def update(self, up, down, left, right, platforms):
        if self.onStairs:
            self.yvel = 0
            if up: self.yvel = -constants.VELOCITY_MOVEMENT
            if down: self.yvel = constants.VELOCITY_MOVEMENT
        if self.onBar and down:
            self.yvel = constants.VELOCITY_MOVEMENT
        if self.onGround and up:
            # only jump if on the ground
            self.yvel -= constants.VELOCITY_JUMP

        if not self.onGround and not self.onStairs and not self.onBar:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > constants.VELOCITY_MAX_FALL: self.yvel = constants.VELOCITY_MAX_FALL

        if left:
            self.xvel = -constants.VELOCITY_MOVEMENT
        if right:
            self.xvel = constants.VELOCITY_MOVEMENT
        if not(left or right):
            self.xvel = 0
        if not(up or down) and self.onStairs and self.onBar:
            self.yvel = 0

        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, up, down, left, right, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # do y-axis collisions
        self.collide(0, self.yvel, up, down, left, right, platforms)

    def collide(self, xvel, yvel, up, down, left, right, platforms):

        any_stairs = False
        any_bar = False
        self.onGround = False
        if isinstance(self, Player):
            self.on_goal = False

        for p in platforms:

            if isinstance(self, Player) and (isinstance(p, GoalBlock) or isinstance(p, GoalBlockLeft) or isinstance(p, GoalBlockRight)):
                offset = 1
                self.rect.top += offset
                if pygame.sprite.collide_rect(self, p) and self.yvel >= 0:
                    self.on_goal = True
                self.rect.top -= offset

            if pygame.sprite.collide_rect(self, p) and p is not self:

                if yvel > 0 and (
                        isinstance(p, PlatformBlock)
                        or isinstance(p, GoalBlock)
                ):
                    self.onGround = True
                if isinstance(p, StairsBlock):
                    any_stairs = True
                if isinstance(p, BarBlock):
                    any_bar = True

                if xvel > 0 and p.collides:
                    self.rect.right = p.rect.left
                    self.xvel = 0
                if xvel < 0 and p.collides:
                    self.rect.left = p.rect.right
                    self.xvel = 0

                if yvel > 0 and p.collides:
                    self.rect.bottom = p.rect.top
                    self.yvel = 0
                if yvel < 0 and p.collides:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
                if yvel > 0 and p.has_grip and not (self.onStairs or self.onBar) and not down:
                    # this is like a collision since we are not moving
                    self.rect.bottom = p.rect.top
                    self.yvel = 0

        if not any_bar and self.onBar and yvel < 0:
            self.yvel = 1

        self.onStairs = any_stairs
        self.onBar = any_bar
