import random
import turtle as t
from turtle_colors import TurtleColors
from turtle import Screen


class TurtleRacer:
    """Initializes each of the racers"""
    
    
    def __init__(self, turtle_color, y_axis):
        """Initializes each colored turtle racer with it's starting position"""
        
        
        self.turtle = t.Turtle(shape="turtle")
        self.turtle.penup()
        self.turtle.color(turtle_color)
        self.turtle.goto(x=-234, y=y_axis)
        self.racer_color = turtle_color


class Race:
    """Main function to initiate the turtle racers and race itself"""
    
    
    def __init__(self):
        """Initializes all the turtle racers from color list"""
        
        
        self.turtle_colors = TurtleColors()
        self.racers = []
        y_axis = -90 # Increasing by 30 for each of the 6 turtles, for even distribution across left side of screen
        for turtle_color in self.turtle_colors.colors_list:
            self.racers.append(TurtleRacer(turtle_color, y_axis))
            y_axis += 30


    def start_race(self):
        """Starts the race by asking user for who they think will win, then randomly moves turtles forward, declares winner, then prompts user to continue"""
        
        
        self.screen = Screen()
        user_choice = self.screen.textinput(title="Turtle Race", prompt=f"Which color turtle will win the race? ({self.turtle_colors.get_colors()})\nPick a color: ")
        still_racing = True
        while still_racing:
            for racing_turtle in self.racers:
                racing_turtle.turtle.forward(random.randint(5,12))
                if racing_turtle.turtle.xcor() >= 230: #Turtle crossed finish line and won
                    if user_choice == racing_turtle.racer_color:
                        return self.screen.textinput(title="Turtle Race", prompt=f"You were correct! The {racing_turtle.racer_color} has won the race!\n"
                                                     "Do you want to have another race? Type 'yes' otherwise type 'no'")
                    return self.screen.textinput(title="Turtle Race", prompt=f"You guessed {user_choice} turtle would win and they have lost! The "
                                                 f"{racing_turtle.racer_color} turtle has won the race.\n"
                                                 "Do you want to have another race? Type 'yes' otherwise type 'no' or hit the Cancel button.")