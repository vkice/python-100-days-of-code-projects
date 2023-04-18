# Coffee Machine
### Default Coffee Machine Options
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
###

from string import digits
from math import fsum

### Coffee Machine Main Functions


def process_money(current_resources, coffee_choice):
    """Inputs and processes money for the coffee order from user if there are sufficient resources"""
    
    def validate_coins(coin_option):
        """Grabs coins from user validating they've entered an integer and passes back only the number"""
        raw_input = input(f"How many {coin_option}?: ")
        coins_inserted = ''
        for i in raw_input:
            if i in digits:
                coins_inserted += str(i)
        if coins_inserted == '':
            print("You did not enter a number, try again.")
            return validate_coins(coin_option)
        return int(coins_inserted)
    
    
    coffee_choice_cost = MENU[coffee_choice]["cost"]
    print(f'{coffee_choice.title()} costs ${coffee_choice_cost:.2f}.\nPlease insert coins.')
    coin_options = {"quarters": .25, "dimes": .10, "nickles": .05, "pennies": .01}
    inserted_coin = []
    for coin in coin_options:
        inserted_coin.append(coin_options[coin] * validate_coins(coin))
    total_coin_value = round(fsum(inserted_coin), 2) # Total amount the user has paid for their coffee
    if total_coin_value < coffee_choice_cost: # Check if user did not pay enough first
        print(f"Sorry that's not enough money, you've only entered ${total_coin_value:.2f}. Coins have been refunded.")
    elif total_coin_value > coffee_choice_cost: # User can afford, process change since they have overpaid
        user_refund = total_coin_value - coffee_choice_cost
        print(f"Here is ${user_refund:.2f} in change.")
    current_resources["money"] += coffee_choice_cost
    return current_resources


def process_coffee(current_resources, coffee_choice):
    """Deducts the resources needed from the machines and makes the coffee for the user"""
    for key in resources:
        if key != "money": # Ignores the money option
            current_resources[key] -= MENU[coffee_choice]["ingredients"][key]
    print(f'Here is your {coffee_choice}. ☕ Enjoy! ')
    return current_resources


def resource_check(current_resources, coffee_choice):
    """Checks if there is a sufficient amount of resources in the machine before processing the users order"""    
    sufficient_resources = True
    for key in current_resources:
        if key != "money": # Ignores the money option
            if MENU[coffee_choice]["ingredients"][key] > current_resources[key]:
                print(f"Sorry there is not enough {key}.")
                sufficient_resources = False # Sets to false if we are missing a key ingredient
    if sufficient_resources:
        current_resources = process_money(current_resources, coffee_choice)
        current_resources = process_coffee(current_resources, coffee_choice)
    return current_resources


def coffee_choice():
    """Asks for and validates the choice of coffee input by user, and secret off and reports options for maintainers"""
    valid_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if valid_choice in ('espresso', 'latte', 'cappuccino'): # Current coffee options provided
        return valid_choice
    elif valid_choice == 'off': # Secret option to turn off the coffee machine i.e. shut down the Python script
        print("Shutting down the coffee machine..")
        exit()
    elif valid_choice == 'report': # Secret option to print out a report of current resources in the coffee machine
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]:.2f}')
        return coffee_choice()
    print("Sorry, we don't have that! Please try choosing one of the three available options.")
    return coffee_choice()


# Coffee Machine Loop
while True: # Maintainer can break loop by entering "off"
    resources = resource_check(resources, coffee_choice())