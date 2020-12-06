#!/usr/bin/env python
FILENAME = '01-report-repair.txt'

def report_repair(path):
    complement_map = {} # maps 2020 minus x to x

    with open(FILENAME, 'r') as fd:
        for line in fd:
            value = int(line.strip())
            if value in complement_map:
                return value, complement_map[value]

            complement = 2020 - value
            complement_map[complement] = value

value, complement = report_repair(FILENAME)
print(value, complement, value * complement)

            
