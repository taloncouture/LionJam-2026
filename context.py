import config


def coords_to_iso(x, y):

    iso_x = (x - y) * config.HALF_W
    iso_y = (x + y) * config.HALF_H

    return config.ORIGIN_X + iso_x, config.ORIGIN_Y + iso_y

class GameContext:
    def __init__(self):
        self.selected_item = None
        self.credits = 10
        self.bricks = 0
        self.required_bricks = [0, 10, 30, 50, 80, 110]
        #self.required_bricks = [0, 1, 2, 3, 4, 5]
        self.pyramid_stage = 0
        self.built = False
        self.turn = 1
        self.production_tiles = 0
        self.lives = 3

        #self.next_network_id = 1