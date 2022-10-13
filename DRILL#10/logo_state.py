from pico2d import *
import game_framework
import title_state
import  play_state
# fill here
image = None
running = True
logo_time = 0.0

def enter():
    # fill here
    global image, logo_time, running
    image = load_image('tuk_credit.png')
    logo_time = 0.0
    running = True
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    # fill here
    global logo_time

    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        # running = False
        game_framework.change_state(play_state)
    pass

def draw():
    # fill here
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()

# enter()
# while running:
#     handle_events()
#     Update()
#     Draw()
#     pico2d.delay(0.05)
# exit()




