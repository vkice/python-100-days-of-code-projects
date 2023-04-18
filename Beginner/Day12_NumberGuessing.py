# Number Guessing Game
## Player gets 10 attempts on easy, 5 on hard, to guess the number correctly
import os
from random import randint
from string import digits

# Functions
def clear():
   """Grab the version of OS to clear screen"""
    # Windows
   if os.name == 'nt':
        os.system('cls')
   # Linux/Mac
   else:
        os.system('clear')

def diff_choice():
    """Asks the user to choose a difficulty, validates, and returns the amount of guesses from that difficulty"""
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == 'easy':
        guesses = 10
        return guesses
    elif diff == 'hard':
        guesses = 5
        return guesses
    else:
        print("Invalid option, please enter a valid option.")
        return diff_choice()

def keep_playing():
    """Modifies the core while loop to False if user does not want to keep playing"""
    global is_playing
    user_opt = input("Do you want to keep playing? Type 'yes' otherwise type 'no' to stop: ")
    if user_opt != 'yes':
        is_playing = False

def start_guessing(guesses_left, number_to_guess, game_ratio):
    """Main function to play the game with the chosen difficulty option"""
    def make_guess():
        """Has the player input an integer and passes back only the number"""
        raw_input = input("Make a guess: ")
        player_input = ''
        for i in raw_input:
            if i in digits:
                player_input += str(i)
        if player_input == '':
            print("You did not enter a number, try again.")
            return make_guess()
        return int(player_input)
    
    def wrong_guess(player_wrong_guess, correct_number, remaining_guesses):
        """Removes one guess from player as number was wrong, provides a hint if value is higher or lower"""
        remaining_guesses -= 1
        if correct_number < player_wrong_guess:
            print("Too High.")
        else:
            print("Too Low.")
        return remaining_guesses

    
    def player_wins(game_ratio_add, num_correct):
        """If the player has correctly guessed the number they have won, asks if they'd like to play again."""
        game_ratio_add[0] += 1 # Adds one win to player
        print(f"That's right! The number I was thinking of is {num_correct}.\nYou now have {game_ratio_add[0]} wins this game.")
        keep_playing()
        return game_ratio_add
    def player_loses(game_ratio_add, num_correct):
        """If the player is out of guesses they have lost, then asks if they'd like to play again."""
        game_ratio_add[1] += 1 # Adds one loss to player
        print(f"You've ran out of guesses! The number I was thinking of is {num_correct}.\nYou now have {game_ratio_add[1]} losses this game.")
        keep_playing()
        return game_ratio_add
    
    # Core function gameplay
    while guesses_left > 0:
        if guesses_left == 1: # Grammar if only one guess
            print(f"You have {guesses_left} guess remaining.")
        else:
            print(f"You have {guesses_left} guesses remaining.")
        player_guess = make_guess()
        if player_guess == number_to_guess:
            game_ratio = player_wins(game_ratio, number_to_guess)
            return game_ratio
        else:
            guesses_left = wrong_guess(player_guess, number_to_guess, guesses_left)
    game_ratio = player_loses(game_ratio, number_to_guess) # If player is out of guesses
    return game_ratio

# Core game loop
is_playing = True
game_ratio = [0, 0] # Keeps track of players score, first int will be wins second losses
input("Welcome to the Number Guessing Game!\nGuess the number I am thinking of to win!\nPress 'enter' to start playing.\n")
while is_playing:
    clear()
    print("I'm thinking of a number between 1 and 100.")
    game_ratio = start_guessing(diff_choice(), randint(1, 100), game_ratio)
print(f"Thank you for playing! The final score was {game_ratio[0]} wins and {game_ratio[1]} losses.")