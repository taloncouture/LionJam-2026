from config import *
import assets
import pygame
from states import *
import items
import context
import graphics

class ShopState(State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)

        self.x = (WIDTH - (128 * SCALE_FACTOR)) // 2
        self.y = (HEIGHT - (64 * SCALE_FACTOR)) // 2
        self.width = INVENTORY_WIDTH
        self.height = INVENTORY_HEIGHT
        self.selected_x = None
        self.selected_y = None

        self.highlighted_x = None
        self.highlighted_y = None

        self.engine = engine
        self.gameContext = gameContext

        self.slots = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        self.slots[0][0] = items.RoadItem(self.x, self.y)
        self.slots[0][1] = items.FarmItem(self.x + (16 * SCALE_FACTOR), self.y)
        self.slots[0][2] = items.PizzeriaItem(self.x + (16 * 2 * SCALE_FACTOR), self.y)
        self.slots[0][3] = items.FactoryItem(self.x + (16 * 3 * SCALE_FACTOR), self.y)
        self.slots[1][0] = items.MonumentItem(self.x, self.y + (ITEM_HEIGHT))

    def update(self):
        
        mx = self.engine.mouse_x
        my = self.engine.mouse_y
        if(self.x <= mx < self.x + self.width and self.y <= my < self.y + self.height):
            self.selected_x = int((mx - self.x) / (16 * SCALE_FACTOR))
            self.selected_y = int((my - self.y) / (16 * SCALE_FACTOR))

        #print(self.selected_x, self.selected_y)

    def on_click(self):
        mx = self.engine.mouse_x
        my = self.engine.mouse_y
        if(self.x <= mx < self.x + self.width and self.y <= my < self.y + self.height):
            x = int((mx - self.x) / (16 * SCALE_FACTOR))
            y = int((my - self.y) / (16 * SCALE_FACTOR))

            if(self.slots[y][x] != ' '):
                self.gameContext.selected_item = self.slots[y][x]
                self.highlighted_x = x
                self.highlighted_y = y

        else:
            self.highlighted_x = None
            self.highlighted_y = None
            self.selected_x = None
            self.selected_y = None
            self.gameContext.selected_item = None

    def on_close(self):
        self.highlighted_x = None
        self.highlighted_y = None


    def render(self, screen, surface):

        screen.fill((102, 197, 255))
        surface.fill((102, 197, 255))

        # screen.fill((185, 157, 51))
        # surface.fill((185, 157, 51))

        surface.blit(assets.cheese, ((WIDTH / 2) - (TILE_SIZE / 2), (PADDING * 6)))
        graphics.renderText(surface, (WIDTH / 2) + PADDING * 3, (PADDING * 5.5) + (TILE_SIZE / 2), 24, f'x{self.gameContext.credits}', 0, 1)


        surface.blit(assets.inventory, (self.x, self.y))

        for y in range(len(self.slots)):
            for x in range(len(self.slots)):
                if(self.slots[y][x] != ' '):
                    self.slots[y][x].render(surface)


        if(self.selected_x != None):
            surface.blit(assets.inventory_selector, (self.x + (self.selected_x * 16 * SCALE_FACTOR), self.y + (self.selected_y * 16 * SCALE_FACTOR)))

        if(self.highlighted_x != None):
            surface.blit(assets.inventory_selected, (self.x + (self.highlighted_x * 16 * SCALE_FACTOR), self.y + (self.highlighted_y * 16 * SCALE_FACTOR)))

        surface.blit(assets.shop_border, (self.x - (16 * SCALE_FACTOR), self.y - (16 * SCALE_FACTOR)))

        

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))
