# functions that generate, track and update player information

def generate_players(numplayers):
    # takes number of players and returns that many dictionaries with info on each player
    players_info = []
    for i in range(numplayers):
        # separate round cash and total cash, round cash changes within round, at end of round, if win, round_cash goes to total cash
        # if lose, round_cash to 0
        playerID = i+1
        player = {'player_ID':playerID,'total_cash':0,'round_cash:':0}
        players_info.append(player)
    
def update_player_roundcash(players_info,playerID,cash):
    # takes players information dictionary and playerID and updates that players round cash with specified value
    # always adding the cash value, so enter negative number to subract
    # if we get a bankrupt, make cash = None on the input, so if cash = None, reset round_cash to 0
    dict = players_info[playerID-1]
    if cash == None:
        dict[2] = 0
    else:
        dict[2] += cash

def update_player_allcash(players_info):
    # takes players information dictionary and playerID and updates that players total cash. only occurs at end of round.
    # returns a round winner index in case we need to go to round 3
    cashlist = []
    for playerdict in players_info:
        cashlist.append(playerdict[2])
    
    # now find max in list
    max_value = max(cashlist)

    max_index = cashlist.index(max_value)

    # now the player with max cash sends their round cash to their total cash
    maxplayerdict = players_info[max_index]
    # add round cash to total for winner
    maxplayerdict[1] += maxplayerdict[2]
    # reset round cash to 0 for all players
    for playerdict in players_info:
        playerdict[2] = 0
    
    # returns the index of the highest cash player, aka the index of the winner of that round
    return max_index