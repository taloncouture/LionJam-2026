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
screen = pygame.display.set_mode((WIDTH, HEIGHT))


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
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', 'f', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'f', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

grass = pygame.image.load('grass.png')
grass = pygame.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

selector = pygame.image.load('selector.png')
selector = pygame.transform.scale(selector, (TILE_SIZE, TILE_SIZE))

boundingbox = pygame.image.load('boundingbox.png')
boundingbox = pygame.transform.scale(boundingbox, (TILE_SIZE, TILE_SIZE))

forest = pygame.image.load('forest.png')
forest = pygame.transform.scale(forest, (TILE_SIZE, TILE_SIZE))

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

        screen.fill((255, 255, 255))

        for y in range(len(tiles)):
            for x in range(len(tiles[y])):

                if (tiles[y][x] == '0'):
                    ix, iy = coords_to_iso(x, y)
                    screen.blit(grass, (ix, iy))

        for y in range(len(tiles2)):
            for x in range(len(tiles2[y])):

                if (tiles2[y][x] == 'b'):
                    ix, iy = coords_to_iso(x, y)
                    screen.blit(boundingbox, (ix, iy - HALF_W))

                if(tiles2[y][x] == 'f'):
                    ix, iy = coords_to_iso(x, y)
                    screen.blit(forest, (ix, iy - HALF_W))

        mx, my = pygame.mouse.get_pos()
        imx, imy = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
        if(imx < len(tiles[y]) and imy < len(tiles) and tiles[imy][imx] != ' '):
            screen.blit(selector, coords_to_iso(imx, imy))
    

        pygame.display.update()
        clock.tick(30)




if __name__ == "__main__":
    main()