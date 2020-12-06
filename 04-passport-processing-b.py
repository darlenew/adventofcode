#!/usr/bin/env python
import re


def _is_four_digits(val):
    return bool(re.match(r'^\d\d\d\d$', str(val)))

def is_passport_valid(passport):
    """Return True if the passport is valid, otherwise False. 
    The passport is a dict of kv-pairs.
    """
    # ignore cid
    passport.pop('cid', None)

    # should have 7 fields remaining
    if len(passport.keys()) != 7:
        return False

    # byr
    val = int(passport['byr'])
    if not (_is_four_digits(val) and val >= 1920 and val <= 2002):
        return False

    # iyr
    val = int(passport['iyr'])
    if not (_is_four_digits(val) and val >= 2010 and val <= 2020):
        return False

    # eyr
    val = int(passport['eyr'])
    if not (_is_four_digits(val) and val >= 2020 and val <= 2030):
        return False

    # hgt
    m = re.match(r'^(\d+)(.*)$', passport['hgt'])
    if not m:
        return False
    num, units = m.groups()
    num = int(num)
    if units == 'cm':
        if not (num >= 150 and num <= 193):
            return False
    elif units == 'in':
        if not (num >= 59 and num <= 76):
            return False
    else:
        return False

    # hcl
    if not re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
        return False

    # ecl
    if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    # pid
    if not re.match(r'^\d{9}$', passport['pid']):
        return False

    return True

def process_passports(path):
    valid = 0
    passport = {}

    with open(path, 'r') as fd:
        for line in fd:
            line = line.strip()
            if not line:
                # we're in between passports, so see if the fields for the 
                # last passport were valid and clear all the fields for the next
                # passport
                valid += int(is_passport_valid(passport))
                passport.clear()
            else:
                # add this line's data to the passport
                passport.update({k: v for k, v in [field.split(':') for field in line.split()]})

    # process the final passport
    valid += int(is_passport_valid(passport))
    
    return valid

valid = process_passports('04-passport-processing.txt')
print(valid)