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
            if(tiles.place_tile(x, y, self.gameContext.selected_item)):
                self.gameContext.selected_item = None
                return True
        return False
    
    def next_turn(self):
        self.gameContext.turn += 1
        #produce items

    def on_click(self):
        mx = self.engine.mouse_x
        my = self.engine.mouse_y
        selected_x, selected_y = states.screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)

        if(self.gameContext.selected_item != None):

            self.place_item(selected_x, selected_y)

        if(self.next_turn_button.selected == True):
            self.next_turn_button.selected = False
            self.next_turn()

    def update(self):
        pass

    def render(self, screen, surface):

        # screen.fill((186, 246, 255))
        # surface.fill((186, 246, 255))
        screen.fill((102, 197, 255))
        surface.fill((102, 197, 255))

        for y in range(len(tiles.ground_tile_map)):
            for x in range(len(tiles.ground_tile_map[y])):
                tiles.ground_tile_map[y][x].render(surface)

        for y in range(len(tiles.tile_map)):
            for x in range(len(tiles.tile_map[y])):
                if(tiles.tile_map[y][x] != None):
                    tiles.tile_map[y][x].render(surface)

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

        graphics.renderText(surface, PADDING, PADDING, 24, "Credits: 67")
        graphics.renderText(surface, WIDTH / 2, PADDING, 24, f"Turn: {self.gameContext.turn}", 1)
        
        self.next_turn_button.update()
        self.next_turn_button.render()

        #selector
        imx, imy = states.screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        if(0 <= imy < len(tiles.tiles_ground) and 0 <= imx < len(tiles.tiles_ground[imy]) and tiles.tiles_ground[imy][imx] != ' '):
            surface.blit(assets.selector, tiles.coords_to_iso(imx, imy))
        #selector

        screen.blit(pygame.transform.smoothscale(surface, (scaled_w, scaled_h)), (x, y))