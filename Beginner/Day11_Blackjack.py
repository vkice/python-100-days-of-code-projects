# Blackjack Game
import random, os
### Rules for this game ###
## The deck is unlimited in size
## Jack/Queens/Kings display as 10
## Ace displays as 11 or 1 depending on hand score
## No Jokers are in play
## Equal probability of being drawn
## Cards not removed from deck if drawn
## Using below list without modification
cards_values = [ 11, 2, 3, 4, 5, 6, 7 , 8, 9, 10, 10, 10, 10]
###

# Functions, smaller ones with defined actions
def clear():
   """Grab the version of OS to clear screen"""
    # Windows
   if os.name == 'nt':
        os.system('cls')
   # Linux/Mac
   else:
        os.system('clear')


def deal_card():
    """Draw a random card from the deck and returns the value"""
    return random.choice(cards_values)


def ace_check(current_hand):
    """Calculate if ace value should be 1 or 11 so hand is not bust"""
    if 11 in current_hand and sum(current_hand) > 21:
        current_hand.remove(11)
        current_hand.append(1)
    return current_hand


def draw_hand(gen_hand):
    """Generate a hand for the dealer and user"""
    for _ in range(0, 2):
        gen_hand["dealer"].append(deal_card())
        gen_hand["player"].append(deal_card())
    return gen_hand


def continue_playing(player_bank_current):
    """Check if player is out of money and ask the player if they would like to continue playing"""
    if player_bank_current <= 0:
        play = input("Looks like you're out of money! Better luck next time.\nWould like to buy in to a new game and start with $100 again? Type 'yes' otherwise type 'no': ")
        if play == 'yes':
            player_bank_current = 100
            return True, player_bank_current
        return False, player_bank_current
    else:
        play = input(f"Would you like to play another round? Type 'y' otherwise type 'n': ").lower()
        if play == 'y':
            return True, player_bank_current
        return False, player_bank_current


def reset_game(hands_reset):
    """Reset the game values to prepare for a new round"""
    clear()
    hands_reset = {"dealer": [], "player": []}
    return hands_reset


