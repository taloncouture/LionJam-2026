import pygame
from config import *

grass = pygame.image.load('assets/grass.png')
grass = pygame.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

selector = pygame.image.load('assets/selector.png')
selector = pygame.transform.scale(selector, (TILE_SIZE, TILE_SIZE))

boundingbox = pygame.image.load('assets/boundingbox.png')
boundingbox = pygame.transform.scale(boundingbox, (TILE_SIZE, TILE_SIZE))

forest = pygame.image.load('assets/forest.png')
forest = pygame.transform.scale(forest, (TILE_SIZE, TILE_SIZE))

factory = pygame.image.load('assets/factory.png')
factory = pygame.transform.scale(factory, (TILE_SIZE, TILE_SIZE))

pyramid = pygame.image.load('assets/pyramid.png')
pyramid = pygame.transform.scale(pyramid, (TILE_SIZE * 3, TILE_SIZE * 3))

mrpizza = pygame.image.load('assets/mrpizza.png')
mrpizza = pygame.transform.scale(mrpizza, (TILE_SIZE, TILE_SIZE))