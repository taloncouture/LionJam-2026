import assets
import config

def coords_to_iso(x, y):

    iso_x = (x - y) * config.HALF_W
    iso_y = (x + y) * config.HALF_H

    return config.ORIGIN_X + iso_x, config.ORIGIN_Y + iso_y

tiles_ground = [[' ', ' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', '0', '0', '0', ' ', ' '],
                [' ', 'p', 'p', 'p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
                [' ', 'p', 'p', 'p', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
                [' ', 'p', 'p', 'p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
                [' ', ' ', '0', ' ', ' ', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
                ['p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
                [' ', ' ', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', '0', '0', '0', ' '],
                [' ', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', '0', '0', '0', '0'],
                [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
                [' ', '0', '0', '0', ' ', ' ', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
                [' ', ' ', '0', '0', ' ', '0', '0', '0', '0', '0', ' ', ' ', '0', '0', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', ' ', ' ', ' ', ' ']]

tiles2 =       [[' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', '!', '~', '~', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 't', ' ', 't', 't', ' ', ' '],
                ['@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['t', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['t', ' ', ' ', ' ', ' ', 't', ' ', 't', ' ', ' ', ' ', 't', ' ', ' ', ' '],
                [' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', ' ', ' '],
                [' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

tile_map = []
ground_tile_map = []

def place_tile(x, y, tile):

    if(0 <= y < len(tile_map) and 0 <= x < len(tile_map[y]) and type(ground_tile_map[y][x]) is GrassTile and type(tile_map[y][x]) is AirTile):
        #print(tile_map[y][x])
        #print(ground_tile_map[y][x])
        tile_map[y][x] = tile(x, y)
        return True
    return False


def get_neighbors(x, y, tilemap):
    result = []
    
    # if(x > 0 and y > 0):
    #     result[0][0] = tilemap[y - 1][x - 1]
    # if(y > 0):
    #     result[0][1] = tilemap[y - 1][x]
    # if(x < len(tilemap[0]) - 1 and y > 0):
    #     result[0][2] = tilemap[y - 1][x + 1]
    # if(x > 0):
    #     result[1][0] = tilemap[y][x - 1]
    # if(x < len(tilemap[0]) - 1):
    #     result[1][2] = tilemap[y][x + 1]
    # if(x > 0 and y < len(tilemap) - 1):
    #     result[2][0] = tilemap[y + 1][x - 1]
    # if(y < len(tilemap) - 1):
    #     result[2][1] = tilemap[y + 1][x]
    # if(y < len(tilemap) - 1 and x < len(tilemap[0]) - 1):
    #     result[2][2] = tilemap[y + 1][x + 1]
    if(x > 0):
        result.append(tilemap[y][x - 1])
    if(x < len(tilemap[0]) - 1):
        result.append(tilemap[y][x + 1])
    if(y > 0):
        result.append(tilemap[y - 1][x])
    if(y < len(tilemap) - 1):
        result.append(tilemap[y + 1][x])

    return result



class Resource():
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y


class PizzaResource(Resource):

    image = assets.pizza

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

class Tile:

    def __init__(self, x, y):
        self.image = assets.grass
        self.x = x
        self.y = y
        self.cost = 0
        self.credits_produced = 0
        self.network_id = None
        self.required_connections = {}
        self.connected_tiles = {}

    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy - config.HALF_W - config.SCALE_FACTOR))

    def update(self):
        pass

    def on_click(self):
        pass

    def place_tile(self):
        pass

class ResourceTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.claimed = None

class ProductionTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.has_item = False
        self.required_farms = 0
        self.claimed = None
        self.requirements_met = False

    def produce(self):
        if(self.requirements_met):
            self.has_item = True

    def collect(self):
        if(self.has_item):
            self.has_item = False
            return True
        return False

    def update(self):
        self.produce()

class GrassTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy))

class PlatformTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.platform

    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy))

    # def on_click(self):
    #     place_tile(self.x, self.y, FactoryTile)

class FactoryTile(ProductionTile):

    resource = PizzaResource

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.factory
        self.credits_produced = 3
        self.required_farms = 2
        self.required_connections = {Farm : 2}

class PizzeriaTile(ProductionTile):

    resource = PizzaResource

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.pizzeria
        self.credits_produced = 1
        self.required_connections = {Farm : 1}
        

class RoadTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.road

class MonumentTile(Tile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.monument
        self.credits_produced = 5

class CheeseTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.cheese

class ForestTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.forest

class AirTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, surface):
        pass

    # def on_click(self):
    #     place_tile(self.x, self.y)

class Restricted(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def render(self, surface):
        pass

class Pyramid(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.stages = [None, assets.stage_1, assets.stage_2, assets.stage_3, assets.stage_4, assets.stage_5]
        self.stage = 0

    def render(self, surface):
        if(self.stage != 0):
            ix, iy = coords_to_iso(self.x, self.y)
            surface.blit(self.stages[self.stage], (ix - (config.HALF_W * (2)) - config.SCALE_FACTOR * 2, iy - (config.HALF_H * (5)) - config.HALF_W + config.SCALE_FACTOR))

    def build(self):
        if(self.stage < len(self.stages) - 1):
            self.stage += 1

class MRPizza(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.mrpizza

class Critics(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.critics

class Farm(ResourceTile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.farm
        self.credits_produced = 1

class RedBull(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.redbulls


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
        elif tiles2[y][x] == '@':
            tile_row.append(MRPizza(x, y))
        elif tiles2[y][x] == 'c':
            tile_row.append(Critics(x, y))
        elif tiles2[y][x] == 'r':
            tile_row.append(Farm(x, y))
        elif tiles2[y][x] == 'e':
            tile_row.append(RedBull(x, y))
        else:
            tile_row.append(AirTile(x, y))
    tile_map.append(tile_row)

for y in range(len(tiles_ground)):
    tile_row = []
    for x in range(len(tiles_ground[y])):
        if tiles_ground[y][x] == '0':
            tile_row.append(GrassTile(x, y))
        elif tiles_ground[y][x] == 'p':
            tile_row.append(PlatformTile(x, y))
        else:
            tile_row.append(AirTile(x, y))
    ground_tile_map.append(tile_row)

