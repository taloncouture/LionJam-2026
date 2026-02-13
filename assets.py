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

grass = pygame.image.load(resource_path('assets/grass_sand.png'))
grass = pygame.transform.scale(grass, (TILE_SIZE, TILE_SIZE))

selector = pygame.image.load(resource_path('assets/selector.png'))
selector = pygame.transform.scale(selector, (TILE_SIZE, TILE_SIZE))

boundingbox = pygame.image.load(resource_path('assets/boundingbox.png'))
boundingbox = pygame.transform.scale(boundingbox, (TILE_SIZE, TILE_SIZE))

forest = pygame.image.load(resource_path('assets/forest.png'))
forest = pygame.transform.scale(forest, (TILE_SIZE, TILE_SIZE))

factory_1 = pygame.image.load(resource_path('assets/factory_1.png'))
factory_1 = pygame.transform.scale(factory_1, (TILE_SIZE, TILE_SIZE))

factory_2 = pygame.image.load(resource_path('assets/factory_2.png'))
factory_2 = pygame.transform.scale(factory_2, (TILE_SIZE, TILE_SIZE))

factory_3 = pygame.image.load(resource_path('assets/factory_3.png'))
factory_3 = pygame.transform.scale(factory_3, (TILE_SIZE, TILE_SIZE))

pizzeria = pygame.image.load(resource_path('assets/pizzeria.png'))
pizzeria = pygame.transform.scale(pizzeria, (TILE_SIZE, TILE_SIZE))

tower = pygame.image.load(resource_path('assets/tower.png'))
tower = pygame.transform.scale(tower, (TILE_SIZE, TILE_SIZE))

road = pygame.image.load(resource_path('assets/road.png'))
road = pygame.transform.scale(road, (TILE_SIZE, TILE_SIZE))

monument = pygame.image.load(resource_path('assets/monument.png'))
monument = pygame.transform.scale(monument, (TILE_SIZE, TILE_SIZE))

cheese = pygame.image.load(resource_path('assets/gem.png'))
cheese = pygame.transform.scale(cheese, (TILE_SIZE, TILE_SIZE))

pizza = pygame.image.load(resource_path('assets/pizza.png'))
pizza = pygame.transform.scale(pizza, (TILE_SIZE, TILE_SIZE))

stage_5 = pygame.image.load(resource_path('assets/pyramid.png'))
stage_5 = pygame.transform.scale(stage_5, (TILE_SIZE * 3, TILE_SIZE * 3))

stage_4 = pygame.image.load(resource_path('assets/stage_4.png'))
stage_4 = pygame.transform.scale(stage_4, (TILE_SIZE * 3, TILE_SIZE * 3))

stage_3 = pygame.image.load(resource_path('assets/stage_3.png'))
stage_3 = pygame.transform.scale(stage_3, (TILE_SIZE * 3, TILE_SIZE * 3))

stage_2 = pygame.image.load(resource_path('assets/stage_2.png'))
stage_2 = pygame.transform.scale(stage_2, (TILE_SIZE * 3, TILE_SIZE * 3))

stage_1 = pygame.image.load(resource_path('assets/stage_1.png'))
stage_1 = pygame.transform.scale(stage_1, (TILE_SIZE * 3, TILE_SIZE * 3))

mrpizza = pygame.image.load(resource_path('assets/mrpizza.png'))
mrpizza = pygame.transform.scale(mrpizza, (TILE_SIZE, TILE_SIZE))

mrpizza_2 = pygame.image.load(resource_path('assets/mrpizza_2.png'))
mrpizza_2 = pygame.transform.scale(mrpizza_2, (TILE_SIZE, TILE_SIZE))

nolat_1 = pygame.image.load(resource_path('assets/nolat_1.png'))
nolat_1 = pygame.transform.scale(nolat_1, (TILE_SIZE, TILE_SIZE))

