import pygame
from config import *
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

grass = pygame.image.load(resource_path('assets/grass.png'))
grass = pygame.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

selector = pygame.image.load(resource_path('assets/selector.png'))
selector = pygame.transform.scale(selector, (TILE_SIZE, TILE_SIZE))

boundingbox = pygame.image.load(resource_path('assets/boundingbox.png'))
boundingbox = pygame.transform.scale(boundingbox, (TILE_SIZE, TILE_SIZE))

forest = pygame.image.load(resource_path('assets/forest.png'))
forest = pygame.transform.scale(forest, (TILE_SIZE, TILE_SIZE))

factory = pygame.image.load(resource_path('assets/factory.png'))
factory = pygame.transform.scale(factory, (TILE_SIZE, TILE_SIZE))

pyramid = pygame.image.load(resource_path('assets/pyramid.png'))
pyramid = pygame.transform.scale(pyramid, (TILE_SIZE * 3, TILE_SIZE * 3))

mrpizza = pygame.image.load(resource_path('assets/mrpizza.png'))
mrpizza = pygame.transform.scale(mrpizza, (TILE_SIZE, TILE_SIZE))

inventory = pygame.image.load(resource_path('assets/inventory2.png'))
inventory = pygame.transform.scale(inventory, (128 * SCALE_FACTOR, 64 * SCALE_FACTOR))

inventory_selector = pygame.image.load(resource_path('assets/inventory_selector.png'))
inventory_selector = pygame.transform.scale(inventory_selector, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

critics = pygame.image.load(resource_path('assets/critics.png'))
critics = pygame.transform.scale(critics, (TILE_SIZE, TILE_SIZE))

farm = pygame.image.load(resource_path('assets/farm.png'))
farm = pygame.transform.scale(farm, (TILE_SIZE, TILE_SIZE))

redbull = pygame.image.load(resource_path('assets/redbull2.png'))
redbull = pygame.transform.scale(redbull, (TILE_SIZE, TILE_SIZE))

