#!/usr/bin/env python3

import time
import math
import random
import colorsys

from gpiozero import Button

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()
uh.set_brightness(0.3)

class JumpingGame():
    def __init__(self):
        self.color = (255, 0, 0)
        self.game_on= True
        self.pos_x = 4
        self.pos_y = 4
        self.size = 2
        
    
    def player_up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            
    def update(self):
        
        
        
        
        uh.set_pixel(self.pos_x, self.pos_y, 255, 255, 255)
        uh.show()
        
        
        


game = JumpingGame()

while game.game_on:
    game.update()
