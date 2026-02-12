import pygame
import config
import os
import sys

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def renderText(surface, x, y, size, content, centered_x = 0, centered_y = 0, color=(255, 255, 255)):
    font = pygame.font.Font(resource_path('assets/pixel.ttf'), size)
    text = font.render(content, True, color)
    text_rect = text.get_rect()

    text_rect.x = x
    text_rect.y = y

    if(centered_x == 1):
        text_rect.x = x - (text_rect.width / 2)
    if(centered_y == 1):
        text_rect.y = y - (text_rect.height / 2)
        

    surface.blit(text, text_rect)
    

