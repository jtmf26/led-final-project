# Unicorn HAT Mini

[![Build Status](https://travis-ci.com/pimoroni/unicornhatmini-python.svg?branch=master)](https://travis-ci.com/pimoroni/unicornhatmini-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/unicornhatmini-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/unicornhatmini-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/unicornhatmini.svg)](https://pypi.python.org/pypi/unicornhatmini)
[![Python Versions](https://img.shields.io/pypi/pyversions/unicornhatmini.svg)](https://pypi.python.org/pypi/unicornhatmini)

# Requirements

You must enable SPI on your Raspberry Pi:

* Run: `sudo raspi-config nonint do_spi 0`

# Installing

Stable library from PyPi:

* Just run `sudo pip3 install unicornhatmini`

Or for Python 2:

* `sudo pip install unicornhatmini`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/unicornhatmini-python`
* `cd unicornhatmini-python`
* `sudo ./install.sh`

# London Bridge
---
To start the game press the X button, or the one on the top of the right side on the game controller. Once the game has started, a small colored dot appears that represents the player. To change the color of your player simply press the A button, or the one on the right, until you find the color you most like. The objective of the game is to avoid the obstacles as they fall from the sky. Once you have hit the start button, the game has begun and the objects will begin to fall. Using the left and right arrow buttons on the left side of the controller, you can move your player left and right to avoid hitting the falling obstacles. If you fail to avoid one of the obstacles, the game is over and you lose. To start the game again press Y or the button on the left to restart the game. If you don't want to restart the game press the up arrow on the top to quit. Good luck!

Jason's Favorite Code
---
    def get_pos_x(self):
            return self.pos_x
            
    def get_pos_y(self):
            return self.pos_y
   ----
    def get_pos_y(self):
        return [i + self.pos_y for i in range(self.size)]
      
    def get_pos_x(self):
        return self.pos_x
----
    if game.get_pos_y() in obstacle.get_pos_y() and game.get_pos_x() == obstacle.get_pos_x():
        game.game_over()
        with open("text.py") as f:
            exec(f.read())

---

My favorite part of the code are the lines that handle the player - object collisions. Each class has a getter to find the x and y position. In the case of the obstacle, I had to use list comprehension to add all the y elements to a list. Then it checks to see if the y position of the player is in the list of y positions for the obstacle, and if the x positions are the same. If they are, it executes the text.py file, an example file that was included in the unicorn hat mini repo, which flashes game over
    
 
                

Molly's Favorite Code
---
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
___

My favorite part of the code is the obstacles class because it constitutes the obstacles that move across the Unicorn Hat and without these the game would lose its gameplay component. Essentially, this chunk of code is what makes the game a game. The update method specifically is my favorite smaller chunk of code within the obstacles class because it is what makes the obstacles move across the Unicorn Hat. The update method is called when the game updates, and it subtracts 1 from the obstacles x position if its x position is greater than 0, moving it down (technically left but down if you hold the LED matrix vertically). When the obstacle's x positon reaches 0, the x position will be set back to 16 (the top), the y position and size of the obstacle will be randomized, and the delay for the obstacle to move down by 1 will be reduced by 0.005 seconds. Reducing the delay makes the obstacle fall faster every time it reaches 0, so the game gets harder as you continue. 

Another couple of reasons I like this part of the code are because it represents one of the two classes that we used -- and classes were an important concept from this course because they are a key part of object-oriented programming -- and because it was one of the obstacles (get it) that we ran into during this process and overcame.




Erica's Favorite Code
---
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
---

My favorite part of the code was the initializer of the class game because it is essentially the backbone of our project. I specifically liked the colors part because we were able to not just make the game cool technically, but also add a fun creative twist to it. Also we were able to use a tuple to do it learning a bit more about lists within Python on the way. Additionally, I got to experience how to make something random in Python as we struggled a little bit with that before figuring it out. List comprehension is one of the important topics of our class and I feel as thought this part of the code allowed me to both understand that better and add a fun twist to our game at the same time.

Citations

Chatterjee, C. C. (2019, July 31). Basics of the classic CNN. Medium. Retrieved May 2, 2023, from https://towardsdatascience.com/basics-of-the-classic-cnn-a3dce1225add 

Engber, D. (2005, September 2). How do they estimate hurricane damage? Slate Magazine. Retrieved May 2, 2023, from https://slate.com/news-and-politics/2005/09/how-do-they-estimate-hurricane-damage.html#:~:text=Risk%2Dmodeling%20companies%20predict%20damage,the%20storm%20at%20various%20locations 

Mandal, M. (2023, April 28). Introduction to convolutional neural networks (CNN). Analytics Vidhya. Retrieved May 2, 2023, from https://www.analyticsvidhya.com/blog/2021/05/convolutional-neural-networks-cnn/ 

