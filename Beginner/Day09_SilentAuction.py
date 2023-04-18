# Silent Auction
import string, os
print("Welcome to the Silent Auction.")

### Functions start ###
def clear():
    """Grab the version of OS to clear screen"""
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux/Mac
    else:
        os.system('clear')

def bid_conv(str_input):
    """Function to convert bid input into a float"""
    user_bid =  ''
    for i in str_input:
        if i in string.digits or i == ".":
            user_bid += str(i)
    return float(user_bid)

def user_check(user_input):
    """Check for users with same name and asks to modify if duplicate is found"""
    global list_of_bidders
    for i in list_of_bidders:
        if i["bidder"] == user_input:
            user_input = user_check(input("There is another person with the same name, could you enter part of your last name?: "))
    return user_input.title()

def user_add():
    """Get the inputs from the user and add to the list of bidders"""
    global list_of_bidders, total_bids
    if total_bids > 0:
        clear()
    user_name = user_check(input("What is your name?: "))
    user_bid_input = bid_conv(input("What is your bid?: "))
    list_of_bidders.append({"bidder": user_name, "bid": user_bid_input})
    total_bids += 1

def other_bidders():
    """Check if there are any other bidders to continue the loop"""
    other_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bids == 'yes':
        return True
    elif other_bids == 'no':
        return False
    else:
        print("Invalid entry, please try again.")
        other_bidders()

def winner_calc():
    """Calculate and announce the winner of the auction"""
    global still_bidding, list_of_bidders, total_bids
    winner_bid = 0
    # Find value of winning bid and index for bidder name
    for i in range(0, len(list_of_bidders)):
        if list_of_bidders[i]["bid"] > winner_bid:
            winner_bid = list_of_bidders[i]["bid"]
            winner_index = i
    winner_name = list_of_bidders[winner_index]["bidder"]
    clear()
    print(f"There was a total of {total_bids} bidders, and the auction winner is {winner_name} with a bid of ${winner_bid:.2f}.")
    still_bidding = False
    list_of_bidders = []
    total_bids = 0
    play_again = input("Would you like to have another auction? Type 'yes', otherwise type 'no': ")
    if play_again == 'yes':
        still_bidding = True
### Functions end ###

# Starting Auction loop
list_of_bidders = []
total_bids = 0
still_bidding = True
while still_bidding:
    user_add()
    if not other_bidders():
        winner_calc()