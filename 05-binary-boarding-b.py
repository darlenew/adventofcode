#!/usr/bin/env python

def get_data(path):
    with open(path, 'r') as fd:
        return [line.strip() for line in fd]

def binary_partition(ticket_segment):
    value = 0

    segment = list(ticket_segment)
    segment.reverse()
    for i, c in enumerate(segment):
        if c in ('B', 'R'):
            value += pow(2, i)
    
    return value

def get_ticket_id(ticket):
    """Return Seat ID"""
    row = binary_partition(ticket[:7])
    col = binary_partition(ticket[7:])

    return row * 8 + col

def find_my_seat(ids):
    """Return the id such that id + 1 and id - 1 exists in the list of ids"""
    full = set(range(min(ids), max(ids) + 1))
    my_seat = full - set(ids)

    return my_seat.pop()

 
data = get_data('05-binary-boarding.txt')
ids = [get_ticket_id(ticket) for ticket in data]
print(max(ids))
my_seat = find_my_seat(ids)
print(my_seat)

# print(binary_partition('RLR'))
# print(binary_partition('FBFBBFF'))
# print(get_ticket_id('FBFBBFFRLR'))
# print(get_ticket_id('BFFFBBFRRR'))
# print(get_ticket_id('FFFBBBFRRR'))
# print(get_ticket_id('BBFFBBFRLL'))