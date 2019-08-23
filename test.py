import pygame
from pygame import *

from entities import constants
from entities import Entity
from entities import PlatformBlock
from entities import StairsBlock
from entities import GoalBlock
from entities import Player

fileName = "levels/01_level.txt"

with open(fileName) as f:
  lineList = f.readlines()

lineList = [line.rstrip('\n') for line in open(fileName)]

lineList

level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                       P",
        "P                                       P",
        "P                             EPPPP     P",
        "P                             E         P",
        "P                             E         P",
        "P                             E         P",
        "P                             E         P",
        "P                          PPPPPPP      P",
        "P                                       P",
        "P               PPPP                    P",
        "P                                       P",
        "P                                       P",
        "P     PPP     EPPPPPPPPPP               P",
        "P             E                         P",
        "P             E                         P",
        "P      EPPPPPPPPPPP                     P",
        "P      E                                P",
        "P      E                                P",
        "P      E                                P",
        "P      E                                P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]

lineList
level