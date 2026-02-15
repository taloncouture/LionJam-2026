import tiles
import pygame
from config import *
import math
import assets
import graphics
import items

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

class State:
    def __init__(self, engine, gameContext):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def on_click(self):
        pass

    def on_close(self):
        pass

    def on_open(self):
        pass

class EndState(State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext

        self.text_y = HEIGHT

    def render(self, screen, surface):

        # screen.fill((102, 197, 255))
        # surface.fill((102, 197, 255))
        screen.fill((0, 0, 0))
        surface.fill((255, 243, 193))


        if(self.gameContext.lives <= 0):
            graphics.renderText(surface, WIDTH / 2, self.text_y, 100, "Game Over", 1, 0, (178, 0, 0))
        else:
            graphics.renderText(surface, WIDTH / 2, self.text_y - 100, 100, "You have made", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, self.text_y, 100, "King Pizza proud", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 300, 50, f"Turns: {self.gameContext.turn}", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 400, 50, f"Pizzas Cooked: {self.gameContext.bricks}", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 550, 25, "Created by Talon Couture", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 620, 25, "Art by Talon Couture", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 690, 25, "Sounds from Pixabay.com", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 760, 25, "Music: Kawai Kitsune by Kevin MacLeod", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, self.text_y + 850, 60, "Thanks For Playing!", 1, 0, (178, 0, 0))
        
        surface.blit(assets.talon, (WIDTH / 2 - assets.talon.get_width() / 2, self.text_y + 3000))
        

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))

        

    def update(self):
        if(self.text_y > -10000):
            self.text_y -= 1.2

class TitleState(State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext

    def render(self, screen, surface):
        screen.fill((0, 0, 0))
        surface.fill((255, 243, 193))

        graphics.renderText(surface, WIDTH / 2, HEIGHT / 2, 60, "Great Pyramid of", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, HEIGHT / 2 + 60, 140, "PIZZA", 1, 0, (178, 0, 0))
        graphics.renderText(surface, WIDTH / 2, HEIGHT - (HEIGHT / 7), 20, "press space to start", 1, 0, (178, 0, 0))

        surface.blit(assets.pyramid_icon, (WIDTH / 2 - assets.pyramid_icon.get_width() / 2, HEIGHT / 20))

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))

class InstructionState(State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext

        self.pages = 10
        self.current_page = 0

        self.text_size = 25

    def render(self, screen, surface):
        # screen.fill((0, 0, 0))
        # surface.fill((255, 243, 193))

        surface.blit(assets.instructions_background, ((WIDTH / 2) - (assets.instructions_background.get_width() / 2), HEIGHT - (HEIGHT / 2)))
        graphics.renderText(surface, WIDTH / 2, HEIGHT / 2 + PADDING * 3, 45, "Instructions", 1, 0, (178, 0, 0))

        if(self.current_page == 0):
            
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "Press space to open and close the shop and use", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "your credits to buy tiles or items.", 1, 0, (178, 0, 0))

        if(self.current_page == 1):

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "Tiles must be placed adjacent to each other", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "and starting from the Pyramid construction site.", 1, 0, (178, 0, 0))

        if(self.current_page == 2):

            surface.blit(assets.road, ((WIDTH / 2) - (TILE_SIZE / 2), HEIGHT - 50 - 50 - 50 - TILE_SIZE))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "Place roads to connect tiles to each other.", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "Corner connections do not count.", 1, 0, (178, 0, 0))

        if(self.current_page == 3):

            surface.blit(assets.pizzeria, ((WIDTH / 2) - TILE_SIZE - (PADDING * 3), HEIGHT - 50 - 50 - 50 - TILE_SIZE))
            surface.blit(assets.factory_1, ((WIDTH / 2) + (PADDING * 3), HEIGHT - 50 - 50 - 50 - TILE_SIZE))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "Production tiles will need to be connected to farms", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "to produce pizza.", 1, 0, (178, 0, 0))

        if(self.current_page == 4):

            surface.blit(assets.next_turn, ((WIDTH / 2) - (ITEM_WIDTH / 2), HEIGHT - 50 - 50 - 50 - ITEM_HEIGHT))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "When you are done placing tiles, click the", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "next turn button", 1, 0, (178, 0, 0))

        if(self.current_page == 5):

            surface.blit(assets.cheese, ((WIDTH / 2) - (TILE_SIZE / 2), HEIGHT - 50 - 50 - 50 - TILE_SIZE))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "At the beginning of each turn, credits will be given", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "based on the number and type of buildings and...", 1, 0, (178, 0, 0))

        if(self.current_page == 6):

            surface.blit(assets.pizza, ((WIDTH / 2) - (TILE_SIZE / 2), HEIGHT - 50 - 50 - 50 - TILE_SIZE))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "...pizza can be collected to build the pyramid.", 1, 0, (178, 0, 0))

        if(self.current_page == 7):

            surface.blit(assets.nolat_platform, ((WIDTH / 2) - TILE_SIZE - (PADDING * 3), HEIGHT - 50 - 50 - 25 - TILE_SIZE))
            surface.blit(assets.nolat_2, ((WIDTH / 2) + (PADDING * 3), HEIGHT - 50 - 50 - 50 - TILE_SIZE))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "Nolats may spawn on one of the purple platforms,", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "and will go toward the Pyramid.", 1, 0, (178, 0, 0))

        if(self.current_page == 8):

            surface.blit(assets.redbull, ((WIDTH / 2) - (TILE_SIZE / 2), HEIGHT - 50 - 50 - 50 - TILE_SIZE))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "You should try to stop them if you can,", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "and you can do so by giving them an energy drink.", 1, 0, (178, 0, 0))

        if(self.current_page == 9):

            surface.blit(assets.heart, ((WIDTH / 2) - (TILE_SIZE / 2), HEIGHT - 50 - 50 - 50 - TILE_SIZE))

            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50 - 50, self.text_size, "You have three lives, and each time a Nolat", 1, 0, (178, 0, 0))
            graphics.renderText(surface, WIDTH / 2, HEIGHT - 50, self.text_size, "reaches the Pyramid, then you lose one.", 1, 0, (178, 0, 0))
            

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))

    def on_click(self):
        pass

    def on_press(self):
        self.current_page += 1
        pygame.mixer.Sound.play(assets.click)



