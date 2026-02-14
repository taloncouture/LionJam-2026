import * as assets from './assets.js';
import * as config from './config.js';

export function coords_to_iso(x, y) {
    const iso_x = (x - y) * config.HALF_W;
    const iso_y = (x + y) * config.HALF_H;
    return [config.ORIGIN_X + iso_x, config.ORIGIN_Y + iso_y];
}

export const tiles_ground = [
    [' ', ' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', '0', '0', '#', ' ', ' '],
    [' ', 'p', 'p', 'p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
    [' ', 'p', 'p', 'p', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
    [' ', 'p', 'p', 'p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
    [' ', ' ', '0', ' ', ' ', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' '],
    ['p', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
    [' ', ' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '],
    [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', '0', '0', '0', '0'],
    [' ', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' ', '0', '0', '0', '#'],
    [' ', '#', '0', '0', ' ', ' ', '0', '0', '0', '0', ' ', '0', '0', '0', ' '],
    [' ', ' ', '0', '0', ' ', '0', '0', '0', '0', '0', ' ', ' ', '0', '0', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0', ' ', ' ', ' ', ' ', ' ', ' ']
];

export const tiles2 = [
    [' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '!', '~', '~', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '~', '~', '~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 't', ' ', 't', 't', ' ', ' '],
    ['@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['t', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['t', ' ', ' ', ' ', ' ', 't', ' ', 't', ' ', ' ', ' ', 't', ' ', ' ', ' '],
    [' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', ' ', ' '],
    [' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
];

export const pathfinding = [
    [' ', ' ', ' ', ' ', ' ', ' ', 16, 15, ' ', ' ', 12, 11, 10, ' ', ' '],
    [' ', 'p', 'p', 'p', ' ', 18, 17, 16, 15, 14, 13, 12, 11, ' ', ' '],
    [' ', 'p', 'p', 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, ' '],
    [' ', 'p', 21, 'p', ' ', 18, 17, 16, 15, 14, 13, 12, 11, 10, ' '],
    [' ', ' ', 20, ' ', ' ', 17, 16, 15, 14, 13, 12, 11, 10, ' ', ' '],
    ['p', ' ', 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, ' '],
    [' ', ' ', 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, ' '],
    [' ', 16, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
    [14, 15, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4],
    [13, 14, 15, 14, 13, 12, 11, 10, 9, ' ', 7, 6, 5, 4, 3],
    [12, 13, 14, 13, 12, 11, 10, 9, 8, ' ', ' ', 5, 4, 3, 2],
    [' ', 12, 13, 12, 11, 10, 9, 8, 7, 6, ' ', 4, 3, 2, ' '],
    [' ', 11, 12, 11, ' ', ' ', 8, 7, 6, 5, ' ', 3, 2, 1, ' '],
    [' ', ' ', 11, 10, ' ', 6, 7, 6, 5, 4, ' ', ' ', 1, 0, ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 5, 4, ' ', ' ', ' ', ' ', ' ', ' ']
];

export let tile_map = [];
export let ground_tile_map = [];
export let nolat_platforms = [];

export function is_valid(x, y, tilemap) {
    return (0 <= y && y < tilemap.length && 0 <= x && x < tilemap[y].length);
}

export function adjacent_to_building(x, y, tilemap) {
    const neighbors = get_neighbors(x, y, tilemap);
    for (const neighbor of neighbors) {
        if (neighbor.building === true) return true;
    }
    return false;
}

export function place_tile(x, y, TileClass, tilemap) {
    if (0 <= y && y < tilemap.length && 0 <= x && x < tilemap[y].length
        && ground_tile_map[y][x] instanceof GrassTile
        && tilemap[y][x] instanceof AirTile) {

        if (adjacent_to_building(x, y, tilemap)) {
            if (TileClass === FactoryTile) {
                const neighbors = get_neighbors(x, y, ground_tile_map);
                for (const neighbor of neighbors) {
                    if (neighbor === null || neighbor instanceof AirTile) {
                        tile_map[y][x] = new TileClass(x, y);
                        return true;
                    }
                }
            } else {
                tile_map[y][x] = new TileClass(x, y);
                return true;
            }
        }
    }
    return false;
}

export function destroy_tile(x, y, tilemap) {
    tilemap[y][x] = new AirTile(x, y);
}

export function get_neighbors(x, y, tilemap) {
    const result = [];
    if (is_valid(x - 1, y, tilemap)) result.push(tilemap[y][x - 1]);
    if (is_valid(x + 1, y, tilemap)) result.push(tilemap[y][x + 1]);
    if (is_valid(x, y - 1, tilemap)) result.push(tilemap[y - 1][x]);
    if (is_valid(x, y + 1, tilemap)) result.push(tilemap[y + 1][x]);
    return result;
}

// --- Resource classes ---
export class Resource {
    constructor(image, x, y) {
        this.image = image;
        this.x = x;
        this.y = y;
    }
}

export class PizzaResource extends Resource {
    constructor(image, x, y) {
        super(image, x, y);
    }
}
// Static image reference (set after assets load)
PizzaResource.image = null;

// --- Tile classes ---
export class Tile {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.cost = 0;
        this.credits_produced = 0;
        this.network_id = null;
        this.required_connections = null;
        this.connected_tiles = {};
        this.claimable = false;
        this.claimed = null;
        this.image = assets.grass;
        this.building = false;
        this.frames = [];
        this.index = 0;
        this.anim_speed = 0;
    }

    render(ctx) {
        const [ix, iy] = coords_to_iso(this.x, this.y);
        ctx.drawImage(this.image, ix, iy - config.HALF_W - config.SCALE_FACTOR);
    }

    update() {
        this.animate();
    }

    on_click() {}

    animate() {
        this.index += this.anim_speed;
        if (this.index >= this.frames.length) this.index = 0;
        if (this.frames.length > 0) {
            this.image = this.frames[Math.floor(this.index)];
        }
    }
}

export class ResourceTile extends Tile {
    constructor(x, y) {
        super(x, y);
        this.claimed = null;
        this.claimable = true;
        this.building = true;
    }
}

export class ProductionTile extends Tile {
    constructor(x, y) {
        super(x, y);
        this.has_item = false;
        this.required_farms = 0;
        this.claimed = null;
        this.requirements_met = false;
        this.claimable = true;
        this.building = true;
        this.production_quantity = 1;
    }

    produce() {
        if (this.requirements_met) this.has_item = true;
    }

    collect() {
        if (this.has_item) {
            this.has_item = false;
            return true;
        }
        return false;
    }

    update() {
        this.produce();
    }
}

export class GrassTile extends Tile {
    constructor(x, y) {
        super(x, y);
    }
    render(ctx) {
        const [ix, iy] = coords_to_iso(this.x, this.y);
        ctx.drawImage(this.image, ix, iy);
    }
}

export class PlatformTile extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.platform;
    }
    render(ctx) {
        const [ix, iy] = coords_to_iso(this.x, this.y);
        ctx.drawImage(this.image, ix, iy);
    }
}

export class FactoryTile extends ProductionTile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.factory_1;
        this.credits_produced = 3;
        this.required_farms = 3;
        this.required_connections = new Map([
            [Farm, 2],
            [Housing, 1],
            [Restricted, 1]
        ]);
        this.production_quantity = 3;
        this.frames = [assets.factory_1, assets.factory_2, assets.factory_3];
        this.anim_speed = 0.02;
    }
}
// Attach resource as static property
FactoryTile.resource = PizzaResource;

export class PizzeriaTile extends ProductionTile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.pizzeria;
        this.credits_produced = 1;
        this.required_connections = new Map([
            [Farm, 1],
            [Restricted, 1]
        ]);
    }
}
PizzeriaTile.resource = PizzaResource;

export class RoadTile extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.road;
        this.building = true;
    }
}

