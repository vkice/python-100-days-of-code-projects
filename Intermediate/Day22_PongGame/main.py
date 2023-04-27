### Pong game against a computer opponent, play to 5 to win
from game_logic import GameLogic,ComputerPaddle
from paddle import Paddle
from ball import Ball
from turtle import Screen
from time import sleep

WINNING_SCORE = 5
GAME_SPEED = .035

def update_game():
    """Update the screen and set tick rate for game"""
    screen.update()
    sleep(GAME_SPEED)

# Screen and game initialization
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.update()
game_logic = GameLogic()
player_paddle = Paddle()
computer_paddle = ComputerPaddle()
ball = Ball()

# Listen for control input
screen.listen()
screen.onkeypress(player_paddle.up, "Up")
screen.onkeypress(player_paddle.down, "Down")

# Start game
sleep(1)
game_running = True
while game_running:
    update_game() # Speed of game
    ball.move() # Keeps ball moving
    computer_paddle.track_ball(ball.ycor()) # Computer follows ball
    game_logic.detect_ball_loc(ball, player_paddle, computer_paddle) # Determine if ball should bounce or out of bounds
    
    GAME_SPEED = game_logic.game_speed()
    
    if game_logic.interface.game_over(WINNING_SCORE): # Check if the score reaches 5 and game is over
        game_running = False

# User clicks to exit game
screen.exitonclick()