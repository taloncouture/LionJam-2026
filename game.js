import * as items from './items.js';
import * as assets from './assets.js';
import { WIDTH, HEIGHT, SCALE_FACTOR, TILE_SIZE, PADDING, ORIGIN_X, ORIGIN_Y, HALF_W } from './config.js';
import * as tiles from './tiles.js';
import { State, screen_to_iso } from './states.js';
import { renderText } from './graphics.js';
import { Button } from './items.js';

export class GameState extends State {
    constructor(engine, gameContext) {
        super(engine, gameContext);
        this.built = false;
        this.roads = [];

        this.next_turn_button = new Button(assets.next_turn,
            WIDTH - (16 * SCALE_FACTOR) - PADDING,
            HEIGHT - (16 * SCALE_FACTOR) - PADDING,
            this.engine);

        // Fade effect
        this.fade_alpha = 255;
        this.fade_speed = 10;

        this.game_finished = false;
    }

    // BFS connected tiles algorithm
    generate_connected_tiles(start, tilemap) {
        const visited = new Set();
        const queue = [start];
        const collected = new Set();

        while (queue.length > 0) {
            const [x, y] = queue.shift();
            const key = `${x},${y}`;

            if (visited.has(key)) continue;
            visited.add(key);
            collected.add(key);

            const neighbors = tiles.get_neighbors(x, y, tilemap);
            for (const tile of neighbors) {
                if (tile === null || tile === undefined) continue;
                if (tile instanceof tiles.RoadTile) {
                    queue.push([tile.x, tile.y]);
                } else {
                    collected.add(`${tile.x},${tile.y}`);
                }
            }
        }

        return collected;
    }

    update_connections(tile, claim = true) {
        if (!tile.required_connections) return;

        const neighbors = tiles.get_neighbors(tile.x, tile.y, tiles.tile_map);
        let connected_tiles_set = new Set();
        for (const neighbor of neighbors) {
            if (neighbor && neighbor instanceof tiles.RoadTile) {
                const connected = this.generate_connected_tiles([neighbor.x, neighbor.y], tiles.tile_map);
                for (const key of connected) connected_tiles_set.add(key);
            }
        }

        if (!tile.connected_tiles || !(tile.connected_tiles instanceof Map)) {
            tile.connected_tiles = new Map();
        }

        for (const [required_type] of tile.required_connections) {
            if (!tile.connected_tiles.has(required_type)) {
                tile.connected_tiles.set(required_type, new Set());
            }
        }

        for (const key of connected_tiles_set) {
            const [tx, ty] = key.split(',').map(Number);
            const t = tiles.tile_map[ty][tx];

            for (const [required_class, required_count] of tile.required_connections) {
                if (tile.connected_tiles.get(required_class).size >= required_count) continue;
                if (t instanceof required_class) {
                    if (t.claimed === null || t.claimed === undefined || t.claimed === tile) {
                        tile.connected_tiles.get(required_class).add(t);
                    }
                }
            }
        }

        let requirements_met = true;
        for (const [t_type, count] of tile.required_connections) {
            if (tile.connected_tiles.get(t_type).size < count) {
                requirements_met = false;
                break;
            }
        }

        tile.requirements_met = requirements_met;

        if (requirements_met) {
            for (const [required_type, required_count] of tile.required_connections) {
                let owned_count = 0;
                for (const t of tile.connected_tiles.get(required_type)) {
                    if (t.claimed === tile) owned_count++;
                }
                let to_claim_count = required_count - owned_count;

                for (const t of tile.connected_tiles.get(required_type)) {
                    if (to_claim_count <= 0) break;
                    if (claim && t.claimable && (t.claimed === null || t.claimed === undefined || t.claimed === tile)) {
                        t.claimed = tile;
                        to_claim_count--;
                    }
                }
            }
        }
    }

