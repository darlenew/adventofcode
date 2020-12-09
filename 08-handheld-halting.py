#!/usr/bin/env python

def get_data(path):
    with open(path, 'r') as fd:
        data = [line.strip() for line in fd]
    
    return data

def find_infinite_loop(instructions):
    ic = 0
    accumulator = 0
    seen = set()

    while True:
        if ic in seen:
            return accumulator

        seen.add(ic)
        op, arg = instructions[ic].split(' ')
        if op == 'nop':
            ic += 1
        elif op == 'acc':
            accumulator += int(arg)
            ic += 1
        elif op == 'jmp':
            ic += int(arg)

instructions = get_data('08-handheld-halting.txt')
accumulator = find_infinite_loop(instructions)
print(accumulator)