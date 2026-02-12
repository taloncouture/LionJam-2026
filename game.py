import items
import assets
from config import *
import tiles
import states
import graphics
import pygame
from collections import deque

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None 

class GameState(states.State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext
        self.built = False

        self.roads = []

        self.next_turn_button = items.Button(assets.next_turn, WIDTH - (16 * SCALE_FACTOR) - PADDING, HEIGHT - (16 * SCALE_FACTOR) - PADDING, self.engine)

        self.fade_surface = pygame.Surface((WIDTH, HEIGHT))
        self.fade_surface.fill((0, 0, 0))
        self.fade_surface.set_alpha(0)
        self.fade_alpha = 255
        self.fade_speed = 10

        self.game_finished = False

    
    # cool algorithm i found
    def generate_connected_tiles(self, start, tilemap):
        visited = set()
        queue = deque([start])
        collected = set()

        while queue:
            x, y = queue.popleft()

            if(x, y) in visited:
                continue

            visited.add((x, y))
            collected.add((x, y))

            for tile in tiles.get_neighbors(x, y, tilemap):
                if tile is None:
                    continue

                if(isinstance(tile, tiles.RoadTile)):
                    queue.append((tile.x, tile.y))
                else:
                    collected.add((tile.x, tile.y))

        return collected
    
    # function of insanity
    def update_connections(self, tile, claim=True):

        if not tile.required_connections:
            return
        
        neighbors = tiles.get_neighbors(tile.x, tile.y, tiles.tile_map)
        connected_tiles = set()
        for neighbor in neighbors:
            if(neighbor and isinstance(neighbor, tiles.RoadTile)):
                connected_tiles.update(self.generate_connected_tiles((neighbor.x, neighbor.y), tiles.tile_map))

        if not hasattr(tile, 'connected_tiles'):
            tile.connected_tiles = {}

        for required_type in tile.required_connections:

            if(required_type not in tile.connected_tiles):
                tile.connected_tiles[required_type] = set()

            #tile.connected_tiles.setdefault(cls, set())

        for tx, ty in connected_tiles:
            t = tiles.tile_map[ty][tx]
            
            for required_class, required_count in tile.required_connections.items():

                if len(tile.connected_tiles[required_class]) >= required_count:
                    #print("fulfilled")
                    continue

                if(isinstance(t, required_class)):

                    if getattr(t, 'claimed', None) in (None, tile):
                        tile.connected_tiles[required_class].add(t)


        requirements_met = all(len(tile.connected_tiles[t_type]) >= count for t_type, count in tile.required_connections.items())


        tile.requirements_met = requirements_met

        if(requirements_met):
            for required_type, required_count in tile.required_connections.items():

                owned_count = sum(1 for t in tile.connected_tiles[required_type] if t.claimed is tile)

                to_claim_count = required_count - owned_count

                for t in tile.connected_tiles[required_type]:
                    if(to_claim_count <= 0):
                        break
                    
                    if(claim and getattr(t, "claimable", False) and getattr(t, 'claimed', None) in (None, tile)):
                        t.claimed = tile
                        to_claim_count -= 1

        if requirements_met:
            #print(f"{type(tile).__name__} at {(tile.x, tile.y)} requirements met!")
            if(not tile.requirements_met):
                tile.requirements_met = True


    def place_item(self, x, y):
        if(0 <= y < len(tiles.tile_map) and 0 <= x < len(tiles.tile_map[y])):

            if(tiles.place_tile(x, y, self.gameContext.selected_item.tile, tiles.tile_map)):
                self.gameContext.selected_item = None

                for y in range(len(tiles.tile_map)):
                    for x in range(len(tiles.tile_map[y])):
                        tile = tiles.tile_map[y][x]
                        if tile and tile.required_connections:
                            self.update_connections(tile, claim=False)

                for y in range(len(tiles.tile_map)):
                    for x in range(len(tiles.tile_map[y])):
                        tile = tiles.tile_map[y][x]
                        if tile and tile.required_connections:
                            self.update_connections(tile, claim=True)

                    
                return True
        return False
    
    def next_turn(self):

        if(self.gameContext.built):
            self.game_finished = True
            return

        self.gameContext.turn += 1

        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                
                self.gameContext.credits += tiles.tile_map[y][x].credits_produced

                tiles.tile_map[y][x].update()
                # if(type(tiles.tile_map[y][x]) == tiles.FactoryTile and tiles.tile_map[y][x].has_item == True):
                #     tx, ty = tiles.coords_to_iso(x, y)
                #     self.engine.render(assets.pizza, tx, ty - TILE_SIZE)
                    #print("pizza!")



    def on_click(self):
        mx = self.engine.mouse_x
        my = self.engine.mouse_y
        selected_x, selected_y = states.screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)

        if(self.gameContext.selected_item != None and self.gameContext.selected_item.cost <= self.gameContext.credits):
            cost = self.gameContext.selected_item.cost

            if(isinstance(self.gameContext.selected_item, items.DestructionItem)):
                if(tiles.is_valid(selected_x, selected_y, tiles.tile_map) and isinstance(tiles.tile_map[selected_y][selected_x], self.gameContext.selected_item.targets)):
                    tiles.destroy_tile(selected_x, selected_y, tiles.tile_map)
                    self.gameContext.credits -= cost


            elif(self.place_item(selected_x, selected_y)):
                self.gameContext.credits -= cost

        elif(self.next_turn_button.selected == True):
            self.next_turn_button.selected = False
            self.next_turn()
        
        if(0 <= selected_y < len(tiles.tile_map) and 0 <= selected_x < len(tiles.tile_map[selected_y])):
            if(isinstance(tiles.tile_map[selected_y][selected_x], tiles.ProductionTile)):
                if(tiles.tile_map[selected_y][selected_x].collect()):
                    self.gameContext.bricks += tiles.tile_map[selected_y][selected_x].production_quantity
                    print(self.gameContext.bricks)
                        #print(self.gameContext.bricks)
        

    def update(self):

        if self.fade_alpha > 0:
            self.fade_alpha -= self.fade_speed
            if self.fade_alpha < 0:
                self.fade_alpha = 0
        self.fade_surface.set_alpha(self.fade_alpha)


        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                
                
                if(isinstance(tiles.tile_map[y][x], tiles.Pyramid)):

                    pyramid = tiles.tile_map[y][x]
                    if(self.gameContext.pyramid_stage >= len(pyramid.stages) - 1):
                        self.built = True
                        self.gameContext.built = True
                    else:
                        next_stage = self.gameContext.pyramid_stage + 1

                        if(self.gameContext.bricks >= self.gameContext.required_bricks[next_stage]):
                            self.gameContext.pyramid_stage = next_stage
                            pyramid.stage = next_stage
                            self.built = True
                            #self.gameContext.built = True

        

    def render(self, screen, surface):

        # screen.fill((186, 246, 255))
        # surface.fill((186, 246, 255))
        #screen.fill((102, 197, 255))
        # surface.fill((102, 197, 255))
        # screen.fill((0, 0, 0))
        # surface.fill((0, 0, 0))
        screen.fill((0, 0, 0))
        surface.fill((255, 243, 193))
        

        for y in range(len(tiles.ground_tile_map)):
            for x in range(len(tiles.ground_tile_map[y])):
                tiles.ground_tile_map[y][x].render(surface)

        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                if(tiles.tile_map[y][x] != None):

                    tiles.tile_map[y][x].animate()

                    tiles.tile_map[y][x].render(surface)

                    if(isinstance(tiles.tile_map[y][x], tiles.ProductionTile) and tiles.tile_map[y][x].has_item):
                        ix, iy = tiles.coords_to_iso(x, y)
                        surface.blit(tiles.tile_map[y][x].resource.image, (ix, iy - TILE_SIZE))

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

        surface.blit(assets.cheese, (PADDING, 0))
        graphics.renderText(surface, PADDING * 8.2, (PADDING * 4), 24, f'x{self.gameContext.credits}', 0, 1, (178, 0, 0))
        
        
        graphics.renderText(surface, PADDING, HEIGHT - PADDING * 5, 24, f"Turn: {self.gameContext.turn}", 0, 0, (178, 0, 0))
        
        self.next_turn_button.update()
        self.next_turn_button.render()

        #selector
        imx, imy = states.screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        if(0 <= imy < len(tiles.tiles_ground) and 0 <= imx < len(tiles.tiles_ground[imy]) and tiles.tiles_ground[imy][imx] != ' '):
            tx, ty = tiles.coords_to_iso(imx, imy)
            surface.blit(assets.selector, (tx, ty))

            tile = tiles.tile_map[imy][imx]

            if(not isinstance(tile, tiles.AirTile) and not isinstance(tile, tiles.ForestTile) and not isinstance(tile, tiles.Restricted)):
                graphics.renderText(surface, tx + (TILE_SIZE / 2), ty + (TILE_SIZE / 2), 25, f"Producing Credits: {tile.credits_produced}", 1, 0, (178, 0, 0))
                if(isinstance(tile, tiles.ProductionTile)):
                    graphics.renderText(surface, tx + (TILE_SIZE / 2), ty + (TILE_SIZE / 2) + PADDING * 3, 25, f"Requirements Met: {tile.requirements_met}", 1, 0, (178, 0, 0))
        #selector





        screen.blit(pygame.transform.smoothscale(surface, (scaled_w, scaled_h)), (x, y))

        scaled_fade = pygame.transform.smoothscale(self.fade_surface, (self.engine.scaled_w, self.engine.scaled_h))
        screen.blit(scaled_fade, (self.engine.offset_x, self.engine.offset_y))