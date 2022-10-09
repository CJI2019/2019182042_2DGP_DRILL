from pico2d import *

BackGround_WITDH , BackGround_HEIGHT = 600,600

# floor 를 저장 할 값a
x = [BackGround_WITDH//2  ,200,400,400,400,400,400,400]
xcount = 0
y = [BackGround_HEIGHT//20,200,300,400,500,600,700,800]
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


def SizeOfFloor():
    return len(x)

# 플레이어 현재 floor 레벨
Player_Floor_Level = 0
# floor 레벨 변화
FloorLevelAnimeCount = 0
# floor 에 따른 애니메이션 속도
FloorLevelAnimeSpeed = 9 

def FloorChange(Player,floors):
    global Player_Floor_Level ,FloorLevelAnimeCount,FloorLevelAnimeSpeed
    
    if (Player_Floor_Level != Player.CompliteLevel and FloorLevelAnimeCount == 0):
        FloorLevelAnimeCount = (Player_Floor_Level - Player.CompliteLevel) * FloorLevelAnimeSpeed # 높아 지면 음수 
        Player_Floor_Level = Player.CompliteLevel
        
    if(FloorLevelAnimeCount != 0):
        # 한 단계당 FloorLevelAnimeSpeed 에 따라 위치 변함.
        for floor in floors:
            if FloorLevelAnimeCount > 0:
                floor.y1 += FloorLevelAnimeSpeed; floor.y2 += FloorLevelAnimeSpeed
                floor.yPos += FloorLevelAnimeSpeed
            else :
                floor.y1 -= FloorLevelAnimeSpeed; floor.y2 -= FloorLevelAnimeSpeed
                floor.yPos -= FloorLevelAnimeSpeed
        # 플레이어 좌표 y값 floor 에 맞추기
        Player.CoordinateInput(floors[Player.CompliteLevel].y1 + Player.Right_Idle.h//2)
        if FloorLevelAnimeCount > 0 :
            FloorLevelAnimeCount -= 1
        else:
            FloorLevelAnimeCount += 1