from pico2d import *

BackGround_WITDH ,BackGround_HEIGHT  = 600 , 600

open_canvas(BackGround_WITDH,BackGround_HEIGHT)

def KeyDown_event():
    global play , xPos , yPos ,MoveLeft ,MoveRight ,dir
    events = get_events()

    for event in events:
        if(event.type == SDL_QUIT or event.key == SDLK_ESCAPE):
            play = False
        elif (event.type == SDL_KEYDOWN):
            if(event.key == SDLK_RIGHT):
                MoveRight ,MoveLeft = True ,False
                dir = 0
                Current_KeyDown_List[0] = 1
                xPos += 1
            if(event.key == SDLK_LEFT):
                MoveRight ,MoveLeft = False , True
                dir = 1
                Current_KeyDown_List[1] = 1
                xPos -= 1
        elif (event.type == SDL_KEYUP):
            if(event.key == SDLK_RIGHT):
                Current_KeyDown_Status()
                Current_KeyDown_List[0] = 0
                if Current_KeyDown_List[1] == 1 :
                    MoveRight ,MoveLeft = False , True
                xPos -= 1
            if(event.key == SDLK_LEFT):
                Current_KeyDown_Status()
                Current_KeyDown_List[1] = 0
                if Current_KeyDown_List[0] == 1 :
                    MoveRight ,MoveLeft = True , False
                xPos += 1

# 현재 다른 키와 같이 눌려있는지 상태 확인 하나만 눌려있으면 idle 상태로
def Current_KeyDown_Status():
    global Current_KeyDown_List , MoveRight ,MoveLeft
    temp = 0
    for i in Current_KeyDown_List:
        if i == 1:
            temp +=1
    if temp == 1 :
        MoveRight ,MoveLeft = False ,False

# BackGround = load_image(" ")
Player_Left = load_image('characterLeft_512x245.png')
Player_Right = load_image('characterRight_512x245.png')

# 플레이어 이미지 크기
Image_WIDTH,Image_HEIGHT = 512//8 , 245//3

play = True

MoveRight ,MoveLeft = False , False
frame = 0
x,y = 300 , 300
xPos , yPos = 0,0

# dir 0 이면 오른쪽 1 이면 왼쪽을 마지막에 봄.
dir = 0

Current_KeyDown_List = [0,0]

while play:
    clear_canvas()
    # BackGround.draw(BackGround_WITDH,BackGround_HEIGHT)
    if(MoveRight == True and MoveLeft == False):
        Player_Right.clip_draw(frame*Image_WIDTH,Image_HEIGHT*2,Image_WIDTH,Image_HEIGHT,x,y)
    elif(MoveRight == False and MoveLeft == True):
        Player_Left.clip_draw((7-frame)*Image_WIDTH,Image_HEIGHT*2,Image_WIDTH,Image_HEIGHT,x,y)
    elif(MoveRight == False and MoveLeft == False):
        if(dir == 0):
            Player_Right.clip_draw(3*Image_WIDTH , Image_HEIGHT*0,Image_WIDTH,Image_HEIGHT,x,y)
        else :
            Player_Left.clip_draw(4*Image_WIDTH , Image_HEIGHT*0,Image_WIDTH,Image_HEIGHT,x,y)

    update_canvas()

    KeyDown_event()
    frame = ( frame + 1 ) % 8

    delay(0.03)
    x += xPos * 5
    y += yPos * 5

close_canvas()
