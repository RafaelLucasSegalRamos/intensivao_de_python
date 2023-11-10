import arcade
import random
import math

width = 800
height = 600
title = "Space Invaders"


class Snow_Fall():
    def __init__(self):
        self.x, self.y = 0

    def reset_snow(self):
        self.x = random.randrange(width)
        self.y = random.randrange(height, height + 100)


class Fall(arcade.Window):
    def __init__(self, width, heigth, title):
        super().__init__(width, heigth, title)

    def start_snowfall(self):
        self.snowfall_list = []
        for i in range(500):
            snowfall = Snow_Fall()
            snowfall.x = random.randrange(width)
            snowfall.y = random.randrange(height)

            snowfall.size = random.randrange(8)
            snowfall.speed = random.randrange(20, 40)
            snowfall.angle = random.uniform(math.pi, math.pi * 2)

            self.snowfall_list.append(snowfall)

    def on_draw(self):
        arcade.start_render()
        for snowfall in self.snowfall_list:
            arcade.draw_circle_filled(snowfall.x, snowfall.y, snowfall.size, arcade.color.WHITE)

    def on_update(self, delta_time):
        for snowfall in self.snowfall_list:
            snowfall.y -= snowfall.speed * delta_time
            snowfall.x += snowfall.speed * math.cos(snowfall.angle) * delta_time

            if snowfall.y < 0:
                snowfall.reset_snow()
            snowfall.x += snowfall.speed * math.cos(snowfall.angle) * delta_time
            snowfall.angle += 1 * delta_time


screen = Fall(width, height, title)

# No meu não funcionou por erro de driver, o Erro: pyglet.gl.lib.MissingFunctionException: glCreateShader is not exported by the available OpenGL driver.  OpenGL 2.0 is required for this functionality.
