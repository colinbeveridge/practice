import numpy as np
import math
import csv
import tournament-tracker-menu-functions as MenuFuncs

''' Tournament Tracker App. App that creates tournament entries and allows user to enter names of participants.'''
# this is the opening page of the app, where we enter the number of participants
'''

print('Welcome to Tournament Creator')
print('=============================')
numparticipants = ''
# while this entry is not a digit
while not numparticipants.isdigit():
    print('Number of participants must be an integer.')
    numparticipants = input('Enter the number of participants in your tournament: ')

participant_records = makeslots(numparticipants)
print(f'There are {numparticipants} participant slots ready for sign up.')
# after participants are initialized we send the user to the main menu
place = 0
saved = False
'''



if __name__ == '__main__':
    participant_records = makeslots(15)
    print(participant_records)
    place,participant_records,saved = SignUp(participant_records)
    place,participant_records,saved = SignUp(participant_records)
    place,participant_records,saved = SignUp(participant_records)
    place,participant_records,saved = SignUp(participant_records)
    print(participant_records)
    place,saved = SaveChanges(participant_records)
    
    
    
