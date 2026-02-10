import assets
import config

def coords_to_iso(x, y):

    iso_x = (x - y) * config.HALF_W
    iso_y = (x + y) * config.HALF_H

    return config.ORIGIN_X + iso_x, config.ORIGIN_Y + iso_y

tiles_ground = [[' ', ' ', ' ', ' ', '0', '0', '0', '0', ' ', ' ', '0', '0', '0', ' ', ' '],
         [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
         [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
         [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
         [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
         [' ', '0', '0', '0', ' ', ' ', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
         [' ', ' ', '0', '0', ' ', '0', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', ' ', ' ', ' ', ' ']]

tiles2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '~', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '~', '!', '~', '~', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '~', '~', '~', '~', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '~', '~', '~', '~', '~', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' '],
         [' ', '~', '@', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

tile_map = []
ground_tile_map = []

def place_tile(x, y, tile):

    if(0 <= y < len(tile_map) and 0 <= x < len(tile_map[y]) and type(ground_tile_map[y][x]) is GrassTile and type(tile_map[y][x]) is AirTile):
        print(tile_map[y][x])
        print(ground_tile_map[y][x])
        tile_map[y][x] = tile(x, y)
        return True
    return False

class Tile:
    def __init__(self, x, y):
        self.image = assets.grass
        self.x = x
        self.y = y

    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy - config.HALF_W - config.SCALE_FACTOR))

    def update(self):
        pass

    def on_click(self):
        pass

    def place_tile(self):
        pass

class GrassTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy))

    # def on_click(self):
    #     place_tile(self.x, self.y, FactoryTile)

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

class AirTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, surface):
        pass

    def on_click(self):
        place_tile(self.x, self.y, FactoryTile)

class Restricted(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, surface):
        pass

class Pyramid(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, surface):
        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(assets.pyramid, (ix - (config.HALF_W * (2)) - config.SCALE_FACTOR * 2, iy - (config.HALF_H * (5)) - config.HALF_W + config.SCALE_FACTOR))


#tile_list = {'f': FactoryTile, 't': ForestTile, '0': GrassTile}


for y in range(len(tiles2)):
    tile_row = []
    for x in range(len(tiles2[y])):
        if tiles2[y][x] == 'f':
            tile_row.append(FactoryTile(x, y))
        elif tiles2[y][x] == 't':
            tile_row.append(ForestTile(x, y))
        elif tiles2[y][x] == '~':
            tile_row.append(Restricted(x, y))
        elif tiles2[y][x] == '!':
            tile_row.append(Pyramid(x, y))
        else:
            tile_row.append(AirTile(x, y))
    tile_map.append(tile_row)

for y in range(len(tiles_ground)):
    tile_row = []
    for x in range(len(tiles_ground[y])):
        if tiles_ground[y][x] == '0':
            tile_row.append(GrassTile(x, y))
        else:
            tile_row.append(AirTile(x, y))
    ground_tile_map.append(tile_row)

