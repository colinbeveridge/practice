import numpy as np
import WheelFuncs as WF
import PlayerInfo as PI
import GameplayFuncs as GF
import WebscrapeAnswers as WA

def playWOF(numplayers,numstandardrounds):
    # takes a number of players and a number of standard rounds to play and plays wheel of fortune
    # generate the players
    players_info = PI.generate_players(numplayers)
    keystrings = ['player_ID','total_cash','round_cash']
    # import full board options dictionary
    print('Loading answer dictionary.')
    answers = WA.load_answers()

    

    # initialize went first to none before first round played
    wentfirst = None

    for i in range(numstandardrounds):
        # play this many standard rounds
        # define the board and answer for that round
        print(f'Begin Round {i+1}')
        board = GF.generate_board((WA.select_answer(answers).lower()))
        players_info,max_round_index,max_total_index,wentfirst = GF.playStandardRound(players_info,board,wentfirst)
    
    # console our two losers
    for count,player in enumerate(players_info):
        # if they arent max total cash, say good game and tell them winnings.
        if count != max_total_index:
            print(f'Great game player {count+1}. You will go home with ${player[keystrings[1]]}. Thanks for playing!')

    # now that two standard rounds are played, play final round
    # figure out who is the overall winner
    winner = players_info[max_total_index]
    prize = 10000
    
    print(f'Player {max_total_index+1}, you are the overall winner for the first two rounds! You will play in our final round.')
    print(f'You have already won {winner[keystrings[1]]}. If you win this final round, you will earn an additional cash prize of ${prize}!')
    print(f'In our final round, R S T L N and E have already been guessed. You are to select 3 consonants and 1 vowel to add to the puzzle.')
    print(f'Then, you will be asked to solve the puzzle.')
    print()
    print()
    board = GF.generate_board(WA.select_answer(answers).lower())
    win  = GF.playFinalRound(board)

    # final messages and updates for if win or lose
    if win:
        print(f'Congratulations! Player {max_total_index+1} you win ${prize}.')
        winner['total_cash'] += prize
    
    else:
        print('You lose. Better luck next time.')
        print(f'The correct answer was {board[2]}.')
        print('On the bright side, you still take home some money.')
    
    print(f'Your total winnings from today are ${winner[keystrings[1]]}. Thanks for playing!')

    return winner

if __name__ == '__main__':
    players = 3
    rounds = 2
    winner = playWOF(players,rounds)