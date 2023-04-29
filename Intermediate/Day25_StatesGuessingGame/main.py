import turtle
import pandas
ALIGN = "center"
FONT = ("Arial", 8, "normal")
WIN_FONT = ("Arial", 20, "bold")

# Setup window
screen = turtle.Screen()
screen.title("U.S. States Guessing Game")
screen.setup(width=730, height=495)

# Set background US map
state_img = "./blank_states_img.gif"
screen.addshape(state_img)
turtle.shape(state_img)

# Initialize the panadas dataframe
states_df = pandas.read_csv("./50_states.csv")
unguessed_states = states_df.state.to_list()

# Functions
def state_guessed(state):
    """Function to place the guessed State text on screen"""
    unguessed_states.remove(state.title())
    
    # Grab coordinates from states dataframe
    x_cor = int(states_df.x[states_df.state == state])
    y_cor = int(states_df.y[states_df.state == state])
    
    new_text = turtle.Turtle()
    new_text.hideturtle()
    new_text.penup()
    new_text.pencolor("black")
    new_text.goto(x=x_cor, y=y_cor)
    new_text.write(f"{state}", align=ALIGN, font=FONT)
    

def game_won():
    """User guessed all states, present win message and total guesses"""
    white_box = turtle.Turtle(shape="square")
    white_box.color("white")
    white_box.shapesize(stretch_len=28, stretch_wid=8)
    
    
    game_won = turtle.Turtle()
    game_won.hideturtle()
    game_won.penup()
    game_won.pencolor("black")
    game_won.write(f"You've guessed all the states and won!\n         "
                   f"It took you {user_guesses} guesses", align=ALIGN, font=WIN_FONT)


# Start guessing game
still_guessing = True
user_guesses = 0
while still_guessing:
    user_guess = str(screen.textinput(title=f"{50 - len(unguessed_states)}/50 States Guessed", prompt="Type 'exit' to stop playing\n\nGuess a state:")).title()
    user_guesses += 1

    # Exit game if the user types exit, generates a CSV of states they couldn't guess
    if user_guess == 'Exit':
        still_guessing = False
        
    # Remove guessed state from list and add to the map
    elif user_guess in unguessed_states:
        state_guessed(user_guess)
        
    # If user guessed all states correctly
    if len(unguessed_states) == 0:
        game_won()
        screen.exitonclick()

# Generating CSV(one column for readability) of unguessed states
if not still_guessing:
    dict_unguessed_states = {
        "States that were not guessed:": unguessed_states
    }
    df_to_csv = pandas.DataFrame(dict_unguessed_states)
    df_to_csv.to_csv("unguessed_states.csv", index=False)