#!/usr/bin/env python

def get_map(path):
    _map = []

    with open(path, 'r') as fd:
        for line in fd:
            _map.append(list(line.strip()))

    return _map

def traverse(_map):
    HEIGHT = len(_map)
    PAGE_WIDTH = len(_map[0])

    i = j = 0
    trees = 0
    while (i < height):
        if _map[i][j % PAGE_WIDTH] == '#':
            trees += 1

        i += 1 
        j += 3

    return trees

_map = get_map('03-toboggan-trajectory.txt')
print(_map)
height = len(_map)
page_width = len(_map[0])
print(height, page_width)
trees = traverse(_map)
print(trees)
