from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

def move_rect():#사각형 운동
    x = 0

    y = 90
    while 1 :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 5
        if x > 780 :# 몸이 밖으로 안나가게
            break;
        delay(0.01)
    while 1 :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y += 5
        if y > 550 :# 몸이 밖으로 안나가게
            break;
        delay(0.01)
        
    while 1 :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= 5
        if x < 20 :# 몸이 밖으로 안나가게
            break;
        delay(0.01)
    while 1 :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y -= 5
        if y < 50 :# 몸이 밖으로 안나가게
            break;
        delay(0.01)
        
def move_circle():#원 운동
    x= -60 # 위 에서 원 운동 시작
    grass.draw_now(400,30)
    character.draw_now(400,90)
    
    while 1 :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(200*(math.cos((-x/360)*(2*math.pi)))+400,
                           200*(math.sin((-x/360)*(2*math.pi)))+300)
        x += 1
        if x > 300 :# 한 바퀴 돌면 종료
            break;
        delay(0.01)
        
while 1:
    move_rect()
    move_circle()

close_canvas()
