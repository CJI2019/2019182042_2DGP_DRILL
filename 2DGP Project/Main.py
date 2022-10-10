from pico2d import *

BackGround_WITDH ,BackGround_HEIGHT  = 600 , 600
#open canvas를 먼저 해야 load image 가능
open_canvas(BackGround_WITDH,BackGround_HEIGHT)

# Player 정보가 담겨있다
import PlayerObject
import FloorObject

BackGround = load_image("back_2_2000.png")

BackGroundHeight = 0

floors = [FloorObject.FLOOR() for i in range(FloorObject.SizeOfFloor())]

# 플레이어 객체 생성
Player = PlayerObject.PLAYER() 
PlayerObject.y = (floors[0].y1) + (Player.Right_Idle.h//2) 

while PlayerObject.play:
    clear_canvas()
    BackGround.clip_draw(0,(int)(BackGroundHeight),BackGround.w,BackGround.h-(int)(BackGroundHeight)
                ,BackGround_WITDH,BackGround_HEIGHT)

    # 0.1 씩 배경 이미지 내려가게함.
    BackGroundHeight += 0.1
    
    for floor in floors:
        floor.Draw()
    Player.Player_Movement(floors)
    PlayerObject.KeyDown_event(floors)
    FloorObject.FloorChange(Player,floors)
    
    update_canvas()

close_canvas()
