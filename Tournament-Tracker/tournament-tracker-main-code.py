import numpy as np
import math
import csv
import MenuFuncs as MF
import os

if __name__ == '__main__':

    ''' Tournament Tracker App. App that creates tournament entries and allows user to enter names of participants.'''
    # this is the opening page of the app, where we enter the number of participants
    print('Welcome to Tournament Creator')
    print('=============================')

    # initialize participants so we go into loop to get correct input
    numparticipants = ''

    # while this entry is not a digit
    while not numparticipants.isdigit():
        print('Number of participants must be a positive integer.')
        numparticipants = input('Enter the number of participants in your tournament: ')

    # make empty records of specified length
    participant_records,saved = MF.makeslots(numparticipants)
    print(f'There are {numparticipants} participant slots ready for sign up.')

    # after participants are initialized we send the user to the main menu
    place = 0
    print(len(participant_records))

    # while loop that keeps program running until exit 
    while place != None:
        if place == 0:
            place = MF.MainMenu(place)
        
        elif place == 1:
            place,participant_records,saved = MF.SignUp(participant_records)
        
        elif place == 2:
            place,participant_records,saved = MF.CancelSignUp(participant_records)
        
        elif place == 3:
            place = MF.ViewParticipants(participant_records)
        
        elif place == 4:
            place,saved = MF.SaveChanges(participant_records)
        
        elif place == 5:
            place = MF.Exit(saved)
        
        else:
            place = 0
        
    
    
