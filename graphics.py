import pygame
import config

pygame.init()

def renderText(surface, x, y, size, content, centered_x = 0, centered_y = 0):
    font = pygame.font.Font('assets/pixel.ttf', size)
    text = font.render(content, True, (255, 255, 255))
    text_rect = text.get_rect()

    text_rect.x = x
    text_rect.y = y

    if(centered_x == 1):
        text_rect.x = x - (text_rect.width / 2)
    if(centered_y == 1):
        text_rect.y = y - (text_rect.height / 2)
        

    surface.blit(text, text_rect)

