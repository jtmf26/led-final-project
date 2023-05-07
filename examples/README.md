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

My favorite part of the code are the lines that handle the player - object collisions. Each class has a getter to find the x and y position. In the case of the obstacle, I had to use list comprehension to add all the y elements to a list. Then in checks to see if the y position of the player is in the list of y positions for the obstacle, and if the x positions are the same. If they are, it executes the text.py file, an example file that was included in the unicorn hat mini repo, which flashes game over
    
 
                

Molly's Favorite Code
---

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