class IntroductionState(State):
    def __init__(self, engine, gameContext):
        super().__init__(engine, gameContext)
        self.engine = engine
        self.gameContext = gameContext

        self.text_y = HEIGHT

        self.finished = False
        self.alpha = 255
        self.fade_surface = pygame.Surface((WIDTH, HEIGHT))
        self.fade_surface.fill((0, 0, 0))
        self.fade_surface.set_alpha(self.alpha)

        self.played = False

    def render(self, screen, surface):

        # screen.fill((102, 197, 255))
        # surface.fill((102, 197, 255))
        screen.fill((0, 0, 0))
        surface.fill((0, 0, 0))


        graphics.renderText(surface, WIDTH / 2, self.text_y, 30, "In a world... with oceans made of cheese...", 1, 0)
        graphics.renderText(surface, WIDTH / 2, self.text_y + 100, 30, "...and land made of pizza dough...", 1, 0)
        graphics.renderText(surface, WIDTH / 2, self.text_y + 300, 30, "...King Pizza has commanded you to build a Great Pyramid.", 1, 0)

        if(self.text_y < -400):
            scaled_kingpizza = pygame.transform.scale(assets.mrpizza, (TILE_SIZE * 3, TILE_SIZE * 3))
            surface.blit(scaled_kingpizza, ((WIDTH / 2) - (scaled_kingpizza.get_width() / 2), (HEIGHT / 2) - (scaled_kingpizza.get_height() / 2)))

        screen.blit(pygame.transform.smoothscale(surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))

        if(self.text_y < -400):
            screen.blit(pygame.transform.smoothscale(self.fade_surface, (self.engine.scaled_w, self.engine.scaled_h)), (self.engine.offset_x, self.engine.offset_y))

        

    def update(self):
        if(self.text_y > -1000):
            self.text_y -= 1.5

        if(self.text_y < -400 and self.text_y > -500):
            self.alpha -= 3
            if(self.alpha < 0):
                self.alpha = 0

        if(self.text_y < -450):
            if(self.played == False):
                pygame.mixer.Sound.play(assets.laugh)
                self.played = True

        if(self.text_y < -550):
            self.alpha += 3
            if(self.alpha > 255):
                self.alpha = 255

        if(self.text_y < -700):
            self.finished = True

        self.fade_surface.set_alpha(self.alpha)


    




