from pico2d import *

BackGround_WITDH ,BackGround_HEIGHT  = 600 , 600
#open canvas를 먼저 해야 load image 가능
open_canvas(BackGround_WITDH,BackGround_HEIGHT)

# Player 정보가 담겨있다
import PlayerObject

BackGround = load_image("BackGround.jpg")

while PlayerObject.play:
    clear_canvas()
    BackGround.draw(BackGround_WITDH/2,BackGround_HEIGHT/2)
    PlayerObject.Player_Movement()
    PlayerObject.KeyDown_event()

    update_canvas()

close_canvas()
