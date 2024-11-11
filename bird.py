# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, load_font
from state_machine import *
from ball import Ball
import game_world
import random
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 16)
        self.frame, self.action = 0, 0
        self.w, self.h = 183 / 3, 168 / 3
        self.x, self.y = random.randint(100, 1500), random.randint(100, 500)
        self.speed = 3

        self.rad, self.flip = 0, 0
        self.dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = self.frame + self.speed * FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
        if self.action < 2 and self.frame >= 4:
            self.action += 1
            self.frame = self.frame % 4
        elif self.action == 2 and self.frame >= 3:
            self.action = 0
            self.frame = self.frame % 3
        self.x += self.dir * self.speed * RUN_SPEED_PPS * game_framework.frame_time
        if self.x <= self.w / 2:
            self.dir *= -1
            self.x = self.w / 2
        elif self.x >= 1600 - self.w / 2:
            self.dir *= -1
            self.x = 1600 - self.w / 2

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 183, self.action * 168, 183, 168, self.x, self.y, self.w, self.h)
        else:
            self.image.clip_composite_draw(int(self.frame) * 183, self.action * 168, 183, 168, self.rad, 'h', self.x, self.y, self.w, self.h)
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))