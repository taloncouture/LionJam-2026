import tiles
import pygame
from config import *
import math
import assets

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
    def __init__(self, engine):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def on_click(self):
        pass

class InventoryState(State):
    def __init__(self, engine):
        super().__init__(engine)

        self.x = (WIDTH - (128 * SCALE_FACTOR)) // 2
        self.y = (HEIGHT - (64 * SCALE_FACTOR)) // 2
        self.width = INVENTORY_WIDTH
        self.height = INVENTORY_HEIGHT
        self.selected_x = 0
        self.selected_y = 0

        self.engine = engine

        self.slots = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    def update(self):
        
        mx = self.engine.mouse_x
        my = self.engine.mouse_y
        if(self.x <= mx < self.x + self.width and self.y <= my < self.y + self.height):
            self.selected_x = int((mx - self.x) / (16 * SCALE_FACTOR))
            self.selected_y = int((my - self.y) / (16 * SCALE_FACTOR))

        #print(self.selected_x, self.selected_y)


    def render(self, screen, surface):

        screen.fill((186, 246, 255))
        surface.fill((186, 246, 255))


        surface.blit(assets.inventory, (self.x, self.y))
        surface.blit(assets.inventory_selector, (self.x + (self.selected_x * 16 * SCALE_FACTOR), self.y + (self.selected_y * 16 * SCALE_FACTOR)))

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))


class GameState(State):
    def __init__(self, engine):
        super().__init__(engine)
        self.engine = engine

    def on_click(self):
        mx = self.engine.mouse_x
        my = self.engine.mouse_y

        selected_x, selected_y = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        #print(selected_x, selected_y)

        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                if(tiles.tile_map[y][x].x == selected_x and tiles.tile_map[y][x].y == selected_y):
                    tiles.tile_map[y][x].on_click()

    def update(self):
        pass

    def render(self, screen, surface):

        screen.fill((186, 246, 255))
        surface.fill((186, 246, 255))

        for y in range(len(tiles.ground_tile_map)):
            for x in range(len(tiles.ground_tile_map[y])):
                tiles.ground_tile_map[y][x].render(surface)

        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                if(tiles.tile_map[y][x] != None):
                    tiles.tile_map[y][x].render(surface)

         # converting mouse coordinates - kind of weird (somehow works) do not change
        win_w, win_h = screen.get_size()
        scale = min(win_w / WIDTH, win_h / HEIGHT)
        scaled_w, scaled_h = int(WIDTH * scale), int(HEIGHT * scale)
        x = (win_w - scaled_w) // 2
        y = (win_h - scaled_h) // 2
        
        mx, my = pygame.mouse.get_pos()
        mx = (mx - x) / scale
        my = (my - y) / scale
        # converting mouse coordinates


        #selector
        imx, imy = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        if(0 <= imy < len(tiles.tiles_ground) and 0 <= imx < len(tiles.tiles_ground[imy]) and tiles.tiles_ground[imy][imx] != ' '):
            surface.blit(assets.selector, tiles.coords_to_iso(imx, imy))
        #selector

        screen.blit(pygame.transform.smoothscale(surface, (scaled_w, scaled_h)), (x, y))