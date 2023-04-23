#!/usr/bin/env python
import time
import math
import random
import colorsys

from gpiozero import Button
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.5)
width, height = unicornhatmini.get_shape()

class Pong():
    def __init__(self):
        # start the paddles roughly halfway vertically
        self.l_paddle_y = 3
        self.r_paddle_y = 3
        self.delay = 0.3
        self.ball_x = 1
        self.ball_y = 1
        self.ball_horiz = 1
        self.ball_vert = 1
        self.game_on = True
        self.paddle_height = 3
        self.colors = (
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (255, 255, 255)
        )
        self.color = random.choice(self.colors)

    def l_paddle_down(self):
        if self.l_paddle_y < height - self.paddle_height:
            self.l_paddle_y += 1

    def l_paddle_up(self):
        if self.l_paddle_y > 0:
            self.l_paddle_y -= 1

    def r_paddle_down(self):
        if self.r_paddle_y < height - self.paddle_height:
            self.r_paddle_y += 1

    def r_paddle_up(self):
        if self.r_paddle_y > 0:
            self.r_paddle_y -= 1

    def update(self):
        # check if the game is over
        if self.ball_x in (0, width - 1):
            self.game_on = False
            return

        # clear the board state
        unicornhatmini.clear()

        # set the position of the paddles
        for i in range(3):
            unicornhatmini.set_pixel(0,
                    self.l_paddle_y + i,
                    255, 255, 255)
            unicornhatmini.set_pixel(width - 1,
                    self.r_paddle_y + i,
                    255, 255, 255)

        # calculate the next position of the ball
        ball_x_next = self.ball_x + self.ball_horiz
        ball_y_next = self.ball_y + self.ball_vert

        # check if the ball needs to bounce off of a paddle
        if (
                (ball_x_next == 0 and ball_y_next in
                    (self.l_paddle_y + i for i in range(3))) or
                (ball_x_next == width - 1 and ball_y_next in
                    (self.r_paddle_y + i for i in range(3)))
            ):
            # the paddle has hit the ball, so change direction
            self.ball_horiz = -self.ball_horiz
            # recalculate ball_x_next
            ball_x_next = self.ball_x + self.ball_horiz

            # since the ball hit a paddle
            # reduce the delay to speed up the game
            self.delay -= 0.01

            # change the color of the ball every time
            # the ball hits a paddle
            self.color = random.choice(self.colors)

        # check if the ball needs to bounce off of an edge
        if (
                (self.ball_y == 6 and self.ball_vert == 1) or
                (self.ball_y == 0 and self.ball_vert == -1)
            ):
            self.ball_vert = -self.ball_vert
            ball_y_next = self.ball_y + self.ball_vert

        self.ball_x = ball_x_next
        self.ball_y = ball_y_next
        unicornhatmini.set_pixel(self.ball_x,
                self.ball_y,
                *self.color)

        # show the game state
        unicornhatmini.show()

pong_game = Pong()

button_a = Button(5)   # left paddle up
button_b = Button(6)   # left paddle down
button_x = Button(16)  # right paddle up
button_y = Button(24)  # right paddle down

button_a.when_pressed = pong_game.l_paddle_up
button_b.when_pressed = pong_game.l_paddle_down
button_x.when_pressed = pong_game.r_paddle_up
button_y.when_pressed = pong_game.r_paddle_down

while pong_game.game_on:
    pong_game.update()
    time.sleep(pong_game.delay)