    place_item(x, y) {
        if (0 <= y && y < tiles.tile_map.length && 0 <= x && x < tiles.tile_map[y].length) {
            if (tiles.place_tile(x, y, this.gameContext.selected_item.tile, tiles.tile_map)) {
                this.gameContext.selected_item = null;

                // Two-pass connection update (matching Python logic)
                for (let yy = 0; yy < tiles.tile_map.length; yy++) {
                    for (let xx = 0; xx < tiles.tile_map[yy].length; xx++) {
                        const t = tiles.tile_map[yy][xx];
                        if (t && t.required_connections) {
                            this.update_connections(t, false);
                        }
                    }
                }
                for (let yy = 0; yy < tiles.tile_map.length; yy++) {
                    for (let xx = 0; xx < tiles.tile_map[yy].length; xx++) {
                        const t = tiles.tile_map[yy][xx];
                        if (t && t.required_connections) {
                            this.update_connections(t, true);
                        }
                    }
                }

                return true;
            }
        }
        return false;
    }

    next_turn() {
        if (this.gameContext.built) {
            this.game_finished = true;
            return;
        }

        this.gameContext.turn += 1;

        let spawning_nolat = false;
        if (Math.random() < tiles.Nolat.spawn_chance) {
            spawning_nolat = true;
        }

        if (spawning_nolat && tiles.nolat_platforms.length > 0) {
            const platform = tiles.nolat_platforms[Math.floor(Math.random() * tiles.nolat_platforms.length)];
            platform.spawn();
        }

        const actors = [];
        for (let y = 0; y < tiles.tile_map.length; y++) {
            for (let x = 0; x < tiles.tile_map[y].length; x++) {
                this.gameContext.credits += tiles.tile_map[y][x].credits_produced;
                actors.push(tiles.tile_map[y][x]);
            }
        }

        for (const tile of actors) {
            tile.update();
            if (tile instanceof tiles.MilitaryTile) {
                tile.lookout();
            }
        }

        for (let y = 0; y < tiles.tile_map.length; y++) {
            for (let x = 0; x < tiles.tile_map[y].length; x++) {
                const tile = tiles.tile_map[y][x];
                if (tile instanceof tiles.EnemyTile) {
                    if (tiles.ground_tile_map[tile.y][tile.x] instanceof tiles.PlatformTile) {
                        tile.destroy();
                        this.gameContext.lives -= 1;
                    }
                }
            }
        }
    }

    on_click() {
        const mx = this.engine.mouse_x;
        const my = this.engine.mouse_y;
        const [selected_x, selected_y] = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y);

        if (this.gameContext.selected_item !== null && this.gameContext.selected_item.cost <= this.gameContext.credits) {
            const cost = this.gameContext.selected_item.cost;

            if (this.gameContext.selected_item instanceof items.DestructionItem) {
                if (tiles.is_valid(selected_x, selected_y, tiles.tile_map)) {
                    const target_tile = tiles.tile_map[selected_y][selected_x];
                    let matches = false;
                    for (const targetClass of this.gameContext.selected_item.targets) {
                        if (target_tile instanceof targetClass) {
                            matches = true;
                            break;
                        }
                    }
                    if (matches) {
                        tiles.destroy_tile(selected_x, selected_y, tiles.tile_map);
                        this.gameContext.credits -= cost;
                    }
                }
            } else if (this.place_item(selected_x, selected_y)) {
                this.gameContext.credits -= cost;
            }
        } else if (this.next_turn_button.selected === true) {
            this.next_turn_button.selected = false;
            this.next_turn();
        }

