# %% import common packages

import numpy as np
import re


class Day2():

    def __init__(self,input_list):
        
        self.input_list = input_list
        self.solution = 0
        return
    
    
    def loop_input(self):
        for i in self.input_list:
            self.calc_range(i)
        
        return
    
    def calc_range(self,id_range):
        splits = id_range.split("-")
        
        start_id = int(splits[0])
        end_id = int(splits[-1])
        for id in range(start_id,end_id+1):
            print(id)
            self.solution += self.calc_invalid(id)      
        
        return
    
    def calc_invalid(self,id):
        str_id = str(id)
        
        if len(str_id) % 2 != 0:
            return 0
        else:
            
            return id



# %% part 1 input read-in
import csv
input = []
with open('input_day2.txt', mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        for r in row:
            if r == "":
                continue
            else:
                input.append(r)

# print(input)

d = Day2(input)
d.loop_input()