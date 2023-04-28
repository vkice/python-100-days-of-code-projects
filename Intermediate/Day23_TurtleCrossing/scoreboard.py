from turtle import Turtle
from car_manager import CarManager
ALIGN = "center"
FONT = ("Courier", 24, "bold")
GAME_OVER_FONT = ("Courier", 60, "bold")
LEFT = 180
SPAWN_RATE_INC_LEVELS = [4, 7, 10]


class Scoreboard(Turtle):
    """Tracks players highest level reached"""


    def __init__(self):
        """Initializes all of the game elements"""
        
        super().__init__()
        self.cars = CarManager()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(-210, 260)
        self.level_reached = 0
        self.update_level()
    
    
    def update_level(self):
        """Increases the level by one"""
        
        self.level_reached += 1
        if self.level_reached in SPAWN_RATE_INC_LEVELS:
            self.cars.increase_spawn_rate()
        self.clear()
        self.write(f"Level: {self.level_reached}", align=ALIGN, font=FONT)
        
        
    def get_speed(self):
        """Returns the speed cars should move based off current level"""
        
        return ((self.level_reached * 5)/2) + 3
                
        
        
    def game_over(self):
        """Determines if the game is over by score threshold"""
        
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=GAME_OVER_FONT)