        if (0 <= selected_y && selected_y < tiles.tile_map.length && 0 <= selected_x && selected_x < tiles.tile_map[selected_y].length) {
            if (tiles.tile_map[selected_y][selected_x] instanceof tiles.ProductionTile) {
                if (tiles.tile_map[selected_y][selected_x].collect()) {
                    this.gameContext.bricks += tiles.tile_map[selected_y][selected_x].production_quantity;
                }
            }
            if (tiles.tile_map[selected_y][selected_x] instanceof tiles.EnemyTile || tiles.tile_map[selected_y][selected_x] instanceof tiles.MilitaryTile) {
                tiles.tile_map[selected_y][selected_x].on_click();
            }
        }
    }

    update() {
        if (this.fade_alpha > 0) {
            this.fade_alpha -= this.fade_speed;
            if (this.fade_alpha < 0) this.fade_alpha = 0;
        }

        for (let y = 0; y < tiles.tile_map.length; y++) {
            for (let x = 0; x < tiles.tile_map[y].length; x++) {
                if (tiles.tile_map[y][x] instanceof tiles.Pyramid) {
                    const pyramid = tiles.tile_map[y][x];
                    if (this.gameContext.pyramid_stage >= pyramid.stages.length - 1) {
                        this.built = true;
                        this.gameContext.built = true;
                    } else {
                        const next_stage = this.gameContext.pyramid_stage + 1;
                        if (this.gameContext.bricks >= this.gameContext.required_bricks[next_stage]) {
                            this.gameContext.pyramid_stage = next_stage;
                            pyramid.stage = next_stage;
                            this.built = true;
                        }
                    }
                }
            }
        }
    }

    render(screenCtx, surfaceCtx) {
        screenCtx.fillStyle = '#000';
        screenCtx.fillRect(0, 0, screenCtx.canvas.width, screenCtx.canvas.height);
        surfaceCtx.fillStyle = 'rgb(255, 243, 193)';
        surfaceCtx.fillRect(0, 0, WIDTH, HEIGHT);

        // Render ground tiles
        for (let y = 0; y < tiles.ground_tile_map.length; y++) {
            for (let x = 0; x < tiles.ground_tile_map[y].length; x++) {
                tiles.ground_tile_map[y][x].render(surfaceCtx);
            }
        }

        // Render tile map
        for (let y = 0; y < tiles.tile_map.length; y++) {
            for (let x = 0; x < tiles.tile_map[y].length; x++) {
                const tile = tiles.tile_map[y][x];
                if (tile !== null) {
                    tile.animate();

                    if (tile instanceof tiles.EnemyTile && tile.occupied_tile !== null && tile.occupied_tile !== undefined) {
                        tile.occupied_tile.render(surfaceCtx);
                    }

                    tile.render(surfaceCtx);

                    if (tile instanceof tiles.ProductionTile && tile.has_item) {
                        const [ix, iy] = tiles.coords_to_iso(x, y);
                        surfaceCtx.drawImage(assets.pizza, ix, iy - TILE_SIZE);
                    }
                }
            }
        }

        // HUD
        const mx = this.engine.mouse_x;
        const my = this.engine.mouse_y;

        surfaceCtx.drawImage(assets.cheese, PADDING, 0);
        renderText(surfaceCtx, PADDING * 8.2, PADDING * 4, 24, `x${this.gameContext.credits}`, 0, 1, [178, 0, 0]);
        renderText(surfaceCtx, PADDING, HEIGHT - PADDING * 5, 24, `Turn: ${this.gameContext.turn}`, 0, 0, [178, 0, 0]);

        this.next_turn_button.update();
        this.next_turn_button.render();

        // Selector
        const [imx, imy] = screen_to_iso(mx, my, ORIGIN_X, ORIGIN_Y);
        if (0 <= imy && imy < tiles.tiles_ground.length && 0 <= imx && imx < tiles.tiles_ground[imy].length && tiles.tiles_ground[imy][imx] !== ' ') {
            const [tx, ty] = tiles.coords_to_iso(imx, imy);
            surfaceCtx.drawImage(assets.selector, tx, ty);

            const tile = tiles.tile_map[imy][imx];

            if (!(tile instanceof tiles.AirTile) && !(tile instanceof tiles.ForestTile) && !(tile instanceof tiles.Restricted)) {
                renderText(surfaceCtx, tx + (TILE_SIZE / 2), ty + (TILE_SIZE / 2), 25, `Producing Credits: ${tile.credits_produced}`, 1, 0, [178, 0, 0]);
                if (tile instanceof tiles.ProductionTile) {
                    renderText(surfaceCtx, tx + (TILE_SIZE / 2), ty + (TILE_SIZE / 2) + PADDING * 3, 25, `Requirements Met: ${tile.requirements_met}`, 1, 0, [178, 0, 0]);
                }
            }
        }

        // Blit surface to screen with scaling
        screenCtx.drawImage(surfaceCtx.canvas, 0, 0, WIDTH, HEIGHT,
            this.engine.offset_x, this.engine.offset_y, this.engine.scaled_w, this.engine.scaled_h);

        // Fade overlay
        if (this.fade_alpha > 0) {
            screenCtx.save();
            screenCtx.globalAlpha = this.fade_alpha / 255;
            screenCtx.fillStyle = '#000';
            screenCtx.fillRect(this.engine.offset_x, this.engine.offset_y, this.engine.scaled_w, this.engine.scaled_h);
            screenCtx.restore();
        }
    }
}
