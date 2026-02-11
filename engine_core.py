from config import *
import pygame

class Engine:
    def __init__(self, surface):
        self.mouse_x = 0
        self.mouse_y = 0
        self.scale = 1
        self.offset_x = 0
        self.offset_y = 0
        self.scaled_w, self.scaled_h = 0, 0

        self.surface = surface

        #self.selected_item = None


    def update(self, screen):
        win_w, win_h = screen.get_size()
        scale = min(win_w / WIDTH, win_h / HEIGHT)
        self.scaled_w, self.scaled_h = int(WIDTH * scale), int(HEIGHT * scale)
        self.offset_x = (win_w - self.scaled_w) // 2
        self.offset_y = (win_h - self.scaled_h) // 2
        mx, my = pygame.mouse.get_pos()
        self.mouse_x = (mx - self.offset_x) / scale
        self.mouse_y = (my - self.offset_y) / scale

    def render(self, image, x, y):
        self.surface.blit(image, (x, y))
