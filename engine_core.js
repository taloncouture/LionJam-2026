import { WIDTH, HEIGHT } from './config.js';

export class Engine {
    constructor(surface, screen) {
        this.mouse_x = 0;
        this.mouse_y = 0;
        this.scale = 1;
        this.offset_x = 0;
        this.offset_y = 0;
        this.scaled_w = 0;
        this.scaled_h = 0;

        this.surface = surface;   // offscreen canvas context
        this.screen = screen;     // main canvas context
    }

    update() {
        const win_w = this.screen.canvas.width;
        const win_h = this.screen.canvas.height;
        const scale = Math.min(win_w / WIDTH, win_h / HEIGHT);
        this.scaled_w = Math.floor(WIDTH * scale);
        this.scaled_h = Math.floor(HEIGHT * scale);
        this.offset_x = Math.floor((win_w - this.scaled_w) / 2);
        this.offset_y = Math.floor((win_h - this.scaled_h) / 2);
        this.scale = scale;
    }

    render(image, x, y) {
        this.surface.drawImage(image, x, y);
    }
}
