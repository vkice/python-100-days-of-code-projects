import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
cars = CarManager()

# Listen for control input
screen.listen()
screen.onkeypress(player.move, "Up")

# Start game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move(scoreboard.get_speed())
    
    # Check if player has reached top of screen
    if player.at_top():
        player.reset()
        scoreboard.update_level()

    # Check if player has collided with a car
    if player.detect_collision(cars.car_list):
        screen.update()
        scoreboard.game_over()
        game_is_on = False
    
    
# User clicks to exit game
screen.exitonclick()