# Core game functions that call above individual functions
def play_game(next_game_bank):
    """Core function to play the BlackJack game"""


    def next_round(hands_this_round, player_bank_round):
        """Prints out the current hands and asks player to draw a card or pass"""
        # Check for aces in players hand first
        hands_this_round["player"] = ace_check(hands_this_round["player"])
        hands_this_round, players_hand_score = print_cards(hands_this_round, False, player_bank_round)
        # Check if user score is 21 or busted before proceeding with input for user to hit
        if players_hand_score >= 21:
            return hands_this_round, True, player_bank_round
        else:
            player_choice = input("Type 'y' to be dealt another card, type 'n' to stand: ").lower()
            if player_choice == 'y':
                hands_this_round["player"].append(deal_card())
                return hands_this_round, False, player_bank_round
            return hands_this_round, True, player_bank_round
        
        
    def print_cards(hands_this_round, is_final, player_bank_print):
        """Prints out a screen showing the current status of the game with a check to reveal the Dealer's hand"""
        clear()
        print (f"Player's bank: ${player_bank_print}\nPlayer's bet: $10")
        
        
        def hand_to_fstring(hands_this_round, is_final):
            """Returns an fstring revealing the cards that player or dealer has to the print_cards function"""
            player_list = ["Dealer", "Player"]
            # Check if Dealer hand should not be revealed yet
            if not is_final:
                dealer_hand = f'''\tDealer's hand: {hands_this_round["dealer"][0]}, ▯'''
                player_list = ["Player"]
            for owner in player_list:
                list_of_cards = hands_this_round[owner.lower()]
                # Append each card to string
                hand_fstring = f'''\t{owner}'s hand: '''
                for i in list_of_cards:
                    hand_fstring += f'{str(i)}, '
                # Sum up their scores
                hand_score = sum(list_of_cards)
                if not is_final: 
                    hand_fstring += f'Current Score: {hand_score}'
                else:
                    hand_fstring += f'Final Score: {hand_score}'
                # Assign strings to returns and score if players.
                if owner == "Player":
                    player_hand = hand_fstring
                    player_score = hand_score
                else:
                    dealer_hand = hand_fstring
            return dealer_hand, player_hand, player_score
        dealer_fstring, player_fstring, players_hand_score = hand_to_fstring(hands_this_round, is_final)
        print(f"{dealer_fstring}\n{player_fstring}")
        return hands_this_round, players_hand_score
    
    

    def end_game(final_hands, player_bank_final):
        """Player is no longer drawing cards, calculate if the player won, lost, or drawn with dealer"""
        
        
        def dealer_draws(dealer_hand):
            """Plays out the dealer drawing phase for the player"""
            dealer_score = sum(dealer_hand)
            # Dealer draw cards until the sum is over 17
            while dealer_score < 17:
                dealer_hand.append(deal_card())
                dealer_hand = ace_check(dealer_hand)
                dealer_score = sum(dealer_hand)
            return dealer_hand
        ### First check if the player has busted before calculating the hand for the dealer.
        player_score = sum(final_hands["player"])
        player_busted = False
        if player_score > 21:
            final_message = f"You lose! You have busted by going over 21."
            player_busted = True
        final_hands["dealer"] = dealer_draws(final_hands["dealer"])
        dealer_score = sum(final_hands["dealer"])
        print_cards(final_hands, True, player_bank_final)

        ### Start with player Blackjack checks
        if player_score == 21 and len(final_hands["player"]) == 2:
            if dealer_score == 21 and len(final_hands["dealer"]) == 2:
                final_message = f"You and the dealer have hit Blackjack! It's a draw!"
                player_bank_final += 10 # +10 returns player bet, +20 player won and received 10, nothing return for loss player loses 10
            elif dealer_score > 21:
                final_message = f"You win! You've hit Blackjack, and the dealer has busted!"
                player_bank_final += 20
            else:
                final_message = f"You win! You've hit Blackjack!"
                player_bank_final += 20
        ### Dealer Blackjack checks
        elif dealer_score == 21 and len(final_hands["dealer"]) == 2:
            if player_score > 21:
                final_message = f"You lose! Dealer has hit Blackjack, and you have busted!"
            else:
                final_message = f"You lose! Dealer has hit Blackjack!"
        ### Rest of checks without any blackjacks
        elif dealer_score == player_score: # tie
            final_message = f"You and the Dealer have tied with a score of {player_score}."
            player_bank_final += 10
        elif dealer_score > 21 and not player_busted: # dealer busted but player under 21
            final_message = f"You win! Dealer has busted!"
            player_bank_final += 20
        elif dealer_score > player_score: # dealer higher score, no busts
            final_message = f"You lose! Dealer has beaten your score of {player_score} with {dealer_score}."
        elif not player_busted: # final check, player score must be higher and no busts
            final_message = f"You win! Your score of {player_score} has beaten the Dealer's {dealer_score}."
            player_bank_final += 20
        print(f'{final_message}\n\nYour current bank value is now ${player_bank_final}.') # return player bank after calculating win/loss
        return player_bank_final
    ### End function assignments
    
    ### Initial Setup for core game function
    no_more_rounds = False # Boolean value sent to next round
    player_bank = next_game_bank
    player_bank -= 10 # Take bet for this game
    hands = {"dealer": [], "player": []}
    hands = draw_hand(hands)
    # Start loop of rounds
    while not no_more_rounds:
        hands, no_more_rounds, player_bank = next_round(hands, player_bank)
    player_bank = end_game(hands, player_bank)
    return player_bank
# End Functions

# Start game loop
input("Welcome to Blackjack!\n\nStart with $100, bets are $10 a round. See how many money you can make!\n\nReady to play? Press enter to begin.\n")
clear()
is_playing = True
bank_value = 100 # Starting out with 100
while is_playing:
    bank_value = play_game(bank_value)
    is_playing, bank_value = continue_playing(bank_value)
print(f"Thanks for playing! Your final bank value was ${bank_value}")