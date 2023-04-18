# Hangman Game
import random, string, os
from Day7Mod_Wordbank_Art import word_bank, hangman_ascii

# Grab OS for clear
def clear():
    # Windows
   if os.name == 'nt':
        os.system('cls')
   # Linux/Mac
   else:
        os.system('clear')

# Starting Game
print(f"========={hangman_ascii[6]}\nWelcome to Hangman! Try to guess the word!")
game_status = True
while game_status:

    # Generating our random word, list version, comparative list version, ascii lowercase, and total number of guesses
    answer = random.choice(word_bank)
    answer_list = list(answer)
    answer_comparison_string = ' '.join(answer_list)
    guesses_left = 6
    game_guessed_letters = ''

    # Generating list of blank chars, string separated version for game
    blank_char_list = []
    for i in range(0, len(answer)):
        blank_char_list.append('_')
    blank_char_string = ' '.join(blank_char_list)

    # Entering another while loop for this selected word
    while guesses_left > 0:

        # Grabbing guess from player, then validating input
        char_guess = input(f"{blank_char_string}\n{hangman_ascii[6-guesses_left]}\n\nPreviously guessed letter bank: {game_guessed_letters}\nGuess a letter: ").lower()

        valid_guess = False
        while not valid_guess:
            # If already guessed that letter
            if char_guess in game_guessed_letters:
                    char_guess = input("You've already guessed that letter, try another: ").lower()
            # If guess is valid
            elif char_guess in string.ascii_lowercase:
                 valid_guess = True
            # If guessed more than one letter
            elif len(char_guess) > 1:
                    char_guess = input("No cheating, only one letter: ").lower()
            # If guess is invalid
            elif char_guess not in string.ascii_lowercase:
                    char_guess = input("Please guess a valid letter: ").lower()

        # Input is validated, add to guessed letters  
        game_guessed_letters += char_guess

        # Check if guessed letter is in the answer, then update visual with that letter
        correct_guesses = 0
        for i in range(0, len(answer_list)):
            if char_guess == answer_list[i]:
                blank_char_list[i] = char_guess
                correct_guesses += 1
        blank_char_string = ' '.join(blank_char_list)
        clear()

        # First check if player has guessed no correct letters in the answer
        if correct_guesses == 0:
             guesses_left -= 1
             print(f"Sorry! '{char_guess}' was not in the word!")

        # Then check if player is out of guesses
        if guesses_left == 0:
             print(f"{blank_char_string}\n{hangman_ascii[6]}\nOh no, you're out of guesses! The correct answer was {answer}. You lose the game!")

        # Check if player has beaten the game
        if blank_char_string == answer_comparison_string: 
             print(f"{blank_char_string}\n{hangman_ascii[6-guesses_left]}\nCongratulations, the correct answer was {answer}! You win!")
             # Set guesses_left to 0 so current game loop breaks, player has won
             guesses_left = 0
    
    # Ask player if they would like to play again, if not break loop and end game.
    ask_player = input('Would you like to play the game again? Please enter "yes" if you would like to keep playing: ').lower()
    if ask_player != 'yes':
         game_status = False
clear()
print(f"\nThank you for playing Hangman!\n========={hangman_ascii[6]}")