import tiles
import pygame
from config import *
import math
import assets
import graphics
import items

def screen_to_iso(mx, my, origin_x, origin_y):

    mx -= origin_x
    my -= origin_y

    mx -= HALF_W
    my -= HALF_H

    dx = mx / HALF_W
    dy = my / HALF_H

    x = (dx + dy) / 2
    y = (dy - dx) / 2

    return math.floor(x + 0.5), math.floor(y + 0.5)

class State:
    def __init__(self, engine, gameContext):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def on_click(self):
        pass

    def on_close(self):
        pass




