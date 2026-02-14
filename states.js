import { WIDTH, HEIGHT, HALF_W, HALF_H } from './config.js';
import { renderText } from './graphics.js';

export function screen_to_iso(mx, my, origin_x, origin_y) {
    mx -= origin_x;
    my -= origin_y;
    mx -= HALF_W;
    my -= HALF_H;

    const dx = mx / HALF_W;
    const dy = my / HALF_H;

    const x = (dx + dy) / 2;
    const y = (dy - dx) / 2;

    return [Math.floor(x + 0.5), Math.floor(y + 0.5)];
}

export class State {
    constructor(engine, gameContext) {
        this.engine = engine;
        this.gameContext = gameContext;
    }
    update() {}
    render(screenCtx, surfaceCtx) {}
    on_click() {}
    on_close() {}
    on_open() {}
}

export class EndState extends State {
    constructor(engine, gameContext) {
        super(engine, gameContext);
        this.text_y = HEIGHT;
    }

    render(screenCtx, surfaceCtx) {
        screenCtx.fillStyle = '#000';
        screenCtx.fillRect(0, 0, screenCtx.canvas.width, screenCtx.canvas.height);
        surfaceCtx.fillStyle = 'rgb(255, 243, 193)';
        surfaceCtx.fillRect(0, 0, WIDTH, HEIGHT);

        let message = '';
        if (this.gameContext.lives <= 0) {
            message = 'Game Over';
        } else {
            message = 'You Built The Pyramid!';
        }

        renderText(surfaceCtx, WIDTH / 2, this.text_y, 100, message, 1, 0, [178, 0, 0]);
        renderText(surfaceCtx, WIDTH / 2, this.text_y + 150, 60, 'Thanks For Playing!', 1, 0, [178, 0, 0]);
        renderText(surfaceCtx, WIDTH / 2, this.text_y + 250, 50, `Turns: ${this.gameContext.turn}`, 1, 0, [178, 0, 0]);
        renderText(surfaceCtx, WIDTH / 2, this.text_y + 350, 50, `Pizzas Cooked: ${this.gameContext.bricks}`, 1, 0, [178, 0, 0]);
        renderText(surfaceCtx, WIDTH / 2, this.text_y + 500, 25, 'Created by Talon Couture', 1, 0, [178, 0, 0]);

        screenCtx.drawImage(surfaceCtx.canvas, 0, 0, WIDTH, HEIGHT,
            this.engine.offset_x, this.engine.offset_y, this.engine.scaled_w, this.engine.scaled_h);
    }

    update() {
        if (this.text_y > -1000) {
            this.text_y -= 1;
        }
    }
}

export class TitleState extends State {
    constructor(engine, gameContext) {
        super(engine, gameContext);
    }

    render(screenCtx, surfaceCtx) {
        screenCtx.fillStyle = '#000';
        screenCtx.fillRect(0, 0, screenCtx.canvas.width, screenCtx.canvas.height);
        surfaceCtx.fillStyle = 'rgb(255, 243, 193)';
        surfaceCtx.fillRect(0, 0, WIDTH, HEIGHT);

        renderText(surfaceCtx, WIDTH / 2, HEIGHT / 3, 60, 'Great Pyramid of', 1, 0, [178, 0, 0]);
        renderText(surfaceCtx, WIDTH / 2, HEIGHT / 3 + 60, 140, 'PIZZA', 1, 0, [178, 0, 0]);
        renderText(surfaceCtx, WIDTH / 2, HEIGHT - (HEIGHT / 5), 20, 'press e to start', 1, 0, [178, 0, 0]);

        screenCtx.drawImage(surfaceCtx.canvas, 0, 0, WIDTH, HEIGHT,
            this.engine.offset_x, this.engine.offset_y, this.engine.scaled_w, this.engine.scaled_h);
    }
}
