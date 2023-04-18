# Rock, Paper, Scissors Game
import random

# Create a list of possible options
computer_choice = ["rock", "paper", "scissors"]

# Start game, advise when to end.
print("####################")
print("Welcome to Rock, Paper, Scissors! Type 'quit' to end the game.")
print("####################\n")

# Assign a random choice to the computer
computer = computer_choice[random.randint(0,2)]

# Game in a while loop
while True:
    player = input("Rock, Paper, Scissors? ").lower()
    if player == "quit":
        print("Thanks for playing!")
        break
    elif player == computer:
        print(f"It's a tie! You both played {computer.title()}")
    elif player == "rock":
        if computer == "paper":
            print("You lose! Paper covers Rock.")
        else:
            print(f"You win! Rock smashes Scissors!")
    elif player == "paper":
        if computer == "scissors":
            print(f"You lose! Scissors cut Paper.")
        else:
            print(f"You win! Paper covers Rock!")
    elif player == "scissors":
        if computer == "rock":
            print(f"You lose! Rock smashes Scissors.")
        else:
            print(f"You win! Scissors cut Paper!")
    else:
        print(f"No cheating! Choose a valid option.")
    # Generator a new option for computer before continuing the loop.
    computer = computer_choice[random.randint(0,2)]

