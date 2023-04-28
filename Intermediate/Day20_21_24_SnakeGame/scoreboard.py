from turtle import Turtle
ALIGN = "center"
FONT = ("calibri", 16, "bold")
GAME_OVER_FONT = ("calibri", 60, "bold")
HIGH_SCORE_LOCATION = "high_score.txt"

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
        with open(HIGH_SCORE_LOCATION) as file:
            self.high_score = int(file.read())
        self.update_score()
    
    
    def update_score(self):
        """Moves the food to a new location and increases the current score"""
        
        self.score_total += 1
        self.clear()
        self.write(f"Score: {self.score_total}  High Score: {self.high_score}", align=ALIGN, font=FONT)
        
        
    def reset_game(self):
        """Game is over, player hit wall or self, update high score and reset"""
        
        if self.score_total > self.high_score:
            self.high_score = self.score_total
            with open(HIGH_SCORE_LOCATION, mode="w") as file:
                file.write(str(self.high_score))
        self.score_total = -1
        self.update_score()
        # self.goto(0, 0)
        # self.write(f"GAME OVER", align=ALIGN, font=GAME_OVER_FONT)