import pygame
import math
import tiles
import assets
from config import *
import states
import engine_core
import shop
import context
import game
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
game_surface = pygame.Surface((WIDTH, HEIGHT))

pygame.display.set_caption("Great Pyramid of Pizza")

mixer.init()

# I have no idea why this actually works now lol DO NOT CHANGE


def window_to_game(mx, my):
    win_w, win_h = screen.get_size()
    scale = min(win_w / WIDTH, win_h / HEIGHT)
    x = (win_w - int(WIDTH * scale)) // 2
    y = (win_h - int(HEIGHT * scale)) // 2
    return (mx - x) / scale, (my - y) / scale



def main():

    engine = engine_core.Engine(game_surface, screen)
    gameContext = context.GameContext()

    gameState = game.GameState(engine, gameContext)
    shopState = shop.ShopState(engine, gameContext)
    endState = states.EndState(engine, gameContext)
    titleState = states.TitleState(engine, gameContext)
    instructionState = states.InstructionState(engine, gameContext)
    introState = states.IntroductionState(engine, gameContext)
    currentState = instructionState

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                currentState.on_click()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    if(currentState == titleState):
                        currentState = introState
                        pygame.mixer.Sound.play(assets.click)

                    if(currentState == instructionState):
                        instructionState.on_press()
                        
                    if(currentState == instructionState and currentState.current_page >= currentState.pages):
                        currentState = gameState

                    elif currentState == shopState:
                        currentState.on_close()
                        currentState = gameState
                        pygame.mixer.Sound.play(assets.click)
                    elif currentState == gameState:
                        currentState.on_close()
                        currentState = shopState
                        pygame.mixer.Sound.play(assets.click)

    
        if((currentState == gameState and gameState.game_finished) or (currentState == gameState and gameContext.lives <= 0)):
            currentState = endState

        if(currentState == introState and currentState.finished == True):
            currentState = instructionState
            gamemusic = mixer.music.load(assets.resource_path('assets/kitsune.mp3'))
            mixer.music.set_volume(0.1)
            mixer.music.play(-1)


        #main game loop

        engine.update()

        if(currentState == instructionState or currentState == shopState):
            gameState.render(screen, game_surface)

        #loop goes here
        currentState.update()
        currentState.render(screen, game_surface)



        
        #general rendering
        
        pygame.display.update()
        clock.tick(30)




if __name__ == "__main__":
    main()