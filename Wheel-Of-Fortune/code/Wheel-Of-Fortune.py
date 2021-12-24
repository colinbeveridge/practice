import numpy as np
import WheelFuncs as WF
import PlayerInfo as PI
import GameplayFuncs as GF

def playWOF(numplayers,numstandardrounds):
    # takes a number of players and a number of standard rounds to play and plays wheel of fortune
    # generate the players
    players_info = PI.generate_players(numplayers)

    # define the board and answer
    board = GF.generate_board(GF.load_words())

    # initialize went first to none before first round played
    wentfirst = None

    for i in range(numstandardrounds):
        # play this many standard rounds
        players_info,max_round_index,max_total_index,wentfirst = GF.playStandardRound(players_info,board,wentfirst)
    
    # now that two standard rounds are played, play final round
    # figure out who is the overall winner
    winner = players_info[max_total_index]
    print(f'Player {winner+1}, you are the overall winner for the first two rounds! You will play in our final round.')