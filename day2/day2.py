# %% import common packages

import numpy as np
import re


class Day2():

    def __init__(self,input_list):
        
        self.input_list = input_list
        self.solution = 0
        return
    
    
    def loop_input(self):
        for i in input_list:
            self.calc_invalid(i)
        
        return
    
    def calc_invalid(self,id_range):
        splits = id_range.split("-")
        
        start_id = splits[0]
        end_id = splits[1]
        
        
        return



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