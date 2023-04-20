from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
### Custom code starts here ###

# Initialize the objects for the office
office_coffee_machine = CoffeeMaker()
office_money_machine = MoneyMachine()
office_menu = Menu()

# Primary function
def coffee_machine_on():
    """Asks for and validates the choice of coffee input by user, with secret off and reports options for maintainers"""
    user_choice = input(f'What would you like? ({office_menu.get_items()}) ').lower()
    
    if user_choice == 'off': # Secret option to turn off the coffee machine i.e. shut down the Python script
        print("Shutting down the coffee machine..")
        exit()

    elif user_choice == 'report': # Secret option to print out a report of current resources in the coffee machine
        office_coffee_machine.report()
        office_money_machine.report()
        return coffee_machine_on()
    
    else:
        order_name = office_menu.find_drink(user_choice)
        if (order_name != None) and (office_coffee_machine.is_resource_sufficient(order_name)) and (office_money_machine.make_payment(order_name.cost)):
                    office_coffee_machine.make_coffee(order_name)
        return coffee_machine_on()


# Coffee Machine On Loop
while True: # Maintainer can break loop and shut down coffee machine by entering "off"
    coffee_machine_on()