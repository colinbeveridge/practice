# functions that generate, track and update player information

def find_max_index(players_info,key):
    # given player info dictionaries and the index of the field we want to find max of, returns index of player with max that value
    cashlist = []
    for player in players_info:
        cashlist.append(player[key])

    max_value = max(cashlist)
    max_index = cashlist.index(max_value)

    return max_index

def generate_players(numplayers):
    # takes number of players and returns that many dictionaries with info on each player
    players_info = []
    for i in range(numplayers):
        # separate round cash and total cash, round cash changes within round, at end of round, if win, round_cash goes to total cash
        # if lose, round_cash to 0
        playerID = i+1
        player = {'player_ID':playerID,'total_cash':0,'round_cash':0}
        players_info.append(player)

    return players_info
    
def update_player_roundcash(players_info,player_index,cash):
    # takes players information dictionary and playerID and updates that players round cash with specified value
    # always adding the cash value, so enter negative number to subract
    # if we get a bankrupt, make cash = None on the input, so if cash = None, reset round_cash to 0
    player = players_info[player_index]
    if cash == None:
        player['round_cash'] = 0
    else:
        player['round_cash'] += cash
        print(player['round_cash'])
    
    return players_info

def update_player_allcash(players_info):
    # takes players information dictionary and playerID and updates that players total cash. only occurs at end of round.
    # returns a round winner index in case we need to go to round 3
    # first find max index for round cash, key for round cash in dictionary is 2
    max_round_index = find_max_index(players_info,'round_cash')

    # now the player with max cash sends their round cash to their total cash
    maxplayerdict = players_info[max_round_index]

    # add round cash to total for winner
    maxplayerdict['total_cash'] += maxplayerdict['round_cash']

    # reset round cash to 0 for all players
    for players in players_info:
        players['round_cash'] = 0
    
    # now find max index for total cash and return at end of function
    max_total_index = find_max_index(players_info,'total_cash')

    # returns list of player info and the index of the highest cash player, aka the index of the winner of that round
    return players_info, max_round_index, max_total_index