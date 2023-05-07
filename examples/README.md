To start the game press the X button, or the one on the top of the right side on the game controller. Once the game has started, a small colored dot appears that represents the player. To change the color of your player simply press the A button, or the one on the right, until you find the color you most like. The objective of the game is to avoid the obstacles as they fall from the sky. Once you have hit the start button, the game has begun and the objects will begin to fall. Using the left and right arrow buttons on the left side of the controller, you can move your player left and right to avoid hitting the falling obstacles. If you fail to avoid one of the obstacles, the game is over and you lose. To start the game again press Y or the button on the left to restart the game. If you don't want to restart the game press the up arrow on the top to quit. Good luck!

Jason's Favorite Code

Molly's Favorite Code

Erica's Favorite Code
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

