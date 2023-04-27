from turtle import Screen
from paddle import Paddle
from interface import Interface
import random

# Difficulty of computer, lower the HARD constant to make it hard, increase EASY constant to make it easier
HARD = 30
EASY = 90

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


class ComputerPaddle(Paddle):
    """Player controller paddle for the Pong game"""

    def __init__(self):
        """Snake starting position"""
        
        super().__init__()
        self.screen = Screen()
        self.goto(-350, 0)
        self.screen.update()
        
        
    def track_ball(self, ball_y_cor):
        """Computer paddles follows the current y coordinate of the ball based on tracking number"""

        if abs(self.ycor() - ball_y_cor) < random.randint(HARD, EASY):
            return
        elif ball_y_cor > self.ycor():
            self.up()
        else:
            self.down()


class GameLogic:
    """Core game logic for Pong"""
    
    def __init__(self):
        """"""
        self.interface = Interface()
        
        
    def game_speed(self):
        """Returns a game speed according to the combined scores of player/computer"""
        
        default_speed = .03 # Default speed
        game_speed = default_speed - ((self.interface.player_score + self.interface.computer_score) * .002)
        return game_speed
    
    def detect_ball_loc(self, ball, player_paddle, computer_paddle):
        """Checks if ball has hit a wall, paddle, or went out of bounds"""

        self.detect_walls(ball)
        self.detect_paddle(ball, player_paddle, computer_paddle)
        self.out_of_bounds(ball)
             
        
    def detect_walls(self, ball):
        """Detects if the ball has hit the top or bottom walls of game"""
        
        if ball.ycor() > 285 and ball.heading() in range(RIGHT, UP): # Top wall going right
            ball.setheading(SE)
        elif ball.ycor() > 285 and ball.heading() in range(UP, LEFT): # Top wall going left
            ball.setheading(SW)
        elif ball.ycor() < -285 and ball.heading() in range(LEFT, DOWN): # Bottom wall going right
            ball.setheading(NW)
        elif ball.ycor() < -285 and ball.heading() in range(DOWN, RIGHT_HI): # Bottom wall going left
            ball.setheading(NE)
            
            
    def detect_paddle(self, ball, player_paddle, computer_paddle):
        """Detects if the ball is within range of a paddle"""
        
        if ball.distance(player_paddle) < 40 and ball.xcor() > 335 and ball.xcor() < 370: # Ball approaching right side of screen
            if ball.heading() in range(RIGHT, UP): # Bounces ball up
                ball.setheading(NW)
            elif ball.heading() in range(DOWN, RIGHT_HI): # Bounces ball down
                ball.setheading(SW)
                
        if ball.distance(computer_paddle) < 40 and ball.xcor() < -335 and ball.xcor() > -370: # Ball approaching left side of screen
            if ball.heading() in range(UP, LEFT): # Bounces ball up
                ball.setheading(NE)
            elif ball.heading() in range(LEFT, DOWN): # Bounces ball down
                ball.setheading(SE)
                
                
    def out_of_bounds(self, ball):
        """Detects if the ball has reached out of bounds, assigns the point, and resets to middle."""
        
        if ball.xcor() > 390: # Computer scores
            self.interface.update_score('computer', ball)
        elif ball.xcor() < -390: # Player scores
            self.interface.update_score('player', ball)