from pico2d import *

GameWindow_WITDH ,GameWindow_HEIGHT  = 600 , 600

class WATER:
    def __init__(self):
        self.image = load_image('Water.png')
        self.x = GameWindow_WITDH//2
        self.y = -self.image.h+300
        self.speed = 0.5
    def drawAupdate(self):
        self.image.draw(self.x,self.y)
        self.y += self.speed

        