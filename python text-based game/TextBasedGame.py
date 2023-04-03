# In this TextBasedGame.py move from room to room and find the items in order to defeat the villain and escape the kitchen.
# use this to play Turkey Escape!
#Author Justin Ramirez
#Date: 12/10/2022

def Show_instructions():
    print('-' * 25, "Welcome to Turkey Escape!", '-' * 25)
    print('You are a turkey who woke up in a kitchen, about to be the main course for the holiday dinner. \n'
          'Luckily, the head chef has fallen asleep behind a locked door in the kitchen. You see the exit, \n'
          'two big metal doors but they are locked. You notice two keyholes, one red and one blue, if you \n'
          'can find the keys you will be able to escape.\n')
    print('the commands are: north, east, south, west and get if there is an item in the room. When prompted\n'
          'type yes or no to get the special item or do an activity.')


# This function is the heads-up display it shows players current room and the player inventory.
def hud(room, inv):
    print('-' * 22)
    print('you are at the : {}'.format(room))
    print('inventory: {}'.format(inv))
    print('-' * 22)


# this take the input from the user and changes the room
def change_room(current_room, user_move):
    if user_move != 'get':
        current_room = (rooms.get(current_room, oops(current_room)).get(user_move, oops(current_room)))
    return current_room


# this catches incorrect input
def incorrect(playerInput, currentRoom):
    if playerInput != 'get':
        if playerInput not in rooms.get(currentRoom):
            print(
                '!!!!! oops, try another direction and make sure that your input is valid.\nRemember north, east, south, west '
                'are the commands to move and get if there is an item in the room.!!!!! ')


# this keeps the current room the same if the input was a wrong input
def oops(currentRoom):
    currentRoom = currentRoom
    return currentRoom


'''
Here is a bunch of if statements, I was unable to find a better way of writing this section of code.
during this week of 12/5/2022 -12/9/2022. I had to take care of my sisters babies, she was going in to labor, it was a 
challenge writing the code. later I hope I can find a better way to write this section of code.
This message is for future me and my instructor Ryan McArthur.
'''


