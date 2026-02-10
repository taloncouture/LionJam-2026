import pygame
import math
import tiles
import assets
from config import *
import states
import engine_core

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

    engine = engine_core.Engine()

    gameState = states.GameState(engine)
    inventoryState = states.InventoryState(engine)
    currentState = gameState

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
               currentState.on_click()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if currentState == inventoryState:
                        currentState = gameState
                    elif currentState == gameState:
                        currentState = inventoryState

    

        #main game loop

        engine.update(screen)

        #loop goes here
        currentState.update()
        currentState.render(screen, game_surface)



        
        #general rendering
        
        pygame.display.update()
        clock.tick(30)




if __name__ == "__main__":
    main()