import assets
import tiles
from config import *

class Item:
    def __init__(self, image, x, y):
        self.image = image
        self.description = ""
        self.x = x
        self.y = y
        self.tile = None
        self.cost = 0

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))


class FactoryItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.factory_item, x, y)
        self.tile = tiles.FactoryTile
        self.cost = 5

class FarmItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.farm_item, x, y)
        self.tile = tiles.Farm
        self.cost = 2

class RoadItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.road_item, x, y)
        self.tile = tiles.RoadTile
        self.cost = 1

class MonumentItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.monument_item, x, y)
        self.tile = tiles.MonumentTile
        self.cost = 20

class Button:
    def __init__(self, image, x, y, engine):
        self.image = image
        self.x = x
        self.y = y
        self.width = ITEM_WIDTH
        self.height = ITEM_WIDTH
        self.engine = engine
        self.selected = False

    def render(self):
        self.engine.render(self.image, self.x, self.y)
        if(self.x <= self.engine.mouse_x <= self.x + self.width and self.y <= self.engine.mouse_y <= self.y + self.height):
            self.engine.render(assets.inventory_selector, self.x, self.y)

    def update(self):
        if(self.x <= self.engine.mouse_x <= self.x + self.width and self.y <= self.engine.mouse_y <= self.y + self.height):
            self.selected = True
        else:
            self.selected = False


    