

class GameContext:
    def __init__(self):
        self.selected_item = None
        self.credits = 10000
        self.bricks = 0
        self.required_bricks = 100
        self.turn = 1
        self.production_tiles = 0

        self.next_network_id = 1