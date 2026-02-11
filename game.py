import items
import assets
from config import *
import tiles
import states
import graphics
import pygame

class GameState(states.State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext

        self.next_turn_button = items.Button(assets.next_turn, WIDTH - (16 * SCALE_FACTOR) - PADDING, HEIGHT - (16 * SCALE_FACTOR) - PADDING, self.engine)


    def place_item(self, x, y):
        if(0 <= y < len(tiles.tile_map) and 0 <= x < len(tiles.tile_map[y])):
            if(tiles.place_tile(x, y, self.gameContext.selected_item.tile)):
                self.gameContext.selected_item = None
                return True
        return False
    
    def next_turn(self):
        self.gameContext.turn += 1

        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                tiles.tile_map[y][x].update()
                if(type(tiles.tile_map[y][x]) is tiles.FactoryTile and tiles.tile_map[y][x].has_item == True):
                    tx, ty = tiles.coords_to_iso(x, y)
                    self.engine.render(assets.pizza, tx, ty - TILE_SIZE)
                    #print("pizza!")

    def on_click(self):
        mx = self.engine.mouse_x
        my = self.engine.mouse_y
        selected_x, selected_y = states.screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)

        if(self.gameContext.selected_item != None and self.gameContext.selected_item.cost <= self.gameContext.credits):
            cost = self.gameContext.selected_item.cost
            if(self.place_item(selected_x, selected_y)):
                self.gameContext.credits -= cost

        elif(self.next_turn_button.selected == True):
            self.next_turn_button.selected = False
            self.next_turn()
        
        else:
            if(0 <= selected_y <= len(tiles.tile_map) and 0 <= selected_x <= len(tiles.tile_map[selected_y])):
                tiles.tile_map[selected_y][selected_x].on_click()
        

    def update(self):
        pass

    def render(self, screen, surface):

        # screen.fill((186, 246, 255))
        # surface.fill((186, 246, 255))
        screen.fill((102, 197, 255))
        surface.fill((102, 197, 255))
        # screen.fill((0, 0, 0))
        # surface.fill((0, 0, 0))

        for y in range(len(tiles.ground_tile_map)):
            for x in range(len(tiles.ground_tile_map[y])):
                tiles.ground_tile_map[y][x].render(surface)

        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                if(tiles.tile_map[y][x] != None):
                    tiles.tile_map[y][x].render(surface)

                    if(isinstance(tiles.tile_map[y][x], tiles.ProductionTile) and tiles.tile_map[y][x].has_item):
                        ix, iy = tiles.coords_to_iso(x, y)
                        surface.blit(assets.pizza, (ix, iy - TILE_SIZE))

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
        graphics.renderText(surface, PADDING * 8.2, (PADDING * 4), 24, f'x{self.gameContext.credits}', 0, 1)
        
        
        graphics.renderText(surface, PADDING, HEIGHT - PADDING * 5, 24, f"Turn: {self.gameContext.turn}")
        
        self.next_turn_button.update()
        self.next_turn_button.render()

        #selector
        imx, imy = states.screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        if(0 <= imy < len(tiles.tiles_ground) and 0 <= imx < len(tiles.tiles_ground[imy]) and tiles.tiles_ground[imy][imx] != ' '):
            surface.blit(assets.selector, tiles.coords_to_iso(imx, imy))
        #selector

        screen.blit(pygame.transform.smoothscale(surface, (scaled_w, scaled_h)), (x, y))