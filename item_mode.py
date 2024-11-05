import game_framework
from pico2d import*

import game_world
from pannel import Pannel
import play_mod


def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 3)

def finish():
    game_world.remove_object(pannel)

def update():
    pass

def draw():
    clear_canvas()
    pannel.draw()
    update_canvas()

def handle_events(play_mode=None):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_mode()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0):
            play_mode.boy.set_item('NONE')
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            play_mode.boy.set_item('SmallBall')
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            play_mode.boy.set_item('BigBall')

def pause():
    pass

def resume():
    pass