# here is most of the text for the game including the special items, for each room and activities
def room_activity(room, player_inventory, gh_inventory):
    # Kitchen-----------------------------------------------------------------------------------------------------------
    if room == "Kitchen":
        print('You are in a kitchen; it is big and very clean, you can smell something cooking in a pot on the stove.')

    # Metal doors-------------------------------------------------------------------------------------------------------
    if room == 'Metal doors':
        # if  player inventory does not have Red key and Blue key
        if 'Red key' and 'Blue key' not in player_inventory:  # checks if blue and red key are not in the player inventory
            print(
                'The doors have two locks on them, one red and one blue, you see that the blue lock is connected to an\n'
                'alarm by a cut resistant wire. you need both keys to open the door')
        # if  player inventory has Red key and Blue key
        elif 'Red key' and 'Blue key' in player_inventory:
            gh_inventory.append('chef head')  # adds chefs head to ghost list this is to end the game loop
            # checks if jar of lard is in the player inventory
            if 'ghostJar' in gh_inventory:  # checks if ghostJar is in the ghost inventory
                print(
                    'As you unlock the big metal doors with the keys you hear a loud alarm go off! The chef wakes up\n'
                    'and runs out of the room, he sees you trying to push the doors open but they are too heavy for you.\n'
                    'The chef runs over to you and grabs you by the neck! \n Sorry, you are Christmas dinner!')
            else:
                print(
                    'As you unlock the big metal doors with the keys you hear a loud alarm go off! The chef wakes up and \n'
                    'runs out of the room, he then slips on the lard you poured out in front of his door! He screams as \n'
                    'he slides headfirst into the metal doors, forcing them open. You watch as he continues to slide \n'
                    'all the way off a cliff!\n With the doors open you can now make your escape.')

    # Chefs door------------------------------------------------------------------------------------------
    if room == 'Chefs’ door':
        # checks to see if ghostJar is not in ghost inventory
        if 'ghostJar' not in gh_inventory:
            print('The floor is slippery you cant get any closer')
        # checks to see if ghostJar is in ghost inventory
        elif 'ghostJar' in gh_inventory:
            print(
                'You are at the front of the chefs door and can see him when you look through the key whole. if you \n'
                'had somthing slippery you could pour it out in front of his door.')
            # checks player inventory for jar of lard if so the uses it
            if 'Jar of lard' in player_inventory:
                Front_answer = input('Do you want to pour out the jar of lard? yes or no: ')
                Front_answer = Front_answer.lower()
                if Front_answer == 'yes':
                    print('You pour the lard out in front of the chefs door.')
                    player_inventory.remove('Jar of lard')  # removes jar of lard from the player inventory
                    gh_inventory.remove('ghostJar')  # removes ghostJar from the ghost inventory

    # Storage Room------------------------------------------------------------------------------------------------------
    if room == 'Storage room':
        # # checks inventory for flashlight if none gets flashlight
        if 'Flashlight' not in player_inventory:
            print('There is a flashlight in the room. type get to pick it up:')

    # Fuse box room-----------------------------------------------------------------------------------------------------
    if room == 'Fuse box room':
        print('There is a fuse box at the end of the room, you can use bolt cutters to open it.')
        # # checks inventory for rope if none gets rope
        if 'Rope' not in player_inventory:
            print('There is a rope in the room. type get to pick it up:')
        # use bolt cutter and move them from player inventory to ghost inventory
        if 'Bolt cutters' in player_inventory:
            Fuse_answer = input(
                'Do you want to use the bolt cutters to cut the switch for the freezer room? yes or no: ')
            Fuse_answer = Fuse_answer.lower()
            if Fuse_answer == 'yes':
                print(
                    'After you cut the lock the bolt cutters break, you then flip the switch off to the freezer room.')
                player_inventory.remove('Bolt cutters')
                gh_inventory.append('Bolt cutters')
                gh_inventory.append('Freezer power off')  # this item is needed to change the text for the freezer room

    # Compactor room-----------------------------------------------------------------------------------------------------
    if room == 'Compactor room':
        # check player inventory for rope
        if 'Rope' not in player_inventory:
            print(
                "You find your self  in a compactor room you can see a box full of batteries down in the pit but you can't \n"
                "reach them")
        # use rope
        elif 'Rope' in player_inventory:
            print('you see a box of batteries at the bottom of the pit.')
            # checks inventory for batteries if none gets batteries
            if 'Batteries' not in player_inventory:
                comp_answer = input('Do you want to use the rope to get down in to the pit? yes or no:')
                comp_answer = comp_answer.lower()
                if comp_answer == 'yes':
                    print(
                        'You use the rope to reach the bottom of the pit,you take some batteries  out of the  box \n'
                        'and go back up')
                    player_inventory.append('Batteries')
        if 'Bucket' not in player_inventory:
            print('There is a bucket in the room. type get to pick it up:')

    # Bathroom-----------------------------------------------------------------------------------------------------------
    if room == 'Bathroom':
        # checks if Red key in inventory or not
        if 'Red key' not in player_inventory:
            print('the door is locked turn back, you need the Red key to get in.')
        elif 'Red key' in player_inventory:
            print('You unlock the door and find a tub of dirty water')
            # use Bucket if red key in inventory
            if 'Bucket' in player_inventory and "ghostBucket" in gh_inventory:
                bath_answer = input('do you want to use the bucket to scoop the water out? yes or no: ')
                bath_answer = bath_answer.lower()
                if bath_answer == 'yes':
                    print('you now have the Blue key, the tub fills up with dirty water again.')
                    player_inventory.append('Blue key')
                    gh_inventory.remove('ghostBucket')

    # Shelf room--------------------------------------------------------------------------------------------------------
    if room == 'Shelf room':
        # checks to see if ghostJar in inventory
        if 'ghostJar' in gh_inventory:
            # checks inventory for Jar of lard if none gets Jar of lard
            if 'Jar of lard' not in player_inventory:
                print('There is a jar of lard in this room type get to pick it up:')

    # dark room---------------------------------------------------------------------------------------------------------
    if room == 'dark room':
        # checks for flashlight and batteries in inventory
        if 'Flashlight' and 'Batteries' not in player_inventory:
            print('It is to dark to see anything')
        elif 'Flashlight' and 'Batteries' in player_inventory:  # use flashlight
            print('You use the flashlight to see in the room.')
            # checks inventory for bolt cutters if none gets bolt cutters
            if 'Bolt cutters' not in player_inventory:
                dark_answer = input('there is some bolt cutters do you want to take them? yes or no: ')
                dark_answer = dark_answer.lower()
                if dark_answer == 'yes':
                    print('you now have the Bolt cutters')
                    player_inventory.append('Bolt cutters')

    # Freezer-----------------------------------------------------------------------------------------------------------
    if room == 'Freezer':
        # checks ghost inventory for Freezer power off.
        if 'Freezer power off' not in gh_inventory:  # this is a ghost item the player does not see it.
            print(
                "You see a turkey frozen in a block of ice, and it's holding a red key, but you can’t get it because\n"
                "of the ice. You'll need to cut the power to the freezer room.")
        elif 'Freezer power off' in gh_inventory:
            print('All the ice has melted')
            # checks inventory for red key if none gets Red key
            if 'Red key' not in player_inventory:
                free_answer = input(
                    'The frozen turkey has dropped the red key, do you want to pick it up? yes or no:')
                free_answer = free_answer.lower()
                if free_answer == 'yes':
                    print('you now have the Red key')
                    player_inventory.append('Red key')


