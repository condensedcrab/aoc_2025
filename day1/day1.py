# %% set up class 
import re
import numpy as np

class Dial:
    
    def __init__(self, prompt):
        self.dial_pos = 50 # range is 0-99
        self.dial_zero_count = 0
        self.dial_zero_cross = 0
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
        old_pos = self.dial_pos
        new_pos = (self.dial_pos + sign_polarity*turn_amt) % 100
        self.dial_pos = new_pos
        
        # part 1 password
        if self.dial_pos == 0:
            self.dial_zero_count += 1
            
        # part 2 password
        
        new_pos_unmod = (self.dial_pos + sign_polarity*turn_amt)
        change = abs(new_pos_unmod // 100)
        divisor = change
        
        print(f"During operation, {divisor} zero crossings found")
        self.dial_zero_cross += divisor
        print(self.dial_zero_cross)
        
        if self.dial_pos == 0:
            self.dial_zero_cross += 1
        
        print(f"Old pos: {old_pos}, Command Change is: {input}")
        print(f"    ---> New pos: {self.dial_pos}, Dial Zero Count: {self.dial_zero_count}")

        return new_pos
    
    
    def loop_input(self):
        for i in self.prompt:
            self.rotate_circle(i)

        return
# %% day 1 - read in input and run through class 

with open('input_day1.txt', 'r') as f:
    lines = f.readlines() # Reads all lines into a list, including newline characters
    # To remove newline characters:
    lines = [line.strip() for line in lines]
    

d = Dial(lines)

d.loop_input()

# %% day 1 - part 2 testing
