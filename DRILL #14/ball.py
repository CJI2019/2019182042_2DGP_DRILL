import random
from pico2d import *
import game_world
import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1800), random.randint(0, 1100)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        # if (server.background.old_left != server.background.window_left):
        # self.x += server.boy.oldX - server.boy.x
        # if server.background.old_bottom != server.background.window_bottom:
        #     self.y += server.boy.oldY - server.boy.y
        self.x += server.background.old_left - server.background.window_left
        self.y += server.background.old_bottom - server.background.window_bottom
        pass

    def get_bb(self):
        return self.x - 20 , self.y - 20, self.x + 20,self.y + 20

    def handle_collision(self,other,group):
        if group == 'boy:ball':
            game_world.remove_object(self)
            server.count += 1
            print(server.count)