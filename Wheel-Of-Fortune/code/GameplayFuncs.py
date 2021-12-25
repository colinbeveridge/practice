# these functions can be stitched together in final interface to facilitate gameplay
import numpy as np
import WheelFuncs as WF
import PlayerInfo as PI

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())

    return valid_words

def generate_board(wordlist):
    # takes one of the words in the large word list and makes it the solution to the puzzle
    # board is a list, first entry is empty board to be guessed on, second is full board for comparing, third is the answer in a string for full compare
    selectword = np.random.randint(1,len(wordlist)+1)
    word = wordlist[selectword]
    answer = list(word)
    board = [['-']*len(word),answer,word]
    
    
    return board

def ask_vowel():
    # user can decide if they want to buy a vowel
    want_vowel = None
    while want_vowel != 'y' and want_vowel != 'n':
        want_vowel = input('Would you like to buy a vowel? [y/n] ')
    
    # convert to boolean
    if want_vowel == 'y':
        want_vowel = True
    else:
        want_vowel = False

    return want_vowel

def ask_solve():
    # ask the user if they would like to solve the puzzle
    want_solve = None
    while want_solve != 'y' and want_solve != 'n':
        # get input from user
        want_solve = input('Would you like to solve the puzzle? [y/n] ')
    
    # convert to boolean
    if want_solve == 'y':
        want_solve = True
    else:
        want_solve = False
    
    return want_solve

def get_proper_guess(priorguesses,want_vowel=False):
    # function that defines the sets of letters that a proper guess can be in and only allows advancement if in the correct set
    # for the full guess, the logic in the turn function skips this, so it does not account for a full word
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    vowels = {'a','e','i','o','u'}
    consonants = alphabet - vowels

    #boolean for when the guess given matches the desired type
    guessinset = False

    # boolean for when the guess is already in the puzzle (has already been guessed)
    alreadyguessed = True
    # initialize guess for logic
    
    while guessinset == False or alreadyguessed == True:
        # initailize boolean to reask if something tripped (if it was in the set but was already guessed, we have to check new guess is in set first)
        guessinset = False
        # reset guess
        guess = None
        if want_vowel == False:
            while guess not in consonants:
                # if we want a consonant and then we have to keep taking inputs until we get a consonant
                guess = input('Enter a lowercase consonant: ')
                
        else:
            while guess not in vowels:
                # if want a vowel, keep getting input til we get a vowel
                guess = input('Enter a lowercase vowel: ')
        # now we have gotten a guess in the desired set, flip first variable
        guessinset = True

        # now check if already guessed
        if guess in priorguesses:
            print('That letter has already been guessed. Try again.')
        
        else:
            alreadyguessed = False

    # once guess is proper, add it to priorguesses so it cannot be guessed again
    priorguesses.append(guess)

    return guess,priorguesses

def apply_guess(guess,board):
    # since this guess logic will repeated, we put it in a function
    # count how many times guess appears in word
    # full word
    word = board[2]
    # full word in list form
    wordlist = board[1]
    # whatever is guess so far in the puzzle
    puzzlestatus = board[0]
    # first check if already guessed
    locations = [i for i in range(len(word)) if word.startswith(guess, i)]
    # number of time guess appears
    appearances = len(locations)
    # for now the turn will not end, only if does not appear in puzzle
    turnend = False

    if appearances == 0:
        # if letter doesnt appear, alert user and end player turn
        print(guess + ' is not in the puzzle. Your turn is over.')
        turnend = True
                
    else:
        print(guess + ' is in the puzzle. Your turn continues.')
        for i in range(len(guess)):
            for index in locations:
                # add whatever letter we are looking at to the starting index, this case only matters when full word is being guessed
                index += i
                # if there is at least one appearance, apply the correct letters
                puzzlestatus[index] = wordlist[index]
        print(puzzlestatus)

    return appearances,board,turnend

def check_solved(board):
    # function that takes the board and sees if the puzzle has been solved yet
    issolved = board[0] == board[1]
    return issolved

