#!/usr/bin/env python
import operator
from functools import reduce


def get_map(path):
    _map = []

    with open(path, 'r') as fd:
        for line in fd:
            _map.append(list(line.strip()))

    return _map

def traverse(_map, right, down):
    HEIGHT = len(_map)
    PAGE_WIDTH = len(_map[0])

    i = j = 0
    trees = 0
    while (i < HEIGHT):
        if _map[i][j % PAGE_WIDTH] == '#':
            trees += 1

        i += down 
        j += right 

    return trees

_map = get_map('03-toboggan-trajectory.txt')

# (right, down)
STEPS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = [traverse(_map, step[0], step[1]) for step in STEPS]

print(reduce(lambda x, y: x * y, trees))
