import pygame
import context
import assets
import graphics
from config import *

class Indicator:

    def __init__(self, image, x, y, quantity):
        self.image = image
        self.quantity = 1
        self.tile_x = x
        self.tile_y = y
        self.quantity = quantity

    def render(self, surface):
        ix, iy = context.coords_to_iso(self.tile_x, self.tile_y)
        surface.blit(self.image, (ix, iy - context.config.HALF_W - context.config.SCALE_FACTOR - 50))
        if(self.quantity > 1):
            graphics.renderText(surface, ix + PADDING * 7.5, iy - context.config.HALF_W - context.config.SCALE_FACTOR, 24, f'x{self.quantity}', 0, 1, (178, 0, 0))

class PizzaIndicator(Indicator):
    def __init__(self, x, y, quantity):
        super().__init__(assets.pizza, x, y, quantity)


class AttackIndicator(Indicator):
    def __init__(self, x, y, quantity):
        super().__init__(assets.energydrink, x, y, quantity)