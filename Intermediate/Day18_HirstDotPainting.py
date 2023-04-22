import turtle, random# , colorgram

#### Extracted colors from picture, no longer needed every run. Set a new list with tuples of RGB values.
# colors = colorgram.extract('my_picture.jpg', 15) # Extract our colors
# rgb_colors = []
# for color_index in range(len(colors)):
#     rgb_colors.append((colors[color_index].rgb.r, colors[color_index].rgb.g, colors[color_index].rgb.b))
# Results of print(rgb_colors)
rgb_colors = [(71, 95, 116), (113, 143, 168), (34, 51, 68), (251, 245, 196),
              (46, 65, 84), (122, 88, 50), (249, 190, 99), (102, 130, 155),
              (219, 239, 244), (194, 228, 220), (28, 15, 8), (70, 181, 91),
              (223, 147, 97), (8, 20, 11), (100, 179, 118)
            ]


# Initialize object and values
turtle.colormode(255) # RGB Mode
turtle.screensize(canvwidth=1000, canvheight=1000)
turtle.setworldcoordinates(llx = 0, lly = -50, urx = 1000, ury = 1000) # Optimal values for starting point and the drawing for-loop
drawing_point = turtle.Turtle()
drawing_point.hideturtle()
drawing_point.penup() # No line is drawn
drawing_point.speed("fastest")


# Drawing for-loop
y_pos = 0 # Initialize the position of y axis
for _ in range(10): # Moves drawing point vertically
    # Move horizontal
    for i in range(10): # 10 dots horizontal across the screen
        drawing_point.forward(50)
        drawing_point.dot(50, random.choice(rgb_colors))
        drawing_point.forward(50)
    drawing_point.setx(0) # Reset back to left side of screen
    y_pos += 100
    drawing_point.sety(y_pos)

screen = turtle.Screen()
screen.exitonclick()