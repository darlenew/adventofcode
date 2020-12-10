#!/usr/bin/env python

"""
adapter: can take input 1, 2, or 3 jolts lower than rating and still produce rated output
adapters can only connect to a source 1-3 jolts lower than its rating

device: rated for 3 jolts higher than the highest-rated adapter in your bag
outlet: effective joltage rating of 0
"""

def get_data(path):
    with open(path, 'r') as fd:
        data = [int(line.strip()) for line in fd]

    return data

def find_chain(data):
    chain = sorted(data)
    diffs = [] # index x contains difference between chain[x] and chain[x+1]
    prev = 0
    for i in range(len(chain)):
        diffs.append(chain[i] - prev)
        prev = chain[i]
    diffs.append(3) # account for your device's built-in adapter

    print(chain)
    print(diffs)
    return diffs.count(1), diffs.count(3)

data = get_data('10-adapter-array.txt')

jolt_diff_1, jolt_diff_3 = find_chain(data)
print(jolt_diff_1, jolt_diff_3)
print(jolt_diff_1 * jolt_diff_3)