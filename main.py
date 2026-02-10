import pygame
import math
import tiles
import assets
from config import *
import states

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
game_surface = pygame.Surface((WIDTH, HEIGHT))


# I have no idea why this actually works now lol DO NOT CHANGE


def window_to_game(mx, my):
    win_w, win_h = screen.get_size()
    scale = min(win_w / WIDTH, win_h / HEIGHT)
    x = (win_w - int(WIDTH * scale)) // 2
    y = (win_h - int(HEIGHT * scale)) // 2
    return (mx - x) / scale, (my - y) / scale

def main():

    selected_x = 0
    selected_y = 0

    gameState = states.GameState()
    currentState = gameState

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx, my = window_to_game(mx, my)
                selected_x, selected_y = states.screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y)
                print(selected_x, selected_y)

                for y in range(len(tiles.tile_map)):
                    for x in range(len(tiles.tile_map[y])):
                        if(tiles.tile_map[y][x].x == selected_x and tiles.tile_map[y][x].y == selected_y):
                            tiles.tile_map[y][x].on_click()

    

        #main game loop

        #loop goes here
        currentState.update()
        currentState.render(screen, game_surface)



        
        #general rendering
        
        pygame.display.update()
        clock.tick(30)




if __name__ == "__main__":
    main()