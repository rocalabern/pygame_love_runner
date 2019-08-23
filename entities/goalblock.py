import pygame
from pygame import *

from entities import constants
from .platformblock import PlatformBlock


class GoalBlock(PlatformBlock):

    collides = True
    has_grip = False

    def __init__(self, x, y):
        PlatformBlock.__init__(self, x, y)
        self.image.fill(Color("#99ff99"))
