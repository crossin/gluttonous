# -*- coding: utf-8 -*-
import random
from cocos.actions import MoveTo, CallFuncS
from cocos.sprite import Sprite

import define


def kill(spr):
    spr.unschedule(spr.update)
    arena = spr.parent.parent
    if not spr.is_big:
        arena.batch.add(Dot())
        spr.killer.add_score()
    else:
        spr.killer.add_score(2)
    arena.batch.remove(spr)
    if not spr.killer.is_enemy:
        arena.parent.update_score()
    del spr

class Dot(Sprite):
    def __init__(self, pos=None, color=None):
        if color is None:
            color = random.choice(define.ALL_COLOR)

        super(Dot, self).__init__('circle.png', color=color)
        self.killed = False
        if pos is None:
            self.position = (random.randint(40, define.WIDTH - 40),
                             random.randint(40, define.HEIGHT - 40))
            self.is_big = False
            self.scale = 0.8
        else:
            self.position = (pos[0] + random.random() * 32 - 16,
                             pos[1] + random.random() * 32 - 16)
            self.is_big = True
        self.schedule_interval(self.update, random.random() * 0.2 + 0.1)

    def update(self, dt):
        arena = self.parent.parent
        snake = arena.snake
        self.check_kill(snake)
        for s in arena.enemies:
            self.check_kill(s)

    def check_kill(self, snake):
        if (not self.killed and not snake.is_dead) and (
            abs(snake.x - self.x) < 32 and abs(snake.y - self.y) < 32
        ):
            self.killed = True
            self.killer = snake
            self.do(MoveTo(snake.position, 0.1) + CallFuncS(kill))
