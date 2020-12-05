#!/usr/bin/env python
def get_password_db(path):
    with open(path, 'r') as fd:
       	data = fd.read()

    return data

def validate_passwords(db):
    valid_count = 0

    for line in db.strip().split('\n'):
        policy, password = line.split(':')
        _range, c = policy.split(' ')
        _min, _max = [int(x) for x in _range.split('-')]
        if password.count(c) in range(_min, _max + 1):
            valid_count += 1

    return valid_count
	
	
db = get_password_db('02-password-philosophy.txt')
count = validate_passwords(db)
print(count)
