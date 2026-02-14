import { WIDTH, HEIGHT } from './config.js';
import { loadAllAssets } from './assets.js';
import { Engine } from './engine_core.js';
import { GameContext } from './context.js';
import { GameState } from './game.js';
import { ShopState } from './shop.js';
import { TitleState, EndState } from './states.js';
import { initTileMaps } from './tiles.js';

async function main() {
    // Wait for the custom font to load
    await document.fonts.load('16px PixelFont');

    // Load all image assets
    await loadAllAssets();

    // Initialize tile maps (depends on assets being loaded)
    initTileMaps();

    // Set up canvases
    const screenCanvas = document.getElementById('screen');
    const screenCtx = screenCanvas.getContext('2d');

    const surfaceCanvas = document.createElement('canvas');
    surfaceCanvas.width = WIDTH;
    surfaceCanvas.height = HEIGHT;
    const surfaceCtx = surfaceCanvas.getContext('2d');
    surfaceCtx.imageSmoothingEnabled = false;

    function resize() {
        screenCanvas.width = window.innerWidth;
        screenCanvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    const engine = new Engine(surfaceCtx, screenCtx);
    const gameContext = new GameContext();

    const gameState = new GameState(engine, gameContext);
    const shopState = new ShopState(engine, gameContext);
    const endState = new EndState(engine, gameContext);
    const titleState = new TitleState(engine, gameContext);
    let currentState = titleState;

    // Mouse tracking
    let rawMouseX = 0, rawMouseY = 0;

    screenCanvas.addEventListener('mousemove', (e) => {
        rawMouseX = e.clientX;
        rawMouseY = e.clientY;
    });

    screenCanvas.addEventListener('mousedown', (e) => {
        currentState.on_click();
    });

    window.addEventListener('keydown', (e) => {
        if (e.key === 'e' || e.key === 'E') {
            if (currentState === titleState) {
                currentState = gameState;
            } else if (currentState === shopState) {
                currentState.on_close();
                currentState = gameState;
            } else if (currentState === gameState) {
                currentState.on_close();
                currentState = shopState;
            }
        }
    });

    // Game loop at 30 FPS
    const frameInterval = 1000 / 30;
    let lastTime = 0;

    function gameLoop(timestamp) {
        requestAnimationFrame(gameLoop);

        const delta = timestamp - lastTime;
        if (delta < frameInterval) return;
        lastTime = timestamp - (delta % frameInterval);

        // Check win/lose conditions
        if (currentState === gameState && (gameState.game_finished || gameContext.lives <= 0)) {
            currentState = endState;
        }

        // Update mouse position in engine (convert window coords to game coords)
        const win_w = screenCanvas.width;
        const win_h = screenCanvas.height;
        const scale = Math.min(win_w / WIDTH, win_h / HEIGHT);
        const ox = Math.floor((win_w - Math.floor(WIDTH * scale)) / 2);
        const oy = Math.floor((win_h - Math.floor(HEIGHT * scale)) / 2);
        engine.mouse_x = (rawMouseX - ox) / scale;
        engine.mouse_y = (rawMouseY - oy) / scale;

        engine.update();

        currentState.update();
        currentState.render(screenCtx, surfaceCtx);
    }

    requestAnimationFrame(gameLoop);
}

main();
