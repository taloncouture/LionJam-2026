import assets
import config
import random
import indicator
import pygame
import animation

def coords_to_iso(x, y):

    iso_x = (x - y) * config.HALF_W
    iso_y = (x + y) * config.HALF_H

    return config.ORIGIN_X + iso_x, config.ORIGIN_Y + iso_y

tiles_ground = [[' ', ' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', '0', '0', '#', ' ', ' '],
                [' ', 'p', 'p', 'p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
                [' ', 'p', 'p', 'p', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
                [' ', 'p', 'p', 'p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
                [' ', ' ', '0', ' ', ' ', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
                ['p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
                [' ', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
                [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', '0', '0', '0', '0'],
                [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', '#'],
                [' ', '#', '0', '0', ' ', ' ', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
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

pathfinding =  [[' ', ' ', ' ', ' ', ' ', ' ', 16, 15, ' ', ' ', 12, 11, 10, ' ', ' '],
                [' ', 'p', 'p', 'p', ' ', 18, 17, 16, 15, 14, 13, 12, 11, ' ', ' '],
                [' ', 'p', 'p', 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, ' '],
                [' ', 'p', 21, 'p', ' ', 18, 17, 16, 15, 14, 13, 12, 11, 10, ' '],
                [' ', ' ', 20, ' ', ' ', 17, 16, 15, 14, 13, 12, 11, 10, ' ', ' '],
                ['p', ' ', 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, ' '],
                [' ', ' ', 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, ' '],
                [' ', 16, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
                [14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
                [13, 14, 15, 14, 13, 12, 11, 10, 9, ' ', 7, 6, 5, 4, 3],
                [12, 13, 14, 13, 12, 11, 10, 9, 8, ' ', ' ', 5, 4, 3, 2],
                [' ', 12, 13, 12, 11, 10, 9, 8, 7, 6, ' ', 4, 3, 2, ' '],
                [' ', 11, 12, 11, ' ', ' ', 8, 7, 6, 5, ' ', 3, 2, 1, ' '],
                [' ', ' ', 11, 10, ' ', 6, 7, 6, 5, 4, ' ', ' ', 1, 0, ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 5, 4, ' ', ' ', ' ', ' ', ' ', ' ']]

tile_map = []
ground_tile_map = []

def is_valid(x, y, tilemap):
    if(0 <= y < len(tilemap) and 0 <= x < len(tilemap[y])):
        return True
    else:
        return False
    
def adjacent_to_building(x, y, tilemap):
    neighbors = get_neighbors(x, y, tilemap)

    for neighbor in neighbors:
        if(neighbor.building == True):
            return True
        
    return False

def place_tile(x, y, tile, tilemap):

    if(0 <= y < len(tilemap) and 0 <= x < len(tilemap[y]) and type(ground_tile_map[y][x]) is GrassTile and type(tilemap[y][x]) is AirTile):

        if(adjacent_to_building(x, y, tilemap)):


            if(issubclass(tile, FactoryTile)):
                neighbors = get_neighbors(x, y, ground_tile_map)

                for neighbor in neighbors:
                    #print(neighbor)
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
    # else:
    #     result.append(None)
    
    if(is_valid(x + 1, y, tilemap)):
        result.append(tilemap[y][x + 1])
    # else:
    #     result.append(None)

    if(is_valid(x, y - 1, tilemap)):
        result.append(tilemap[y - 1][x])
    # else:
    #     result.append(None)

    if(is_valid(x, y + 1, tilemap)):
        result.append(tilemap[y + 1][x])
    # else:
    #     result.append(None)

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
        self.building = False
        self.indicator = None
        self.indicator_quantity = 0

        self.frames = []
        self.index = 0
        self.anim_speed = 0


    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy - config.HALF_W - config.SCALE_FACTOR))

        if(self.indicator != None and self.indicator_quantity > 0):
            self.indicator.render(surface)

    def update(self):
        self.animate()

    def on_click(self):
        pass

    def place_tile(self):
        pass

    def destroy(self):
        tile_map[self.y][self.x] = AirTile(self.x, self.y)
        pygame.mixer.Sound.play(assets.construct)

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
        self.building = True

class ProductionTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.required_farms = 0
        self.claimed = None
        self.requirements_met = False
        self.claimable = True
        self.building = True
        self.production_quantity = 0

        self.produced = 0

    def produce(self):
        if(self.requirements_met):
            self.indicator_quantity += self.production_quantity
            self.indicator.quantity = self.indicator_quantity

    def collect(self):
        if(self.indicator_quantity > 0):
            result = self.indicator_quantity
            pygame.mixer.Sound.play(assets.collect)
            #pygame.mixer.Sound.play(random.choice([assets.pizza_sound, assets.pizza_sound_2, assets.pizza_sound_3]))
            self.indicator_quantity = 0
            return result
        return 0

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
        self.credits_produced = 1
        self.required_farms = 3
        self.required_connections = {Farm : 2, Housing : 1, Restricted : 1}
        self.production_quantity = 3
        
        self.frames = [assets.factory_1, assets.factory_2, assets.factory_3]
        self.anim_speed = 0.02

        self.indicator = indicator.PizzaIndicator(self.x, self.y, self.production_quantity)


class PizzeriaTile(ProductionTile):

    resource = PizzaResource

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.pizzeria
        self.credits_produced = 1
        self.production_quantity = 1
        self.required_connections = {Farm : 1, Restricted : 1}
        self.indicator = indicator.PizzaIndicator(self.x, self.y, self.production_quantity)
        

        

class RoadTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.road
        self.building = True

class MonumentTile(Tile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.monument
        self.credits_produced = 5
        self.building = True

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
        self.building = True

    def render(self, surface):
        pass

class Pyramid(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.stages = [assets.stage_0, assets.stage_1, assets.stage_2, assets.stage_3, assets.stage_4, assets.stage_5]
        self.stage = 0

    def render(self, surface):
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

class MilitaryTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

class Tower(MilitaryTile):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.tower
        self.building = True
        self.age = 0
        self.indicator = indicator.AttackIndicator(self.x, self.y, 0)

    def on_click(self):
        self.attack()
        self.indicator_quantity = 0
    
    def attack(self):
        if(self.age > 0):
            neighbors = get_neighbors(self.x, self.y, tile_map)
            for neighbor in neighbors:
                if(isinstance(neighbor, EnemyTile)):
                    neighbor.destroy()
                    pygame.mixer.Sound.play(assets.open_can)

    def lookout(self):
        #print(f"Tower: {(self.x, self.y)} looking out")
        self.indicator_quantity = 0

        neighbors = get_neighbors(self.x, self.y, tile_map)
        for neighbor in neighbors:
            if(isinstance(neighbor, EnemyTile)):
                self.indicator_quantity += 1

    def update(self):
        self.age += 1

        

class RedBull(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.redbulls


#tile_list = {'f': FactoryTile, 't': ForestTile, '0': GrassTile}

class NolatPlatform(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.nolat_platform

    def render(self, surface):

        ix, iy = coords_to_iso(self.x, self.y)
        surface.blit(self.image, (ix, iy))

    def spawn(self):
        if(isinstance(tile_map[self.y][self.x], AirTile)):
            tile_map[self.y][self.x] = Nolat(self.x, self.y)

class EnemyTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        pass

    def update(self):
        self.move()


class Nolat(EnemyTile):

    spawn_chance = 0.4

    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = assets.nolat_1
        self.frames = [assets.nolat_1, assets.nolat_1_1, assets.nolat_2, assets.nolat_2_1]
        self.anim_speed = 0.02
        self.age = 0
        self.occupied_tile = None

    def on_click(self):
        # print("clicked")
        # self.destroy()
        pass


    def destroy(self):
        if(self.occupied_tile != None): 
            tile_map[self.y][self.x] = self.occupied_tile
        else:
            tile_map[self.y][self.x] = AirTile(self.x, self.y)

        ix, iy = coords_to_iso(self.x, self.y)
        pop_anim = animation.Animation(ix, iy, [assets.explode_1, assets.explode_2, assets.explode_3], 0.3)
        # if(isinstance(tiles_ground[self.y][self.x], PlatformTile) != True):
        #     pygame.mixer.Sound.play(assets.open_can)

    def pathfind(self):
        neighbors = get_neighbors(self.x, self.y, tile_map)
        valid_neighbors = []

        for neighbor in neighbors:
            if(isinstance(neighbor, AirTile) or isinstance(neighbor, RoadTile) or isinstance(neighbor, Farm) or isinstance(neighbor, Restricted)):
                if(isinstance(ground_tile_map[neighbor.y][neighbor.x], AirTile) != True):
                    valid_neighbors.append(neighbor)

        if(len(valid_neighbors) > 0):

            best_neighbor = valid_neighbors[0]
            for neighbor in valid_neighbors:
                if(pathfinding[neighbor.y][neighbor.x] != ' ' and pathfinding[best_neighbor.y][best_neighbor.x] != ' '):
                    if(pathfinding[neighbor.y][neighbor.x] > pathfinding[best_neighbor.y][best_neighbor.x]):
                        best_neighbor = neighbor
                    elif(pathfinding[neighbor.y][neighbor.x] == pathfinding[best_neighbor.y][best_neighbor.x]):
                        if(random.random() < 0.5):
                            best_neighbor = neighbor

            # if(isinstance(best_neighbor, RoadTile)):
            #     self.occupied_tile = RoadTile
            # else:
            #     self.occupied_tile = AirTile
            # tile_map[self.y][self.x] = self.occupied_tile(self.x, self.y)
            # self.x = best_neighbor.x
            # self.y = best_neighbor.y
            # tile_map[best_neighbor.y][best_neighbor.x] = self

            if(isinstance(self.occupied_tile, RoadTile)):
                tile_map[self.y][self.x] = self.occupied_tile
            else:
                tile_map[self.y][self.x] = AirTile(self.x, self.y)

            if(isinstance(tile_map[best_neighbor.y][best_neighbor.x], RoadTile)):
                self.occupied_tile = tile_map[best_neighbor.y][best_neighbor.x]
            else:
                self.occupied_tile = None

            # if self.occupied_tile is not None:
            #     tile_map[self.y][self.x] = self.occupied_tile

            # # Save the new tile you are stepping on
            # if(isinstance(tile_map[best_neighbor.y][best_neighbor.x], RoadTile)):
            #     tile_map[self.y][self.x] = self.occupied_tile
            # else:
            #     tile_map[self.y][self.x] = AirTile(self.x, self.y)

            # if isinstance(tile_map[best_neighbor.y][best_neighbor.x], RoadTile):
            #     self.occupied_tile = tile_map[best_neighbor.y][best_neighbor.x]
            # else:
            #     self.occupied_tile = None  # nothing to restore, gets replaced with AirTile

            # Put yourself on the tile_map
            self.x = best_neighbor.x
            self.y = best_neighbor.y
            tile_map[self.y][self.x] = self

    def move(self):

        neighbors = get_neighbors(self.x, self.y, tile_map)

        #print("Buildings: ", neighbors)

        valid_neighbors = []
        
        for neighbor in neighbors:

            if(isinstance(neighbor, AirTile) or isinstance(neighbor, RoadTile)):
                #print("ground_neighbor: ", ground_tile_map[neighbor.y][neighbor.x])
                if(isinstance(ground_tile_map[neighbor.y][neighbor.x], AirTile) != True):
                    valid_neighbors.append(neighbor)

            
        if(len(valid_neighbors) > 0):
            target = random.choice(valid_neighbors)

            if(isinstance(target, RoadTile)):
                tile_map[self.y][self.x] = RoadTile(self.x, self.y)
            else:
                tile_map[self.y][self.x] = AirTile(self.x, self.y)
            self.x = target.x
            self.y = target.y
            tile_map[target.y][target.x] = self

    def update(self):
        if(self.age > 0):
            self.pathfind()
        self.age += 1
        
nolat_platforms = []


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
        elif tiles2[y][x] == 'n':
            tile_row.append(Nolat(x, y))
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
        elif tiles_ground[y][x] == '#':
            platform = NolatPlatform(x, y)
            tile_row.append(platform)
            nolat_platforms.append(platform)
        else:
            tile_row.append(AirTile(x, y))
    ground_tile_map.append(tile_row)

