import turtle as t
from turtle import Screen
from turtle_racers import Race

t.setup(width=500, height=400)
screen = Screen()
screen.title("Turtle Race")
race = Race()
is_racing = True

while is_racing:
    if race.start_race() == 'yes':
        screen.clear() # Clear winning turtles
        race = Race() # Reinitialize turtles and their positions
    else:
        is_racing = False # End races
