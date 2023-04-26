from turtle import Turtle
ALIGN = "center"
FONT = ("calibri", 16, "bold")
GAME_OVER_FONT = ("calibri", 60, "bold")

class Scoreboard(Turtle):
    """Scoreboard for the Snake Game to keep track of players score"""
    
    def __init__(self):
        """Initializes the Scoreboard for the game"""
        
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.score_total = -1
        self.update_score()
    
    
    def update_score(self):
        """Moves the food to a new location and increases the current score"""
        
        self.score_total += 1
        self.clear()
        self.write(f"Score: {self.score_total}", align=ALIGN, font=FONT)
        
        
    def game_over(self):
        """Game is over, player hit wall or self"""
        
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=GAME_OVER_FONT)