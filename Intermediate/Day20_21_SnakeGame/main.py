from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep


def update_game():
    """Update the screen and set tick rate for game"""
    screen.update()
    sleep(.15)

# Screen and game initialization
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.update()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for control input
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# Start game
game_running = True
while game_running:
    update_game()
    snake.move()
    
    # Detect if snake reached food
    if snake.snake_head.distance(food) < 15:
        scoreboard.update_score()
        food.move()
        snake.ate_food()
        

    # Detect collision with wall or tail
    if  snake.detect_collision():
        update_game()
        snake.move()
        scoreboard.game_over()
        game_running = False
    
# User clicks to exit game
screen.exitonclick()