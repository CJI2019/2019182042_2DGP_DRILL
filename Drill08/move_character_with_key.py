from pico2d import *

TUK_WIDTH , TUK_HEIGHT = 800 , 600

def Not_Move(x): # 다른 키를 누르고 있을때 idle 상태 안바꾸도록
    global  dirKeyDown
    global dirLeft,dirRight
    temp = 0
    for i in dirKeyDown:
        if (i == 1):
            temp += 1
    if (temp == 1):
        dirLeft, dirRight = False, False
    dirKeyDown[x] = 0

def handle_events():
    # fill here
    global running , dirLeft,dirRight
    global dirx , diry , dirData,dirKeyDown
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirLeft , dirRight= False, True
                dirKeyDown[0] = 1
                dirData = 0
                dirx +=1
            elif event.key == SDLK_LEFT:
                dirLeft , dirRight= True , False
                dirKeyDown[1] = 1
                dirData = 1
                dirx -=1
            elif event.key == SDLK_UP:
                if dirData == 0:
                    dirLeft, dirRight = False, True
                elif dirData == 1:
                    dirLeft , dirRight= True , False
                dirKeyDown[2] = 1
                diry +=1
            elif event.key == SDLK_DOWN:
                if dirData == 0:
                    dirLeft, dirRight = False, True
                elif dirData == 1:
                    dirLeft, dirRight = True, False
                dirKeyDown[3] = 1
                diry -=1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                Not_Move(0)
                if dirKeyDown[1] == 1:
                    dirLeft ,dirRight= True, False
                dirx -= 1
            elif event.key == SDLK_LEFT:
                Not_Move(1)
                if dirKeyDown[0] == 1:
                    dirLeft ,dirRight= False, True
                dirx += 1
            elif event.key == SDLK_UP:
                Not_Move(2)
                diry -= 1
            elif event.key == SDLK_DOWN:
                Not_Move(3)
                diry += 1
    pass


open_canvas(TUK_WIDTH,TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = 90
frame = 0
dirx ,diry = 0,0

dirLeft,dirRight = False, False
dirData, dirKeyDown = 0 , [0,0,0,0]

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dirRight == True and dirLeft == False:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dirLeft == True and dirRight == False:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif dirLeft == False and dirRight == False and dirData == 1: # 기존 방향이 오른쪽 일때 Idle
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    elif dirLeft == False and dirRight == False and dirData == 0:# 기존 방향이 왼쪽 일때 Idle
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    if x < 20 :
        x += 5
    elif x > TUK_WIDTH-20:
        x -= 5
    y += diry * 5
    if y < 40 :
        y += 5
    elif y > TUK_HEIGHT-40:
        y -= 5
    delay(0.01)

close_canvas()

