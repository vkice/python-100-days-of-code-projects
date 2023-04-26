from turtle import Turtle
import random

class Food(Turtle):
    """Food for the Snake Game to randomly spawn"""
    
    def __init__(self):
        """Initializes based off the Turtle class"""
        
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.color("cyan")
        self.speed("fastest")
        self.goto(random.randint(-275, 275), random.randint(-275, 260))
    
    
    def move(self):
        """Moves the food to a new location"""
        self.goto(random.randint(-275, 275), random.randint(-275, 260))