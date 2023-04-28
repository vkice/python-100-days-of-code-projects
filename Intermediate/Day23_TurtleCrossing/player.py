from turtle import Screen, Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    """Player controlled character for turtle crossing game"""


    def __init__(self):
        """Initializes the player on screen"""
        
        super().__init__()
        self.screen = Screen()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.resizemode("user")
        self.setheading(UP)
        self.goto(STARTING_POSITION)
        self.screen.update()
    
    
    def move(self):
        """Moves the player up the screen"""
        
        self.forward(MOVE_DISTANCE)
        
        
    def at_top(self):
        """Checks if player has reached top of screen returning boolean value"""
        
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
    
    
    def reset(self):
        """Resets the position of the player"""
        
        self.goto(STARTING_POSITION)
        
        
    def detect_collision(self, car_list):
        """Detects if the player has collided with any on screen cars returning a boolean value"""
        
        for car in car_list:
            if (self.distance(car) < 25) and (abs(self.ycor() - car.ycor())) < 19:
                return True
        return False