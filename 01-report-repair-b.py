#!/usr/bin/env python
from itertools import combinations

FILENAME = '01-report-repair.txt'

def report_repair(path):
    values = []
    complements = {}

    with open(FILENAME, 'r') as fd:
        for line in fd:
            value = int(line.strip())
            if value in complements:
                return value, complements[value].keys()[0]

            values.append(value)

            for combo in combinations(values, 2): 
                x, y = combo
                z = 2020 - x - y
                complements.setdefault(z, {})
                complements[z][combo] = None


value, complements = report_repair(FILENAME)
complement_a, complement_b = complements
print(value, complement_a, complement_b)
print(value * complement_a * complement_b)
            

    


            
