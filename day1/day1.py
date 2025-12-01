# %% set up class 
import re
import numpy as np

class Dial:
    
    def __init__(self, prompt):
        self.dial_pos = 50 # range is 0-99
        self.dial_zero_count = 0
        self.prompt = prompt
        
        return
    
    def rotate_circle(self, input):

        # parse input string and determine dial turn number
        pat = r'\d+'
        match = re.findall(pat,input)
        turn_amt = int(match[0])
        
        sign_polarity = 1
        # parse the polarity of the input
        if "R" in input:
            sign_polarity = 1    # R is CW, towards higher
        elif "L" in input:
            sign_polarity = -1    # L is CCW, towards lower
    
        # now determine what the new position is and update 0 crossing if needed
        new_pos = self.dial_pos + sign_polarity*input
        
    
        return new_pos
# %% day 1 - read in input and run through class 

with open('input_day1.txt', 'r') as f:
    lines = f.readlines() # Reads all lines into a list, including newline characters
    # To remove newline characters:
    lines = [line.strip() for line in lines]
    

d = Dial(lines)
