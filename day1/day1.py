# %% set up class 

import numpy 

class Dial:
    
    def __init__(self):
        self.dial_pos = 50 # range is 0-99
        self.dial_zero_count = 0
        
        return
    
    def rotate_circle(self, input):
        sign_pos = True
        
        # parse the polarity of the input
        if "R" in input:
            sign_pos = True     # R is CW, towards higher
        elif "L" in input:
            sign_pos = False    # L is CCW, towards lower
    
        # now determine what the new position is and update 0 crossing if needed
        
    
        return
# %%
