from pico2d import *
# import PlayerObject

class WALL:
    def __init__(self,x,y):
        self.image = load_image('wall.png')
        print("생성")
        self.x = x
        self.y = y
        self.x1 , self.y1= x - (self.image.w//2) , y + (self.image.h//2)
        self.x2 , self.y2= x + (self.image.w//2) , y - (self.image.h//2)
        # 화면에 그려질지 말지 플레이어와 부딫히면 그려짐.
        self.status = False
    def Draw(self):
        if not self.status:
            self.image.draw(self.x,self.y)
    def Crash(self,player):
        # x + player.Right_Idle.w//2 와 y + player.Right_Idle.h//2 는 player x1 , y1 
        # 이 둘이 벽의 사각형 내에 있으면 막음. 총 4개의 점
        if (player.x1 > self.x1 and player.x1 < self.x2 and
        player.y1 < self.y1 and player.y1 > self.y2):
            player.WallCrash()
            print("충돌")
        elif (player.x2 > self.x1 and player.x2 < self.x2 and
        player.y1 < self.y1 and player.y1 > self.y2):
            player.WallCrash()
            print("충돌")
        elif (player.x1 > self.x1 and player.x1 < self.x2 and
        player.y2 < self.y1 and player.y2 > self.y2):
            player.WallCrash()
            print("충돌")
        elif (player.x2 > self.x1 and player.x2 < self.x2 and
        player.y2 < self.y1 and player.y2 > self.y2):
            player.WallCrash()
            print("충돌")
