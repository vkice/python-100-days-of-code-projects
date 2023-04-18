# Caesar Cypher
from string import ascii_lowercase

# Caesar Function
def caesar(msg, shift, instr):

    # Set blank string and overflow value
    cyph = ''
    overflow_adj = 26

    # Check if decode picked, negate the index
    if instr == 'decode':
        shift *= -1
        overflow_adj *= -1
    for i in range(0, len(msg)):

        # Append anything not a letter
        if msg[i] not in ascii_lowercase:
            cyph += msg[i]
        else:
            char_index = ascii_lowercase.index(msg[i]) + shift
            # Check if rotated around alphabet to avoid index errors
            while -25 > char_index or char_index > 25:
                char_index -= overflow_adj
            cyph += ascii_lowercase[char_index]

    # Print final message
    print(f"The {instr}d message is: {cyph}")

# Starting loop
is_translating = True
while is_translating:

    # Validate instructions
    instructions = input("Type 'encode' to encrypt your message, type 'decode' to descript your message, or 'quit' to stop: ")
    if instructions == 'quit':
        is_translating = False
        continue
    elif instructions != 'encode' and instructions != 'decode':
        print("You did not choose 'encode', 'decode', or 'quit'")
        continue

    # Grab other inputs from user
    message = input("Type your message:\n").lower()
    shift_num = int(input("Type the shift number:\n"))
    
    # Printing cypher text
    caesar(msg=message, shift=shift_num, instr=instructions)