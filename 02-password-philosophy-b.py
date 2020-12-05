#!/usr/bin/env python
def get_password_db(path):
    with open(path, 'r') as fd:
       	data = fd.read()

    return data

def is_valid(policy, password):
    """Returns True if the password is valid, otherwise False"""
    positions, c = policy.split(' ')
    i, j = [int(position) - 1 for position in positions.split('-')]
    verdict = bool(password[i] == c) ^ bool(password[j] == c)

    return verdict


def validate_passwords(db):
    valid_count = 0

    for line in db.strip().split('\n'):
        policy, password = line.split(':')
        password = password.strip()
        print(policy, password)
        if is_valid(policy, password):
            print("valid")
            valid_count += 1
        else:
            print("invalid")

    return valid_count
	
	
db = get_password_db('02-password-philosophy.txt')
count = validate_passwords(db)
print(count)
# print(is_valid('1-3 a', 'abcde'))
# print(is_valid('1-3 b', 'cdefg'))
# print(is_valid('2-9 c', 'ccccccccc'))
# print(is_valid('1-3 m', 'vmnh'))