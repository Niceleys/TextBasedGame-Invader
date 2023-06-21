def user_instructions():  # Introduction and instructions for play.
    print('-----------------------------')
    print('Welcome to the text based game: Intruder')
    print('-----------------------------')
    print('\nYou have just gotten home and noticed there is an intruder in your office.')
    print('There have been reports of people acting strangely on the radio, biting, shambling.')
    print('Your goal is to make it through the house and gather 6 items to protect yourself.')
    print('\nTo move through rooms, use a command from this list: go north/south/east/west or exit/quit')
    print('To pick up the item in each room, use the command: get (item name)')
    print('\nGood luck!')
    return'\n-----------------------------\n'


rooms = {  # Dictionary containing all rooms and their items.
    'Porch': {'west': 'Mud Room'},  # Starting point.
    'Mud Room': {'east': 'Porch', 'south': 'Dining Room', 'item': 'Flashlight'},
    'Dining Room': {'north': 'Mud Room', 'west': 'Kitchen', 'east': 'Garage', 'south': 'Living Room',
                    'item': 'Coffee'},
    'Kitchen': {'east': 'Dining Room', 'item': 'Knife'},
    'Garage': {'west': 'Dining Room', 'north': 'Utility Room', 'item': 'Jacket'},
    'Utility Room': {'south': 'Garage', 'item': 'Mask'},
    'Living Room': {'north': 'Dining Room', 'east': 'Office', 'item': 'Pillow'},
    'Office': {'west': 'Living Room', 'item': 'Zombie'}  # Villain room.
}


starting_room = 'Porch'
current_room = starting_room
inventory = []
direction = ('north', 'south', 'east', 'west')


def move_rooms(direction, current_room):
    new_room = current_room
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
    else:
        print('There are no room this way.\n')
    return new_room


def main():
    global current_room
    print(user_instructions())
    while True:
        if current_room == 'Office':
            if len(inventory) == 6:
                print('You made it to the office with your supplies and notice someone shuffling around aimlessly')
                print('They turn and look like something out of a horror movie!')
                print('You ready yourself and charge at what looks like a Zombie')
                print('After a tiring fight, you defeat the intruder!')
                print('Congratulations!')
                break
            else:
                print('You came unprepared and the intruder got you!')
                print('Try again!')
                break

            # display current location
        if starting_room == 'Porch':
            print('-----------------------------\n')
            print('You are at the {}'.format(current_room))
            print('Inventory:', inventory)
            room_dict = rooms[current_room]
            if "item" in room_dict:
                item = room_dict["item"]
                if item not in inventory:
                    print("You see a", item)
            # get user input
            command = input("\nWhat do you do? Either 'go' a direction, or 'get' an item\n").split()
            if command[0] == 'go':  # movement
                if command[1] in direction:
                    room_dict = rooms[current_room]
                    if command[1] in room_dict:
                        current_room = room_dict[command[1]]
                    else:
                        print('You cannot go that way.\n')  # bad movement
                        print('-----------------------------\n')
                else:
                    print("Invalid entry")

            elif command[0] in ['exit', 'quit']:  # quit game
                print('Thanks for playing!')
                break
            elif command[0] == 'get':  # get item
                if command[1] == item:
                    inventory.append(item)
                    print(item, "collected")
                    print('-----------------------------\n')
                else:
                    print('Invalid command')
            else:  # bad command
                print('Invalid input')


main()

input('To exit this program press anything and hit enter.\n')
