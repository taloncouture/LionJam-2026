import config

animations = set()

class Animation():
    def __init__(self, x, y, frames, speed, loop=False):
        self.frames = frames
        self.speed = speed
        self.is_looping = loop
        self.frames.append(frames[-1])
        self.x = x
        self.y = y
        self.active = True
        animations.add(self)

        self.index = 0
        #animations.add(self)

    def update(self):
        if(self.is_looping == False):
            self.index += self.speed
            if(self.index >= len(self.frames) - 1):
                self.active = False
                return False
            return True
        
    def render(self, surface):
        surface.blit(self.frames[int(self.index)], (self.x, self.y - config.HALF_W - config.SCALE_FACTOR))