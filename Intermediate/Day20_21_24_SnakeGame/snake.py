from turtle import Screen, Turtle

# Directions converted to turtle coords
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Snake for the Snake Game and core components to move the snake"""

    def __init__(self):
        """Snake starting position"""
        
        self.screen = Screen()
        self.segment_list = []
        x_axis = 0
        for _ in range(3):
            self.create_segment(x_axis, 0)
            x_axis -= 20
        self.screen.update()
        self.snake_head = self.segment_list[0]


    def create_segment(self, x_cord, y_cord):
        """Creates the segments for the starting snake and grown from eating food"""
        
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(x=x_cord, y=y_cord)
        self.segment_list.append(segment)



    def move(self):
        """Moves the snake forward"""
        
        for seg_index in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_index - 1].xcor()
            new_y = self.segment_list[seg_index - 1].ycor()
            self.segment_list[seg_index].goto(new_x, new_y)
        self.snake_head.forward(20)
        
        
    def detect_collision(self):
        """Detects if the moved snake head position is on a segment of it's body"""
        
        if self.snake_head.xcor() > 280 or self.snake_head.xcor() < -280 or self.snake_head.ycor() > 280 or self.snake_head.ycor() < -280:
            return True
        
        for segment in self.segment_list[1:]:
            if self.snake_head.distance(segment) < 10:
                return True
        return False
    
    
    def ate_food(self):
        """Snake ate some food and the body has grown"""
        
        tail_x_pos = self.segment_list[-1].position()[0]
        tail_y_pos = self.segment_list[-1].position()[1]
        self.move()
        self.create_segment(tail_x_pos, tail_y_pos)
        self.screen.update()
        
    
    def reset_snake(self):
        """Player has hit a wall/tail, reset the snake body and position"""
        
        for segment in self.segment_list:
            segment.hideturtle()
        self.__init__()
        
    # Four functions to change heading of the snake head, checks if attempting to move opposite current heading
    def up(self):
        """Changes snake direction to up"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    def down(self):
        """Changes snake direction to down"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
    def left(self):
        """Changes snake direction to left"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    
    def right(self):
        """Changes snake direction to right"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
    ###
    
    
    