export class MonumentTile extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.monument;
        this.credits_produced = 5;
        this.building = true;
    }
}

export class CheeseTile extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.cheese;
    }
}

export class ForestTile extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.forest;
    }
}

export class AirTile extends Tile {
    constructor(x, y) {
        super(x, y);
    }
    render(_ctx) {}
}

export class Restricted extends Tile {
    constructor(x, y) {
        super(x, y);
        this.building = true;
    }
    render(_ctx) {}
}

export class Pyramid extends Tile {
    constructor(x, y) {
        super(x, y);
        this.stages = [null, null, null, null, null, null]; // filled after assets load
        this.stage = 0;
    }
    render(ctx) {
        if (this.stage !== 0 && this.stages[this.stage]) {
            const [ix, iy] = coords_to_iso(this.x, this.y);
            ctx.drawImage(this.stages[this.stage],
                ix - (config.HALF_W * 2) - config.SCALE_FACTOR * 2,
                iy - (config.HALF_H * 5) - config.HALF_W + config.SCALE_FACTOR);
        }
    }
}

export class MRPizza extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.mrpizza;
        this.frames = [assets.mrpizza, assets.mrpizza_2];
        this.anim_speed = 0.03;
    }
}

export class Critics extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.critics;
    }
}

export class Farm extends ResourceTile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.farm_1;
        this.credits_produced = 1;
        this.frames = [assets.farm_1, assets.farm_2, assets.farm_3];
        this.anim_speed = 0.1;
    }
}

