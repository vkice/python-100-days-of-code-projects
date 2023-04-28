from turtle import Screen, Turtle

# Paddle dimensions
PADDLE_LEN = 3.5
PADDLE_WID = .6

# Directions converted to turtle coords
UP = 90
DOWN = 270

class Paddle(Turtle):
    """Player controller paddle for the Pong game"""

    def __init__(self):
        """Snake starting position"""
        
        super().__init__()
        self.screen = Screen()
        self.shape("square")
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.setheading(UP)
        self.shapesize(stretch_len=PADDLE_LEN, stretch_wid=PADDLE_WID)
        self.goto(350, 0)
        self.screen.update()
        
    
    # Change heading of the player's paddle and moves in that direction, does not let paddle outside of screen
    def up(self):
        """Moves the player paddle up"""
        if self.ycor() < 250:
            self.setheading(UP)
            self.forward(20)
    
    def down(self):
        """Moves the player paddle down"""
        if  self.ycor() > -250:
            self.setheading(DOWN)
            self.forward(20)
    ###
    
    
    