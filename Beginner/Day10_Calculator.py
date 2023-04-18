# Visual Calculator
import os, string

### Functions start ###
def clear():
   """Grab the version of OS to clear screen"""
    # Windows
   if os.name == 'nt':
        os.system('cls')
   # Linux/Mac
   else:
        os.system('clear')

def num_conv(which_input):
    """Convert inputs into a float or int"""
    str_input = str(input(f"What is the {which_input} number?: "))
    conv_num =  ''
    for i in str_input:
        if i in string.digits or i == ".":
            conv_num += str(i)
    # If the string is blank, then user did not enter a number, ask again
    if len(conv_num) == 0:
        print("Invalid entry, please enter a number.")
        return num_conv(which_input)
    conv_num = float(conv_num)
    if conv_num.is_integer():
        return int(conv_num)
    return conv_num

def op_sel():
    """Validate the operator selected"""
    op_input = input("+\n-\n*\n/\nPick an operation: ")
    if (op_input in "+-*/") and (len(op_input) == 1):
        return op_input
    print("Invalid operator, please select a valid option.")
    return op_sel()

def inputs():
    """Get inputs from the user and validates the entered prompts"""
    if not continue_calculating:
        first_num = num_conv("first")
    else:
        first_num = result
    operator = op_sel()
    second_num = num_conv("second")
    return first_num, operator, second_num

def should_continue():
    """Ask the user if they want to keep calculating"""
    global result, continue_calculating, is_calculating
    prompt_cont = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'q' to stop calculating: ")
    if prompt_cont == 'y':
        continue_calculating = True
    elif prompt_cont == 'n':
        continue_calculating = False
    else:
        is_calculating = False


def calc(first_to_calc, operator, second_to_calc):
    """Calculate the variabless based on selected operator"""
    global result
    # Adding
    if operator == '+':
        result = first_to_calc + second_to_calc
    
    # Subtracting
    elif operator == '-':
        result = first_to_calc - second_to_calc

    # Multiplying
    elif operator == '*':
        result = first_to_calc * second_to_calc
    
    # Dividing
    elif operator == '/':
        # Check for divide by zero error
        if second_to_calc == 0:
            print("Sorry, you cannot divide by zero! Please enter a new number to divide by.")
            second_to_calc = num_conv("new")
        result = first_to_calc / second_to_calc
    # Convert to integer if true for cleaner output
    result = float(result)
    if result.is_integer():
        result = int(result)
    
    # Print final calculations
    print(f"{first_to_calc} {operator} {second_to_calc} = {result}")

# Start Calculator Loop
result = 0
is_calculating = True
continue_calculating = False
while is_calculating:
    num_first, chosen_op, num_second = inputs()
    calc(first_to_calc = num_first, operator = chosen_op, second_to_calc = num_second)
    should_continue()