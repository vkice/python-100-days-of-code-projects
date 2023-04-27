from turtle import Screen, Turtle
from time import sleep
import random
BALL_SIZE = .7
# Directions converted to turtle coords
UP = 90
NE = 45
NW = 135

DOWN = 270
SE = 315
SW = 225

LEFT = 180
RIGHT = 0
RIGHT_HI = 360


class Ball(Turtle):
    """Ball for the Pong Game with location detection logic"""
    
    def __init__(self):
        """Initializes ball with a random heading towards player paddle"""
        
        super().__init__()
        self.screen = Screen()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=BALL_SIZE, stretch_wid=BALL_SIZE)
        self.player_directions = [0, 7, -7, 15, -15, 33, -33]
        self.computer_directions = [180, 187, 173, 195, 165, 213, 143]
        self.setheading(random.choice(self.player_directions))
    
    
    def move(self):
        """Moves ball across the screen and checks for location"""
        
        self.forward(10)


    def reset(self, who_scored):
        """Player or computer has scored, reset the ball to middle position"""
        
        self.hideturtle()
        self.goto(0, 0)
        if who_scored == 'player':
            self.setheading(random.choice(self.computer_directions))
        elif who_scored == 'computer':
            self.setheading(random.choice(self.player_directions))
        self.screen.update()
        sleep(.5)
        self.showturtle()
        self.screen.update()
        sleep(1)
        