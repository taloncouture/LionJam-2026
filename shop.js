import { WIDTH, HEIGHT, SCALE_FACTOR, TILE_SIZE, INVENTORY_WIDTH, INVENTORY_HEIGHT, PADDING, ITEM_WIDTH } from './config.js';
import * as assets from './assets.js';
import { State } from './states.js';
import * as items from './items.js';
import { renderText } from './graphics.js';

export class ShopState extends State {
    constructor(engine, gameContext) {
        super(engine, gameContext);

        this.x = Math.floor((WIDTH - (128 * SCALE_FACTOR)) / 2);
        this.y = Math.floor((HEIGHT - (64 * SCALE_FACTOR)) / 2);
        this.width = INVENTORY_WIDTH;
        this.height = INVENTORY_HEIGHT;
        this.selected_x = null;
        this.selected_y = null;
        this.highlighted_x = null;
        this.highlighted_y = null;

        this.slots = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ];

        this.slots[0][0] = new items.RoadItem(this.x, this.y);
        this.slots[0][1] = new items.FarmItem(this.x + (16 * SCALE_FACTOR), this.y);
        this.slots[0][2] = new items.AxeItem(this.x + (16 * 2 * SCALE_FACTOR), this.y);
        this.slots[0][3] = new items.PizzeriaItem(this.x + (16 * 3 * SCALE_FACTOR), this.y);
        this.slots[0][4] = new items.HousingItem(this.x + (16 * 4 * SCALE_FACTOR), this.y);
        this.slots[0][5] = new items.FactoryItem(this.x + (16 * 5 * SCALE_FACTOR), this.y);
        this.slots[0][6] = new items.TowerItem(this.x + (ITEM_WIDTH * 6), this.y);
        this.slots[0][7] = new items.MonumentItem(this.x + (ITEM_WIDTH * 7), this.y);
    }

    update() {
        const mx = this.engine.mouse_x;
        const my = this.engine.mouse_y;
        if (this.x <= mx && mx < this.x + this.width && this.y <= my && my < this.y + this.height) {
            this.selected_x = Math.floor((mx - this.x) / (16 * SCALE_FACTOR));
            this.selected_y = Math.floor((my - this.y) / (16 * SCALE_FACTOR));
        }
    }

    on_click() {
        const mx = this.engine.mouse_x;
        const my = this.engine.mouse_y;
        if (this.x <= mx && mx < this.x + this.width && this.y <= my && my < this.y + this.height) {
            const x = Math.floor((mx - this.x) / (16 * SCALE_FACTOR));
            const y = Math.floor((my - this.y) / (16 * SCALE_FACTOR));

            if (this.slots[y][x] !== ' ') {
                this.gameContext.selected_item = this.slots[y][x];
                this.highlighted_x = x;
                this.highlighted_y = y;
            }
        } else {
            this.highlighted_x = null;
            this.highlighted_y = null;
            this.selected_x = null;
            this.selected_y = null;
            this.gameContext.selected_item = null;
        }
    }

    on_close() {
        this.highlighted_x = null;
        this.highlighted_y = null;
    }

    render(screenCtx, surfaceCtx) {
        screenCtx.fillStyle = '#000';
        screenCtx.fillRect(0, 0, screenCtx.canvas.width, screenCtx.canvas.height);
        surfaceCtx.fillStyle = 'rgb(255, 243, 193)';
        surfaceCtx.fillRect(0, 0, WIDTH, HEIGHT);

        surfaceCtx.drawImage(assets.cheese, (WIDTH / 2) - (TILE_SIZE / 2), PADDING * 6);
        renderText(surfaceCtx, (WIDTH / 2) + PADDING * 3, (PADDING * 5.5) + (TILE_SIZE / 2), 24, `x${this.gameContext.credits}`, 0, 1, [178, 0, 0]);

        surfaceCtx.drawImage(assets.inventory, this.x, this.y);

        for (let y = 0; y < this.slots.length; y++) {
            for (let x = 0; x < this.slots[y].length; x++) {
                if (this.slots[y][x] !== ' ') {
                    this.slots[y][x].render(surfaceCtx);
                }
            }
        }

        if (this.selected_x !== null) {
            surfaceCtx.drawImage(assets.inventory_selector,
                this.x + (this.selected_x * 16 * SCALE_FACTOR),
                this.y + (this.selected_y * 16 * SCALE_FACTOR));
        }

        if (this.highlighted_x !== null) {
            surfaceCtx.drawImage(assets.inventory_selected,
                this.x + (this.highlighted_x * 16 * SCALE_FACTOR),
                this.y + (this.highlighted_y * 16 * SCALE_FACTOR));
        }

        surfaceCtx.drawImage(assets.shop_border,
            this.x - (16 * SCALE_FACTOR),
            this.y - (16 * SCALE_FACTOR));

        if (this.selected_x !== null && this.selected_y !== null && this.slots[this.selected_y][this.selected_x] !== ' ') {
            const item = this.slots[this.selected_y][this.selected_x];
            renderText(surfaceCtx, WIDTH / 2, HEIGHT - (HEIGHT / 4), 40, `${item.name}`, 1, 0, [178, 0, 0]);
            renderText(surfaceCtx, WIDTH / 2, HEIGHT - (HEIGHT / 6), 30, `Cost: ${item.cost}`, 1, 0, [178, 0, 0]);
            renderText(surfaceCtx, WIDTH / 2, HEIGHT - (HEIGHT / 8), 30, `Description: ${item.description}`, 1, 0, [178, 0, 0]);
        }

        screenCtx.drawImage(surfaceCtx.canvas, 0, 0, WIDTH, HEIGHT,
            this.engine.offset_x, this.engine.offset_y, this.engine.scaled_w, this.engine.scaled_h);
    }
}
