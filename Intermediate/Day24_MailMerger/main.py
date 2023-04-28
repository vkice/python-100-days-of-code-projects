#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# Start out by reading files and assigning to a var
with open("./Input/Letters/starting_letter.txt") as data:
    starting_letter = data.read()
    
with open("./Input/Names/invited_names.txt") as data:
    names_file = data.readlines()
#

# Remove new lines from list
for name in range(0, len(names_file)):
    names_file[name] = names_file[name].strip('\n')

# Output each letter replacing with each distinct name
for name in names_file:
    output = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as data:
        data.write(output)