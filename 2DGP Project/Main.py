from pico2d import *

BackGround_WITDH ,BackGround_HEIGHT  = 600 , 600
#open canvas를 먼저 해야 load image 가능
open_canvas(BackGround_WITDH,BackGround_HEIGHT)

# Player 정보가 담겨있다
import PlayerObject

BackGround = load_image("back_2_2000.png")
Main_Floor = load_image("Floor\main_floor_1.png")

BackGroundHeight = 0

PlayerObject.y =(BackGround_HEIGHT//20) + (Main_Floor.h//2) + (PlayerObject.Player_Right_Idle.h//2) 

while PlayerObject.play:
    clear_canvas()
    BackGround.clip_draw(0,0+(int)(BackGroundHeight),BackGround.w,BackGround.h-(int)(BackGroundHeight),BackGround_WITDH//2,BackGround_HEIGHT//2)
    Main_Floor.draw(BackGround_WITDH//2,BackGround_HEIGHT//20)

    # 0.1 씩 배경 이미지 내려가게함.
    BackGroundHeight += 0.1

    PlayerObject.Player_Movement()
    PlayerObject.KeyDown_event()

    update_canvas()

close_canvas()
