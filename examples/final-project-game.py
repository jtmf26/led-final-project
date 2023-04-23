#!/usr/bin/env python3

import time
import math
import random
import colorsys


from gpiozero import Button

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()
width, height = uh.get_shape()
uh.set_brightness(0.5)

class JumpingGame():
    def __init__(self):
        self.colors = (
            (255, 0, 0),
            (252, 123, 3),
            (252, 215, 3),
            (0, 255, 0),
            (113, 214, 245),
            (0, 0, 255),
            (145, 13, 212),
            (247, 37, 202))
        self.game_on= True
        self.pos_x = 4
        self.pos_y = 4
        self.size = 2
        self.color = random.choice(self.colors)
        
    
    def player_up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            uh.set_pixel(self.pos_x, (self.pos_y + 1), 0, 0, 0)
      
            
    def player_down(self):
        if self.pos_y <= height - self.size:
            self.pos_y += 1
            uh.set_pixel(self.pos_x, (self.pos_y - 1), 0, 0, 0)
        
 
    def color_picker(self):
        self.color = random.choice(self.colors)
            
            
            
    def update(self):
        uh.set_pixel(self.pos_x, self.pos_y, *self.color)
        uh.show()

        
        
        


game = JumpingGame()

button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)

button_a.when_pressed = game.player_up
button_b.when_pressed = game.player_down
button_x.when_pressed = game.color_picker

while game.game_on:
    game.update()
