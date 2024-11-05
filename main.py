from pico2d import *
import play_mod

open_canvas()
play_mod.init()
# game loop
while play_mod.running:
    play_mod.handle_events()
    play_mod.update()
    play_mod.draw()
    delay(0.01)
# finalization code
play_mod.finish()
close_canvas()
