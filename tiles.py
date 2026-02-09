import assets
import config

def coords_to_iso(x, y):

    iso_x = (x - y) * config.HALF_W
    iso_y = (x + y) * config.HALF_H

    return config.ORIGIN_X + iso_x, config.ORIGIN_Y + iso_y

class Tile:
    def __init__(self, x, y):
        self.image = assets.grass
        self.x = x
        self.y = y

    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy - config.HALF_W - config.SCALE_FACTOR))

        #empty

    def update(self):
        pass

    def on_click(self):
        pass


class FactoryTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.factory

    def on_click(self):
        print("factory clicked")

class ForestTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.forest