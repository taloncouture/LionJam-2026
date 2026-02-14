import * as assets from './assets.js';
import { ITEM_WIDTH } from './config.js';
import {
    FactoryTile, Farm, RoadTile, MonumentTile, Tower, PizzeriaTile, Housing, ForestTile
} from './tiles.js';

export class Item {
    constructor(image, x, y) {
        this.image = image;
        this.name = '';
        this.description = '';
        this.x = x;
        this.y = y;
        this.tile = null;
        this.cost = 0;
        this.credits_produced = 0;
    }

    render(ctx) {
        ctx.drawImage(this.image, this.x, this.y);
    }
}

export class FactoryItem extends Item {
    constructor(x, y) {
        super(assets.factory_item, x, y);
        this.tile = FactoryTile;
        this.cost = 10;
        this.name = 'Factory';
        this.description = 'Makes 3 pizzas. Requires connection to 1 Housing and 2 Farms.';
    }
}

export class FarmItem extends Item {
    constructor(x, y) {
        super(assets.farm_item, x, y);
        this.tile = Farm;
        this.cost = 2;
        this.credits_produced = 1;
        this.name = 'Farm';
        this.description = 'Grows products to make pizza';
    }
}

export class RoadItem extends Item {
    constructor(x, y) {
        super(assets.road_item, x, y);
        this.tile = RoadTile;
        this.cost = 1;
        this.name = 'Road';
        this.description = 'Connects tiles together';
    }
}

export class MonumentItem extends Item {
    constructor(x, y) {
        super(assets.monument_item, x, y);
        this.tile = MonumentTile;
        this.cost = 20;
        this.name = 'Energy Drink Monument';
        this.description = 'Red Bull is awesome.';
    }
}

export class TowerItem extends Item {
    constructor(x, y) {
        super(assets.tower_item, x, y);
        this.tile = Tower;
        this.cost = 10;
        this.name = 'Military Tower';
        this.description = 'Defends from Nolats within 3 blocks';
    }
}

export class PizzeriaItem extends Item {
    constructor(x, y) {
        super(assets.pizzeria_item, x, y);
        this.tile = PizzeriaTile;
        this.cost = 2;
        this.name = 'Pizzeria';
        this.description = 'Makes 1 pizza. Requires connection to 1 Farm.';
    }
}

export class HousingItem extends Item {
    constructor(x, y) {
        super(assets.housing_item, x, y);
        this.tile = Housing;
        this.cost = 3;
        this.name = 'Housing';
        this.description = 'Supplies workers to Factories.';
    }
}

export class DestructionItem extends Item {
    constructor(image, x, y) {
        super(image, x, y);
        this.targets = [];
    }
}

export class AxeItem extends DestructionItem {
    constructor(x, y) {
        super(assets.axe_item, x, y);
        this.cost = 1;
        this.targets = [ForestTile];
        this.name = 'Axe';
        this.description = 'Cuts down forests.';
    }
}

export class Button {
    constructor(image, x, y, engine) {
        this.image = image;
        this.x = x;
        this.y = y;
        this.width = ITEM_WIDTH;
        this.height = ITEM_WIDTH;
        this.engine = engine;
        this.selected = false;
    }

    render() {
        this.engine.render(this.image, this.x, this.y);
        if (this.x <= this.engine.mouse_x && this.engine.mouse_x <= this.x + this.width
            && this.y <= this.engine.mouse_y && this.engine.mouse_y <= this.y + this.height) {
            this.engine.render(assets.inventory_selector, this.x, this.y);
        }
    }

    update() {
        if (this.x <= this.engine.mouse_x && this.engine.mouse_x <= this.x + this.width
            && this.y <= this.engine.mouse_y && this.engine.mouse_y <= this.y + this.height) {
            this.selected = true;
        } else {
            this.selected = false;
        }
    }
}
