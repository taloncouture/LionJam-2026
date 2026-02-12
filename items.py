import assets
from config import *

class Item:

    credits_produced = 0

    def __init__(self, image, x, y):
        self.image = image
        self.description = ""
        self.x = x
        self.y = y
        self.tile = None
        self.cost = 0
        self.credits_produced = 0

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))


class FactoryItem(Item):

    def __init__(self, x, y):
        super().__init__(assets.factory_item, x, y)
        from tiles import FactoryTile
        self.tile = FactoryTile
        self.cost = 10

class FarmItem(Item):

    credits_produced = 1

    def __init__(self, x, y):
        super().__init__(assets.farm_item, x, y)
        from tiles import Farm
        self.tile = Farm
        self.cost = 2
        self.credits_produced = 1

class RoadItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.road_item, x, y)
        from tiles import RoadTile
        self.tile = RoadTile
        self.cost = 1

class MonumentItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.monument_item, x, y)
        from tiles import MonumentTile
        self.tile = MonumentTile
        self.cost = 20

class PizzeriaItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.pizzeria_item, x, y)
        from tiles import PizzeriaTile
        self.tile = PizzeriaTile
        self.cost = 2



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


    