export class Housing extends ResourceTile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.housing;
        this.credits_produced = 1;
    }
}

export class MilitaryTile extends Tile {
    constructor(x, y) {
        super(x, y);
    }
}

export class Tower extends MilitaryTile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.tower;
        this.building = true;
    }
    on_click() {
        this.attack();
    }
    attack() {
        const neighbors = get_neighbors(this.x, this.y, tile_map);
        for (const neighbor of neighbors) {
            if (neighbor instanceof EnemyTile) {
                neighbor.destroy();
            }
        }
    }
    lookout() {
        // Tower lookout logic (attacks nearby enemies on turn)
    }
}

export class RedBull extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.redbull;
    }
}

export class NolatPlatform extends Tile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.nolat_platform;
    }
    render(ctx) {
        const [ix, iy] = coords_to_iso(this.x, this.y);
        ctx.drawImage(this.image, ix, iy);
    }
    spawn() {
        if (tile_map[this.y][this.x] instanceof AirTile) {
            tile_map[this.y][this.x] = new Nolat(this.x, this.y);
        }
    }
}

export class EnemyTile extends Tile {
    constructor(x, y) {
        super(x, y);
    }
    move() {}
    update() {
        this.move();
    }
}

export class Nolat extends EnemyTile {
    constructor(x, y) {
        super(x, y);
        this.image = assets.nolat_1;
        this.frames = [assets.nolat_1, assets.nolat_1_1, assets.nolat_2, assets.nolat_2_1];
        this.anim_speed = 0.02;
        this.age = 0;
        this.occupied_tile = null;
    }

    on_click() {
        this.destroy();
    }

    destroy() {
        tile_map[this.y][this.x] = new AirTile(this.x, this.y);
    }