# get function gets the items that are in the rooms dictionary
def get(c_room, p_inv, p_answer):
    if p_answer == 'get':
        item = (rooms.get(c_room, oops(c_room)).get('item', oops(c_room)))
        if item == c_room:
            print('there are no items in here.')
            c_room = c_room
        elif item not in p_inv:
            p_inv.append(item)
            c_room = c_room


# this loops the game unit the input is quit or the game is over
def main():
    Show_instructions()
    user_input = input('press enter to start or type quit to end game: ')
    answer = user_input.lower()  # this is the users input
    current_room = 'Kitchen'  # the current room starts off at the kitchen

    # this list is invisible it holds items that are not ment to be seen by the player
    ghost_inventory = ['ghostJar', "ghostBucket"]  # the item ghostJar is given to the list at the start
    inventory = []  # here is the player inventory it is empty at the start

    while answer != 'quit':

        hud(current_room, inventory)  # this calls the hud function
        room_activity(current_room, inventory, ghost_inventory)  # this calls the room_activity function

        if 'chef head' not in ghost_inventory:  # this is used to end game after unlocking the metal doors
            user_input = input('type your move or type quit:')
            answer = user_input.lower()
            incorrect(answer, current_room)
            get(current_room, inventory, answer)  # this calls the get function
            current_room = change_room(current_room, answer)
        else:
            input("thank you for playing! press enter to end the game.")
            break


# dictionary of all the rooms, sections are labeled starting room, East wing, West wing
rooms = {
    # --------------Starting room---------------------------------------------------------------------------------------
    'Kitchen': {'north': 'Metal doors', 'east': 'Lounge room', 'south': 'Chefs’ door',
                'west': 'Shelf room',
                'quit': 'Exit'},
    'Metal doors': {'south': 'Kitchen', 'quit': 'Exit'},
    'Chefs’ door': {'north': 'Kitchen', 'quit': 'Exit'},
    # -------------East wing--------------------------------------------------------------------------------------------
    'Lounge room': {'north': 'Storage room', 'east': 'Compactor room', 'south': 'Bathroom', 'west': 'Kitchen',
                    'quit': 'Exit'},
    'Storage room': {'east': 'Fuse box room', 'south': 'Lounge room', 'quit': 'Exit', 'item': 'Flashlight'},
    'Fuse box room': {'west': 'Storage room', 'quit': 'Exit', 'item': 'Rope'},
    'Compactor room': {'west': 'Lounge room', 'quit': 'Exit', 'item': 'Bucket'},
    'Bathroom': {'north': 'Lounge room', 'quit': 'Exit'},
    # -------------West wing--------------------------------------------------------------------------------------------
    'Shelf room': {'north': 'dark room', 'south': 'Freezer', 'east': 'Kitchen', 'quit': 'Exit', 'item': 'Jar of lard'},
    'dark room': {'south': 'Shelf room', 'quit': 'Exit'},
    'Freezer': {'north': 'Shelf room', 'quit': 'Exit'},
    # ----------------Exit room----------------------------------------------------------------------------------------
    'Exit': {}

}

# -----------------------------------Game Loop---------------------------------------------------

if __name__ == "__main__":
    main()
