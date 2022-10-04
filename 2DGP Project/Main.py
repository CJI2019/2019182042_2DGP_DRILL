from pico2d import *

# 점프 높이
JUMPHEIGHT = 14

BackGround_WITDH ,BackGround_HEIGHT  = 600 , 600

open_canvas(BackGround_WITDH,BackGround_HEIGHT)

def KeyDown_event():
    global play , xPos , yPos ,MoveLeft ,MoveRight ,dir ,JUMPKEYDOWN
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
            if(event.key == SDLK_SPACE):
                if yPos != 0:
                    continue
                yPos = JUMPHEIGHT
                JUMPKEYDOWN = True
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

BackGround = load_image("BackGround.jpg")

Player_Left_Idle = load_image('Player\player_left_idle.png')
Player_Right_Idle = load_image('Player\player_right_idle.png')

Player_Left_Run = load_image('Player\player_left_run.png')
Player_Right_Run = load_image('Player\player_right_run.png')

Player_Left_Jump = load_image('Player\player_left_jump.png')
Player_Right_Jump = load_image('Player\player_right_jump.png')
Player_Left_Fall = load_image('Player\player_left_fall.png')
Player_Right_Fall = load_image('Player\player_right_fall.png')

play = True

MoveRight ,MoveLeft = False , False
JUMPKEYDOWN = False
FALLING = False
frame = 0
x,y = 300 , 300
xPos , yPos = 0,0

# dir 0 이면 오른쪽 1 이면 왼쪽을 마지막에 봄.
dir = 0

Current_KeyDown_List = [0,0]

while play:
    clear_canvas()
    BackGround.draw(BackGround_WITDH/2,BackGround_HEIGHT/2)
    if(JUMPKEYDOWN == False):
        if(MoveRight == True and MoveLeft == False):
            frame = ( frame + 1 ) % 10
            Player_Right_Run.clip_draw(frame*(Player_Right_Run.w//10), 0, Player_Right_Run.w//10, Player_Right_Run.h,x,y)
            delay(0.01)
        elif(MoveRight == False and MoveLeft == True):
            frame = ( frame + 1 ) % 10
            Player_Left_Run.clip_draw(frame*(Player_Left_Run.w//10), 0, Player_Left_Run.w//10, Player_Left_Run.h,x,y)
            delay(0.01)
        elif(MoveRight == False and MoveLeft == False):
            frame = ( frame + 1 ) % 7
            if(dir == 0):
                Player_Right_Idle.clip_draw(frame*(Player_Right_Idle.w//7), 0,Player_Right_Idle.w//7,Player_Right_Idle.h,x,y)
            else :
                Player_Left_Idle.clip_draw(frame*(Player_Left_Idle.w//7), 0,Player_Left_Idle.w//7,Player_Left_Idle.h,x,y)
            delay(0.05)
    elif (JUMPKEYDOWN == True):
        frame = ( frame + 1 ) % 3
        if yPos != 0:
            if FALLING == False: # 점프로 올라가는 애니메이션
                y += yPos
                if dir == 0: 
                    Player_Right_Jump.clip_draw(frame*(Player_Right_Jump.w//3), 0,Player_Right_Jump.w//3,Player_Right_Jump.h,x,y)
                elif dir == 1:
                    Player_Left_Jump.clip_draw(frame*(Player_Left_Jump.w//3), 0,Player_Left_Jump.w//3,Player_Left_Jump.h,x,y)
            elif FALLING == True: # 점프 이후 떨어지는 애니메이션
                if yPos <= JUMPHEIGHT :
                    y -= yPos
                if dir == 0: 
                    Player_Right_Fall.clip_draw(frame*(Player_Right_Fall.w//3), 0,Player_Right_Fall.w//3,Player_Right_Fall.h,x,y)
                elif dir == 1:
                    Player_Left_Fall.clip_draw(frame*(Player_Left_Fall.w//3), 0,Player_Left_Fall.w//3,Player_Left_Fall.h,x,y)
            yPos -= 1
            if(yPos == 0 ):
                if FALLING == True :
                    FALLING = False
                    JUMPKEYDOWN = False
                else :
                    FALLING = True
                    yPos = JUMPHEIGHT + 7 # + 7 은 공중에서 체공하는 시간정도를 나타냄.
        delay(0.01)
    

    update_canvas()

    KeyDown_event()
    
    x += xPos * 4

close_canvas()
