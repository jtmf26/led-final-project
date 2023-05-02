#!/usr/bin/env python3

import time
import math
import random
import colorsys
import controllertest as pad


from gpiozero import Button

from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()
width, height = uh.get_shape()
uh.set_brightness(0.5)



class game():
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
        self.game_on = False
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
        
    def game_over(self):
        self.game_on = False
        for x in range(16):
            for y in range(6):
                uh.set_pixel(x, y, 255, 0, 0)
                
    def start_game(self):
        self.game_on = True
       
    def get_pos_x(self):
            return self.pos_x
            
    def get_pos_y(self):
            return self.pos_y
        
        


class obstacles():
    def __init__(self):
        self.pos_x = 16
        self.pos_y = random.randint(0, 3)
        self.size = random.randint(1, 4)
        self.delay = 0.07

        
    def update(self):
        pos_x_last = self.pos_x
        pos_y_last = self.pos_y
        if self.pos_x > 0:
            self.pos_x = self.pos_x - 1
            for i in range(self.size):
                uh.set_pixel(self.pos_x, self.pos_y + i, 42, 26, 14)
                time.sleep(self.delay)
                uh.set_pixel(pos_x_last, self.pos_y + i, 0, 0, 0)
                
        elif self.pos_x == 0:
            if self.delay > 0.01:
                self.delay -= 0.005
            uh.clear()
            self.pos_x = 16
            self.pos_y = random.randint(0, 3)
            self.size = random.randint(1, 4)
            for i in range(self.size):
                uh.set_pixel(self.pos_x, self.pos_y + i, 42, 26, 14)
                time.sleep(self.delay)
                uh.set_pixel(pos_x_last, self.pos_y + i, 0, 0, 0)
                
                
    def get_pos_y(self):
        return [i + self.pos_y for i in range(self.size)]
      
    def get_pos_x(self):
        return self.pos_x
                
                
                    
game = game()
obstacle = obstacles()


button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)




button_a.when_pressed = game.player_up
button_b.when_pressed = game.player_down
button_x.when_pressed = game.color_picker








while game.game_on == False:
    if pad.buttons(pad.gamepad) == 'X':
        game.start_game()
    
    

while game.game_on:
    game.update()
    obstacle.update()
    obstacle.get_pos_x()
    obstacle.get_pos_y()
    if pad.d_pad(pad.gamepad) == 'LEFT':
        game.player_up()
    elif pad.d_pad(pad.gamepad) == 'RIGHT':
        game.player_down()
    elif pad.buttons(pad.gamepad) == 'A':
        game.color_picker() 
    game.get_pos_x()
    game.get_pos_y()
    if game.get_pos_y() in obstacle.get_pos_y() and game.get_pos_x() == obstacle.get_pos_x():
        game.game_over()
        with open("text.py") as f:
            exec(f.read())
       
        


