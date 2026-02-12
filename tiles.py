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

def is_valid(x, y, tilemap):
    if(0 <= y < len(tilemap) and 0 <= x < len(tilemap[y])):
        return True
    else:
        return False

def place_tile(x, y, tile, tilemap):

    if(0 <= y < len(tilemap) and 0 <= x < len(tilemap[y]) and type(ground_tile_map[y][x]) is GrassTile and type(tilemap[y][x]) is AirTile):

        if(issubclass(tile, FactoryTile)):
            neighbors = get_neighbors(x, y, ground_tile_map)

            for neighbor in neighbors:
                print(neighbor)
                if(neighbor == None or isinstance(neighbor, AirTile)):
                    tile_map[y][x] = tile(x, y)
                    return True
        else:
            tile_map[y][x] = tile(x, y)
            return True
    return False

def destroy_tile(x, y, tilemap):
    tilemap[y][x] = AirTile(x, y)


def get_neighbors(x, y, tilemap):
    result = []

    if(is_valid(x - 1, y, tilemap)):
        result.append(tilemap[y][x - 1])
    else:
        result.append(None)
    
    if(is_valid(x + 1, y, tilemap)):
        result.append(tilemap[y][x + 1])
    else:
        result.append(None)

    if(is_valid(x, y - 1, tilemap)):
        result.append(tilemap[y - 1][x])
    else:
        result.append(None)

    if(is_valid(x, y + 1, tilemap)):
        result.append(tilemap[y + 1][x])
    else:
        result.append(None)

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
        self.x = x
        self.y = y
        self.cost = 0
        self.credits_produced = 0
        self.network_id = None
        self.required_connections = {}
        self.connected_tiles = {}
        self.claimable = False
        self.claimed = None
        self.image = assets.grass

        self.frames = []
        self.index = 0
        self.anim_speed = 0


    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy - config.HALF_W - config.SCALE_FACTOR))

    def update(self):
        self.animate()

    def on_click(self):
        pass

    def place_tile(self):
        pass

    def animate(self):
        
        self.index += self.anim_speed
        if(self.index >= len(self.frames)):
            self.index = 0

        if(len(self.frames) > 0):
            self.image = self.frames[int(self.index)]

class ResourceTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.claimed = None
        self.claimable = True

class ProductionTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.has_item = False
        self.required_farms = 0
        self.claimed = None
        self.requirements_met = False
        self.claimable = True

        self.production_quantity = 1

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
        self.image = assets.factory_1
        self.credits_produced = 3
        self.required_farms = 3
        self.required_connections = {Farm : 2, Housing : 1, Restricted : 1}
        self.production_quantity = 3
        
        self.frames = [assets.factory_1, assets.factory_2, assets.factory_3]
        self.anim_speed = 0.02


class PizzeriaTile(ProductionTile):

    resource = PizzaResource

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.pizzeria
        self.credits_produced = 1
        self.required_connections = {Farm : 1, Restricted : 1}
        

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

class MRPizza(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.mrpizza
        self.frames = [assets.mrpizza, assets.mrpizza_2]
        self.anim_speed = 0.03

class Critics(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.critics

class Farm(ResourceTile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.farm_1
        self.credits_produced = 1
        self.frames = [assets.farm_1, assets.farm_2, assets.farm_3]
        self.anim_speed = 0.1
      


class Housing(ResourceTile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.housing
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

