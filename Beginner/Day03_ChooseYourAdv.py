# Choose your own adventure game.
print('#############################################')
print(f"{'Welcome to Treasure Island.':^50}")
print('#############################################')
print('Your mission is to find the treasure.\n')

# Ask the user to choose a direction, in a While loop to break out of the game if the user chooses an invalid choice.
while True:
    ##########
    start = 'You\'re at a cross road. To the left is a coastline to a sizeable lake, to the right is a dark forest with an overgrown trail. Where do you want to go? Type "left" or "right" '
    direction = input(start).lower()

    ##########
    # If the user chooses right, they lose.
    if direction == 'right':
        print('You step into the overgrown trail and walk for some distance. Suddenly, the ground is soft and gives way. You\'ve fallen into a hole and died.')
        break

    # If the user chooses left, ask them to choose a swim or wait.
    elif direction == 'left':
        direction_left = 'Walking along the shoreline you\'ve come to the edge of the lake. There is an island in the middle of the lake with some indistinguishable buildings. You can swim across the lake or wait for a boat to come. What do you choose? Type "swim" or "wait" '
        swim_or_wait = input(direction_left).lower()

    # If the user chooses any other option, break.
    else:
        print('You\'ve chosen an invalid direction. You\'re suddenly lost in a field, and die of starvation.')
        break
    ##########

    ##########
    # If the user chooses swim, they lose.
    if swim_or_wait == 'swim':
        print('You start to swim towards the island. Suddenly, the weather turns for the worse and a storm blows up. The waves are too high, and unfortunately you\'re swept away and drowned.')
        break
        
    # If the user chooses wait, ask them to choose a door.
    if swim_or_wait == 'wait':
        door_choice = 'You wait for a boat to come. After a while, a boat arrives and you get on board. You try to look at the hooded boat captain but he grunts and turns away from you. The boat takes you to the island. Upon walking to the buildings, you see there are three doors to choose from. One is red, one is yellow and one is blue. Which door do you choose? Type "red", "yellow" or "blue" '
        door = input(door_choice).lower()
    
    # If the user chooses any other option, break.
    else:
        print('You\'ve chosen an invalid action. You wait on the coast for too long, and die of starvation.')
        break
    ##########

    ##########
    # If the user chooses red, they lose.
    if door == 'red':
        print('You open the red door and enter the room. Suddenly, flames burst out from the walls in all directions. The fire is too hot and you burn to death.')
        break

    # If the user chooses blue, they lose.
    if door == 'blue':
        print('You open the blue door and enter the room. The door shuts behind you, you try to open the door but it has been locked. There is a growl behind you, a bear has woken up from slumber. The bear is hungry, and it is not known what happens next.')
        break

    # If the user chooses yellow, they win.
    if door == 'yellow':
        print('You open the yellow door and enter a room with a treasure chest. You open the chest and find a treasure map. You\'re going to be rich! You take the treasure map and leave the room, the boat captain takes you back to the mainland, and you set off to the find the treasure.\nYou win!')
        break
    # If the user chooses any other option, break.
    else:
        print('You\'ve chosen an invalid door. You\'re lost opening door after door, and die of starvation.')
        break
    ##########
# End of game.