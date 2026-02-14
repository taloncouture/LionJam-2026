export class GameContext {
    constructor() {
        this.selected_item = null;
        this.credits = 10;
        this.bricks = 0;
        this.required_bricks = [0, 2, 10, 20, 30, 40];
        this.pyramid_stage = 0;
        this.built = false;
        this.turn = 1;
        this.production_tiles = 0;
        this.lives = 3;
    }
}
