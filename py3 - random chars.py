#!/usr/bin/python
import urllib2
import string
charFreq = {}
letters = "aeilquty"

with open('py3.txt', 'r') as f:
    read_data = f.read()

for b in read_data:
    if b in letters:
        print b

uniques = set(read_data)

for unique in uniques:
    charCount = read_data.count(unique)
    charFreq[unique] = charCount

print charFreq
print string.ascii_lowercase