    pathfind() {
        const neighbors = get_neighbors(this.x, this.y, tile_map);
        const valid_neighbors = [];

        for (const neighbor of neighbors) {
            if (neighbor instanceof AirTile || neighbor instanceof RoadTile || neighbor instanceof Farm || neighbor instanceof Restricted) {
                if (!(ground_tile_map[neighbor.y][neighbor.x] instanceof AirTile)) {
                    valid_neighbors.push(neighbor);
                }
            }
        }

        if (valid_neighbors.length > 0) {
            let best_neighbor = valid_neighbors[0];
            for (const neighbor of valid_neighbors) {
                if (pathfinding[neighbor.y][neighbor.x] !== ' ' && pathfinding[best_neighbor.y][best_neighbor.x] !== ' ') {
                    if (pathfinding[neighbor.y][neighbor.x] > pathfinding[best_neighbor.y][best_neighbor.x]) {
                        best_neighbor = neighbor;
                    } else if (pathfinding[neighbor.y][neighbor.x] === pathfinding[best_neighbor.y][best_neighbor.x]) {
                        if (Math.random() < 0.5) best_neighbor = neighbor;
                    }
                }
            }

            if (this.occupied_tile instanceof RoadTile) {
                tile_map[this.y][this.x] = this.occupied_tile;
            } else {
                tile_map[this.y][this.x] = new AirTile(this.x, this.y);
            }

            if (tile_map[best_neighbor.y][best_neighbor.x] instanceof RoadTile) {
                this.occupied_tile = tile_map[best_neighbor.y][best_neighbor.x];
            } else {
                this.occupied_tile = null;
            }

            this.x = best_neighbor.x;
            this.y = best_neighbor.y;
            tile_map[this.y][this.x] = this;
        }
    }

    move() {
        const neighbors = get_neighbors(this.x, this.y, tile_map);
        const valid_neighbors = [];

        for (const neighbor of neighbors) {
            if (neighbor instanceof AirTile || neighbor instanceof RoadTile) {
                if (!(ground_tile_map[neighbor.y][neighbor.x] instanceof AirTile)) {
                    valid_neighbors.push(neighbor);
                }
            }
        }

        if (valid_neighbors.length > 0) {
            const target = valid_neighbors[Math.floor(Math.random() * valid_neighbors.length)];

            if (target instanceof RoadTile) {
                tile_map[this.y][this.x] = new RoadTile(this.x, this.y);
            } else {
                tile_map[this.y][this.x] = new AirTile(this.x, this.y);
            }
            this.x = target.x;
            this.y = target.y;
            tile_map[target.y][target.x] = this;
        }
    }

    update() {
        if (this.age > 0) {
            this.pathfind();
        }
        this.age += 1;
    }
}

Nolat.spawn_chance = 0.25;

// --- Initialize tile maps (called after assets are loaded) ---
export function initTileMaps() {
    PizzaResource.image = assets.pizza;

    tile_map.length = 0;
    ground_tile_map.length = 0;
    nolat_platforms.length = 0;

    for (let y = 0; y < tiles2.length; y++) {
        const tile_row = [];
        for (let x = 0; x < tiles2[y].length; x++) {
            const ch = tiles2[y][x];
            if (ch === 'f') tile_row.push(new FactoryTile(x, y));
            else if (ch === 't') tile_row.push(new ForestTile(x, y));
            else if (ch === '~') tile_row.push(new Restricted(x, y));
            else if (ch === '!') {
                const p = new Pyramid(x, y);
                p.stages = [null, assets.stage_1, assets.stage_2, assets.stage_3, assets.stage_4, assets.stage_5];
                tile_row.push(p);
            }
            else if (ch === '@') tile_row.push(new MRPizza(x, y));
            else if (ch === 'c') tile_row.push(new Critics(x, y));
            else if (ch === 'r') tile_row.push(new Farm(x, y));
            else if (ch === 'e') tile_row.push(new RedBull(x, y));
            else if (ch === 'n') tile_row.push(new Nolat(x, y));
            else tile_row.push(new AirTile(x, y));
        }
        tile_map.push(tile_row);
    }

    for (let y = 0; y < tiles_ground.length; y++) {
        const tile_row = [];
        for (let x = 0; x < tiles_ground[y].length; x++) {
            const ch = tiles_ground[y][x];
            if (ch === '0') tile_row.push(new GrassTile(x, y));
            else if (ch === 'p') tile_row.push(new PlatformTile(x, y));
            else if (ch === '#') {
                const np = new NolatPlatform(x, y);
                tile_row.push(np);
                nolat_platforms.push(np);
            }
            else tile_row.push(new AirTile(x, y));
        }
        ground_tile_map.push(tile_row);
    }
}
