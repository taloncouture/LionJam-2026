import pygame
from config import *

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

pyramid = pygame.image.load('pyramid.png')
pyramid = pygame.transform.scale(pyramid, (TILE_SIZE * 3, TILE_SIZE * 3))

mrpizza = pygame.image.load('mrpizza.png')
mrpizza = pygame.transform.scale(mrpizza, (TILE_SIZE, TILE_SIZE))