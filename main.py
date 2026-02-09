import pygame
import math

pygame.init()

WIDTH = int (26 * 42)
HEIGHT = int (26 * 26)
SCALE_FACTOR = 3
TILE_SIZE = 26 * SCALE_FACTOR
HALF_W = 12 * SCALE_FACTOR
HALF_H = 6 * SCALE_FACTOR
ORIGIN_X = (WIDTH // 2) - (TILE_SIZE // 2)
ORIGIN_Y = HEIGHT // 4 - 100

clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
game_surface = pygame.Surface((WIDTH, HEIGHT))



tiles = [[' ', ' ', ' ', ' ', '0', '0', '0', '0', ' ', ' ', '0', '0', '0', ' ', ' '],
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
         [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
         [' ', '0', '0', '0', ' ', ' ', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
         [' ', ' ', '0', '0', ' ', '0', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', ' ', '0', ' ', ' ']]

tiles2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 't', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 'f', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

grass = pygame.image.load('grass.png')
grass = pygame.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

selector = pygame.image.load('selector.png')
selector = pygame.transform.scale(selector, (TILE_SIZE, TILE_SIZE))

boundingbox = pygame.image.load('boundingbox.png')
boundingbox = pygame.transform.scale(boundingbox, (TILE_SIZE, TILE_SIZE))

forest = pygame.image.load('forest.png')
forest = pygame.transform.scale(forest, (TILE_SIZE, TILE_SIZE))

factory = pygame.image.load('factory.png')
factory = pygame.transform.scale(factory, (TILE_SIZE, TILE_SIZE))

selected_x = 0
selected_y = 0


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

def coords_to_iso(x, y):

    iso_x = (x - y) * HALF_W
    iso_y = (x + y) * HALF_H

    return ORIGIN_X + iso_x, ORIGIN_Y + iso_y

def main():

    selected_x = 0
    selected_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                selected_x, selected_y = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)

    

        #main game loop

        screen.fill((207, 236, 255))
        game_surface.fill((207, 236, 255))
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):

                if (tiles[y][x] == '0'):
                    ix, iy = coords_to_iso(x, y)
                    game_surface.blit(grass, (ix, iy))

        for y in range(len(tiles2)):
            for x in range(len(tiles2[y])):

                if (tiles2[y][x] == 'b'):
                    ix, iy = coords_to_iso(x, y)
                    game_surface.blit(boundingbox, (ix, iy - HALF_W - SCALE_FACTOR))

                if(tiles2[y][x] == 'f'):
                    ix, iy = coords_to_iso(x, y)
                    game_surface.blit(factory, (ix, iy - HALF_W - SCALE_FACTOR))
                if(tiles2[y][x] == 't'):
                    ix, iy = coords_to_iso(x, y)
                    game_surface.blit(forest, (ix, iy - HALF_W - SCALE_FACTOR))
                

        win_w, win_h = screen.get_size()
        scale = min(win_w / WIDTH, win_h / HEIGHT)
        scaled_w, scaled_h = int(WIDTH * scale), int(HEIGHT * scale)
        x = (win_w - scaled_w) // 2
        y = (win_h - scaled_h) // 2

        mx, my = pygame.mouse.get_pos()

        mx = (mx - x) / scale
        my = (my - y) / scale

        imx, imy = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        if(0 <= imy < len(tiles) and 0 <= imx < len(tiles[imy]) and tiles[imy][imx] != ' '):
            game_surface.blit(selector, coords_to_iso(imx, imy))

        #screen.fill((0, 0, 0))  # black bars
        screen.blit(pygame.transform.smoothscale(game_surface, (scaled_w, scaled_h)), (x, y))

        #screen.blit(game_surface, (0, 0))
        pygame.display.update()
        clock.tick(30)




if __name__ == "__main__":
    main()