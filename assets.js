import { TILE_SIZE, SCALE_FACTOR } from './config.js';

function scaleImage(img, w, h) {
    const c = document.createElement('canvas');
    c.width = w;
    c.height = h;
    const ctx = c.getContext('2d');
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(img, 0, 0, w, h);
    return c;
}

function loadImg(path) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = () => resolve(img);
        img.onerror = reject;
        img.src = path;
    });
}

// All exported asset canvases (populated by loadAllAssets)
export let grass, selector, boundingbox, forest, factory_1, factory_2, factory_3;
export let pizzeria, tower, road, monument, cheese, pizza;
export let stage_1, stage_2, stage_3, stage_4, stage_5;
export let mrpizza, mrpizza_2;
export let nolat_1, nolat_2, nolat_1_1, nolat_2_1;
export let inventory, shop_border, inventory_selector, inventory_selected;
export let factory_item, pizzeria_item, farm_item, road_item, monument_item, tower_item, axe_item, housing_item;
export let platform, nolat_platform, next_turn, critics;
export let farm_1, farm_2, farm_3, housing, redbull;

export async function loadAllAssets() {
    const base = '../assets/';

    const entries = {
        grass:       ['grass_sand.png', TILE_SIZE, TILE_SIZE],
        selector:    ['selector.png', TILE_SIZE, TILE_SIZE],
        boundingbox: ['boundingbox.png', TILE_SIZE, TILE_SIZE],
        forest:      ['forest.png', TILE_SIZE, TILE_SIZE],
        factory_1:   ['factory_1.png', TILE_SIZE, TILE_SIZE],
        factory_2:   ['factory_2.png', TILE_SIZE, TILE_SIZE],
        factory_3:   ['factory_3.png', TILE_SIZE, TILE_SIZE],
        pizzeria:    ['pizzeria.png', TILE_SIZE, TILE_SIZE],
        tower:       ['tower.png', TILE_SIZE, TILE_SIZE],
        road:        ['road.png', TILE_SIZE, TILE_SIZE],
        monument:    ['monument.png', TILE_SIZE, TILE_SIZE],
        cheese:      ['gem.png', TILE_SIZE, TILE_SIZE],
        pizza:       ['pizza.png', TILE_SIZE, TILE_SIZE],
        stage_5:     ['pyramid.png', TILE_SIZE * 3, TILE_SIZE * 3],
        stage_4:     ['stage_4.png', TILE_SIZE * 3, TILE_SIZE * 3],
        stage_3:     ['stage_3.png', TILE_SIZE * 3, TILE_SIZE * 3],
        stage_2:     ['stage_2.png', TILE_SIZE * 3, TILE_SIZE * 3],
        stage_1:     ['stage_1.png', TILE_SIZE * 3, TILE_SIZE * 3],
        mrpizza:     ['mrpizza.png', TILE_SIZE, TILE_SIZE],
        mrpizza_2:   ['mrpizza_2.png', TILE_SIZE, TILE_SIZE],
        nolat_1:     ['nolat_1.png', TILE_SIZE, TILE_SIZE],
        nolat_2:     ['nolat_2.png', TILE_SIZE, TILE_SIZE],
        nolat_1_1:   ['nolat_1_1.png', TILE_SIZE, TILE_SIZE],
        nolat_2_1:   ['nolat_2_1.png', TILE_SIZE, TILE_SIZE],
        inventory:   ['inventory2.png', 128 * SCALE_FACTOR, 64 * SCALE_FACTOR],
        shop_border: ['shop_border.png', 16 * 10 * SCALE_FACTOR, 16 * 6 * SCALE_FACTOR],
        inventory_selector: ['inventory_selector.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        inventory_selected: ['inventory_selected.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        factory_item:  ['factory_item.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        pizzeria_item: ['pizzeria_item.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        farm_item:     ['farm_item.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        road_item:     ['road_item.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        monument_item: ['monument_item.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        tower_item:    ['tower_item.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        axe_item:      ['axe.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        housing_item:  ['housing_item.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        platform:      ['platform2.png', TILE_SIZE, TILE_SIZE],
        nolat_platform:['nolat_platform.png', TILE_SIZE, TILE_SIZE],
        next_turn:     ['next_turn.png', 16 * SCALE_FACTOR, 16 * SCALE_FACTOR],
        critics:       ['critics.png', TILE_SIZE, TILE_SIZE],
        farm_1:        ['farm_1.png', TILE_SIZE, TILE_SIZE],
        farm_2:        ['farm_2.png', TILE_SIZE, TILE_SIZE],
        farm_3:        ['farm_3.png', TILE_SIZE, TILE_SIZE],
        housing:       ['housing.png', TILE_SIZE, TILE_SIZE],
        redbull:       ['redbull0.png', TILE_SIZE, TILE_SIZE],
    };

    const keys = Object.keys(entries);
    const promises = keys.map(k => loadImg(base + entries[k][0]));
    const images = await Promise.all(promises);

    const scaled = {};
    for (let i = 0; i < keys.length; i++) {
        const [, w, h] = entries[keys[i]];
        scaled[keys[i]] = scaleImage(images[i], w, h);
    }

    // Assign to module-level exports
    grass = scaled.grass;
    selector = scaled.selector;
    boundingbox = scaled.boundingbox;
    forest = scaled.forest;
    factory_1 = scaled.factory_1;
    factory_2 = scaled.factory_2;
    factory_3 = scaled.factory_3;
    pizzeria = scaled.pizzeria;
    tower = scaled.tower;
    road = scaled.road;
    monument = scaled.monument;
    cheese = scaled.cheese;
    pizza = scaled.pizza;
    stage_1 = scaled.stage_1;
    stage_2 = scaled.stage_2;
    stage_3 = scaled.stage_3;
    stage_4 = scaled.stage_4;
    stage_5 = scaled.stage_5;
    mrpizza = scaled.mrpizza;
    mrpizza_2 = scaled.mrpizza_2;
    nolat_1 = scaled.nolat_1;
    nolat_2 = scaled.nolat_2;
    nolat_1_1 = scaled.nolat_1_1;
    nolat_2_1 = scaled.nolat_2_1;
    inventory = scaled.inventory;
    shop_border = scaled.shop_border;
    inventory_selector = scaled.inventory_selector;
    inventory_selected = scaled.inventory_selected;
    factory_item = scaled.factory_item;
    pizzeria_item = scaled.pizzeria_item;
    farm_item = scaled.farm_item;
    road_item = scaled.road_item;
    monument_item = scaled.monument_item;
    tower_item = scaled.tower_item;
    axe_item = scaled.axe_item;
    housing_item = scaled.housing_item;
    platform = scaled.platform;
    nolat_platform = scaled.nolat_platform;
    next_turn = scaled.next_turn;
    critics = scaled.critics;
    farm_1 = scaled.farm_1;
    farm_2 = scaled.farm_2;
    farm_3 = scaled.farm_3;
    housing = scaled.housing;
    redbull = scaled.redbull;
}
