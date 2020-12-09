#!/usr/bin/env python

def get_data(path):
    with open(path, 'r') as fd:
        data = [line.strip() for line in fd]
    
    return data

def find_infinite_loop(instructions):
    
    for (i, instruction) in enumerate(instructions):
        op, arg = instruction.split(' ')
        # try changing this instruction
        saved = instruction
        if op == 'nop':
            instructions[i] = 'jmp ' + arg
        elif op == 'jmp':
            instructions[i] = 'nop ' + arg
        else:
            continue

        ic = 0
        accumulator = 0
        processed = set()
    
        while True:
            if ic in processed:
                # infinite loop
                break

            processed.add(ic)
            try:
                op, arg = instructions[ic].split(' ')
            except IndexError:
                return accumulator
    
            if op == 'nop':
                ic += 1
            elif op == 'acc':
                accumulator += int(arg)
                ic += 1
            elif op == 'jmp':
                ic += int(arg)

        # restore
        instructions[i] = saved
    
instructions = get_data('08-handheld-halting.txt')
accumulator = find_infinite_loop(instructions)
print(accumulator)