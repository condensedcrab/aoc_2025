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
        new_pos_unmod = (old_pos + sign_polarity*turn_amt)
        change = abs(new_pos_unmod // 100)
        
        
        if change == 0 and new_pos == 0:
            print("Small turn, adding +1")
            change += 1
        
        self.dial_zero_cross += change
        
        
        print(f"Input: {input}. {old_pos} --> {self.dial_pos}. Change: {change}, total zero-crossings: {self.dial_zero_cross}")

        return new_pos
    

    def rotate_circle2(self,input):
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
            
        for i in range(turn_amt):
            self.dial_pos += sign_polarity
            self.dial_pos = self.dial_pos % 100
            if self.dial_pos == 0:
                self.dial_zero_cross += 1

        return
        
    
    def loop_input(self):
        for i in self.prompt:
            print(f"Prompt: {i}, Total Zero Crossings: {self.dial_zero_cross}")
            self.rotate_circle2(i)

        return
# %% day 1 - read in input and run through class 

with open('input_day1.txt', 'r') as f:
    lines = f.readlines() # Reads all lines into a list, including newline characters
    # To remove newline characters:
    lines = [line.strip() for line in lines]
    

d = Dial(lines)

d.loop_input()

# %% day 1 - part 2 testing
with open('ex_day1', 'r') as f:
    lines = f.readlines() # Reads all lines into a list, including newline characters
    # To remove newline characters:
    lines = [line.strip() for line in lines]
    

d = Dial(lines)

d.loop_input()