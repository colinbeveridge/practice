import numpy as np
import math

''' Tournament Tracker App. App that creates tournament entries and allows user to enter names of participants.'''
# this is the opening page of the app, where we enter the number of participants
print('Welcome to Tournament Creator')
print('=============================')
numparticipants = ''
# while this entry is not a digit
while not numparticipants.isdigit():
    print('Number of participants must be an integer.')
    numparticipants = input('Enter the number of participants in your tournament: ')

print(f'There are {numparticipants} participant slots ready for sign up.')

