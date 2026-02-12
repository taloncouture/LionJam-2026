

class GameContext:
    def __init__(self):
        self.selected_item = None
        self.credits = 10
        self.bricks = 0
        self.required_bricks = [0, 2, 10, 20, 30, 40]
        #self.required_bricks = [0, 1, 2, 3, 4, 5]
        self.pyramid_stage = 0
        self.built = False
        self.turn = 1
        self.production_tiles = 0

        #self.next_network_id = 1