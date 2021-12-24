# Function library dealing with the wheel for wheel of fortune game
# definitely want a random number generator here
import numpy as np

def spinWheel():
    # running this function prints what the wheel landed on and changes cash value to that number, returns cash
    num = np.random.randint(1,25)

    if num == 1 or num == 2:
        print('Bankrupt! Lose all round cash and end your turn.')
        cash = None
    
    elif num == 3:
        print('Lose a turn. Your turn is over.')
        cash = 0

    elif num == 4 or num == 5:
        print('$300')
        cash = 300

    elif num == 6:
        print('$350')
        cash = 350

    elif num == 7:
        print('$400')
        cash = 400

    elif num == 8:
        print('$450')
        cash = 450

    elif num == 9:
        print('$550')
        cash = 550

    elif num == 10:
        print('$600')
        cash = 600

    elif num == 11:
        print('$650')
        cash = 650

    elif num == 12 or num == 13:
        print('$700')
        cash = 700

    elif num == 14:
        print('$750')
        cash = 750

    elif num == 15 or num == 16:
        print('$800')
        cash = 800

    elif num == 17 or num == 18:
        print('$900')
        cash = 900

    elif num == 19:
        print('$5000')
        cash = 5000

    else:
        print('$500')
        cash = 500

    return cash

