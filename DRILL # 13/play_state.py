from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy


# boy = None
boy = []
grass = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            for i in boy:
                i.handle_event(event)


# 초기화
def enter():
    global boy, grass
    boy = [Boy() for i in range(10)]
    grass = Grass()
    game_world.add_object(grass, 0)
    for i in boy:
        game_world.add_object(i, 1)


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 강제로 성능 저하
    # delay(0.5)
    # 터널링 임팩트 (순간적인 프레임 드랍현상으로 벽을 통과하는 현상)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
