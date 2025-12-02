# %% import common packages

import numpy as np
import re


class Day2():

    def __init__(self):
        
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

print(input)