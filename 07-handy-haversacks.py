#!/usr/bin/env python
import re

def parse_data(path):
    bags = {} # maps bag style to a list of tuples containing parents and their count

    child_re = re.compile(r'^ ([^ ])+ ([a-z0-9 ]+) bag.*$')

    with open(path, 'r') as fd:
        for line in fd:
            line = line.strip()
            parent, children = line.split("bags contain")
            parent = parent.strip()
            bags.setdefault(parent, set()) 

            for child in children.split(','):
                if child == " no other bags.":
                    continue

                m = child_re.match(child)
                style = m.group(2)
                bags.setdefault(style, set())
                bags[style].add(parent)
    
    return bags

def get_ancestors(bags, style):
    if not bags[style]:
        return set()

    parents = bags[style]
    return parents.union(*[get_ancestors(bags, s) for s in parents]) 


bags = parse_data('07-handy-haversacks.txt')
from pprint import pprint
pprint(bags)
num = len(get_ancestors(bags, "shiny gold"))
print(num)




