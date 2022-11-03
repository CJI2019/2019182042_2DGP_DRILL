from pico2d import *

class Grass:

    def __init__(self):
        self.image = load_image('grass.png')
        self.depth = 0
        self.y = 30

    def draw(self):
        self.image.draw(400, self.y)

    def update(self): pass


