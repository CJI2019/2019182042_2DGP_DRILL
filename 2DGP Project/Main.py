from pico2d import *

BackGround_WITDH ,BackGround_HEIGHT  = 600 , 600

open_canvas(BackGround_WITDH,BackGround_HEIGHT)

def KeyDown_event():
    global play , xPos , yPos
    events = get_events()
    for event in events:
        if(event.type == SDL_QUIT):
            play =False
        elif (event.type == SDL_KEYDOWN):
            if(event.key == SDLK_RIGHT):
                xPos += 5



# BackGround = load_image(" ")
Player_Left = load_image('characterLeft.png')
Image_WIDTH,Image_HEIGHT = 1024//8 , 489//3
Player_Right = load_image('characterRight.png')

play = True

MoveRight ,MoveLeft = True , False
frame = 0
xPos , yPos = 300,300
count = 0
while play:
    clear_canvas()
    # BackGround.draw(BackGround_WITDH,BackGround_HEIGHT)
    if(MoveRight , MoveLeft == True , False):
        Player_Right.clip_draw(frame*Image_WIDTH,Image_HEIGHT*2
    ,Image_WIDTH,Image_HEIGHT,xPos,yPos)
    update_canvas()

    KeyDown_event()
    frame = ( frame + 1 ) % 8
    delay(0.03)
    count += 1
    if count == 100 :
        break

close_canvas()