def playStandardTurn(players_info,turn,board,priorguesses):
    # this defines one players turn. turn picks the player from player info
    print(f'Player {turn+1}\'s turn.')
    show_board(board)
    # boolean variable for if turn ends
    # boolean variable for if round ends
    turnend = False
    roundend = False

    # guess counter so we know to ask them if they want to buy a vowel
    guesscounter = 0

    # if cash is not 0 or None, then we have to guess
    while not turnend:
        # on each iteration the user should have an opportunity to say they want to solve the puzzle
        want_solve = ask_solve()

        # this code block handles if player wants to guess the puzzle
        if want_solve:
            guess = input('What do you think the word is? ')
            guess = guess.lower()
            iscorrect = guess == board[2]

            if iscorrect:
                # here we apply the correct guess to the board
                appearances,board,turnend = apply_guess(guess,board)
                # print congrats
                print('Congratulations! You have guessed the word correctly. The round is over.')
                # if guessed correctly, we end the round as well
                roundend = True
            print(board[0])
            # regardless of correct or not, turn will end when person attempts solve     
            turnend = True
            break
        
        # to start turn we spin if user didn't try to guess
        cash = WF.spinWheel()
        # if we get bankrupt or lose a turn we end the turn
        if cash == None or cash == 0:
            turnend = True
            # bankrupt them if bankrupt, just skip turn if skip turn
            players_info = PI.update_player_roundcash(players_info,turn,cash)
        
        else:
            if guesscounter == 0:
            # if they have not had their first guess yet, must be consonant
                # now they have to guess a consonant that hasn't already been guessed
                guess,priorguesses = get_proper_guess(priorguesses,want_vowel=False)
                # now that we have guess, check if guess is in the correct answer
                appearances,board,turnend = apply_guess(guess,board)
                # give them the amount of money they have earned, appearances times the cash they spun for, if not present, they will get 0 cash
                cash *= appearances
                # this line gets the locations of each appearance of the guess in the word
                players_info = PI.update_player_roundcash(players_info,turn,cash)
                guesscounter += 1
            
            else:
            # now if guesscounter is above 0 and we run through loop again, it means they have already guessed their first consonant
            # allow them to buy a vowel
            
                want_vowel = ask_vowel()

                if want_vowel:
                    # the user has specified they want to buy a vowel
                    # now they have to guess a vowel that hasn't already been guessed
                    guess,priorguesses = get_proper_guess(priorguesses,want_vowel)
                    # now that we have guess, check if guess is in the correct answer
                    appearances,board,turnend = apply_guess(guess,board)
                    # cash should be minus 250 if we buy a vowel
                    cash = -250
                    # this line gets the locations of each appearance of the guess in the word
                    players_info = PI.update_player_roundcash(players_info,turn,cash)
                    # now check after full updates if we solved the puzzle on that guess
                    roundend = check_solved(board)

                else:
                    # user does not want vowel, is guessing consonant with cash value defined above after wheel spin
                    guess,priorguesses = get_proper_guess(priorguesses,want_vowel)
                    # now that we have guess, check if guess is in the correct answer
                    appearances,board,turnend = apply_guess(guess,board)
                    # cash should be minus 250 if we buy a vowel
                    cash *= appearances
                    # this line gets the locations of each appearance of the guess in the word
                    players_info = PI.update_player_roundcash(players_info,turn,cash)
                    # check fully solved
                    roundend = check_solved(board)
        
        # if the round ended in one of the loops, tell the loop so it can end the turn as well
        if roundend:
            turnend = True
    print(players_info)
    # return boolean for if the round ended
    return roundend

def playStandardRound(players_info,board,wentfirst=None):
    # defines the full playing of one round. takes list of player info dictionaries and the index of the player that went first in the first round
    # wentfirst=None if in first round. wentfirst= (who went first in first round) if in second round
    # returns wentfirst (who went first for past round)
    # for one round we also have to generate the board, so here is where we will call the function that generates the board

    # initialize empty list for priorguesses
    priorguesses = []
    # set variable for while loop ending round
    endround = False

    # get number of players
    numplayers = len(players_info)

    # randomly select player to go first
    counter = np.random.randint(1,numplayers+1)
    
    while counter == wentfirst:
        # if selected player already went first, pick new random until someone who didn't go first
        counter = np.random.randint(1,numplayers+1)

    # capture who ends up going first for this round
    wentfirst = counter

    while not endround:
        # defines which players turn it is for this while loop iteration, mod divide maps us back over the number of players infinitely
        turn = counter%numplayers
        # standard turn will return true if the round ended
        endround = playStandardTurn(players_info,turn,board,priorguesses)
        counter += 1

    # round ends, we update the player total cash information
    players_info,max_round_index,max_total_index = PI.update_player_allcash(players_info)

    # return who went first this round in case we call this again for another round
    return players_info, max_round_index, max_total_index, wentfirst

def show_board(board):
    # prints current board for the player to see progress
    print(board[0])

def playFinalRound(board):
    # function that runs the final round for the given player and board
    # make list out of given letters
    priorguesses = list('rstlne')

    # apply all given guesses
    for letter in priorguesses:
        appearances,board,turnend = apply_guess(letter,board)
    
    # show board
    print('Current board before your guesses: ')
    show_board()
    print('Guess 3 consonants.')

    # get consonants
    consonantslist = []
    for i in range(3):
        consonant,priorguesses = get_proper_guess(priorguesses,want_vowel=False)
        consonantslist.append(consonant)

    # get vowel
    vowel,priorguesses = get_proper_guess(priorguesses,want_vowel=True)
    
    # merge lists
    finalguesslist = consonantslist.append(vowel)

    # apply final guesses
    for letter in finalguesslist:
        appearances,board,turnend = apply_guess(letter,board)

    # show boad again
    print('After all your guesses, here is the board. Time for your final guess.')
    show_board()

    # initialize final guess
    finalguess = ''

    # Keep prompting until user enters guess of correct length
    while len(finalguess) != len(board[2]):
        print('Make sure your final guess is the same length as the board.')
        finalguess = input('Final Guess: ')

    # standardize casing    
    finalguess = finalguess.lower()
    
    # check if correct
    iscorrect = finalguess == board[2]

    # can do congratulating in the game function
    return iscorrect
    
if __name__ == '__main__':
    guess = input('full guess: ')
    board = [['-','-','-','-','-','-'],['a','b','b','c','a','b'],'abbcab']
    appearances,board,turnend = apply_guess(guess,board)

    print(appearances)
    print(board)
    print(turnend)
