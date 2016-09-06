import cocos
from cocos.director import director

import define
from snake import Snake
from dot import Dot

class Arena(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Arena, self).__init__(250, 255, 255, 255, define.WIDTH, define.HEIGHT)
        self.center = (director.get_window_size()[0] / 2, director.get_window_size()[1] / 2)
        self.batch = cocos.batch.BatchNode()
        self.add(self.batch)

        self.snake = Snake()
        self.add(self.snake, 10000)
        self.snake.init_body()

        self.enemies = []
        for i in range(7):
            self.add_enemy()

        self.keys_pressed = set()

        for i in range(50):
            self.batch.add(Dot())

        self.schedule(self.update)

    def add_enemy(self):
        enemy = Snake(True)
        self.add(enemy, 10000)
        enemy.init_body()
        self.enemies.append(enemy)

    def update(self, dt):
        self.x = self.center[0] - self.snake.x
        self.y = self.center[1] - self.snake.y

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.snake.update_angle(self.keys_pressed)

    def on_key_release (self, key, modifiers):
        self.keys_pressed.remove(key)
        self.snake.update_angle(self.keys_pressed)
