import pico2d
from pico2d import *
import game_framework
import title_state
import  play_state
from random import randint
# fill here
image = None

def enter():
    # fill here
    print('item enter')
    global image
    # image = load_image('pause.png')
    image = load_image('add_delete_boy.png')

def exit():
    global image
    print('item exit')
    del image

def update():
    pass

def draw():
    # fill here
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                # case pico2d.SDLK_0:
                #     # game_framework.stack[-2].boy.item = 'BigBall'
                #     play_state.boy.item = None
                #     game_framework.pop_state()
                # case pico2d.SDLK_1:
                #     # game_framework.stack[-2].boy.item = 'BigBall'
                #     play_state.boy.item = 'BigBall'
                #     game_framework.pop_state()
                # case pico2d.SDLK_2:
                #     # game_framework.stack[-2].boy.item = 'BigBall'
                #     play_state.boy.item = 'Ball'
                #     game_framework.pop_state()
                case pico2d.SDLK_KP_PLUS:
                    play_state.team += [play_state.Boy()]
                    play_state.team[-1].x = randint(0, 800)
                    # game_framework.pop_state()
                case pico2d.SDLK_KP_MINUS:
                    if len(play_state.team) > 1:
                        play_state.team.pop(-1)
                case pico2d.SDLK_PLUS:
                    play_state.team += [play_state.Boy()]
                    play_state.team[-1].x = randint(0,800)
                    # game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    if len(play_state.team) > 1:
                        play_state.team.pop(-1)


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()



