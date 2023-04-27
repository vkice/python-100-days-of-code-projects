from turtle import Turtle

# Interface Elements
ALIGN = "center"
FONT = ("calibri", 60, "bold")
GAME_OVER_FONT = ("calibri", 40, "bold")
SPACES = "          "

# Directions converted to turtle coords
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Interface(Turtle):
    """Game interface for Pong including the scoreboard"""
    
    def __init__(self):
        """Initializes all of the game elements"""
        
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.interface_components = []
        self.create_scoreboard()
        self.center_line()
    
    
    def center_line(self):
        """Creates the center line of the game"""
        
        self.goto(0, -300)
        self.setheading(UP)
        for i in range(100):
            self.forward(10)
            if i % 2 == 0:
                self.penup()
            else:
                self.pendown()
    
    
    def create_scoreboard(self):
        """Initializes the Scoreboard for the game"""
        
        scoreboard = Turtle()
        scoreboard.hideturtle()
        scoreboard.penup()
        scoreboard.pencolor("white")
        scoreboard.goto(0, 220)
        self.interface_components.append(scoreboard)
        self.scoreboard = self.interface_components[0]
        self.player_score = 0
        self.computer_score = 0
        self.update_score('init', None)
    
    
    def update_score(self, who_scored, ball):
        """Updates the score based on who scores a point"""
        if who_scored == 'player':
            self.player_score += 1
        elif who_scored == 'computer':
            self.computer_score += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"{self.computer_score}{SPACES}{self.player_score}", align=ALIGN, font=FONT)
        if ball != None:
            if who_scored == 'player':
                ball.reset('player')
            elif who_scored == 'computer':
                ball.reset('computer')
                
        
        
    def game_over(self, winning_score):
        """Determines if the game is over by score threshold"""
        
        if self.player_score >= winning_score:
            self.goto(10, 0)
            self.write(f"GAME OVER, PLAYER WINS", align=ALIGN, font=GAME_OVER_FONT)
            return True
        elif self.computer_score >= winning_score:
            self.goto(10, 0)
            self.write(f"GAME OVER, PLAYER LOST", align=ALIGN, font=GAME_OVER_FONT)
            return True
        return False