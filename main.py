import pygame
import math
import tiles
from tiles import FactoryTile
from tiles import ForestTile
import assets
from config import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
game_surface = pygame.Surface((WIDTH, HEIGHT))



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
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', '!', '~', '~', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', '~', '~', '~', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', '~', '~', '~', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


selected_x = 0
selected_y = 0


#very temporary, will use objects soon
def place_tile(x, y):

    if(0 <= y < len(tiles_ground) and 0 <= x < len(tiles_ground[y]) and tiles_ground[y][x] == '0' and tiles2[y][x] == ' '):
        tiles2[y][x] = 'f'
        return True
    return False


# I have no idea why this actually works now lol DO NOT CHANGE
def screen_to_iso(mx, my, origin_x, origin_y):

    mx -= origin_x
    my -= origin_y

    mx -= HALF_W
    my -= HALF_H

    dx = mx / HALF_W
    dy = my / HALF_H

    x = (dx + dy) / 2
    y = (dy - dx) / 2

    return math.floor(x + 0.5), math.floor(y + 0.5)

def window_to_game(mx, my):
    win_w, win_h = screen.get_size()
    scale = min(win_w / WIDTH, win_h / HEIGHT)
    x = (win_w - int(WIDTH * scale)) // 2
    y = (win_h - int(HEIGHT * scale)) // 2
    return (mx - x) / scale, (my - y) / scale

tile_map = []

for y in range(len(tiles2)):
    for x in range(len(tiles2[y])):
        if tiles2[y][x] == 'f':
            tile = FactoryTile(x, y)
            tile_map.append(tile)

        if tiles2[y][x] == 't':
            tile = ForestTile(x, y)
            tile_map.append(tile)

def main():

    selected_x = 0
    selected_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx, my = window_to_game(mx, my)
                selected_x, selected_y = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
                place_tile(selected_x, selected_y)

                for tile in tile_map:
                    if (tile.x == selected_x and tile.y == selected_y):
                        tile.on_click()

    

        #main game loop

        screen.fill((207, 236, 255))
        game_surface.fill((207, 236, 255))
        for y in range(len(tiles_ground)):
            for x in range(len(tiles_ground[y])):

                if (tiles_ground[y][x] == '0'):
                    ix, iy = tiles.coords_to_iso(x, y)
                    game_surface.blit(assets.grass, (ix, iy))

        # for y in range(len(tiles2)):
        #     for x in range(len(tiles2[y])):

        #         if (tiles2[y][x] == 'b'):
        #             ix, iy = tiles.coords_to_iso(x, y)
        #             game_surface.blit(assets.boundingbox, (ix, iy - HALF_W - SCALE_FACTOR))

        #         if(tiles2[y][x] == 'f'):
        #             ix, iy = tiles.coords_to_iso(x, y)
        #             game_surface.blit(assets.factory, (ix, iy - HALF_W - SCALE_FACTOR))
        #         if(tiles2[y][x] == 't'):
        #             ix, iy = tiles.coords_to_iso(x, y)
        #             game_surface.blit(assets.forest, (ix, iy - HALF_W - SCALE_FACTOR))

        #         if(tiles2[y][x] == '@'):
        #             ix, iy = tiles.coords_to_iso(x, y)
        #             game_surface.blit(assets.mrpizza, (ix, iy - HALF_W - SCALE_FACTOR))

        #         if(tiles2[y][x] == '!'):
        #             ix, iy = tiles.coords_to_iso(x, y)
        #             game_surface.blit(assets.pyramid, (ix - (HALF_W * (2)) - SCALE_FACTOR * 2, iy - (HALF_H * (5)) - HALF_W + SCALE_FACTOR))
                
        for tile in tile_map:
            tile.render(game_surface)


        win_w, win_h = screen.get_size()
        scale = min(win_w / WIDTH, win_h / HEIGHT)
        scaled_w, scaled_h = int(WIDTH * scale), int(HEIGHT * scale)
        x = (win_w - scaled_w) // 2
        y = (win_h - scaled_h) // 2

        mx, my = pygame.mouse.get_pos()

        mx = (mx - x) / scale
        my = (my - y) / scale

        imx, imy = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        if(0 <= imy < len(tiles_ground) and 0 <= imx < len(tiles_ground[imy]) and tiles_ground[imy][imx] != ' '):
            game_surface.blit(assets.selector, tiles.coords_to_iso(imx, imy))

        #screen.fill((0, 0, 0))  # black bars
        screen.blit(pygame.transform.smoothscale(game_surface, (scaled_w, scaled_h)), (x, y))

        #screen.blit(game_surface, (0, 0))
        pygame.display.update()
        clock.tick(30)




if __name__ == "__main__":
    main()