nolat_2 = pygame.image.load(resource_path('assets/nolat_2.png'))
nolat_2 = pygame.transform.scale(nolat_2, (TILE_SIZE, TILE_SIZE))

nolat_1_1 = pygame.image.load(resource_path('assets/nolat_1_1.png'))
nolat_1_1 = pygame.transform.scale(nolat_1_1, (TILE_SIZE, TILE_SIZE))

nolat_2_1 = pygame.image.load(resource_path('assets/nolat_2_1.png'))
nolat_2_1 = pygame.transform.scale(nolat_2_1, (TILE_SIZE, TILE_SIZE))

inventory = pygame.image.load(resource_path('assets/inventory2.png'))
inventory = pygame.transform.scale(inventory, (128 * SCALE_FACTOR, 64 * SCALE_FACTOR))

shop_border = pygame.image.load(resource_path('assets/shop_border.png'))
shop_border = pygame.transform.scale(shop_border, (16 * 10 * SCALE_FACTOR, 16 * 6 * SCALE_FACTOR))

inventory_selector = pygame.image.load(resource_path('assets/inventory_selector.png'))
inventory_selector = pygame.transform.scale(inventory_selector, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

inventory_selected = pygame.image.load(resource_path('assets/inventory_selected.png'))
inventory_selected = pygame.transform.scale(inventory_selected, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

factory_item = pygame.image.load(resource_path('assets/factory_item.png'))
factory_item = pygame.transform.scale(factory_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

pizzeria_item = pygame.image.load(resource_path('assets/pizzeria_item.png'))
pizzeria_item = pygame.transform.scale(pizzeria_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

farm_item = pygame.image.load(resource_path('assets/farm_item.png'))
farm_item = pygame.transform.scale(farm_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

road_item = pygame.image.load(resource_path('assets/road_item.png'))
road_item = pygame.transform.scale(road_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

monument_item = pygame.image.load(resource_path('assets/monument_item.png'))
monument_item = pygame.transform.scale(monument_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

tower_item = pygame.image.load(resource_path('assets/tower_item.png'))
tower_item = pygame.transform.scale(tower_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

axe_item = pygame.image.load(resource_path('assets/axe.png'))
axe_item = pygame.transform.scale(axe_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

housing_item = pygame.image.load(resource_path('assets/housing_item.png'))
housing_item = pygame.transform.scale(housing_item, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

platform = pygame.image.load(resource_path('assets/platform2.png'))
platform = pygame.transform.scale(platform, (TILE_SIZE, TILE_SIZE))

nolat_platform = pygame.image.load(resource_path('assets/nolat_platform.png'))
nolat_platform = pygame.transform.scale(nolat_platform, (TILE_SIZE, TILE_SIZE))

next_turn = pygame.image.load(resource_path('assets/next_turn.png'))
next_turn = pygame.transform.scale(next_turn, (16 * SCALE_FACTOR, 16 * SCALE_FACTOR))

critics = pygame.image.load(resource_path('assets/critics.png'))
critics = pygame.transform.scale(critics, (TILE_SIZE, TILE_SIZE))

farm_1 = pygame.image.load(resource_path('assets/farm_1.png'))
farm_1 = pygame.transform.scale(farm_1, (TILE_SIZE, TILE_SIZE))

farm_2 = pygame.image.load(resource_path('assets/farm_2.png'))
farm_2 = pygame.transform.scale(farm_2, (TILE_SIZE, TILE_SIZE))

farm_3 = pygame.image.load(resource_path('assets/farm_3.png'))
farm_3 = pygame.transform.scale(farm_3, (TILE_SIZE, TILE_SIZE))

housing = pygame.image.load(resource_path('assets/housing.png'))
housing = pygame.transform.scale(housing, (TILE_SIZE, TILE_SIZE))

redbull = pygame.image.load(resource_path('assets/redbull0.png'))
redbull = pygame.transform.scale(redbull, (TILE_SIZE, TILE_SIZE))

