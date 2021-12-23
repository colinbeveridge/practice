import numpy as np
import csv

# create function that makes tournament slots
def makeslots(numplayers):
    # make dictionary with all slot numbers, name slots empty for now
    # since numplayers is user input we convert to int
    numplayers = int(numplayers)
    keylist = list(np.arange(1,(numplayers+1)))
    participant_records = dict.fromkeys(keylist)
    saved = False
    return participant_records,saved

# define function for main menu interface
def MainMenu(place):
    # here the user will select where they would like to navigate within the tracker UI
    print('Participant Menu')
    print('========================')
    print('1. Sign Up')
    print('2. Cancel Sign Up')
    print('3. View Participants')
    print('4. Save Changes')
    print('5. Exit')
    
    # make sure the user inputs a valid entry
    while place not in ['1','2','3','4','5']:
        print('Please enter an integer from 1-5 to navigate to the corresponding menu.')
        place = input('Where would you like to navigate to? ')

    place = int(place)

    return place
# define function for Sign Up Menu
def SignUp(participant_records):
    # function that allows user to enter a name into a desired starting slot, given that it is not already filled
    print('Participant Sign Up')
    print('===================')
    print('Enter "Exit" to exit from this menu.')
    # big while loop so that we can keep working until we find a slot or the user hits quit.
    numentries = len(participant_records)
    slotfound = False
    while not slotfound:

        participant_name = input('Participant Name: ')

        # check if the user exits
        if participant_name == 'Exit':
            break

        desired_slot = input(f'Desired starting slot #[1-{numentries}]: ')

        # make sure to get a digit for desired slot, for now we will take anything for the participant name, so we dont have to re enter participant name each time
        while not desired_slot.isdigit():
            print(f'Please enter an integer between 1 and {numentries}.')
            desired_slot = input(f'Desired starting slot #[1-{numentries}]: ')

        # once we know desired_slot is a number then we can compare it to numentries
        while int(desired_slot) > numentries or int(desired_slot) < 1:
            print(f'Please enter an integer between 1 and {numentries}.')
            desired_slot = input(f'Desired starting slot #[1-{numentries}]: ')

        # logic to see if slot is full
        desired_slot = int(desired_slot)
        if participant_records[desired_slot] == None:
            participant_records[desired_slot] = participant_name
            print('Success:')
            print(f'{participant_name} is signed up in starting slot #{desired_slot}.')
            slotfound = True
            saved = False
        
        else:
            print('Error:')
            print(f'Slot #{desired_slot} is filled. Please try again.')
            print(f'To cancel the current participant from slot #{desired_slot}, exit this menu and go to "Cancel Sign Up" menu.')

    place = 0
    saved = False
    return place, participant_records, saved

    # write function to handle sign up cancellations
def CancelSignUp(participant_records):
    # here is the menu where user can cancel sign ups
    # each of the conditions
    print('Participant Cancellation')
    print('========================')
    print('Enter "Exit" to exit from this menu.')

    # logic to run while loop until the correct name slot combo is entered
    matchfound = False
    numentries = len(participant_records)
    while not matchfound:
        participant_name = input('Participant Name: ')

        # check if the user exits
        if participant_name == 'Exit':
            break

        cancel_slot = input(f'Starting Slot #[1-{numentries}]: ')

        # make sure the cancel slot entered is a number in the correct range, so we dont have to re enter participant name each time
        while not cancel_slot.isdigit():
            print(f'Please enter an integer between 1 and {numentries}.')
            cancel_slot = input(f'Starting slot #[1-{numentries}]: ')

        # once we know cancel_slot is a number then we can compare it to numentries
        while int(cancel_slot) > numentries or int(cancel_slot) < 1:
            print(f'Please enter an integer between 1 and {numentries}.')
            cancel_slot = input(f'Desired starting slot #[1-{numentries}]: ')

        # now that we have confirmed the number is in range, convert to integer for reference
        cancel_slot = int(cancel_slot)

        # check if the entered name matches the name in that spot exactly. if so, remove participant from spot
        if participant_records[cancel_slot] == participant_name:
            print('Success:')
            print(f'{participant_records[cancel_slot]} has been removed from starting slot #{cancel_slot}')
            matchfound = True
            participant_records[cancel_slot] = None
            saved = False

        # if nobody in slot, tell them that then reset them to enter again
        elif participant_records[cancel_slot] == None:
            print('Error:')
            print('There is no participant in the slot selected. Select another slot.')

        # if not, send an error and return who is in that spot, then restart user entries
        else:
            print('Error:')
            print(f'{participant_name} is not in that starting slot.')
            print(f'Currently the participant in that slot is {participant_records[cancel_slot]}.')

    place = 0
    saved = False
    return place, participant_records, saved

def ViewParticipants(participant_records):
    # this function displays the participants menu based on user input
    print('View Participants')
    print('=================')
    numentries = len(participant_records)
    startslot = input(f'Starting Slot #[1-{numentries}]: ')

    # these while loops confirm the slot entered is valid
    while not startslot.isdigit():
        print(f'Please enter an integer between 1 and {numentries}.')
        startslot = input(f'Starting Slot #[1-{numentries}]: ')
    
    while int(startslot) > numentries or int(startslot) < 1:
        print(f'Please enter an integer between 1 and {numentries}.')
        startslot = input(f'Starting Slot #[1-{numentries}]: ')

    # define top and bottom of for loop for printing participants
    startslot = int(startslot)
    bottom = startslot - 5
    top = startslot + 5

    # set top and bottom to their min/max if they go beyond edges
    if bottom < 1:
        bottom = 1
    
    if top > numentries:
        top = numentries
    
    # display participants
    print('Starting Slot: Participant')
    for i in range(bottom,(top+1)):
        if participant_records[i] == None:
            dispstatement = '[empty]'
        else:
            dispstatement = participant_records[i]

        print(f'{i}: {dispstatement}')

    place = 0
    return place

# function for saving tournament slots
def SaveChanges(participant_records):
    print('Save Changes')
    print('============')
    save = input('Save your changes to CSV? [y/n] ')
    while save != 'y' and save != 'n':
        print('Must enter "y" or "n" to save or not save respectively.')
        save = input('Save your changes to CSV? [y/n]')
    
    if save == 'y':
        file_name = 'c:/Users/cbevr/OneDrive/Documents/GitHub/practice/Tournament-Tracker/your_tournament_data.csv'
        with open(file_name,'w') as f:
            for key in participant_records.keys():
                f.write("%s,%s\n"%(key,participant_records[key]))
            f.close()
        saved = True

    else:
        saved = False

    place = 0
    
    return place, saved

def Exit(saved):
    # function for exit menu, displays warning about unsaved changes if they exist
    print('Exit')
    print('=====')
    # logic for unsaved changes
    if not saved:
        print('Warning: your document has unsaved changes. Any unsaved changes will be lost.')
    
    exit = ''
    # while incorrect input, reprompt for y or n
    while exit != 'y' and exit != 'n':
        print('Please enter "y" to exit or "n" to continue editing your tournament.')
        exit = input('Are you sure you want to exit? [y/n] ')

    # do something based on what exit is
    if exit == 'n':
        place = 0
    else:
        place = None
    print(place)
    return place

