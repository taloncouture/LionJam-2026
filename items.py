import assets
import tiles

class Item:
    def __init__(self, image, x, y):
        self.image = image
        self.description = ""
        self.x = x
        self.y = y
        self.tile = None

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))


class FactoryItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.factory_item, x, y)
        self.tile = tiles.FactoryTile

class FarmItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.farm_item, x, y)
        self.tile = tiles.Farm

class RoadItem(Item):
    def __init__(self, x, y):
        super().__init__(assets.road_item, x, y)
        self.tile = tiles.RoadTile



    