# -*- coding: utf-8 -*-
import cocos
from cocos.director import director
import define

class Gameover(cocos.layer.ColorLayer):
    def __init__(self):
        super(Gameover, self).__init__(200, 235, 235, 200, 400, 300)
        self.position = (director.get_window_size()[0] / 2 - 200,
                         director.get_window_size()[1] / 2 - 150)
        self.visible = False
        self.score = cocos.text.Label('',
                                      font_name='SimHei',
                                      font_size=36,
                                      color=define.MAROON)
        self.score.position = 250, 200
        self.add(self.score)

        text = cocos.text.Label('SCORE: ',
                                font_name='SimHei',
                                font_size=24,
                                color=define.MAROON)
        text.position = 50, 200
        self.add(text)
        text = cocos.text.Label('CLICK TO REPLAY...',
                                font_name='SimHei',
                                font_size=24,
                                color=define.MAROON)
        text.position = 50, 100
        self.add(text)
