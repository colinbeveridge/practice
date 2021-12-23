# Function library dealing with the wheel for wheel of fortune game
# definitely want a random number generator here
import numpy as np

def spinWheel():
    # running this function returns a value the wheel landed on
    num = np.random.randint(1,25)

    if num == 1 or num == 2:
        
