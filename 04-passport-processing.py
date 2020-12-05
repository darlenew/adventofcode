#!/usr/bin/env python
REQUIRED = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
}

def process(path):
    valid = 0
    fields = set()

    with open(path, 'r') as fd:
        for line in fd:
            line = line.strip()
            if not line:
                # we're in between passports, so see if the fields for the 
                # last passport were valid and clear all the fields for the next
                # passport
                fields.discard('cid') # ignore cid
                if len(fields) == 7:
                    valid += 1
                fields.clear()
            else:
                # add the keys on this line to the fields
                fields |= set([kv.split(':')[0] for kv in line.split()])
    # process the final passport
    fields.discard('cid')
    if len(fields) == 7:
        valid += 1
    
    return valid

valid = process('04-passport-processing.txt')
print(valid)