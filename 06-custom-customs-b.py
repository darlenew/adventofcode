#!/usr/bin/env python

def get_groups(path):
    with open(path, 'r') as fd:
        groups = fd.read().split('\n\n')

    return groups

def yes_count(group):
    return len(set.intersection(*[set(person) for person in group.split('\n')]))

groups = get_groups('06-custom-customs.txt')
print(sum([yes_count(group) for group in groups]))

