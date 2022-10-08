from pico2d import *

BackGround_WITDH , BackGround_HEIGHT = 600,600

# floor 를 저장 할 값a
x = [BackGround_WITDH//2,100]
xcount = 0
y = [BackGround_HEIGHT//20, 200]
ycount = 0
# Floor index : 플레이어가 어디발판에 있는지 확인
level = 0
class FLOOR:
    def __init__(self):
        global x,y,xcount,ycount,level
        # random.randint(0,6)
        self.image = load_image("Floor/floor_01.png")
        if(xcount == 0):
            self.image = load_image("Floor\main_floor_1.png")
        self.level = level
        level += 1
        # floor 의 위치
        self.xPos = x[xcount]
        xcount += 1
        self.yPos = y[ycount]
        ycount += 1
        # floor 의 영역
        self.x1 ,self.y1 = self.xPos - self.image.w//2 + 10, self.yPos + self.image.h//2
        self.x2 ,self.y2 = self.xPos + self.image.w//2 - 10, self.yPos - self.image.h//2
    def Draw(self):
        self.image.draw(self.xPos,self.yPos)
