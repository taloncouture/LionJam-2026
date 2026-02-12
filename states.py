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

    def on_open(self):
        pass

class EndState(State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext

        self.text_y = HEIGHT

    def render(self, screen, surface):

        # screen.fill((102, 197, 255))
        # surface.fill((102, 197, 255))
        screen.fill((0, 0, 0))
        surface.fill((255, 243, 193))

        graphics.renderText(surface, WIDTH / 2, self.text_y, 60, "Thanks For Playing!", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 100, 50, f"Turns: {self.gameContext.turn}", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 200, 50, f"Pizzas Cooked: {self.gameContext.bricks}", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 400, 25, "Created by Talon Couture", 1, 0, (178, 0, 0))

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))

        

    def update(self):
        if(self.text_y > -1000):
            self.text_y -= 1

class TitleState(State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext

    def render(self, screen, surface):
        screen.fill((0, 0, 0))
        surface.fill((255, 243, 193))

        graphics.renderText(surface, WIDTH / 2, HEIGHT / 3, 60, "Great Pyramid of", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, HEIGHT / 3 + 60, 140, "PIZZA", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, HEIGHT - (HEIGHT / 5), 20, "press e to start", 1, 0, (178, 0, 0))

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))





    




