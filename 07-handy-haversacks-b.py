#!/usr/bin/env python
import re

def parse_data(path):
    bags = {} # maps bag style to list of two-tuples of the style and count of bags they contain

    child_re = re.compile(r'^ ([^ ])+ ([a-z0-9 ]+) bag.*$')

    with open(path, 'r') as fd:
        for line in fd:
            line = line.strip()
            parent, children = line.split("bags contain")
            parent = parent.strip()
            bags.setdefault(parent, []) 

            for child in children.split(','):
                if child == " no other bags.":
                    continue

                m = child_re.match(child)
                style = m.group(2)
                count = int(m.group(1))
                bags[parent].append((style, count))

    return bags

def count_contains(bags, style):
    """Returns the number of bags inside this bag style"""
    if not bags[style]:
        return 0

    return sum([t[1] + t[1] * count_contains(bags, t[0]) for t in bags[style]])


bags = parse_data('07-handy-haversacks.txt')
from pprint import pprint
pprint(bags)
num = count_contains(bags, "shiny gold")
print(num)




